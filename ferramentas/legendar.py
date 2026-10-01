#!/usr/bin/env python3
"""Transcreve a fala e gera legendas dinâmicas (palavra em destaque no tempo da fala).

Gera .srt (legenda simples) e .ass (legenda estilizada). Com --queimar, já entrega o vídeo legendado.

Uso:
  pip install faster-whisper
  python3 ferramentas/legendar.py video.mp4 --queimar
  python3 ferramentas/legendar.py video.mp4 --queimar --destaque "HN,vendas,resultado" --cor "#7C3AED" --maiusculas
"""
import argparse
import json
import os
import subprocess


def tamanho_video(arquivo):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
         "-of", "json", arquivo],
        capture_output=True, text=True, check=True,
    ).stdout
    s = json.loads(out)["streams"][0]
    return s["width"], s["height"]


def transcrever(arquivo, modelo):
    from faster_whisper import WhisperModel

    m = WhisperModel(modelo, device="cpu", compute_type="int8")
    segs, _ = m.transcribe(arquivo, language="pt", word_timestamps=True, vad_filter=True)
    return [(w.start, w.end, w.word.strip()) for s in segs for w in s.words if w.word.strip()]


def agrupar(palavras, max_palavras, max_letras):
    blocos, atual = [], []
    for i, p in enumerate(palavras):
        atual.append(p)
        texto = " ".join(x[2] for x in atual)
        prox = palavras[i + 1] if i + 1 < len(palavras) else None
        fecha = (
            len(atual) >= max_palavras
            or len(texto) >= max_letras
            or p[2][-1:] in ".!?,;:"
            or (prox and prox[0] - p[1] > 0.35)
        )
        if fecha:
            blocos.append(atual)
            atual = []
    if atual:
        blocos.append(atual)
    return blocos


def t_srt(t):
    h, r = divmod(t, 3600)
    m, s = divmod(r, 60)
    return f"{int(h):02}:{int(m):02}:{s:06.3f}".replace(".", ",")


def t_ass(t):
    h, r = divmod(t, 3600)
    m, s = divmod(r, 60)
    return f"{int(h)}:{int(m):02}:{s:05.2f}"


def cor_ass(hexcor):
    h = hexcor.lstrip("#")
    return f"&H00{h[4:6]}{h[2:4]}{h[0:2]}".upper()


def limpar(palavra):
    return palavra.strip(".,!?;:\"'()").lower()


def escrever(blocos, base, largura, altura, a):
    destaques = {d.strip().lower() for d in a.destaque.split(",") if d.strip()}
    cor = cor_ass(a.cor)
    fmt = (lambda s: s.upper()) if a.maiusculas else (lambda s: s)

    with open(base + ".srt", "w", encoding="utf-8") as f:
        for i, b in enumerate(blocos, 1):
            f.write(f"{i}\n{t_srt(b[0][0])} --> {t_srt(b[-1][1])}\n{' '.join(x[2] for x in b)}\n\n")

    tam = round(altura * (0.045 if altura > largura else 0.06))
    margem = round(altura * (0.22 if altura > largura else 0.08))
    cab = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {largura}
PlayResY: {altura}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Legenda,{a.fonte},{tam},&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,{max(2, tam // 12)},{max(1, tam // 20)},2,60,60,{margem},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    linhas = []
    for b in blocos:
        for k, (ini, fim, _) in enumerate(b):
            fim_evento = b[k + 1][0] if k + 1 < len(b) else fim
            partes = []
            for j, (_, _, w) in enumerate(b):
                if j == k:
                    partes.append(f"{{\\c{cor}\\fscx112\\fscy112}}{fmt(w)}{{\\r}}")
                elif limpar(w) in destaques:
                    partes.append(f"{{\\c{cor}}}{fmt(w)}{{\\r}}")
                else:
                    partes.append(fmt(w))
            linhas.append(f"Dialogue: 0,{t_ass(ini)},{t_ass(fim_evento)},Legenda,,0,0,0,,{' '.join(partes)}")
    with open(base + ".ass", "w", encoding="utf-8") as f:
        f.write(cab + "\n".join(linhas) + "\n")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("video")
    p.add_argument("--modelo", default="small", help="tiny, base, small, medium, large-v3 (maior = mais preciso e mais lento)")
    p.add_argument("--max-palavras", type=int, default=3)
    p.add_argument("--max-letras", type=int, default=22)
    p.add_argument("--fonte", default="Montserrat ExtraBold")
    p.add_argument("--cor", default="#A855F7", help="cor da palavra falada e dos destaques")
    p.add_argument("--destaque", default="", help="palavras-chave sempre coloridas, separadas por vírgula")
    p.add_argument("--maiusculas", action="store_true")
    p.add_argument("--queimar", action="store_true", help="gera também o vídeo com a legenda aplicada")
    a = p.parse_args()

    base = os.path.splitext(a.video)[0]
    largura, altura = tamanho_video(a.video)
    palavras = transcrever(a.video, a.modelo)
    blocos = agrupar(palavras, a.max_palavras, a.max_letras)
    escrever(blocos, base, largura, altura, a)
    with open(base + ".transcricao.txt", "w", encoding="utf-8") as f:
        f.write(" ".join(w for _, _, w in palavras) + "\n")
    print(f"{len(palavras)} palavras · {len(blocos)} blocos -> {base}.srt / {base}.ass / {base}.transcricao.txt")

    if a.queimar:
        saida = base + "-legendado.mp4"
        ass = (base + ".ass").replace("\\", "/").replace(":", "\\:").replace("'", "\\'")
        subprocess.run(
            ["ffmpeg", "-hide_banner", "-y", "-i", a.video, "-vf", f"ass='{ass}'",
             "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-c:a", "copy",
             "-movflags", "+faststart", saida],
            check=True,
        )
        print(f"Vídeo legendado: {saida}")


if __name__ == "__main__":
    main()

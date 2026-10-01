#!/usr/bin/env python3
"""Remove as pausas de uma gravação usando o silencedetect do ffmpeg.

Uso:
  python3 ferramentas/cortar_silencios.py entrada.mp4 saida.mp4
  python3 ferramentas/cortar_silencios.py entrada.mp4 saida.mp4 --limiar -32 --pausa 0.45 --respiro 0.12
"""
import argparse
import re
import subprocess
import sys


def duracao(arquivo):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", arquivo],
        capture_output=True, text=True, check=True,
    ).stdout
    return float(out.strip())


def detectar_silencios(arquivo, limiar_db, pausa_min):
    log = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", arquivo, "-af",
         f"silencedetect=noise={limiar_db}dB:d={pausa_min}", "-f", "null", "-"],
        capture_output=True, text=True,
    ).stderr
    inicios = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", log)]
    fins = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
    return list(zip(inicios, fins + [None] * (len(inicios) - len(fins))))


def trechos_com_fala(silencios, total, respiro):
    trechos, cursor = [], 0.0
    for ini, fim in silencios:
        fim = total if fim is None else fim
        corte_ini = max(cursor, ini + respiro)
        if corte_ini > cursor:
            trechos.append((cursor, corte_ini))
        cursor = max(cursor, fim - respiro)
    if cursor < total:
        trechos.append((cursor, total))
    return [(a, b) for a, b in trechos if b - a > 0.08]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("entrada")
    p.add_argument("saida")
    p.add_argument("--limiar", type=float, default=-32, help="volume (dB) abaixo do qual conta como silêncio")
    p.add_argument("--pausa", type=float, default=0.45, help="duração mínima (s) de uma pausa para ser cortada")
    p.add_argument("--respiro", type=float, default=0.12, help="folga (s) mantida antes e depois de cada fala")
    a = p.parse_args()

    total = duracao(a.entrada)
    trechos = trechos_com_fala(detectar_silencios(a.entrada, a.limiar, a.pausa), total, a.respiro)
    if not trechos:
        sys.exit("Nenhuma fala encontrada. Tente um --limiar mais baixo (ex.: -40).")

    expr = "+".join(f"between(t,{x:.3f},{y:.3f})" for x, y in trechos)
    filtro = (
        f"[0:v]select='{expr}',setpts=N/FRAME_RATE/TB[v];"
        f"[0:a]aselect='{expr}',asetpts=N/SR/TB[a]"
    )
    subprocess.run(
        ["ffmpeg", "-hide_banner", "-y", "-i", a.entrada, "-filter_complex", filtro,
         "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", a.saida],
        check=True,
    )
    final = sum(y - x for x, y in trechos)
    print(f"{len(trechos)} trechos mantidos · {total:.1f}s -> {final:.1f}s ({total - final:.1f}s de pausas removidas)")


if __name__ == "__main__":
    main()

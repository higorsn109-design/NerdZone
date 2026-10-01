# Ferramentas

Scripts que fazem o trabalho pesado no seu computador, sem gastar IA. Você pode
rodar direto ou pedir para o Codex/Claude Code rodar por você.

## Instalar
Requer **ffmpeg** e **Python 3**. Depois:
```
pip install faster-whisper markdown
```

## Cortar pausas
```
python3 ferramentas/cortar_silencios.py 01-bruto/take-01.mp4 05-amostras/sem-pausas.mp4
```
| Opção | Padrão | Quando mudar |
|---|---|---|
| `--limiar` | `-32` | Abaixe para `-40` se estiver cortando falas baixas |
| `--pausa` | `0.45` | Duração mínima (s) de uma pausa para ser cortada |
| `--respiro` | `0.12` | Aumente se o corte ficar seco no início/fim das palavras |

## Legenda dinâmica
```
python3 ferramentas/legendar.py 05-amostras/sem-pausas.mp4 --queimar --maiusculas --cor "#7C3AED" --destaque "HN,vendas"
```
Gera `.srt`, `.ass`, a transcrição em texto e, com `--queimar`, o vídeo legendado.
Na primeira vez, baixa o modelo de transcrição (precisa de internet).

## Atualizar este site
Editou algum `.md`? Gere o site de novo:
```
python3 ferramentas/gerar_site.py
```

# HN · Máquina de Edição com IA

Central de edição de vídeos com IA da **HN Gestão Comercial e Marketing**: você dá o
comando em português, e o Codex ou o Claude Code edita.

## Comece por aqui
1. Leia o curso: [`curso/MANUAL-EDICAO-COM-IA-HN.md`](curso/MANUAL-EDICAO-COM-IA-HN.md)
2. Prepare o computador (Aula 01).
3. Crie a pasta do primeiro vídeo com o [modelo de pastas](modelos/estrutura-de-pastas.md).

## O que tem aqui
| Pasta | Conteúdo |
|---|---|
| `curso/` | Manual completo: 10 aulas + 2 bônus |
| `modelos/` | Guia de comandos, briefing, pasta modelo e ficha de revisão |
| `.claude/skills/` | 5 skills de edição (estilo, ritmo, legendas, movimento e composição) |
| `ferramentas/` | Scripts testados para cortar pausas e gerar legendas dinâmicas |
| `AGENTS.md` | Instruções que o Codex e o Claude Code seguem neste repositório |

## Primeira edição em 2 comandos
```bash
pip install faster-whisper   # requer ffmpeg e Python 3
python3 ferramentas/cortar_silencios.py take-01.mp4 sem-pausas.mp4
python3 ferramentas/legendar.py sem-pausas.mp4 --queimar --maiusculas --destaque "HN,vendas"
```

> Não suba gravações brutas nem vídeos finais para este repositório: eles são grandes.
> Guarde as pastas de vídeo fora dele ou num armazenamento próprio.

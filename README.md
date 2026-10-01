# HN · Edição com IA

Central de edição de vídeos com IA da **HN Gestão Comercial e Marketing**: você dá o
comando em português, e o Codex ou o Claude Code edita.

## Os cursos
| Arquivo | Curso |
|---|---|
| `CURSO.html` | **Edição com IA**: editar anúncios e conteúdos dando comandos em português |
| `CURSO-MESA-AGENTES.html` | **Mesa Operada por Agentes**: o método do AlgoMaker e a mesa comercial da HN |

## Abrir o curso no navegador
**Dois cliques no arquivo `.html` do curso.** Abre direto no navegador, sem instalar nada e sem internet.

Opcional, com servidor local para o curso de edição (precisa de Python):
- **Windows:** dois cliques em `abrir-curso.bat`
- **Mac:** dois cliques em `abrir-curso.command` (na primeira vez: botão direito → Abrir)
- **Linux:** `sh abrir-curso.command`

Nesse caso o curso abre em **http://localhost:8000**, só enquanto a janela do atalho estiver aberta.

## Comece por aqui
1. Faça o curso no navegador (ou leia [`curso/MANUAL-EDICAO-COM-IA-HN.md`](curso/MANUAL-EDICAO-COM-IA-HN.md)).
2. Prepare o computador (Aula 01).
3. Crie a pasta do primeiro vídeo com o [modelo de pastas](modelos/estrutura-de-pastas.md).

## O que tem aqui
| Pasta | Conteúdo |
|---|---|
| `site/` | O curso em página única para o navegador (gerado por `ferramentas/gerar_site.py`) |
| `curso/` | Manual completo: 10 aulas + 2 bônus |
| `modelos/` | Guia de comandos, briefing, pasta modelo e ficha de revisão |
| `.claude/skills/` | 5 skills de edição (estilo, ritmo, legendas, movimento e composição) |
| `ferramentas/` | Scripts testados para cortar pausas e gerar legendas dinâmicas |
| `algomaker/` | Curso da mesa operada por agentes: manual, mandato, painel de aderência, funil de campanhas e servidor MCP |
| `AGENTS.md` | Instruções que o Codex e o Claude Code seguem neste repositório |

## Primeira edição em 2 comandos
```bash
pip install faster-whisper   # requer ffmpeg e Python 3
python3 ferramentas/cortar_silencios.py take-01.mp4 sem-pausas.mp4
python3 ferramentas/legendar.py sem-pausas.mp4 --queimar --maiusculas --destaque "HN,vendas"
```

> Não suba gravações brutas nem vídeos finais para este repositório: eles são grandes.
> Guarde as pastas de vídeo fora dele ou num armazenamento próprio.

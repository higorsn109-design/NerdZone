---
name: edicao-legendas
description: Padrão de legendas da HN — tamanho, posição e destaque de palavras. Use ao legendar qualquer vídeo.
---

# Legendas — tamanho e destaque

Use `ferramentas/legendar.py` (transcreve com faster-whisper e gera legenda dinâmica).

## Padrão
```
python3 ferramentas/legendar.py <video> --queimar --maiusculas --cor "#7C3AED" --destaque "<palavras-chave do briefing>"
```
- **Maiúsculas**, Montserrat ExtraBold, branco com contorno preto.
- **Até 3 palavras por bloco** (máx. 22 letras). Quebre em pontuação e em pausas.
- **Palavra falada** em destaque na cor primária, levemente ampliada.
- **Palavras-chave** do briefing sempre na cor primária.

## Posição
- Vertical (9:16): um pouco abaixo do centro, acima da área de botões das redes (~22% da base).
- Quadrado/horizontal: terço inferior.
- Nunca cubra a boca, um card de motion ou o CTA. Se houver conflito, suba a legenda.

## Revisão obrigatória
- Leia o `.srt` antes de queimar: nomes próprios, marcas (HN, nomes de clientes) e números costumam sair errados na transcrição.
- Corrija no `.srt`/`.ass` e só então queime.

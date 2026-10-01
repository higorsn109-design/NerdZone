#!/bin/sh
cd "$(dirname "$0")" || exit 1
URL="http://localhost:8000"
if command -v open >/dev/null 2>&1; then ABRIR=open; else ABRIR=xdg-open; fi
if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3 não encontrado. Abrindo o curso direto do arquivo..."
  "$ABRIR" "site/index.html"
  exit 0
fi
echo "Curso HN rodando em $URL (Ctrl+C para parar)"
(sleep 2 && "$ABRIR" "$URL") >/dev/null 2>&1 &
python3 -m http.server 8000 --bind 127.0.0.1 --directory site

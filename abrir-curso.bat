@echo off
cd /d "%~dp0"
set PY=
where py >nul 2>nul && set PY=py
if not defined PY where python >nul 2>nul && set PY=python
if not defined PY (
  echo Python nao encontrado. Abrindo o curso direto do arquivo...
  start "" "%~dp0site\index.html"
  exit /b
)
echo Curso HN rodando em http://localhost:8000
echo Feche esta janela para parar.
start "" cmd /c "timeout /t 2 >nul & start http://localhost:8000"
%PY% -m http.server 8000 --bind 127.0.0.1 --directory site

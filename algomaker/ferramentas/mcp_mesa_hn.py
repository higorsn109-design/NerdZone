#!/usr/bin/env python3
"""Servidor MCP da mesa comercial da HN: expõe o funil e o diário como ferramentas para o agente.

Não existe ferramenta para gastar verba, publicar anúncio ou mandar mensagem: isso é decisão
humana, na tela de cada plataforma. A ausência é proposital.

Instalar e registrar no Claude Code (rode na raiz do repositório):
  pip install mcp
  claude mcp add mesa-hn -- python3 algomaker/ferramentas/mcp_mesa_hn.py
"""
import json
import sys
from datetime import datetime
from pathlib import Path

from mcp.server.fastmcp import FastMCP

sys.path.insert(0, str(Path(__file__).resolve().parent))
from funil_campanhas import avaliar, carregar  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
MANDATO = BASE / "modelos" / "mandato.json"
DIARIO = BASE / "diario-de-decisoes.md"

mcp = FastMCP("mesa-hn")


def _mandato():
    if not MANDATO.exists():
        return None
    return json.loads(MANDATO.read_text(encoding="utf-8"))


@mcp.tool()
def mandato_ler() -> dict:
    """Lê o mandato comercial (objetivo, verba, CPA máximo, horizonte e o que exige aprovação humana)."""
    m = _mandato()
    return m or {"erro": f"sem mandato em {MANDATO}. Preencha antes de qualquer análise."}


@mcp.tool()
def funil_avaliar(csv_campanhas: str) -> dict:
    """Passa as variantes de campanha pelos 4 portões (porteiro, fora da amostra, robustez, estresse de custo).

    csv_campanhas: caminho do CSV com variante,periodo(treino|selado),impressoes,cliques,conversoes,gasto.
    Usa o CPA máximo e a queda aceita do mandato. Sem mandato, recusa.
    """
    m = _mandato()
    if not m:
        return {"recusado": "sem mandato definido: o funil não roda sem objetivo, verba e CPA máximo."}
    caminho = Path(csv_campanhas)
    if not caminho.is_absolute():
        caminho = BASE.parent / caminho
    if not caminho.exists():
        return {"erro": f"arquivo não encontrado: {caminho}"}
    res = avaliar(carregar(caminho), m["cpa_max"], queda_max=m.get("queda_max_aceita", 0.30))
    aprovadas = [r["variante"] for r in res if r["status"] == "APROVADA"]
    return {
        "cpa_max": m["cpa_max"],
        "aprovadas": aprovadas,
        "resumo": f"{len(aprovadas)} de {len(res)} aprovadas",
        "variantes": res,
        "lembrete": "Aumentar verba ou publicar exige aprovação humana (mandato.aprovacao_humana_para).",
    }


@mcp.tool()
def diario_registrar(decisao: str, motivo: str, dados: str = "") -> str:
    """Registra uma decisão ou recomendação no diário, com o motivo e os números que a sustentam."""
    agora = datetime.now().strftime("%Y-%m-%d %H:%M")
    novo = not DIARIO.exists()
    with DIARIO.open("a", encoding="utf-8") as f:
        if novo:
            f.write("# Diário de decisões — mesa comercial HN\n\n")
        f.write(f"## {agora} — {decisao}\n- **Motivo:** {motivo}\n")
        if dados:
            f.write(f"- **Dados:** {dados}\n")
        f.write("\n")
    return f"registrado em {DIARIO.name}"


@mcp.tool()
def diario_ler(ultimas: int = 10) -> str:
    """Lê as últimas decisões registradas no diário."""
    if not DIARIO.exists():
        return "diário vazio"
    blocos = DIARIO.read_text(encoding="utf-8").split("\n## ")[1:]
    return "\n## ".join([""] + blocos[-ultimas:]).strip() or "diário vazio"


if __name__ == "__main__":
    mcp.run()

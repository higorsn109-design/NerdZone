#!/usr/bin/env python3
"""Funil cético de campanhas: reprova a variante que só funciona no período em que foi ajustada.

O CSV tem uma linha por variante e período:
  variante,periodo,impressoes,cliques,conversoes,gasto
  periodo = treino (onde a campanha foi ajustada) ou selado (período que ninguém usou para decidir)

Portões, nesta ordem (a variante para no primeiro que reprova):
  1. Porteiro       — amostra mínima de conversões nos dois períodos
  2. Fora da amostra — CPA no período selado dentro do teto e sem desabar em relação ao treino
  3. Robustez        — probabilidade (simulação Monte Carlo) de o CPA real ficar dentro do teto
  4. Estresse de custo — CPA selado com custo inflado continua dentro do teto

Uso:
  python3 algomaker/ferramentas/funil_campanhas.py algomaker/modelos/exemplo-campanhas.csv --cpa-max 80
"""
import argparse
import csv
import random
import sys
from collections import defaultdict


def carregar(caminho):
    dados = defaultdict(dict)
    with open(caminho, newline="", encoding="utf-8") as f:
        for linha in csv.DictReader(f):
            periodo = linha["periodo"].strip().lower()
            if periodo not in ("treino", "selado"):
                sys.exit(f"Período inválido '{linha['periodo']}' na variante {linha['variante']}: use treino ou selado.")
            dados[linha["variante"].strip()][periodo] = {
                "impressoes": int(linha["impressoes"]),
                "cliques": int(linha["cliques"]),
                "conversoes": int(linha["conversoes"]),
                "gasto": float(linha["gasto"]),
            }
    return dados


def cpa(p):
    return p["gasto"] / p["conversoes"] if p["conversoes"] else float("inf")


def prob_cpa_dentro(p, cpa_max, simulacoes, rng):
    """Sorteia a taxa de conversão real (Beta) e mede quantas vezes o CPA fica dentro do teto."""
    if p["cliques"] == 0:
        return 0.0
    custo_por_clique = p["gasto"] / p["cliques"]
    dentro = 0
    for _ in range(simulacoes):
        taxa = rng.betavariate(p["conversoes"] + 1, p["cliques"] - p["conversoes"] + 1)
        if custo_por_clique / taxa <= cpa_max:
            dentro += 1
    return dentro / simulacoes


def avaliar(dados, cpa_max, min_conversoes=30, queda_max=0.30, prob_min=0.80, estresse=1.25,
            simulacoes=4000, semente=7):
    rng = random.Random(semente)
    resultado = []
    for nome, periodos in dados.items():
        r = {"variante": nome, "status": "REPROVADA", "portao": "", "motivo": ""}
        resultado.append(r)
        if "treino" not in periodos or "selado" not in periodos:
            r.update(portao="porteiro", motivo="falta o período treino ou selado")
            continue
        t, s = periodos["treino"], periodos["selado"]
        r.update(cpa_treino=cpa(t), cpa_selado=cpa(s))

        if min(t["conversoes"], s["conversoes"]) < min_conversoes:
            r.update(portao="porteiro",
                     motivo=f"amostra pequena: {min(t['conversoes'], s['conversoes'])} conversões, mínimo {min_conversoes}")
            continue

        taxa_t = t["conversoes"] / t["cliques"]
        taxa_s = s["conversoes"] / s["cliques"]
        if cpa(s) > cpa_max:
            r.update(portao="fora da amostra", motivo=f"CPA selado R$ {cpa(s):.2f} acima do teto R$ {cpa_max:.2f}")
            continue
        if taxa_s < taxa_t * (1 - queda_max):
            r.update(portao="fora da amostra",
                     motivo=f"conversão caiu {100 * (1 - taxa_s / taxa_t):.0f}% no período selado (máx. {100 * queda_max:.0f}%)")
            continue

        prob = prob_cpa_dentro(s, cpa_max, simulacoes, rng)
        r["prob"] = prob
        if prob < prob_min:
            r.update(portao="robustez", motivo=f"só {100 * prob:.0f}% de chance de o CPA ficar no teto (mín. {100 * prob_min:.0f}%)")
            continue

        if cpa(s) * estresse > cpa_max:
            r.update(portao="estresse de custo",
                     motivo=f"com custo +{100 * (estresse - 1):.0f}% o CPA vira R$ {cpa(s) * estresse:.2f}")
            continue

        r.update(status="APROVADA", portao="—", motivo="passou nos 4 portões")
    return resultado


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("csv")
    p.add_argument("--cpa-max", type=float, required=True, help="teto de custo por conversão do mandato (R$)")
    p.add_argument("--min-conversoes", type=int, default=30)
    p.add_argument("--queda-max", type=float, default=0.30, help="queda máxima de conversão do treino para o selado")
    p.add_argument("--prob-min", type=float, default=0.80, help="chance mínima de o CPA real ficar dentro do teto")
    p.add_argument("--estresse", type=float, default=1.25, help="multiplicador de custo no teste de estresse")
    p.add_argument("--simulacoes", type=int, default=4000)
    a = p.parse_args()

    res = avaliar(carregar(a.csv), a.cpa_max, a.min_conversoes, a.queda_max, a.prob_min, a.estresse, a.simulacoes)
    print(f"{'variante':<24}{'CPA treino':>12}{'CPA selado':>12}{'P(teto)':>9}  status")
    for r in res:
        fmt = lambda v: "—" if v is None or v == float("inf") else f"{v:.2f}"
        prob = f"{100 * r['prob']:.0f}%" if "prob" in r else "—"
        print(f"{r['variante']:<24}{fmt(r.get('cpa_treino')):>12}{fmt(r.get('cpa_selado')):>12}{prob:>9}  "
              f"{r['status']}  [{r['portao']}] {r['motivo']}")
    aprovadas = sum(r["status"] == "APROVADA" for r in res)
    print(f"\n{aprovadas} de {len(res)} variantes aprovadas. Reprovar é o funil funcionando.")


if __name__ == "__main__":
    main()

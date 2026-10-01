# Ferramentas da mesa comercial

Requer **Python 3**. O funil não precisa de nenhuma biblioteca; o servidor MCP precisa do
pacote `mcp`.

## Funil de campanhas
Passa cada variante pelos 4 portões: porteiro, fora da amostra, robustez e estresse de custo.
```
python3 algomaker/ferramentas/funil_campanhas.py algomaker/modelos/exemplo-campanhas.csv --cpa-max 80
```
| Opção | Padrão | O que controla |
|---|---|---|
| `--cpa-max` | obrigatório | Teto de custo por conversão do mandato (R$) |
| `--min-conversoes` | `30` | Amostra mínima em cada período (porteiro) |
| `--queda-max` | `0.30` | Queda máxima de conversão do treino para o selado |
| `--prob-min` | `0.80` | Chance mínima de o CPA real ficar dentro do teto |
| `--estresse` | `1.25` | Multiplicador de custo no teste de estresse |

Formato do CSV (uma linha por variante e período):
```
variante,periodo,impressoes,cliques,conversoes,gasto
gancho-resultado-cliente,treino,52000,1610,71,3900.00
gancho-resultado-cliente,selado,25000,790,34,1880.00
```

## Servidor MCP da mesa
Expõe `mandato_ler`, `funil_avaliar`, `diario_registrar` e `diario_ler` para o Claude.
Não tem ferramenta para gastar verba, publicar ou mandar mensagem, e isso é proposital.
```
pip install mcp
claude mcp add mesa-hn -- python3 algomaker/ferramentas/mcp_mesa_hn.py
```
Reinicie o Claude Code e confira com `/mcp`.

## Atualizar este site
```
pip install markdown
python3 ferramentas/gerar_site.py
```

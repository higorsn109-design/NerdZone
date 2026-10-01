# Mandato comercial — guia de preenchimento

> Sem mandato, a mesa não analisa nada. É proposital: é o mandato que impede o agente (e a
> equipe) de "otimizar" na direção errada. Preencha com o cliente, antes do primeiro teste.

## A entrevista (5 perguntas)
1. **Objetivo:** o que conta como resultado? (reunião agendada, venda, cadastro, mensagem no WhatsApp)
2. **Verba:** quanto pode ser gasto por mês? E por teste, no máximo?
3. **Teto de custo:** quanto, no máximo, vale pagar por um resultado (CPA máximo)?
   *Dica: margem por venda × taxa de fechamento das reuniões = o máximo que se paga por reunião.*
4. **Horizonte:** em quanto tempo vamos avaliar? (mínimo de 1 mês para ter amostra)
5. **Aprovação humana:** quem aprova gastar, publicar e falar com clientes?

## Os campos (`mandato.json`)
| Campo | Exemplo | Para quê |
|---|---|---|
| `cliente` | HN Gestão Comercial e Marketing | Identificação |
| `objetivo` | gerar reuniões de diagnóstico | O que conta como conversão |
| `verba_mensal` | 15000 | Limite total do mês |
| `cpa_max` | 80 | Teto que o funil usa para aprovar/reprovar |
| `verba_max_por_teste` | 3000 | Quanto um teste pode consumir antes de ser avaliado |
| `queda_max_aceita` | 0.30 | Quanto a conversão pode cair do treino para o selado |
| `horizonte_meses` | 3 | Janela de avaliação |
| `canais` | Meta Ads, Google Ads | Onde se executa (custo e público mudam por canal) |
| `aprovacao_humana_para` | gastar, publicar, enviar mensagem, mudar oferta | O que o agente nunca faz |

## Regras
- **Escreva antes, não depois.** Mudar o teto depois de ver o resultado é decorar o resultado.
- **Um mandato por cliente.** Custo, margem e público mudam tudo.
- **Revise no fim do horizonte**, com o painel de aderência na mão.

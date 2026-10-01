# Mesa Operada por Agentes — Curso HN

> Como funciona o método do AlgoMaker (algomakers.com), como operar o produto passo a passo
> e como aplicar a mesma arquitetura na **HN Gestão Comercial e Marketing**: agentes de IA
> que trabalham dentro de um mandato, um funil que reprova o que não se sustenta, e a
> decisão de gastar dinheiro sempre na mão de um humano.

---

## Como usar este manual

Este curso foi montado a partir de **tudo o que o AlgoMaker publica abertamente**: as 13
páginas do sitemap (institucional em 5 idiomas, página "em português claro", plataforma e
preço, quiz, diagnóstico, contato, termos e privacidade), o `llms.txt`, o **manual público do
cliente** e o **plugin público** que o próprio site distribui para o Claude Code (com a
doutrina que o agente segue). Nada foi tirado de área restrita. O conteúdo é escrito do zero.
Ele não é material oficial do AlgoMaker.

**O que foi e o que não foi testado.** As ferramentas da HN deste curso (o funil de campanhas
e o servidor MCP da mesa comercial) foram executadas e validadas. O **produto AlgoMaker em
si não foi instalado nem executado**: os passos das Aulas 03 a 08 reproduzem o manual
público dele. Comandos e versões podem mudar — na dúvida, siga o que o próprio Claude
devolver ao pedir "instala o AlgoMaker nesta máquina".

> **Aviso de risco.** O AlgoMaker é software de pesquisa e execução para operar mercado
> financeiro. Operar envolve risco real de perda, inclusive do capital inteiro. Nada neste
> curso é recomendação de investimento. Resultado passado, simulado ou real, não garante
> resultado futuro.

O curso tem quatro partes:

| Parte | Aulas | Para quê |
|---|---|---|
| **Entender** | 01–02 | O que muda quando a IA opera por funções, e a mesa de cinco postos |
| **Operar o AlgoMaker** | 03–08 | Instalar, minerar, acompanhar, ligar dinheiro real e resolver problemas |
| **A doutrina** | 09–10 | O funil cético e os controles que tornam isso confiável |
| **Aplicar na HN** | 11–14 | A mesa comercial da HN, com ferramentas prontas e testadas |
| **Bônus** | B1–B2 | O funil de vendas do AlgoMaker e riscos/conformidade |

---

## A ideia central em uma frase

> **Autonomia é a parte fácil. O produto é a contenção.**

Qualquer coisa pode ser automatizada com IA. O que separa uma operação séria de uma aposta é
o que o sistema **se recusa a fazer** e o que ele **registra** enquanto faz o resto. Todo o
método decorre disso:

1. **Mandato antes de ação** — sem objetivo, limite de perda e horizonte escritos, nada roda.
2. **Funil que mata** — as ideias passam por testes desenhados para reprovar, não para confirmar.
3. **Simulação antes do real** — tudo roda primeiro sem dinheiro.
4. **Portão humano** — ligar dinheiro real é um clique humano, numa tela, nunca do agente.
5. **Previsto contra realizado** — o sistema presta contas do que prometeu.
6. **Registro de tudo** — cada decisão fica gravada com o motivo.

Guarde essas seis regras. A Parte 4 aplica cada uma delas na HN.

---

## Aula 01 — A virada: o agente não finge ser mouse

**Objetivo:** entender por que a IA deve operar por **funções** e não clicando em telas.

### Conceito

Um robô que move o cursor quebra no dia em que um botão muda de lugar — e não deixa nada
auditável para trás. A alternativa é o sistema **expor as próprias operações como funções**:

```
data.download()       baixar dados
mine.strategies()     gerar candidatas
retest.funnel()       passar pelo funil
portfolio.run()       montar a carteira
deploy.paper()        simular sem dinheiro
exec.status()         ver como está
```

O agente **chama** essas funções; o **mandato limita** o que ele pode chamar; e **cada decisão
fica registrada com o motivo**. É a diferença entre um histórico que você explica e um que
você apenas mostra.

### O que é MCP

**MCP (Model Context Protocol)** é o padrão aberto que liga um agente de IA (Claude, ChatGPT,
Codex) a ferramentas externas. O sistema publica uma lista de funções com descrição e travas;
o agente descobre essa lista sozinho e chama o que precisa. É assim que o AlgoMaker se
conecta "ao modelo que você já paga": **a plataforma não vende inteligência — ela expõe a
mesa, e o seu agente traz o raciocínio**, pela sua própria assinatura.

O AlgoMaker oferece quatro formas de integração:

| Integração | Para quê |
|---|---|
| **Servidor MCP** | O agente descobre e chama as ferramentas diretamente |
| **API local** | Interface HTTP autenticada na máquina, para sistemas sem agente |
| **Painel (cabine)** | A visão humana do mesmo motor: campanhas, carteiras, monitor |
| **Implantação própria** | Roda na sua infraestrutura (inclusive VPS), sem custódia de recursos |

### Exercício HN
Liste 5 tarefas da HN que hoje alguém faz "clicando em tela" (ex.: puxar relatório do Meta
Ads, atualizar CRM). Para cada uma, escreva como seria a **função** equivalente:
`relatorio.campanhas(periodo)`, `crm.leads_novos(desde)`…

---

## Aula 02 — A mesa de cinco postos

**Objetivo:** entender a estrutura de trabalho que o AlgoMaker automatiza — e que serve de
modelo para qualquer operação.

### Os cinco problemas que caem numa pessoa só

Numa mesa profissional, cada problema tem um responsável, um horário e um método. Na mesa de
uma pessoa só, todos chegam nela ao mesmo tempo:

| Problema | Como aparece |
|---|---|
| **Tempo** | O mercado não fecha. Você fecha. O movimento acontece no meio do expediente. |
| **Conhecimento** | Ninguém te ensinou a medir se o padrão é real ou coincidência. |
| **Código** | A estratégia mora na sua cabeça: não pode ser testada, repetida nem auditada. |
| **Emocional** | Três da manhã, duas perdas seguidas — e é você, cansado, que decide o tamanho da próxima. |
| **Validação** | A curva sobe bonita no histórico. Ninguém testou no pedaço que ela nunca viu. |

### Os cinco postos — cada um vira um agente

| Posto | Função na mesa |
|---|---|
| **Macro** | Lê dados globais, calendário e notícias; ajusta quanto pode estar exposto hoje |
| **Quant** | Transforma a ideia em hipótese mensurável e a submete a testes que quase nada sobrevive |
| **Programador** | Escreve o código, versiona e deixa rastro — a estratégia vira artefato conferível |
| **Risco e compliance** | O cão de guarda: confere cada ordem contra o limite e recusa dizendo o motivo |
| **Execução** | Encontra liquidez, calcula o tamanho, envia a ordem e registra a proteção |

Na plataforma, esses postos aparecem como cinco "estações": **Macro** (base tratada),
**Tese** (hipótese testável, janela selada), **Modelo** (tamanho pela liquidez medida),
**Robô** (executa sem tela aberta) e **Mesa** (cobra o que foi prometido).

### Exercício HN
Desenhe os cinco postos da **área comercial** da HN (a Aula 11 traz uma proposta pronta).
Quem faz cada função hoje? Quanto tempo por semana?

---

## Aula 03 — Preparar e ligar o conector

**Objetivo:** deixar o Claude conhecendo o AlgoMaker.

### O que é grátis e o que pede licença

| Grátis, sem cadastro | Pede licença |
|---|---|
| Baixar dados históricos | Operar com dinheiro real (modo LIVE) |
| Minerar estratégias | Exportar o código da estratégia (.mq5 / Python) |
| Testar robustez (walk-forward, Monte Carlo, estresse de custo) | Exportar arquivos .alg |
| Montar carteira e medir correlação | |
| Simular em papel (preço real, ordem simulada) | |

**Tudo até ter a primeira carteira em simulação é grátis.** A licença (R$ 497 à vista ou
12× R$ 51,40, válida por 12 meses, sem renovação automática, 7 dias para desistir — valores
publicados no site em 2026) só entra para operar com dinheiro real.

### O que você precisa ter
- **Claude Pro ou Max** — app de desktop (Mac/Windows), claude.ai ou Claude Code. O uso sai
  da sua assinatura; não há custo de API.
- **Windows 10/11 ou macOS** (Linux pelo terminal).
- Para minerar: **4 núcleos e 8 GB de RAM** no mínimo.

### Caminho A — Claude Desktop ou claude.ai
1. **Configurações → Conectores → Adicionar conector personalizado.**
2. Preencha: **Nome** `AlgoMakers` · **URL** `https://algomakers.com/mcp` ·
   **Autenticação** nenhuma · **Cabeçalhos** vazio · **Avançada** não mexa.
3. O aviso laranja ("sem credenciais, qualquer pessoa pode usar") é esperado: esse conector
   **só orienta**, não executa nada nem vê seus dados.
4. **Adicionar.** Abra uma conversa nova, confira que o conector está ligado e pergunte:
   *"O que é o AlgoMaker?"*

### Caminho B — Claude Code
Dentro do Claude Code, um comando de cada vez:
```
/plugin marketplace add https://algomakers.com/claude/marketplace.json
/plugin install algomaker@algomakers
```
Confirme a confiança no marketplace e escolha o escopo **usuário**. Confira com `/mcp`: devem
aparecer `algomaker-onboarding` e `algomaker-motor` (este só conecta depois da Aula 04).

### A conversa de orientação
Com o conector ligado, frases que funcionam: *"Como instalo no Windows?"*, *"Preciso pagar
para testar?"*, *"Já tenho uma chave de licença"*.

---

## Aula 04 — Ligar o motor e abrir o painel

**Objetivo:** instalar o motor (é ele que minera) e abrir a tela de controle.

### Conceito
**Não existe aplicativo para baixar.** Instala-se só o **motor**, pelo `uv` (um gerenciador
de Python), e a tela é um **painel servido no seu navegador**, em `127.0.0.1` — ou seja, na
sua própria máquina, sem nada na internet.

### O jeito mais simples
No Claude Code, peça: **"instala o AlgoMaker nesta máquina"**. O agente roda os comandos.

### Se for você a digitar
**1. Instale o `uv` (uma vez só):**
```
# Windows (PowerShell):
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Mac/Linux (Terminal):
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**2. Registre o motor.** O comando exato traz o número da versão do motor e muda com o
tempo — peça ao Claude *"como instalo no Mac?"* (ou Windows) e use a linha que ele devolver.
No Claude Code com o plugin da Aula 03, basta ter o `uv`: o plugin sobe o motor sozinho.

**3. Feche e abra o Claude por completo.** Ele só lê a lista de conectores ao iniciar. É o
passo que mais gente esquece. Para conferir, pergunte *"qual é o status da minha licença?"*
— a resposta vem do motor: plano **free** e o identificador da máquina.

### O painel
Diga **"abre o painel"**. Abre no navegador uma tela com **Início, Construtor, Databank,
Fábrica, Monitor e Configurações**. O link é de uso único e vence em 5 minutos. É **no
painel** que você faz o que o agente não pode: cadastrar chave de corretora, armar dinheiro
real, fechar posição. O painel continua rodando mesmo com o Claude fechado.

Onde ficam seus dados: `%APPDATA%\@mm\desktop` (Windows), `~/Library/Application
Support/AlgoMaker` (Mac), `~/.local/share/algomaker` (Linux).

---

## Aula 05 — O mandato e a primeira carteira

**Objetivo:** fazer o sistema minerar, validar e simular uma carteira.

### Primeiro, o mandato — sem ele, nada roda
O agente precisa saber quem você é antes de minerar. **É proposital.** Diga as quatro coisas:
```
Meu capital é 10 mil dólares, aguento 20% de queda, quero crescimento,
horizonte de 6 meses.
```
Depois:
```
Monta uma carteira pra mim.
```

### O que acontece, na ordem
1. **Destino:** ele pergunta onde você vai executar (ex.: Bybit ou robô `.mq5`). Isso muda
   dados, custo e tipo de ordem. *Minerar no destino errado não dá erro: dá um backtest
   aprovado com o custo da corretora errada.*
2. **Dados:** baixa o necessário (minutos).
3. **Porteiro:** mede se cada ativo tem liquidez para o seu tamanho. Se não tem, **recusa e
   diz o número**. Isso é o produto funcionando.
4. **Mineração:** gera candidatas e valida em **três fatias de tempo** — a última é um
   **trimestre selado** que nada influenciou (minutos a horas).
5. **Carteira:** monta, mede correlação e põe em **simulação com preço real** (papel).

> **Espere recusas.** O funil descarta mais de 99% das candidatas. Poucas e sólidas é o
> objetivo. "Mineração salvou zero" com motivo escrito é melhor que dez estratégias ruins.

---

## Aula 06 — Acompanhar a carteira

**Objetivo:** ler o que importa — e não a curva bonita.

Pergunte: **"Como está minha carteira?"** e leia três números antes de qualquer conclusão:

| Número | O que mostra |
|---|---|
| **Retorno sobre o capital em risco** | Quanto rendeu sobre o que estava de fato posicionado, não sobre a conta inteira |
| **Ocupação** | Quanto do tamanho planejado está no mercado. Gap alto = ordem que não está entrando |
| **Bloqueios da corretora** | Recusas que exigem ação sua, já com a ação escrita |

### Aderência: previsto contra realizado
O painel compara, linha por linha, o que o estudo previu com o que a conta está fazendo:

| Métrica | Previsto | Ao vivo |
|---|---|---|
| Taxa de acerto | 50,08% | 50,00% |
| Ritmo de operações | 15,0/dia | 4,0/dia |
| Risco consumido | 13,2% | 0,01% |

*(valores ilustrativos do próprio site)*

É uma **leitura de comportamento, não de retorno**: se a operação real se afasta do que o
teste prometeu, algo mudou — e você descobre cedo.

### Três formas de ver a mesma informação
O painel se adapta a quem olha: **terminal** (para quem opera), **diário** em português com
cada decisão e o motivo (para quem está aprendendo) ou **um personagem que avisa** (para quem
não quer pensar nisso). Exemplo do diário: *"14:32 recusou — TAO · ordem pequena demais"*.

---

## Aula 07 — Licença, corretora e dinheiro real

**Objetivo:** passar da simulação para o real com todas as travas no lugar.

### 1. Comprar e ativar
Ao pedir *"põe ao vivo"*, o motor recusa e devolve o endereço de compra. A chave chega por
e-mail (formato `MM-…`). Cole no chat: *"Ativa a licença: MM-XXXX-…"*. Ela fica **travada
naquela máquina**. O agente **nunca adivinha, gera ou completa** uma chave.

### 2. Cadastrar a corretora — só você, na tela
No painel: **Configurações → Conexões → Nova conexão**. A chave de API é digitada **na
página, nunca no chat**. Use chave **sem permissão de saque** e só com permissão de
negociação. Sem IP fixo, ela vence em 90 dias (o agente avisa 14 dias antes).

### 3. Armar o LIVE — o portão humano
O agente prepara tudo (carteira, tamanhos, stops), mas **não arma sozinho**. No painel:
**Monitor → Armar LIVE**, com confirmação e um segundo fator digitado por você.

> **Atenção (está nos Termos de Uso):** definir um limite de perda tolerada no aplicativo
> **não faz a plataforma ajustar os tamanhos sozinha** para respeitá-lo. Esse limite se
> atinge na composição da carteira e no dimensionamento que **você** escolhe. Confira os
> tamanhos antes de armar.

### Depois de armado
- **Parar tudo, o agente pode** (chave de corte). **Destravar, só você.**
- Stop e alvo ficam **na corretora** como ordens próprias: se o computador desligar, a
  proteção continua — só param as novas entradas.
- Para operar com o computador desligado, o caminho é um servidor (VPS).
- O dinheiro **não sai da sua conta**: o sistema não recebe, não guarda e não saca.

> Comece pequeno. O site informa que alguns ativos aceitam ordem com cerca de US$ 6 de
> margem — dá para ver tudo funcionando antes de escalar. Lembre do aviso de risco no início.

---

## Aula 08 — Problemas comuns

| Sintoma | Causa e solução |
|---|---|
| O Claude só tem ferramentas `algomaker_*` | Motor não ligado ou Claude não reiniciado. Peça "instala o AlgoMaker nesta máquina" e reinicie |
| O conector não mostra "Detectado" | URL errada: tem que ser exatamente `https://algomakers.com/mcp` |
| Mandaram baixar um instalador `.exe` | Não existe mais. Instala-se só o motor; a tela é o painel no navegador |
| `uvx: command not found` | Instale o `uv` e feche e abra o terminal |
| "porteiro recusou a campanha" | Ativo sem liquidez para o seu lote, ou dado insuficiente. Ajuste capital, ativo ou tempo gráfico |
| Mineração salvou zero | Normal em campanhas curtas. Aumente população/gerações ou troque de ativo |
| Ordem recusada "regulatory restrictions" | A corretora bloqueou a conta naquele contrato. Fale com o suporte dela |
| Chave de API "invalid" | Venceu, foi revogada ou é de outra região. Gere outra e cadastre de novo |
| Página de confirmação "expirou" | Vale poucos minutos. Peça outra ao agente |
| Atualizei e os robôs pararam | Instalar reinicia o app. Abra o Monitor e relance |

Suporte humano do produto: support@algomakers.com.

---

## Aula 09 — O funil cético

**Objetivo:** entender os testes que separam padrão de sorte — o coração do método.

### As quatro perguntas, nesta ordem
1. **Ela funciona onde nunca olhou?** Um pedaço do histórico é guardado e ninguém o usa para
   decidir (**janela selada**). Se a estratégia só acerta no trecho que usou para se montar,
   ela **decorou**. É aqui que a maioria cai.
2. **Ela aguenta um mercado diferente?** Ninguém prevê o futuro, mas dá para saber se o
   resultado sobrevive quando você **mexe nos próprios números** dela.
3. **O que segura a queda?** Limite de perda por operação e por dia escrito **antes**, com a
   proteção registrada na corretora.
4. **E o custo?** O teste é refeito com custo **mais caro** do que a corretora cobra.

### Os termos, em português claro
| Termo | O que é |
|---|---|
| **Fora da amostra** | Testar em dados que não foram usados para criar a estratégia |
| **Walk-forward** | Ajustar num período, testar no seguinte, avançar a janela e repetir |
| **Monte Carlo** | Embaralhar/sortear a sequência de resultados milhares de vezes para ver o pior caso plausível |
| **Estresse de custo** | Refazer a conta com taxa e escorregamento maiores que os reais |
| **Porteiro / pré-voo** | Recusar antes de gastar processamento, dizendo por que daria zero |

> **Honestidade de custo:** a tabela de custo usada na pesquisa é a mesma que o executor
> cobra. **A pesquisa não pode ser mais barata que a realidade.**

---

## Aula 10 — Contenção: os controles que tornam isso confiável

**Objetivo:** conhecer as travas que valem para qualquer sistema operado por IA.

| Controle | Como funciona |
|---|---|
| **Portão humano** | Armar capital real e cadastrar chaves são ações humanas na tela. O agente prepara, monitora e desliga — não se liga sozinho |
| **Recusa por projeto** | Sem mandato (capital, queda máxima, objetivo, horizonte), o funil se recusa a rodar |
| **Pré-voo** | Antes de gastar horas de máquina, confere restrições e explica por que daria zero |
| **Chave de corte** | Parar e encerrar são operações de primeira classe, chamáveis a qualquer momento |
| **Local primeiro** | Detalhes ficam na máquina do operador; só saem agregados anônimos |
| **Honestidade de custo** | A pesquisa usa o mesmo custo que a execução cobra |

### "Por arquitetura, não por promessa"
O ponto mais importante: o agente **não tem** a função de armar dinheiro real ou gravar chave
de corretora. Não é uma regra que ele "promete" seguir — **a rota não existe**. Contenção
boa é aquela que não depende da boa vontade da IA.

### Inteligência de frota
O dado raro não é o histórico de preço (todo mundo tem o mesmo). É o **par**: o que o teste
prometeu e o que executar custou de verdade. O AlgoMaker devolve esse custo **medido** para
apertar o funil. Isso só acontece com consentimento, perguntado uma vez antes do primeiro
LIVE: saem percentuais anônimos e, no mesmo consentimento, o total de volume negociado —
nunca chaves, saldos, posições ou ordem a ordem. Com isso, uma estratégia que só
sobrevive com premissa otimista de execução deixa de ser aprovada.

---

## Aula 11 — A mesa comercial da HN operada por agentes

**Objetivo:** levar a arquitetura para a gestão comercial e de marketing da HN.

### Os cinco postos, traduzidos
| Posto na mesa | Posto na HN | O agente faz | Entrega |
|---|---|---|---|
| Macro | **Inteligência de mercado** | Lê sazonalidade, concorrência, calendário do cliente | Quanto a verba pode estar exposta no mês |
| Quant | **Hipóteses de campanha** | Transforma ideia em teste com janela selada | Variantes aprovadas/reprovadas com motivo |
| Programador | **Automação** | Escreve integrações, relatórios, scripts | Código versionado e conferível |
| Risco e compliance | **Verba, marca e LGPD** | Confere cada ação contra o mandato | Recusa com motivo, nunca exceção |
| Execução | **Operação de mídia e CRM** | Prepara publicação, segmentação, cadência | Tudo pronto para o humano aprovar |

### O mandato comercial
Assim como o AlgoMaker não minera sem capital, queda máxima, objetivo e horizonte, a mesa da
HN não analisa nada sem **objetivo, verba, CPA máximo e horizonte**. O modelo está em
`algomaker/modelos/mandato.json` e o guia de preenchimento em
`algomaker/modelos/mandato-comercial.md`.

### O que o agente da HN NUNCA faz
- **Gastar ou aumentar verba** — só o humano, na plataforma de anúncios.
- **Publicar anúncio** ou **enviar mensagem** a clientes/leads.
- **Mudar preço, oferta ou contrato.**

Ele **prepara, analisa, recomenda e registra**. Igual ao AlgoMaker: *parar* ele pode
(pausar um teste que estourou o mandato pode ser uma função liberada); *ligar* dinheiro é
sempre humano.

### Exercício HN
Preencha o mandato de um cliente real da HN usando `mandato-comercial.md`.

---

## Aula 12 — O funil de campanhas da HN

**Objetivo:** aplicar o funil cético a criativos, ofertas e públicos.

### A tradução do funil
| Portão do AlgoMaker | Portão na HN |
|---|---|
| Porteiro (liquidez para o lote) | **Amostra mínima** de conversões nos dois períodos |
| Fora da amostra (trimestre selado) | **Período selado**: CPA dentro do teto e conversão sem desabar |
| Robustez (Monte Carlo) | **Probabilidade** de o CPA real ficar dentro do teto |
| Estresse de custo | **CPA com custo +25%** continua dentro do teto |

O **período selado** é a chave: separe as últimas semanas da campanha e **não use esse
pedaço para decidir nada** durante o ajuste. Só no fim você olha. Variante que só funcionou
no período em que foi otimizada **decorou** o público — e vai decepcionar quando escalar.

### Rodando o funil (ferramenta pronta e testada)
O CSV tem uma linha por variante e período (`treino` ou `selado`):
```
variante,periodo,impressoes,cliques,conversoes,gasto
gancho-resultado-cliente,treino,52000,1610,71,3900.00
gancho-resultado-cliente,selado,25000,790,34,1880.00
```
```
python3 algomaker/ferramentas/funil_campanhas.py algomaker/modelos/exemplo-campanhas.csv --cpa-max 80
```
Resultado real do exemplo:
```
variante                  CPA treino  CPA selado  P(teto)  status
gancho-dor-processo            60.00       59.63        —  REPROVADA  [porteiro] amostra pequena: 27 conversões, mínimo 30
gancho-resultado-cliente       54.93       55.29      98%  APROVADA  [—] passou nos 4 portões
oferta-diagnostico-gratis       42.00       46.67     100%  APROVADA  [—] passou nos 4 portões
promocao-relampago             40.00       95.00        —  REPROVADA  [fora da amostra] CPA selado R$ 95.00 acima do teto R$ 80.00
video-depoimento               50.86       72.22        —  REPROVADA  [fora da amostra] conversão caiu 33% no período selado (máx. 30%)
carrossel-metodo               67.35       74.19      70%  REPROVADA  [robustez] só 70% de chance de o CPA ficar no teto (mín. 80%)
publico-donos-pme              46.44       68.00      97%  REPROVADA  [estresse de custo] com custo +25% o CPA vira R$ 85.00

2 de 7 variantes aprovadas. Reprovar é o funil funcionando.
```
Repare na `promocao-relampago`: o **melhor CPA no treino** (R$ 40) e o **pior no selado**
(R$ 95). Sem o período selado, seria a primeira a receber verba.

### Ajustes do funil
`--min-conversoes 30` · `--queda-max 0.30` · `--prob-min 0.80` · `--estresse 1.25`.
Ajuste ao cliente, **antes** de rodar — mudar a régua depois de ver o resultado é decorar.

---

## Aula 13 — Previsto contra realizado e o diário de decisões

**Objetivo:** prestar contas ao cliente do que foi prometido — como o painel de aderência.

### O painel de aderência da HN
Toda variante aprovada sai do funil com um **previsto** (CPA, taxa de conversão, ritmo de
conversões por semana). Quando a verba escala, compare toda semana:

| Métrica | Previsto (selado) | Realizado (escala) | Leitura |
|---|---|---|---|
| CPA | R$ 46,67 | R$ 51,20 | dentro do teto, +10% |
| Taxa de conversão | 4,6% | 4,3% | estável |
| Conversões/semana | 24 | 21 | ocupação 88% |

Se o realizado se afasta do previsto, **algo mudou** (público saturou, concorrência, oferta
cansou) — e você vê antes de queimar a verba. O modelo de relatório está em
`algomaker/modelos/painel-aderencia.md`.

### O diário de decisões
Cada decisão (escalar, pausar, reprovar) é registrada **com o motivo e os números**. É o que
transforma "achamos que funcionou" em um histórico que o cliente consegue auditar — e o que
diferencia a HN de uma agência que só mostra print de resultado.

---

## Aula 14 — Montando a mesa da HN com Claude Code

**Objetivo:** ligar tudo no Claude Code, com a mesma arquitetura do AlgoMaker.

### Camada 1 — A doutrina (skill)
A skill `.claude/skills/mesa-comercial-hn/SKILL.md` ensina o agente a trabalhar como a mesa:
mandato antes de ação, funil antes de verba, portão humano, registro de tudo. O Claude Code
carrega sozinho quando você trabalha neste repositório.

### Camada 2 — As funções (servidor MCP)
O servidor `algomaker/ferramentas/mcp_mesa_hn.py` expõe as operações da mesa como funções:

| Ferramenta | O que faz |
|---|---|
| `mandato_ler` | Lê objetivo, verba, CPA máximo e o que exige aprovação humana |
| `funil_avaliar` | Passa as variantes pelos 4 portões — **recusa se não houver mandato** |
| `diario_registrar` | Grava a decisão com motivo e números |
| `diario_ler` | Lê as últimas decisões |

E, **de propósito, não existe** ferramenta para gastar verba, publicar ou enviar mensagem.
Contenção por arquitetura, não por promessa.

Instalar e registrar (na raiz do repositório):
```
pip install mcp
claude mcp add mesa-hn -- python3 algomaker/ferramentas/mcp_mesa_hn.py
```
Reinicie o Claude Code e confira com `/mcp`. Depois é só conversar:
```
Leia o mandato e passe as campanhas de algomaker/modelos/exemplo-campanhas.csv
pelo funil. Registre no diário a recomendação para cada aprovada.
```

> **Testado:** com um cliente MCP real, o servidor listou as 4 ferramentas, aprovou 2 de 7
> variantes, gravou e leu o diário — e recusou rodar quando o mandato foi removido.

### Camada 3 — Próximos passos
Quando a mesa estiver madura, novas funções entram uma de cada vez, sempre com trava:
`relatorio_meta_ads(periodo)` (só leitura), `crm_leads(desde)` (só leitura),
`pausar_variante(id)` (parar é permitido — como a chave de corte). **Ligar verba nunca entra.**

---

## Bônus 01 — O funil de vendas do AlgoMaker (para a HN copiar)

**Objetivo:** estudar como o AlgoMaker vende — é gestão comercial de primeira, e a HN pode
aplicar para os próprios clientes.

### 1. Uma página por público
| Página | Público | Tom |
|---|---|---|
| Institucional (`/`, em 5 idiomas) | Mesas, family offices, gestoras | Técnico, cético, "veja o funil reprovar" |
| "Em português claro" (`/comprar`) | Quem investe e não programa | Analogias: "um escritório onde quem opera são agentes" |
| Plataforma (`/plataforma`) | Quem já decidiu | Preço, "no ar em 20 minutos", FAQ, garantia |

**Para a HN:** a mesma oferta, contada de três jeitos, para três níveis de consciência.

### 2. "Para quem isto NÃO é"
O site diz com todas as letras: *"Se você procura sinal, conta gerida ou retorno alvo, esta é
a porta errada — e é melhor saber agora."* Desqualificar aumenta a confiança de quem fica e
economiza o tempo do comercial.

### 3. O quiz que qualifica e educa (`/algomakerquiz`)
Um questionário curto (~4 minutos) que pergunta qual IA você já usa, o que te descreve, o que quer operar,
quanto pretende colocar, qual relação risco/retorno espera, em quais padrões já acreditou e o
que te trava. Cada resposta **ensina algo** ("abaixo de certo valor o custo come qualquer
resultado") e **segmenta** o lead. No fim: *"A maioria vai ser reprovada. Inclusive as
minhas."*

### 4. O diagnóstico que coloca o problema em reais (`/diagnostico`)
Vídeo de 3 minutos → 5 blocos (dados, renda, objetivo, travas, tentativas anteriores, horas
por dia gastas) → **a página calcula o custo anual do tempo gasto tentando resolver sozinho**
→ escolha de turnos para uma ligação de 30 minutos com um consultor que **já chega com o
diagnóstico na mão**. "Uma sessão por pessoa" cria escassez honesta.

**Para a HN:** um diagnóstico comercial que calcula, em reais, quanto o cliente perde por mês
com lead não respondido, follow-up esquecido ou verba em criativo cansado — e agenda a
reunião já com esse número.

### 5. A demonstração honesta
A chamada não é "veja nossos resultados", é **"veja o funil reprovar uma estratégia, ao
vivo"**. Mostrar o que o método recusa vende mais rigor do que qualquer curva bonita.

### 6. Transparência como posicionamento
Avisos de risco em toda página, "sem promessa de retorno, sem taxa sobre o que você ganhar",
e até a divulgação de que o link da corretora é **parceria remunerada**, dito na mesma
resposta. Os termos declaram o rebate que recebem das corretoras "em linha com o espírito da
Resolução CVM 179, ainda que não estejamos sujeitos a ela" — transparência que vira argumento
de venda.

---

## Bônus 02 — Riscos, ética e conformidade

- **Trading:** risco real de perda total. Nada aqui é recomendação. Comece em simulação,
  depois com o mínimo, e nunca com dinheiro que fará falta.
- **A HN não deve operar o AlgoMaker em nome de clientes.** Os Termos de Uso proíbem operar
  em nome de terceiros sem habilitação legal, e gerir recurso de terceiros no Brasil exige
  autorização da CVM. Usar para a própria conta é uma coisa; oferecer como serviço é outra.
  A aplicação da HN é a **arquitetura** (Aulas 11–14), não a operação de mercado.
- **Chaves e senhas:** nunca no chat. Chave de corretora sem permissão de saque.
- **Dados de clientes da HN (LGPD):** a mesa processa localmente; não cole dados pessoais de
  leads em ferramentas sem base legal. Prefira agregados (como a "frota" do AlgoMaker).
- **Promessas comerciais:** copie o rigor, não a promessa. Nada de "retorno garantido" em
  oferta da HN — nem de "CPA garantido".
- **Remuneração de parceiros:** se a HN indicar ferramenta com comissão, diga isso junto.

---

## Os materiais que acompanham o curso

- **Mandato comercial** → `algomaker/modelos/mandato-comercial.md` e `algomaker/modelos/mandato.json`
- **Painel de aderência** → `algomaker/modelos/painel-aderencia.md`
- **Dados de exemplo** → `algomaker/modelos/exemplo-campanhas.csv`
- **Funil de campanhas** → `algomaker/ferramentas/funil_campanhas.py`
- **Servidor MCP da mesa** → `algomaker/ferramentas/mcp_mesa_hn.py`
- **Doutrina para o agente** → `.claude/skills/mesa-comercial-hn/SKILL.md`

## Glossário rápido

- **Agente de IA** — IA que chama ferramentas e executa tarefas (Claude, Codex).
- **MCP** — padrão aberto que liga o agente a ferramentas externas.
- **Mandato** — objetivo, limite de perda/custo e horizonte escritos antes de qualquer ação.
- **Janela/período selado** — dados guardados que ninguém usa para decidir; servem de prova final.
- **Walk-forward** — ajustar num período, testar no seguinte e avançar.
- **Monte Carlo** — milhares de sorteios para ver o resultado plausível, não só o médio.
- **Estresse de custo** — refazer a conta com custo maior que o real.
- **Papel (paper trading)** — operar com preço real e ordem simulada, sem dinheiro.
- **Portão humano** — ação que só um humano pode executar, numa tela.
- **Chave de corte (kill-switch)** — parar tudo, a qualquer momento.
- **Aderência** — o realizado comparado ao que o teste previu.
- **CPA** — custo por aquisição (gasto ÷ conversões).

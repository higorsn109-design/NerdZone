# Mesa Operada por Agentes — Curso HN

> O conteúdo do AlgoMaker (algomakers.com) completo e organizado em aulas. No fim, a
> aplicação do mesmo método na **HN Gestão Comercial e Marketing**, separada e marcada.

---

## Como usar este manual

### De onde vem cada coisa
Cada aula começa com uma etiqueta de fonte:

| Etiqueta | Significa |
|---|---|
| **ORIGINAL** | Conteúdo do AlgoMaker, com a página de onde veio. Reescrito em formato de aula, sem mudar o sentido. Trechos entre aspas são citações. |
| **ADAPTAÇÃO HN** | Criado para este curso. **Não existe no AlgoMaker.** Sempre começa mostrando o original em que se baseia. |

As **Aulas 01 a 14 são ORIGINAIS** (o produto é de trading). As **Aulas 15 a 18 são
ADAPTAÇÃO HN** (o AlgoMaker não fala de marketing nem de área comercial). Os bônus misturam
os dois e cada parte está marcada.

### As fontes (todas públicas)
Todas as rotas do `sitemap.xml` do site, mais as que ele cita:

| Rota | O que tem |
|---|---|
| `/` (e `/pt/`, `/es/`, `/zh/`, `/ru/`) | Página institucional: a virada, a pilha, frota, controles, integração, para quem é |
| `/comprar` | A versão "em português claro" para quem investe sem programar |
| `/plataforma` | O produto, o preço, as skills, as telas, as perguntas frequentes |
| `/claude/manual` | O manual do cliente, etapa por etapa |
| `/algomakerquiz` | O questionário de entrada |
| `/diagnostico` | O diagnóstico com cálculo do custo do tempo |
| `/contato` | Pedido de demonstração técnica |
| `/termos` · `/privacidade` | Termos de uso e política de privacidade |
| `/robots.txt` · `/llms.txt` | Instruções para robôs e resumo para IAs |
| `/claude/marketplace.json` | O plugin para Claude Code e a skill com a doutrina do agente |

Não foi acessada nenhuma área restrita. A parte da doutrina que só o motor instalado entrega
(o "chip") **não está aqui**, porque exigiria rodar o software de trading.

### O que foi testado
- **Testado:** as ferramentas da adaptação HN (funil de campanhas e servidor MCP), com
  resultados reais mostrados nas Aulas 16 e 18.
- **Não testado:** o produto AlgoMaker. As Aulas 05 a 11 reproduzem o manual dele.
  Comandos e versões podem mudar.

> **Aviso de risco (original, presente em todas as páginas do AlgoMaker).** "AlgoMaker é
> software de pesquisa e execução. Nada nesta página é recomendação de investimento, oferta,
> solicitação ou indicação de qualquer ativo. Desempenho passado, simulado ou real, não
> garante resultado futuro. Operar mercado envolve risco de perda, inclusive total do
> capital."

### Mapa do curso
| Parte | Aulas | Fonte |
|---|---|---|
| **1. Entender o AlgoMaker** | 01–04 | ORIGINAL |
| **2. Operar o AlgoMaker** | 05–11 | ORIGINAL |
| **3. A doutrina e o negócio** | 12–14 | ORIGINAL |
| **4. Aplicar na HN** | 15–18 | ADAPTAÇÃO HN |
| **Bônus** | B1–B2 | ORIGINAL + ADAPTAÇÃO HN, marcados |

---

## Aula 01 — A virada: o agente não finge ser mouse

**Fonte:** ORIGINAL — `/` (institucional), `/llms.txt`

### A promessa
O AlgoMaker se apresenta como "da ideia à ordem executada, com prova em cada etapa": "um
laboratório cético para a IA operar onde errar custa dinheiro". Ele mede o desempenho fora
da amostra, o custo por instrumento, o lote que a corretora aceita e a divergência entre o
que o teste prometeu e o que a mesa entregou. "Roda na sua infraestrutura, com a sua chave.
Armar capital real continua sendo um clique humano."

### A virada
"Um agente não deveria ter que fingir ser um mouse." Robô que move cursor quebra no dia em
que um botão muda de lugar e não deixa nada auditável. A alternativa é a mesa **expor as
próprias operações como funções**: o agente chama, o mandato limita o que ele pode chamar, e
cada decisão fica registrada com o motivo. "É a diferença entre um histórico que você
explica e um que você apenas mostra."

| Feito para a mão | Feito para o agente |
|---|---|
| Comprar. Vender. Arrastar o stop. Ler o gráfico. Cada decisão passando por atenção, cansaço e tempo de tela. | `data.download()` · `mine.strategies()` · `retest.funnel()` · `portfolio.run()` · `deploy.paper()` · `exec.status()` |

Os números da página: **39** domínios de capacidade · **MCP** como interface nativa para
agente · **Demo → Live** como caminho de promoção · **Humano** na decisão de armar.

### O que é MCP
MCP (Model Context Protocol) é o padrão aberto que liga um agente de IA a ferramentas
externas. O sistema publica a lista de funções com descrição e travas. O agente descobre essa
lista e chama o que precisa.

### As quatro formas de integração (original)
"Ele se conecta ao modelo que você já paga. A plataforma não vende inteligência. Ela expõe a
mesa, e o seu agente traz o raciocínio — pela sua própria assinatura, sob a sua própria
governança."

| Integração | Descrição original |
|---|---|
| **MCP** | Servidor MCP nativo. O agente descobre a superfície de capacidades e chama diretamente, com descrição e travas por ferramenta |
| **API local** | Interface HTTP autenticada na máquina do operador, para sistemas que não são baseados em agente |
| **Cabine desktop** | Uma visão humana sobre o mesmo motor: campanhas, portfólios, monitor ao vivo e o plano de desvio |
| **Implantação** | Roda na infraestrutura do próprio operador, incluindo nós VPS isolados. Sem custódia de recursos do cliente |

O `llms.txt` resume: o endpoint remoto é `https://algomakers.com/mcp`, o registro oficial
MCP é `com.algomakers/algomaker`, e o motor faz dados, mineração, portfólio, papel e live,
com o live "armado só pelo dono, na tela dele".

---

## Aula 02 — O escritório de cinco postos

**Fonte:** ORIGINAL — `/comprar`, `/plataforma`

### Em português claro
"Um escritório de investimentos onde quem opera são agentes de IA." É um programa instalado
no seu computador. Você conversa com ele como com uma pessoa: diz quanto quer investir,
quanto aceita perder e em quanto tempo. Ele cria as estratégias e testa cada uma "como um
fundo testaria". Só opera na sua conta da corretora depois que você autorizar.

### Os cinco problemas que caem numa pessoa só
"Cinco problemas diferentes. Uma pessoa só para todos."

| Problema | Cena (original) | Explicação (original) |
|---|---|---|
| **Tempo** | O movimento aconteceu às 14h, no meio do expediente. Você só viu à noite. | O mercado não fecha. Você fecha. |
| **Conhecimento** | Dois gráficos idênticos: um seguiu, o outro desmanchou. | Ninguém te ensinou a medir se o que você viu é padrão ou coincidência. |
| **Código** | Você pede à IA um robô e não consegue conferir uma linha. | A estratégia mora na sua cabeça e morre lá: não pode ser testada, repetida nem auditada. |
| **Emocional** | Três da manhã, duas perdas seguidas, você cansado decide o tamanho da próxima. | Nenhum humano foi feito para isso. |
| **Validação** | A curva sobe bonita no histórico que ela viu. | Prova é sobreviver ao pedaço de mercado que ela nunca viu. |

### Os cinco postos (cada um é um agente, 24 horas)
| Posto | O que faz (original) |
|---|---|
| **Macro** | Lê dados globais, calendário e notícia, e ajusta o quanto da conta pode estar exposta hoje |
| **Quant** | Transforma a ideia em hipótese mensurável e a submete ao trecho que ela nunca viu, ao custo maior que o real e à mudança nos próprios parâmetros |
| **Programador** | Escreve o código, versiona e deixa rastro. A estratégia vira "um artefato que dá para conferir linha a linha" |
| **Risco e compliance** | "O cão de guarda." Confere cada ordem contra o limite por operação e no dia, e recusa dizendo o motivo. "Não abre exceção porque desta vez parecia óbvio" |
| **Execução** | Encontra liquidez, calcula o tamanho, roteia e registra a ordem de proteção na corretora |

Na `/plataforma`, os mesmos postos aparecem como **cinco estações**: 01 **Macro** (base
tratada e atualizada) · 02 **Tese** (hipótese testável, janela selada) · 03 **Modelo**
(tamanho pela liquidez medida) · 04 **Robô** (executa sem tela aberta) · 05 **Mesa** (cobra o
que foi prometido). "Já construídas. Sua IA opera todas — não precisa criar nenhuma."

### Os quatro passos (original, `/comprar`)
"Ninguém liga o dinheiro por você."
1. **Você diz o que quer**: em português, quanto quer alocar, quanto aceita perder e em quanto tempo.
2. **O escritório constrói e testa**: submete cada estratégia a um pedaço de mercado que ela nunca viu, com custo maior que o real. "Quase todas são reprovadas — e é para isso que serve."
3. **Você vê o resultado e decide**: o que sobreviveu chega com o teste inteiro à vista.
4. **Você liga, quando quiser**: só então ele conecta na corretora e opera sozinho, dentro dos limites que você escreveu.

### Onde fica o dinheiro
"O dinheiro não sai da sua conta." Você deposita na sua corretora, como já faz. O escritório
não recebe, não guarda e não saca: manda ordem para dentro da sua conta e presta contas.

---

## Aula 03 — A pilha: pesquisa, portfólio e execução

**Fonte:** ORIGINAL — `/` (institucional), `/plataforma`

"Três camadas, um funil, nada pulado."

| Camada | O que faz (original) | Inclui |
|---|---|---|
| **01 Pesquisa** | Gera candidatas em vários instrumentos e tempos gráficos e passa por "um funil desenhado para matar, não para confirmar": portões fora da amostra, walk-forward e Monte Carlo antes de qualquer promoção | Ingestão de dados e universo por liquidez · custo de execução modelado por instrumento, "não presumido" · arbitragem estatística em pares cointegrados como trilha separada |
| **02 Portfólio** | As sobreviventes vão para bancos e são compostas em portfólios, com a correlação examinada no livro inteiro | Composição, ranqueamento e reteste de um livro existente contra dados novos · análise de cenário sobre parâmetros e premissas de custo |
| **03 Execução** | "Demonstração primeiro, sempre." A execução real roda nas corretoras conectadas, com posição, execuções e custo realizado medidos contra o que o backtest presumiu | Mercados perpétuo e à vista, com taxa e slippage por corretora · leitura de desvio ao vivo por estratégia · parada e encerramento a qualquer momento, independentes do agente |

### Cobertura de mercados
"Vários mercados entram. Decisão medida sai." **Cripto · Ações · Índices · Metais ·
Commodities · Forex.** Cada mercado executa num lugar diferente, com custo, horário e tipos
de ordem próprios, e a plataforma trata cada um pelo contrato da corretora certa. "Minerar
no destino errado não dá erro: dá um backtest aprovado pelo preço da corretora errada."

### No ar em 20 minutos (original, `/plataforma`)
| Tempo | Passo |
|---|---|
| 2 min | Você define objetivo e quanto aceita perder |
| 3 min | Conecta sua conta com chave **sem permissão de saque** |
| 5 min | Liga a sua IA (Claude, ChatGPT ou a que já usa) |
| 10 min | Sobe em simulação. Vai a real só quando você mandar |

"A primeira ordem sai quando aparecer sinal — pode ser no mesmo dia, pode demorar." Os
estudos já vêm instalados. Minerar estratégias novas "roda em horas, não em minutos". O
painel de exemplo mostra: tamanho da posição calculado pela liquidez medida · risco do dia
0,07% de 2,0% permitidos · aderência 50,00% contra 50,08% previsto · diário com 418 ciclos de
análise e 3 decisões.

---

## Aula 04 — O que você pode pedir e como você vê

**Fonte:** ORIGINAL — `/plataforma`

### As skills da plataforma
"Você escreve em português. Ela chama a ferramenta, mede e responde com o dado atrás — nunca
de cabeça."

| Skill | O que faz (original) |
|---|---|
| **Diagnóstico de risco** | Quanto você está arriscando de verdade (por operação, no dia e no portfólio inteiro) contra o limite que você definiu |
| **Explica a estratégia** | Mostra no gráfico onde ela entra, onde protege e onde sai, e explica "como se você nunca tivesse operado" |
| **Pesquisa de estratégia** | Mede o regime do mercado, roda o preflight e minera dentro do seu perfil e capital. Volta com estatística em janela selada |
| **Teste de estresse** | Monte Carlo sobre a sequência de operações e custo de execução dobrado, "antes do dinheiro entrar, não depois" |
| **Aderência ao vivo** | O previsto contra o realizado, linha por linha, enquanto a conta opera |

### "A tela é sua": três formas de ver a mesma informação
| Para quem | Forma | Exemplo do site |
|---|---|---|
| **Trader experiente** | O terminal: candles, médias, VWAP, volume e oscilador | acerto 50,0% · payoff 3,09 · custo/ordem 0,055% |
| **Está aprendendo** | O diário: cada decisão e o motivo, em português | "14:32 comprou HYPE · o gatilho tocou" · "recusou TAO · ordem pequena demais" · "recusou DOGE · já tem 5 setups no ativo" · "olhou 33 setups · 30 sem sinal" |
| **Não quer nem pensar** | Um personagem que avisa | "Olhei tudo. Nada pra fazer — as duas posições estão com stop no servidor." |

### A prova: "ela presta contas do que prometeu"
| Métrica | Previsto | Ao vivo |
|---|---|---|
| Taxa de acerto | 50,08% | 50,00% |
| Ritmo de operações | 15,0/dia | 4,0/dia |
| Risco consumido | 13,2% | 0,01% |

"Leitura de comportamento, não de retorno. Valores ilustram o formato do painel."

---

## Aula 05 — Preparar e ligar o conector

**Fonte:** ORIGINAL — `/claude/manual` (seções 0 a 4), `/claude/marketplace.json`

### O caminho inteiro, em uma olhada
| Etapa | O que você faz | Tempo |
|---|---|---|
| 1 | Liga o conector no seu Claude | 2 min |
| 2 | Pergunta "o que é o AlgoMaker?" | 1 min |
| 3 | Liga o motor: instala o `uv` e o agente roda os comandos | 5 min |
| 4 | Fecha e abre o Claude | 10 s |
| 5 | Diz o perfil e pede uma carteira | minutos a horas |
| 6 | Dinheiro real: compra, ativa a chave, cadastra a corretora e confirma o LIVE numa tela | 5 min |

"Tudo até a etapa 5 é grátis. A licença só entra na 6."

### O que é grátis e o que pede licença
| Grátis, sem cadastro | Pede licença |
|---|---|
| Baixar dados históricos | Operar com dinheiro real (modo live) |
| Minerar estratégias | Exportar o código da estratégia (.mq5 / Python) |
| Testar robustez (walk-forward, Monte Carlo, estresse de custo) | Exportar arquivos .alg |
| Montar carteira e medir correlação | |
| Simular em papel (preço real, ordem simulada) | |
| Desenhar/simular um grid para o bot gratuito da corretora (doutrina do plugin) | |

### O que você precisa ter
- Claude com plano **Pro ou Max**: app de desktop (Mac ou Windows), claude.ai ou Claude Code.
  O uso sai da sua assinatura do Claude e não tem custo de API.
- **Windows 10/11 ou macOS.** Linux funciona pelo terminal.
- Para minerar: **4 núcleos e 8 GB de RAM** no mínimo.

### Etapa 1a — Claude Desktop ou claude.ai
1. **Configurações → Conectores → Adicionar conector personalizado.**
2. Preencha:

| Campo | O que colocar |
|---|---|
| Nome | `AlgoMakers` (é só o rótulo) |
| URL do servidor MCP remoto | `https://algomakers.com/mcp` |
| Autenticação | **Nenhum.** O Claude marca "Detectado" sozinho |
| Cabeçalhos de requisição | Vazio. Não há chave de API nesta etapa |
| Avançada | Não mexa |

3. O aviso laranja ("Sem credenciais, qualquer pessoa com acesso à URL poderá usar este
   conector") "é verdade e é proposital": este conector só orienta. Ele não confere licença,
   não executa nada e não vê seus dados.
4. **Adicionar.** Abra uma conversa nova e confira que o AlgoMakers está ligado.
5. Pergunte **"O que é o AlgoMaker?"**. Se o Claude pedir permissão para usar a ferramenta,
   pode "Permitir sempre": as três ferramentas desta etapa só devolvem texto.

### Etapa 1b — Claude Code
```
/plugin marketplace add https://algomakers.com/claude/marketplace.json
/plugin install algomaker@algomakers
```
Confirme que confia no marketplace e escolha o escopo **usuário**. Confira com `/mcp`. Devem
aparecer `algomaker-onboarding` e `algomaker-motor`; o motor depende do `uv` (Aula 06).

O plugin (versão 1.4.26 quando foi lido) traz três coisas: o **conector remoto** (3
ferramentas: o que é, como instalar, como a licença funciona), o **motor** (cerca de 41 a 47
ferramentas, conforme a versão: dados, minerar, validar, compor carteira, simular em papel,
ativar licença) e a **skill de doutrina** (Aula 13).

### Etapa 2 — A conversa de orientação
O Claude ainda não minera. Ele conduz você para a instalação. Frases que funcionam:
- "Como instalo no Windows?" / "Como instalo no Mac?": o próprio agente roda os comandos.
- "Preciso pagar para testar?": não; ele explica o que é grátis.
- "Já tenho uma chave de licença": ele guarda para a hora certa e manda instalar primeiro.

---

## Aula 06 — Ligar o motor e abrir o painel

**Fonte:** ORIGINAL — `/claude/manual` (seções 5 e 6)

"Não existe aplicativo para baixar." Em Windows, Mac e Linux instala-se só o **motor**, pelo
`uv`, e a tela é o **painel** que ele serve no navegador. O antigo programa de janela do
Windows foi descontinuado: se você ainda o tem, feche e não abra mais.

> Os comandos abaixo estão como no manual quando ele foi lido (motor `0.0.184`). **A versão
> muda.** O jeito mais seguro é pedir ao Claude "instala o AlgoMaker nesta máquina" e usar o
> que ele devolver.

### Windows (inclui Windows Server/VPS), no PowerShell
Instale o `uv` (uma vez só, não pede administrador):
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Aqueça o motor (1 a 3 minutos na primeira vez) e registre-o no Claude:
```
& "$env:USERPROFILE\.local\bin\uvx.exe" --python 3.11 --from https://algomakers.com/claude/mm_engine-0.0.184-cp311-none-any.whl mm-engine --aquecer
& "$env:USERPROFILE\.local\bin\uvx.exe" --python 3.11 --from https://algomakers.com/claude/mm_engine-0.0.184-cp311-none-any.whl mm-engine --conectar-claude
```
Se você usa o app de chat do Claude (e não o Claude Code), acrescente `--desktop` na segunda
linha.

### macOS e Linux, no Terminal
Se nunca instalou o `uv` (depois feche e abra o Terminal):
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Depois:
```
claude mcp add algomaker -- uvx --python 3.11 --from https://algomakers.com/claude/mm_engine-0.0.184-cp311-none-any.whl mm-engine --mcp
```

### Claude Code com o plugin
O plugin já traz o motor. Só falta o `uv`. Se `algomaker-motor` aparecer como falho em
`/mcp`, o `uv` não está no caminho: feche o Claude por completo e abra de novo. Se persistir
no Mac, rode a linha do macOS acima.

### Claude Desktop no Mac, sem o Claude Code
**Configurações → Desenvolvedor → Editar configuração** abre o `claude_desktop_config.json`.
Acrescente:
```
{
  "mcpServers": {
    "algomaker": {
      "command": "uvx",
      "args": ["--python", "3.11", "--from",
        "https://algomakers.com/claude/mm_engine-0.0.184-cp311-none-any.whl",
        "mm-engine", "--mcp"]
    }
  }
}
```

### Onde ficam os dados
`%APPDATA%\@mm\desktop` (Windows) · `~/Library/Application Support/AlgoMaker` (Mac) ·
`~/.local/share/algomaker` (Linux).

### O painel
Diga **"abre o painel"**. Abre no navegador uma página em `http://127.0.0.1:…`, servida pelo
motor na sua máquina, sem nada na internet. O link "serve uma vez e vence em 5 minutos".
- Telas: **Início, Construtor, Databank, Fábrica, Monitor, Configurações**. No canto superior
  direito, `engine pid:…` mostra o motor rodando.
- É no painel que você faz o que o agente não pode: cadastrar a chave da corretora, armar
  dinheiro real e fechar posição.
- O painel "é um processo que fica": fechar o Claude não o derruba, e os robôs em papel ou
  LIVE continuam. A mesma chamada liga o arranque automático (volta quando o computador
  reinicia).
- Se o link disser "já foi usado" sem você ter aberto, "estranhe e peça outro".

### Etapa 4 — Fechar e abrir o Claude
"Este passo não é opcional — é o que mais gente esquece." O Claude só lê a lista de
conectores ao iniciar. Feche por completo (Mac: ⌘+Q; Windows: ícone da bandeja → Sair) e abra.
Para conferir, pergunte **"qual é o status da minha licença?"**. A resposta vem do motor:
plano **free** e o identificador da máquina.

---

## Aula 07 — O mandato e a primeira carteira

**Fonte:** ORIGINAL — `/claude/manual` (seção 7), skill do plugin

### O mandato vem primeiro, e é proposital
"Diga as quatro coisas":
```
Meu capital é 10 mil dólares, aguento 20% de queda, quero crescimento,
horizonte de 6 meses.
```
Depois:
```
Monta uma carteira pra mim.
```
A doutrina do plugin define as opções: objetivo "crescimento" ou "consistência". "Sem perfil
a fábrica não minera."

### O que acontece, na ordem
1. **Destino:** ele pergunta onde você vai executar, pela Bybit (robô no app) ou por um robô
   `.mq5` (mesas tipo FTMO). "Isso muda os dados, o custo e o tipo de ordem — não é detalhe."
2. **Dados:** baixa o necessário (minutos).
3. **O porteiro:** mede se cada ativo tem liquidez para o seu lote. Se não tem, recusa e diz
   o número. "Isso é o produto funcionando."
4. **Mineração:** minutos a horas, conforme o processador, validando em **três fatias de
   tempo**. A última é "um trimestre selado que nada influenciou".
5. **Carteira:** monta, mede correlação e põe em **simulação com preço real** (papel).

> "Espere recusas. O funil descarta mais de 99% das candidatas. Poucas e sólidas é o objetivo."

---

## Aula 08 — Acompanhar a carteira

**Fonte:** ORIGINAL — `/claude/manual` (seção 8), skill do plugin

Pergunte **"Como está minha carteira?"**. "Três números que valem mais que a curva de capital":

| Número | O que mostra (original) |
|---|---|
| **Retorno sobre o capital em risco** | Quanto rendeu sobre o que estava de fato posicionado, não sobre a conta inteira. "É o que separa 'pequena e boa' de 'pequena e perdendo'" |
| **Ocupação** | Quanto do tamanho projetado está no mercado. Se o modelo pede posição e a corretora não tem, o agente avisa: "é ordem que não está entrando" |
| **Bloqueios da corretora** | Recusas que exigem ação sua (termos de contrato, restrição regulatória, chave sem permissão), já com a ação escrita |

A doutrina do agente manda ler os três **antes** de concluir que a carteira está
"conservadora". A ocupação compara desenho, modelo e corretora: um `gap_execucao_pct` alto
significa ordem que não entra.

Para comparar o previsto com o ao vivo e escolher a forma de visualização, veja a Aula 04.

---

## Aula 09 — Grid no bot gratuito da corretora

**Fonte:** ORIGINAL — skill do plugin (quarta frase)

"Quero rodar um grid em SOL." Um **grid** compra e vende em degraus dentro de uma faixa de
preço.
- `grid_desenhar` mede a faixa no histórico e dimensiona a escada.
- `grid_simular` responde perguntas como "e se eu apertar a faixa?".
- A Bybit não expõe os bots dela por API: **você digita** faixa, grades e capital no bot
  gratuito da corretora.
- Leia `fora_da_faixa` **antes** do lucro: o grid ganha oscilando dentro da faixa e perde
  quando o preço sai dela.
- Desenhar e simular grid é grátis.

A doutrina também registra que entradas por ordem limite/stop rodam ao vivo desde a versão
0.0.150 do motor.

---

## Aula 10 — Licença, corretora e dinheiro real

**Fonte:** ORIGINAL — `/claude/manual` (seção 9), `/plataforma`, `/termos`

### Preço (como publicado em 2026)
**R$ 497 à vista ou 12× R$ 51,40**, licença de **12 meses**. "Não é assinatura que renova
sozinha." Ao fim, você decide se renova. **7 dias para desistir.** Também existe a opção
"para parceiros e instituições" (instalação por cliente, mesa própria ou estrutura de
captação), "sob conversa", com triagem.

### 1. Comprar
Ao pedir "põe ao vivo", o motor recusa e responde com `algomakers.com/comprar`. A chave chega
por e-mail (support@algomakers.com), no formato `MM-…`.

### 2. Ativar
Cole no chat: **"Ativa a licença: MM-XXXX-XXXX-…"**. O agente valida e responde "A licença
ficou travada NESTA máquina". O motor "renasce como PRO". A chave vale para uma máquina; para
trocar, fale com o suporte. "O agente nunca adivinha, gera ou completa uma chave."

### 3. Cadastrar a corretora: só você, numa tela
No painel: **Configurações → Conexões → Nova conexão** (nome, chave de API e segredo da
Bybit). A chave é digitada **na página, nunca no chat**. Precisa de permissão de negociação
(Contract/Derivatives). Sem IP fixo, vence em **90 dias**, e o agente avisa 14 dias antes. Em
servidor (VPS), o agente prepara o envio e você confirma numa página local. "O agente não pode
gravar chave de corretora por conta própria: essa rota é bloqueada por construção."

### 4. Armar o LIVE
O agente prepara carteira, tamanhos e stops, mas **não arma sozinho**.
- **No painel:** Monitor → **Armar LIVE**. Uma janela pede confirmação e um segundo fator.
  Na primeira vez, pergunta se você quer participar da inteligência coletiva; recusar não
  tira nada.
- **Mac com servidor (VPS):** o agente abre uma página local com o que vai ser armado. Você
  lê e clica em **Confirmar e armar**. A página vale poucos minutos e serve uma vez só.

"A partir daí os robôs operam. Parar tudo o agente pode (kill-switch). Destravar é só você."
Para operar com o computador desligado, o caminho é um servidor (VPS).

### Perguntas frequentes (original, `/plataforma`)
| Pergunta | Resposta |
|---|---|
| O que ele faz sozinho? | Roda em ciclos: atualiza dados, lê cada setup, calcula o tamanho pela liquidez, confere o limite de risco e arma, ou recusa dizendo o motivo. Tudo registrado |
| E se eu desligar o computador? | Stop e alvo ficam na corretora como ordens próprias. A proteção continua; para a abertura de novas operações |
| Como sei que a IA não está inventando? | Ela não responde de cabeça: chama ferramentas que leem os dados e devolvem número |
| Preciso pagar uma IA separada? | Sim (Claude, ChatGPT ou outra compatível), pela sua assinatura ou chave de API. "Não vendemos inteligência" |
| Nunca operei. Serve pra mim? | Você não vai analisar gráfico, mas vai acompanhar e decidir. "Quem quer entregar e nunca mais olhar não deve comprar" |
| É mensalidade? | Não. Licença de 12 meses |

"Comece pequeno. Aumente quando quiser." A página diz que há ativos em que a corretora aceita
ordem com cerca de **seis dólares** de margem (o "começa com ~US$ 6").

> **Dos Termos de Uso:** definir um limite de perda tolerada no aplicativo "não faz a
> Plataforma ajustar tamanhos sozinha para respeitá-lo". Esse alvo se atinge na composição e
> no dimensionamento que você escolhe.

---

## Aula 11 — Problemas comuns

**Fonte:** ORIGINAL — `/claude/manual` (seção 10)

| Sintoma | Causa e solução |
|---|---|
| O Claude só tem ferramentas `algomaker_*` | O motor não está ligado ou o Claude não foi reiniciado. Peça "instala o AlgoMaker nesta máquina" e reinicie |
| Na janela do conector, "Autenticação" não mostra "Detectado" | URL errada. Tem que ser exatamente `https://algomakers.com/mcp` |
| Alguém mandou baixar um instalador `.exe` | Não existe mais. Instala-se só o motor; a tela é o painel no navegador |
| `uvx: command not found` | Instale o `uv` e feche e abra o Terminal |
| "porteiro recusou a campanha" | O ativo não tem liquidez para o seu lote, ou o dado é insuficiente. Ajuste capital, ativo ou timeframe |
| Mineração salvou zero | Normal em campanhas curtas. Aumente população/gerações ou troque de ativo. "Zero salvo com motivo escrito é melhor que dez estratégias ruins" |
| Ordem recusada "regulatory restrictions" (10024) | A corretora bloqueou a conta neste contrato. O agente para de insistir e mostra a ação (suporte da Bybit com o UID). Fechar posição continua permitido |
| Chave de API "invalid" | Venceu, foi revogada ou é de outra entidade regional. Gere outra e cadastre de novo |
| A página de confirmação diz "expirou" | Vale poucos minutos. Peça outra |
| Instalei versão nova e os robôs pararam | Instalar reinicia o app; os robôs em live não voltam sozinhos. Abra o Monitor e relance |

"Dúvida em qualquer passo: pergunte ao próprio Claude." Suporte humano: support@algomakers.com.

---

## Aula 12 — O funil cético

**Fonte:** ORIGINAL — `/comprar`, `/`, `/algomakerquiz`

### As quatro perguntas
"Quatro perguntas. Quase nada passa das duas primeiras."
1. **Ela funciona onde nunca olhou?** A estratégia é mantida longe de um pedaço do histórico.
   "Se ela só acerta no trecho que usou para se montar, ela decorou — e é aqui que a maioria cai."
2. **Ela aguenta um mercado diferente?** "Nenhum teste prevê o futuro." Dá para saber se o
   resultado sobrevive quando você mexe nos próprios números dela.
3. **O que segura a queda?** O limite de perda por operação e no dia é escrito antes, e a
   ordem de proteção fica na corretora, "não no seu computador".
4. **E em que ordem ela é peneirada?** "Primeiro o trecho que ela nunca viu, depois a mudança
   nos números, por último o custo — refeito mais caro do que a sua corretora cobra de
   verdade. Quase tudo cai no primeiro degrau."

### Os termos, em português claro
| Termo | O que é |
|---|---|
| **Fora da amostra / janela selada** | Testar em dados que não foram usados para criar a estratégia |
| **Walk-forward** | Ajustar num período, testar no seguinte, avançar a janela e repetir |
| **Monte Carlo** | Sortear a sequência de resultados milhares de vezes para ver o pior caso plausível |
| **Estresse de custo** | Refazer a conta com custo maior que o real (na skill da plataforma: "custo de execução dobrado") |
| **Porteiro / pré-voo** | Recusar antes de gastar processamento, dizendo por que daria zero |

### O que o questionário ensina sobre padrões (original, `/algomakerquiz`)
O questionário pede para marcar em quais padrões você "já acreditou". São as famílias de
estratégia que o funil testa:

| Família | Como o site descreve |
|---|---|
| Reversão | "Esticou demais e volta." "Quando sobe rápido demais, costuma voltar." |
| Rompimento | "Escapou da faixa e continua." "Preço parado por muito tempo acaba explodindo pra algum lado." |
| Seguimento de tendência | "Já está andando — vai junto." "Nadar contra a maré sai caro na maioria das vezes." |
| Tempo passando | "Dá pra ganhar só com o tempo passando, sem acertar direção." |
| Calendário | "Começo e fim de mês se comportam diferente do resto." "A primeira e a última hora do dia não são iguais ao meio." |
| Volatilidade | "Depois de um período calmo costuma vir um agitado." "Dá pra ganhar com a agitação sem adivinhar a direção." |
| Pares | "Dois ativos parecidos que se separam voltam a se juntar." |

"Escolher mais de um reduz a chance de tudo quebrar no mesmo dia."

### Risco contra retorno (original, `/algomakerquiz`)
| Escolha | Consequência |
|---|---|
| Arrisco 1 pra tentar ganhar 1 | Precisa acertar mais da metade das vezes |
| Arrisco 1 pra tentar ganhar 2 | Pode errar mais do que acerta e ainda fechar no azul |
| Arrisco 1 pra tentar ganhar 3 ou mais | Erra muito, acerta pouco, mas acerta grande |

E sobre o valor da primeira operação: "abaixo de certo valor o custo de operar come qualquer
resultado — e o funil precisa saber disso pra não te aprovar uma estratégia que não cabe no
seu bolso".

---

## Aula 13 — Contenção, frota e a doutrina do agente

**Fonte:** ORIGINAL — `/` (institucional), skill do plugin, `/privacidade`

### "Autonomia é a parte fácil. O produto é a contenção."
"Qualquer coisa pode ser automatizada. O que importa numa mesa é o que o sistema se recusa a
fazer, e o que ele registra enquanto faz o resto."

| Controle | Descrição original |
|---|---|
| **Portão humano** | Armar capital real e cadastrar chaves de corretora são ações humanas na tela. "O agente prepara, monitora e desliga — ele não se liga sozinho" |
| **Recusa por projeto** | Sem mandato (capital, queda máxima tolerada, objetivo, horizonte), o funil se recusa a rodar |
| **Pré-voo** | As campanhas são conferidas contra restrições medidas antes de consumir horas de processamento, e o sistema informa por que uma configuração devolveria zero |
| **Chave de corte** | Parada e encerramento forçado são operações de primeira classe, chamáveis independentemente do que o agente esteja fazendo |
| **Local primeiro** | O detalhe fica na máquina do operador. Só saem agregados derivados e anônimos |
| **Honestidade de custo** | "A tabela de taxa e slippage usada na pesquisa é a mesma que o executor cobra ao fechar. A pesquisa não pode ser mais barata que a realidade" |

### Inteligência de frota
"O dado que importa não é o histórico. É o que aconteceu depois." O histórico de preço é
igual para todos. O raro é o par: "o genoma que a máquina propôs e o que executá-lo custou de
verdade, ativo por ativo".

| Princípio | Original |
|---|---|
| **Medido, não presumido** | Slippage, spread e custo realizado vêm de execuções reais na frota, por ativo e por corretora |
| **Só agregado** | Só percentuais anônimos saem, e apenas com fontes independentes suficientes para não identificar ninguém. Posição, saldo, estratégia e chave nunca viajam |
| **Ele aperta o portão** | O custo medido vira um prior no pré-voo. "Uma estratégia que só sobrevive com premissa otimista de execução deixa de ser aprovada" |
| **Visível, não opaco** | A população é inspecionável: famílias de estratégia, indicadores em comum, amostra, e onde o ao vivo diverge do teste |

Pela política de privacidade, a participação é opcional e pedida uma vez antes do primeiro
LIVE. No mesmo consentimento, o app também envia o **total de volume negociado**, nunca ordem
a ordem. Recusar não tira nenhuma função.

### A doutrina do agente (skill pública do plugin)
**Em que passo ele está:** se só existem ferramentas `algomaker_*`, o motor não está ligado
e o agente deve instalar. Se existem `mine_preflight`, `portfolio_estrutura`,
`licenca_status` e `exec_status`, o motor está instalado.

**As quatro frases que iniciam tudo:**
1. **Perfil:** capital, queda aceita, crescimento ou consistência, horizonte (`perfil_set`).
2. **Carteira:** perguntar o destino (`bybit_api` ou `mt5`) e então `mine_preflight` →
   `mine_strategies` → `portfolio_run` → `deploy_paper`.
3. **Acompanhamento:** `exec_status`, lendo retorno sobre risco, ocupação e bloqueios.
4. **Grid:** `grid_desenhar` e `grid_simular` (Aula 09).

**O que o agente NUNCA faz, "por arquitetura, não por promessa":** armar LIVE, cadastrar
chave de corretora, mexer nas travas de risco, destravar kill-switch, enviar ordem por conta
própria "mesmo de teste". Encerrar tudo em emergência **pode** (`exec_kill`).

**Honestidade > promessa:** a fábrica recusa campanha que produziria lixo, com o motivo em
números. Mais de 99% são descartadas. "Simule antes de armar." Em respostas grandes, o agente
pede só os campos necessários; `_omitido` quer dizer que o dado existe e foi cortado, não
que falta.

**O "chip":** a doutrina completa (entrevista do mandato, regime por ativo, universo medido,
preset, funil, composição, validade, travas, checkpoint, troca de safra e rotina) é servida
pelo próprio motor instalado, pela ferramenta `chip`. Ela não está neste curso.

**O painel:** `painel_abrir` sobe o painel, liga o arranque automático e abre o navegador. O
agente nunca abre o link nem pede chave no chat. A resposta traz `pendencias` (licença,
mandato, corretora), que são o próximo passo.

---

## Aula 14 — Para quem é, para quem não é, e as regras do jogo

**Fonte:** ORIGINAL — `/` (institucional), `/plataforma`, `/termos`, `/privacidade`, `/contato`

### "Mesas que já acreditam no processo, não na previsão"
| Público | Descrição original |
|---|---|
| **Já é instituição** | Mesas proprietárias, family offices, gestoras sistemáticas e times de tecnologia em instituições financeiras. "O mandato e o capital você já tem" |
| **Está virando uma** | Operadores tocando o próprio livro com intenção de captar. "O que separa você de um fundo raramente é a estratégia — é o registro." A pilha produz esse registro como subproduto de operar |
| **Para quem isto não é** | "Se você procura sinal, conta gerida ou retorno alvo, esta é a porta errada — e é melhor saber agora." Não assessoram, não recomendam ativos, nunca custodiam |

O formulário de contato oferece estas categorias: mesa proprietária, family office, gestor
sistemático, construindo histórico, imprensa, parceria, outro. Parceiros citados na
plataforma: **Zenite Ventures** e **Bybit** (execução).

### Termos de Uso (pontos principais)
- A AlgoMaker é **provedora de tecnologia**. Não é consultora, gestora, corretora,
  custodiante nem instituição financeira.
- IA "erra, e o erro pode causar prejuízo financeiro"; a mesma entrada pode gerar saídas
  diferentes.
- Chaves e credenciais são suas e ficam na sua máquina.
- **Não prometem rentabilidade.** O dimensionamento para um alvo de queda **não é automático**.
- Licença pessoal e intransferível: é vedado copiar, redistribuir ou descompilar. "As
  estratégias que você gera com a Plataforma são suas."
- **Rebate das corretoras:** declarado "em linha com o espírito da Resolução CVM 179".
- **Uso aceitável:** proibido usar para manipulação de mercado, "operação em nome de terceiros
  sem habilitação legal" ou serviço que exija autorização regulatória que você não tem.
- Responsabilidade limitada ao valor pago nos 12 meses anteriores, ressalvado o Código de
  Defesa do Consumidor. Lei brasileira; o texto em português prevalece.

### Privacidade (pontos principais)
Dados, estratégias, carteiras e chaves ficam na sua máquina. Saem apenas a ativação da
licença (chave + identificador da máquina) e, se você consentir, percentuais anônimos e o
total de volume. O conector remoto recebe só o que você digitar ao chamá-lo e não guarda
histórico. O link de abertura de conta na corretora é parceria remunerada, e a ferramenta
avisa isso na mesma resposta.

---

## Aula 15 — A mesa comercial da HN operada por agentes

**Fonte:** ADAPTAÇÃO HN — não existe no AlgoMaker.

> **Original em que se baseia:** os cinco postos e as cinco estações (Aula 02), o mandato
> (Aula 07) e o portão humano (Aula 13). No AlgoMaker, isso tudo é sobre **operar mercado
> financeiro**.

### Os cinco postos, traduzidos para a área comercial
| Posto original | Posto na HN | O agente faz | Entrega |
|---|---|---|---|
| Macro | **Inteligência de mercado** | Lê sazonalidade, concorrência, calendário do cliente | Quanto da verba pode estar exposto no mês |
| Quant | **Hipóteses de campanha** | Transforma ideia em teste com período selado | Variantes aprovadas/reprovadas com motivo |
| Programador | **Automação** | Escreve integrações, relatórios, scripts | Código versionado e conferível |
| Risco e compliance | **Verba, marca e LGPD** | Confere cada ação contra o mandato | Recusa com motivo, nunca exceção |
| Execução | **Operação de mídia e CRM** | Prepara publicação, segmentação, cadência | Tudo pronto para o humano aprovar |

### O mandato comercial
| Original (Aula 07) | HN |
|---|---|
| Capital | Verba mensal e verba máxima por teste |
| Queda máxima tolerada | CPA máximo (teto de custo por conversão) |
| Crescimento ou consistência | Objetivo (reunião, venda, cadastro) |
| Horizonte | Horizonte de avaliação |

Modelo: `algomaker/modelos/mandato.json`. Guia de preenchimento:
`algomaker/modelos/mandato-comercial.md`.

### O que o agente da HN nunca faz
| Original (Aula 13) | HN |
|---|---|
| Armar LIVE | Gastar ou aumentar verba |
| Cadastrar chave de corretora | Publicar anúncio, enviar mensagem a clientes/leads |
| Mexer nas travas de risco | Mudar preço, oferta ou contrato |
| Encerrar em emergência: **pode** | Recomendar pausa do que saiu do mandato: **pode** |

---

## Aula 16 — O funil de campanhas da HN

**Fonte:** ADAPTAÇÃO HN — não existe no AlgoMaker.

> **Original em que se baseia:** o funil cético (Aula 12) e a pilha de pesquisa (Aula 03).
> No AlgoMaker, o funil filtra **estratégias de trading** com janela selada, mudança de
> parâmetros (robustez), Monte Carlo e custo mais caro.

### A tradução dos portões
| Portão original | Portão na HN |
|---|---|
| Porteiro (liquidez para o lote) | **Amostra mínima** de conversões nos dois períodos |
| Fora da amostra (trimestre selado) | **Período selado**: CPA dentro do teto e conversão sem desabar |
| Monte Carlo | **Probabilidade** de o CPA real ficar dentro do teto |
| Custo mais caro que o real | **CPA com custo +25%** continua dentro do teto |

O **período selado**: separe as últimas semanas da campanha e não use esse pedaço para
decidir nada durante o ajuste. Variante que só funcionou no período em que foi otimizada
"decorou" o público.

### Rodando (ferramenta testada)
```
python3 algomaker/ferramentas/funil_campanhas.py algomaker/modelos/exemplo-campanhas.csv --cpa-max 80
```
Resultado real com os dados de exemplo:
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
Os dados de exemplo e o teto de R$ 80 são fictícios, só para ensinar. A `promocao-relampago`
tem o melhor CPA no treino (R$ 40) e o pior no selado (R$ 95). Sem o período selado, seria a
primeira a receber verba.

Ajustes: `--min-conversoes 30` · `--queda-max 0.30` · `--prob-min 0.80` · `--estresse 1.25`.
Defina **antes** de rodar. Mudar a régua depois de ver o resultado é decorar.

---

## Aula 17 — Previsto contra realizado e o diário de decisões

**Fonte:** ADAPTAÇÃO HN — não existe no AlgoMaker.

> **Original em que se baseia:** a prova "ela presta contas do que prometeu" e a
> aderência ao vivo (Aula 04), o diário em português (Aula 04) e a leitura de desvio
> (Aula 03).

### O painel de aderência da HN
Toda variante aprovada sai do funil com um **previsto**. Quando a verba escala, compare toda
semana:

| Métrica | Previsto (selado) | Realizado (escala) | Leitura |
|---|---|---|---|
| CPA | R$ 46,67 | R$ 51,20 | dentro do teto, +10% |
| Taxa de conversão | 4,6% | 4,3% | estável |
| Conversões/semana | 24 | 21 | ocupação 88% |

*(números fictícios)* Se o realizado se afasta do previsto, algo mudou (público saturou,
concorrência, oferta cansou). Modelo: `algomaker/modelos/painel-aderencia.md`.

### O diário de decisões
No original, o diário mostra "14:32 recusou — TAO · ordem pequena demais". Na HN, cada
decisão (escalar, pausar, reprovar) é registrada com motivo e números.

---

## Aula 18 — Montando a mesa da HN com Claude Code

**Fonte:** ADAPTAÇÃO HN — não existe no AlgoMaker.

> **Original em que se baseia:** a arquitetura do plugin (Aulas 05 e 13). Um conector com as
> funções, uma skill com a doutrina, e as ações perigosas sem rota nenhuma.

### Camada 1: a doutrina (skill)
`.claude/skills/mesa-comercial-hn/SKILL.md`: mandato antes de ação, funil antes de verba,
portão humano e registro de tudo. O Claude Code carrega sozinho neste repositório.

### Camada 2: as funções (servidor MCP)
| Ferramenta | O que faz |
|---|---|
| `mandato_ler` | Lê objetivo, verba, CPA máximo e o que exige aprovação humana |
| `funil_avaliar` | Passa as variantes pelos 4 portões e **recusa se não houver mandato** |
| `diario_registrar` | Grava a decisão com motivo e números |
| `diario_ler` | Lê as últimas decisões |

De propósito, **não existe** ferramenta para gastar verba, publicar ou enviar mensagem.
```
pip install mcp
claude mcp add mesa-hn -- python3 algomaker/ferramentas/mcp_mesa_hn.py
```
Reinicie o Claude Code e confira com `/mcp`.

> **Testado:** com um cliente MCP real, o servidor listou as 4 ferramentas, aprovou 2 de 7
> variantes, gravou e leu o diário, e recusou rodar quando o mandato foi removido.

### Camada 3: próximos passos
Novas funções, uma de cada vez e sempre com trava: `relatorio_meta_ads(periodo)` (só
leitura), `crm_leads(desde)` (só leitura), `pausar_variante(id)` (parar é permitido, como a
chave de corte). Ligar verba nunca entra.

---

## Bônus 01 — O funil de vendas do AlgoMaker

**Fonte:** ORIGINAL (cada item) + ADAPTAÇÃO HN (as caixas "Para a HN")

### 1. Uma página para cada público (original)
| Página | Público | Tom |
|---|---|---|
| `/` em 5 idiomas | Mesas, family offices, gestoras | Técnico, cético: "veja o funil reprovar" |
| `/comprar` | Quem investe e não programa | "Um escritório onde quem opera são agentes" |
| `/plataforma` | Quem já decidiu | Preço, "no ar em 20 minutos", perguntas frequentes |

> **Para a HN (adaptação):** a mesma oferta contada de três jeitos, para três níveis de consciência.

### 2. "Para quem isto não é" (original)
Veja a Aula 14. Desqualificar abertamente é parte da venda.

> **Para a HN (adaptação):** dizer com clareza que cliente a HN não atende.

### 3. O questionário de entrada (original, `/algomakerquiz`)
"Quero construir meu escritório de IA. São 4 perguntas e leva uns 4 minutos. Eu leio cada uma
e, se fizer sentido, te chamo para uma conversa. Nada é cobrado nessa etapa."

As perguntas que aparecem no código da página:
1. Qual agente de IA você já usa? ("O laboratório se conecta ao agente que você já paga.")
2. O que melhor descreve você? (Opero na mão: decido cada entrada olhando o gráfico · Programo minhas estratégias · Sei programar, mas não opero · Vim entender do que se trata)
3. O que você gostaria de operar? (vários mercados ou "Ainda não sei")
4. Quanto você imagina colocar na primeira operação? (mínimo possível · só simulação)
5. Quando você entra numa operação, o que espera? (risco 1 para 1, 2 ou 3, ou "Nunca pensei nisso")
6. O que você tem hoje? (ideia nunca testada · robô em que não confia · ideias soltas · nada ainda)
7. O que te trava hoje? (não sei se é real ou sorte · não sei programar · já perdi com robô de papel · sem onde testar · não sei quanto risco tomar · sem tempo de tela)
8. Que tipo de padrão te interessa / em quais você já acreditou? (Aula 12)

No fim, o site avisa que "a maioria vai ser reprovada", "inclusive as minhas", e que
"descobrir isso aqui custa dois minutos de máquina — descobrir na conta real custa
dinheiro". Ele também mostra como o funil funciona dentro do agente escolhido.

> **Para a HN (adaptação):** um questionário que ensina enquanto qualifica, para cada cliente.

### 4. O diagnóstico do custo de tentar sozinho (original, `/diagnostico`)
"Quanto custa continuar tentando resolver sozinho?" Há um vídeo de 3 minutos ("vídeo em
breve" quando foi lido), e depois 5 blocos:
1. Nome, WhatsApp, e-mail, fonte de renda, quanto entrou nos últimos 3 meses ("é o que
   transforma o diagnóstico em número") e com quem divide a decisão.
2. Objetivo: investir, carreira ou os dois (deal ou job).
3. O que trava: programador que não entrega, falta de conhecimento, de código, de validação,
   de manutenção. No pessoal: tempo, emocional, capital.
4. Como tentou resolver: copy/sinal, sala de sinais, dinheiro com terceiros, "curso que
   comprei e não assisto", robô que não sei atualizar, "corujão com IA".
5. Horas por dia gastas e autorização de contato.

**Resultado:** "a conta do seu tempo" (custo estimado por ano), o que você usa e onde está o
gargalo. Depois você escolhe os turnos para uma conversa de cerca de 30 minutos com um
consultor que "já vai com o seu diagnóstico na mão". "Cada pessoa tem direito a uma sessão."
"Se não resolver, a gente te diz isso."

> **Para a HN (adaptação):** um diagnóstico comercial que calcula em reais quanto o cliente
> perde com lead não respondido, follow-up esquecido ou verba em criativo cansado.

### 5. A demonstração honesta (original, `/` e `/contato`)
"Veja o funil reprovar uma estratégia, ao vivo." "É uma primeira reunião mais honesta do que
uma curva de capital." Se o envio do formulário de contato falhar, a página não finge que
deu certo: mostra o que você escreveu e um e-mail para mandar ("Rather than tell you it
worked, here is what you wrote").

### 6. Transparência como posicionamento (original)
Aviso de risco em toda página. "Sem promessa de retorno. Sem taxa sobre o que você ganhar."
Parceria remunerada declarada e rebate declarado (Aula 14). Assinatura da página `/comprar`:
"© 2026 Fercama Consultoria · AlgoMaker · @ofercama · Máquinas Invisíveis".

---

## Bônus 02 — Riscos, ética e conformidade

**Fonte:** ORIGINAL (Termos e avisos) + ADAPTAÇÃO HN (onde marcado)

- **Original:** operar envolve risco real de perda, inclusive total. Nada é recomendação.
  Comece em simulação, depois com o mínimo.
- **Original:** chave de corretora nunca no chat e sem permissão de saque.
- **Original (Termos):** é proibido operar "em nome de terceiros sem habilitação legal".
  - **Adaptação HN:** por isso a HN **não deve operar o AlgoMaker em nome de clientes**.
    Gerir recurso de terceiros no Brasil exige autorização da CVM. A aplicação na HN é a
    arquitetura (Aulas 15–18), não a operação de mercado.
- **Adaptação HN:** dados de leads e clientes seguem a LGPD. Prefira agregados, como a
  "frota" do original.
- **Adaptação HN:** copie o rigor, não a promessa. Nada de "CPA garantido".
- **Original + HN:** se indicar ferramenta com comissão, diga isso junto, como o AlgoMaker faz.

---

## Os materiais que acompanham o curso

**Adaptação HN (criados para este curso):**
- **Mandato comercial:** `algomaker/modelos/mandato-comercial.md` e `algomaker/modelos/mandato.json`
- **Painel de aderência:** `algomaker/modelos/painel-aderencia.md`
- **Dados de exemplo (fictícios):** `algomaker/modelos/exemplo-campanhas.csv`
- **Funil de campanhas:** `algomaker/ferramentas/funil_campanhas.py`
- **Servidor MCP da mesa:** `algomaker/ferramentas/mcp_mesa_hn.py`
- **Doutrina para o agente:** `.claude/skills/mesa-comercial-hn/SKILL.md`

**Originais do AlgoMaker (no site):** manual do cliente em `algomakers.com/claude/manual`;
plugin em `algomakers.com/claude/marketplace.json`.

## Glossário rápido

- **Agente de IA:** IA que chama ferramentas e executa tarefas (Claude, Codex).
- **MCP:** padrão aberto que liga o agente a ferramentas externas.
- **Mandato:** objetivo, limite de perda/custo e horizonte escritos antes de qualquer ação.
- **Janela/período selado:** dados guardados que ninguém usa para decidir; servem de prova final.
- **Walk-forward:** ajustar num período, testar no seguinte e avançar.
- **Monte Carlo:** milhares de sorteios para ver o resultado plausível, não só o médio.
- **Estresse de custo:** refazer a conta com custo maior que o real.
- **Papel (paper trading):** operar com preço real e ordem simulada, sem dinheiro.
- **Grid:** compra e venda em degraus dentro de uma faixa de preço.
- **Portão humano:** ação que só um humano pode executar, numa tela.
- **Chave de corte (kill-switch):** parar tudo, a qualquer momento.
- **Aderência:** o realizado comparado ao que o teste previu.
- **Ocupação:** quanto do tamanho planejado está de fato no mercado.
- **CPA:** custo por aquisição (gasto ÷ conversões). *(adaptação HN)*

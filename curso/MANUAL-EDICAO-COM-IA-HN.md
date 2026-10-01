# Edição com IA — Curso HN

> Curso prático para a **HN Gestão Comercial e Marketing** editar anúncios e conteúdos
> dando comandos em português para uma IA. Da instalação às edições avançadas,
> mesmo para quem nunca editou.

---

## Como usar este manual

Este manual reconstrói, em formato de curso, o método apresentado publicamente em
`edicaomia.com.br` ("Máquina de Edição com IA", de Tiago Lemos), **adaptado para a
rotina da HN**. Ele foi escrito do zero a partir da página de vendas pública, da
transcrição do vídeo de apresentação e da análise dos vídeos de exemplo — **não é
cópia das aulas pagas**, que ficam numa área restrita. Onde a página não detalhava
o "como", o conteúdo foi completado com prática testada de verdade (os scripts em
`ferramentas/` foram executados e validados).

Siga as aulas em ordem. Cada uma tem: **objetivo**, **conceito**, **passo a passo**,
**comandos prontos** e **exercício aplicado à HN**.

| | Aula | Você sai sabendo |
|---|---|---|
| 01 | Ambiente pronto | Instalar Codex ou Claude Code e as ferramentas de vídeo |
| 02 | Seu primeiro projeto | Organizar a pasta para a IA acertar |
| 03 | Custos sob controle | Gastar pouco e não refazer à toa |
| 04 | O pedido certo | Escrever comandos que viram edição |
| 05 | Primeira edição | Cortar pausas e legendar automaticamente |
| 06 | Imagens com função | Inserir imagens no momento certo da fala |
| 07 | Motion explicativo | Fazer a fala virar interface animada |
| 08 | Variações para ads | Gerar várias versões de um anúncio |
| 09 | Revisar sem refazer | Corrigir só o trecho errado |
| 10 | Rotina de produção | Transformar tudo numa linha de produção semanal |
| B1 | Perspectiva e composição 3D | Camadas com profundidade |
| B2 | Recorte, moldura e lettering | Texto atrás de você, sem tela verde |

---

## A ideia central: você dirige, a IA edita

O método inteiro cabe numa frase: **você deixa de montar efeito por efeito e passa
a dizer, em português, o que quer ver na tela.** A IA constrói a edição.

Isso funciona porque Codex (OpenAI) e Claude Code (Anthropic) são **agentes que
escrevem e executam código no seu computador**. Quando você pede "corta as pausas e
coloca legenda", a IA não "clica" num editor — ela escreve e roda comandos de
ferramentas de vídeo (como o `ffmpeg`) que fazem o corte, a legenda e a animação.
Você nunca precisa abrir um editor de vídeo.

Seu papel muda de **editor** para **diretor**. E a regra de ouro do curso é:

> **Quanto melhor a direção, melhor a edição. E direção se aprende.**

### O método em 4 etapas

Toda edição, da mais simples à mais avançada, segue o mesmo ciclo:

1. **Prepare** — organize o material (gravação, roteiro, referências, marca) numa
   pasta que a IA entende.
2. **Peça** — dê um comando claro: o que, onde, com que estilo.
3. **Revise** — confira a **amostra** curta antes do vídeo inteiro e corrija só o
   que estiver errado.
4. **Reutilize** — salve o que foi aprovado (estilo, comandos, templates) para o
   próximo vídeo sair mais rápido e igual.

Guarde esse ciclo. As aulas 01–04 ensinam a **Preparar** e **Pedir**; a 09 ensina a
**Revisar**; a 10 fecha com **Reutilizar**.

### Por que isso importa para a HN

A HN vive de **anúncios, conteúdo e explicação de oferta** — exatamente os três
casos em que a edição trava:

| Situação na HN | O problema | A virada |
|---|---|---|
| **Ads** de clientes | O criativo cansa e a próxima versão não sai | Gerar variações em minutos (Aula 08) |
| **Conteúdo** da própria HN | Grava, mas a edição fica pra depois e nada vai ao ar | Rotina semanal de produção (Aula 10) |
| **Oferta** (vender o serviço de gestão comercial) | Paredão de texto, o cliente rola antes de entender | Motion explicativo (Aula 07) |

Nos três casos a virada é a mesma: **você direciona, a IA edita.**

---

## Aula 01 — Ambiente pronto

**Objetivo:** deixar o computador pronto para editar com IA.

### Conceito

Você precisa de duas coisas:

1. **Um agente de IA** que escreve e executa código — escolha **um**:
   - **Codex** (OpenAI) — vem com assinaturas do ChatGPT.
   - **Claude Code** (Anthropic) — vem com assinaturas do Claude.

   Os dois funcionam bem para o método. Os aplicativos, planos e limites são
   diferentes, então escolha o que já combina com o que a HN assina.

2. **As ferramentas de vídeo** que a IA vai comandar:
   - **ffmpeg** — corta, junta, converte, aplica legenda. É o "motor" de tudo.
   - **Python 3** — roda os scripts de corte e legenda.
   - **faster-whisper** — transcreve a fala (gera o texto e o tempo de cada palavra
     para as legendas).
   - **Node.js** — necessário para as animações avançadas (Aulas 07, B1, B2).

> **Você vai precisar de um computador.** As práticas usam arquivos e ferramentas
> instaladas na máquina. O tempo de processamento varia conforme o computador, a
> duração do vídeo e a complexidade dos efeitos — por isso sempre comece com testes
> curtos.

### Passo a passo

**1. Instale o agente de IA (escolha um).** Siga o instalador oficial do produto que
você assina. Depois abra o terminal dentro da pasta do projeto e inicie o agente.

**2. Deixe a própria IA instalar as ferramentas de vídeo.** Esse é o primeiro uso do
método: em vez de você instalar tudo na mão, **peça**. Abra o agente e cole:

```
Prepare este computador para editar vídeos. Verifique se ffmpeg, Python 3,
Node.js e a biblioteca faster-whisper estão instalados. Instale o que faltar,
usando o gerenciador de pacotes adequado ao meu sistema. No fim, rode
"ffmpeg -version" e "python3 --version" e me mostre o resultado.
```

**3. Confirme.** O ambiente está pronto quando a IA mostrar as versões do ffmpeg e
do Python sem erro.

### Exercício HN
Peça à IA para listar a versão de cada ferramenta e salvar num arquivo
`ambiente-ok.txt` na pasta da HN. Esse arquivo vira seu "checklist de máquina pronta".

---

## Aula 02 — Seu primeiro projeto

**Objetivo:** organizar os arquivos de um jeito que faça a IA acertar.

### Conceito

A IA só edita bem o que ela consegue **encontrar e entender**. Uma pasta bagunçada
("gravacao_01.mov … gravacao_08.mov, AGUARDANDO EDIÇÃO") gera pedidos vagos e
resultados errados. Uma pasta organizada é metade da direção.

### Passo a passo

Use **uma pasta por vídeo**, sempre com a mesma estrutura. O modelo completo está em
[`modelos/estrutura-de-pastas.md`](../modelos/estrutura-de-pastas.md). Em resumo:

```
2026-10-hn-ads-gestao-comercial/
├── 00-briefing.md        ← o que é o vídeo (modelo em modelos/briefing.md)
├── 01-bruto/             ← gravações originais (nunca edite aqui)
├── 02-roteiro/           ← roteiro e transcrição
├── 03-assets/            ← logo, imagens, fontes, cores da marca
├── 04-referencias/       ← vídeos de outros criadores que servem de estilo
├── 05-amostras/          ← trechos curtos para revisar antes do vídeo inteiro
└── 06-final/             ← versões aprovadas, prontas para postar
```

Regras de ouro:
- **Nunca edite o bruto.** A IA sempre gera arquivos novos a partir dele.
- **Nomes que dizem o que são:** `take-01.mp4`, não `IMG_8823.MOV`.
- **Use só assets que a HN tem direito de usar** (gravações, imagens, músicas).

### Comando pronto
```
Crie a estrutura de pasta de um novo vídeo da HN chamado
"2026-10-hn-ads-gestao-comercial", seguindo modelos/estrutura-de-pastas.md.
Copie modelos/briefing.md para dentro dela como 00-briefing.md.
```

### Exercício HN
Crie a pasta do primeiro vídeo real da HN e preencha o `00-briefing.md`.

---

## Aula 03 — Custos sob controle

**Objetivo:** usar a IA sem estourar créditos nem refazer trabalho.

### Conceito

Cada pedido consome **tokens** (o "combustível" da IA) e tempo de processamento. O
desperdício não vem de pedir demais — vem de **refazer**: pedir o vídeo inteiro,
descobrir um erro no segundo 40 e mandar fazer tudo de novo.

> O treinamento não inclui as ferramentas. Assinaturas, créditos e serviços externos
> são contratados separadamente. Avalie esses gastos antes de escalar.

### As 4 regras de economia

1. **Teste numa amostra.** Antes do vídeo inteiro, peça 5–10 segundos. Aprovou o
   estilo? Aí sim aplique no resto.
2. **Corrija o trecho certo.** Se só a legenda do segundo 12 está errada, peça para
   corrigir **só aquilo** (Aula 09), não para refazer o vídeo.
3. **Reaproveite o aprovado.** Estilo aprovado vira template/skill (Aula 10). O
   próximo vídeo não começa do zero — e nem a IA.
4. **Faça o trabalho pesado com ferramenta, não com IA.** Cortar silêncio e
   transcrever é trabalho do `ffmpeg` e do `faster-whisper`, que rodam no seu
   computador de graça. A IA só precisa escrever e disparar o comando.

### Exercício HN
Antes de cada vídeo, anote no briefing: **quanto tempo** e **quantas tentativas**
você aceita gastar. Se passar disso, o problema é a direção — volte à Aula 04.

---

## Aula 04 — O pedido certo

**Objetivo:** escrever comandos que a IA transforma em edição de primeira.

### Conceito

A diferença entre um vídeo genérico e um vídeo bom está no pedido.

| Pedido vago | Pedido dirigido |
|---|---|
| "Edita esse vídeo e deixa bonito." | "Corte as pausas de `01-bruto/take-01.mp4`, adicione legendas com a palavra falada em destaque roxo e anime o título 'Gestão que vende' nos 3 primeiros segundos." |

Sem direção, **a IA adivinha o resto**. Com direção, ela acerta.

### A fórmula do pedido certo

Todo bom comando responde 5 perguntas:

1. **O quê?** Qual arquivo, qual trecho (`take-01.mp4`, de 0:05 a 0:20).
2. **Faça o quê?** A ação (cortar pausas, legendar, inserir imagem, animar).
3. **Como fica?** O estilo (cor, fonte, ritmo) — ou aponte para uma skill.
4. **Onde vai?** Formato e destino (vertical 9:16 para Reels, 1:1 para feed).
5. **Entregue o quê?** Primeiro uma **amostra**; depois o vídeo inteiro.

### Usar um vídeo de referência

"Gostei da edição de um vídeo que vi, consigo fazer nesse estilo?" — sim. Coloque o
vídeo em `04-referencias/` e peça para a IA **analisar** antes de editar:

```
Analise o vídeo 04-referencias/referencia.mp4. Descreva o ritmo dos cortes,
o estilo das legendas, as transições e as composições. Depois adapte essa
direção ao meu roteiro e à identidade da HN, sem copiar a marca de ninguém.
Me mostre uma amostra de 8 segundos antes de aplicar no vídeo inteiro.
```

### Exercício HN
Reescreva 3 pedidos vagos que você faria hoje usando a fórmula das 5 perguntas.

---

## Aula 05 — Primeira edição

**Objetivo:** sair do bruto para o editado — pausas cortadas e legenda dinâmica.

### Conceito

A primeira edição é a que mais economiza tempo e a que todo vídeo da HN vai usar:
**retirar o silêncio, juntar as falas sem buracos e inserir legendas no tempo de
cada fala.** A IA faz isso em 3 passos:

1. **Retira o silêncio** — encontra as pausas e corta.
2. **Aproxima os trechos** — junta as falas, sem buracos.
3. **Insere as legendas** — no tempo exato de cada palavra.

Este repositório já traz as duas ferramentas prontas e **testadas**:

- [`ferramentas/cortar_silencios.py`](../ferramentas/cortar_silencios.py)
- [`ferramentas/legendar.py`](../ferramentas/legendar.py)

### Passo a passo

**Cortar as pausas:**
```
python3 ferramentas/cortar_silencios.py 01-bruto/take-01.mp4 05-amostras/sem-pausas.mp4
```
Ajustes, se precisar:
- `--limiar -32` — abaixe (ex.: `-40`) se estiver cortando falas baixas.
- `--pausa 0.45` — duração mínima de uma pausa para ser cortada.
- `--respiro 0.12` — folga mantida antes/depois de cada fala (evita corte seco).

**Legendar (com a palavra falada em destaque):**
```
python3 ferramentas/legendar.py 05-amostras/sem-pausas.mp4 --queimar \
  --destaque "HN,vendas,resultado" --cor "#7C3AED" --maiusculas
```
Gera `.srt` (legenda simples), `.ass` (legenda estilizada), a transcrição em texto e,
com `--queimar`, o vídeo já legendado.

### Ou simplesmente peça
Você não precisa decorar os comandos. Diga à IA:
```
Corte as pausas e coloque legenda em 01-bruto/take-01.mp4. Use as ferramentas
da pasta ferramentas/. Legenda em maiúsculas, palavra falada em destaque na
cor #7C3AED, e sempre destaque as palavras "HN" e "vendas".
Me mostre os primeiros 10 segundos antes de processar o vídeo inteiro.
```

> **Resultado comprovado:** num teste, uma pausa de 1,5 s caiu para ~0,25 s de
> respiro, e a legenda saiu sincronizada com a palavra falada destacada em roxo.

### Exercício HN
Grave 30 segundos explicando o que a HN faz. Corte as pausas e legende.

---

## Aula 06 — Imagens com função

**Objetivo:** inserir imagens que **reforçam** a fala, no momento certo.

### Conceito

Imagem sem função é enfeite. Imagem com função **prova** o que você está dizendo no
exato momento em que você diz. Se você fala "nosso cliente dobrou as vendas", o
gráfico de crescimento aparece **naquela palavra** — não 3 segundos depois.

A chave é a **transcrição com tempo de cada palavra** (gerada na Aula 05): ela diz à
IA exatamente quando cada coisa foi dita.

### Passo a passo
1. Coloque as imagens em `03-assets/` com nomes que dizem o que são
   (`grafico-crescimento.png`, `logo-cliente.png`).
2. Peça a inserção amarrada à fala:
```
Use a transcrição de 05-amostras/sem-pausas. Quando eu disser "dobrou as
vendas", mostre 03-assets/grafico-crescimento.png entrando com zoom suave,
por 2 segundos, ocupando a metade de cima do vídeo vertical. Me mostre uma
amostra só desse trecho.
```

### Boas práticas
- **Uma ideia por imagem.** Imagem que precisa de explicação atrapalha.
- **Entre no tempo da fala**, saia logo depois.
- **Não cubra o rosto** durante a parte emocional da fala.

### Exercício HN
Liste 5 frases que você sempre fala ao vender o serviço da HN e, para cada uma, a
imagem que a prova.

---

## Aula 07 — Motion explicativo

**Objetivo:** fazer a **fala virar interface** — cards, listas e ícones animados que
explicam a oferta enquanto você fala.

### Conceito

É o estilo mais poderoso para **explicar a oferta da HN**. Em vez de um paredão de
texto, a explicação aparece animada, item por item, no ritmo da sua fala. Exemplo
clássico: "Três pontos para sua rotina — **Planejamento** (organizar a semana),
**Escolhas possíveis** (respeitar preferências), **Acompanhamento** (ajustar o
caminho)" — cada card acende quando você fala dele.

Tecnicamente, essas animações são **desenhadas em código** (HTML/CSS ou uma
biblioteca de vídeo em código) e depois renderizadas por cima da gravação. Você não
escreve esse código — a IA escreve. Você só dirige.

### Passo a passo — sempre por amostra
**Etapa 1 — descreva a composição:**
```
Crie um motion explicativo para o trecho em que explico os 3 pilares da HN:
"Diagnóstico", "Estratégia" e "Execução". Faça uma lista de 3 cards no topo
do vídeo vertical, estilo roxo escuro da HN. Cada card acende no momento em que
eu falo o nome dele (use a transcrição). Meu rosto continua visível embaixo.
```
**Etapa 2 — peça a primeira amostra:** a IA gera só esse trecho, com o ritmo de cada
elemento, **antes** do vídeo inteiro. Revise (Aula 09), ajuste e só então aplique.

### Exercício HN
Transforme a oferta principal da HN em um motion explicativo de 3 itens.

---

## Aula 08 — Variações para ads

**Objetivo:** gerar várias versões de um anúncio para testar, sem regravar.

### Conceito

Anúncio cansa. A solução não é gravar mais — é **variar mais**. Com a base aprovada,
a IA cria **Versão B, C, D** trocando só o que importa testar:

- **Abertura (gancho)** — os 3 primeiros segundos que param o scroll.
- **Imagens** de prova.
- **Formato** — vertical (9:16), quadrado (1:1), horizontal (16:9).
- **Chamada final** (CTA).

### Passo a passo
```
Use 06-final/anuncio-base.mp4 como base aprovada. Crie 3 variações para teste:
- Versão B: abre com o título "Sua equipe vende sem processo?"
- Versão C: abre com o gráfico de resultado antes da fala
- Versão D: mesma da B, mas em formato quadrado 1:1
Mantenha a legenda e o estilo iguais. Salve em 06-final/ com o nome da versão.
```

### Exercício HN
Pegue o anúncio de um cliente e gere 3 ganchos diferentes para teste A/B.

---

## Aula 09 — Revisar sem refazer

**Objetivo:** corrigir só o que está errado, sem refazer o vídeo.

### Conceito

A revisão é onde se ganha ou se perde tempo (e dinheiro). O erro comum é pedir "faz
de novo". O certo é **apontar o trecho e a correção**. Use a ficha em
[`modelos/ficha-de-revisao.md`](../modelos/ficha-de-revisao.md).

### Como pedir uma correção
Sempre diga **onde** (tempo), **o quê** está errado e **como** deve ficar:
```
No segundo 0:12 a legenda escreveu "vendaz", o certo é "vendas".
Entre 0:20 e 0:23 a imagem entrou atrasada: faça ela entrar quando eu digo
"resultado". Não mexa em mais nada do vídeo.
```

### A regra "não mexa em mais nada"
Termine toda correção com **"não mexa em mais nada"**. Isso impede a IA de "melhorar"
partes que já estavam aprovadas.

### Exercício HN
Revise o vídeo da Aula 05 usando a ficha de revisão e corrija só os pontos marcados.

---

## Aula 10 — Rotina de produção

**Objetivo:** transformar o método numa linha de produção semanal da HN.

### Conceito

Um vídeo é projeto. Vários vídeos por semana é **rotina**. A rotina funciona porque
você **reutiliza** tudo o que aprovou: estrutura de pasta, briefing, comandos e
estilo (skills). O próximo vídeo não começa do zero.

### A semana de produção da HN
| Dia | Etapa | O que fazer |
|---|---|---|
| Seg | **Prepare** | Roteiros da semana + briefings preenchidos |
| Ter | **Grave** | Grave todos os takes de uma vez |
| Qua | **Peça** | Primeira edição (Aula 05) de tudo |
| Qui | **Revise** | Amostras + correções pontuais (Aula 09) |
| Sex | **Reutilize** | Variações de ads (Aula 08) + salvar o que funcionou |

### Reutilizar = salvar o aprovado
Quando um estilo for aprovado, peça:
```
Salve o estilo deste vídeo (cores, fonte, legenda, ritmo e animações) como
uma skill reutilizável na pasta .claude/skills/, para eu aplicar nos próximos
vídeos da HN com um único comando.
```

### Exercício HN
Monte o calendário de conteúdo do próximo mês da HN usando a semana acima.

---

## Bônus 01 — Perspectiva e composição 3D

**Objetivo:** dar profundidade de três dimensões às camadas do vídeo.

### Conceito
Elementos (cards, telas, imagens) são posicionados em **camadas com profundidade**,
girados em perspectiva, como se estivessem no espaço. Exemplos do estilo: uma sala
"montada camada por camada", "5 camadas em 3D", um tutorial em que "o pedido vira
vídeo" em perspectiva. Novamente: a IA desenha isso em código, você dirige.

### Comando base
```
Monte uma composição 3D para mostrar o processo da HN em 3 camadas:
"Diagnóstico", "Estratégia" e "Execução". Cada camada é um card que entra em
perspectiva, empilhado com profundidade, girando levemente. Mostre uma amostra
de 6 segundos antes de aplicar.
```

> Dica: 3D é o efeito mais pesado de processar. **Sempre** valide numa amostra curta
> (Aula 03) antes de renderizar o vídeo inteiro.

---

## Bônus 02 — Recorte, moldura e lettering

**Objetivo:** colocar texto **atrás** de você e emoldurar a cena, **sem tela verde**.

### Conceito
1. **Recorte de fundo** — a IA separa você do fundo (sem tela verde), o que permite
   trocar o cenário (cidade à noite, gráfico neon, cor sólida) com uma gravação só.
2. **Lettering** — com o recorte, um texto grande ("SEM TELA VERDE") passa **atrás**
   da sua cabeça e na frente do fundo. É o efeito "a palavra vira a cena".
3. **Moldura** — uma borda com brilho que abre espaço para uma explicação do lado que
   você indicar.

### Comando base
```
Recorte meu fundo em 01-bruto/take-01.mp4 sem tela verde. Coloque o texto
"GESTÃO QUE VENDE" em letras grandes atrás de mim e na frente do fundo, nos
4 primeiros segundos. Depois adicione uma moldura roxa com brilho abrindo
espaço à direita para uma explicação. Amostra de 6 segundos primeiro.
```

---

## Os materiais que acompanham o curso

Assim como no original, você não começa do zero — e a IA também não:

- **O guia entrega o pedido certo para você** → [`modelos/guia-de-comandos.md`](../modelos/guia-de-comandos.md)
- **As skills entregam o critério para a IA** → [`.claude/skills/`](../.claude/skills/)
  (o Claude Code carrega sozinho; no Codex, o arquivo `AGENTS.md` aponta para elas)
- **Modelo de briefing** → [`modelos/briefing.md`](../modelos/briefing.md)
- **Pasta modelo para os arquivos** → [`modelos/estrutura-de-pastas.md`](../modelos/estrutura-de-pastas.md)
- **Ficha de revisão** → [`modelos/ficha-de-revisao.md`](../modelos/ficha-de-revisao.md)
- **Ferramentas testadas** → [`ferramentas/`](../ferramentas/)

### Por que as skills fazem tanta diferença
Sem skills, um pedido como "edita esse vídeo e deixa bonito" devolve a gravação quase
sem edição — **a IA adivinha o resto**. Com as skills ligadas, ela consulta 5
critérios antes de editar, e a primeira amostra já chega perto do que você imaginou:

| Skill | Define |
|---|---|
| **Estilo** | cor, fonte e clima |
| **Ritmo** | cortes e respiros |
| **Legendas** | tamanho e destaque |
| **Movimento** | entradas e transições |
| **Composição** | camadas e molduras |

---

## Glossário rápido

- **Agente de IA** — IA que escreve e executa código no seu computador (Codex, Claude Code).
- **Amostra** — trecho curto (5–10 s) gerado para revisar antes do vídeo inteiro.
- **Bruto** — a gravação original, sem edição. Nunca é alterada.
- **ffmpeg** — ferramenta que faz cortes, junções, conversões e legendas.
- **Motion** — animação gráfica (cards, ícones, textos) sobre o vídeo.
- **Skill** — arquivo de critérios que a IA consulta para editar no seu estilo.
- **Token** — unidade de consumo da IA; refazer gasta tokens à toa.
- **Transcrição com tempo** — o texto da fala com o momento exato de cada palavra.

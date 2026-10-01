# Guia de comandos — HN

> Copie, troque o que está entre `< >` e cole no Codex ou no Claude Code.
> Organizado por aula e etapa. Sempre peça **amostra antes do vídeo inteiro**.

---

## Aula 01 — Ambiente pronto

**Instalar tudo**
```
Prepare este computador para editar vídeos. Verifique se ffmpeg, Python 3,
Node.js e a biblioteca Python faster-whisper estão instalados. Instale o que
faltar com o gerenciador de pacotes do meu sistema. No fim, mostre as versões.
```

**Diagnosticar erro**
```
O comando abaixo deu erro. Explique em português simples o que aconteceu e
corrija:
<cole o erro>
```

---

## Aula 02 — Seu primeiro projeto

**Criar a pasta do vídeo**
```
Crie a pasta de um novo vídeo chamado "<AAAA-MM-cliente-tema>" seguindo
modelos/estrutura-de-pastas.md e copie modelos/briefing.md para 00-briefing.md.
```

**Organizar gravações soltas**
```
Os arquivos em <pasta> estão com nomes aleatórios. Renomeie para take-01,
take-02… pela ordem de gravação (data do arquivo) e mova para 01-bruto/.
Me mostre a lista antes de renomear.
```

---

## Aula 03 — Custos sob controle

**Estimar antes de rodar**
```
Antes de editar, me diga quais etapas você vai executar, quais rodam só no
meu computador (sem gastar IA) e qual a duração total dos vídeos em
01-bruto/. Não execute nada ainda.
```

---

## Aula 04 — O pedido certo

**Analisar uma referência**
```
Analise 04-referencias/<arquivo>.mp4. Descreva ritmo dos cortes, estilo das
legendas, transições e composições. Adapte essa direção ao roteiro e à
identidade da HN, sem copiar a marca de ninguém. Amostra de 8 s primeiro.
```

**Transformar pedido vago em dirigido**
```
Reescreva meu pedido abaixo respondendo: qual arquivo/trecho, qual ação,
qual estilo, qual formato e qual entrega. Depois execute só a amostra.
Pedido: "<seu pedido vago>"
```

---

## Aula 05 — Primeira edição

**Etapa 1 — Cortar pausas**
```
Corte as pausas de 01-bruto/<take>.mp4 com ferramentas/cortar_silencios.py.
Salve em 05-amostras/sem-pausas.mp4 e me diga quantos segundos foram removidos.
```

**Etapa 2 — Legendar**
```
Legende 05-amostras/sem-pausas.mp4 com ferramentas/legendar.py: maiúsculas,
palavra falada na cor <#7C3AED>, destaque sempre "<HN>", "<vendas>".
Queime a legenda no vídeo.
```

**Tudo de uma vez**
```
Corte as pausas e coloque legenda dinâmica em 01-bruto/<take>.mp4 usando as
ferramentas da pasta ferramentas/ e as skills de legenda e ritmo.
Me mostre os primeiros 10 segundos antes do vídeo inteiro.
```

---

## Aula 06 — Imagens com função

```
Use a transcrição de <vídeo>. Quando eu disser "<frase>", mostre
03-assets/<imagem> entrando com <zoom suave / deslize>, por <2> segundos,
na <metade de cima> do vídeo. Amostra só desse trecho.
```

**Sugerir imagens**
```
Leia a transcrição de <vídeo> e sugira em quais 5 momentos uma imagem
provaria o que estou dizendo. Para cada um: tempo, frase e imagem ideal.
Não edite ainda.
```

---

## Aula 07 — Motion explicativo

**Etapa 1 — Composição**
```
Crie um motion explicativo para o trecho em que falo "<item 1>", "<item 2>"
e "<item 3>". Lista de 3 cards no topo do vídeo vertical, no estilo da skill
de estilo da HN. Cada card acende quando falo o nome dele (use a transcrição).
Meu rosto continua visível embaixo.
```

**Etapa 2 — Primeira amostra**
```
Gere só a amostra desse trecho, com o ritmo de cada elemento, antes de
aplicar no vídeo inteiro.
```

---

## Aula 08 — Variações para ads

```
Use 06-final/<base>.mp4 como base aprovada. Crie variações:
- Versão B: abertura com o título "<gancho B>"
- Versão C: abertura com <imagem de prova> antes da fala
- Versão D: igual à B em formato 1:1
Mantenha legenda e estilo. Salve em 06-final/ com sufixo da versão e formato.
```

**Gerar ganchos**
```
Leia o briefing e a transcrição e escreva 5 ganchos de 3 segundos para
anúncio, cada um atacando uma dor diferente do público. Não edite ainda.
```

---

## Aula 09 — Revisar sem refazer

```
Corrija apenas os itens abaixo em <arquivo>:
- <0:12>: <legenda "vendaz"> → <"vendas">
- <0:20–0:23>: <imagem atrasada> → <entra quando digo "resultado">
Não mexa em mais nada do vídeo. Me mostre só os trechos corrigidos.
```

---

## Aula 10 — Rotina de produção

**Salvar o estilo aprovado**
```
Salve o estilo deste vídeo (cores, fonte, legenda, ritmo e animações) como
skill reutilizável em .claude/skills/, para eu aplicar nos próximos vídeos
da HN com um único comando.
```

**Processar a semana em lote**
```
Para cada pasta de vídeo desta semana: corte as pausas, legende e gere uma
amostra de 10 s em 05-amostras/. Não processe o vídeo inteiro. Me mostre a
lista de amostras para eu revisar.
```

---

## Bônus 01 — Perspectiva e composição 3D

```
Monte uma composição 3D com <3> camadas: "<camada 1>", "<camada 2>",
"<camada 3>". Cada camada é um card que entra em perspectiva, empilhado com
profundidade, girando levemente. Amostra de 6 segundos primeiro.
```

---

## Bônus 02 — Recorte, moldura e lettering

**Recorte de fundo + troca de cenário**
```
Recorte meu fundo em <take> sem tela verde e gere 3 versões de cenário:
<cidade à noite>, <gráfico neon>, <cor sólida #...>. Amostra de 5 s de cada.
```

**Lettering atrás da pessoa**
```
Com o fundo recortado, coloque "<TEXTO>" em letras grandes atrás de mim e
na frente do fundo, nos <4> primeiros segundos. Amostra de 6 s primeiro.
```

**Moldura**
```
Adicione uma moldura <roxa> com brilho abrindo espaço à <direita> para uma
explicação entre <0:10> e <0:18>. Amostra só desse trecho.
```

# Pasta modelo de um vídeo

Uma pasta por vídeo, sempre com a mesma estrutura. Nome: `AAAA-MM-cliente-tema`.

```
2026-10-hn-ads-gestao-comercial/
├── 00-briefing.md        o que é o vídeo (copie de modelos/briefing.md)
├── 01-bruto/             gravações originais — nunca edite aqui
│   ├── take-01.mp4
│   └── take-02.mp4
├── 02-roteiro/           roteiro e transcrições
│   └── roteiro.md
├── 03-assets/            logo, imagens, prints, fontes, música
│   ├── logo-hn.png
│   └── grafico-crescimento.png
├── 04-referencias/       vídeos de estilo (só para análise, nunca para publicar)
├── 05-amostras/          trechos curtos para revisar antes do vídeo inteiro
└── 06-final/             versões aprovadas, prontas para postar
    ├── anuncio-v-a-9x16.mp4
    └── anuncio-v-b-1x1.mp4
```

## Regras
1. **Nunca edite o bruto.** Toda edição gera um arquivo novo.
2. **Nomes que dizem o que são.** `grafico-crescimento.png`, não `IMG_2231.png`.
3. **Amostra antes do inteiro.** Tudo passa por `05-amostras/` antes de `06-final/`.
4. **Versão no nome.** `-v-a`, `-v-b`… e o formato (`-9x16`, `-1x1`, `-16x9`).
5. **Só use o que a HN tem direito de usar.** Gravações, imagens, músicas e fontes.

## Comando para criar
```
Crie a pasta de um novo vídeo chamado "<nome>" seguindo
modelos/estrutura-de-pastas.md e copie modelos/briefing.md para 00-briefing.md.
```

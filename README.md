# translate-deck-catalog

Catalogo de traducões do [translate-deck](https://github.com/VictorCabral99/translate-deck).
Publicado em GitHub Pages; o plugin baixa `index.json` e confere o SHA-256 de
`index.sha256` antes de exibir qualquer entrada.

## Estrutura

```
schema/game.schema.json          # schema JSON (2020-12)
schema/translation.schema.json
games/<appid>.json               # um arquivo por jogo
index.json + index.sha256        # gerados por scripts/build_index.py
```

## Adicionar uma traducao

1. Copie o formato de `schema/game.schema.json`.
2. Só entram artefatos que o tradutor/autor permita redistribuir. `permission.status`
   fica `unknown` (nao instala) ate existir `evidence_url` https + `checked_at`.
   `denied` nunca instala.
3. `sha256` do artefato e obrigatorio e conferido no download.
4. Rode `python scripts/build_index.py` e abra PR. O CI falha se o indice
   estiver desatualizado ou o JSON estiver fora do schema.

Este repositorio contem **apenas metadados e URLs canonicas**. Nenhum arquivo do
jogo e nenhum binario de traducao e hospedado aqui.

## Remocao

Pedido do autor ou problema legal: abra uma issue. Entradas sao removidas em ate
24 h; o `index.json` e regenerado e o SHA muda no mesmo commit, de modo que o
plugin para de oferecer a traducao assim que a atualizacao chega.

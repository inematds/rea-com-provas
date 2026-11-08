# CLAUDE.md — rea-com-provas

Kit aberto: 4 regras + 3 construções (prompts/) + conferidor de provas (`confere_provas.py`).

## Regras do projeto

- Repo público `inematds/rea-com-provas`; autor dos commits `inematds <inematds@gmail.com>`.
- Projeto sem fonte: não citar material de referência, autor ou comunidade de origem; nos
  prompts os apps estudados são genéricos ("[app open source de agentes]").
- Instalação do REA/harness não se repete aqui: link para https://inematds.github.io/rea-sem-travas/guia/.
- Comandos do REA só os que existem na documentação dele (conferidos na 6.4.0:
  `analyze-javascript-application`, `list-browser-targets`, `inspect-web-page`,
  `capture-web-screenshot`). Não inventar comando.
- Conferidor: só biblioteca padrão, sem rede. Mudou regra do conferidor → teste novo em `tests/`.
- Guia em `guia/` (PT) + `guia/en/` + `guia/es/`; tradução pelo `inema-traduz`; dentro de `<pre>`
  os comandos ficam byte a byte iguais ao PT.
- Testes: `python3 -m unittest discover tests` (ou `pytest`).

## Self-learning

Quando o Nei corrigir algo, ou você perceber um erro seu: antes de continuar, acrescente a lição
como regra de uma linha no TOPO da seção ## Lessons abaixo.

## Lessons

- HTML salvo de site vem numa linha só: quebrar em uma tag por linha antes de pedir provas com número de linha (08/11/2026).
- Gerar banners do Codex em paralelo pode gravar a mesma imagem em dois arquivos: conferir `md5sum` e refazer o repetido sozinho (08/11/2026).

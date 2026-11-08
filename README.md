# REA com provas

[![Refaça com provas](guia/assets/banner.jpg)](https://inematds.github.io/rea-com-provas/guia/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

> **A IA diz que entendeu o app. Peça a prova.**

## O que é

O **REA com provas** é um kit aberto e gratuito para quem usa um agente de IA (Claude Code, Codex ou o harness dsh) para estudar um app e fazer a própria versão. O problema: o agente diz que entendeu como o app funciona e inventa o que não viu. O kit traz 4 regras, 3 pedidos prontos (painel de agentes, reator de leads e site refeito) e um conferidor em Python que reprova o arquivo de provas quando falta prova. Para usar, você precisa de Python 3 e de um agente de IA no terminal.

## 📖 Guia de uso

Guia completo (landing + passo a passo): **https://inematds.github.io/rea-com-provas/guia/**

> [!WARNING]
> **Segurança e licença.** Use só em **software seu** ou **open source cuja licença deixa
> estudar** (MIT, Apache-2.0, BSD, GPL, MPL…). Estudar não é copiar: a sua versão é escrita do
> zero, com seu nome, seus textos e seu visual. Rode o agente numa pasta separada, sem senhas,
> chaves ou dados de clientes. Detalhes em [REGRAS.md](REGRAS.md).

## As 4 regras

1. **Sempre peça o arquivo de provas `provas.md`**: cada conclusão com o arquivo/trecho que a prova, mais a seção "O que NÃO deu para provar".
2. **Foco no código do próprio app**, não nas bibliotecas embutidas (mande ignorar `node_modules`, `vendor`, `site-packages`).
3. **Só software seu ou open source que a licença deixa estudar.** Depois construa a SUA versão, com seu nome e visual.
4. **Descreva o visual em detalhe** (cores, fontes, movimento) num brief de design.

## O que vem no kit

| Arquivo | Para que serve |
|---|---|
| [`REGRAS.md`](REGRAS.md) | As 4 regras e o aviso de segurança e licença |
| [`prompts/a-painel-de-agentes.md`](prompts/a-painel-de-agentes.md) | Construção A: painel com 6 agentes vivos para um negócio + caixa de comando |
| [`prompts/b-reator-de-leads.md`](prompts/b-reator-de-leads.md) | Construção B: lead entra → qualificar, responder, agendar, acompanhar → comemora |
| [`prompts/c-site-refeito.md`](prompts/c-site-refeito.md) | Construção C: mapear o SEU site e refazer numa versão premium |
| [`provas/MODELO-provas.md`](provas/MODELO-provas.md) | Formato do arquivo de provas |
| [`confere_provas.py`](confere_provas.py) | Conferidor: nota 0–10, APROVADO/REPROVADO e o que falta |
| [`brief/MODELO-brief-design.md`](brief/MODELO-brief-design.md) | Brief de design com exemplo preenchido no padrão INEMA |
| [`exemplos/`](exemplos/) | `provas-boa.md` (aprovada), `provas-ruim.md` (reprovada) e a rodada real |
| [`tests/`](tests/) | Testes do conferidor, sem internet |

O kit vem configurado com o INEMA como exemplo (brief no padrão INEMA, rodada real no site inema.club). Troque os [colchetes] dos prompts e o brief pelo seu negócio.

## O conferidor

```bash
python3 confere_provas.py provas.md          # relatório em texto
python3 confere_provas.py provas.md --json   # mesmo resultado em JSON
```

Reprova (código de saída 1) quando falta a seção "O que NÃO deu para provar" (ou ela está vazia),
quando uma conclusão não cita arquivo/trecho, ou quando todas as referências apontam para
bibliotecas (`node_modules`, `vendor`, `site-packages`…). Aprova com código 0. Não conseguiu ler: código 2.
O conferidor checa o formato; abrir 2 ou 3 provas e ver se o trecho está lá continua sendo com você.

## O processo, do início ao fim

Quem faz: 🧠 você (com o agente aberto) · ⚙️ script · 🤖 agente de IA (Claude Code, Codex ou dsh)

| # | Passo | Comando | Quem |
|---|---|---|---|
| 1 | Baixar o kit e rodar os testes | `cd ~ && git clone https://github.com/inematds/rea-com-provas.git && cd rea-com-provas && python3 -m unittest discover tests` | ⚙️ |
| 2 | (Opcional) Instalar REA + harness | guia https://inematds.github.io/rea-sem-travas/guia/ | 🧠 |
| 3 | Escolher o alvo e conferir a licença | `cat ~/estudo/app/LICENSE` | 🧠 |
| 4 | Preencher o brief de design | `cp brief/MODELO-brief-design.md ~/estudo/brief.md` | 🧠 |
| 5 | Colar uma construção de `prompts/` no agente (fase 1: estudar) | `cd ~/estudo && claude` (ou `codex`) | 🧠 → 🤖 |
| 6 | Agente entrega o `provas.md` e roda o conferidor até APROVADO | `python3 ~/rea-com-provas/confere_provas.py provas.md` | 🤖 + ⚙️ |
| 7 | Conferir 2 ou 3 provas à mão e liberar | escrever `pode construir` | 🧠 |
| 8 | Agente constrói a sua versão (fase 2) | — | 🤖 |
| 9 | Abrir, testar e pedir ajustes | abrir o `index.html` gerado | 🧠 |

## Teste real (08/11/2026)

A construção C rodou no Claude Code (pela assinatura) com o site inema.club no papel de "seu site", jeito 1 (HTML salvo, sem REA), fase 1 e fase 2 de uma vez:

- **23 conclusões** no `provas.md`, conferidor: **NOTA 10/10 — APROVADO**;
- **4 de 4** provas abertas à mão (linhas 72, 113, 144 e 161 do HTML salvo) tinham o trecho citado;
- **472 s** (7 min 52 s) e 42 turnos do agente para as duas fases;
- saiu um `index.html` de 94 KB, sem rolagem lateral em 390 px e 1440 px.

Tudo em [`exemplos/rodada-real/`](exemplos/rodada-real/): o pedido usado, o `provas.md`, o HTML salvo e a versão nova.

## Testes

```bash
python3 -m unittest discover tests     # ou: pytest
```

Sem internet. Cobrem: falta a seção "não deu para provar", seção vazia, conclusão sem
referência, referências só em `node_modules`/`vendor`, títulos em EN/ES, modelo em branco e os
dois exemplos pela linha de comando.

## Veja também

- [O que é o REA](https://inematds.github.io/rea-engenharia-reversa/guia/) — a ferramenta de engenharia reversa por trás de tudo.
- [REA sem travas](https://inematds.github.io/rea-sem-travas/guia/) — instalar modelo aberto + harness + REA no seu computador.

## Licença

MIT. Conteúdo aberto e gratuito do [INEMA.CLUB](https://inema.club).

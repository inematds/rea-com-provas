# As 4 regras

> **A IA diz que entendeu o app. Peça a prova.**

> [!WARNING]
> **Segurança e licença — leia antes de usar.**
> - Estude só **software seu** ou **open source cuja licença deixa estudar** (MIT, Apache-2.0,
>   BSD, GPL, MPL…). App fechado de outra empresa, ou cuja licença proíbe engenharia reversa:
>   não use este método nele.
> - Estudar não é copiar. A sua versão é escrita do zero, com **seu nome, seus textos e seu
>   visual**. Não copie arquivos, ícones, marca nem textos do app estudado.
> - Licença que pede atribuição ou que "contamina" (GPL, AGPL): se você reaproveitar qualquer
>   trecho, siga as condições dela. Na dúvida, não reaproveite código, só a ideia.
> - Rode o app estudado e o agente numa pasta separada (ou num contêiner) e não dê ao agente
>   senhas, chaves nem acesso a dados de clientes.
> - Este kit só lê e escreve arquivos na pasta do trabalho. Nada é enviado, apagado ou
>   publicado sozinho.

## Regra 1 — Sempre peça o arquivo de provas

Antes de construir, o agente entrega o `provas.md` (modelo em
[`provas/MODELO-provas.md`](provas/MODELO-provas.md)):

- cada conclusão com o **arquivo e a linha** que a provam, mais o trecho copiado;
- a seção **"O que NÃO deu para provar"**, com tudo o que ele acha mas não achou.

Depois rode o conferidor:

```bash
python3 confere_provas.py provas.md
```

Ele reprova se faltar a seção "O que NÃO deu para provar", se alguma conclusão não citar
arquivo/trecho, ou se as referências apontarem só para bibliotecas. Só passe para a
construção quando sair `APROVADO`.

## Regra 2 — Foco no código do próprio app

App grande carrega milhares de arquivos de bibliotecas embutidas. Se o agente "prova" com
eles, ele está explicando a biblioteca, não o app. Mande ignorar `node_modules`, `vendor`,
`site-packages`, `dist` e arquivos `.min.js`. O conferidor reprova quando todas as provas
estão nessas pastas e avisa quando uma conclusão só cita biblioteca.

## Regra 3 — Só software seu ou open source que deixa estudar

Confira a licença **antes** (o modelo de provas tem a linha "Licença:"). Depois construa a
**sua** versão, com seu nome e seu visual. O estudo serve para entender o comportamento,
não para levar o código.

## Regra 4 — Descreva o visual em detalhe

"Faz bonito" dá painel feio. Preencha o [brief de design](brief/MODELO-brief-design.md):
cores com código, fontes, movimento em milissegundos, densidade e o que é proibido. É a
diferença entre um painel genérico e uma tela que dá vontade de usar.

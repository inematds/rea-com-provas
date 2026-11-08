# Construção B — Reator de leads

**O que sai:** um fluxo de leads na tela: o lead entra e passa por 4 raias (qualificar,
responder, agendar, acompanhar), cada raia com o seu agente, e o painel comemora quando o
lead agenda.

**De onde vem a ideia:** você estuda como um app open source divide um pedido grande em
tarefas para agentes trabalhadores e constrói o SEU fluxo de leads. Não copia o app.

**Antes de colar:** troque tudo que está entre [colchetes]. Tenha o código do app estudado numa
pasta e confira a licença (regra 3). Preencha o brief de design (`brief/MODELO-brief-design.md`).

Funciona no Claude Code, no Codex ou no harness dsh (instalação no guia
https://inematds.github.io/rea-sem-travas/guia/).

---

```text
Você vai trabalhar em duas fases. Não pule a fase 1.

FASE 1 — ESTUDAR COM PROVAS (não escreva código ainda)
Estude o app open source em [caminho da pasta, ex.: ~/estudo/app-orquestrador] e responda:
como ele recebe um pedido, divide em tarefas, entrega cada tarefa a um agente
trabalhador, acompanha o andamento e junta o resultado.

Regras do estudo:
1. Antes de tudo, abra o arquivo de licença e diga qual é. Se não for uma licença que
   deixa estudar (MIT, Apache-2.0, BSD, GPL, MPL...), pare e me avise.
2. Estude só o código do próprio app. Ignore node_modules, vendor, site-packages, dist,
   build e arquivos .min.js.
3. Entregue o arquivo provas.md no formato de provas/MODELO-provas.md: "## Alvo" (com
   "Licença:"), "## Conclusões" com "### C1. ..." e, em cada uma, "Prova:" =
   `caminho/do/arquivo.ext:linha-linha` e "Trecho:", e "## O que NÃO deu para provar".
4. Nenhuma conclusão sem arquivo e linha. O que você acha mas não achou vai para
   "O que NÃO deu para provar".
5. Rode: python3 [caminho]/confere_provas.py provas.md — até sair APROVADO.
Pare aqui e me mostre o resultado do conferidor.

FASE 2 — CONSTRUIR A SUA VERSÃO (só depois que eu disser "pode construir")
Construa do zero, em [stack, ex.: um único index.html com HTML, CSS e JavaScript], na
pasta [pasta, ex.: ~/projetos/reator-de-leads], o "[nome do seu reator]" para
[tipo de negócio, ex.: uma clínica odontológica]:
- Um botão "novo lead" (e um lead de exemplo a cada [20] segundos) com nome, canal
  ([Instagram, WhatsApp, site]) e pedido.
- 4 raias lado a lado, cada uma com o seu agente:
  1. Qualificar — dá nota de 0 a 10 e diz por quê ([regra, ex.: tem urgência, mora perto]).
  2. Responder — escreve a primeira mensagem no tom [do seu negócio].
  3. Agendar — propõe [2] horários livres e marca o escolhido.
  4. Acompanhar — lembra o lead [1 dia] antes e pergunta se vem.
- O cartão do lead anda de raia em raia, mostrando quem está cuidando dele.
- Lead que não qualifica sai do fluxo com o motivo escrito.
- Quando um lead agenda: comemoração na tela (confete ou brilho) e o contador
  "agendados hoje" sobe.
Os agentes são simulados (sem IA, sem API, sem chave, sem mandar mensagem de verdade).

Regras da construção:
- Use o provas.md só para entender a divisão em tarefas. Não copie arquivos, textos,
  nomes, ícones nem o visual do app estudado.
- O visual vem do brief de design em [caminho do brief preenchido].
- No fim, me diga como abrir, o que ficou de fora e o que precisa de teste manual.
```

---

**Conferir:** `python3 confere_provas.py provas.md` tem de sair `APROVADO` antes da fase 2.

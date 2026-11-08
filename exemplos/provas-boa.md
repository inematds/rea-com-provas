# Provas — painel de agentes (exemplo ilustrativo)

> Exemplo de provas.md que PASSA no conferidor. O app é fictício: os caminhos mostram
> o formato, não um projeto real. `python3 confere_provas.py exemplos/provas-boa.md` → APROVADO.

## Alvo

- App estudado: [app open source de agentes] (código público)
- Licença: MIT (`LICENSE`, linha 1)
- Versão / commit: v0.9.3
- Pastas ignoradas: node_modules, vendor, dist
- Pergunta: como o app mostra vários agentes lado a lado e manda a tarefa para o agente certo

## Conclusões

### C1. Cada agente é um cartão numa grade de colunas responsivas

- Prova: `src/components/AgentGrid.tsx:12-48`
- Trecho: `grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))`
- Confiança: alta

### C2. O estado de cada agente (parado, pensando, trabalhando) vem de um evento do servidor

- Prova: `src/hooks/useAgentStatus.ts:20-41` e `server/events.ts:88`
- Trecho: `source.addEventListener("agent-status", ...)`
- Confiança: alta

### C3. A caixa de comando escolhe o agente pela palavra-chave do pedido, não por IA

- Prova: `src/router/pickAgent.ts:5-30`
- Trecho: `if (text.includes("agenda")) return "agenda"`
- Confiança: média — há um caso padrão que manda tudo ao agente "suporte"

### C4. O brilho do cartão ativo é só CSS, sem biblioteca de animação

- Prova: `src/styles/card.css:60-74`
- Trecho: `@keyframes pulse { 0% { box-shadow: ... } }`
- Confiança: alta

## O que NÃO deu para provar

- Onde o histórico de cada agente é salvo: o código chama `/api/history`, mas o servidor dessa rota não está no repositório.
- Se existe limite de agentes por tela: não achei número fixo; pode depender só da largura.
- O som de "tarefa concluída": o arquivo `public/done.mp3` existe, mas não achei quem toca.

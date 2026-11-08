# Provas — painel de agentes (exemplo ilustrativo)

> Exemplo de provas.md que REPROVA no conferidor. É o que o agente costuma entregar
> quando ninguém pede a prova: soa convincente e não mostra nada.
> `python3 confere_provas.py exemplos/provas-ruim.md` → REPROVADO.

## Alvo

- App estudado: [app open source de agentes]
- Pergunta: como o app mostra vários agentes lado a lado

## Conclusões

### C1. O app usa uma arquitetura moderna baseada em microsserviços

- Analisei o projeto e ficou claro que cada agente roda isolado.
- Confiança: alta

### C2. A grade de agentes é feita com uma biblioteca de layout

- Prova: `node_modules/react-grid-layout/build/ReactGridLayout.js:120`
- Confiança: alta

### C3. As animações deixam a experiência fluida e profissional

- Prova: `vendor/animate/animate.min.css`
- Confiança: alta

### C4. Dá para refazer tudo em uma tarde

- Confiança: alta

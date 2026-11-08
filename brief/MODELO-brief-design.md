# Brief de design — [nome da sua versão]

> Regra 4: descreva o visual em detalhe. "Faz bonito" dá painel feio; cor, fonte e
> movimento escritos dão tela que dá vontade de usar. Preencha e entregue junto com o prompt.
> Embaixo do modelo há um exemplo preenchido no padrão INEMA.

## Modelo (troque os [colchetes])

### 1. Sensação
- Em 3 palavras: [ex.: calmo, preciso, premium]
- Parece com: [ex.: painel de cabine de avião à noite] · Não parece com: [ex.: planilha]

### 2. Cores (código hex)
- Fundo: [#......] · Fundo de cartão: [#......] · Borda: [#......]
- Texto: [#......] · Texto secundário: [#......]
- Cor de destaque (só UMA): [#......] — onde usa: [botão, número importante]
- Estados (sempre com rótulo de texto junto, nunca só cor):
  ok [#......] · atenção [#......] · erro [#......]

### 3. Fontes
- Títulos: [nome, peso] · Texto: [nome, tamanho mínimo 16 px] · Números/código: [nome]

### 4. Movimento
- Entrada da tela: [ex.: cartões sobem 8 px e aparecem em 300 ms, um depois do outro]
- Estado "trabalhando": [ex.: borda pulsa a cada 1,6 s]
- Ao concluir: [ex.: brilho de 600 ms + número sobe contando]
- Quem pede menos movimento (prefers-reduced-motion): [ex.: tudo parado no estado final]

### 5. Densidade e forma
- Densidade: [arejado | médio | denso] · Cartões por linha no computador: [3]
- Cantos: [ex.: 14 px] · Sombra: [ex.: nenhuma, separa por borda de 1 px]
- Celular (390 px): [ex.: 1 cartão por linha, caixa de comando fixa embaixo]

### 6. Proibido
- [ex.: gradiente roxo, emoji no texto, ícone de robô fofo, mais de uma cor de destaque]

---

## Exemplo preenchido — padrão INEMA

### 1. Sensação
- Em 3 palavras: escuro, preciso, premium
- Parece com: sala de controle à noite com luz quente · Não parece com: painel infantil colorido

### 2. Cores
- Fundo: `#0c0c10` · Fundo de cartão: `#16161e` · Borda: `#272730`
- Texto: `#e9e9ee` · Texto secundário: `#9a9aa6`
- Cor de destaque: amarelo `#FACC15` — botão principal (letra `#1a1206`), número importante, agente ativo
- Estados com rótulo: ok `#7CE0C6` "pronto" · atenção `#F2B45C` "esperando" · erro `#F0918A` "falhou"

### 3. Fontes
- Títulos: Sora 700 · Texto: Inter 16 px · Números e código: JetBrains Mono

### 4. Movimento
- Entrada: cartões sobem 8 px e aparecem em 300 ms, com 60 ms entre um e outro
- Trabalhando: borda amarela pulsa a cada 1,6 s; ponto de status pisca devagar
- Ao concluir: brilho amarelo de 600 ms e o contador sobe contando
- prefers-reduced-motion: sem animação, estado final parado

### 5. Densidade e forma
- Densidade média · 3 cartões por linha no computador, 1 no celular
- Cantos 14 px nos cartões, 10 px nos botões · sem sombra: borda de 1 px `#272730`
- Celular (390 px): caixa de comando fixa embaixo, sem rolagem para o lado

### 6. Proibido
- Gradiente roxo, neon azul, mais de uma cor de destaque, emoji no meio do texto,
  robô cartoon, letra menor que 14 px

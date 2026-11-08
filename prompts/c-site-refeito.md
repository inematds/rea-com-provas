# Construção C — Site refeito

**O que sai:** uma versão premium do SEU site, com as SUAS palavras, a partir de um mapa
provado do site que existe hoje (seções, fontes, scripts, botões).

**Só para site seu** (ou de quem te autorizou por escrito). Site de outra empresa: estude
para aprender, mas não publique a cópia.

**Antes de colar:** troque tudo que está entre [colchetes] e preencha o brief de design
(`brief/MODELO-brief-design.md`).

## Jeito 1 — sem instalar nada (salvar a página)

```bash
mkdir -p ~/estudo/meu-site && cd ~/estudo/meu-site
curl -sL [https://seu-site.com.br] -o site-salvo.html
python3 -c "t=open('site-salvo.html',encoding='utf-8').read(); open('site-linhas.html','w',encoding='utf-8').write(t.replace('><','>\n<'))"
```

A segunda linha quebra o HTML (que costuma vir numa linha só) em uma tag por linha. O agente
lê o `site-linhas.html` e cita as linhas dele no provas.md.

## Jeito 2 — com o REA (vê scripts, rede e a tela de verdade)

Instalação do REA e do harness: guia https://inematds.github.io/rea-sem-travas/guia/.
Abra um Chrome separado, só no seu computador, e peça ao REA para olhar a página:

```bash
google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/rea-browser-profile [https://seu-site.com.br]
npx -y rea-agents@latest list-browser-targets http://127.0.0.1:9222 --json
npx -y rea-agents@latest inspect-web-page http://127.0.0.1:9222 [TARGET_ID] --json > rea-pagina.json
npx -y rea-agents@latest capture-web-screenshot http://127.0.0.1:9222 [TARGET_ID] --json > rea-print.json
```

O `[TARGET_ID]` sai do `list-browser-targets`. Feche esse Chrome no fim.

---

```text
Você vai trabalhar em duas fases. Não pule a fase 1.

FASE 1 — MAPEAR COM PROVAS (não escreva o site novo ainda)
Este é o MEU site: [https://seu-site.com.br]. O material salvo está em
[pasta, ex.: ~/estudo/meu-site] (site-linhas.html e, se houver, rea-pagina.json).
Faça o mapa do site:
- Seções da página, na ordem, com o título de cada uma.
- Fontes usadas (nome e onde são carregadas).
- Cores principais.
- Scripts próprios e de terceiros (analytics, chat, pixel), separando os dois.
- Botões e links de ação (texto do botão e para onde vai).
- Textos que são a minha voz (frases que devem continuar na versão nova).

Regras do mapa:
1. Na seção "## Alvo" do provas.md escreva "Licença: site próprio de [seu nome ou empresa]".
2. Scripts de terceiros (pixel, chat, analytics, frameworks) são biblioteca: anote que
   existem, mas as conclusões sobre o site têm de citar o HTML da página.
3. Entregue o provas.md no formato de provas/MODELO-provas.md: "## Conclusões" com
   "### C1. ..." e, em cada uma, "Prova:" = `site-linhas.html:linha` (ou o campo do
   rea-pagina.json) e "Trecho:", e a seção "## O que NÃO deu para provar"
   (ex.: o que só aparece depois de login ou de rolar a página).
4. Rode: python3 [caminho]/confere_provas.py provas.md — até sair APROVADO.
Pare aqui e me mostre o mapa e o resultado do conferidor.

FASE 2 — A VERSÃO PREMIUM (só depois que eu disser "pode construir")
Construa do zero, na pasta [pasta, ex.: ~/estudo/meu-site/versao-nova], um único
index.html (HTML + CSS + JavaScript, sem servidor) com:
- As mesmas seções e os mesmos botões de ação do mapa (mesmos destinos).
- As minhas palavras: reaproveite os textos marcados como "minha voz"; o resto você
  pode reescrever mais curto e mais claro, sem inventar fato, preço ou promessa.
- O visual do brief de design em [caminho do brief preenchido].
- Funciona no celular (390 px) sem rolagem para o lado.
- Sem scripts de terceiros (eu coloco depois os que eu quiser manter).
No fim, me diga como abrir, o que mudou em relação ao site atual e o que ficou de fora.
```

---

**Conferir:** `python3 confere_provas.py provas.md` tem de sair `APROVADO` antes da fase 2.

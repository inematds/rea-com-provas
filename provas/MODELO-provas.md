# Provas — [nome do app estudado]

> Modelo do arquivo que o agente TEM de entregar antes de construir qualquer coisa.
> Copie para `provas.md` na pasta do trabalho e peça ao agente para preencher.
> Depois confira: `python3 confere_provas.py provas.md`

## Alvo

- App estudado: [nome e endereço do código, ex.: github.com/[dono]/[app]]
- Licença: [MIT, Apache-2.0, GPL-3.0… e o arquivo onde ela está, ex.: `LICENSE`]
- Versão / commit: [ex.: v1.4.2 ou commit a1b2c3d]
- Pastas ignoradas: node_modules, vendor, site-packages, dist-packages
- Pergunta: [o que você quer entender, ex.: "como o app mostra vários agentes lado a lado"]

## Conclusões

Uma conclusão por bloco `###`. Cada uma precisa de pelo menos UMA prova no código do
próprio app: caminho do arquivo entre crases, de preferência com a linha
(`src/painel/Grade.tsx:40-62`), e o trecho que mostra a conclusão.

### C1. [frase curta: o que o app faz]

- Prova: `[caminho/do/arquivo.ext:linha-inicial-linha-final]`
- Trecho: `[3 a 10 palavras copiadas do arquivo]`
- Confiança: [alta | média | baixa]

### C2. [outra conclusão]

- Prova: `[caminho/do/arquivo.ext:linha]`
- Trecho: `[trecho]`
- Confiança: [alta | média | baixa]

## O que NÃO deu para provar

Tudo o que o agente acha, mas não achou no código. Esta seção é obrigatória.
Se nada ficou de fora, escreva o que foi checado para ter certeza.

- [ex.: não achei onde o app guarda o histórico; pode estar no servidor]
- [ex.: a animação do cartão parece CSS, mas o arquivo está minificado]

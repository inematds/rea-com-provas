#!/usr/bin/env python3
"""confere_provas.py — confere um provas.md antes de você acreditar no agente.

Uso:
    python3 confere_provas.py provas.md          # relatório em texto
    python3 confere_provas.py provas.md --json   # mesmo resultado em JSON

Reprova (código de saída 1) quando:
  1. falta a seção "O que NÃO deu para provar" (ou ela está vazia);
  2. alguma conclusão (bloco ### dentro de "## Conclusões") não cita arquivo/trecho;
  3. as referências apontam só para bibliotecas (node_modules, vendor, site-packages...).
Aprova (código 0) quando nada disso acontece. Erro de leitura = código 2.

Só biblioteca padrão do Python 3.8+. Não usa rede, não muda nenhum arquivo.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from dataclasses import dataclass, field

# Pastas que são código de terceiros embutido, não o app.
PASTAS_BIBLIOTECA = {
    "node_modules", "vendor", "vendors", "site-packages", "dist-packages",
    "bower_components", "third_party", "third-party", ".venv", "venv", "pods",
}

# Títulos aceitos (sem acento, minúsculo). PT é o padrão; EN/ES para quem traduziu o modelo.
TITULOS_SEM_PROVA = ("deu para provar", "could not be proven", "couldn't be proven",
                     "no se pudo probar")
TITULOS_CONCLUSOES = ("conclusoes", "conclusions", "conclusiones")

# Referência entre crases: `src/a.ts`, `src/a.ts:12`, `src/a.ts:12-30`, `LICENSE`, `app.py:4`
RE_CRASE = re.compile(r"`([^`\n]+)`")
RE_REF = re.compile(r"^(?P<caminho>[\w.@~+/-]*[\w-](?:\.[\w]{1,10})?)(?::(?P<linha>\d+)(?:-\d+)?)?$")
# Referência solta (sem crase): precisa de barra E extensão, ex.: src/painel/Grade.tsx:40
RE_REF_SOLTA = re.compile(r"(?<![\w`/])((?:[\w.@-]+/)+[\w.@-]+\.\w{1,10}(?::\d+(?:-\d+)?)?)")


def _norm(texto: str) -> str:
    sem_acento = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return sem_acento.lower().strip()


def _eh_referencia(token: str) -> bool:
    token = token.strip()
    if not token or " " in token or token.startswith(("[", "http://", "https://")):
        return False
    m = RE_REF.match(token)
    if not m:
        return False
    caminho = m.group("caminho")
    # precisa parecer arquivo: ter barra, ou extensão, ou ser um nome clássico de arquivo
    return "/" in caminho or re.search(r"\.\w{1,10}$", caminho) is not None or caminho.upper() in {
        "LICENSE", "COPYING", "MAKEFILE", "DOCKERFILE", "README"}


def _eh_biblioteca(ref: str) -> bool:
    partes = [p.lower() for p in ref.split(":")[0].split("/")]
    return any(p in PASTAS_BIBLIOTECA for p in partes)


def extrair_referencias(texto: str) -> list[str]:
    refs: list[str] = []
    for token in RE_CRASE.findall(texto):
        if _eh_referencia(token):
            refs.append(token.strip())
    sem_crase = RE_CRASE.sub(" ", texto)
    refs.extend(RE_REF_SOLTA.findall(sem_crase))
    return refs


@dataclass
class Conclusao:
    titulo: str
    corpo: str = ""
    refs: list[str] = field(default_factory=list)


@dataclass
class Resultado:
    nota: int
    aprovado: bool
    falhas: list[str]
    avisos: list[str]
    conclusoes: int
    com_prova_no_app: int

    def como_dict(self) -> dict:
        return {
            "nota": self.nota, "aprovado": self.aprovado, "falhas": self.falhas,
            "avisos": self.avisos, "conclusoes": self.conclusoes,
            "com_prova_no_app": self.com_prova_no_app,
        }


def _secoes(texto: str) -> list[tuple[str, str]]:
    """Divide o markdown em (titulo ##, corpo). Ignora o que está em blocos ```."""
    secoes: list[tuple[str, list[str]]] = []
    atual: tuple[str, list[str]] | None = None
    em_codigo = False
    for linha in texto.splitlines():
        if linha.strip().startswith("```"):
            em_codigo = not em_codigo
        if not em_codigo and re.match(r"^##\s+(?!#)", linha):
            atual = (linha[2:].strip(), [])
            secoes.append(atual)
        elif atual is not None:
            atual[1].append(linha)
    return [(t, "\n".join(c)) for t, c in secoes]


def _conclusoes(corpo: str) -> list[Conclusao]:
    lista: list[Conclusao] = []
    for linha in corpo.splitlines():
        if re.match(r"^###\s+", linha):
            lista.append(Conclusao(titulo=linha[3:].strip()))
        elif lista:
            lista[-1].corpo += linha + "\n"
    for c in lista:
        c.refs = extrair_referencias(c.titulo + "\n" + c.corpo)
    return lista


def _tem_item(corpo: str) -> bool:
    for linha in corpo.splitlines():
        s = linha.strip()
        if s.startswith(("- ", "* ", "+ ")) or re.match(r"^\d+[.)]\s", s):
            item = re.sub(r"^([-*+]|\d+[.)])\s+", "", s)
            if item and not item.startswith("["):  # placeholder do modelo não vale
                return True
    return False


def conferir(texto: str) -> Resultado:
    falhas: list[str] = []
    avisos: list[str] = []
    secoes = _secoes(texto)

    # Regra 1: seção do que não deu para provar
    sem_prova = [c for t, c in secoes if any(k in _norm(t) for k in TITULOS_SEM_PROVA)]
    faltou_secao = False
    if not sem_prova:
        faltou_secao = True
        falhas.append('Falta a seção "## O que NÃO deu para provar". Peça ao agente: '
                      '"liste o que você acha mas não achou no código".')
    elif not _tem_item(sem_prova[0]):
        faltou_secao = True
        falhas.append('A seção "O que NÃO deu para provar" está vazia (ou só tem o exemplo do '
                      'modelo). Se nada ficou de fora, peça para escrever o que foi checado.')

    # Conclusões
    corpos = [c for t, c in secoes if _norm(t).startswith(TITULOS_CONCLUSOES)]
    conclusoes: list[Conclusao] = []
    if not corpos:
        falhas.append('Falta a seção "## Conclusões" com uma conclusão por bloco "###".')
    else:
        conclusoes = _conclusoes(corpos[0])
        if not conclusoes:
            falhas.append('A seção "## Conclusões" não tem nenhuma conclusão (blocos "### C1. ...").')

    # Regra 2: cada conclusão com referência
    todas_refs: list[str] = []
    com_prova_no_app = 0
    for i, c in enumerate(conclusoes, 1):
        nome = c.titulo if len(c.titulo) <= 70 else c.titulo[:67] + "..."
        if "[" in c.titulo and "]" in c.titulo:
            avisos.append(f'"{nome}": o título ainda tem [colchetes] do modelo.')
        if not c.refs:
            falhas.append(f'"{nome}": conclusão sem prova. Falta o arquivo/trecho '
                          '(ex.: `src/arquivo.ts:40-62`).')
            continue
        todas_refs.extend(c.refs)
        do_app = [r for r in c.refs if not _eh_biblioteca(r)]
        if do_app:
            com_prova_no_app += 1
            if not any(":" in r for r in do_app):
                avisos.append(f'"{nome}": a prova não diz a linha (use `arquivo.ext:linha`).')
        else:
            avisos.append(f'"{nome}": só cita biblioteca embutida; mostre onde o PRÓPRIO app usa isso.')

    # Regra 3: referências só em bibliotecas
    if todas_refs and all(_eh_biblioteca(r) for r in todas_refs):
        falhas.append("Todas as referências apontam para bibliotecas (node_modules, vendor, "
                      "site-packages...). Mande o agente ignorar essas pastas e provar no código do app.")

    # Avisos extras do modelo
    alvo = [c for t, c in secoes if _norm(t).startswith(("alvo", "target", "objetivo"))]
    if not alvo or not re.search(r"licen[cç]|license|licencia", alvo[0], re.I):
        avisos.append('Sem a linha "Licença:" em "## Alvo". Confira se você pode estudar esse app.')

    total = len(conclusoes)
    nota = round(10 * com_prova_no_app / total) if total else 0
    if faltou_secao:
        nota = min(nota, 4)
    nota = max(0, min(10, nota - (1 if any("sem prova" in f for f in falhas) else 0)))
    aprovado = not falhas
    if not aprovado:
        nota = min(nota, 6)
    return Resultado(nota, aprovado, falhas, avisos, total, com_prova_no_app)


def relatorio(r: Resultado) -> str:
    linhas = [f"NOTA {r.nota}/10 — {'APROVADO' if r.aprovado else 'REPROVADO'}",
              f"Conclusões: {r.conclusoes} · com prova no código do app: {r.com_prova_no_app}"]
    if r.falhas:
        linhas.append("\nO que falta (reprova):")
        linhas += [f"  ✗ {f}" for f in r.falhas]
    if r.avisos:
        linhas.append("\nAvisos (não reprova, mas melhore):")
        linhas += [f"  ! {a}" for a in r.avisos]
    if r.aprovado and not r.avisos:
        linhas.append("\nTudo provado. Agora sim: peça a SUA versão.")
    return "\n".join(linhas)


def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 1 or "-h" in argv or "--help" in argv:
        print(__doc__.strip())
        return 2
    try:
        with open(args[0], encoding="utf-8") as f:
            texto = f.read()
    except OSError as e:
        print(f"Não consegui ler {args[0]}: {e}", file=sys.stderr)
        return 2
    r = conferir(texto)
    if "--json" in argv:
        print(json.dumps(r.como_dict(), ensure_ascii=False, indent=2))
    else:
        print(relatorio(r))
    return 0 if r.aprovado else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

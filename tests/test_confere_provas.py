"""Testes do conferidor. Sem rede. Rode: python3 -m unittest discover tests  (ou pytest)."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

import confere_provas as cp  # noqa: E402

BOM = """# Provas — app

## Alvo
- Licença: MIT (`LICENSE`)

## Conclusões

### C1. A grade usa CSS grid
- Prova: `src/Grade.tsx:10-20`
- Trecho: `display: grid`

### C2. O status vem por evento
- Prova: `src/status.ts:5`

## O que NÃO deu para provar
- Onde o histórico é salvo.
"""


class TestConferidor(unittest.TestCase):
    def test_bom_aprova(self):
        r = cp.conferir(BOM)
        self.assertTrue(r.aprovado, r.falhas)
        self.assertEqual(r.nota, 10)
        self.assertEqual(r.conclusoes, 2)

    def test_falta_secao_nao_deu_para_provar(self):
        texto = BOM.split("## O que NÃO deu para provar")[0]
        r = cp.conferir(texto)
        self.assertFalse(r.aprovado)
        self.assertTrue(any("NÃO deu para provar" in f for f in r.falhas), r.falhas)
        self.assertLessEqual(r.nota, 4)

    def test_secao_vazia_reprova(self):
        texto = BOM.replace("- Onde o histórico é salvo.", "")
        r = cp.conferir(texto)
        self.assertFalse(r.aprovado)
        self.assertTrue(any("vazia" in f for f in r.falhas), r.falhas)

    def test_conclusao_sem_referencia(self):
        texto = BOM.replace("- Prova: `src/status.ts:5`", "- Analisei e está claro.")
        r = cp.conferir(texto)
        self.assertFalse(r.aprovado)
        self.assertTrue(any("C2" in f and "sem prova" in f for f in r.falhas), r.falhas)
        self.assertEqual(r.com_prova_no_app, 1)

    def test_referencias_so_em_bibliotecas(self):
        texto = (BOM.replace("`src/Grade.tsx:10-20`", "`node_modules/grid/index.js:3`")
                    .replace("`src/status.ts:5`", "`vendor/events/bus.php:9`"))
        r = cp.conferir(texto)
        self.assertFalse(r.aprovado)
        self.assertTrue(any("bibliotecas" in f for f in r.falhas), r.falhas)
        self.assertEqual(r.nota, 0)

    def test_site_packages_conta_como_biblioteca(self):
        self.assertTrue(cp._eh_biblioteca(".venv/lib/python3.12/site-packages/flask/app.py:1"))
        self.assertFalse(cp._eh_biblioteca("app/vendors_page.py:4"))

    def test_dist_build_e_min_js_contam_como_biblioteca(self):
        self.assertTrue(cp._eh_biblioteca("dist/bundle.js:4"))
        self.assertTrue(cp._eh_biblioteca("build/static/main.js:2"))
        self.assertTrue(cp._eh_biblioteca("assets/jquery.min.js:1"))
        self.assertFalse(cp._eh_biblioteca("src/build.ts:3"))
        texto = (BOM.replace("`src/Grade.tsx:10-20`", "`dist/bundle.js:4`")
                    .replace("`src/status.ts:5`", "`assets/app.min.js:9`"))
        self.assertFalse(cp.conferir(texto).aprovado)

    def test_uma_biblioteca_e_uma_do_app_nao_reprova(self):
        texto = BOM.replace("`src/status.ts:5`", "`node_modules/sse/index.js:5`")
        r = cp.conferir(texto)
        self.assertTrue(r.aprovado, r.falhas)
        self.assertTrue(any("só cita biblioteca" in a for a in r.avisos), r.avisos)

    def test_titulo_em_ingles_e_espanhol(self):
        en = BOM.replace("## O que NÃO deu para provar", "## What could NOT be proven")
        es = BOM.replace("## O que NÃO deu para provar", "## Lo que NO se pudo probar")
        self.assertTrue(cp.conferir(en).aprovado)
        self.assertTrue(cp.conferir(es).aprovado)

    def test_modelo_em_branco_reprova(self):
        texto = (RAIZ / "provas" / "MODELO-provas.md").read_text(encoding="utf-8")
        r = cp.conferir(texto)
        self.assertFalse(r.aprovado, "o modelo sem preencher não pode passar")


class TestExemplosPelaLinhaDeComando(unittest.TestCase):
    def rodar(self, arquivo, *extra):
        return subprocess.run([sys.executable, str(RAIZ / "confere_provas.py"), str(arquivo), *extra],
                              capture_output=True, text=True, timeout=30)

    def test_exemplo_bom_aprova(self):
        p = self.rodar(RAIZ / "exemplos" / "provas-boa.md")
        self.assertEqual(p.returncode, 0, p.stdout)
        self.assertIn("APROVADO", p.stdout)

    def test_exemplo_ruim_reprova(self):
        p = self.rodar(RAIZ / "exemplos" / "provas-ruim.md", "--json")
        self.assertEqual(p.returncode, 1, p.stdout)
        d = json.loads(p.stdout)
        self.assertFalse(d["aprovado"])
        textos = " ".join(d["falhas"])
        self.assertIn("NÃO deu para provar", textos)
        self.assertIn("sem prova", textos)
        self.assertIn("bibliotecas", textos)

    def test_arquivo_inexistente_sai_2(self):
        p = self.rodar(RAIZ / "nao-existe.md")
        self.assertEqual(p.returncode, 2)


if __name__ == "__main__":
    unittest.main()

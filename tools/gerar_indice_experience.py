"""Gera o catálogo do JET Experience a partir da API pública do portal.

Por que existe: o JET Experience tem 273 tutoriais e é a documentação oficial da
plataforma. Sem um índice local, toda dúvida vira busca manual no portal e o
mesmo artigo é redescoberto várias vezes.

Por que só o índice: o rodapé do portal proíbe reprodução parcial ou total sem
autorização da JET. Título, categoria, data e URL são metadados factuais e podem
viver aqui; o texto do artigo não. Quando um artigo for necessário, leia no
portal e escreva a afirmação canônica com as nossas palavras em
`docs/canonical/knowledge-base.md`, citando a URL como evidência.

Uso:
    python tools/gerar_indice_experience.py
"""
from __future__ import annotations

import html
import json
import re
import sys
import unicodedata
import urllib.request
from collections import defaultdict
from pathlib import Path

BASE = "https://experience.jet.com.br"
RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "docs" / "sources" / "experience-index.md"
INVENTARIO = RAIZ / "docs" / "canonical" / "admin-module-inventory.md"

for _f in (sys.stdout, sys.stderr):  # console do Windows é cp1252
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")


def _get(caminho: str) -> list[dict]:
    req = urllib.request.Request(BASE + caminho,
                                 headers={"User-Agent": "jet-knowledge/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def _limpo(t: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", t)).replace("–", "-").strip()


def _chave(t: str) -> str:
    """Normaliza para casar título de artigo com nome de módulo do painel."""
    t = unicodedata.normalize("NFKD", t.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9 ]+", " ", t)


def coletar() -> tuple[list[dict], dict[int, str]]:
    cats = {c["id"]: c["name"] for c in _get("/wp-json/wp/v2/categories?per_page=100")}
    posts: list[dict] = []
    pagina = 1
    while True:
        campos = "id,slug,link,date,modified,title,categories"
        lote = _get(f"/wp-json/wp/v2/posts?per_page=100&page={pagina}&_fields={campos}")
        if not lote:
            break
        posts.extend(lote)
        if len(lote) < 100:
            break
        pagina += 1
    return posts, cats


def modulos_do_painel() -> list[str]:
    """Nomes de módulo extraídos da primeira coluna das tabelas do inventário."""
    if not INVENTARIO.exists():
        return []
    nomes = []
    for linha in INVENTARIO.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*([^|]+?)\s*\|\s*(COBERTO|PARCIAL|⚠ LACUNA|LACUNA)", linha)
        if m:
            nomes.append(m.group(1).replace("`", "").strip())
    return nomes


def main() -> None:
    posts, cats = coletar()
    linhas = []
    for p in posts:
        linhas.append({
            "titulo": _limpo(p["title"]["rendered"]),
            "pub": p["date"][:10],
            "cats": [cats.get(i, str(i)) for i in p.get("categories", [])],
            "url": p["link"],
        })
    linhas.sort(key=lambda x: x["pub"], reverse=True)

    por_cat: dict[str, list[dict]] = defaultdict(list)
    for x in linhas:
        for c in x["cats"]:
            por_cat[c].append(x)

    # roteamento módulo do painel -> artigo, por casamento de nome normalizado
    mods = modulos_do_painel()
    rotas: list[tuple[str, list[dict]]] = []
    for m in mods:
        km = _chave(m)
        # descarta qualificadores entre parênteses e sufixos de área
        km = re.sub(r"\s+", " ", km).strip()
        achados = [x for x in linhas if km and (km in _chave(x["titulo"])
                                                or _chave(x["titulo"]) in km)]
        rotas.append((m, achados[:3]))

    sem_artigo = [m for m, a in rotas if not a]

    out = [
        "# Catálogo do JET Experience",
        "",
        f"{len(linhas)} tutoriais publicados em `{BASE}` — documentação oficial da",
        "plataforma JET. Gerado por `tools/gerar_indice_experience.py`.",
        "",
        "## O que este arquivo é, e o que não é",
        "",
        "É um **catálogo**: título, categoria, data de publicação e URL. Serve para",
        "achar rápido o artigo certo e para saber o que a JET documenta.",
        "",
        "Não é uma cópia do conteúdo. O portal proíbe reprodução sem autorização, e",
        "além disso conteúdo copiado envelhece calado. Ao usar um artigo, leia no",
        "portal, escreva a afirmação com as nossas palavras em",
        "`docs/canonical/knowledge-base.md` e cite a URL como evidência.",
        "",
        "## Cuidado com a data",
        "",
        "A data mostrada é a de **publicação**. O portal migrou e carimbou quase todo",
        "o acervo com a mesma data de modificação, então `modified` não diz nada sobre",
        "atualidade. Artigo antigo pode descrever tela que não existe mais — vale a",
        "guardrail 6 do `CLAUDE.md`: afirmação temporal expira.",
        "",
        "## Roteamento: módulo do painel → tutorial",
        "",
        "Casamento por nome entre os módulos de `admin-module-inventory.md` e os",
        "títulos dos tutoriais. É um ponto de partida para a varredura, não uma",
        "afirmação de que o artigo cobre o módulo por completo.",
        "",
        "| Módulo do painel | Tutorial | Publicado |",
        "|---|---|---|",
    ]
    for m, achados in rotas:
        if not achados:
            continue
        for i, a in enumerate(achados):
            out.append(f"| {m if i == 0 else ''} | [{a['titulo']}]({a['url']}) | {a['pub']} |")

    out += [
        "",
        f"### Módulos sem tutorial de nome equivalente ({len(sem_artigo)})",
        "",
        "Não significa ausência de documentação — pode estar sob outro título ou",
        "dentro de um artigo maior. Significa que a busca por nome não resolve e",
        "alguém precisa procurar (ou perguntar à JET) antes de operar o módulo.",
        "",
    ]
    out += [f"- {m}" for m in sem_artigo]

    out += ["", "## Catálogo por categoria", ""]
    for c in sorted(por_cat, key=lambda k: -len(por_cat[k])):
        out += [f"### {c} ({len(por_cat[c])})", "",
                "| Tutorial | Publicado |", "|---|---|"]
        for x in por_cat[c]:
            out.append(f"| [{x['titulo']}]({x['url']}) | {x['pub']} |")
        out.append("")

    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    SAIDA.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(linhas)} tutoriais, {len(por_cat)} categorias -> {SAIDA}")
    print(f"módulos sem tutorial de nome equivalente: {len(sem_artigo)}")


if __name__ == "__main__":
    main()

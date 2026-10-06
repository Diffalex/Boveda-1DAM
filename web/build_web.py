#!/usr/bin/env python3
"""Generador del sitio web estático de la bóveda 1DAM.

Convierte las notas de Obsidian (Markdown + wikilinks + callouts) a un sitio
HTML estático, sin dependencias externas. La bóveda no se modifica: la salida
se escribe solo en la carpeta web/ (este mismo directorio).

Uso:
    python3 web/build_web.py

Salida:
    web/index.html            portada + buscador
    web/index.json            índice para el buscador
    web/assets/style.css      estilos
    web/assets/app.js         buscador client-side
    web/<seccion>/<nota>.html páginas de cada nota
    web/anexos/               PDFs fuente de Anexos (con su índice)
"""
import html
import json
import os
import re
import shutil
import sys
import unicodedata
from pathlib import Path
from urllib.parse import quote

SCRIPT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = SCRIPT_DIR.parent
OUT_DIR = SCRIPT_DIR

SECTION_ORDER = [
    "00 - General",
    "Programación",
    "Sistemas informáticos",
    "Bases de datos",
    "Entornos de desarrollo",
    "Lenguajes de marcas",
    "Sostenibilidad",
    "Prevención de riesgos laborales",
    "Digitalización",
]

CALLOUT_LABELS = {
    "note": "Nota",
    "tip": "Tip",
    "important": "Importante",
    "warning": "Aviso",
    "info": "Info",
    "danger": "Peligro",
}

_ESCAPE = re.compile(r"[^0-9A-Za-zÀ-ÖØ-öø-ÿ_\-\s]")


def slugify(text, keep_unicode=True):
    """Convierte un texto en slug usable para anclas / nombres de fichero."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^0-9a-z_\- ]", "", text).strip()
    text = re.sub(r"\s+", "-", text)
    return text


def esc(text):
    return html.escape(text, quote=False)


# ----------------------------------------------------------------------------
# Frontmatter
# ----------------------------------------------------------------------------

def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm = text[4:end]
    body = text[end + len("\n---") :]
    meta = {}
    tags = []
    current_list = None
    for raw in fm.splitlines():
        if not raw.strip():
            continue
        m = re.match(r"^([\w\-]+):\s*(.*)$", raw)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if key == "tags":
                current_list = tags
            current_list = None
            if key != "tags":
                meta[key] = val.strip("\" '")
        else:
            m2 = re.match(r"^\s*-\s*(.*)$", raw)
            if m2 and current_list is not None:
                current_list.append(m2.group(1).strip())
    meta["tags"] = tags
    return meta, body.lstrip("\n")


def note_title(meta, body, stem):
    m = re.search(r"^\s*#\s+(.+)$", body, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return meta.get("tema") or stem


# ----------------------------------------------------------------------------
# Conversor Markdown -> HTML (bloques)
# ----------------------------------------------------------------------------

def render_markdown(text, ctx):
    lines = text.splitlines()
    out = []
    i = 0
    n = len(lines)

    def flush(p):
        out.append(p)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # Fenced code
        m = re.match(r"^(```|~~~)\s*([\w+-]*)\s*$", stripped)
        if m:
            fence = m.group(1)
            lang = m.group(2) or "text"
            j = i + 1
            buf = []
            while j < n and not lines[j].startswith(fence):
                buf.append(lines[j])
                j += 1
            j += 1  # skip closing fence (or EOF)
            code = "\n".join(buf)
            flush(f'<pre class="code"><code class="language-{esc(lang)}">{esc(code)}</code></pre>')
            i = j
            continue

        # Code fences that start with backspaces inside? (none in vault)

        # Table
        if i + 1 < n and stripped.startswith("|") and "|" in lines[i + 1]:
            rows = []
            j = i
            while j < n and lines[j].strip().startswith("|"):
                cells = [c.strip() for c in lines[j].strip().strip("|").split("|")]
                rows.append(cells)
                j += 1
            if len(rows) >= 2 and all(re.fullmatch(r":?-+:?", c or "-") for c in rows[1]):
                header, body = rows[0], rows[2:]
            else:
                header, body = rows[0], rows[1:]
            t = ["<table>"]
            if header:
                t.append("<thead><tr>" + "".join(f"<th>{inline(c, ctx)}</th>" for c in header) + "</tr></thead>")
            if body:
                t.append("<tbody>")
                for row in body:
                    if len(row) == 1 and not row[0]:
                        continue
                    pad = len(header) - len(row)
                    t.append("<tr>" + "".join(f"<td>{inline(c, ctx)}</td>" for c in row))
                    if pad > 0:
                        t.append("<td></td>" * pad)
                    t.append("</tr>")
                t.append("</tbody>")
            t.append("</table>")
            flush("".join(t))
            i = j
            continue

        # Blockquote / callout
        if stripped.startswith(">"):
            j = i
            buf = []
            while j < n and lines[j].startswith(">"):
                buf.append(lines[j])
                j += 1
            inner = []
            for bl in buf:
                tmp = bl[1:]
                if tmp.startswith(" "):
                    tmp = tmp[1:]
                inner.append(tmp)
            m = re.match(r"^\[!(\w+)\]\s*(.*)$", inner[0].strip())
            if m:
                ctype = m.group(1).lower()
                ctitle = m.group(2).strip() or CALLOUT_LABELS.get(ctype, ctype.capitalize())
                cbody = render_markdown("\n".join(inner[1:]), ctx).strip()
                flush(
                    '<div class="callout callout-' + esc(ctype) + '">'
                    '<div class="callout-title">' + esc(ctitle) + "</div>"
                    '<div class="callout-body">' + cbody + "</div></div>"
                )
            else:
                cbody = render_markdown("\n".join(inner), ctx).strip()
                flush("<blockquote>" + cbody + "</blockquote>")
            i = j
            continue

        # Heading
        m = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if m:
            level = len(m.group(1))
            text = inline(m.group(2), ctx)
            ident = slugify(text)
            flush(f"<h{level} id='{ident}'>{text}</h{level}>")
            i += 1
            continue

        # Horizontal rule
        if re.fullmatch(r"[-*_]{3,}", stripped):
            flush("<hr>")
            i += 1
            continue

        # List (single level)
        if re.match(r"^(\s*)([-*+]|\d+[.)])\s+", line):
            ordered = re.match(r"^\s*\d+[.)]", line) is not None
            m = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", line)
            indent0 = len(m.group(1))
            items = []
            while i < n:
                lm = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", lines[i])
                if not lm or len(lm.group(1)) != indent0:
                    break
                marker = lm.group(2)
                item_text = lm.group(3)
                is_ordered = re.match(r"^\d+[.)]", marker) is not None
                if is_ordered != ordered:
                    break
                items.append(render_list_item(item_text, ctx))
                i += 1
            tag = "ol" if ordered else "ul"
            flush(f"<{tag}>" + "".join(f"<li>{it}</li>" for it in items) + f"</{tag}>")
            continue

        # Paragraph
        j = i
        buf = []
        while j < n:
            s = lines[j].strip()
            if not s:
                break
            if s.startswith("|") and j + 1 < n and "|" in lines[j + 1]:
                break
            if s.startswith(">"):
                break
            if re.match(r"^(#{1,6})\s", s):
                break
            if re.fullmatch(r"[-*_]{3,}", s):
                break
            if re.match(r"^(\s*)([-*+]|\d+[.)])\s+", lines[j]):
                break
            buf.append(lines[j])
            j += 1
        if buf:
            para = " ".join(b.strip() for b in buf)
            flush(f"<p>{inline(para, ctx)}</p>")
        i = j

    return "\n".join(out)


def render_list_item(item_text, ctx):
    m = re.match(r"^\[([ xX])\]\s*(.*)$", item_text)
    if m:
        checked = m.group(1).lower() == "x"
        inner = inline(m.group(2), ctx)
        cb = f'<input type="checkbox" disabled{" checked" if checked else ""}> '
        return f'<span class="task">' + cb + inner + "</span>"
    return inline(item_text, ctx)


# ----------------------------------------------------------------------------
# Inline: wikilinks, links, código, negrita/cursiva
# ----------------------------------------------------------------------------

def inline_label(text):
    """Énfasis solo, para etiquetas de enlace (sin volver a escapar todo)."""
    text = esc(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


def inline(text, ctx):
    text = esc(text)
    codes = []

    def save_code(m):
        codes.append(m.group(1))
        return f"\x00C{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", save_code, text)

    toks = []

    def wl(m):
        target = m.group(1).strip()
        disp = (m.group(2) or "").strip()
        frag = ""
        if "#" in target:
            target, frag = target.split("#", 1)
        base = target.split("/")[-1].strip()
        href, ok = resolve(ctx, base, frag)
        if not ok:
            toks.append(f'<span class="wl-missing">[[{esc(target)}]]</span>')
        else:
            label = inline_label(disp or base)
            toks.append(f'<a href="{href}">{label}</a>')
        return f"\x00L{len(toks) - 1}\x00"

    def md_link(m):
        label = m.group(1)
        url = m.group(2)
        toks.append(f'<a href="{esc(url)}">{inline_label(label)}</a>')
        return f"\x00L{len(toks) - 1}\x00"

    text = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]*))?\]\]", wl, text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", md_link, text)

    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)

    for i, t in enumerate(toks):
        text = text.replace(f"\x00L{i}\x00", t)
    for i, c in enumerate(codes):
        text = text.replace(f"\x00C{i}\x00", f"<code>{c}</code>")
    return text


# ----------------------------------------------------------------------------
# Páginas
# ----------------------------------------------------------------------------

sections = {}
notes = {}
by_name = {}
name_conflicts = set()


def discover():
    global sections, notes, by_name, name_conflicts
    sections = {}
    notes = {}
    by_name = {}
    name_conflicts = set()

    for entry in sorted(VAULT_ROOT.iterdir()):
        if not entry.is_dir() or entry.name.startswith(".") or entry.name == OUT_DIR.name:
            continue
        sections[entry.name] = []

    md_files = sorted(VAULT_ROOT.rglob("*.md"))
    for p in md_files:
        rel = p.relative_to(VAULT_ROOT)
        if any(part.startswith(".") for part in rel.parts):
            continue
        if rel.parts[0] == OUT_DIR.name:
            continue
        section = rel.parts[0] if len(rel.parts) > 1 else "Inicio"
        if section.startswith(".") or section == OUT_DIR.name:
            continue
        if section not in sections:
            sections[section] = []
        sections[section].append(p)
        stem = p.stem
        if stem in by_name:
            name_conflicts.add(stem)
        else:
            by_name[stem] = (section, p)

    bases = []
    for section, files in sections.items():
        for p in files:
            stem = p.stem
            if name_conflicts and stem in name_conflicts:
                # páginas con nombre repetido: se desambiguan con la sección
                note_file = OUT_DIR / section / (section + " - " + stem + ".html")
            else:
                note_file = OUT_DIR / section / (stem + ".html")
            bases.append((stem, quote(str((OUT_DIR / section))), note_file))
    return bases


def build_context():
    from types import SimpleNamespace
    return SimpleNamespace(by_name=by_name, notes=[], page=None)


def resolve(ctx, base, frag):
    if base not in ctx.by_name:
        return None, False
    sec, p = ctx.by_name[base]
    target_root = OUT_DIR / sec
    if base in name_conflicts:
        fname = sec + " - " + base + ".html"
    else:
        fname = base + ".html"
    target = target_root / fname
    page_dir = ctx.page.parent if ctx.page else OUT_DIR
    href = os.path.relpath(target, page_dir)
    href = quote(href)
    if frag:
        href += "#" + slugify(frag)
    return href, True


def collect_pdfs(section):
    base = VAULT_ROOT / section
    pdfs = []
    for anexo in sorted((base / "Anexos").glob("*.pdf"), key=lambda x: x.name.lower()):
        pdfs.append(anexo.name)
    return pdfs


THEME_BOOT = """<script>
try { if (localStorage.getItem("t") === "dark") document.documentElement.dataset.theme = "dark"; } catch (e) {}
</script>"""

THEME_BTN = '<button id="theme" class="theme-btn" type="button"></button>'


def body_end(prefix=""):
    return f'<script src="{prefix}assets/app.js"></script>\n</body>'


def page_html(title, section, body, ctx, meta):
    breadcrumb = f'<a href="../index.html">Inicio</a> &rsaquo; {esc(section)}'
    if section == "Inicio":
        breadcrumb = '<a href="../index.html">Inicio</a>'
    tags = meta.get("tags", [])
    tag_html = ""
    if tags:
        tag_html = '<div class="tags">' + "".join(f'<span class="tag">{esc(t)}</span>' for t in tags) + "</div>"
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} · Bóveda 1DAM</title>
{THEME_BOOT}
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<header class="topbar">
  <div class="wrap">
    <a class="brand" href="../index.html">Bóveda 1DAM</a>
    <nav class="crumbs">{breadcrumb}</nav>
    {THEME_BTN}
  </div>
</header>
<main class="wrap">
  <article>
    {tag_html}
    {body}
  </article>
  <footer class="site-foot">
    <p>Apuntes de 1º DAM · {esc(section)}</p>
    <p><a href="../index.html">Inicio</a> · <a href="../anexos/index.html">Fuentes y PDFs</a> · <a href="../index.html#notas">Todas las notas</a></p>
  </footer>
</main>
{body_end("../")}
</html>"""


def main():
    global by_name, name_conflicts
    discover()
    ctx = build_context()
    meta_cache = {}

    # pre-cargar metadatos y cuerpo de cada nota
    parsed = {}
    for base, (sec, p) in by_name.items():
        raw = p.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)
        parsed[base] = (sec, p, meta, body)

    search_index = []

    # portada: ordenar secciones
    order = {s: i for i, s in enumerate(SECTION_ORDER)}
    sections_sorted = sorted(sections.keys(), key=lambda s: (order.get(s, 100), s.lower()))

    pdf_list = {}

    for sec in sections_sorted:
        pdfs = collect_pdfs(sec)
        if pdfs:
            pdf_list[sec] = pdfs
            dest = OUT_DIR / "anexos" / sec
            dest.mkdir(parents=True, exist_ok=True)
            src = VAULT_ROOT / sec / "Anexos"
            for name in pdfs:
                shutil.copy2(src / name, dest / name)

    for sec in sections_sorted:
        out_sec = OUT_DIR / sec
        out_sec.mkdir(parents=True, exist_ok=True)

    for base, (sec, p, meta, body) in parsed.items():
        stem = p.stem
        if base in name_conflicts:
            fname = sec + " - " + stem + ".html"
        else:
            fname = stem + ".html"
        page_file = OUT_DIR / sec / fname
        title = note_title(meta, body, stem)
        ctx.page = page_file
        body_html = render_markdown(body, ctx)
        if stem.startswith("_Índice") and pdf_list.get(sec):
            links = "".join(f'<li><a href="../anexos/{quote(sec)}/{quote(name)}" target="_blank">{esc(name)}</a></li>' for name in pdf_list[sec])
            body_html += f'\n<h2 id="fuentes">Fuentes (PDF)</h2>\n<p>Documentos de apoyo de este tema (en <code>Anexos/</code> del curso):</p>\n<ul class="pdf-list">{links}</ul>'
        html_page = page_html(title, sec, body_html, ctx, meta)
        page_file.write_text(html_page, encoding="utf-8")
        plain = re.sub(r"[^\S\n]+", " ", re.sub(r"[#*_`>|\[\]!-]", " ", body))
        excerpt = re.sub(r"\s+", " ", plain).strip()[:1200]
        search_index.append({
            "t": title,
            "s": sec,
            "g": meta.get("tags", []),
            "u": f"{sec}/{fname}",
            "x": excerpt,
        })

    make_home(sections_sorted, search_index, pdf_list)
    make_anexos_index(pdf_list)

    (OUT_DIR / "index.json").write_text(json.dumps(search_index, ensure_ascii=False, indent=1), encoding="utf-8")
    Path(OUT_DIR / ".nojekyll").write_text("", encoding="utf-8")

    print(f"OK: {len(search_index)} notas · {sum(len(v) for v in pdf_list.values())} PDFs · {len(sections_sorted)} secciones")


def make_home(sections_sorted, search_index, pdf_list):
    cards = []
    by_sec = {}
    for item in search_index:
        by_sec.setdefault(item["s"], []).append(item)

    for sec in sections_sorted:
        items = by_sec.get(sec, [])
        idx = next((it for it in items if it["u"].startswith(sec + "/_Índice")), None)
        link = idx["u"] if idx else (items[0]["u"] if items else "#")
        if link != "#":
            link = quote(link)
        label = sec if sec != "Inicio" else "Acerca de / README"
        desc = "" if link == "#" else f"{len(items)} notas en {sec}"
        if sec == "Inicio":
            desc = "Información general de la bóveda y cómo está organizada."
        cards.append(
            f'<a class="card" href="{link}">'
            f'<h2>{esc(label)}</h2>'
            f"<p>{esc(desc) if desc else ''}</p>"
            f"</a>"
        )

    groups = []
    for sec in sections_sorted:
        items = by_sec.get(sec, [])
        lis = []
        for it in sorted(items, key=lambda d: d["t"].lower()):
            lis.append(f'<li><a href="{quote(it["u"])}">{esc(it["t"])}</a></li>')
        groups.append(
            f'<details class="group">'
            f'<summary><span class="g-name">{esc(sec)}</span> <span class="g-count">{len(lis)} nota{"s" if len(lis) != 1 else ""}</span></summary>'
            f'<ul class="note-list">{ "".join(lis) }</ul>'
            f"</details>"
        )

    total_pdfs = sum(len(v) for v in pdf_list.values())
    pdf_note = ""
    if total_pdfs:
        pdf_note = f'<p class="pdf-line">Fuentes y PDFs: <a href="anexos/index.html">{total_pdfs} documentos</a></p>'
    home = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bóveda 1DAM — Apuntes de 1º DAM</title>
{THEME_BOOT}
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="hero">
  <div class="wrap">
    <div class="hero-top">
      <div>
        <h1>Bóveda 1DAM</h1>
        <p class="sub">Apuntes de clase de 1º de DAM, compartidos como web para estudiarlos sin Obsidian.</p>
      </div>
      {THEME_BTN}
    </div>
    <div class="search-box">
      <input id="q" type="search" placeholder="Buscar en los apuntes…" autocomplete="off">
      <div id="results" class="results"></div>
    </div>
  </div>
</header>
<main class="wrap">
  <h2 class="section-title">Asignaturas</h2>
  <div class="cards"><!--CARDS--></div>
  {pdf_note}
  <h2 id="notas" class="section-title">Todas las notas (desplegables)</h2>
  <!--GROUPS-->
  <footer class="site-foot">
    <p>Contenido de la bóveda de Obsidian · <a href="https://github.com/Diffalex/Boveda-1DAM">repositorio GitHub</a></p>
  </footer>
</main>
{body_end()}
</html>"""
    home = home.replace("<!--CARDS-->", "\n  ".join(cards))
    home = home.replace("<!--GROUPS-->", "\n  ".join(groups))
    (OUT_DIR / "index.html").write_text(home, encoding="utf-8")


def make_anexos_index(pdf_list):
    sec_blocks = []
    for sec in sorted(pdf_list):
        links = "".join(f'<li><a href="{quote(sec)}/{quote(n)}" target="_blank">{esc(n)}</a></li>' for n in pdf_list[sec])
        sec_blocks.append(f"<section><h2>{esc(sec)}</h2><ul>{links}</ul></section>")
    html_page = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fuentes y PDFs · Bóveda 1DAM</title>
{THEME_BOOT}
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<header class="topbar">
  <div class="wrap">
    <a class="brand" href="../index.html">Bóveda 1DAM</a>
    <nav class="crumbs"><a href="../index.html">Inicio</a> &rsaquo; Fuentes y PDFs</nav>
    {THEME_BTN}
  </div>
</header>
<main class="wrap">
  <h1>Fuentes y PDFs</h1>
  <p>Documentos de apoyo de los temas (copias de los <code>Anexos/</code> de la bóveda):</p>
  <!--SECTIONS-->
  <footer class="site-foot"><p><a href="../index.html">← Volver al inicio</a></p></footer>
</main>
{body_end("../")}
</html>"""
    html_page = html_page.replace("<!--SECTIONS-->", "\n  ".join(sec_blocks))
    (OUT_DIR / "anexos" / "index.html").write_text(html_page, encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
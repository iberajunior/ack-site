"""Gera a versão em espanhol (/es/) a partir das páginas em português já geradas.
Traduções em _build/es.json (PT -> ES). Textos sem tradução são listados ao final do build."""
import os, re, json
from es_lib import segments, attrs

HERE = os.path.dirname(__file__)
SITE = "https://www.ackinstitute.com.br"

def load():
    return json.load(open(os.path.join(HERE, "es.json"), encoding="utf-8"))

def tr_text(s, D, miss):
    out = []; pos = 0
    items = sorted(segments(s) + attrs(s))
    for a, b, t in items:
        if a < pos: continue
        out.append(s[pos:a])
        if t in D: out.append(D[t])
        else: out.append(t); miss.add(t)
        pos = b
    out.append(s[pos:])
    return "".join(out)

KEEP = ("@type","@id","@context","url","item","email","telephone","postalCode","addressCountry","addressRegion","mainEntityOfPage","streetAddress","addressLocality","name_","courseMode","inLanguage")
def tr_jsonld(block, D, plain):
    def walk(o):
        if isinstance(o, dict): return {k: (v if (k in KEEP and isinstance(v, str)) or k in ("sameAs",) else walk(v)) for k, v in o.items()}
        if isinstance(o, list): return [walk(x) for x in o]
        if isinstance(o, str): return plain.get(o, D.get(o, o))
        return o
    try:
        data = json.loads(block)
    except Exception:
        return block
    data = walk(data)
    def lang(o):
        if isinstance(o, dict):
            if o.get("inLanguage") == "pt-BR": o["inLanguage"] = "es"
            for v in o.values(): lang(v)
        elif isinstance(o, list):
            for v in o: lang(v)
    lang(data)
    if isinstance(data, dict):
        g = data.get("@graph")
        for it in (g if isinstance(g, list) else [data]):
            if isinstance(it, dict) and it.get("@type") == "BreadcrumbList":
                for li in it.get("itemListElement", []):
                    li["item"] = li["item"].replace(SITE + "/", SITE + "/es/", 1)
    return json.dumps(data, ensure_ascii=False, indent=1)

def run(out, slugs):
    D = load()
    strip = lambda x: re.sub(r"<[^>]+>", "", x)
    plain = {strip(k): strip(v) for k, v in D.items()}
    esdir = os.path.join(out, "es"); os.makedirs(esdir, exist_ok=True)
    miss = set()
    for slug in slugs:
        src = open(os.path.join(out, slug), encoding="utf-8").read()
        # protege scripts JSON-LD e traduz separadamente
        blocks = []
        def keep(m):
            blocks.append(m.group(1)); return f"@@LD{len(blocks)-1}@@"
        s = re.sub(r'(?s)<script type="application/ld\+json">(.*?)</script>', lambda m: '<script type="application/ld+json">' + keep(m) + '</script>', src)
        s = tr_text(s, D, miss)
        for i, b in enumerate(blocks):
            s = s.replace(f"@@LD{i}@@", "\n" + tr_jsonld(b, D, plain) + "\n")
        # idioma, URLs e caminhos
        s = s.replace('<html lang="pt-BR">', '<html lang="es">', 1)
        s = s.replace('content="pt_BR"', 'content="es_LA"')
        u = "" if slug == "index.html" else slug
        s = s.replace(f'<link rel="canonical" href="{SITE}/{slug}">', f'<link rel="canonical" href="{SITE}/es/{slug}">')
        s = s.replace(f'<meta property="og:url" content="{SITE}/{slug}">', f'<meta property="og:url" content="{SITE}/es/{slug}">')
        s = re.sub(r'(src|href)="assets/', r'\1="../assets/', s)
        s = re.sub(r"url\((['\"]?)assets/", r"url(\1../assets/", s)
        s = re.sub(r'class="lg-pt on" href="[^"]*"', f'class="lg-pt" href="../{slug}"', s)
        s = re.sub(r'class="lg-es" href="[^"]*"', f'class="lg-es on" href="{slug}"', s)
        s = s.replace('aria-label="Idioma"', 'aria-label="Idioma"')
        # telefones no formato internacional
        s = re.sub(r'>\(41\) 99576-0079<', '>+55 41 99576-0079<', s)
        s = re.sub(r'>\(11\) 99788-1112<', '>+55 11 99788-1112<', s)
        s = s.replace('placeholder="(41) 9 0000-0000"', 'placeholder="+55 41 9 0000-0000"')
        # páginas que não existem em ES (RH removido) voltam para a consultoria
        s = s.replace('href="servicos-de-rh.html"', 'href="consultoria-empresarial.html"')
        open(os.path.join(esdir, slug), "w", encoding="utf-8").write(s)
    print(f"es: {len(slugs)} páginas")
    if miss:
        print(f"es: {len(miss)} textos sem tradução (ficaram em PT):")
        for m in sorted(miss): print("   -", m[:120])

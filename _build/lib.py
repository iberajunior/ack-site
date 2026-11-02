import json, html as H

SITE = "https://www.institutoackler.com.br"
WA = "https://wa.me/5541995760079"
AREA_ALUNO = "#area-do-aluno"  # PENDENTE: URL da área do aluno na EngagEd

def img(id_, w=1200, h=800):
    return f"https://static.wixstatic.com/media/{id_}/v1/fill/w_{w},h_{h},al_c,q_80/img.jpg"

I_A = "b2ec3b_0b32a0513e31408cbd51f6734576c3c6~mv2.jpg"
I_B = "b2ec3b_aea394d31d5d4caf941dc48244599010~mv2.jpg"
I_C = "0781f9_fd85651bc43d48eb8d55098894318090~mv2.png"
I_D = "b2ec3b_015b3805258849c5b860f8d6d2f0cf41~mv2.jpg"
I_E = "nsplsh_2f219259ee3b40d594cc6e1d663bf0ee~mv2.jpg"
I_F = "11062b_5f1706105a6e4225ad02a522f4b2d65d~mv2.jpg"
I_G = "ce0b413e62d04e8abd4afe96b12047fa.jpg"

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHEV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M6 9l6 6 6-6"/></svg>'

ICO = {
 "chart": '<path d="M3 20h18M6 16V9m6 7V5m6 11v-4"/>',
 "people": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c.6-3.4 3-5.4 6-5.4s5.4 2 6 5.4M16 4.5a3 3 0 0 1 0 6M18 14.8c1.7.7 2.7 2.4 3 5.2"/>',
 "cap": '<path d="M3 7l9-4 9 4-9 4-9-4z"/><path d="M7 9v5c0 1.7 2.2 3 5 3s5-1.3 5-3V9M21 7v6"/>',
 "cal": '<rect x="3" y="5" width="18" height="15" rx="2"/><path d="M8 3v4M16 3v4M7 12h4M7 16h7"/>',
 "flow": '<rect x="3" y="3" width="7" height="6" rx="1.5"/><rect x="14" y="15" width="7" height="6" rx="1.5"/><path d="M6.5 9v4.5a2 2 0 0 0 2 2H14"/>',
 "target": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1"/>',
 "shield": '<path d="M12 3l8 3v6c0 4.4-3.4 8-8 9-4.6-1-8-4.6-8-9V6l8-3z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
 "loop": '<path d="M20 11a8 8 0 0 0-14.3-4.9L4 8M4 4v4h4M4 13a8 8 0 0 0 14.3 4.9L20 16M20 20v-4h-4"/>',
 "mic": '<path d="M4 12h3l3-7 4 14 3-7h3"/>',
 "search": '<circle cx="11" cy="11" r="6.5"/><path d="M20 20l-4.2-4.2"/>',
 "id": '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="11" r="2.5"/><path d="M5.5 17c.6-1.8 1.9-2.8 3.5-2.8s2.9 1 3.5 2.8M15 10h3M15 14h3"/>',
 "brief": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
 "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
 "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
 "book": '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2V5z"/><path d="M4 19a2 2 0 0 1 2-2h13"/>',
 "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9L12 3z"/>',
 "wa": '<path d="M4 20l1.3-4A8 8 0 1 1 8 18.7L4 20z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5l1-1.5-2-1-1 .8a4 4 0 0 1-1.8-1.8l.8-1-1-2L9 9.5z"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
 "screen": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
}
def ico(k, w=1.6):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{w}">{ICO[k]}</svg>'

NAV = [
 ("Consultoria", None, [
    ("consultoria-empresarial.html","Consultoria Empresarial","Gestão e governança, da PME à indústria"),
    ("planejamento-estrategico.html","Planejamento Estratégico","Seu plano pronto em 30 dias"),
    ("servicos-de-rh.html","Serviços de RH","Recrutamento, BPO e perfis comportamentais")]),
 ("Treinamentos", None, [
    ("treinamentos.html","Treinamentos In Company","Temas aplicados à rotina da sua equipe"),
    ("team-building.html","Team Building","Vivências in company e offsite")]),
 ("Cursos","cursos.html",None),
 ("Sobre","sobre.html",None),
 ("Conteúdos","conteudos.html",None),
 ("Contato","contato.html",None),
]

def header(active):
    items=[]
    for label,href,sub in NAV:
        if sub:
            on = ' class="on"' if active in [s[0] for s in sub] else ''
            subs="".join(f'<a href="{h}">{t}<small>{d}</small></a>' for h,t,d in sub)
            items.append(f'<div class="dd"><a href="{sub[0][0]}"{on}>{label} {CHEV}</a><div class="sub">{subs}</div></div>')
        else:
            on = ' class="on"' if active==href else ''
            items.append(f'<a href="{href}"{on}>{label}</a>')
    items.append(f'<a href="{AREA_ALUNO}" style="color:var(--gold)">Área do aluno</a>')
    dl=[]
    for label,href,sub in NAV:
        if sub:
            dl.append(f'<a href="{sub[0][0]}">{label}</a>')
            dl += [f'<a class="s" href="{h}">{t}</a>' for h,t,d in sub]
        else:
            dl.append(f'<a href="{href}">{label}</a>')
    dl.append(f'<a href="{AREA_ALUNO}" style="color:var(--gold)">Área do aluno</a>')
    return f'''<header id="hd">
  <div class="wrap nav">
    <a class="logo" href="index.html" aria-label="Instituto Ackler, página inicial"><img src="assets/logo.png" alt="Instituto Ackler · Valores e Resultados"></a>
    <nav class="menu">{"".join(items)}</nav>
    <a class="btn btn-gold" href="contato.html">Falar com um consultor</a>
    <button class="burger" aria-label="Abrir menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h10"/></svg></button>
  </div>
</header>
<div class="drawer" id="drawer" role="dialog" aria-label="Menu">
  <div class="top"><img src="assets/logo.png" alt="Instituto Ackler"><button class="x" aria-label="Fechar menu">×</button></div>
  <nav>{"".join(dl)}</nav>
  <a class="btn btn-gold" href="contato.html">Falar com um consultor {ARROW}</a>
</div>'''

FOOTER = f'''<footer>
  <div class="wrap">
    <div class="foot">
      <div><img src="assets/logo.png" alt="Instituto Ackler"><p style="max-width:300px;line-height:1.6">Consultoria, treinamentos e cursos em gestão, governança e melhoria contínua. Curitiba, PR.</p></div>
      <div><h4>Soluções</h4><a href="consultoria-empresarial.html">Consultoria Empresarial</a><a href="planejamento-estrategico.html">Planejamento Estratégico</a><a href="treinamentos.html">Treinamentos</a><a href="team-building.html">Team Building</a><a href="servicos-de-rh.html">Serviços de RH</a></div>
      <div><h4>Instituto</h4><a href="sobre.html">Sobre</a><a href="cursos.html">Cursos</a><a href="conteudos.html">Conteúdos</a><a href="perguntas-frequentes.html">Perguntas frequentes</a><a href="contato.html">Contato</a></div>
      <div><h4>Redes</h4><a href="https://www.linkedin.com/company/instituto-ackler">LinkedIn</a><a href="https://www.instagram.com/institutoackler/">Instagram</a><a href="https://www.youtube.com/@InstitutoAckler">YouTube</a><a href="http://facebook.com/institutoackler">Facebook</a></div>
    </div>
    <div class="copy"><span>© <span data-year>2026</span> Instituto Ackler · Valores e Resultados</span><span>Política de privacidade · Cookies</span></div>
  </div>
</footer>
<a class="wa" href="{WA}" aria-label="Conversar no WhatsApp"><svg viewBox="0 0 32 32"><path d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.6c-2 0-4-.6-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.6 10.6 0 1 1 16 26.6zm5.8-7.9c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2l-1 1.2c-.2.2-.4.2-.7.1a8.7 8.7 0 0 1-4.3-3.8c-.3-.6.3-.5.9-1.6.1-.2 0-.4 0-.5l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.2 1.4 3.4c.2.2 2.4 3.6 5.7 5 2.1.9 2.9 1 4 .8.6-.1 1.9-.8 2.2-1.5.3-.8.3-1.4.2-1.5-.1-.2-.3-.2-.6-.4z"/></svg></a>'''

ORG = {"@type":"ProfessionalService","@id":SITE+"/#org","name":"Instituto Ackler","url":SITE,"telephone":"+55 41 99576-0079","email":"contato@institutoackler.com.br",
       "address":{"@type":"PostalAddress","streetAddress":"Rua do Herval, 636","addressLocality":"Curitiba","addressRegion":"PR","postalCode":"81530-420","addressCountry":"BR"}}

def crumbs_ld(trail):
    return {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":SITE+"/"+h} for i,(n,h) in enumerate(trail)]}

def page(slug, title, desc, active, body, trail, extra_ld=(), body_class=""):
    ld={"@context":"https://schema.org","@graph":[ORG,crumbs_ld(trail),*extra_ld]}
    bc=f' class="inner {body_class}"'.replace(' "','"')
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{H.escape(desc)}">
<link rel="canonical" href="{SITE}/{slug}">
<meta property="og:type" content="website"><meta property="og:title" content="{H.escape(title)}"><meta property="og:description" content="{H.escape(desc)}"><meta property="og:url" content="{SITE}/{slug}"><meta property="og:locale" content="pt_BR">
<link rel="icon" href="assets/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=1)}
</script>
</head>
<body{bc}>
{header(active)}
{body}
{FOOTER}
<script src="assets/main.js" defer></script>
</body>
</html>
'''

def crumbs(trail):
    parts=['<a href="index.html">Início</a>']
    for n,h in trail[1:-1]:
        parts.append(f'<span>/</span><a href="{h}">{n}</a>')
    parts.append(f'<span>/</span><b style="font-weight:600;color:var(--lav)">{trail[-1][0]}</b>')
    return '<nav class="crumbs rv" aria-label="Você está em">'+"".join(parts)+'</nav>'

def phero(trail, eyebrow, h1, lead, image, ctas="", chips="", cls=""):
    c = f'<div class="hero-ctas rv d3">{ctas}</div>' if ctas else ''
    ch = f'<div class="chips rv d3">{chips}</div>' if chips else ''
    return f'''<section class="phero {cls}" id="top">
  <div class="bg"><img src="{img(image,1800,1000)}" alt="" fetchpriority="high"></div>
  <div class="wrap">
    {crumbs(trail)}
    <span class="eyebrow rv">{eyebrow}</span>
    <h1 class="rv d1">{h1}</h1>
    <p class="lead rv d2">{lead}</p>
    {c}{ch}
  </div>
</section>'''

def btn(text, href, gold=True, magnetic=True):
    cls = "btn btn-gold" + (" magnetic" if magnetic else "") if gold else "btn btn-ghost"
    arrow = ARROW if gold else ""
    return f'<a class="{cls}" href="{href}">{text} {arrow}</a>'

def sec_head(eyebrow, h2, lead=""):
    l = f'<p class="lead rv d1">{lead}</p>' if lead else '<div></div>'
    return f'<div class="sec-head"><div class="rv"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2></div>{l}</div>'

def cards(items, cls="c3 sm"):
    out=[]
    for i,(ic,t,p,lis,more,href) in enumerate(items):
        ul = "<ul>"+"".join(f"<li>{x}</li>" for x in lis)+"</ul>" if lis else ""
        m = f'<span class="more">{more} →</span>' if more else ""
        tag = "a" if href else "div"
        hr = f' href="{href}"' if href else ""
        out.append(f'<{tag} class="card rv d{i%3}"{hr}><span class="num">{i+1:02d}</span><div class="ico">{ico(ic)}</div><h3>{t}</h3><p>{p}</p>{ul}{m}</{tag}>')
    return f'<div class="cards {cls}">'+"".join(out)+'</div>'

def steps(items):
    s="".join(f'<div class="step"><div class="dot">{i+1}</div><h3>{t}</h3><p>{p}</p></div>' for i,(t,p) in enumerate(items))
    cols = f' style="grid-template-columns:repeat({len(items)},1fr)"' if len(items)!=4 else ''
    return f'<div class="steps"{cols}><div class="bar"></div>{s}</div>'

def faq_items(qs, open_first=True):
    return "".join(f'<details{" open" if (i==0 and open_first) else ""}><summary>{q}<span class="pm"></span></summary><p>{a}</p></details>' for i,(q,a) in enumerate(qs))

def faq_ld(qs):
    import re
    strip=lambda s: re.sub(r'<[^>]+>','',s)
    return {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":strip(q),"acceptedAnswer":{"@type":"Answer","text":strip(a)}} for q,a in qs]}

def faq_section(qs, title='Dúvidas sobre <span class="it gold">este serviço</span>', lead="Se a sua pergunta não estiver aqui, chame a gente no WhatsApp."):
    return f'''<section class="sec" id="faq" style="padding-top:40px">
  <div class="wrap faq">
    <div class="rv"><span class="eyebrow">Perguntas frequentes</span><h2 style="margin-top:18px">{title}</h2><p class="lead" style="margin-top:22px">{lead}</p>
      <a class="btn btn-ghost" style="margin-top:30px" href="perguntas-frequentes.html">Ver todas as perguntas</a></div>
    <div class="rv d1">{faq_items(qs)}</div>
  </div>
</section>'''

def final(h2, lead, assunto=None):
    q = f"contato.html?assunto={assunto}" if assunto else "contato.html"
    return f'''<section class="final" id="contato">
  <div class="ring"></div>
  <div class="wrap" style="position:relative">
    <span class="eyebrow rv">Vamos conversar</span>
    <h2 class="rv d1">{h2}</h2>
    <p class="lead rv d2">{lead}</p>
    <div class="hero-ctas rv d3">
      <a class="btn btn-gold magnetic" href="{WA}">Chamar no WhatsApp {ARROW}</a>
      <a class="btn btn-ghost" href="{q}">Preencher o formulário</a>
    </div>
  </div>
</section>'''

def band(tag, h2, p, btn_text, href):
    return f'''<section style="padding:40px 0 120px"><div class="band rv">
  <div><span class="tag" style="display:inline-block;padding:8px 14px;border-radius:999px;background:rgba(255,184,0,.14);color:var(--gold);font-size:13px;font-weight:700;margin-bottom:22px">{tag}</span><h2>{h2}</h2></div>
  <div class="side"><p>{p}</p>{btn(btn_text, href)}</div>
</div></section>'''

def checks(items):
    return '<div class="checks">'+"".join(f'<div><b>{t}</b><small>{d}</small></div>' for t,d in items)+'</div>'

def bullets(items):
    return '<ul class="bullets">'+"".join(f'<li>{x}</li>' for x in items)+'</ul>'

LOGOS = [("b2ec3b_b3c1f7812e4549b7bd5d8b05ded44332~mv2.png","Fundação Copel"),("b2ec3b_4ab3041f06cc469780744e2dad8fc5c5~mv2.png","Grupo Risotolândia"),("b2ec3b_41f7d3c23b3749c4a66e551cb622f6e1~mv2.jpeg","Outdoormidia"),("b2ec3b_7a638cb7745e42d5accaa4e8955540c2~mv2.png","Grupo Boticário"),("b2ec3b_17c372e255414bc081576a0636fa7da2~mv2.png","Cliente"),("b2ec3b_9b897b8df04342d6904cad922a7d01c1~mv2.png","Cliente"),("b2ec3b_53d8e52f7d554983ba6ae094748b99ec~mv2.png","Cliente"),("b2ec3b_3f11023a19f24f9b9f27add189e3ca4a~mv2.png","Cliente"),("b2ec3b_4486e6c75cb349e18c1490d40080f217~mv2.png","C12 Brasil"),("b2ec3b_a4e451e87dfb47aaae48b37c3a69a2df~mv2.png","Abigraf")]
def logos(label="Empresas e parceiros que confiam no Instituto"):
    ims="".join(f'<img src="https://static.wixstatic.com/media/{i}" alt="{a}" loading="lazy">' for i,a in LOGOS)
    return f'<div class="logos"><p>{label}</p><div class="marquee" id="marq"><div>{ims}</div></div></div>'

# ===== Cabeçalho, rodapé e hero das internas (v2, ajustes de 02/11) =====
SOCIAL = [
 ("LinkedIn","https://www.linkedin.com/company/instituto-ackler",'<path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.5h4v11H3zM9.5 9.5h3.8v1.6h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.6 4.8 6v5.4h-4v-4.8c0-1.2 0-2.6-1.6-2.6s-1.9 1.3-1.9 2.5v4.9h-4z"/>'),
 ("Instagram","https://www.instagram.com/institutoackler/",'<path d="M12 7.3a4.7 4.7 0 1 0 0 9.4 4.7 4.7 0 0 0 0-9.4zm0 7.7a3 3 0 1 1 0-6 3 3 0 0 1 0 6zM17 5.9a1.1 1.1 0 1 0 0 2.2 1.1 1.1 0 0 0 0-2.2zM12 3c-2.4 0-2.7 0-3.7.1-3.3.1-5.1 1.9-5.2 5.2C3 9.3 3 9.6 3 12s0 2.7.1 3.7c.1 3.3 1.9 5.1 5.2 5.2 1 .1 1.3.1 3.7.1s2.7 0 3.7-.1c3.3-.1 5.1-1.9 5.2-5.2.1-1 .1-1.3.1-3.7s0-2.7-.1-3.7c-.1-3.3-1.9-5.1-5.2-5.2C14.7 3 14.4 3 12 3zm0 1.6c2.4 0 2.6 0 3.6.1 2.4.1 3.6 1.3 3.7 3.7.1 1 .1 1.2.1 3.6s0 2.6-.1 3.6c-.1 2.4-1.3 3.6-3.7 3.7-1 .1-1.2.1-3.6.1s-2.6 0-3.6-.1c-2.4-.1-3.6-1.3-3.7-3.7-.1-1-.1-1.2-.1-3.6s0-2.6.1-3.6c.1-2.4 1.3-3.6 3.7-3.7 1-.1 1.2-.1 3.6-.1z"/>'),
 ("YouTube","https://www.youtube.com/@InstitutoAckler",'<path d="M21.6 7.2a2.5 2.5 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4a2.5 2.5 0 0 0-1.8 1.8C2 8.8 2 12 2 12s0 3.2.4 4.8a2.5 2.5 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.5 2.5 0 0 0 1.8-1.8c.4-1.6.4-4.8.4-4.8s0-3.2-.4-4.8zM10 15V9l5.2 3L10 15z"/>'),
 ("Facebook","http://facebook.com/institutoackler",'<path d="M13.5 21v-8h2.7l.4-3.2h-3.1v-2c0-.9.3-1.6 1.6-1.6h1.7V3.4c-.3 0-1.3-.1-2.5-.1-2.5 0-4.1 1.5-4.1 4.2v2.3H7.4V13h2.8v8h3.3z"/>'),
]
def socials(cls="soc"):
    return f'<div class="{cls}">'+"".join(f'<a href="{u}" aria-label="{n}" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor">{p}</svg></a>' for n,u,p in SOCIAL)+'</div>'

def svg(k, w=1.8):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{w}">{ICO[k]}</svg>'

MEGA = [
 ("Consultoria", [("consultoria-empresarial.html","chart","Consultoria Empresarial","Gestão e governança, da PME à indústria"),
                  ("planejamento-estrategico.html","target","Planejamento Estratégico","Seu plano pronto em 30 dias"),
                  ("servicos-de-rh.html","id","Serviços de RH","Recrutamento, BPO e perfis comportamentais")]),
 ("Capacitação", [("treinamentos.html","people","Treinamentos In Company","Temas aplicados à rotina da equipe"),
                  ("team-building.html","heart","Team Building","Vivências in company e offsite"),
                  ("cursos.html","cap","Cursos","On-line e presenciais, com certificado")]),
]
SOL = [h for _,its in MEGA for h,*_ in its if h!="cursos.html"]
MAIN = [("Cursos","cursos.html"),("Sobre","sobre.html"),("Conteúdos","conteudos.html"),("FAQ","perguntas-frequentes.html"),("Contato","contato.html")]
ON = ' class="on"'

def header(active):
    cols="".join(f'<div class="mcol"><b>{t}</b>'+"".join(f'<a href="{h}"{ON if h==active else ""}><i>{svg(k,1.6)}</i><span>{n}<small>{d}</small></span></a>' for h,k,n,d in its)+'</div>' for t,its in MEGA)
    feat=f'<a class="mfeat" href="planejamento-estrategico.html"><span class="tag">Projeto de 30 dias</span><strong>Um plano estratégico pronto em 30 dias</strong><em>Conhecer o projeto {ARROW}</em></a>'
    son=' on' if active in SOL else ''
    items=[f'<div class="dd"><button class="dd-t{son}" type="button" aria-haspopup="true">Soluções {CHEV}</button><div class="mega"><div class="wrap mega-in">{cols}{feat}</div></div></div>']
    items+=[f'<a href="{h}"{ON if h==active else ""}>{t}</a>' for t,h in MAIN]
    dl=['<span class="dl-h">Soluções</span>']+[f'<a class="s" href="{h}">{n}</a>' for _,its in MEGA for h,k,n,d in its]
    dl+=[f'<a href="{h}">{t}</a>' for t,h in MAIN if h!="cursos.html"]
    return f'''<header id="hd">
  <div class="topbar"><div class="wrap tb">
    <div class="tb-l">
      <a href="{WA}">{svg("wa")}(41) 99576-0079</a>
      <a href="mailto:contato@institutoackler.com.br">{svg("mail")}contato@institutoackler.com.br</a>
      <span>{svg("pin")}Curitiba, PR · atendimento em todo o Brasil</span>
    </div>
    <div class="tb-r">{socials()}<a class="tb-aluno" href="{AREA_ALUNO}">{svg("cap")}Área do aluno</a></div>
  </div></div>
  <div class="bar"><div class="wrap nav">
    <a class="logo" href="index.html" aria-label="Instituto Ackler, página inicial"><img src="assets/logo.png" alt="Instituto Ackler · Valores e Resultados"></a>
    <nav class="menu">{"".join(items)}</nav>
    <div class="nav-cta">
      <a class="call" href="{WA}"><i>{svg("wa")}</i><span><small>Fale com um consultor</small><b>(41) 99576-0079</b></span></a>
      <a class="btn btn-gold" href="contato.html">Agendar conversa</a>
    </div>
    <button class="burger" aria-label="Abrir menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h10"/></svg></button>
  </div></div>
</header>
<div class="drawer" id="drawer" role="dialog" aria-label="Menu">
  <div class="top"><img src="assets/logo.png" alt="Instituto Ackler"><button class="x" aria-label="Fechar menu">×</button></div>
  <nav>{"".join(dl)}<a href="{AREA_ALUNO}" style="color:var(--gold)">Área do aluno</a></nav>
  <a class="btn btn-gold" href="contato.html">Agendar conversa {ARROW}</a>
  {socials("soc dsoc")}
</div>'''

HEART = '<svg class="hrt" viewBox="0 0 24 24" fill="currentColor" role="img" aria-label="amor"><path d="M12 21s-7.5-4.6-9.6-9.4C.9 8 3 4 6.8 4c2.1 0 3.7 1.1 5.2 3 1.5-1.9 3.1-3 5.2-3C21 4 23.1 8 21.6 11.6 19.5 16.4 12 21 12 21z"/></svg>'
WA_SVG = '<svg viewBox="0 0 32 32"><path d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.6c-2 0-4-.6-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.6 10.6 0 1 1 16 26.6zm5.8-7.9c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2l-1 1.2c-.2.2-.4.2-.7.1a8.7 8.7 0 0 1-4.3-3.8c-.3-.6.3-.5.9-1.6.1-.2 0-.4 0-.5l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.2 1.4 3.4c.2.2 2.4 3.6 5.7 5 2.1.9 2.9 1 4 .8.6-.1 1.9-.8 2.2-1.5.3-.8.3-1.4.2-1.5-.1-.2-.3-.2-.6-.4z"/></svg>'

FOOTER = f'''<footer>
  <div class="wrap">
    <div class="foot">
      <div><img src="assets/logo.png" alt="Instituto Ackler"><p style="max-width:300px;line-height:1.6">Consultoria, treinamentos e cursos em gestão, governança e melhoria contínua. Curitiba, PR.</p>{socials("soc fsoc")}</div>
      <div><h4>Soluções</h4><a href="consultoria-empresarial.html">Consultoria Empresarial</a><a href="planejamento-estrategico.html">Planejamento Estratégico</a><a href="treinamentos.html">Treinamentos</a><a href="team-building.html">Team Building</a><a href="servicos-de-rh.html">Serviços de RH</a></div>
      <div><h4>Instituto</h4><a href="sobre.html">Sobre</a><a href="cursos.html">Cursos</a><a href="conteudos.html">Conteúdos</a><a href="perguntas-frequentes.html">Perguntas frequentes</a><a href="{AREA_ALUNO}">Área do aluno</a></div>
      <div><h4>Contato</h4><a href="{WA}">(41) 99576-0079</a><a href="mailto:contato@institutoackler.com.br">contato@institutoackler.com.br</a><a href="contato.html">Rua do Herval, 636 · Curitiba, PR</a></div>
    </div>
    <div class="copy"><span>© <span data-year>2026</span> Instituto Ackler · Valores e Resultados</span><span class="made">Feito com {HEART} por <a href="https://agenciakroma.com.br" target="_blank" rel="noopener">Agência KROMA</a></span></div>
  </div>
</footer>
<button class="totop" id="totop" type="button" aria-label="Voltar ao topo"><svg class="ring" viewBox="0 0 48 48"><circle cx="24" cy="24" r="22"/><circle class="pr" cx="24" cy="24" r="22"/></svg><svg class="ar" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 19V5M6 11l6-6 6 6"/></svg></button>
<a class="wa" href="{WA}" aria-label="Conversar no WhatsApp">{WA_SVG}</a>'''

HERO_PHOTO = {"sobre.html":"sobre","consultoria-empresarial.html":"consultoria","planejamento-estrategico.html":"planejamento",
 "treinamentos.html":"treinamentos","team-building.html":"team-building","cursos.html":"cursos","curso-especialista-melhoria-continua.html":"curso",
 "servicos-de-rh.html":"rh","contato.html":"contato"}

def phero(trail, eyebrow, h1, lead, image, ctas="", chips="", cls=""):
    c = f'<div class="hero-ctas rv d3">{ctas}</div>' if ctas else ''
    ch = f'<div class="chips rv d3">{chips}</div>' if chips else ''
    ph = HERO_PHOTO.get(trail[-1][1])
    person = f'<div class="person" aria-hidden="true"><span class="halo1"></span><span class="arc"></span><img src="assets/img/hero-{ph}.webp" alt=""></div>' if ph else ''
    hp = ' has-person' if ph else ''
    return f'''<section class="phero {cls}{hp}" id="top">
  <div class="bg"><img src="{img(image,1800,1000)}" alt=""></div>
  {person}
  <div class="wrap ph-in">
    <div class="ph-txt">
    {crumbs(trail)}
    <span class="eyebrow rv">{eyebrow}</span>
    <h1 class="rv d1">{h1}</h1>
    <p class="lead rv d2">{lead}</p>
    {c}{ch}
    </div>
  </div>
</section>'''

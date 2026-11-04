import re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
import pages1, pages2, pages3, pages4

OUT = os.path.join(os.path.dirname(__file__), "..")
A = os.path.join(OUT, "assets"); S = os.path.dirname(__file__)
open(os.path.join(A,"styles.css"),"w").write(open(os.path.join(S,"base.css")).read()+"\n"+open(os.path.join(S,"inner.css")).read())

def finalize(h, slug):
    u = "" if slug=="index.html" else slug
    alt = f'<link rel="alternate" hreflang="pt-BR" href="{SITE}/{u}">\n<link rel="alternate" hreflang="es" href="{SITE}/es/{u}">\n<link rel="alternate" hreflang="x-default" href="{SITE}/{u}">\n'
    h = h.replace("</head>", alt+"</head>", 1)
    return h.replace("@@PT@@", slug).replace("@@ES@@", "es/"+slug)

ALL = {**pages1.P, **pages2.P, **pages3.P, **pages4.P}
for slug, t in ALL.items():
    title, desc, active, body, trail, ld, *rest = t
    html = page(slug, title, desc, active, body, trail, ld, rest[0] if rest else "")
    open(os.path.join(OUT, slug), "w", encoding="utf-8").write(finalize(html, slug))
    print("ok", slug, len(html))

# ---- Home: passa a usar os arquivos compartilhados e linka as páginas internas
s = open(os.path.join(os.path.dirname(__file__), "index-fonte.html"), encoding="utf-8").read()
s = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="assets/styles.css">\n<link rel="icon" href="assets/favicon.png" type="image/png">\n<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">\n<meta name="theme-color" content="#0A0840">', s, count=1, flags=re.S)
s = re.sub(r'<script>\n\(\(\)=>\{.*?</script>', '<script src="assets/main.js" defer></script>', s, count=1, flags=re.S)
s = re.sub(r'<header id="hd">.*?</header>', header("index.html").replace('href="index.html" aria-label','href="#top" aria-label'), s, count=1, flags=re.S)
s = re.sub(r'<footer>.*?</footer>\s*<a class="wa".*?</a>', FOOTER, s, count=1, flags=re.S)
s = s.replace('family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&', 'family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&')
rep = [
 ('<a class="card rv" href="#contato"><span class="num">01</span>', '<a class="card rv" href="consultoria-empresarial.html"><span class="num">01</span>'),
 ('<a class="card rv d1" href="#treinamentos"><span class="num">02</span>', '<a class="card rv d1" href="treinamentos.html"><span class="num">02</span>'),
 ('<a class="card rv d2" href="#treinamentos"><span class="num">03</span>', '<a class="card rv d2" href="cursos.html"><span class="num">03</span>'),
 ('href="#contato">Quero o meu plano em 30 dias', 'href="planejamento-estrategico.html">Quero o meu plano em 30 dias'),
 ('href="#contato">Planejar um team building', 'href="team-building.html">Planejar um team building'),
 ('href="#contato">Ver catálogo completo', 'href="cursos.html">Ver catálogo completo'),
 ('<a class="post rv" href="#">', '<a class="post rv" href="5s-por-onde-comecar.html">'),
 ('<a class="post rv d1" href="#">', '<a class="post rv d1" href="conteudos.html">'),
 ('<a class="post rv d2" href="#">', '<a class="post rv d2" href="conteudos.html">'),
 ('<section class="sec" id="servicos">', '<section class="sec light" id="servicos">'),
 ('href="#contato">Quero um diagnóstico da minha empresa', 'href="contato.html?assunto=Consultoria">Quero um diagnóstico da minha empresa'),
]
for a,b in rep:
    assert a in s, a
    s = s.replace(a,b)
# trilha de treinamentos -> página de treinamentos
s = s.replace('<div class="trow" data-img=', '<a class="trow" href="treinamentos.html" data-img=')
s = re.sub(r'(<a class="trow"[^\n]*?</span>)</div>', r'\1</a>', s)
# link para a FAQ completa e para conteúdos
s = s.replace('<p class="lead" style="margin-top:22px">Respostas diretas para as dúvidas mais comuns de empresários e gestores.</p></div>',
              '<p class="lead" style="margin-top:22px">Respostas diretas para as dúvidas mais comuns de empresários e gestores.</p><a class="btn btn-ghost" style="margin-top:30px" href="perguntas-frequentes.html">Ver todas as perguntas</a></div>')
s = s.replace('<p class="lead rv d1">Artigos práticos sobre melhoria contínua, indicadores e liderança, para aplicar na sua empresa ainda nesta semana.</p>',
              '<div class="rv d1"><p class="lead">Artigos práticos sobre melhoria contínua, indicadores e liderança, para aplicar na sua empresa ainda nesta semana.</p><a class="btn" style="margin-top:24px;border:1px solid #d5d3ea" href="conteudos.html">Ver todos os conteúdos</a></div>')
# conteúdo do ackinstitute.com.br: foto do Josemar, logos de clientes e depoimentos
import re as _re
s = s.replace('<img src="https://static.wixstatic.com/media/b2ec3b_015b3805258849c5b860f8d6d2f0cf41~mv2.jpg/v1/fill/w_900,h_1120,al_c,q_80/sobre.jpg" alt="ACK Institute">',
              f'<img src="{wix(JOSEMAR,900,1120,"t")}" alt="Josemar Ackler, fundador e CEO da ACK Institute">')
s = s.replace('<div class="sig"><b>Josemar Thans Ackler</b>','<div class="sig"><b>Josemar Ackler</b>')
s = _re.sub(r'(<div class="marquee" id="marq">\s*<div>).*?(</div>\s*</div>)', lambda m: m.group(1)+logos_imgs()+m.group(2), s, count=1, flags=_re.S)
s = s.replace('<p>Empresas e parceiros que confiam na ACK</p>','<p>Empresas que confiam na ACK</p>')
s = s.replace('<!-- FAQ -->', testimonials_section()+'\n\n<!-- FAQ -->', 1)
# ===== Ajustes pedidos pelo Thayson em 04/11 =====
CARDS_NEW = '''<div class="cards">
      <a class="card rv" href="consultoria-excelencia-operacional.html"><span class="num">01</span>
        <div class="ico">'''+ico("loop")+'''</div>
        <h3>Excelência Operacional</h3>
        <p>Consultoria em LEAN, TPM e WCM para aumentar a eficiência e reduzir perdas na operação.</p>
        <ul><li>TPM e preparação JIPM</li><li>WCM e Lean Manufacturing</li><li>Gestão da manutenção</li></ul>
        <span class="more">Conhecer a consultoria →</span></a>
      <a class="card rv d1" href="consultoria-empresarial.html"><span class="num">02</span>
        <div class="ico">'''+ico("chart")+'''</div>
        <h3>Gestão Operacional</h3>
        <p>Gestão, governança e redução de custos sob medida, da pequena empresa à grande indústria.</p>
        <ul><li>Assessment de custos e perdas</li><li>Indicadores e rotina de gestão</li><li>Planejamento estratégico</li></ul>
        <span class="more">Conhecer a consultoria →</span></a>
      <a class="card rv d2" href="treinamentos.html"><span class="num">03</span>
        <div class="ico">'''+ico("people")+'''</div>
        <h3>Treinamentos In Company</h3>
        <p>Programas aplicados dentro da sua empresa, com conteúdo ajustado à realidade da equipe.</p>
        <ul><li>5S, PDCA e causa raiz</li><li>Comunicação e liderança</li><li>Normas ISO</li></ul>
        <span class="more">Ver treinamentos →</span></a>
      <a class="card rv d3" href="cursos.html"><span class="num">04</span>
        <div class="ico">'''+ico("cap")+'''</div>
        <h3>Cursos</h3>
        <p>Mais de 20 cursos para profissionais que querem crescer na carreira industrial.</p>
        <ul><li>Especialista em Melhoria Contínua</li><li>Lean e Indústria 4.0</li><li>Ferramentas da Qualidade</li></ul>
        <span class="more">Ver cursos →</span></a>
    </div>'''
s, n = re.subn(r'<div class="cards">\s*<a class="card rv" href="consultoria-empresarial.html">.*?</a>\s*</div>', lambda m: CARDS_NEW, s, count=1, flags=re.S)
assert n==1
rep2 = [
 ('<p class="lead rv d2">Consultoria em gestão e governança, treinamentos in company e cursos de melhoria contínua para pequenas empresas e grandes indústrias. Com a experiência de quem passou 35 anos dentro delas.</p>',
  '<p class="lead rv d2">Consultoria em Gestão, Governança e Excelência Operacional. Atuamos na estruturação de processos, desenvolvimento de lideranças e melhoria contínua, transformando desafios em resultados sustentáveis para empresas e indústrias.</p>'),
 ('<p class="lead rv d1">Cada empresa chega por uma porta diferente. Algumas precisam organizar a gestão, outras querem capacitar a equipe ou estruturar o RH. A gente começa pelo problema que mais pesa hoje.</p>',
  '<p class="lead rv d1">Cada empresa tem desafios e necessidades diferentes. Algumas precisam melhorar a gestão, outras aumentar a eficiência operacional, desenvolver lideranças ou reduzir custos. Na ACK, começamos entendendo a realidade do negócio e atuamos diretamente nos pontos que mais impactam seus resultados.</p>'),
 ('<details><summary>A ACK oferece serviços de RH?<span class="pm"></span></summary><p>Sim. Oferecemos consultoria e treinamentos para o departamento de RH, incluindo recrutamento e seleção, BPO em RH e análise de perfis comportamentais.</p></details>',
  '<details><summary>A ACK trabalha com Lean, TPM e WCM?<span class="pm"></span></summary><p>Sim. Nossa consultoria em Excelência Operacional implanta Lean Manufacturing, TPM e WCM, incluindo a preparação para premiações JIPM, com a experiência de quem conduziu esses programas em grandes indústrias.</p></details>'),
 ('Temos unidades em Curitiba (Batel) e em São Paulo (Itaim Bibi). Atendemos empresas de todo o Brasil, presencialmente ou a distância, conforme o tipo de projeto.',
  'Temos unidades em Curitiba (Batel), São Paulo (Itaim Bibi), Porto Alegre (RS) e Asunción, no Paraguai. Atendemos empresas de todo o Brasil e da América Latina, presencialmente ou a distância, conforme o tipo de projeto.'),
]
for a,b in rep2:
    assert a in s, a[:80]
    s = s.replace(a,b)
s, n = re.subn(r'<div><small>Unidades</small><b>Curitiba \(Batel\) · São Paulo \(Itaim Bibi\)</b></div>\s*</div>', lambda m: '</div>\n    '+units_html(), s, count=1)
assert n==1
s = s.replace('<div class="contacts rv">','<div class="contacts c2 rv">',1)
s = s.replace('content="Consultoria empresarial em gestão e governança, treinamentos in company e cursos de melhoria contínua para pequenas empresas e grandes indústrias. Curitiba, PR."',
              'content="Consultoria em gestão, governança e excelência operacional (Lean, TPM e WCM), redução de custos, treinamentos in company e cursos de melhoria contínua para empresas e indústrias. Brasil e América Latina."',1)
assert 'data:image' not in s
open(os.path.join(OUT,"index.html"),"w",encoding="utf-8").write(finalize(s,"index.html"))
print("home", len(s))

# Serviços de RH removido: a URL antiga redireciona para a consultoria
open(os.path.join(OUT,"servicos-de-rh.html"),"w",encoding="utf-8").write('''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>ACK Institute</title>
<meta name="robots" content="noindex"><link rel="canonical" href="https://www.ackinstitute.com.br/consultoria-empresarial.html">
<meta http-equiv="refresh" content="0; url=consultoria-empresarial.html"></head>
<body><p><a href="consultoria-empresarial.html">Ir para Consultoria em Gestão Operacional</a></p></body></html>
''')

# ===== Versão em espanhol (/es/) =====
import es
es.run(OUT, [*ALL.keys(), "index.html"])

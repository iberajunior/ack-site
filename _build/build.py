import re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
import pages1, pages2, pages3

OUT = os.path.join(os.path.dirname(__file__), "..")
A = os.path.join(OUT, "assets"); S = os.path.dirname(__file__)
open(os.path.join(A,"styles.css"),"w").write(open(os.path.join(S,"base.css")).read()+"\n"+open(os.path.join(S,"inner.css")).read())

ALL = {**pages1.P, **pages2.P, **pages3.P}
for slug, t in ALL.items():
    title, desc, active, body, trail, ld, *rest = t
    html = page(slug, title, desc, active, body, trail, ld, rest[0] if rest else "")
    open(os.path.join(OUT, slug), "w", encoding="utf-8").write(html)
    print("ok", slug, len(html))

# ---- Home: passa a usar os arquivos compartilhados e linka as páginas internas
s = open(os.path.join(os.path.dirname(__file__), "index-fonte.html"), encoding="utf-8").read()
s = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="assets/styles.css">\n<link rel="icon" href="assets/logo.png">', s, count=1, flags=re.S)
s = re.sub(r'<script>\n\(\(\)=>\{.*?</script>', '<script src="assets/main.js" defer></script>', s, count=1, flags=re.S)
s = re.sub(r'<header id="hd">.*?</header>', header("index.html").replace('href="index.html" aria-label','href="#top" aria-label'), s, count=1, flags=re.S)
s = re.sub(r'<footer>.*?</footer>\s*<a class="wa".*?</a>', FOOTER, s, count=1, flags=re.S)
s = s.replace('family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&', 'family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&')
rep = [
 ('<a class="card rv" href="#contato"><span class="num">01</span>', '<a class="card rv" href="consultoria-empresarial.html"><span class="num">01</span>'),
 ('<a class="card rv d1" href="#treinamentos"><span class="num">02</span>', '<a class="card rv d1" href="treinamentos.html"><span class="num">02</span>'),
 ('<a class="card rv d2" href="#treinamentos"><span class="num">03</span>', '<a class="card rv d2" href="cursos.html"><span class="num">03</span>'),
 ('<a class="card rv d3" href="#contato"><span class="num">04</span>', '<a class="card rv d3" href="servicos-de-rh.html"><span class="num">04</span>'),
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
assert 'data:image' not in s
open(os.path.join(OUT,"index.html"),"w",encoding="utf-8").write(s)
print("home", len(s))

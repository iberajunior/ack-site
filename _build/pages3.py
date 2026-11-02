from lib import *
import pages1, pages2
P = {}
HOME = ("Início","")
CURSO_URL = "curso-especialista-melhoria-continua.html"
ENGAGED = "#comprar-engaged"  # PENDENTE: link de compra do curso na EngagEd

# ============ CURSOS (catálogo) ============
# Exemplo de catálogo. No site final, os cards são gerados pelo painel WordPress.
CURSOS=[("Especialista em Melhoria Contínua",I_A,"online","On-line","40h","Formação completa em 5S, PDCA, causa raiz, VSM e indicadores para quem quer liderar projetos de melhoria.",True),
 ("5S na Prática",I_B,"online incompany","On-line","8h","Como implantar e, principalmente, manter o 5S no posto de trabalho.",False),
 ("Análise de Causa Raiz",I_C,"online incompany","On-line","8h","Ishikawa, 5 porquês e plano de ação para resolver problemas de vez.",False),
 ("PDCA e Ferramentas da Qualidade",I_D,"online","On-line","12h","O ciclo de melhoria e as sete ferramentas da qualidade com exemplos industriais.",False),
 ("Mapeamento de Processos e VSM",I_E,"presencial incompany","Presencial","16h","Mapa do fluxo de valor, identificação de desperdícios e desenho do estado futuro.",False),
 ("Lean e Indústria 4.0",I_A,"online","On-line","16h","Fundamentos do pensamento lean e como a digitalização muda a fábrica.",False),
 ("Normas ISO: interpretação",I_C,"presencial incompany","Presencial","16h","Leitura dos requisitos e preparação da equipe para auditorias.",False),
 ("Comunicação Assertiva",I_F,"presencial incompany","Presencial","8h","Feedback, conflitos e conversas difíceis no ambiente de trabalho.",False),
 ("Gestão do Tempo e Produtividade",I_G,"online incompany","On-line","6h","Prioridades, agenda e reuniões que rendem para gestores e equipes.",False)]
def course_card(c,i=0):
    t,im,cat,mod,ch,res,dest=c
    clk='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></svg>'
    scr='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/></svg>'
    badge='<span class="mod g">Destaque</span>' if dest else f'<span class="mod">{mod}</span>'
    return f'''<a class="course rv d{i%3}" href="{CURSO_URL}" data-cat="{cat}"><div class="ph"><img src="{img(im,800,500)}" alt="" loading="lazy">{badge}</div><div class="bd"><div class="meta"><span>{clk}{ch}</span><span>{scr}{mod}</span></div><h3>{t}</h3><p>{res}</p><span class="go">Ver curso →</span></div></a>'''
tr=[HOME,("Cursos","cursos.html")]
FAQ_CU=[("Como compro um curso?","Na página de cada curso, clique em “Comprar curso”. Você será levado para a plataforma EngagEd, onde faz o pagamento com segurança e recebe o acesso."),
 ("Onde assisto às aulas on-line?","Na Área do aluno, dentro da plataforma EngagEd, pelo computador ou pelo aplicativo no celular. O link fica no topo de todas as páginas do site."),
 ("Os cursos têm certificado?","Sim. Ao concluir o curso, você recebe o certificado de conclusão."),
 ("Posso levar um curso para a minha empresa?","Pode. Os cursos marcados como in company podem ser aplicados para a sua equipe, com conteúdo ajustado. Fale com a gente para receber uma proposta.")]
body=phero(tr,"Cursos",'Cursos para quem quer <span class="it gold">crescer na indústria</span>',
 "Mais de 20 cursos em melhoria contínua, qualidade e gestão, criados por quem passou 35 anos dentro de grandes indústrias. On-line, presenciais ou na sua empresa.",I_B,
 btn("Ver catálogo","#catalogo")+f'<a class="btn btn-ghost" href="{AREA_ALUNO}">Já sou aluno</a>',
 '<span><b>+20</b> cursos</span><span>On-line e presencial</span><span>Com certificado</span>')
body+=f'''
<section class="sec light" id="catalogo">
  <div class="wrap">
    {sec_head("Catálogo",'Encontre o <span class="it" style="color:var(--blue)">próximo passo</span> da sua carreira',"Filtre por modalidade ou busque pelo tema que você precisa.")}
    <div class="filters rv">
      <button class="on" data-f="todos">Todos</button><button data-f="online">On-line</button><button data-f="presencial">Presencial</button><button data-f="incompany">Para empresas</button>
      <label class="search"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="6.5"/><path d="M20 20l-4.2-4.2"/></svg><input id="q" type="search" placeholder="Buscar curso" aria-label="Buscar curso"></label>
    </div>
    <!-- Os cards abaixo são exemplos. No site final, são gerados automaticamente pelo painel (WordPress) a partir dos cursos cadastrados pela equipe ACK. -->
    <div class="courses" id="courses">{"".join(course_card(c,i) for i,c in enumerate(CURSOS))}</div>
    <div class="empty" id="empty">Nenhum curso encontrado com esse filtro. <a href="contato.html?assunto=Cursos" style="color:var(--blue);font-weight:700">Fale com a gente</a> e indicamos o mais adequado.</div>
  </div>
</section>

{band("Área do aluno",'Já comprou um curso? <span class="it gold">Suas aulas estão aqui.</span>',"O acesso às aulas, materiais e certificados fica na plataforma EngagEd, no computador ou no aplicativo.","Entrar na Área do aluno",AREA_ALUNO)}
{faq_section(FAQ_CU,'Dúvidas sobre <span class="it gold">os cursos</span>')}
{final('Quer levar um curso <span class="it gold">para a sua equipe?</span>',"Qualquer curso do catálogo pode virar treinamento in company, com exemplos da sua operação.","Cursos")}
'''
P["cursos.html"]=("Cursos de Melhoria Contínua, Qualidade e Lean · Instituto Ackler",
 "Cursos on-line e presenciais de melhoria contínua, 5S, causa raiz, PDCA, VSM, Lean, Indústria 4.0 e normas ISO, com certificado. Instituto Ackler, Curitiba.",
 "cursos.html",body,tr,[{"@type":"ItemList","name":"Cursos do Instituto Ackler","itemListElement":[{"@type":"ListItem","position":i+1,"item":{"@type":"Course","name":c[0],"description":c[5],"provider":{"@id":SITE+"/#org"}}} for i,c in enumerate(CURSOS)]},faq_ld(FAQ_CU)])

# ============ PÁGINA DO CURSO (modelo) ============
tr=[HOME,("Cursos","cursos.html"),("Especialista em Melhoria Contínua",CURSO_URL)]
MODS=[("Fundamentos da melhoria contínua","4h",["O que é melhoria contínua e por que projetos param no meio","Kaizen e o papel de cada nível da empresa","Como escolher o primeiro problema"]),
 ("5S do início à manutenção","6h",["Os cinco sensos na prática","Auditoria e padrão visual","Como evitar que o 5S vire mutirão de limpeza"]),
 ("PDCA e ferramentas da qualidade","8h",["Ciclo PDCA aplicado","Pareto, Ishikawa, histograma e folha de verificação","Exercícios com dados reais"]),
 ("Análise de causa raiz","6h",["5 porquês sem chegar em “falta de atenção”","Diagrama de causa e efeito","Plano de ação e verificação de eficácia"]),
 ("Mapeamento do fluxo de valor (VSM)","8h",["Estado atual e identificação de desperdícios","Desenho do estado futuro","Plano de implantação"]),
 ("Indicadores e rotina de gestão","8h",["Como escolher indicadores que importam","Gestão à vista","Reuniões de resultado curtas e objetivas"])]
FAQ_CM=[("Preciso ter experiência na área?","Não. O curso começa pelos fundamentos. Quem já trabalha com qualidade ou produção aproveita os módulos práticos para organizar o que já sabe."),
 ("Por quanto tempo tenho acesso?","O período de acesso é informado na plataforma EngagEd no momento da compra."),
 ("Recebo certificado?","Sim. Ao concluir todos os módulos, o certificado fica disponível na Área do aluno."),
 ("Posso fazer pelo celular?","Pode. As aulas funcionam no computador e no aplicativo da EngagEd.")]
learn=["Conduzir um projeto de melhoria do início ao fim","Implantar e manter o 5S","Usar PDCA e as ferramentas da qualidade","Encontrar a causa real de um problema","Mapear o fluxo de valor de um processo","Montar indicadores e uma rotina de gestão"]
mods="".join(f'<details{" open" if i==0 else ""}><summary><span>Módulo {i+1} · {t}</span><em>{h}</em><span class="pm"></span></summary><ul>{"".join(f"<li>{x}</li>" for x in it)}</ul></details>' for i,(t,h,it) in enumerate(MODS))
body=phero(tr,"Curso on-line · Destaque",'Especialista em <span class="it gold">Melhoria Contínua</span>',
 "Formação prática para quem quer liderar projetos de melhoria na indústria: 5S, PDCA, causa raiz, VSM e indicadores, com exemplos de 35 anos de chão de fábrica.",I_A,
 "",'<span><b>40h</b> de conteúdo</span><span>On-line</span><span>6 módulos</span><span>Com certificado</span>')
body+=f'''
<section class="sec" style="padding-top:80px">
  <div class="wrap cgrid">
    <div>
      <div class="block rv"><h2 class="h3">Sobre o curso</h2>
        <div class="prose" style="margin-top:18px"><p>Muitos profissionais conhecem as ferramentas da qualidade de nome, mas travam na hora de aplicar. Este curso foi montado para resolver isso: cada módulo mostra a ferramenta, um caso real e um exercício para você aplicar no seu ambiente de trabalho.</p><p>Ao final, você tem repertório para <strong>conduzir um projeto de melhoria completo</strong>, do problema escolhido até o resultado medido.</p></div></div>
      <div class="block rv"><h2 class="h3">O que você vai aprender</h2><div class="learn">{"".join(f"<div>{x}</div>" for x in learn)}</div></div>
      <div class="block rv"><h2 class="h3">Para quem é</h2>{bullets(["Analistas e técnicos de qualidade, produção e processos","Supervisores e líderes que querem resultados mais consistentes","Profissionais em transição para a área industrial","Empreendedores que querem organizar a própria operação"])}</div>
      <div class="block rv mods"><h2 class="h3">Conteúdo programático</h2><p style="color:var(--muted);margin-bottom:10px">6 módulos · 40 horas</p>{mods}</div>
      <div class="block rv"><h2 class="h3" style="margin-bottom:22px">Quem ensina</h2>
        <div class="instr"><div class="av"><img src="{img(I_D,300,300)}" alt="Josemar Thans Ackler" loading="lazy"></div><div><b>Josemar Thans Ackler</b><p>Fundador do Instituto Ackler. Passou 35 anos em grandes indústrias, no Brasil e no exterior, implantando programas de melhoria contínua e rotinas de gestão.</p></div></div></div>
      <div class="block rv"><h2 class="h3" style="margin-bottom:10px">Dúvidas sobre o curso</h2>{faq_items(FAQ_CM)}</div>
    </div>
    <aside class="buy rv d1" id="comprar">
      <div class="ph"><img src="{img(I_A,800,500)}" alt=""></div>
      <div class="in">
        <dl><dt>Carga horária</dt><dd>40 horas</dd><dt>Modalidade</dt><dd>On-line</dd><dt>Módulos</dt><dd>6</dd><dt>Certificado</dt><dd>Sim</dd><dt>Acesso</dt><dd>Computador e app</dd></dl>
        <a class="btn btn-gold" href="{ENGAGED}">Comprar curso {ARROW}</a>
        <a class="alt" href="{WA}?text=Ol%C3%A1!%20Tenho%20d%C3%BAvidas%20sobre%20o%20curso%20Especialista%20em%20Melhoria%20Cont%C3%ADnua.">Tirar dúvidas no WhatsApp</a>
        <p class="note">Pagamento e acesso às aulas pela plataforma EngagEd.</p>
      </div>
    </aside>
  </div>
</section>

<section class="sec light">
  <div class="wrap">
    {sec_head("Continue aprendendo",'Outros cursos <span class="it" style="color:var(--blue)">do catálogo</span>')}
    <div class="courses">{"".join(course_card(c,i) for i,c in enumerate(CURSOS[1:4]))}</div>
  </div>
</section>
<div class="mbar"><b>Especialista em Melhoria Contínua</b><a class="btn btn-gold" href="{ENGAGED}">Comprar curso</a></div>
'''
P[CURSO_URL]=("Curso Especialista em Melhoria Contínua (on-line, 40h) · Instituto Ackler",
 "Curso on-line Especialista em Melhoria Contínua: 5S, PDCA, ferramentas da qualidade, causa raiz, VSM e indicadores. 40 horas, 6 módulos, com certificado.",
 "cursos.html",body,tr,[{"@type":"Course","name":"Especialista em Melhoria Contínua","description":"Formação prática em 5S, PDCA, causa raiz, VSM e indicadores para liderar projetos de melhoria na indústria.","provider":{"@id":SITE+"/#org"},"inLanguage":"pt-BR",
   "hasCourseInstance":{"@type":"CourseInstance","courseMode":"online","courseWorkload":"PT40H","instructor":{"@type":"Person","name":"Josemar Thans Ackler"}}},faq_ld(FAQ_CM)])
P[CURSO_URL]=P[CURSO_URL]+("has-mbar",)

# ============ FAQ ============
tr=[HOME,("Perguntas frequentes","perguntas-frequentes.html")]
GER=[("O que o Instituto Ackler faz?","O Instituto Ackler oferece consultoria empresarial em gestão e governança, treinamentos in company, cursos de melhoria contínua e serviços de RH para pequenas empresas e grandes indústrias."),
 ("Quem fundou o Instituto Ackler?","O Instituto foi fundado por Josemar Thans Ackler, que trabalhou 35 anos em grandes indústrias, no Brasil e no exterior."),
 ("O Instituto Ackler atende pequenas empresas ou só indústrias?","Atendemos os dois. Temos consultoria específica para pequenas e médias empresas e projetos para grandes indústrias. O método é o mesmo, o tamanho do projeto se ajusta à sua realidade."),
 ("Onde o Instituto Ackler fica?","Nosso escritório fica em Curitiba, no Paraná. Atendemos empresas de todo o Brasil, presencialmente ou a distância, conforme o tipo de projeto."),
 ("Como peço um orçamento?","Pelo WhatsApp (41) 99576-0079, pelo e-mail contato@institutoackler.com.br ou pelo formulário da página de contato. A primeira conversa é sem compromisso.")]
GROUPS=[("geral","Sobre o Instituto",GER),
 ("consultoria","Consultoria e planejamento",pages1.FAQ_C[:3]+pages1.FAQ_P[:2]),
 ("treinamentos","Treinamentos e team building",pages2.FAQ_T[:3]+pages2.FAQ_TB[:2]),
 ("cursos","Cursos e Área do aluno",FAQ_CU),
 ("rh","Serviços de RH",pages2.FAQ_RH)]
ALLQ=[q for _,_,qs in GROUPS for q in qs]
ON=' class="on"'
tabs="".join(f'<a href="#{k}"{ON if i==0 else ""}>{t}<em>{len(qs)}</em></a>' for i,(k,t,qs) in enumerate(GROUPS))
groups="".join(f'<div class="fgroup" id="{k}"><h2 class="rv">{t}</h2><div class="rv">{faq_items(qs, i==0)}</div></div>' for i,(k,t,qs) in enumerate(GROUPS))
body=phero(tr,"Perguntas frequentes",'Respostas diretas <span class="it gold">antes da conversa</span>',
 "As dúvidas mais comuns de empresários, gestores e alunos sobre consultoria, treinamentos, cursos e RH, respondidas em poucas linhas.",I_E,"",
 f'<span><b>{len(ALLQ)}</b> perguntas</span><span>5 temas</span>',"short")
body+=f'''
<section class="sec" style="padding-top:80px">
  <div class="wrap faq faqp">
    <div><nav class="ftabs rv" aria-label="Temas">{tabs}</nav></div>
    <div>{groups}</div>
  </div>
</section>
{final('Não encontrou <span class="it gold">a sua dúvida?</span>',"Mande sua pergunta no WhatsApp. Quem responde é a equipe do Instituto.")}
'''
P["perguntas-frequentes.html"]=("Perguntas frequentes sobre consultoria, treinamentos e cursos · Instituto Ackler",
 "Respostas sobre consultoria empresarial, planejamento estratégico em 30 dias, treinamentos in company, team building, cursos on-line e serviços de RH do Instituto Ackler.",
 "perguntas-frequentes.html",body,tr,[faq_ld(ALLQ)])

# ============ CONTEÚDOS (blog) ============
ART="5s-por-onde-comecar.html"
POSTS=[("Indicadores","Quais indicadores uma PME deve acompanhar",I_B,"Poucos números, bem escolhidos, dizem mais do que um painel lotado.","6 min"),
 ("Qualidade","Análise de causa raiz em 5 passos",I_E,"Como parar de apagar incêndio e resolver o problema de vez.","7 min"),
 ("Gestão","PDCA no dia a dia: um exemplo real",I_C,"O ciclo de melhoria aplicado a um problema comum de produção.","5 min"),
 ("Planejamento","Planejamento estratégico para pequena empresa",I_D,"Um roteiro enxuto para quem nunca fez um plano formal.","8 min"),
 ("Pessoas","Team building funciona mesmo?",I_G,"O que diferencia uma vivência útil de um dia de recreação.","5 min"),
 ("RH","Por que tantas contratações não passam da experiência",I_F,"Três ajustes simples no processo seletivo que reduzem a rotatividade.","6 min")]
tr=[HOME,("Conteúdos","conteudos.html")]
cats=["Todos","Melhoria contínua","Indicadores","Qualidade","Gestão","Planejamento","Pessoas","RH"]
posts="".join(f'<a class="post rv d{i%3}" href="{ART}"><div class="ph"><img src="{img(im,800,500)}" alt="" loading="lazy"></div><div class="bd"><small>{c}</small><h3>{t}</h3><p>{p}</p><span class="by">Leitura de {m}</span></div></a>' for i,(c,t,im,p,m) in enumerate(POSTS))
body=phero(tr,"Conteúdos",'Gestão explicada <span class="it gold">sem complicação</span>',
 "Artigos práticos sobre melhoria contínua, indicadores, liderança e RH, para aplicar na sua empresa ainda nesta semana.",I_C,"","","short")
body+=f'''
<section class="sec light" style="padding-top:90px">
  <div class="wrap">
    <!-- Lista de exemplo. No site final, os artigos são publicados pela equipe ACK no painel (WordPress). -->
    <div class="filters rv">{"".join(f'<button{" class=on" if i==0 else ""}>{c}</button>' for i,c in enumerate(cats))}</div>
    <a class="feat rv" href="{ART}"><div class="ph"><img src="{img(I_A,1200,800)}" alt=""></div>
      <div class="bd"><small>Melhoria contínua · Destaque</small><h3>5S: por onde começar na sua empresa</h3><p>Os primeiros passos para organizar o ambiente de trabalho e, mais difícil, manter o padrão depois da primeira semana.</p><span class="by">Josemar Thans Ackler · Leitura de 7 min</span></div></a>
    <div class="posts">{posts}</div>
    <div class="news rv"><div><h3>Receba os próximos artigos</h3><p>Um e-mail por mês, com conteúdo prático sobre gestão e melhoria contínua.</p></div>
      <form><input type="email" required placeholder="Seu melhor e-mail" aria-label="E-mail"><button class="btn btn-gold" style="border:0;cursor:pointer;font-family:inherit">Quero receber</button></form></div>
  </div>
</section>
{final('Quer aplicar isso <span class="it gold">na sua empresa?</span>',"Os artigos mostram o caminho. Na consultoria, a gente percorre com você.")}
'''
P["conteudos.html"]=("Conteúdos sobre gestão, melhoria contínua e liderança · Instituto Ackler",
 "Artigos práticos sobre 5S, indicadores, causa raiz, PDCA, planejamento estratégico, team building e RH para pequenas empresas e indústrias.",
 "conteudos.html",body,tr,[{"@type":"Blog","name":"Conteúdos Instituto Ackler","publisher":{"@id":SITE+"/#org"}}])

# ============ ARTIGO (modelo) ============
tr=[HOME,("Conteúdos","conteudos.html"),("5S: por onde começar",ART)]
SECS=[("o-que-e","O que é o 5S"),("antes","Antes de começar"),("cinco","Os cinco sensos, um por um"),("manter","Como manter o padrão"),("erros","Erros mais comuns")]
toc="".join(f'<a href="#{k}">{t}</a>' for k,t in SECS)
sh_in='<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.5h4v11H3zM9.5 9.5h3.8v1.6h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.6 4.8 6v5.4h-4v-4.8c0-1.2 0-2.6-1.6-2.6s-1.9 1.3-1.9 2.5v4.9h-4z"/></svg>'
sh_wa='<svg viewBox="0 0 32 32" fill="currentColor"><path d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.6c-2 0-4-.6-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.6 10.6 0 1 1 16 26.6z"/></svg>'
sh_ln='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/></svg>'
body=f'''<div class="progress"></div>
'''+phero(tr,"Melhoria contínua",'5S: por onde começar <span class="it gold">na sua empresa</span>',
 "Os primeiros passos para organizar o ambiente de trabalho e, mais difícil, manter o padrão depois da primeira semana.",I_A,"",
 '<span>Josemar Thans Ackler</span><span>Leitura de 7 min</span>',"short")
body+=f'''
<section class="sec light" style="padding-top:80px">
  <div class="wrap agrid">
    <nav class="toc" aria-label="Neste artigo"><b>Neste artigo</b>{toc}</nav>
    <article class="article">
      <div class="tldr"><b>Resumo</b>O 5S é um método japonês de organização do ambiente de trabalho em cinco etapas: utilização, organização, limpeza, padronização e disciplina. Para dar certo, comece por uma área piloto pequena, envolva quem trabalha nela e defina desde o início como o padrão será auditado.</div>

      <h2 id="o-que-e">O que é o 5S</h2>
      <p>O 5S nasceu no Japão e ganhou o nome a partir de cinco palavras que começam com S: <em>seiri, seiton, seiso, seiketsu</em> e <em>shitsuke</em>. Em português, costumam ser chamados de sensos: utilização, organização, limpeza, padronização e disciplina.</p>
      <p>Na prática, o 5S é a base de qualquer programa de melhoria contínua. Sem um ambiente organizado, fica difícil enxergar desperdícios, medir tempo de processo ou identificar a causa de um problema.</p>

      <h2 id="antes">Antes de começar</h2>
      <p>O erro mais comum é tratar o 5S como um dia de faxina. Antes de mexer em qualquer coisa, defina três pontos:</p>
      <ol><li><strong>Uma área piloto.</strong> Escolha um setor pequeno e visível, onde o resultado vai aparecer rápido.</li><li><strong>Quem participa.</strong> As pessoas que trabalham na área precisam fazer parte do processo, e não só receber o resultado pronto.</li><li><strong>Como medir.</strong> Uma folha de auditoria simples, com nota de 1 a 5 para cada senso, já resolve.</li></ol>
      <figure><img src="{img(I_B,1200,675)}" alt="Posto de trabalho organizado" loading="lazy"><figcaption>Comece por uma área pequena e visível: o resultado serve de exemplo para o resto da empresa.</figcaption></figure>

      <h2 id="cinco">Os cinco sensos, um por um</h2>
      <h3>1. Utilização (seiri)</h3><p>Separe o que é necessário do que não é. Tudo que não foi usado nos últimos meses sai da área: vai para descarte, doação ou um local de espera identificado.</p>
      <h3>2. Organização (seiton)</h3><p>Cada item ganha um lugar definido, perto de onde é usado. Identifique com etiquetas, marcações no piso ou quadros de sombra para ferramentas.</p>
      <h3>3. Limpeza (seiso)</h3><p>Limpar é também inspecionar. Ao limpar uma máquina, o operador percebe vazamentos, folgas e desgastes antes que virem quebra.</p>
      <h3>4. Padronização (seiketsu)</h3><p>Registre como a área deve ficar, de preferência com fotos. O padrão visual vale mais do que um procedimento de várias páginas.</p>
      <h3>5. Disciplina (shitsuke)</h3><p>É o senso que segura os outros quatro. Ele aparece na rotina: auditorias periódicas, conversa sobre os resultados e correção rápida dos desvios.</p>

      <blockquote>O 5S não fracassa na implantação. Ele fracassa na terceira semana, quando ninguém mais olha.</blockquote>

      <h2 id="manter">Como manter o padrão</h2>
      <ul><li>Faça auditorias curtas e frequentes, conduzidas por pessoas de outras áreas.</li><li>Mostre as notas no quadro da equipe e comemore a evolução.</li><li>Reserve alguns minutos no fim do turno para a área voltar ao padrão.</li><li>Quando o padrão não for cumprido, pergunte por quê antes de cobrar: às vezes o lugar definido para um item simplesmente não funciona.</li></ul>

      <h2 id="erros">Erros mais comuns</h2>
      <p><strong>Começar pela empresa inteira.</strong> O esforço se dilui e nenhuma área chega ao padrão. <strong>Fazer sem a equipe.</strong> Quem não participou não se sente dono do resultado. <strong>Não ter auditoria.</strong> Sem medição, a área volta ao estado anterior em poucas semanas.</p>
      <p>Se a sua empresa já tentou o 5S e não conseguiu manter, o problema quase sempre está no quinto senso, e ele se resolve com rotina de gestão, não com mais limpeza.</p>

      <div class="share">Compartilhar
        <a href="https://www.linkedin.com/sharing/share-offsite/?url={SITE}/{ART}" aria-label="Compartilhar no LinkedIn">{sh_in}</a>
        <a href="https://wa.me/?text={SITE}/{ART}" aria-label="Compartilhar no WhatsApp">{sh_wa}</a>
        <a href="#" onclick="navigator.clipboard&&navigator.clipboard.writeText(location.href);return false" aria-label="Copiar link">{sh_ln}</a></div>
      <div class="author"><div class="av"><img src="{img(I_D,200,200)}" alt="Josemar Thans Ackler" loading="lazy"></div><div><b>Josemar Thans Ackler</b><p>Fundador do Instituto Ackler, com 35 anos de experiência em grandes indústrias no Brasil e no exterior.</p></div></div>
    </article>
  </div>
</section>

{band("Treinamento 5S na Prática",'Quer implantar o 5S <span class="it gold">com acompanhamento?</span>',"Levamos o treinamento para dentro da sua empresa, com uma área piloto e auditoria definida desde o primeiro dia.","Falar sobre 5S","contato.html?assunto=Treinamentos")}

<section class="sec light" style="padding-top:110px">
  <div class="wrap">
    {sec_head("Leia também",'Mais conteúdos <span class="it" style="color:var(--blue)">sobre gestão</span>')}
    <div class="posts">{"".join(f'<a class="post rv d{i%3}" href="{ART}"><div class="ph"><img src="{img(im,800,500)}" alt="" loading="lazy"></div><div class="bd"><small>{c}</small><h3>{t}</h3><p>{p}</p></div></a>' for i,(c,t,im,p,m) in enumerate(POSTS[:3]))}</div>
  </div>
</section>
'''
P[ART]=("5S: por onde começar na sua empresa · Instituto Ackler",
 "Guia prático de 5S: o que é, como escolher a área piloto, os cinco sensos explicados um a um, como manter o padrão e os erros mais comuns na implantação.",
 "conteudos.html",body,tr,[{"@type":"Article","headline":"5S: por onde começar na sua empresa","author":{"@type":"Person","name":"Josemar Thans Ackler"},"publisher":{"@id":SITE+"/#org"},"inLanguage":"pt-BR","mainEntityOfPage":SITE+"/"+ART}])

# ============ CONTATO ============
tr=[HOME,("Contato","contato.html")]
ASS=["Consultoria","Planejamento","Treinamentos","Team Building","Cursos","RH","Outro"]
ASSL={"Planejamento":"Planejamento 30 dias"}
pills="".join(f'<label><input type="radio" name="assunto" value="{a}"{" checked" if i==0 else ""}><span>{ASSL.get(a,a)}</span></label>' for i,a in enumerate(ASS))
body=phero(tr,"Contato",'Conte o desafio da sua empresa. <span class="it gold">A gente responde.</span>',
 "Uma conversa inicial, sem compromisso, para entender o momento da empresa e indicar a melhor frente de trabalho.",I_D,"","","short")
body+=f'''
<section class="sec" style="padding-top:56px">
  <div class="wrap cgrid2">
    <div>
      <span class="eyebrow rv">Fale direto</span>
      <h2 class="rv d1" style="margin-top:18px">O caminho mais rápido é o <span class="it gold">WhatsApp</span></h2>
      <p class="lead rv d2" style="margin-top:20px">Se preferir, preencha o formulário: a mensagem chega organizada para a nossa equipe e você continua a conversa pelo WhatsApp.</p>
      <div class="clist rv d2">
        <a href="{WA}"><i>{ico("wa",1.8)}</i><div><small>WhatsApp</small><b>(41) 99576-0079</b></div></a>
        <a href="mailto:contato@institutoackler.com.br"><i>{ico("mail",1.8)}</i><div><small>E-mail</small><b>contato@institutoackler.com.br</b></div></a>
        <div><i>{ico("pin",1.8)}</i><div><small>Escritório</small><b>Rua do Herval, 636 · Curitiba, PR</b></div></div>
      </div>
      <div class="values rv" style="margin-top:30px"><a href="https://www.linkedin.com/company/instituto-ackler"><span>LinkedIn</span></a><a href="https://www.instagram.com/institutoackler/"><span>Instagram</span></a><a href="https://www.youtube.com/@InstitutoAckler"><span>YouTube</span></a><a href="http://facebook.com/institutoackler"><span>Facebook</span></a></div>
    </div>
    <form class="form rv d1" id="cform">
      <h2>Envie sua mensagem</h2>
      <p>Respondemos pelo WhatsApp ou por e-mail.</p>
      <div class="fg">
        <div><label for="nome">Nome</label><input id="nome" name="nome" required autocomplete="name"></div>
        <div><label for="empresa">Empresa</label><input id="empresa" name="empresa" autocomplete="organization"></div>
        <div><label for="email">E-mail</label><input id="email" name="email" type="email" required autocomplete="email"></div>
        <div><label for="tel">WhatsApp</label><input id="tel" name="tel" type="tel" autocomplete="tel" placeholder="(41) 9 0000-0000"></div>
        <div class="full"><label>Tenho interesse em</label><div class="pills">{pills}</div></div>
        <div class="full"><label for="msg">Mensagem</label><textarea id="msg" name="msg" placeholder="Conte rapidamente o momento da empresa ou o que você procura"></textarea></div>
      </div>
      <button class="btn btn-gold" type="submit">Enviar pelo WhatsApp {ARROW}</button>
      <div class="ok">Abrimos o WhatsApp com a sua mensagem pronta. É só tocar em enviar.</div>
      <p class="lgpd">Usamos seus dados apenas para responder a este contato.</p>
    </form>
  </div>
</section>
<section class="mapfull" aria-label="Mapa"><iframe title="Mapa do escritório do Instituto Ackler" loading="lazy" src="https://www.google.com/maps?q=Rua+do+Herval,+636,+Curitiba,+PR&output=embed"></iframe></section>
'''
P["contato.html"]=("Contato · Instituto Ackler · Curitiba, PR",
 "Fale com o Instituto Ackler pelo WhatsApp (41) 99576-0079, e-mail ou formulário. Consultoria, treinamentos, cursos e RH em Curitiba, PR.",
 "contato.html",body,tr,[{"@type":"ContactPage","name":"Contato Instituto Ackler","about":{"@id":SITE+"/#org"}}])

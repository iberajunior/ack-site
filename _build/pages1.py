from lib import *

P = {}
HOME = ("Início","")

# ============ SOBRE ============
tr=[HOME,("Sobre","sobre.html")]
VALUES=[("star","Superar expectativas","Entregar o combinado e um pouco mais: o cliente percebe a diferença no resultado, não no discurso."),
        ("shield","Agir com integridade","Recomendamos só o que a empresa precisa. Se o problema for outro, a gente fala."),
        ("book","Nunca parar de aprender","Quem ensina melhoria contínua precisa praticar. Revisamos nossos próprios métodos a cada projeto."),
        ("loop","Flexibilidade","Cada negócio tem sua realidade. Ajustamos método, ritmo e escopo ao momento de cada empresa."),
        ("heart","Valorizar a vida","Produtividade que esgota as pessoas não se sustenta. Organização também é cuidado com quem trabalha.")]
body=phero(tr,"Sobre a ACK",'Experiência de indústria a serviço <span class="it gold">da sua empresa</span>',
  "Consultores com trajetória em indústrias globais como Tetra Pak e Mondelez, e vivência no dia a dia de pequenas e médias empresas. Levamos TPM, WCM e Lean para a prática.",I_D,
  btn("Conversar com a ACK","contato.html")+btn("Ver o que fazemos","consultoria-empresarial.html",False))
body+=f'''
<section class="sec">
  <div class="wrap about">
    <div class="about-img rv">
      <img src="{wix(JOSEMAR,900,1040,'t')}" alt="Josemar Ackler, fundador e CEO da ACK Institute" loading="lazy">
      <div class="sig"><b>Josemar Thans Ackler</b><small>Fundador e CEO da ACK Institute</small></div>
    </div>
    <div>
      <span class="eyebrow rv">Nossa jornada</span>
      <blockquote class="rv d1">Nascemos para cuidar de <em>pessoas</em> e de <em>negócios</em>. Uma empresa organizada produz mais e cuida melhor de quem trabalha nela.</blockquote>
      <div class="prose rv d2">
        <p>A ACK oferece soluções sob medida para cada empresa, entendendo que cada negócio tem sua própria realidade. Nossa atuação se apoia nas metodologias mais consolidadas do mercado, <strong>TPM, WCM e Lean</strong>, aplicadas de forma prática e evolutiva, numa jornada que leva a teoria para o dia a dia.</p>
        <p>O maior desafio das organizações está em alinhar pessoas, cultura e processos, e é aí que está a nossa força. Com experiência em cenários muito diferentes, apoiamos desde demandas simples até transformações de alta complexidade.</p>
        <p>O fundador, <strong>Josemar Ackler</strong>, soma mais de 35 anos em grandes indústrias no Brasil e no exterior. Na Tetra Pak, uma das pioneiras em TPM e WCM, foi Gerente de Qualidade e Produção. Depois, conduziu o piloto de implantação na Mondelez, em uma planta com mais de 5 mil colaboradores.</p>
      </div>
    </div>
  </div>
</section>

<div class="wrap"><div class="numbers rv">
  <div><b><span data-count="35">0</span></b><small>anos de experiência em grandes indústrias</small></div>
  <div><b>+<span data-count="20">0</span></b><small>cursos no portfólio</small></div>
  <div><b data-count="7">0</b><small>profissionais no time fixo</small></div>
  <div><b>4</b><small>frentes: consultoria, treinamentos, cursos e RH</small></div>
</div></div>

<section class="sec">
  <div class="wrap">
    {sec_head("Nossos valores",'O que guia <span class="it gold">cada projeto</span>',"Cinco princípios que aparecem na forma como a gente conversa, propõe e entrega.")}
    <div class="cards c3">{"".join(f'<div class="card sm rv d{i%3}"><span class="num">{i+1:02d}</span><div class="ico">{ico(k)}</div><h3>{t}</h3><p>{p}</p></div>' for i,(k,t,p) in enumerate(VALUES))}
      <a class="card sm rv d2" href="contato.html" style="background:linear-gradient(160deg,rgba(255,184,0,.16),rgba(255,184,0,.03));border-color:rgba(255,184,0,.35)"><div class="ico" style="background:rgba(255,184,0,.18);color:var(--gold)">{ico("brief")}</div><h3>Quer ver isso na prática?</h3><p>Conte o momento da sua empresa e receba uma indicação da melhor frente de trabalho.</p><span class="more">Falar com a ACK →</span></a>
    </div>
  </div>
</section>

<section class="sec light" id="time">
  <div class="wrap">
    {sec_head("Time de gestão e conselho",'Quem conduz <span class="it" style="color:var(--blue)">os projetos</span>',"Experiência em indústrias globais somada à vivência no atendimento a pequenas e médias empresas.")}
    {team_html()}
  </div>
</section>

<section class="sec tight">
  <div class="wrap split" style="align-items:center">
    <div><span class="eyebrow rv">Visão</span><h2 class="rv d1" style="margin-top:18px">Impacto que <span class="it gold">dura</span></h2></div>
    <p class="lead rv d2">Ser uma organização reconhecida pelo impacto duradouro, por meio de soluções personalizadas, cases de sucesso e uma rede de especialistas comprometidos com a excelência.</p>
  </div>
</section>

<section class="sec light">
  <div class="wrap">
    {sec_head("Como trabalhamos",'Melhoria contínua <span class="it" style="color:var(--blue)">na prática</span>',"O mesmo ciclo usado nas grandes indústrias, ajustado ao tamanho da sua operação.")}
    <div style="--line:#dcdaee">{steps([("Diagnóstico","Conversamos com a liderança e a equipe para entender processos, gargalos e números atuais."),("Plano","Definimos prioridades, metas e os indicadores que vão medir cada avanço."),("Implantação","Colocamos o plano em prática junto com o seu time, com treinamento onde for preciso."),("Acompanhamento","Medimos, ajustamos e mantemos a rotina de melhoria funcionando depois da entrega.")])}</div>
  </div>
</section>
{logos()}
{testimonials_section()}
{final('Conte o desafio da sua empresa. <span class="it gold">A gente mostra o caminho.</span>',"Uma conversa inicial, sem compromisso, para entender o momento da empresa e indicar a melhor frente de trabalho.")}
'''
P["sobre.html"]=("Sobre a ACK Institute · 35 anos de experiência industrial em gestão",
 "Conheça a ACK Institute, fundada por Josemar Thans Ackler após 35 anos em grandes indústrias. Consultoria, treinamentos, cursos e RH. Curitiba e São Paulo.",
 "sobre.html",body,tr,[{"@type":"AboutPage","name":"Sobre a ACK Institute","about":{"@id":SITE+"/#org"}},{"@type":"Person","name":"Josemar Thans Ackler","jobTitle":"Fundador","worksFor":{"@id":SITE+"/#org"}}])

# ============ CONSULTORIA ============
tr=[HOME,("Consultoria Empresarial","consultoria-empresarial.html")]
FAQ_C=[("A consultoria atende pequenas empresas?","Sim. Temos um formato pensado para pequenas e médias empresas, com escopo e duração menores. O método é o mesmo usado na indústria, ajustado à sua realidade."),
 ("Quanto tempo dura um projeto de consultoria?","Depende do escopo. Um planejamento estratégico pode ser feito em 30 dias. Projetos de implantação de rotina de gestão e melhoria de processos costumam ser acompanhados por alguns meses. Na conversa inicial a gente define o prazo junto com você."),
 ("A consultoria é presencial?","Pode ser presencial, a distância ou mista. Etapas como diagnóstico e implantação no chão de fábrica funcionam melhor presencialmente; o acompanhamento pode ser on-line."),
 ("Qual a diferença entre consultoria e treinamento?","Na consultoria, trabalhamos junto com a liderança para diagnosticar, planejar e implantar melhorias. No treinamento, capacitamos a equipe em um tema específico. Muitos projetos combinam os dois.")]
body=phero(tr,"Consultoria Empresarial",'Gestão organizada, <span class="it gold">resultado medido</span>',
 "Consultoria em gestão e governança para pequenas empresas e grandes indústrias. A gente diagnostica, monta o plano junto com a liderança e acompanha a implantação.",I_B,
 btn("Quero um diagnóstico da minha empresa","contato.html?assunto=Consultoria")+btn("Como funciona","#metodo",False),
 '<span><b>PME</b> e indústria</span><span>Presencial ou on-line</span><span>Com indicadores de acompanhamento</span>')
body+=f'''
<section class="sec">
  <div class="wrap">
    {sec_head("Para quem é",'Dois formatos, <span class="it gold">o mesmo método</span>',"O tamanho do projeto muda. A disciplina de diagnóstico, plano e acompanhamento continua a mesma.")}
    <div class="grid2">
      <div class="box rv"><div style="width:56px;height:56px;border-radius:16px;display:grid;place-items:center;background:rgba(61,155,233,.12);color:var(--sky);margin-bottom:24px">{ico("brief")}</div>
        <h3>Pequenas e médias empresas</h3><p>Para o empresário que concentra decisões, não tem números confiáveis e sente que a empresa depende dele para tudo. Organizamos processos, definimos poucos indicadores e criamos uma rotina simples de gestão.</p>
        {bullets(["Escopo enxuto e prazo curto","Foco nos gargalos que mais pesam no caixa","Rotina de gestão que o dono consegue manter"])}</div>
      <div class="box rv d1"><div style="width:56px;height:56px;border-radius:16px;display:grid;place-items:center;background:rgba(255,184,0,.14);color:var(--gold);margin-bottom:24px">{ico("chart")}</div>
        <h3>Médias e grandes indústrias</h3><p>Para plantas que precisam padronizar processos, reduzir perdas e alinhar áreas em torno de metas comuns. Trabalhamos com gestores e equipes de produção, qualidade e manutenção.</p>
        {bullets(["Mapeamento de processos e VSM","Desdobramento de metas e indicadores","Programas de melhoria contínua e governança"])}</div>
    </div>
  </div>
</section>

<section class="sec light">
  <div class="wrap">
    {sec_head("Nossas soluções",'Serviços para cada etapa da <span class="it" style="color:var(--blue)">maturidade operacional</span>',"Desenhados sob medida para gerar resultados práticos e mensuráveis, com base em TPM, WCM e Lean.")}
    {cards([("loop","Excelência Operacional","Diagnóstico e melhoria de processos para cortar desperdícios, eliminar gargalos e aumentar a produtividade real da operação.",[],"",None),
            ("chart","Indicadores e Performance","KPIs estratégicos para transformar metas em resultados, com foco em análise e tomada de decisão.",[],"",None),
            ("shield","Governança e Organização","Estruturas de gestão, rotinas e rituais que garantem foco, alinhamento e autonomia em todas as áreas.",[],"",None),
            ("people","Desenvolvimento de Lideranças","Treinamentos e mentorias práticas para formar líderes mais estratégicos, capazes de engajar e entregar.",[],"Ver treinamentos","treinamentos.html"),
            ("flow","Cultura de Melhoria Contínua","Mindset e ferramentas como PDCA, ACR, Kaizen e 5S para evoluir processos e comportamentos de forma contínua.",[],"",None),
            ("target","Planejamento Estratégico","Planos de ação com visão de futuro, metas claras e priorização do que realmente importa.",[],"Projeto de 30 dias","planejamento-estrategico.html")])}
  </div>
</section>

<section class="sec tight">
  <div class="wrap">
    {sec_head("Ramos de atuação",'Do escritório <span class="it gold">ao chão de fábrica</span>',"Empresas que cresceram rápido e hoje enfrentam gargalos, falhas recorrentes e falta de processos, em diferentes setores.")}
    {sectors_html()}
  </div>
</section>

<section class="sec" id="metodo">
  <div class="wrap">
    {sec_head("Como funciona",'Do diagnóstico <span class="it gold">ao resultado</span>',"Cada etapa termina com uma entrega concreta que fica com a sua empresa.")}
    {steps([("Diagnóstico","Entrevistas com a liderança, visita à operação e leitura dos números atuais."),("Plano","Prioridades, metas, indicadores e responsáveis definidos com o seu time."),("Implantação","Execução acompanhada, com treinamento da equipe onde for necessário."),("Acompanhamento","Reuniões de resultado, ajustes de rota e rotina funcionando sem depender da gente.")])}
  </div>
</section>

<section class="sec tight light">
  <div class="wrap split">
    <div class="img-r rv"><img src="{img(I_A,1000,1050)}" alt="Equipe revisando processos" loading="lazy"></div>
    <div>
      <span class="eyebrow rv">Sinais de alerta</span>
      <h2 class="rv d1" style="margin:18px 0 10px">Sua empresa precisa de consultoria quando…</h2>
      {bullets(["As decisões dependem sempre do dono ou de uma única pessoa","Ninguém sabe dizer com segurança qual é a margem de cada produto ou serviço","Os mesmos problemas voltam todo mês, mesmo depois de “resolvidos”","Cada área trabalha com metas diferentes, ou sem meta nenhuma","A empresa cresceu, mas os processos continuam os do começo"])}
      <div style="margin-top:34px" class="rv">{btn("Agendar uma conversa","contato.html?assunto=Consultoria")}</div>
    </div>
  </div>
</section>

{band("Projeto de 30 dias",'Comece pelo <span class="it gold">planejamento estratégico</span>',"Em 30 dias, você sai com metas, prioridades e indicadores definidos para o próximo ano.","Conhecer o projeto","planejamento-estrategico.html")}
{faq_section(FAQ_C)}
{final('Conte o desafio da sua empresa. <span class="it gold">A gente mostra o caminho.</span>',"Uma conversa inicial, sem compromisso, para entender o momento da empresa e indicar o formato de consultoria mais adequado.","Consultoria")}
'''
P["consultoria-empresarial.html"]=("Consultoria Empresarial em Gestão e Governança · ACK Institute",
 "Consultoria em gestão, governança, indicadores e processos para pequenas empresas e grandes indústrias. Diagnóstico, plano e acompanhamento. Curitiba e São Paulo.",
 "consultoria-empresarial.html",body,tr,[{"@type":"Service","name":"Consultoria Empresarial","serviceType":"Consultoria em gestão e governança","provider":{"@id":SITE+"/#org"},"areaServed":"BR","audience":{"@type":"BusinessAudience","name":"Pequenas e médias empresas e indústrias"}},faq_ld(FAQ_C)])

# ============ PLANEJAMENTO 30 DIAS ============
tr=[HOME,("Consultoria","consultoria-empresarial.html"),("Planejamento Estratégico","planejamento-estrategico.html")]
FAQ_P=[("O plano fica pronto mesmo em 30 dias?","Sim. O projeto é organizado em quatro semanas, com encontros marcados desde o início. Para isso funcionar, combinamos a agenda da liderança logo na primeira reunião."),
 ("Quem da empresa precisa participar?","O dono ou diretor e os principais gestores. Em empresas menores, às vezes são duas ou três pessoas. O importante é que quem decide esteja presente."),
 ("Serve para pequena empresa?","Serve. O projeto foi pensado justamente para empresas que nunca fizeram um planejamento formal e precisam de um plano simples de acompanhar."),
 ("E depois dos 30 dias?","Você sai com o plano e a rotina de acompanhamento definidos. Se quiser, a ACK continua acompanhando as reuniões de resultado ao longo do ano.")]
body=phero(tr,"Projeto de 30 dias",'Um <span class="it gold">2027</span> planejado, não improvisado',
 "Em 30 dias, montamos com você um plano estratégico sob medida: onde a empresa está, aonde quer chegar e quais indicadores vão mostrar o caminho.",I_E,
 btn("Quero o meu plano em 30 dias","contato.html?assunto=Planejamento")+btn("Ver as 4 semanas","#semanas",False),
 '<span><b>30</b> dias</span><span><b>4</b> encontros principais</span><span>Plano + indicadores + rotina</span>')
body+=f'''
<section class="cta-x" style="margin-top:110px">
  <canvas></canvas><div class="halo"></div>
  <div class="cta-in">
    <div class="rv"><span class="tag">Por que 30 dias</span><h2>Planejamento que leva meses <span class="it gold">fica na gaveta.</span></h2></div>
    <div class="cta-side rv d1"><p>Um prazo curto mantém a liderança focada e faz o plano sair do papel enquanto o assunto ainda está quente. Cada quadradinho abaixo é um dia do projeto.</p><div class="days" aria-hidden="true"></div></div>
  </div>
</section>

<section class="sec" id="semanas">
  <div class="wrap split" style="align-items:start">
    <div class="rv" style="position:sticky;top:120px"><span class="eyebrow">Semana a semana</span><h2 style="margin:18px 0 22px">Como os <span class="it gold">30 dias</span> são organizados</h2><p class="lead">Cada semana fecha uma parte do plano. Ao final, a empresa tem um documento único, simples de consultar e de acompanhar.</p></div>
    <div class="timeline rv d1">
      <div class="tl"><small>Semana 1</small><h3>Diagnóstico</h3><p>Entrevistas com a liderança, leitura dos números e análise do cenário: forças, fraquezas, oportunidades e ameaças.</p></div>
      <div class="tl"><small>Semana 2</small><h3>Direção</h3><p>Missão, visão e objetivos para o ano, escolhidos a partir do diagnóstico e do que os sócios querem para a empresa.</p></div>
      <div class="tl"><small>Semana 3</small><h3>Metas e indicadores</h3><p>Cada objetivo vira meta com número e prazo. Definimos os indicadores e quem responde por cada um.</p></div>
      <div class="tl" style="padding-bottom:0"><small>Semana 4</small><h3>Plano de ação e rotina</h3><p>Ações, responsáveis e datas. Fechamos com a agenda de reuniões de resultado para o ano inteiro.</p></div>
    </div>
  </div>
</section>

<section class="sec light">
  <div class="wrap split">
    <div>
      <span class="eyebrow rv">O que você recebe</span>
      <h2 class="rv d1" style="margin:18px 0 10px">Ao final do projeto, a empresa tem:</h2>
      {checks([("Diagnóstico do cenário","Retrato honesto de onde a empresa está hoje."),("Objetivos do ano","Poucos, claros e combinados entre os sócios."),("Painel de indicadores","Os números que mostram se o plano está funcionando."),("Plano de ação","Quem faz o quê, até quando."),("Rotina de acompanhamento","Calendário de reuniões de resultado."),("Liderança alinhada","Todo mundo puxando para o mesmo lado.")])}
      <div class="rv">{btn("Quero o meu plano em 30 dias","contato.html?assunto=Planejamento")}</div>
    </div>
    <div class="img-r rv d1"><img src="{img(I_E,1000,1100)}" alt="Reunião de planejamento estratégico" loading="lazy"></div>
  </div>
</section>
{faq_section(FAQ_P,'Dúvidas sobre o <span class="it gold">projeto de 30 dias</span>')}
{final('Comece o ano com <span class="it gold">um plano na mão.</span>',"Conte um pouco sobre a sua empresa e a gente verifica a próxima data disponível para iniciar o projeto.","Planejamento")}
'''
P["planejamento-estrategico.html"]=("Planejamento Estratégico em 30 dias para empresas · ACK Institute",
 "Projeto de Planejamento Estratégico em 30 dias: diagnóstico, objetivos, metas, indicadores e plano de ação para pequenas e médias empresas e indústrias.",
 "consultoria-empresarial.html",body,tr,[{"@type":"Service","name":"Planejamento Estratégico em 30 dias","serviceType":"Planejamento estratégico","provider":{"@id":SITE+"/#org"},"areaServed":"BR"},faq_ld(FAQ_P)])

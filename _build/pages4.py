from lib import *

P = {}
HOME = ("Início","")

# ============ EXCELÊNCIA OPERACIONAL (LEAN, TPM e WCM) ============
URL_EO = "consultoria-excelencia-operacional.html"
tr=[HOME,("Consultoria","consultoria-empresarial.html"),("Excelência Operacional","consultoria-excelencia-operacional.html")]
FAQ_EO=[("Como começa um projeto de excelência operacional?","Com uma imersão na empresa: entrevistas com a diretoria, leitura dos indicadores e visita ao chão de fábrica. Esse diagnóstico mostra onde estão as perdas e qual método faz mais sentido para a sua realidade."),
 ("Qual a diferença entre Lean, TPM e WCM?","O Lean ataca desperdícios no fluxo de valor. O TPM foca na eficiência dos equipamentos e no envolvimento de toda a equipe na manutenção. O WCM integra pilares técnicos e gerenciais num sistema completo de classe mundial. Muitas vezes combinamos os três."),
 ("Que resultados posso esperar?","Os mais comuns são aumento de eficiência (OEE), redução de quebras, perdas e custos, menos tempo de setup, mais qualidade e segurança e uma cultura de melhoria contínua que se mantém depois do projeto."),
 ("A ACK prepara a empresa para premiações JIPM?","Sim. Conduzimos a implantação das 12 etapas e dos 8 pilares do TPM e preparamos a planta para as auditorias de premiação do JIPM."),
 ("Em quais setores e regiões vocês atuam?","Atuamos em manufatura e serviços, como embalagens, papel e celulose, alimentos, bebidas, personal care e logística. Atendemos todo o Brasil e a América Latina, com unidades em Curitiba, São Paulo, Porto Alegre e Asunción.")]
EXP=[("search","Diagnóstico do sistema de gestão","Avaliamos o sistema de excelência operacional da empresa, mapeamos as oportunidades e montamos o plano de correção e implantação.",[],"",None),
 ("loop","TPM · Gestão da Performance Total","Implantação das 12 etapas e dos 8 pilares, no modelo que o cliente escolher, com preparação para premiações JIPM.",["12 etapas e 8 pilares","Preparação para o JIPM","Pilares sob demanda"],"",None),
 ("shield","Gestão da manutenção","Planejamento e controle da manutenção, rotina e indicadores, planos de manutenção e projetos de redução de quebras.",["PCM e indicadores","Análise de quebra e falha","5S nas oficinas"],"",None),
 ("star","WCM · World Class Manufacturing","Implantação dos pilares técnicos e gerenciais, com o sistema ajustado à necessidade de cada planta.",[],"",None),
 ("flow","Lean Manufacturing","Projetos de redução de desperdícios com as ferramentas certas para cada problema.",["VSM e Hoshin Kanri","SMED e Kanban","Kaizen e Six Sigma"],"",None),
 ("chart","Gerenciamento da rotina","Desdobramento da estratégia até o nível operacional, gestão visual e tratamento de desvios.",["Rotina das lideranças","Gestão visual","Acompanhamento de resultados"],"",None),
 ("people","Desenvolvimento de lideranças","Diagnóstico de perfis, coaching de líderes e gestão da mudança para sustentar a transformação.",[],"Ver treinamentos","treinamentos.html"),
 ("link","Gestão da logística","Mapeamento de processos logísticos, redução de estoques e de movimentação, picking e implantação de WMS.",[],"",None),
 ("brief","Excelência em serviços","Lean Office e Lean Service, gestão de processos (BPM) e melhoria de processos administrativos.",[],"",None)]
body=phero(tr,"Excelência Operacional",'LEAN, TPM e WCM para uma operação <span class="it gold">de classe mundial</span>',
 "Consultoria em Excelência Operacional para aumentar a eficiência, reduzir perdas e custos e criar resultados que se sustentam. Com a experiência de quem implantou TPM e WCM em grandes indústrias.",I_A,
 btn("Falar com um consultor","contato.html?assunto=Consultoria LEAN/TPM WCM")+btn("Conhecer o método","#metodo",False),
 '<span><b>LEAN</b> · TPM · WCM</span><span>Indústria e serviços</span><span>Brasil e América Latina</span>')
body+=f'''
<div class="wrap"><div class="numbers rv" style="margin-top:80px">
  <div><b><span data-count="35">0</span></b><small>anos de experiência em grandes indústrias</small></div>
  <div><b>+<span data-count="10">0</span></b><small>consultores associados</small></div>
  <div><b><span data-count="4">0</span></b><small>unidades: Curitiba, São Paulo, Porto Alegre e Asunción</small></div>
  <div><b>JIPM</b><small>preparação para premiações de TPM</small></div>
</div></div>

<section class="sec">
  <div class="wrap split" style="align-items:center">
    <div>
      <span class="eyebrow rv">O que é</span>
      <h2 class="rv d1" style="margin:18px 0 22px">Excelência operacional é <span class="it gold">método aplicado todos os dias</span></h2>
      <div class="prose rv d2">
        <p>Num mercado competitivo, a diferença entre as empresas está na forma como a operação funciona: quanto se perde, quanto se produz com o mesmo recurso e quão rápido os problemas são resolvidos.</p>
        <p>A ACK leva para a sua empresa as metodologias mais consolidadas da indústria, <strong>Lean, TPM e WCM</strong>, de forma prática e no ritmo da sua realidade. A gente trabalha lado a lado com o seu time até o método virar rotina.</p>
      </div>
      <div class="rv" style="margin-top:30px">{btn("Quero falar com um consultor","contato.html?assunto=Consultoria LEAN/TPM WCM")}</div>
    </div>
    <div class="img-r rv d1"><img src="{img(I_B,1000,1050)}" alt="Equipe aplicando ferramentas de excelência operacional" loading="lazy"></div>
  </div>
</section>

<section class="sec light">
  <div class="wrap">
    {sec_head("Expertise",'Soluções para cada etapa da <span class="it" style="color:var(--blue)">jornada operacional</span>',"Os principais temas que trabalhamos. O projeto combina as frentes de acordo com o diagnóstico.")}
    {cards(EXP)}
  </div>
</section>

<section class="sec" id="metodo">
  <div class="wrap">
    {sec_head("Abordagem",'Nosso método <span class="it gold">em 5 etapas</span>',"Do entendimento do negócio à transformação dos processos, sempre com o seu time envolvido.")}
    {steps([("Diagnóstico","Imersão na estratégia, nos indicadores e nos processos de produção, qualidade, manutenção e logística."),("Modelagem da solução","Definimos com o cliente os grupos de perdas a atacar e os métodos de excelência mais adequados."),("Validação","As iniciativas sugeridas são revisadas e ajustadas à experiência e à necessidade da empresa."),("Planejamento","Plano detalhado por ondas, combinando gestão de projetos tradicional e ágil."),("Transformação","Atuamos junto com a equipe, treinando, acompanhando e corrigindo rotas até o resultado aparecer.")])}
  </div>
</section>

{band("Redução de custos",'Quer saber quanto a sua operação <span class="it gold">está perdendo?</span>',"O Assessment Industrial mapeia perdas, monta o baseline de custos e mostra a curva de captura de resultados para os próximos 12 meses.","Conhecer o assessment","assessment-industrial.html")}
{logos()}
{faq_section(FAQ_EO,'Dúvidas sobre <span class="it gold">excelência operacional</span>')}
{final('Qual é o maior desafio da sua operação hoje? <span class="it gold">A gente ajuda a resolver.</span>',"Fale com um consultor da ACK e dê o primeiro passo para transformar os resultados da sua empresa.","Consultoria LEAN/TPM WCM")}
'''
P[URL_EO]=("Consultoria em Excelência Operacional: LEAN, TPM e WCM · ACK Institute",
 "Consultoria em Excelência Operacional com Lean Manufacturing, TPM e WCM: diagnóstico, gestão da manutenção, rotina, lideranças e preparação para o JIPM. Brasil e América Latina.",
 URL_EO,body,tr,[{"@type":"Service","name":"Consultoria em Excelência Operacional: LEAN, TPM e WCM","serviceType":"Excelência operacional, Lean Manufacturing, TPM e WCM","provider":{"@id":SITE+"/#org"},"areaServed":["BR","PY","Latin America"]},faq_ld(FAQ_EO)])

# ============ ASSESSMENT INDUSTRIAL (REDUÇÃO DE CUSTOS) ============
URL_AS = "assessment-industrial.html"
tr=[HOME,("Consultoria","consultoria-empresarial.html"),("Redução de Custos","assessment-industrial.html")]
FAQ_AS=[("O que é o Industrial Cost & Performance Assessment?","É um diagnóstico financeiro e operacional da sua indústria. Identificamos as perdas, construímos o baseline de custos e entregamos uma curva estruturada de captura de resultados."),
 ("Para quem é indicado?","Para CEOs, diretores industriais e financeiros que precisam reduzir custos com base em números, e não em cortes lineares."),
 ("Qual metodologia vocês usam?","Usamos como referência o TPM/JIPM, o Cost Deployment e práticas de excelência operacional, aplicados no Gemba e nos processos administrativos."),
 ("A economia é garantida?","Não trabalhamos com promessa de resultado. O assessment quantifica o potencial de cada oportunidade e mostra como capturá-lo; a captura depende da execução, que podemos acompanhar com a sua equipe.")]
PAINS=[("Custos elevados","Despesas industriais que crescem sem uma causa claramente identificada."),("Perdas invisíveis","Desperdícios incorporados à rotina da operação."),("Baixa produtividade","Equipamentos, processos e equipes abaixo do potencial."),("Falta de captura","Projetos de melhoria que não se convertem em economia comprovada.")]
AREAS=[("brief","Matéria-prima"),("people","Mão de obra"),("shield","Manutenção"),("chart","Performance"),("star","Qualidade"),("loop","Energia e utilidades"),("link","Logística e estoques"),("flow","Processos administrativos"),("target","Gestão e governança")]
CURVE=[0,5,10,20,30,40,50,60,70,80,90,100]
def curve_svg():
    W,H,pl,pb,pt=720,300,48,34,16
    bw=(W-pl-12)/len(CURVE)
    g=[]
    for v in (0,30,60,90,120):
        y=pt+(H-pt-pb)*(1-v/120)
        g.append(f'<line x1="{pl}" y1="{y:.1f}" x2="{W-6}" y2="{y:.1f}"/><text x="{pl-10}" y="{y+4:.1f}" text-anchor="end">{v}</text>')
    bars=[]
    for i,v in enumerate(CURVE):
        h=(H-pt-pb)*v/120; x=pl+i*bw+bw*.18; y=H-pb-h
        bars.append(f'<rect class="b" x="{x:.1f}" y="{y:.1f}" width="{bw*.64:.1f}" height="{max(h,1.5):.1f}" rx="4"><title>M{i+1}: R$ {v} mil</title></rect><text class="m" x="{x+bw*.32:.1f}" y="{H-12}" text-anchor="middle">M{i+1}</text>')
    return f'<svg class="curve" viewBox="0 0 {W} {H}" role="img" aria-label="Exemplo ilustrativo da curva de captura mensal, de R$ 0 no mês 1 até R$ 100 mil no mês 12"><g class="grid">{"".join(g)}</g>{"".join(bars)}</svg>'
body=phero(tr,"Cost & Performance Assessment",'Quanto dinheiro sua indústria <span class="it gold">está deixando de ganhar?</span>',
 "Descubra, quantifique e capture. Identificamos as perdas industriais, construímos o baseline de custos e estruturamos uma curva de captura de resultados para a sua operação.",I_G,
 btn("Quero avaliar minha indústria","contato.html?assunto=Assessment Industrial")+btn("Ver a metodologia","#metodo",False),
 '<span>Diagnóstico <b>financeiro</b> e operacional</span><span>Baseline de custos</span><span>Curva de captura de 12 meses</span>')
body+=f'''
<section class="sec">
  <div class="wrap">
    {sec_head("O problema",'Sua operação pode estar escondendo <span class="it gold">oportunidades milionárias</span>',"Muitas indústrias conhecem seus custos, mas não conseguem dizer com precisão onde estão as perdas, quanto elas representam e como transformá-las em resultado financeiro.")}
    <div class="cards c4 sm">{"".join(f'<div class="card rv d{i%3}"><span class="num">{i+1:02d}</span><h3>{t}</h3><p>{p}</p></div>' for i,(t,p) in enumerate(PAINS))}</div>
  </div>
</section>

<section class="sec light" id="metodo">
  <div class="wrap">
    {sec_head("Nossa metodologia",'Do diagnóstico <span class="it" style="color:var(--blue)">à captura financeira</span>',"Uma abordagem que conecta custos, perdas operacionais, maturidade industrial e execução.")}
    <div style="--line:#dcdaee">{steps([("Baseline de custos","Consolidação da estrutura de custos, dos indicadores e do desempenho histórico da operação."),("Mapeamento de perdas","Identificação e quantificação das perdas no Gemba e nos processos administrativos."),("Potencial de captura","Priorização das oportunidades por impacto financeiro, esforço e investimento."),("Curva de captura","Cronograma de resultados com metas mensais e responsáveis.")])}</div>
  </div>
</section>

<section class="sec tight">
  <div class="wrap">
    {sec_head("Onde buscamos oportunidades",'Os componentes que <span class="it gold">definem o seu custo</span>',"Avaliamos os principais componentes do custo industrial e os fatores que determinam a eficiência da operação.")}
    <div class="sectors">{"".join(f'<div class="sector rv d{i%3}"><i>{ico(k)}</i><span>{t}</span></div>' for i,(k,t) in enumerate(AREAS))}</div>
    <p class="note rv">Referências metodológicas: TPM/JIPM, Cost Deployment e práticas de excelência operacional.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap split" style="align-items:center">
    <div>
      <span class="eyebrow rv">Entregável principal</span>
      <h2 class="rv d1" style="margin:18px 0 22px">Uma curva de captura de resultados <span class="it gold">para a sua indústria</span></h2>
      <p class="lead rv d2">Mais do que apresentar oportunidades, mostramos como elas se transformam em resultado ao longo dos meses.</p>
      <div class="cstats rv d2"><div><b>R$ 555 mil</b><small>captura acumulada no exemplo</small></div><div><b>R$ 1,2 mi</b><small>run rate anualizado no M12</small></div></div>
    </div>
    <figure class="curvebox rv d1">
      <figcaption><b>R$ 100 mil/mês</b><small>potencial no estágio de plena implantação das iniciativas</small></figcaption>
      {curve_svg()}
      <p>Exemplo hipotético de evolução da captura mensal, em milhares de reais. Simulação ilustrativa, não representa promessa de economia ou resultado garantido.</p>
    </figure>
  </div>
</section>

<section class="sec light">
  <div class="wrap split">
    <div>
      <span class="eyebrow rv">O que sua empresa recebe</span>
      <h2 class="rv d1" style="margin:18px 0 10px">Ao final do assessment, a diretoria tem:</h2>
      {checks([("Baseline financeiro e operacional","O ponto de partida em números."),("Mapa de perdas e oportunidades","Onde a operação perde dinheiro."),("Matriz de priorização financeira","Impacto, esforço e investimento de cada frente."),("Potencial de captura por iniciativa","Quanto cada ação pode trazer."),("Curva de captura de 12 meses","Metas mensais e responsáveis."),("Roadmap e apresentação executiva","Execução, governança e a visão para a diretoria.")])}
      <div class="rv">{btn("Quero avaliar minha indústria","contato.html?assunto=Assessment Industrial")}</div>
    </div>
    <div class="img-r rv d1"><img src="{img(I_A,1000,1100)}" alt="Análise de perdas no chão de fábrica" loading="lazy"></div>
  </div>
</section>

{band("Excelência operacional",'Não basta identificar perdas. <span class="it gold">É preciso capturar resultados.</span>',"A ACK combina experiência industrial, gestão de custos e execução para transformar oportunidades em resultados sustentáveis.","Conhecer a consultoria",URL_EO)}
{faq_section(FAQ_AS,'Dúvidas sobre o <span class="it gold">assessment</span>')}
{final('Vamos avaliar o potencial <span class="it gold">da sua indústria?</span>',"Conte um pouco sobre a sua operação e a nossa equipe entra em contato para agendar a conversa.","Assessment Industrial")}
'''
P[URL_AS]=("Redução de Custos Industriais · Cost & Performance Assessment · ACK Institute",
 "Industrial Cost & Performance Assessment: identificamos perdas, construímos o baseline de custos e entregamos a curva de captura de resultados da sua indústria.",
 URL_AS,body,tr,[{"@type":"Service","name":"Industrial Cost & Performance Assessment","serviceType":"Redução de custos industriais e diagnóstico de perdas","provider":{"@id":SITE+"/#org"},"areaServed":["BR","PY"],"audience":{"@type":"BusinessAudience","name":"CEOs, diretores industriais e financeiros"}},faq_ld(FAQ_AS)])

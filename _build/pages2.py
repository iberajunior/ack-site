from lib import *
P = {}
HOME = ("Início","")

# ============ TREINAMENTOS ============
tr=[HOME,("Treinamentos","treinamentos.html")]
TEMAS=[("5S na prática",I_A,"Organização, limpeza e padrão no posto de trabalho","In company · Curso"),
 ("Análise de Causa Raiz",I_B,"Ishikawa, 5 porquês e plano de ação","In company · Curso"),
 ("PDCA e Ferramentas da Qualidade",I_C,"O ciclo de melhoria e as 7 ferramentas","Curso"),
 ("Mapeamento de Processos e VSM",I_D,"Fluxo de valor, desperdícios e estado futuro","In company · Curso"),
 ("Planejamento Estratégico",I_E,"Objetivos, metas e indicadores para gestores","In company"),
 ("Comunicação Assertiva e Perfis Comportamentais",I_F,"Feedback, conflitos e trabalho em equipe","In company"),
 ("Gestão do Tempo e Produtividade",I_G,"Prioridades, agenda e reuniões que rendem","In company"),
 ("Lean e Indústria 4.0",I_A,"Fundamentos lean e transformação digital","Curso"),
 ("Normas ISO",I_C,"Interpretação e preparação para auditoria","In company")]
FAQ_T=[("Os treinamentos são feitos dentro da empresa?","Sim. O formato principal é in company, na estrutura da sua empresa, com exemplos tirados da sua operação. Alguns temas também existem como curso aberto ou on-line."),
 ("Dá para adaptar a carga horária?","Dá. Ajustamos carga horária, turno e formato (um dia inteiro, módulos semanais ou encontros curtos) conforme a rotina da equipe."),
 ("Os participantes recebem certificado?","Sim, emitimos certificado de participação para quem cumpre a carga horária do treinamento."),
 ("Qual o número de participantes por turma?","Depende do tema. Treinamentos práticos como 5S e causa raiz funcionam melhor com turmas menores; temas comportamentais aceitam grupos maiores. Combinamos isso na proposta.")]
rows="".join(f'<a class="trow" href="contato.html?assunto=Treinamentos" data-img="{img(i,600,440)}"><span class="n">{k+1:02d}</span><div><h3>{t}</h3><small style="display:block;margin-top:8px;color:#5c5a80;font-size:14px">{d}</small></div><span class="tg">{"".join(f"<em>{x.strip()}</em>" for x in tg.split("·"))}</span></a>' for k,(t,i,d,tg) in enumerate(TEMAS))
body=phero(tr,"Treinamentos In Company",'Escolha o tema. <span class="it gold">A gente adapta</span> para a sua equipe.',
 "Treinamentos em melhoria contínua, qualidade, gestão e comportamento, aplicados dentro da sua empresa com carga horária e exemplos da sua operação.",I_A,
 btn("Solicitar proposta de treinamento","contato.html?assunto=Treinamentos")+btn("Ver os temas","#temas",False),
 '<span>Na sua empresa</span><span>Conteúdo ajustado</span><span>Com certificado</span>')
body+=f'''
<section class="sec">
  <div class="wrap">
    {sec_head("Por que in company",'Treinamento que <span class="it gold">vira rotina</span>',"Quando a equipe aprende com os problemas reais da própria operação, o conteúdo sai da sala e vai para o dia a dia.")}
    {cards([("target","Exemplos da sua operação","Antes do treinamento, conhecemos a realidade da equipe e trazemos casos do seu próprio processo.",[],"",None),
            ("clock","Agenda que cabe na produção","Turnos, módulos curtos ou imersão de um dia. A equipe não precisa parar a operação.",[],"",None),
            ("loop","Aplicação logo depois","Cada treinamento termina com um plano de aplicação para o time colocar em prática.",[],"",None)])}
  </div>
</section>

<section class="sec light" id="temas" style="padding-top:110px">
  <div class="wrap">
    {sec_head("Temas disponíveis",'Os treinamentos <span class="it" style="color:var(--blue)">mais pedidos</span>',"Não encontrou o tema? Muitos treinamentos são montados sob medida a partir da necessidade da empresa.")}
    <div class="tlist">{rows}</div>
    <div style="margin-top:44px;display:flex;gap:14px;flex-wrap:wrap" class="rv">{btn("Solicitar proposta","contato.html?assunto=Treinamentos")}<a class="btn" style="border:1px solid #d5d3ea" href="cursos.html">Ver cursos abertos e on-line</a></div>
  </div>
</section>
<div class="preview" id="preview"><img alt=""></div>

<section class="sec light" style="padding-top:20px">
  <div class="wrap">
    {sec_head("In company ou curso?",'Qual formato faz <span class="it" style="color:var(--blue)">mais sentido</span>')}
    <div class="cmp-wrap rv"><table class="cmp">
      <thead><tr><th></th><th>Treinamento in company</th><th>Curso (aberto ou on-line)</th></tr></thead>
      <tbody>
        <tr><td>Para quem</td><td>Equipes de uma mesma empresa</td><td>Profissionais que querem se desenvolver individualmente</td></tr>
        <tr><td>Conteúdo</td><td>Ajustado à realidade da empresa</td><td>Programa padrão do curso</td></tr>
        <tr><td>Local e agenda</td><td>Na empresa, na data combinada</td><td>Turmas abertas ou acesso on-line</td></tr>
        <tr><td>Como contratar</td><td>Proposta pelo WhatsApp ou formulário</td><td>Compra direta na página do curso</td></tr>
      </tbody></table></div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    {sec_head("Como contratar",'Da conversa <span class="it gold">à sala de treinamento</span>')}
    {steps([("Conversa","Você conta o desafio da equipe e o resultado que espera."),("Proposta","Indicamos tema, carga horária, formato e investimento."),("Ajuste","Conhecemos a operação e adaptamos exemplos e exercícios."),("Aplicação","Treinamento, avaliação e plano de ação para o time.")])}
  </div>
</section>
{faq_section(FAQ_T,'Dúvidas sobre <span class="it gold">treinamentos</span>')}
{final('Qual é o desafio da <span class="it gold">sua equipe?</span>',"Conte o tema, o número de pessoas e o resultado que você espera. A gente monta a proposta.","Treinamentos")}
'''
P["treinamentos.html"]=("Treinamentos In Company: 5S, Causa Raiz, PDCA, Lean e ISO · ACK Institute",
 "Treinamentos in company em 5S, análise de causa raiz, PDCA, mapeamento de processos, Lean, normas ISO, comunicação e gestão do tempo. Conteúdo adaptado à sua empresa.",
 "treinamentos.html",body,tr,[{"@type":"Service","name":"Treinamentos In Company","serviceType":"Treinamento corporativo","provider":{"@id":SITE+"/#org"},"areaServed":"BR",
   "hasOfferCatalog":{"@type":"OfferCatalog","name":"Temas de treinamento","itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":t}} for t,*_ in TEMAS]}},faq_ld(FAQ_T)])

# ============ TEAM BUILDING ============
tr=[HOME,("Treinamentos","treinamentos.html"),("Team Building","team-building.html")]
FAQ_TB=[("Qual a diferença entre in company e offsite?","No in company, as atividades acontecem na estrutura da sua empresa, adaptadas à rotina. No offsite, a equipe sai do ambiente de trabalho para uma imersão completa, o que ajuda a desligar do dia a dia."),
 ("O team building é só recreação?","Não. As atividades são práticas e divertidas, mas cada uma tem um objetivo ligado ao trabalho: comunicação, cooperação, liderança ou compromisso com resultado. No fim, o grupo conversa sobre o que viveu e o que leva para a rotina."),
 ("Para quantas pessoas funciona?","Para equipes pequenas e grandes. O formato e a quantidade de facilitadores mudam conforme o tamanho do grupo."),
 ("Quanto tempo dura?","De algumas horas a um dia inteiro ou mais, dependendo do objetivo e do formato escolhido.")]
body=phero(tr,"Team Building",'Times que confiam uns nos outros <span class="it gold">entregam mais</span>',
 "Vivências práticas, dentro da empresa ou fora dela, para melhorar comunicação, cooperação e compromisso da equipe com os resultados.",I_G,
 btn("Planejar um team building","contato.html?assunto=Team Building")+btn("Ver formatos","#formatos",False))
body+=f'''
<section class="sec light">
  <div class="wrap split">
    <div class="tilt rv"><div class="tilt-in">
      <img src="{wix("b2ec3b_a852c1191f144a999cc6776fbd128753~mv2.jpg",1000,1100)}" alt="Team building com Lego no Grupo Risotolândia" loading="lazy">
      <div class="tilt-badge"><span>Case Grupo Risotolândia</span><span>45 profissionais de PCP</span><span>Dinâmica com Lego</span></div>
    </div></div>
    <div>
      <span class="eyebrow rv">Por que fazer</span>
      <h2 class="rv d1" style="margin:18px 0 22px">O que muda na equipe <span class="it" style="color:var(--blue)">depois da vivência</span></h2>
      <p class="lead rv d2">Problemas de equipe raramente se resolvem com mais uma reunião. Em situações práticas, as pessoas enxergam como se comunicam, como decidem e como reagem sob pressão.</p>
      {bullets(["Comunicação mais direta entre áreas e níveis hierárquicos","Mais cooperação e menos disputa interna","Líderes que entendem melhor o próprio time","Compromisso coletivo com metas e resultados"])}
      <p class="rv" style="margin-top:26px;color:#5c5a80;line-height:1.65;font-size:15px">No Grupo Risotolândia, reunimos mais de 45 profissionais do PCP em uma dinâmica com Lego desenhada para fortalecer a colaboração, a comunicação e a confiança.</p>
    </div>
  </div>
</section>

<section class="sec" id="formatos">
  <div class="wrap">
    {sec_head("Formatos",'Escolha o formato <span class="it gold">pelo objetivo</span>',"Cada programa é montado a partir do que a empresa quer desenvolver na equipe.")}
    {cards([("brief","In Company","Na estrutura da sua empresa, adaptado à rotina da equipe e ao espaço disponível.",[],"",None),
            ("pin","Offsite","Fora do ambiente de trabalho, com imersão completa e tempo para o grupo se conectar.",[],"",None),
            ("star","Liderança","Para gestores que precisam engajar o time, delegar melhor e conduzir conversas difíceis.",[],"",None),
            ("people","Integração","Para equipes novas, fusões de áreas ou momentos de mudança na empresa.",[],"",None)],"")}
  </div>
</section>

<section class="sec light">
  <div class="wrap">
    {sec_head("Como funciona",'Do objetivo <span class="it" style="color:var(--blue)">ao plano de ação</span>')}
    {steps([("Briefing","Entendemos o momento da equipe e o que a liderança quer desenvolver."),("Desenho","Montamos as atividades, o roteiro e a logística do formato escolhido."),("Vivência","Facilitadores conduzem as dinâmicas e as conversas de fechamento."),("Desdobramento","Entregamos um resumo com os aprendizados e combinados do grupo.")])}
  </div>
</section>
{faq_section(FAQ_TB,'Dúvidas sobre <span class="it gold">team building</span>')}
{final('Vamos planejar a próxima <span class="it gold">vivência da sua equipe?</span>',"Conte quantas pessoas, o objetivo e o formato que você imagina. A gente monta a proposta.","Team Building")}
'''
P["team-building.html"]=("Team Building In Company e Offsite para equipes · ACK Institute",
 "Programas de team building in company e offsite para melhorar comunicação, cooperação, liderança e compromisso da equipe com resultados. Curitiba e região.",
 "team-building.html",body,tr,[{"@type":"Service","name":"Team Building","serviceType":"Team building corporativo","provider":{"@id":SITE+"/#org"},"areaServed":"BR"},faq_ld(FAQ_TB)])

# ============ RH ============
tr=[HOME,("Consultoria","consultoria-empresarial.html"),("Serviços de RH","servicos-de-rh.html")]
FAQ_RH=[("O que é BPO em RH?","É a terceirização de rotinas do departamento de pessoas, como processos de admissão, controles e indicadores de RH. A empresa ganha método sem precisar montar uma equipe interna completa."),
 ("Vocês fazem recrutamento para qualquer cargo?","Atendemos vagas operacionais, técnicas e de liderança. Na conversa inicial avaliamos o perfil da vaga e o prazo."),
 ("Como funciona a análise de perfil comportamental?","Os colaboradores respondem a um questionário e recebem uma devolutiva. A liderança usa o resultado para montar equipes, dar feedback e escolher quem ocupa cada função."),
 ("Atendem empresas que não têm RH estruturado?","Sim, e é aí que costumamos ajudar mais. Muitas empresas pequenas começam com recrutamento ou perfis comportamentais e depois estruturam o restante.")]
body=phero(tr,"Serviços de RH",'Um RH que funciona <span class="it gold">com método</span>',
 "Consultoria e treinamentos para o departamento de pessoas: recrutamento e seleção, BPO em RH e análise de perfis comportamentais.",I_F,
 btn("Falar sobre o RH da minha empresa","contato.html?assunto=RH")+btn("Ver serviços","#servicos",False))
body+=f'''
<section class="sec" id="servicos">
  <div class="wrap">
    {sec_head("O que fazemos",'Serviços para cada <span class="it gold">etapa do RH</span>',"Você pode contratar um serviço isolado ou estruturar o departamento por completo.")}
    {cards([("search","Recrutamento e seleção","Da descrição da vaga à indicação dos finalistas, com entrevistas por competência.",["Perfil da vaga","Triagem e entrevistas","Parecer dos finalistas"],"",None),
            ("brief","BPO em RH","Rotinas de RH terceirizadas, com processos claros e indicadores.",["Admissão e integração","Controles e rotinas","Indicadores de RH"],"",None),
            ("id","Perfis comportamentais","Mapeamento do perfil de cada colaborador para decisões de equipe.",["Questionário e devolutiva","Leitura para a liderança","Apoio em feedbacks"],"",None),
            ("people","Consultoria e treinamentos de RH","Estrutura, políticas e capacitação de quem cuida de pessoas.",["Cargos e responsabilidades","Integração de novos colaboradores","Treinamento de gestores"],"",None)],"")}
  </div>
</section>

<section class="sec light">
  <div class="wrap split">
    <div>
      <span class="eyebrow rv">Quando faz sentido</span>
      <h2 class="rv d1" style="margin:18px 0 10px">Sinais de que o RH <span class="it" style="color:var(--blue)">precisa de reforço</span></h2>
      {bullets(["Contratações que não passam do período de experiência","Vagas abertas por muito tempo, atrapalhando a operação","Conflitos de equipe sem critério claro para resolver","Rotinas de RH concentradas em uma única pessoa","Crescimento rápido sem processo de integração de novos colaboradores"])}
      <div style="margin-top:34px" class="rv">{btn("Agendar uma conversa","contato.html?assunto=RH")}</div>
    </div>
    <div class="img-r rv d1"><img src="{img(I_F,1000,1050)}" alt="Entrevista de seleção" loading="lazy"></div>
  </div>
</section>
{faq_section(FAQ_RH,'Dúvidas sobre <span class="it gold">serviços de RH</span>')}
{final('Pessoas certas, <span class="it gold">no lugar certo.</span>',"Conte o que está pesando no RH da sua empresa e a gente indica por onde começar.","RH")}
'''
P["servicos-de-rh.html"]=("Serviços de RH: Recrutamento, BPO e Perfil Comportamental · ACK Institute",
 "Recrutamento e seleção, BPO em RH, análise de perfis comportamentais e consultoria para estruturar o departamento de pessoas. Curitiba e São Paulo.",
 "consultoria-empresarial.html",body,tr,[{"@type":"Service","name":"Serviços de RH","serviceType":"Recrutamento e seleção, BPO em RH, perfis comportamentais","provider":{"@id":SITE+"/#org"},"areaServed":"BR"},faq_ld(FAQ_RH)])

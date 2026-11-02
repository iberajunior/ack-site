/* Instituto Ackler · scripts do site (todas as páginas) */
(()=>{
const $=(s,c=document)=>c.querySelector(s), $$=(s,c=document)=>[...c.querySelectorAll(s)];
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
const fine=matchMedia('(pointer: fine)').matches;

/* header */
const hd=$('#hd');
if(hd){const f=()=>hd.classList.toggle('scrolled',scrollY>40);addEventListener('scroll',f,{passive:true});f();}

/* menu mobile */
const dr=$('#drawer'), bg=$('.burger');
if(dr&&bg){const t=o=>{dr.classList.toggle('open',o);document.body.classList.toggle('lock',o)};
  bg.onclick=()=>t(true); $('.x',dr).onclick=()=>t(false); $$('a',dr).forEach(a=>a.addEventListener('click',()=>t(false)));
  addEventListener('keydown',e=>{if(e.key==='Escape')t(false)});}

/* revelar ao rolar + contadores */
const io=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return; e.target.classList.add('in');
  e.target.querySelectorAll('[data-count]').forEach(c=>{if(c._d)return;c._d=1;const t=+c.dataset.count,s=performance.now();
    const f=n=>{const k=Math.min((n-s)/1400,1);c.textContent=Math.round(t*(1-Math.pow(1-k,3)));if(k<1)requestAnimationFrame(f)};requestAnimationFrame(f)});
  io.unobserve(e.target)}),{threshold:.12});
$$('.rv').forEach(el=>io.observe(el));

/* cards: brilho que segue o mouse */
$$('.card').forEach(c=>c.addEventListener('pointermove',e=>{const r=c.getBoundingClientRect();c.style.setProperty('--x',e.clientX-r.left+'px');c.style.setProperty('--y',e.clientY-r.top+'px')}));

/* botões magnéticos */
if(fine) $$('.magnetic').forEach(b=>{b.addEventListener('pointermove',e=>{const r=b.getBoundingClientRect();b.style.transform=`translate(${(e.clientX-r.left-r.width/2)*.25}px,${(e.clientY-r.top-r.height/2)*.35}px)`});b.addEventListener('pointerleave',()=>b.style.transform='')});

/* HOME: vídeos do topo com crossfade */
const v1=$('#v1'),v2=$('#v2');
if(v1&&v2){const v=[v1,v2],dots=[$('#d1'),$('#d2')];let cur=0,paused=false;
  function swap(){const nx=1-cur;v[nx].currentTime=0;v[nx].play().catch(()=>{});v[nx].classList.remove('off');v[cur].classList.add('off');
    dots[cur].classList.remove('on');void dots[nx].offsetWidth;dots[nx].style.setProperty('--d',(v[nx].duration||9)+'s');dots[nx].classList.add('on');cur=nx;}
  v.forEach((el,i)=>{el.addEventListener('ended',()=>{if(i===cur)swap()});el.addEventListener('loadedmetadata',()=>{if(i===cur)dots[i].style.setProperty('--d',el.duration+'s')});
    el.addEventListener('timeupdate',()=>{if(i===cur&&el.duration&&el.duration-el.currentTime<1.1&&!el._x){el._x=1;swap();setTimeout(()=>el._x=0,2000)}})});
  const vb=$('#vbtn');
  vb.onclick=()=>{paused=!paused;paused?v[cur].pause():v[cur].play();vb.innerHTML=paused?'<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M7 4l13 8-13 8z"/></svg>':'<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M6 4h4v16H6zM14 4h4v16h-4z"/></svg>';dots[cur].style.animationPlayState=paused?'paused':'running'};
  if(reduce)v.forEach(x=>{x.pause();x.removeAttribute('autoplay')});}

/* palavra rotativa */
const rs=$$('.rotator span');let ri=0;
if(rs.length&&!reduce)setInterval(()=>{rs[ri].classList.remove('on');rs[ri].classList.add('out');const p=ri;setTimeout(()=>rs[p].classList.remove('out'),600);ri=(ri+1)%rs.length;rs[ri].classList.add('on')},2600);

/* faixa de logos */
const mq=$('#marq'); if(mq)mq.appendChild(mq.firstElementChild.cloneNode(true));

/* CTA com grade de pontos reativa ao mouse */
$$('.cta-x').forEach(cta=>{const cv=$('canvas',cta);if(!cv)return;const ctx=cv.getContext('2d');
  let W,H,pts=[],mx=-999,my=-999,tmx=-999,tmy=-999;const dpr=Math.min(devicePixelRatio||1,2);
  function size(){const r=cta.getBoundingClientRect();W=r.width;H=r.height;cv.width=W*dpr;cv.height=H*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);pts=[];const g=34;for(let y=g/2;y<H;y+=g)for(let x=g/2;x<W;x+=g)pts.push({x,y})}
  size();addEventListener('resize',size);
  cta.addEventListener('pointermove',e=>{const r=cta.getBoundingClientRect();tmx=e.clientX-r.left;tmy=e.clientY-r.top;cta.style.setProperty('--mx',tmx+'px');cta.style.setProperty('--my',tmy+'px')});
  cta.addEventListener('pointerleave',()=>{tmx=tmy=-999});
  function draw(){mx+=(tmx-mx)*.12;my+=(tmy-my)*.12;ctx.clearRect(0,0,W,H);
    for(const p of pts){const dx=p.x-mx,dy=p.y-my,d=Math.hypot(dx,dy),k=Math.max(0,1-d/220);const ox=k?dx/d*k*14:0,oy=k?dy/d*k*14:0;
      ctx.fillStyle=k>0.02?`rgba(255,${Math.round(184+71*(1-k))},${Math.round(255*(1-k))},${.18+k*.8})`:'rgba(236,232,255,.13)';
      ctx.beginPath();ctx.arc(p.x+ox,p.y+oy,1.2+k*2.6,0,6.283);ctx.fill();}
    requestAnimationFrame(draw)}
  if(!reduce)draw();
  const days=$('.days',cta);
  if(days){for(let i=0;i<30;i++)days.appendChild(document.createElement('i'));const ds=[...days.children];
    cta.addEventListener('pointermove',e=>{const r=cta.getBoundingClientRect();const n=Math.round((e.clientX-r.left)/r.width*30);ds.forEach((d,i)=>d.classList.toggle('lit',i<n))});
    new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)ds.forEach((d,i)=>setTimeout(()=>d.classList.add('lit'),i*35))}),{threshold:.5}).observe(days);}
});

/* etapas: linha de progresso conforme o scroll */
$$('.steps').forEach(st=>{const bar=$('.bar',st),sts=$$('.step',st);if(!bar)return;
  const f=()=>{const r=st.getBoundingClientRect(),vh=innerHeight;const k=Math.min(Math.max((vh*.8-r.top)/(vh*.6),0),1);bar.style.width=k*100+'%';sts.forEach((s,i)=>s.classList.toggle('on',k>=i/(sts.length-1)-.001&&k>0))};
  addEventListener('scroll',f,{passive:true});f();});

/* imagem que inclina com o mouse */
$$('.tilt-in').forEach(tl=>{if(!fine)return;tl.parentElement.addEventListener('pointermove',e=>{const r=tl.getBoundingClientRect();const x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;tl.style.transform=`rotateY(${x*14}deg) rotateX(${-y*14}deg)`});tl.parentElement.addEventListener('pointerleave',()=>tl.style.transform='')});

/* lista de treinamentos: imagem flutuante segue o cursor */
const pv=$('#preview');
if(pv){const pimg=$('img',pv);let px=0,py=0,cx=0,cy=0;
  $$('.trow').forEach(r=>{r.addEventListener('pointerenter',()=>{pimg.src=r.dataset.img;pv.classList.add('show')});r.addEventListener('pointerleave',()=>pv.classList.remove('show'))});
  addEventListener('pointermove',e=>{px=e.clientX+170;py=e.clientY});
  (function mv(){cx+=(px-cx)*.14;cy+=(py-cy)*.14;pv.style.left=cx+'px';pv.style.top=cy+'px';requestAnimationFrame(mv)})();}

/* CTA final: brilho gira na direção do mouse */
$$('.final').forEach(fin=>{const ring=$('.ring',fin);if(!ring)return;fin.addEventListener('pointermove',e=>{const r=fin.getBoundingClientRect();const a=Math.atan2(e.clientY-r.top-r.height/2,e.clientX-r.left-r.width/2)*180/Math.PI+30;ring.style.setProperty('--ang',a+'deg')})});

/* catálogo de cursos: filtro por modalidade + busca */
const grid=$('#courses');
if(grid){const items=$$('.course',grid),fb=$$('.filters button'),q=$('#q'),empty=$('#empty');let cat='todos';
  const run=()=>{const t=(q?.value||'').trim().toLowerCase();let n=0;
    items.forEach(c=>{const ok=(cat==='todos'||c.dataset.cat.includes(cat))&&(!t||c.textContent.toLowerCase().includes(t));c.classList.toggle('hide',!ok);if(ok)n++});
    if(empty)empty.style.display=n?'none':'block'};
  fb.forEach(b=>b.onclick=()=>{fb.forEach(x=>x.classList.remove('on'));b.classList.add('on');cat=b.dataset.f;run()});
  q&&q.addEventListener('input',run);}

/* artigo: barra de leitura + sumário ativo */
const art=$('.article'),prog=$('.progress');
if(art&&prog){const tocs=$$('.toc a'),hs=tocs.map(a=>$(a.getAttribute('href')));
  addEventListener('scroll',()=>{const r=art.getBoundingClientRect();const k=Math.min(Math.max(-r.top/(r.height-innerHeight),0),1);prog.style.width=k*100+'%';
    let i=-1;hs.forEach((h,j)=>{if(h&&h.getBoundingClientRect().top<160)i=j});tocs.forEach((a,j)=>a.classList.toggle('on',j===i))},{passive:true});}

/* FAQ: aba ativa conforme o scroll */
const ft=$$('.ftabs a');
if(ft.length){const gs=ft.map(a=>$(a.getAttribute('href')));
  addEventListener('scroll',()=>{let i=0;gs.forEach((g,j)=>{if(g&&g.getBoundingClientRect().top<200)i=j});ft.forEach((a,j)=>a.classList.toggle('on',j===i))},{passive:true});}

/* formulário de contato: monta a mensagem e abre o WhatsApp */
const cf=$('#cform');
if(cf){const pre=new URLSearchParams(location.search).get('assunto');
  if(pre){const r=cf.querySelector(`input[name="assunto"][value="${pre}"]`);if(r)r.checked=true;}
  cf.addEventListener('submit',e=>{e.preventDefault();const d=new FormData(cf);
    const msg=`Olá! Vim pelo site do Instituto Ackler.\n\nNome: ${d.get('nome')}\nEmpresa: ${d.get('empresa')||'-'}\nE-mail: ${d.get('email')}\nTelefone: ${d.get('tel')||'-'}\nInteresse: ${d.get('assunto')||'-'}\n\n${d.get('msg')||''}`;
    window.open('https://wa.me/5541995760079?text='+encodeURIComponent(msg),'_blank');
    $('.ok',cf).style.display='block';});}

/* newsletter (placeholder até integrar com a ferramenta de e-mail) */
$$('.news form').forEach(f=>f.addEventListener('submit',e=>{e.preventDefault();f.innerHTML='<p style="color:var(--gold);font-weight:700">Pronto! Você vai receber os próximos conteúdos por e-mail.</p>'}));

/* ano no rodapé */
$$('[data-year]').forEach(y=>y.textContent=new Date().getFullYear());
})();

// One WebGL context renders all sculptures. Content and local fallbacks remain HTML.
const stage = document.querySelector('#core-stage');
const traceButton = document.querySelector('#trace');
const traceStatus = document.querySelector('#trace-status');
const reduced = matchMedia('(prefers-reduced-motion: reduce)');
let traceUntil = 0, traceTimer;
function trace() {
  traceUntil = performance.now() + 2600;
  if (!reduced.matches) stage.classList.add('tracing');
  traceStatus.textContent = 'Tracing a conceptual signal from data, through learning, to prediction.';
  clearTimeout(traceTimer);
  traceTimer = setTimeout(() => stage.classList.remove('tracing'), 2600);
}
traceButton.addEventListener('pointerenter', trace);
traceButton.addEventListener('focus', trace);
traceButton.addEventListener('click', trace);

async function createGallery() {
  let THREE;
  try { THREE = await import('./vendor/three.module.js'); } catch { return; }
  const canvas = document.createElement('canvas');
  canvas.className = 'webgl-gallery'; canvas.setAttribute('aria-hidden', 'true');
  let renderer;
  try { renderer = new THREE.WebGLRenderer({canvas, alpha:true, antialias:true, powerPreference:'low-power'}); } catch { return; }
  document.body.append(canvas);
  renderer.autoClear = false;
  renderer.setClearColor(0x030507, 0);
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.25;
  const mobile = matchMedia('(max-width: 800px)');
  const geometries = new Set(), materials = new Set();
  const trackGeometry = geometry => { geometries.add(geometry); return geometry; };
  const material = options => { const m = new THREE.MeshPhysicalMaterial(options); materials.add(m); return m; };
  const titanium = material({color:0x526a7b,metalness:.95,roughness:.22,clearcoat:.6});
  const dark = material({color:0x07111e,metalness:.86,roughness:.29,clearcoat:1});
  const blue = material({color:0x0754bd,metalness:.75,roughness:.2,clearcoat:1});
  const glass = material({color:0x1ac4e8,metalness:.35,roughness:.13,transparent:true,opacity:.58,side:THREE.DoubleSide,clearcoat:1,depthWrite:false});
  const cyan = material({color:0x00d9ff,emissive:0x00bad9,emissiveIntensity:1.1,metalness:.35,roughness:.2});
  const white = material({color:0xc1e6f3,metalness:.7,roughness:.28});
  function mesh(geometry, mat, parent, position = [0,0,0]) {
    const result = new THREE.Mesh(trackGeometry(geometry), mat);
    result.position.set(...position); if(parent) parent.add(result); return result;
  }
  function box(parent, size, position, mat=dark) { return mesh(new THREE.BoxGeometry(...size),mat,parent,position); }
  function tube(parent, points, radius=.018, mat=cyan) {
    const curve = new THREE.CatmullRomCurve3(points);
    return mesh(new THREE.TubeGeometry(curve,mobile.matches?40:80,radius,6,false),mat,parent);
  }
  function arc(parent, radius, thickness, start, length, mat=titanium) {
    return mesh(new THREE.TorusGeometry(radius,thickness,8,mobile.matches?64:112,length),mat,parent);
  }
  function band(parent, radius, width, length, mat, rotation, z) {
    const shape = new THREE.Shape();
    shape.absarc(0,0,radius,-length/2,length/2,false);
    shape.absarc(0,0,radius-width,length/2,-length/2,true);
    shape.closePath();
    const geometry = new THREE.ExtrudeGeometry(shape,{depth:.055,bevelEnabled:true,bevelSegments:2,steps:1,bevelSize:.015,bevelThickness:.014,curveSegments:mobile.matches?32:64});
    const result=mesh(geometry,mat,parent,[0,0,z]); result.rotation.set(...rotation); return result;
  }
  // Procedural studio reflection: soft rectangular lights, no model or texture download.
  const studio=document.createElement('canvas');studio.width=1024;studio.height=512;
  const ctx=studio.getContext('2d');ctx.fillStyle='#081320';ctx.fillRect(0,0,1024,512);
  for (const [x,width,color] of [[100,170,'#d1e5f0'],[440,70,'#1687d0'],[690,230,'#f4fbff']]) {
    const gradient=ctx.createLinearGradient(x,0,x+width,0);gradient.addColorStop(0,'#081320');gradient.addColorStop(.4,color);gradient.addColorStop(.6,color);gradient.addColorStop(1,'#081320');ctx.fillStyle=gradient;ctx.fillRect(x,80,width,350);
  }
  const envTexture=new THREE.CanvasTexture(studio);envTexture.mapping=THREE.EquirectangularReflectionMapping;
  const pmrem=new THREE.PMREMGenerator(renderer);const environment=pmrem.fromEquirectangular(envTexture);envTexture.dispose();pmrem.dispose();
  const views=[];
  function view(element, hero=false) {
    const scene=new THREE.Scene();scene.environment=environment.texture;
    const camera=new THREE.PerspectiveCamera(hero?34:36,1,.1,40);camera.position.set(0,0,hero?10.6:6.7);
    scene.add(new THREE.AmbientLight(0x90b9d0,1.3));
    const key=new THREE.DirectionalLight(0xe3f6ff,4);key.position.set(-3,5,5);scene.add(key);
    const edge=new THREE.DirectionalLight(0x147cff,5);edge.position.set(4,-1,-3);scene.add(edge);
    const group=new THREE.Group();scene.add(group);
    const data={element,scene,camera,group,hero,visible:false,x:0,y:0,boost:0,updates:[]};
    element.addEventListener('pointermove',event=>{
      if(reduced.matches||event.pointerType==='touch')return;
      const r=element.getBoundingClientRect();data.x=Math.max(-1,Math.min(1,(event.clientX-r.left)/r.width*2-1));data.y=Math.max(-1,Math.min(1,(event.clientY-r.top)/r.height*2-1));
    });
    element.addEventListener('pointerleave',()=>{data.x=0;data.y=0;});
    views.push(data);return data;
  }
  const hero=view(stage,true), assembly=hero.group;
  assembly.rotation.set(.2,-.5,-.18);
  const heart=mesh(new THREE.IcosahedronGeometry(.62,0),glass,assembly,[.15,0,.2]);
  const heartInner=mesh(new THREE.OctahedronGeometry(.3,0),cyan,assembly,[.15,0,.2]);
  const heartFrame=mesh(new THREE.IcosahedronGeometry(.65,0),titanium,assembly,[.15,0,.2]);
  const frameEdges=new THREE.EdgesGeometry(heartFrame.geometry);geometries.add(frameEdges);
  const edgeMaterial=new THREE.LineBasicMaterial({color:0x87e8ff,transparent:true,opacity:.6});materials.add(edgeMaterial);
  assembly.remove(heartFrame);const coreEdges=new THREE.LineSegments(frameEdges,edgeMaterial);coreEdges.position.copy(heart.position);assembly.add(coreEdges);
  const bands=[],layers=[];
  for(let l=0;l<4;l++) {
    const rotation=[.48+l*.14,-.38+l*.18,-.52+l*.17];
    const radius=1.13+l*.33;
    const ribbon=band(assembly,radius,.12+l*.025,Math.PI*1.28,l%2?titanium:dark,rotation,-.42+l*.18);
    bands.push(ribbon);
    const edgeArc=arc(ribbon,radius-.035,.012,0,Math.PI*1.28,l%2?blue:cyan);edgeArc.rotation.z=-Math.PI*.64;edgeArc.position.z=.075;
    const points=[];
    for(let i=0;i<7;i++) {
      const angle=-Math.PI*.64+i/6*Math.PI*1.28;
      const local=new THREE.Vector3(Math.cos(angle)*radius,Math.sin(angle)*radius,.095);
      const node=mesh(new THREE.SphereGeometry(.043,10,8),i%3===0?white:cyan,ribbon,[local.x,local.y,local.z]);
      ribbon.updateMatrix();points.push(local.clone().applyMatrix4(ribbon.matrix));
    }
    layers.push(points);
  }
  for(let l=0;l<3;l++)for(let i=1;i<6;i+=2)tube(assembly,[layers[l][i],layers[l+1][i]],.008,blue);
  const orbitA=arc(assembly,2.55,.027,0,Math.PI*1.52,titanium);orbitA.rotation.set(1.08,.4,-.4);
  const orbitB=arc(assembly,2.65,.014,0,Math.PI*1.23,blue);orbitB.rotation.set(.35,.45,-.9);
  const pods=new THREE.Group();assembly.add(pods);
  for(let i=0;i<3;i++) {
    const pod=box(pods,[.14,.14,.14],[2.35+(i%2)*.16,-.6+i*.3,.45],titanium);pod.rotation.set(.4,.4,.4);
    mesh(new THREE.SphereGeometry(.045,8,8),cyan,pods,[pod.position.x,pod.position.y,pod.position.z+.09]);
    tube(assembly,[heart.position.clone(),new THREE.Vector3(1.35,-.15+i*.13,.3),pod.position.clone()],.009,blue);
  }
  const paths=[];
  for(let i=0;i<3;i++) {
    const path=new THREE.CatmullRomCurve3([new THREE.Vector3(-2.7,.6-i*.38,.5),layers[3][2+i],layers[1][2+i],heart.position.clone(),new THREE.Vector3(2.4,-.6+i*.3,.5)]);paths.push(path);
    for(let j=0;j<3;j++) {
      const particle=mesh(new THREE.SphereGeometry(.025,8,6),cyan,assembly);
      hero.updates.push((time,dt,now)=>{const progress=(time*.11+j/3+i*.09)%1;particle.position.copy(path.getPointAt(progress));particle.scale.setScalar(now<traceUntil?2:1);});
    }
  }
  hero.updates.push((time,dt,now)=>{
    heart.rotation.y=time*.18;heart.rotation.z=Math.sin(time*.3)*.1;heartInner.rotation.x=time*.4;coreEdges.rotation.copy(heart.rotation);
    orbitA.rotation.z=-.4+Math.sin(time*.16)*.2;orbitB.rotation.z=-.9+Math.sin(time*.2)*.18;
    bands.forEach((ribbon,i)=>{ribbon.position.z=-.42+i*.18+Math.sin(time*.6+i*.8)*.035;});
    cyan.emissiveIntensity=now<traceUntil?2:1.1;
  });
  for(const element of document.querySelectorAll('[data-sculpture]')) {
    const v=view(element),g=v.group;g.rotation.set(.35,-.4,-.1);
    g.scale.setScalar(element.dataset.sculpture==='message'?1.12:1.45);
    switch(element.dataset.sculpture) {
      case 'pipeline': {
        const tiles=[];
        for(let i=0;i<5;i++) { const tile=box(g,[.65,.1,.8],[-1.1+i*.48,-.35+i*.15,0],i===4?blue:titanium);tile.rotation.z=-.15;box(tile,[.35,.025,.035],[0,.065,.1],cyan);tiles.push(tile); }
        tube(g,[new THREE.Vector3(-1.4,-.5,.4),new THREE.Vector3(0,.3,.4),new THREE.Vector3(1.35,.5,.2)],.022,blue);
        const prediction=mesh(new THREE.OctahedronGeometry(.23),cyan,g,[1.35,.5,.2]);
        v.updates.push(time=>{tiles.forEach((tile,i)=>tile.position.y=-.35+i*.15+Math.sin(time*1.3-i*.6)*.07);prediction.rotation.y=time*.5;});break;
      }
      case 'duality': {
        const one=mesh(new THREE.TorusGeometry(.75,.13,12,64),titanium,g,[-.35,0,0]);one.rotation.x=.6;
        const two=mesh(new THREE.TorusGeometry(.75,.105,12,64),blue,g,[.4,0,.25]);two.rotation.y=1.1;
        const accent=arc(one,.75,.02,0,Math.PI*1.1,cyan);accent.position.z=.135;
        v.updates.push(time=>{one.rotation.y=Math.sin(time*.5)*.18;two.rotation.z=time*.15;});break;
      }
      case 'stack': {
        const chips=[];
        for(let i=0;i<4;i++) {const chip=box(g,[1.35,.14,1.1],[0,(i-1.5)*.36,0],i===2?blue:titanium);box(chip,[.8,.025,.7],[0,.087,0],dark);for(let j=0;j<4;j++)box(chip,[.055,.05,.13],[-.48+j*.32,.04,.61],cyan);chips.push(chip);}
        v.updates.push(time=>chips.forEach((chip,i)=>{chip.rotation.y=Math.sin(time*.55+i*.5)*.12;chip.position.y=(i-1.5)*.36+Math.sin(time+i)*.04;}));break;
      }
      case 'path': {
        const points=[];
        for(let i=0;i<5;i++){const x=-1.05+i*.52,y=-.8+i*.4;const step=box(g,[.42,.08,.5],[x,y,0],i===4?blue:titanium);points.push(new THREE.Vector3(x,y+.12,.15));}
        tube(g,points,.018,cyan);
        const beacon=mesh(new THREE.SphereGeometry(.07,10,8),cyan,g);const curve=new THREE.CatmullRomCurve3(points);
        v.updates.push(time=>beacon.position.copy(curve.getPointAt((time*.16)%1)));break;
      }
      case 'book': {
        const spine=box(g,[.09,.14,1.2],[0,-.1,0],blue);
        const pages=[];
        for(const side of [-1,1])for(let i=0;i<3;i++){const page=box(g,[.8,.035,1.1],[side*.4,i*.09,0],i===0?titanium:white);page.rotation.z=side*(.12+i*.09);pages.push({page,side,i});box(page,[.55,.008,.02],[0,.026,-.25],blue);box(page,[.45,.008,.02],[0,.026,-.1],blue);}
        v.updates.push(time=>pages.forEach(({page,side,i})=>{page.rotation.z=side*(.12+i*.09+Math.sin(time*.6+i)*.025); }));g.rotation.x=.65;break;
      }
      case 'message': {
        const envelope=box(g,[1.65,1.05,.12],[0,0,0],titanium);
        const triangle=new THREE.Shape();triangle.moveTo(-.8,.48);triangle.lineTo(.8,.48);triangle.lineTo(0,-.1);triangle.closePath();
        mesh(new THREE.ExtrudeGeometry(triangle,{depth:.035,bevelEnabled:true,bevelSize:.015,bevelThickness:.015,bevelSegments:1}),blue,g,[0,0,.09]);
        tube(g,[new THREE.Vector3(-.8,-.5,.1),new THREE.Vector3(0,.05,.17),new THREE.Vector3(.8,-.5,.1)],.014,cyan);
        const ring=arc(g,1.5,.016,0,Math.PI*1.65,cyan);ring.rotation.set(.7,.6,-.4);
        v.updates.push(time=>{ring.rotation.z=-.4+time*.12;envelope.rotation.z=Math.sin(time*.7)*.015;});break;
      }
    }
  }
  let frame=0,last=0,time=0,disposed=false;
  const observer=new IntersectionObserver(entries=>{
    for(const entry of entries){const v=views.find(item=>item.element===entry.target);v.visible=entry.isIntersecting;}
    schedule();
  },{rootMargin:'100px'});
  views.forEach(v=>observer.observe(v.element));
  function draw(now) {
    frame=0;if(disposed||document.hidden)return;
    const dt=last?Math.min((now-last)/1000,.05):0;last=now;
    if(!reduced.matches)time+=dt;
    renderer.setScissorTest(false);renderer.clear();renderer.setScissorTest(true);
    let count=0;
    for(const v of views) {
      const r=v.element.getBoundingClientRect();
      if(!v.visible||r.bottom<=0||r.top>=innerHeight||r.width<1||r.height<1)continue;
      count++;
      const visibleTop=Math.max(0,r.top),visibleBottom=Math.min(innerHeight,r.bottom);
      renderer.setViewport(r.left,innerHeight-r.bottom,r.width,r.height);
      renderer.setScissor(Math.max(0,r.left),innerHeight-visibleBottom,Math.min(r.width,innerWidth-Math.max(0,r.left)),visibleBottom-visibleTop);
      v.camera.aspect=r.width/r.height;v.camera.position.z=v.hero?(v.camera.aspect<1.1?12.1:10.6):6.7;v.camera.updateProjectionMatrix();
      if(!reduced.matches){
        const blend=1-Math.exp(-dt*4);
        v.group.rotation.x+=((v.hero?.2:.35)-v.y*.16+Math.sin(time*.3)*.05-v.group.rotation.x)*blend;
        v.group.rotation.y+=((v.hero?-.5:-.4)+v.x*.36+Math.sin(time*.24)*.16-v.group.rotation.y)*blend;
        v.group.position.y=Math.sin(time*.7+(v.hero?0:views.indexOf(v)))*.08;
        v.updates.forEach(update=>update(time,dt,now));
      }
      renderer.clearDepth();renderer.render(v.scene,v.camera);v.element.classList.add('ready');
    }
    renderer.setScissorTest(false);
    if(count&&!reduced.matches)frame=requestAnimationFrame(draw);
  }
  function schedule(){if(!disposed&&!document.hidden&&!frame)frame=requestAnimationFrame(draw);}
  function resize(){renderer.setPixelRatio(Math.min(devicePixelRatio,mobile.matches?1.15:1.5));renderer.setSize(innerWidth,innerHeight,false);schedule();}
  const resizeObserver=new ResizeObserver(schedule);views.forEach(v=>resizeObserver.observe(v.element));
  function visibility(){cancelAnimationFrame(frame);frame=0;last=0;schedule();}
  function motionChange(){cancelAnimationFrame(frame);frame=0;last=0;schedule();}
  addEventListener('resize',resize,{passive:true});addEventListener('scroll',schedule,{passive:true});
  document.addEventListener('visibilitychange',visibility);reduced.addEventListener('change',motionChange);
  function dispose(){
    if(disposed)return;disposed=true;cancelAnimationFrame(frame);observer.disconnect();resizeObserver.disconnect();
    removeEventListener('resize',resize);removeEventListener('scroll',schedule);document.removeEventListener('visibilitychange',visibility);reduced.removeEventListener('change',motionChange);
    views.forEach(v=>v.element.classList.remove('ready'));geometries.forEach(g=>g.dispose());materials.forEach(m=>m.dispose());environment.dispose();renderer.dispose();canvas.remove();
  }
  canvas.addEventListener('webglcontextlost',event=>{event.preventDefault();dispose();},{once:true});
  addEventListener('pagehide',event=>{if(event.persisted){cancelAnimationFrame(frame);frame=0;}else dispose();});
  addEventListener('pageshow',()=>{last=0;schedule();});
  // Position the static particles as well, before the first reduced-motion frame.
  views.forEach(v=>v.updates.forEach(update=>update(0,0,0)));
  resize();schedule();
}
createGallery().catch(error=>{console.warn('3D gallery unavailable; using local artwork.',error);document.querySelectorAll('.ready').forEach(element=>element.classList.remove('ready'));});

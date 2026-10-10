const menu = document.querySelector('.menu-toggle');
const links = document.querySelector('#nav-links');
menu.hidden = false;
document.body.classList.add('menu-enhanced');
function closeMenu() { links.classList.remove('open'); menu.setAttribute('aria-expanded', 'false'); }
menu.addEventListener('click', () => { const open = menu.getAttribute('aria-expanded') !== 'true'; links.classList.toggle('open', open); menu.setAttribute('aria-expanded', String(open)); });
links.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
document.addEventListener('keydown', event => { if (event.key === 'Escape' && links.classList.contains('open')) { closeMenu(); menu.focus(); } });
document.addEventListener('click', event => { if (!event.target.closest('nav')) closeMenu(); });
const desktop = matchMedia('(min-width: 801px)');
desktop.addEventListener('change', closeMenu);
const anchors = [...links.querySelectorAll('a')];
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) if (entry.isIntersecting) {
      for (const link of anchors) { const active = link.hash === `#${entry.target.id}`; link.classList.toggle('active', active); if (active) link.setAttribute('aria-current', 'location'); else link.removeAttribute('aria-current'); }
    }
  }, { rootMargin: '-15% 0px -60% 0px', threshold: 0 });
  for (const anchor of anchors) observer.observe(document.querySelector(anchor.hash));
}

// Section-specific perspective entrances and pointer depth; never hide content.
const motionPreference = matchMedia('(prefers-reduced-motion: reduce)');
const finePointer = matchMedia('(hover: hover) and (pointer: fine)');
const animations = new Set();
const progressBar = document.createElement('div');
progressBar.className = 'scroll-progress';
progressBar.setAttribute('aria-hidden', 'true');
document.body.append(progressBar);
const sections = [...document.querySelectorAll('main section')];
let scrollFrame = 0;
function updateProgress() {
  scrollFrame = 0;
  const total = document.documentElement.scrollHeight - innerHeight;
  document.documentElement.style.setProperty('--page-progress', total > 0 ? scrollY / total : 0);
  for (const section of sections) {
    const bounds = section.getBoundingClientRect();
    if (bounds.bottom >= 0 && bounds.top <= innerHeight) section.style.setProperty('--section-progress', Math.max(0, Math.min(1, (innerHeight - bounds.top) / (bounds.height + innerHeight))));
  }
}
function onScroll() { if (!scrollFrame) scrollFrame = requestAnimationFrame(updateProgress); }
addEventListener('scroll', onScroll, { passive: true });
addEventListener('resize', onScroll, { passive: true });
updateProgress();
const entrances = new IntersectionObserver(entries => {
  for (const entry of entries) {
    entry.target.classList.toggle('is-inview', entry.isIntersecting);
    if (!entry.isIntersecting || entry.target.dataset.animated || motionPreference.matches) continue;
    entry.target.dataset.animated = 'true';
    const children = entry.target.querySelectorAll('h2, .project-copy, .workflow, .security-project, .large-copy, .focus, .skill-row, .timeline article, .degree, .certifications article, .email');
    children.forEach((element, index) => {
      // Animate only elements already near the viewport; remaining rows reveal individually.
      if (element.getBoundingClientRect().top < innerHeight + 30) entrance(element, index % 5);
    });
  }
}, { threshold: .05 });
function entrance(element, index = 0) {
  if (element.dataset.revealed || motionPreference.matches) return;
  element.dataset.revealed = 'true';
  const sideways = element.matches('.skill-row, .certifications article');
  const from = sideways ? 'perspective(1000px) translate3d(-22px,12px,-30px) rotateY(-7deg)' : 'perspective(1000px) translate3d(0,35px,-55px) rotateX(7deg)';
  const animation = element.animate([{ opacity: .35, transform: from }, { opacity: 1, transform: 'perspective(1000px) translate3d(0,0,0) rotateX(0) rotateY(0)' }], { duration: 850, delay: index * 65, easing: 'cubic-bezier(.2,.8,.2,1)' });
  animations.add(animation);
  animation.onfinish = () => animations.delete(animation);
}
sections.forEach(section => entrances.observe(section));
const rowObserver = new IntersectionObserver(entries => {
  for (const entry of entries) if (entry.isIntersecting) { entrance(entry.target); rowObserver.unobserve(entry.target); }
}, { threshold: .12 });
document.querySelectorAll('.skill-row, .timeline article, .certifications article, .workflow, .security-project, .focus').forEach(row => rowObserver.observe(row));
for (const surface of document.querySelectorAll('.featured, .security-art, .degree')) {
  surface.classList.add('tilt-surface');
  surface.addEventListener('pointermove', event => {
    if (motionPreference.matches || !finePointer.matches) return;
    const bounds = surface.getBoundingClientRect();
    const x = Math.max(0, Math.min(1, (event.clientX - bounds.left) / bounds.width));
    const y = Math.max(0, Math.min(1, (event.clientY - bounds.top) / bounds.height));
    surface.style.setProperty('--tilt-x', `${(0.5 - y) * 6}deg`);
    surface.style.setProperty('--tilt-y', `${(x - 0.5) * 8}deg`);
    surface.style.setProperty('--shine-x', `${x * 100}%`);
    surface.style.setProperty('--shine-y', `${y * 100}%`);
  });
  surface.addEventListener('pointerleave', () => { surface.style.setProperty('--tilt-x', '0deg'); surface.style.setProperty('--tilt-y', '0deg'); });
}
function visibilityMotion() {
  document.body.classList.toggle('tab-hidden', document.hidden);
  for (const animation of animations) document.hidden ? animation.pause() : animation.play();
}
document.addEventListener('visibilitychange', visibilityMotion);
motionPreference.addEventListener('change', () => { if (motionPreference.matches) { for (const animation of animations) animation.cancel(); animations.clear(); } });

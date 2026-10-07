/* phones + tablets only (the desktop rail already keeps the ask in view).
   one floating "let's talk", bottom right, on every page: it rises once you're past the first screen,
   and on the homepage steps aside while the "work together" card itself is on screen, so the ask never shows twice. */
(() => {
  const small = matchMedia('(max-width: 1100px)');
  const fab = document.querySelector('.fab');
  if (!fab) return;

  const card = document.querySelector('.rail .cta');
  let cardInView = false;
  if (card && 'IntersectionObserver' in window) {
    new IntersectionObserver(([e]) => { cardInView = e.isIntersecting; update(); }).observe(card);
  }

  function update() {
    const show = small.matches && scrollY > innerHeight * 0.6 && !cardInView;
    fab.classList.toggle('show', show);
    fab.inert = !show;   // hidden means hidden for keyboards and screen readers too
  }

  addEventListener('scroll', update, { passive: true });
  small.addEventListener('change', update);
  update();
})();

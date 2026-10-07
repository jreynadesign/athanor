/* phones + tablets only (the desktop rail already keeps the ask in view).
   homepage: the floating "let's talk" button rises once you're past the first screen,
   and steps aside while the "work together" card itself is on screen, so the ask never shows twice.
   project pages: the header (← / let's talk) sticks to the top, tucks away while you scroll
   down and slides back the moment you scroll up. */
(() => {
  const small = matchMedia('(max-width: 1100px)');

  const fab = document.querySelector('.fab');
  const card = document.querySelector('.rail .cta');
  let cardInView = false;
  if (fab && card && 'IntersectionObserver' in window) {
    new IntersectionObserver(([e]) => { cardInView = e.isIntersecting; update(); }).observe(card);
  }

  const bar = document.querySelector('.project-rail .bar');
  let lastY = scrollY;

  function update() {
    const y = scrollY;
    if (fab) {
      const show = small.matches && y > innerHeight * 0.6 && !cardInView;
      fab.classList.toggle('show', show);
      fab.inert = !show;   // hidden means hidden for keyboards and screen readers too
    }
    if (bar) {
      const dy = y - lastY;
      if (!small.matches || y < 80 || dy < -4) bar.classList.remove('tucked');
      else if (dy > 4) bar.classList.add('tucked');
      bar.classList.toggle('lifted', small.matches && y > 8);
    }
    lastY = y;
  }

  addEventListener('scroll', update, { passive: true });
  small.addEventListener('change', update);
  update();
})();

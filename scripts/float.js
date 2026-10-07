/* phones + tablets only (the desktop rail already keeps the ask in view).
   one floating "let's talk", bottom right, on every page: it comes in as soon as you start scrolling,
   and on the homepage steps aside a little before the "work together" card comes on screen, so the ask never shows twice. */
(() => {
  const small = matchMedia('(max-width: 1100px)');
  const fab = document.querySelector('.fab');
  if (!fab) return;

  const card = document.querySelector('.rail .cta');
  let cardInView = false;
  if (card && 'IntersectionObserver' in window) {
    // the bottom margin widens the watch zone: the button leaves while the card is still a third of a screen away,
    // so it's gone before the card arrives rather than as it does
    new IntersectionObserver(([e]) => { cardInView = e.isIntersecting; update(); }, { rootMargin: '0px 0px 33% 0px' }).observe(card);
  }

  // out as soon as you start scrolling, back in only at the very top. two nearby thresholds (120 / 80)
  // so it can't flicker while you hover around the line
  let out = false;
  function update() {
    if (scrollY > 120) out = true;
    else if (scrollY < 80) out = false;
    const show = small.matches && out && !cardInView;
    fab.classList.toggle('show', show);
    fab.inert = !show;   // hidden means hidden for keyboards and screen readers too
  }

  addEventListener('scroll', update, { passive: true });
  small.addEventListener('change', update);
  update();
})();

/* client logo strip (also worked with): drag to scroll with a mouse, arrow keys
   when focused. trackpads and shift+wheel scroll it natively. */
(() => {
  const strip = document.querySelector('.logo-strip');
  if (!strip) return;
  let down = false, startX = 0, startLeft = 0, moved = false;
  strip.addEventListener('pointerdown', e => {
    if (e.pointerType !== 'mouse') return;
    down = true; moved = false; startX = e.clientX; startLeft = strip.scrollLeft;
    strip.setPointerCapture(e.pointerId);
  });
  strip.addEventListener('pointermove', e => {
    if (!down) return;
    const dx = e.clientX - startX;
    if (Math.abs(dx) > 3) { moved = true; strip.classList.add('dragging'); }
    strip.scrollLeft = startLeft - dx;
  });
  const end = () => { down = false; strip.classList.remove('dragging'); };
  strip.addEventListener('pointerup', end);
  strip.addEventListener('pointercancel', end);
  strip.addEventListener('click', e => { if (moved) e.preventDefault(); }, true);   // a drag isn't a click
  strip.addEventListener('keydown', e => {
    const step = (strip.querySelector('.logo-tile')?.offsetWidth || 160) + 16;
    if (e.key === 'ArrowRight') { strip.scrollBy({ left: step, behavior: 'smooth' }); e.preventDefault(); }
    if (e.key === 'ArrowLeft') { strip.scrollBy({ left: -step, behavior: 'smooth' }); e.preventDefault(); }
  });
})();

/* smooth (eased) scrolling for the whole site via lenis — it drives the native
   scroll position, so sticky elements, find-in-page and assistive tech still work.
   skipped entirely for prefers-reduced-motion. */
(() => {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches || !window.Lenis) return;
  const lenis = new Lenis({ autoRaf: true, lerp: 0.1, anchors: true });

  // stop the page from drifting behind an open modal
  document.querySelectorAll('dialog').forEach(dlg => {
    new MutationObserver(() => (dlg.open ? lenis.stop() : lenis.start()))
      .observe(dlg, { attributes: true, attributeFilter: ['open'] });
  });
})();

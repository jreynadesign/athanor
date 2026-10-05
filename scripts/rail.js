/* the desktop rail is always exactly the window height. when its text card (about,
   or a project's info) is longer than the space it gets, that card scrolls on its own — this adds a
   fade at its bottom edge while there's more to read, and drops it at the end. */
(() => {
  const about = document.querySelector('.rail .scrolls');
  if (!about) return;
  const update = () => {
    const more = about.scrollHeight - about.clientHeight - about.scrollTop > 2;
    about.classList.toggle('has-more', more);
  };
  about.addEventListener('scroll', update, { passive: true });
  addEventListener('resize', update);
  document.fonts?.ready.then(update);
  update();
})();

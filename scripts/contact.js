/* contact modals — "start a project" and "newsletter".
   built on <dialog>, so focus handling, esc-to-close and the backdrop come free.
   the site is static (no server): the project form composes an email to
   hi@justinreyna.design with everything filled in. swap the submit handler for
   a form service (formspree, basin…) when one is chosen. without js, the
   buttons fall back to plain links (mailto / #newsletter). */
(() => {
  const TO = 'hi@justinreyna.design';
  const track = (n, p) => window.track && window.track(n, { page_path: location.pathname, ...p });

  document.querySelectorAll('[data-open]').forEach(btn => {
    const dlg = document.getElementById(btn.dataset.open);
    if (!dlg || !dlg.showModal) return;
    btn.addEventListener('click', e => {
      e.preventDefault();
      dlg.dataset.placement = btn.dataset.trackPlacement || '';
      dlg.dataset.sent = dlg.dataset.started = '';
      dlg.showModal();
      // with a mouse and keyboard, jump straight into the first field. on touch screens don't:
      // focusing a field throws up the keyboard before the sheet has even landed
      // touch: the sheet itself takes focus, so no field (keyboard) and no button (focus ring) lights up
      if (matchMedia('(pointer: fine)').matches) dlg.querySelector('input, textarea, select')?.focus();
      else dlg.focus();
    });
  });

  document.querySelectorAll('dialog').forEach(dlg => {
    dlg.querySelectorAll('[data-close]').forEach(b => b.addEventListener('click', () => dlg.close()));
    // a click on the backdrop lands on the dialog element itself
    dlg.addEventListener('click', e => { if (e.target === dlg) dlg.close(); });
    // funnel: opened (cta_click) → form_start → generate_lead, or contact_close if they leave first
    dlg.addEventListener('input', () => {
      if (!dlg.dataset.started) { dlg.dataset.started = '1'; track('form_start', { form: dlg.id, placement: dlg.dataset.placement }); }
    });
    dlg.addEventListener('close', () => {
      if (!dlg.dataset.sent) track('contact_close', { form: dlg.id, placement: dlg.dataset.placement, started: dlg.dataset.started ? 'yes' : 'no' });
    });
  });

  const project = document.getElementById('project-form');
  project?.addEventListener('submit', e => {
    e.preventDefault();
    const f = new FormData(project);
    const needs = f.getAll('needs');
    const name = f.get('name').trim();
    const company = f.get('company').trim();
    const lines = [`Name: ${name}`, `Email: ${f.get('email').trim()}`];
    if (company) lines.push(`Company: ${company}`);
    if (needs.length) lines.push(`Looking for: ${needs.join(', ')}`);
    if (f.get('timeline')) lines.push(`Timeline: ${f.get('timeline')}`);   // optional: nothing is pre-picked
    lines.push('', f.get('message').trim());
    // counts what and when only — never the name, email or message
    const dlg = project.closest('dialog');
    dlg.dataset.sent = '1';
    track('generate_lead', { form: 'project-dialog', placement: dlg.dataset.placement, needs: needs.join(', ') || 'none', timeline: f.get('timeline') || 'none' });
    const body = lines.join('\n');
    location.href = `mailto:${TO}?subject=${encodeURIComponent(`New project — ${name}`)}&body=${encodeURIComponent(body)}`;
    project.querySelector('.sent').hidden = false;
  });

  // newsletter has no provider yet — say so honestly instead of pretending to subscribe
  const news = document.getElementById('newsletter-form');
  news?.addEventListener('submit', e => {
    e.preventDefault();
    news.querySelector('.sent').hidden = false;
  });
})();

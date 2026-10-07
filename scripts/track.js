/* analytics events (GA4, G-5H5JDX42QB). page views come free from the tag in
   <head>; this adds the moves between them. everything goes through
   window.track, which no-ops when the tag is blocked, so analytics can never
   break the site. no personal data is ever sent: form contents stay in the
   email, only the chips (what / when) are counted.

   events
     cta_click        a "let's chat" button      cta, placement
     select_content   a project row / next card  content_type, item_id, placement
     back_click       the ← on a project page    from
     outbound_click   any link off the site      link_url, link_domain, label
     email_click      a mailto link              placement
     section_view     a homepage section seen    section            (once per page)
     scroll_depth     25 / 50 / 75 / 100 %       percent            (once each)
     logo_strip_use   the logo strip scrolled    —                  (once per page)
     form_start / generate_lead / contact_close come from contact.js */
(() => {
  const track = window.track || (() => {});
  const page = location.pathname;

  // clicks: anything with data-track="event" sends it, with data-track-* as params
  document.addEventListener('click', e => {
    const a = e.target.closest('a, button');
    if (!a) return;
    if (a.dataset.track) {
      const params = { page_path: page };
      for (const [k, v] of Object.entries(a.dataset))
        if (k.startsWith('track') && k !== 'track') params[k.slice(5).replace(/^./, c => c.toLowerCase())] = v;
      track(a.dataset.track, params);
    }
    const href = a.getAttribute('href') || '';
    if (href.startsWith('mailto:') && !a.dataset.open) track('email_click', { page_path: page, placement: a.dataset.place || 'link' });
    else if (/^https?:/.test(href) && a.host !== location.host)
      track('outbound_click', { page_path: page, link_url: href, link_domain: a.host, label: a.textContent.trim().slice(0, 80) });
  }, { capture: true });

  // homepage sections: which ones people actually reach
  if ('IntersectionObserver' in window) {
    const seen = new Set();
    const io = new IntersectionObserver(entries => entries.forEach(en => {
      const id = en.target.id;
      if (en.isIntersecting && !seen.has(id)) { seen.add(id); track('section_view', { page_path: page, section: id }); io.unobserve(en.target); }
    }), { threshold: 0.4 });
    document.querySelectorAll('.main > .panel[id]').forEach(s => io.observe(s));
  }

  // scroll depth, on every page
  const marks = [25, 50, 75, 100], hit = new Set();
  const depth = () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    const pct = max <= 0 ? 100 : (scrollY / max) * 100;
    for (const m of marks) if (pct >= m - 1 && !hit.has(m)) { hit.add(m); track('scroll_depth', { page_path: page, percent: m }); }
  };
  addEventListener('scroll', depth, { passive: true });

  // the logo strip scrolls sideways; count it once if someone does
  const strip = document.querySelector('.logo-strip');
  strip?.addEventListener('scroll', () => track('logo_strip_use', { page_path: page }), { once: true, passive: true });
})();

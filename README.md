# athanor

Personal site of Justin Reyna — justinreyna.design. Static, served by GitHub Pages from `main`.

- `build.py` writes the homepage, `work/*/`, `404.html`, `experiments/index.html` and `sitemap.xml`.
  Edit copy or data there, then run `python3 build.py`. Commit the output.
- `styles/` tokens + layout, `scripts/` small vanilla js (contact modal, rail, smooth scroll, analytics events).
- `experiments/stone-os/` is the 1-bit Stone OS desktop, hand-written, self-contained.
- `tools/og.html` is the source of `/og.jpg` (the link preview); `tools/og.sh` renders it.
- analytics: GA4 `G-5H5JDX42QB`. event list at the top of `scripts/track.js`.

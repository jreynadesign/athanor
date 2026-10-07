"""writes justinreyna.design: the homepage, the project pages, the 404 and the sitemap.
run `python3 build.py` from the repo root after editing anything below or the copy.
output is plain static html, committed as-is — github pages serves it, no build step there.
stone os lives on, hand-written, at /experiments/stone-os/."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
SITE = "https://justinreyna.design"
import time
import hashlib
# cache-buster for css/js: a hash of their contents, so it only changes when they do
# (and a rebuild with no edits produces identical html)
VER = hashlib.sha1(b"".join(f.read_bytes() for f in sorted((ROOT / "styles").glob("*.css")) + sorted((ROOT / "scripts").glob("*.js")))).hexdigest()[:8]

COLOR = {"web": "web", "web design": "web", "design system": "system", "design systems": "system",
         "product": "product", "product design": "product", "mvp design": "product",
         "brand": "brand", "motion": "motion", "ai workflows": "ai", "coming soon": "soon"}

SHOW = {"mvp design": "MVP design", "ai workflows": "AI workflows"}

def tag(t, sm=False):
    label = SHOW.get(t, t[0].upper() + t[1:])
    return f'<span class="tag{" sm" if sm else ""}" data-c="{COLOR[t]}">{escape(label)}</span>'

DESC = "Justin Reyna is a designer and creative technologist in Austin, Texas, working across human–computer interaction, design systems and product."
GA = "G-5H5JDX42QB"

# 16px pixel "JR", ink on paper
_J = ["..###", "...#.", "...#.", "...#.", "#..#.", "#..#.", ".##.."]
_R = ["####.", "#...#", "#...#", "####.", "#.#..", "#..#.", "#...#"]
_FAV = "".join(f"M{x + ox} {y + 4}h1v1h-1z" for ox, L in ((2, _J), (8, _R)) for y, row in enumerate(L) for x, c in enumerate(row) if c == "#")
FAVICON = ("data:image/svg+xml," + f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' shape-rendering='crispEdges'><rect width='16' height='16' rx='3' fill='%23efeae0'/><path fill='%23141311' d='{_FAV}'/></svg>".replace("<", "%3C").replace(">", "%3E").replace(" ", "%20"))

def head(title, path="/", desc=DESC, index=True):
    url = SITE + path
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
{'' if index else '<meta name="robots" content="noindex">'}
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Justin Reyna">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(title)}">
<meta name="twitter:description" content="{escape(desc)}">
<meta name="twitter:image" content="{SITE}/og.jpg">
<link rel="icon" href="{FAVICON}">
<meta name="theme-color" content="#dfdcd5">
<!-- Google tag (gtag.js) — events are in scripts/track.js and scripts/contact.js -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA}');
  window.track = function (name, params) {{ try {{ gtag('event', name, params || {{}}); }} catch (e) {{}} }};
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Host+Grotesk:wght@500..600&family=Instrument+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles/tokens.css?v={VER}">
<link rel="stylesheet" href="/styles/site.css?v={VER}">
<!-- smooth scroll: lenis, pinned version -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lenis@1.3.26/dist/lenis.css">
<script src="https://cdn.jsdelivr.net/npm/lenis@1.3.26/dist/lenis.min.js" defer></script>
<script src="/scripts/smooth.js?v={VER}" defer></script>
<script src="/scripts/track.js?v={VER}" defer></script>

</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="page">
<nav class="bar" aria-label="primary">
  <a class="chip-link me back" href="/" aria-label="Back to home" data-track="back_click" data-track-from="{path}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M11 6l-6 6 6 6"/></svg></a>
  <a class="chip-link dark talk" href="mailto:hi@justinreyna.design?subject=New%20project" data-open="project-dialog" data-track="cta_click" data-track-cta="lets_talk" data-track-placement="project_nav">Let’s talk <span aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3h11A2.5 2.5 0 0 1 20 5.5v8a2.5 2.5 0 0 1-2.5 2.5H11l-4.5 4v-4A2.5 2.5 0 0 1 4 13.5z"/></svg></span></a>
</nav>
"""

FOOT = """</div>
</body>
</html>
"""

PROJECTS = [
    dict(slug="youtube", name="YouTube", tags=["product", "ai workflows"],
         intro=["An AI assistant pilot for creators, launched with Google Labs. I led design from MVP to working prototype, including the assistant's personas."],
         credits=[("Client", "YouTube"), ("Project", "Creator Chatbot"), ("Partner", "Google Labs"), ("Role", "Senior product designer, in-house"), ("Year", "2025")],
         shots=[(f"/work/youtube-0{i}.jpg", 2400, 1350) for i in range(1, 6)]),
    dict(slug="google", name="Google", tags=["web", "design systems"], frame="Google Pixel — portfolio landing page",
         intro=["A single page for the full Pixel portfolio. At Basic, I led design with the Pixel team, extending Google's design system where needed."],
         credits=[("Client", "Google Pixel"), ("Studio", "BASIC® (part of Dept)"), ("Role", "Senior designer"), ("Years", "2021–2023")],
         shots=list(zip([f"/work/google-{i:02d}.jpg" for i in range(1, 24)], [1864] * 23,
                        [1314, 1014, 1130, 332, 1316, 912, 916, 1162, 832, 1384, 276, 1000, 1346, 980, 368, 948, 772, 1288, 978, 1286, 1180, 1028, 734]))),
    dict(slug="apple-tv", name="Apple TV", tags=["web", "design systems"], frame="Apple TV — press site",
         intro=["A refresh of the Apple TV press site. At Elephant, I defined requirements with the Apple TV team and extended its design system."],
         credits=[("Client", "Apple TV"), ("Studio", "Elephant"), ("Role", "Senior designer"), ("Year", "2023")],
         shots=[("/work/appletv-full.jpg", 2048, 6973)]),
]
SOON = [("Meta", ["coming soon"]), ("Yahoo", ["coming soon"])]


def img(src, w, h, alt, eager=False):
    lazy = '' if eager else ' loading="lazy"'
    return f'<img src="{src}" width="{w}" height="{h}" alt="{escape(alt)}"{lazy} decoding="async">'


def tile(href, name, src, w, h, alt, below, extra_cls="", img_cls=""):
    return f"""<a class="card tile {extra_cls}" href="{href}">
      <div class="shot">
        <img class="{img_cls}" src="{src}" width="{w}" height="{h}" alt="{escape(alt)}" loading="lazy" decoding="async">
        <div class="titlebar"><b>{name}</b><span class="plus" aria-hidden="true">+</span></div>
      </div>
      <div class="below">{below}</div>
    </a>"""


SUMMARY = {"youtube": "A pilot testing whether an AI assistant could be genuinely useful to creators. Launched with Google Labs.",
           "google": "A single page presenting the full Pixel portfolio, designed at Basic within Google's design system.",
           "apple-tv": "A refresh of the press site where news about Apple TV shows is published, designed at Elephant."}

# from justin's linkedin export, oct 2026
EDUCATION = [
    ("2022", "Stanford University", "Certificate, Creativity and Design Thinking"),
    ("2016", "General Assembly", "UX Design Online Circuit"),
    ("2016", "MakerSquare", "MakerPrep, front-end web development"),
    ("2015", "Georgetown University", "BBA, International Business & Finance"),
]
# client logos, self-hosted in /img/logos (from simple icons @16.34.0 and wikimedia commons, oct 2026)
LOGOS = {"Airbnb": "airbnb", "Amazon Web Services": "aws", "AMC Networks": "amc-networks", "Axios": "axios",
         "Coinbase": "coinbase", "DocuSign": "docusign", "Google Chrome": "google-chrome", "Google Play": "google-play",
         "Meta": "meta", "Morgan Stanley": "morgan-stanley"}

# inside design (invision's blog) now redirects to miro.com — link the wayback machine copies
WRITING = [
    ("Designing Products with Gender Inclusion in Mind", "Inside Design by InVision", "2018",
     "https://web.archive.org/web/20241105151744/https://www.invisionapp.com/inside-design/designing-products-gender-inclusion/"),
    ("A Guide to Color Accessibility in Product Design", "Inside Design by InVision", "2018",
     "https://web.archive.org/web/20241223183418/https://www.invisionapp.com/inside-design/color-accessibility-product-design/"),
]

# section icons — 12×12 pixel art, drawn as crisp ink squares (a nod to stone os)
PIXEL_ICONS = {
    "work": [            # folder
        "............",
        ".####.......",
        "#....######.",
        "#..........#",
        "############",
        "#..........#",
        "#..........#",
        "#..........#",
        "#..........#",
        "#..........#",
        "############",
        "............"],
    "experiments": [     # flask
        "...######...",
        "....#..#....",
        "....#..#....",
        "....#..#....",
        "...#....#...",
        "..#......#..",
        ".#........#.",
        ".#.######.#.",
        "#.########.#",
        "#.########.#",
        "############",
        "............"],
    "clients": [         # skyline: companies
        "......#####.",
        "......#...#.",
        ".####.#.#.#.",
        ".#..#.#...#.",
        ".#..#.#.#.#.",
        ".#..#.#...#.",
        ".#..#.#.#.#.",
        ".#..#.#...#.",
        ".#..#.#.#.#.",
        ".#..#.#...#.",
        "############",
        "............"],
    "education": [       # open book
        "............",
        ".####..####.",
        "#....##....#",
        "#.##.##.##.#",
        "#....##....#",
        "#.##.##.##.#",
        "#....##....#",
        "#.##.##.##.#",
        "#....##....#",
        "#####..#####",
        "............",
        "............"],
    "writing": [         # page of text
        ".#######....",
        ".#.....##...",
        ".#.....#.#..",
        ".#.....####.",
        ".#........#.",
        ".#.#####..#.",
        ".#........#.",
        ".#.#####..#.",
        ".#........#.",
        ".#.####...#.",
        ".#........#.",
        ".##########."],
}

def pixel_icon(name):
    rows = PIXEL_ICONS[name]
    d = "".join(f"M{x} {y}h1v1h-1z" for y, row in enumerate(rows) for x, c in enumerate(row) if c == "#")
    return f'<span class="pix" aria-hidden="true"><svg viewBox="0 0 12 12" shape-rendering="crispEdges"><path d="{d}"/></svg></span>'

# "also worked with": client, studio (studio kept for reference, not shown)
# justin wants only recognizable names here. the full list (with studios) is in FULL_ROSTER for reference.
ROSTER = [("Airbnb", "Independent"), ("Amazon Web Services", "Instrument"), ("AMC Networks", "Handsome"),
          ("Axios", "Handsome"), ("Coinbase", "ustwo"), ("DocuSign", "Basic"), ("Google Chrome", "Basic"), ("Google Play", "Huge"),
          ("Meta", "Handsome, Code and Theory"), ("Morgan Stanley", "Rebel & Co.")]
FULL_ROSTER = sorted([
    ("Airbnb", "Independent"), ("AMC Networks", "Handsome"), ("Amazon Web Services", "Instrument"),
    ("Axios", "Handsome"), ("Blucora", "Handsome"), ("Coinbase", "ustwo"), ("DocuSign", "Basic"),
    ("Emcee", "Independent"), ("Meta for Business", "Handsome"), ("FIS", "I&CO"), ("Google Chrome", "Basic"),
    ("Google Chromebook", "This Place"), ("Google Learning", "Huge"), ("Google Play", "Huge"),
    ("Google Store", "Basic, Huge"), ("InStride", "Handsome"), ("Keller Williams", "Handsome"),
    ("Liquidity", "Ruca"), ("Lookback", "In-house"), ("InVision", "In-house"), ("Morgan Stanley", "Rebel & Co."),
    ("Nest Renew", "Huge"), ("Proof Analytics", "Rebel & Co."), ("Simpatica", "Rebel & Co."),
    ("TaxAct", "Handsome"), ("Upstart", "Ruca"), ("Voice", "Ruca"), ("WIN Reality", "Independent"),
    ("WP Engine", "Handsome"),
], key=lambda r: r[0].lower())


def home_head(title, **kw):
    # homepage has no top bar — the rail carries the name and the asks
    return head(title, **kw).split('<nav class="bar"')[0]


# "start a project" modal, shared by the homepage and the project pages (their contact button)
PROJECT_DIALOG = f"""<dialog class="modal" id="project-dialog" data-lenis-prevent aria-labelledby="pd-h">
  <form id="project-form" class="modal-body">
    <header class="modal-head"><h2 class="title" id="pd-h">Start a project</h2><button type="button" class="close" data-close aria-label="Close"></button></header>
    <p class="modal-lede">Tell me a little about what you're working on.</p>
    <div class="form-rows">
      <label class="frow"><span class="flabel">Name</span><input name="name" required autocomplete="name" placeholder="Your name"></label>
      <label class="frow"><span class="flabel">Email</span><input name="email" type="email" required autocomplete="email" placeholder="you@company.com"></label>
      <label class="frow"><span class="flabel">Company</span><input name="company" autocomplete="organization" placeholder="Optional"></label>
      <fieldset class="frow"><legend class="flabel">Looking for</legend>
        <div class="picks">{''.join(f'<label class="pick" data-c="{COLOR[t]}"><input type="checkbox" name="needs" value="{SHOW.get(t, t[0].upper() + t[1:])}"><span>{SHOW.get(t, t[0].upper() + t[1:])}</span></label>' for t in ['web', 'design systems', 'product', 'brand', 'motion', 'ai workflows'])}</div>
      </fieldset>
      <fieldset class="frow"><legend class="flabel">Timeline</legend>
        <div class="picks">{''.join(f'<label class="pick ink"><input type="radio" name="timeline" value="{v}"{" checked" if i == 1 else ""}><span>{v}</span></label>' for i, v in enumerate(["As soon as possible", "1–3 months", "3+ months", "Just exploring"]))}</div>
      </fieldset>
      <label class="frow top"><span class="flabel">About</span><textarea name="message" rows="4" required placeholder="The problem, the goal, anything useful"></textarea></label>
    </div>
    <p class="sent" hidden>Your email app should open with everything filled in. If it doesn't, write to hi@justinreyna.design.</p>
    <button class="action primary wide" type="submit">Send <span class="plus send" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"><path d="M21 3 10.5 13.5"/><path d="M21 3 14.5 21l-4-7.5L3 9.5 21 3z"/></svg></span></button>
  </form>
</dialog>
"""


# newsletter: off until a provider is picked (substack / buttondown / …). flip to True and wire
# the form in scripts/contact.js to bring back the link in the rail and its modal.
NEWSLETTER = False
NEWSLETTER_LINK = '        <a href="#newsletter-dialog" data-open="newsletter-dialog">Newsletter</a>\n' if NEWSLETTER else ""
NEWSLETTER_DIALOG = f"""<dialog class="modal small" id="newsletter-dialog" data-lenis-prevent aria-labelledby="nd-h">
  <form id="newsletter-form" class="modal-body">
    <header class="modal-head"><h2 class="title" id="nd-h">Newsletter</h2><button type="button" class="close" data-close aria-label="Close"></button></header>
    <p class="modal-lede">Occasional notes on new work and experiments.</p>
    <div class="form-rows">
      <label class="frow"><span class="flabel">Email</span><input name="email" type="email" required autocomplete="email" placeholder="you@company.com"></label>
    </div>
    <p class="sent" hidden>Sign-ups open soon.</p>
    <button class="action primary wide" type="submit">Sign up <span class="plus send" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"><path d="M21 3 10.5 13.5"/><path d="M21 3 14.5 21l-4-7.5L3 9.5 21 3z"/></svg></span></button>
  </form>
</dialog>
"""

# screen-reader descriptions for the project images, written from the images themselves
ALT = {
  "youtube-01.jpg": "Three circular chatbot avatars on a pale background: a green-clad elf woman, a bearded outdoorsman in a tan jacket, and a smiling yellow wrench.",
  "youtube-02.jpg": "Slide titled “Spectrum of visualizations” for the Creator Chatbot incubator: avatars from a non-human wrench and blue blob, to an elf, to a realistic human.",
  "youtube-03.jpg": "Five phone screens on olive green: a farming video's comments with a Creator AI reply, then a chat with Freya the Farm Fairy.",
  "youtube-04.jpg": "Five phone screens on blue: a hiking video with a “Chat with Chuck AI” button, then a chat suggesting a trip and gear from Chuck's store.",
  "youtube-05.jpg": "Five phone screens on tan: The Handy Home channel page, then a chat with Wilmer the Wrench diagnosing a leaky faucet and linking a video.",
  "appletv-full.jpg": "Full-length Apple TV press page for the show Silo: key art header, trailer, episode images, cast and crew, related news and press contacts.",
  "google-01.jpg": "Top of the Pixel portfolio page: “Engineered by Google. For all that you do.” above phone, watch, earbud and tablet thumbnails.",
  "google-02.jpg": "Overhead product shot of Pixel phones, a foldable, a tablet, a watch and earbuds with case on a pale surface.",
  "google-03.jpg": "Gemini section, “Gemini. Your built-in AI assistant.”, above a Google Maps card of New Orleans with red location pins.",
  "google-04.jpg": "Two tabs, “Do almost anything, like it's nothing” (active) and “Image editing that works wonders”, with a line about Gemini on Pixel.",
  "google-05.jpg": "Pixel Camera section, “Stunning photos and videos come as standard”, with a Pixel Watch on a wrist showing a camera shutter countdown.",
  "google-06.jpg": "“Transform photos and videos in the blink of AI” beside a smiling group photo of three friends, with a replay button.",
  "google-07.jpg": "“Showcase your memories” beside a Pixel Tablet on a desk showing a photo of two laughing friends and a 9:30 clock.",
  "google-08.jpg": "Safety section, “Safe and secure, wherever and whenever”: a phone showing Safety Check beside a watch alerting a car crash.",
  "google-09.jpg": "“Shop the Pixel portfolio” with four tiles: phones, watches, earbuds and tablet.",
  "google-10.jpg": "Health and fitness section, “Your wellness, your way”, with a runner wearing earbuds and a watch against a wall of teal and yellow shapes.",
  "google-11.jpg": "Centered copy about using Pixel Watch 3 to create custom runs, with real-time running guidance and performance insights.",
  "google-12.jpg": "“The perfect workout partners”: cards for Fitbit Premium workouts on a phone, an earbud in an ear, and an athlete stretching with a watch.",
  "google-13.jpg": "“Hands-free help, when and where you need it”: Google Pay on a watch, a woman wearing an earbud, and a Live Translate screen.",
  "google-14.jpg": "“Streamline and save time”: a hand holding a phone with a Pixel Buds Pro 2 pairing prompt and a Connect button.",
  "google-15.jpg": "Two tabs, “Pair your devices, effortlessly” (active) and “Unlock your phone from your watch”, with a Fast Pair description.",
  "google-16.jpg": "“AI helps you catch every word” beside a man in a pink jacket and sunglasses tapping an earbud on a crosswalk.",
  "google-17.jpg": "“Shop the Pixel portfolio” again, with tiles for phones, watches, earbuds and tablet.",
  "google-18.jpg": "Smart home section, “More help for all of your home”, with a phone showing Google Home lighting controls.",
  "google-19.jpg": "“Know who, or what, is at your door” beside a watch showing a live doorbell feed of a delivery person holding a box.",
  "google-20.jpg": "“Organise and personalise your Smart Home from one simple app” over a collage of the Google Home app, cameras, doorbell, watch and speaker.",
  "google-21.jpg": "Entertainment section, “Bring shows and music to life”: a docked tablet, a man with earbuds and phone, and a watch used as a TV remote.",
  "google-22.jpg": "“Discover the world of Pixel” carousel with article cards on eSIM and Dual SIM, SIM setup, and Gemini on Wear OS.",
  "google-23.jpg": "Page footer with support links, social icons, a region selector and legal links.",
}


def home():
    rows = []
    for i, p in enumerate(PROJECTS, 1):
        rows.append(f"""      <a class="row" href="/work/{p['slug']}/" data-track="select_content" data-track-content_type="project" data-track-item_id="{p['slug']}" data-track-placement="home_list">
        <span class="no">{i:02d}</span><span class="name">{p['name']}</span>
        <span class="sum">{SUMMARY[p['slug']]}</span>
        <span class="tags">{''.join(tag(t, True) for t in p['tags'])}</span>
        <span class="plus" aria-hidden="true">+</span>
      </a>""")
    for j, (name, tags) in enumerate(SOON, len(PROJECTS) + 1):
        rows.append(f"""      <div class="row soon">
        <span class="no">{j:02d}</span><span class="name">{name}</span>
        <span class="sum"></span>
        <span class="tags">{''.join(tag(t, True) for t in tags)}</span>
        <span class="plus lock" aria-hidden="true"><svg viewBox="0 0 16 16" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"><rect x="3" y="7" width="10" height="7" rx="1.5"/><path d="M5.5 7V5.2a2.5 2.5 0 0 1 5 0V7"/></svg></span>
      </div>""")
    person = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"Person","name":"Justin Reyna","url":"https://justinreyna.design/","email":"mailto:hi@justinreyna.design","jobTitle":"Designer and creative technologist","address":{"@type":"PostalAddress","addressLocality":"Austin","addressRegion":"TX"},"sameAs":["https://www.linkedin.com/in/justinreyreyna/"]}</script>\n'
    return home_head("Justin Reyna — Designer and creative technologist").replace("</head>", person + "</head>") + f"""<div class="home">

  <aside class="rail">
    <section class="card id marquee-card">
      <h1 class="sr">Justin Reyna is a creative technologist based in Austin, Texas.</h1>
      <div class="marquee" aria-hidden="true"><div class="track">
        <span>Justin Reyna is a creative technologist based in Austin, Texas —</span><span>Justin Reyna is a creative technologist based in Austin, Texas —</span>
      </div></div>
    </section>
    <section class="card about scrolls" aria-label="about" data-lenis-prevent>
      <span class="label">About</span>
      <p>I am a designer and creative technologist working across human–computer interaction, design systems, and product. My practice moves from deep, human-centered research toward holistic experience design.</p>
      <p>I embed with studios and in-house teams, working within or extending design systems so products can scale toward their business goals without losing user trust. Increasingly, I bring AI workflows into that process, shortening the path from research to tested prototype.</p>
      <p>Outside of client work, I am building <a class="ext" href="https://otro.art" target="_blank" rel="noreferrer">OTRO<span aria-hidden="true">&#8239;↗</span><span class="sr"> (opens in a new tab)</span></a>, an artist residency and gathering space in Mexico City, taking my love for experience design into the physical world.</p>
    </section>
    <section class="card capabilities" aria-label="capabilities">
      <span class="label">Capabilities</span>
      <div class="tags">{''.join(tag(t) for t in ['web', 'design systems', 'product', 'brand', 'motion', 'ai workflows'])}</div>
    </section>
    <section class="card cta" id="contact" aria-label="work together">
      <span class="label">Work together</span>
      <p class="ask">Have a project in mind?</p>
      <div class="actions">
        <a class="action primary" href="mailto:hi@justinreyna.design?subject=New%20project" data-open="project-dialog" data-track="cta_click" data-track-cta="lets_talk" data-track-placement="home_rail">Let’s talk <span class="plus chat" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3h11A2.5 2.5 0 0 1 20 5.5v8a2.5 2.5 0 0 1-2.5 2.5H11l-4.5 4v-4A2.5 2.5 0 0 1 4 13.5z"/></svg></span></a>
      </div>
      <nav class="elsewhere" aria-label="elsewhere">
        <a href="https://www.linkedin.com/in/justinreyreyna/" target="_blank" rel="noreferrer">LinkedIn</a>
{NEWSLETTER_LINK}        <a href="mailto:hi@justinreyna.design" data-place="home_rail">Email</a>
        <span>© 2026</span>
      </nav>
    </section>
  </aside>

  <main id="main" class="main">
    <section class="panel" id="work" aria-labelledby="work-h">
      <header class="panel-head"><h2 class="title" id="work-h">Selected work</h2>{pixel_icon("work")}</header>
{chr(10).join(rows)}
    </section>

    <section class="panel" id="clients" aria-labelledby="cl-h">
      <header class="panel-head"><h2 class="title" id="cl-h">Also worked with</h2>
{pixel_icon("clients")}
      </header>
      <ul class="logo-strip" data-lenis-prevent-horizontal tabindex="0" aria-label="Client logos, scrolls sideways">{''.join(
        (f'<li class="logo-tile"><span class="mark"><img src="/img/logos/{LOGOS[c]}.svg" alt="" loading="lazy"></span><span class="label">{escape(c)}</span></li>'
         if c in LOGOS else
         f'<li class="logo-tile word"><span class="mark"><span class="wordmark">{escape(c)}</span></span></li>')
        for c, w in ROSTER)}</ul>
    </section>

    <section class="panel" id="experiments" aria-labelledby="exp-h">
      <header class="panel-head"><h2 class="title" id="exp-h">Experiments</h2>{pixel_icon("experiments")}</header>
      <a class="row" href="/experiments/stone-os/" data-track="select_content" data-track-content_type="experiment" data-track-item_id="stone-os" data-track-placement="home_list">
        <span class="no">01</span><span class="name">Stone OS</span>
        <span class="sum">A 1-bit desktop from a machine that never existed, with an interface that sounds like stone.</span>
        <span class="tags"><span class="label">Aug 2026</span></span>
        <span class="plus go" aria-hidden="true"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="square"><path d="M4.5 11.5l7-7M6 4.5h5.5V10"/></svg></span>
      </a>
    </section>

    <section class="panel" id="education" aria-labelledby="ed-h">
      <header class="panel-head"><h2 class="title" id="ed-h">Education</h2>{pixel_icon("education")}</header>
      <ol class="cv edu">{''.join(f'<li><span class="when">{w}</span><span class="what">{escape(sch)}</span><span class="detail">{escape(deg)}</span></li>' for w, sch, deg in EDUCATION)}</ol>
    </section>

    <section class="panel" id="writing" aria-labelledby="wr-h">
      <header class="panel-head"><h2 class="title" id="wr-h">Writing</h2>{pixel_icon("writing")}</header>
      <ol class="cv writing">{''.join(f'<li><a href="{u}" target="_blank" rel="noreferrer"><span class="when">{d}</span><span class="what">{escape(t)}</span><span class="detail">{escape(pub)}<span class="sr"> (archived copy, opens in a new tab)</span></span><span class="plus go" aria-hidden="true"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="square"><path d="M4.5 11.5l7-7M6 4.5h5.5V10"/></svg></span></a></li>' for t, pub, d, u in WRITING)}</ol>
    </section>
  </main>

</div>

<div class="fab" inert><a class="action primary" href="mailto:hi@justinreyna.design?subject=New%20project" data-open="project-dialog" data-track="cta_click" data-track-cta="lets_talk" data-track-placement="floating">Let’s talk <span class="plus chat" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3h11A2.5 2.5 0 0 1 20 5.5v8a2.5 2.5 0 0 1-2.5 2.5H11l-4.5 4v-4A2.5 2.5 0 0 1 4 13.5z"/></svg></span></a></div>

{PROJECT_DIALOG}
{NEWSLETTER_DIALOG if NEWSLETTER else ""}<script src="/scripts/contact.js?v={VER}" defer></script>
<script src="/scripts/rail.js?v={VER}" defer></script>
<script src="/scripts/float.js?v={VER}" defer></script>
<script src="/scripts/logos.js?v={VER}" defer></script>
""" + FOOT


def project(i, p):
    nxt = PROJECTS[i % len(PROJECTS)]
    part = p.get("frame", "").split(" — ")[-1]
    if p.get("frame"):
        imgs = "".join(img(s, w, h, ALT[s.rsplit("/", 1)[1]], eager=k == 1)
                       for k, (s, w, h) in enumerate(p["shots"], 1))
        plates = f'<figure class="card plate fullpage"><div class="frame">{imgs}</div></figure>'
    else:
        plates = "".join(f'<figure class="card plate">{img(s, w, h, ALT[s.rsplit("/", 1)[1]], eager=k == 1)}</figure>'
                         for k, (s, w, h) in enumerate(p["shots"], 1))
    # project pages: the nav lives at the top of the 100vh rail instead of above the columns
    path, title = f"/work/{p['slug']}/", f"{p['name']} — Justin Reyna"
    full = head(title, path, " ".join(p["intro"]))
    nav = full.split('<nav class="bar"', 1)[1].split('</nav>', 1)[0]
    return full.split('<nav class="bar"')[0] + f"""
<div class="project">
  <aside class="rail project-rail">
    <nav class="bar"{nav}</nav>
    <section class="card info statement scrolls" aria-label="{p['name']}" data-lenis-prevent>
      <div class="info-top"><div class="tags">{''.join(tag(t) for t in p['tags'])}</div><span class="label">{i:02d} / {len(PROJECTS):02d}</span></div>
      <h1>{p['name']}</h1>
      <div>{''.join(f'<p>{escape(x)}</p>' for x in p['intro'])}</div>
      <dl class="credits">{''.join(f'<dt>{k}</dt><dd>{escape(v)}</dd>' for k, v in p['credits'])}</dl>
    </section>
    <a class="card next-card" data-c="{COLOR[nxt['tags'][0]]}" href="/work/{nxt['slug']}/" data-track="select_content" data-track-content_type="project" data-track-item_id="{nxt['slug']}" data-track-placement="next_card"><span class="next-text"><span class="label">Next</span><b>{nxt['name']}</b></span><svg class="next-arrow" viewBox="0 0 100 100" aria-hidden="true"><path d="M18 82 L82 18 M44 18 H82 V56" vector-effect="non-scaling-stroke"/></svg></a>
  </aside>
  <main id="main" class="plates">{plates}</main>
</div>

{PROJECT_DIALOG}<script src="/scripts/contact.js?v={VER}" defer></script>
<script src="/scripts/rail.js?v={VER}" defer></script>
<script src="/scripts/float.js?v={VER}" defer></script>
""" + FOOT


import re

def no_widows(html):
    """join the last two words of every paragraph, summary and credit with a
    non-breaking space, so no line ever ends up holding a single word."""
    def bind(m):
        open_tag, inner, close = m.group(1), m.group(2), m.group(3)
        # only touch the text after the last inline tag
        head, sep, tail = inner.rpartition('>')
        tail = re.sub(r' (\S+)\s*$', r'&nbsp;\1', tail.rstrip()) if ' ' in tail.strip() else tail
        return open_tag + head + sep + tail + close
    return re.sub(r'(<(?:p|dd)\b[^>]*>|<span class="sum">)(.*?)(</(?:p|dd|span)>)', bind, html, flags=re.S)


BACK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>'

def not_found():
    # github pages serves /404.html for any missing path, so every link in it is absolute
    return home_head("Page not found — Justin Reyna", path="/404.html", index=False) + f"""<main id="main" class="lost">
  <section class="card">
    <span class="label">404</span>
    <h1>This page doesn’t exist.</h1>
    <p>It may have moved when the site was rebuilt. Stone OS now lives under <a href="/experiments/stone-os/">experiments</a>.</p>
    <a class="action primary" href="/">Back to home <span class="plus icon" aria-hidden="true">{BACK}</span></a>
  </section>
</main>
""" + FOOT

REDIRECT = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex">
<title>Experiments — Justin Reyna</title>
<link rel="canonical" href="https://justinreyna.design/#experiments">
<meta http-equiv="refresh" content="0; url=/#experiments">
</head><body><a href="/#experiments">Experiments</a></body></html>
"""

pages = {"index.html": home(), "404.html": not_found()}
for i, p in enumerate(PROJECTS, 1):
    pages[f"work/{p['slug']}/index.html"] = project(i, p)
for rel, html in pages.items():
    (ROOT / rel).parent.mkdir(parents=True, exist_ok=True)
    (ROOT / rel).write_text(no_widows(html))
(ROOT / "experiments/index.html").write_text(REDIRECT)

urls = ["/"] + [f"/work/{p['slug']}/" for p in PROJECTS] + ["/experiments/stone-os/"]
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
print("built:", ", ".join(list(pages) + ["experiments/index.html", "sitemap.xml"]))

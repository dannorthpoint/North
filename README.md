# North Point Creative

Source for [northpointcreative.co.uk](https://northpointcreative.co.uk/) — a single-page
static site. There is no build step: the repository root is the deployed site root.

## Layout

| Path | Purpose |
|---|---|
| `index.html` | The entire site — markup, inline CSS, and inline JS |
| `img_*.webp`, `portrait_real_dan.webp` | Portfolio and studio imagery |
| `favicon.*`, `apple-touch-icon.png`, `maskable-512x512.png`, `site.webmanifest` | Icons and PWA manifest |
| `og-image.png` | Social sharing preview |
| `robots.txt`, `sitemap.xml` | Crawling and indexing |
| `docs/` | Audit notes and enhancement write-ups (not part of the site) |
| `tools/` | One-off audit scripts (contrast check, PageSpeed fetch) |

## The compass mark

The mark is drawn once as an SVG `<symbol id="np-mark">` at the top of `<body>` and placed
with `<use href="#np-mark">` wherever it appears. It inherits `currentColor` for its light
facets, so the same markup reads correctly on paper and on noir. It replaced two PNGs that
were referenced but never existed in the repository.

## Known gaps

`index.html` references one asset that is not in this repository: `video_btg_lee.mp4`, the
Beyond The Gate testimonial film. If the file is missing the player stands itself down on
error and the section reads as a pull quote, so nothing visibly breaks — but the film does
not play. Add the file and the player returns on its own.

## The intro

The loader plays once per session, lifts on its own when the page is ready, and offers an
Enter button from the first second. It never appears for `prefers-reduced-motion`, never
appears on a second page view in the same session, and is `display: none` unless a script
has opted into it — so scripting that is off, blocked, or broken leaves the page uncovered
rather than sealed behind a plate.

## Roadmap

`docs/northpointcreative_aesthetic_seo_audit.md` holds the current aesthetic and SEO roadmap.
Its headline recommendation is a light homepage refinement plus a five-page content
architecture, rather than a redesign.

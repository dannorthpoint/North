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

## Known gaps

`index.html` references three assets that are not in this repository:

- `north-point-mark.png` and `north-point-mark-light.png` — the compass mark, used in the
  masthead, cover, and footer. Both `<img>` tags hide themselves via `onerror`, so a missing
  file degrades quietly, but the mark never appears.
- `video_btg_lee.mp4` — the Beyond The Gate testimonial video. The poster image still shows;
  playback fails.

If these files exist on the live host, add them here so the repository is a complete copy of
the deployment. If they do not, either supply them or remove the references.

## Roadmap

`docs/northpointcreative_aesthetic_seo_audit.md` holds the current aesthetic and SEO roadmap.
Its headline recommendation is a light homepage refinement plus a five-page content
architecture, rather than a redesign.

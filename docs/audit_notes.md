# North Point Creative Website Audit Notes

## Initial inspection

- Archive contains a single-page static site (`index.html`), eight locally hosted image assets, favicons, a manifest, `robots.txt`, and `sitemap.xml`.
- The page title is **“North Point Creative | Web Design Studio, Liverpool”** and its principal audience is prospective local and UK-wide web-design clients.
- The initial visual experience is a crafted editorial/gallery aesthetic: warm ivory paper, black ink, restrained champagne/brass accents, Fraunces display type, Jost supporting type, fine rules, folio-like labels, and a compass/star visual mark.
- The rendered hero is elegant and high-end. It has a masthead, sticky navigation, large “NORTH POINT / CREATIVE” wordmark, a two-column value proposition, primary quote CTA, secondary portfolio CTA, and proof points below.
- Initial visual strengths: clear art direction; distinctive typography; cohesive palette; strong brand personality; a portfolio-first information order; and two prominent primary conversion paths.
- Initial opportunities observed: the upper page is visually dense for a new visitor; body copy, eyebrow labels, and nav text appear very small at desktop size; the brand wordmark and actual value proposition compete for attention; the loader and pervasive texture/animation may add perceived loading delay; the primary CTA could be more concrete and conversion-oriented; and a smaller logo/mark could reserve more hero space for credibility and case-study proof.

## Evidence reviewed

- Rendered browser homepage at local file URL, with the loader completed.
- Current visible hierarchy: masthead → sticky nav → “Web Design Studio / Volume I” → oversized brand name → tagline and supporting copy → quote CTA → secondary links.
- Source inspection began: metadata, structured data, CSS system, responsive breakpoints, and asset links are present in the homepage file.

## Next audit steps

1. Review remaining page structure and responsive behavior.
2. Inventory headings, images, links, forms, scripts, schema, robots, sitemap, and performance-sensitive implementation.
3. Produce a prioritised aesthetic and SEO improvement roadmap only; no changes will be made.

## Live deployment and crawlability

The public deployment matches the supplied archive’s core copy and single-page structure. It is publicly crawlable: `robots.txt` allows all user agents and explicitly points to `https://northpointcreative.co.uk/sitemap.xml`. The XML sitemap currently contains one canonical URL, the homepage, last modified on 11 July 2026. This means the technical baseline for discovery is sound, but the site currently has only one indexable content asset through which to compete for the wider range of commercial and location-intent searches relevant to the studio.

The live page presents useful metadata and content for its primary query theme: its title, description, canonical URL, Open Graph metadata, and a `ProfessionalService` JSON-LD entity are present in the supplied source. The page also contains strong business identity signals—Liverpool, UK service area, founder, email address, website, portfolio work, pricing, and a contact form. The key opportunity is not a missing SEO foundation; it is converting the strong single-page foundation into a small, focused search-content system with individual service, location, portfolio, and proof pages.

## Responsive-rendering observation

Headless desktop and mobile captures show the fixed masthead and navigation correctly, but the hero’s animated content remains absent beneath it after the intro sequence. The interactive browser view did render the completed hero correctly, so this is not proof of a universal visitor-facing failure. It does, however, indicate that the hero relies heavily on JavaScript and animation-state transitions. The implementation should be hardened so the core headline, value proposition, and primary CTA are visible by default, then enhanced with motion rather than revealed only after a loader-dependent sequence. This is both a visual-resilience and performance/conversion consideration, especially on slow devices, restrictive browsers, or with interrupted font and script loading.

On a narrow mobile viewport, the top layout is compact and coherent: the masthead label remains readable, the logo, Enquire button, and hamburger fit without collision, and the background/palette stay on-brand. The high-level mobile opportunity is not a structural collapse issue but a first-screen conversion issue: the visible hero message must not be delayed or hidden behind decorative animation.

## Design observations: portfolio, process, and pricing

The gallery treatment is the site’s strongest visual device. The alternating framed-project display, editorial labels, controlled lighting effect, and ample negative space make the work feel curated rather than merely listed. It establishes a premium studio character. Its commercial value would increase further if each featured project supplied a very short outcome signal—such as increased leads, donation sign-ups, bookings, or conversion uplift—next to the existing type/status metadata.

The process and methodology sections retain the dark, quiet visual treatment, but the body copy and fine metadata are relatively low-contrast and small. These areas are aesthetically consistent, yet a visitor seeking fast reassurance may have to work too hard to understand the service. A modest type-size and contrast increase, plus tighter copy blocks, would preserve the editorial restraint while improving scanability.

The pricing presentation is tasteful and unusually transparent. The large price figures establish hierarchy well, and the Standard package is marked as “Best Value.” The feature rows, however, rely on small, horizontally distributed text. On smaller screens this should become a stacked inclusion list with clearer spacing. At the commercial level, pricing would benefit from a concise qualification line—what is included, who each tier is for, and what is explicitly excluded—so prospects can self-select without uncertainty.

## SEO standards used in this audit

The proposed content expansion will follow Google’s guidance to create original, helpful, people-first material that demonstrates firsthand expertise and makes authorship clear. The proposed mobile and animation hardening is also material to search visibility because Google uses the mobile version of content for indexing and ranking, and its guidance specifically emphasizes that primary content must be accessible and renderable on mobile. The schema recommendations will favor fewer, complete, accurate JSON-LD entities tied to visible page content, then validated after deployment. The recommendations do not treat metadata or schema as a substitute for relevant service pages, proof, or useful case studies.

Source references collected for the final report: Google Search Central’s “Creating helpful, reliable, people-first content”; “Mobile site and mobile-first indexing best practices”; “Understanding page experience in Google Search results”; and “Introduction to structured data markup in Google Search.”

## Sitemap detail

The sitemap is located at the root, is referenced in `robots.txt`, and contains the canonical homepage URL—good foundational implementation. Its `lastmod` date is 11 July 2026, while the live homepage response reports a later modification on 15 July 2026. Update `lastmod` only when a material page change occurs, and remove the present `changefreq` and `priority` values if they are being maintained manually, since Google documents that it ignores those fields. This is a low-effort housekeeping item rather than a material ranking lever.

## Performance-measurement scope

A public mobile PageSpeed API request could not be completed because the shared service quota was exhausted. Accordingly, this audit does not claim measured Core Web Vitals or Lighthouse scores. Performance recommendations below are source-based and should be validated after implementation in the site owner’s Search Console and PageSpeed Insights accounts. The live homepage does use gzip compression, and the local image assets are modest in size; the main practical performance risk visible in the code is the deliberate loader/animation sequence and two third-party scripts rather than oversized local imagery.

# North Point Creative: Aesthetic and SEO Enhancement Roadmap

**Prepared for:** North Point Creative  
**Prepared by:** Manus AI  
**Review date:** 20 July 2026  
**Scope:** A review of the supplied static site archive and the publicly available homepage. **No files, copy, settings, or live pages were changed.**

## Executive conclusion

North Point Creative already has a strong and unusually distinctive visual identity. The site feels like a small, confident editorial studio rather than a generic template: the warm paper palette, dark gallery sections, compass motif, quiet typography, and framed portfolio work all reinforce the idea of considered craft. The right direction is therefore **refinement, not a redesign**.

The largest opportunity is to make the same premium visual language work harder commercially. The homepage currently gives substantial space to atmosphere, brand display, and motion before it makes the service proposition, audience, proof, and next step effortless to understand. The SEO foundation is sound—there is a canonical URL, descriptive title and meta description, crawl permission, a sitemap, Open Graph data, and `ProfessionalService` JSON-LD—but the site has only one indexable content page in its sitemap. That prevents it from addressing the distinct searches for web design, web development, packages, local intent, and individual portfolio work. [1] [2] [3]

> **Recommended principle:** retain the gallery/editorial world, but make the first screen, service pages, and case studies more explicit about what North Point does, for whom, where, and why it is credible.

## Current health snapshot

| Area | What is already working | Main constraint | Priority response |
|---|---|---|---|
| **Brand and art direction** | The ivory/ink/champagne palette, serif display type, compass mark, and gallery presentation feel cohesive and memorable. | Some fine labels and dense supporting copy are easy to overlook when a visitor is scanning. | Preserve the system; selectively enlarge supporting text and reduce visual competition. |
| **Hero and conversion path** | The headline, fixed-price promise, portfolio link, and quote CTA are all present. | The brand wordmark and intro sequence dominate attention; the exact service and local relevance arrive second. | Make the descriptive service proposition visible immediately and ensure it never depends on the loader. |
| **Portfolio proof** | Four polished, varied examples prove range and are presented in the site’s strongest visual module. | They show the work but not yet the business result, client voice, scope, or process. | Turn each into a compact case study with outcome evidence. |
| **SEO baseline** | The homepage has a title, description, canonical, robots directive, social preview metadata, responsive markup, sitemap, and `ProfessionalService` structured data. [1] [2] | Search engines can currently discover only one principal content URL from the sitemap. [3] | Build a small, deliberate page architecture rather than publishing volume content. |
| **Mobile and resilience** | The navigation’s mobile layout is compact and coherent, and the page is responsive. | The hero uses a loader and animation gate; core content should remain visible even if animation, fonts, or scripts are delayed. | Treat the motion as progressive enhancement, not as a prerequisite for seeing the value proposition. [5] |
| **Delivery** | The live page is served over HTTPS and gzip; the supplied local images are compact WebP assets. | The loader, Google Analytics, and embedded LinkedIn badge are the most obvious delivery/third-party dependencies in the source. | Validate actual mobile Core Web Vitals in the owner’s accounts after streamlining the opening sequence. [6] |

## Aesthetic enhancement plan

### 1. Protect the visual concept, but simplify the first decision

The homepage’s first screen should answer four visitor questions without making them scroll or wait: **What do you do? Who do you help? Where are you? What should I do next?** The current brand display is elegant, but the visible `H1` is only “North Point”; the useful proposition appears in supporting copy. Keep the large wordmark as a visual element, but use a descriptive, visibly rendered headline such as:

> **Web design studio in Liverpool for businesses that want to be taken seriously.**

The body copy can then retain the current voice while becoming slightly more concrete:

> **Strategy, design and hand-built websites for Liverpool businesses and UK teams. Fixed project quotes within 24 hours.**

This protects the mood while reducing cognitive work. The primary CTA should become more specific, for example **“Get a fixed project quote”**, with the current 24-hour response reassurance directly beneath it. “Request a quote” is serviceable, but the stronger phrasing makes the outcome feel tangible.

### 2. Shorten or remove the full-screen loader

The existing loader is visually on-brand, and a brief mark animation could remain. However, the page begins with `body.loading` and holds the cover animation until the loader sequence releases. The script intentionally allows a minimum 1.9-second dwell and a failsafe of up to 5 seconds. A prospective client should not have to wait to see the service, particularly on a phone or under imperfect network conditions.

Use one of these approaches, in descending order of preference:

| Option | Visual effect | Commercial and technical benefit |
|---|---|---|
| **Progressive enhancement** | The hero is visible at once; text and compass receive a subtle entrance afterward. | The essential content remains available if JavaScript, fonts, or motion fail or are delayed. |
| **Very short opening mark** | Retains a 300–600 ms signature flourish. | Preserves ritual without pushing the CTA below a wait state. |
| **Keep the current loader only for repeat visits off** | First-time visit gets immediate content; a brief animation can be used on navigation or hover. | Reduces friction at the highest-value moment in the funnel. |

This is not merely aesthetic. Google’s mobile-first guidance emphasizes that primary content must be accessible and renderable on the mobile page, while its page-experience guidance encourages an overall usable experience rather than a single metric chase. [5] [6]

### 3. Increase the hierarchy gap between display typography and functional typography

The Fraunces/Jost pairing is excellent. The opportunity is to keep Fraunces dramatic while making Jost more effortless to consume. In practice, this means increasing the smallest navigation, eyebrow, price-feature, metadata, and paragraph treatments by approximately one step; widening line-height slightly in dense dark sections; and avoiding long feature rows that rely on fine uppercase labels.

The palette itself is not the problem: the major foreground/background combinations in the source provide strong measured contrast. The improvement is **scanability**, not a wholesale colour change. Use fewer all-caps micro-labels, shorten sentences in the “Method” and “Process” sections, and introduce a little more vertical separation between each idea. The site will remain sophisticated while becoming easier to use at speed.

### 4. Make proof more prominent than self-description

The “Human Made, AI Built” section is transparent and differentiating. It should remain, but it currently receives more explanatory space than client outcomes. Rebalance the page so that the selected work and real-world proof earn at least as much visual authority as the production philosophy.

For each work tile, add one compact, substantiated outcome line beside the existing **Type** and **Status** labels. Examples include “Launched a new direct-to-consumer store,” “Created a resource hub for schools,” “Improved clarity for referral partners,” or a quantified result where the client permits it. Add a one-sentence client endorsement or testimonial beneath the most relevant two projects. This will reinforce the existing premium gallery treatment without turning it into a noisy agency grid.

### 5. Refine the price list for decision-making, not merely presentation

The pricing section feels unusually transparent and should be kept. Its large price figures and “Best Value” marker work well. The supporting package inclusions should become easier to compare, especially on mobile. Give each tier a one-sentence fit statement before its feature list, then stack the inclusions on narrow screens.

| Package | Suggested fit statement |
|---|---|
| **Basic Website** | For a new business that needs a credible, conversion-ready starting point. |
| **Standard Website** | For a growing service business that needs clearer pages, proof, and room to sell. |
| **Premium Website** | For a more established brand that needs deeper content, richer layouts, and an SEO-ready foundation. |
| **Care Plan** | For clients who want one trusted point of contact after launch. |

A small “What is not included?” disclosure next to the feature list will also prevent poor-fit enquiries without making the price list feel defensive.

### 6. Keep motion as texture, not a test of patience

The lamp-following portfolio interaction and subtle parallax are more distinctive than most agency-site effects. Retain them. The practical change is to cap motion to elements that reward exploration, while allowing the page structure and core content to stand silently on their own. The LinkedIn profile badge in the footer is a mismatched third-party visual element; replacing it with a simple text link or custom icon link will make the footer feel more finished and remove one external widget dependency.

## SEO roadmap

### What is already correct

The technical starting point is good for a single-page studio site. The homepage uses the canonical URL `https://northpointcreative.co.uk/`, a descriptive title and meta description, index/follow robots instructions, Open Graph/Twitter preview data, responsive viewport markup, image alt text, a root `robots.txt`, and a root sitemap. It also contains a `ProfessionalService` JSON-LD entity with the studio name, founder, Liverpool locality, UK service area, email, offer catalogue, and pricing. [1] [2] [3]

The recommended SEO work is therefore **not** keyword stuffing, duplicate landing pages, or a generic blog. It is creating useful pages that capture the genuine expertise already demonstrated in the portfolio and answer real pre-enquiry questions. Google’s current documentation explicitly prioritizes original, people-first, useful content and encourages clear authorship and firsthand expertise. [4]

### The primary SEO constraint: one-page discoverability

The current sitemap lists only the homepage. That is appropriate for the present build but restricts the site to a single indexable URL for search intent coverage. A person searching for “web design Liverpool,” “website designer Liverpool,” “website design packages,” “small business website design,” or a named client project has little chance to land on a page built for that exact need. [3]

Build the following small architecture over time. Each page should contain genuinely different information, a clear purpose, original examples, and its own carefully written title/description—not copied variations of the homepage.

| Suggested page | User intent it should serve | Essential original content |
|---|---|---|
| **`/web-design-liverpool/`** | Someone looking for a local studio. | Local relevance, who you work with, what a project includes, portfolio links, contact path, and accurate service-area wording. |
| **`/web-development/`** | Someone comparing a custom build with a template or builder. | Your approach to custom code, ownership, performance, accessibility, handover, and relevant work. |
| **`/website-design-prices/`** | Someone who needs clarity before enquiring. | The current package information in a more scannable format, fit guidance, timelines, exclusions, and common questions. |
| **`/work/dr-shrooms/`**, etc. | Someone assessing credibility or finding a project by name. | Client context, problem, scope, approach, visual decisions, launch, outcome, and a client quote when permitted. |
| **`/about/`** | Someone assessing the founder and studio. | Dan’s background, working principles, why the model is hands-on, process, and direct contact details. |
| **`/care-plan/`** | A client comparing ongoing support options. | Exact service boundaries, response expectations, types of updates, and who benefits. |

Start with **the Liverpool service page, the pricing page, and two case studies**. That is enough to create meaningful depth without spreading the studio too thin.

### Improve the homepage’s semantic relevance without losing its aesthetic

The current `H1` is the brand name. Brand-led headings can be beautiful, but they leave the topical meaning to supporting text. The best solution is not hidden text. Instead, make the meaningful service phrase visible in the hero and give it the `H1` role, while retaining “North Point Creative” as the visual masthead or brand display. A useful title template for the homepage would be:

> **Web Design Studio in Liverpool | North Point Creative**

A suitable meta description could be:

> **North Point Creative is a Liverpool web design studio creating custom, conversion-focused websites for businesses across the UK. Fixed project quotes within 24 hours.**

Keep titles and descriptions specific to each new page. They should summarize the page accurately rather than target an arbitrary word count. Google advises using descriptive, helpful titles and people-first content rather than material created mainly to chase search visits. [4] [7]

### Turn the portfolio into evidence-led case studies

The four existing project previews are an ideal SEO asset because they demonstrate firsthand experience. Each dedicated case study should include a short brief, constraints, user or business problem, the design/build decisions, the work delivered, and the outcome. Include links to the live project with an appropriate disclosure if the client has since changed the site.

Avoid manufacturing performance claims. If a result is not measurable, describe the tangible outcome: a new enquiry route, a better resource structure, easier content management, an approved launch, a clearer positioning, or a more credible digital presence. This type of original material aligns more naturally with the experience and expertise signals Google asks site owners to demonstrate. [4]

### Expand structured data cautiously and accurately

The existing `ProfessionalService` JSON-LD is a good foundation. Do not add schema simply because a property exists in Schema.org. Google advises that structured data should describe visible page content, be complete and accurate, and be validated after deployment. [8]

The practical next step is an `@graph` that connects the organisation/business entity, the `WebSite`, and a `Person` entity for Dan. Add only verified public details: an official telephone number if one exists, an exact public business address only if it is suitable to publish, a `sameAs` link to the real LinkedIn profile, and opening hours only if they are stable and client-facing. Individual service and case-study pages can then carry page-specific `Service` or `CreativeWork` information that matches their visible content.

### Complete the small technical housekeeping items

| Item | Current observation | Recommended action |
|---|---|---|
| **Sitemap `lastmod`** | The sitemap records 11 July 2026 while the live homepage response reports a later modification on 15 July 2026. | Update `lastmod` on material changes only, and automate it once the site has multiple pages. |
| **Sitemap optional fields** | The file includes `changefreq` and `priority`. | Remove them unless another search engine requires them; Google documents that it ignores both. [9] |
| **Sitemap coverage** | Only the homepage is listed. | Add every canonical, indexable service, work, pricing, and about page when published. [9] |
| **Search Console** | No owner-account data was available for this audit. | Verify the domain, submit the sitemap, inspect the homepage and new pages, then monitor queries, indexing, and Core Web Vitals. |
| **Performance validation** | A public third-party API report was unavailable during this review, so no lab score is asserted. | After the loader change, check mobile performance in the owner’s PageSpeed Insights and Search Console accounts. |

## Phased implementation sequence

| Window | Focus | Completion standard |
|---|---|---|
| **First 1–2 weeks** | Make the hero instantly resilient, shorten or remove the full-screen loader, clarify the visible `H1` and primary CTA, improve functional type sizing, and simplify the LinkedIn footer treatment. | A first-time mobile visitor can understand the service, local relevance, proof, and next action immediately—without waiting for a sequence. |
| **Weeks 3–6** | Publish the Liverpool service page, pricing page, two detailed work pages, and a proper About page; update internal links and sitemap. | Each page has unique intent, visible expertise, a contextual CTA, a distinct title/description, and a canonical URL. |
| **Weeks 6–10** | Improve business/schema entities, add client testimonials where approved, build the remaining work and Care Plan pages, and establish reporting. | Search Console shows all intended pages discovered and indexed; reporting is based on impressions, queries, clicks, and enquiry quality. |
| **Ongoing** | Publish evidence, not filler: meaningful case studies, project launches, or answers to recurring client questions. | New content is tied to genuine work, visible experience, and a clear prospective-client need. |

## What I would deliberately avoid

Do not flatten the site into a conventional blue-and-white agency layout. Do not replace the editorial gallery, warm material palette, or quiet confidence that currently differentiates the brand. Do not add a wide, generic blog simply to create URLs. Do not hide keyword-heavy copy or use schema that is not represented on the page. These approaches would weaken the site’s strongest quality—its clear point of view—without solving the actual discoverability gap.

## Recommended next decision

The highest-value next step is a **light homepage refinement plus a five-page content architecture**, not a full redesign. The homepage should retain its current world, but reveal the commercial proposition earlier and make core content immediately available. The new pages should build on the existing visual language and turn the portfolio into proof that can rank, reassure, and convert.

## References

[1]: https://northpointcreative.co.uk/ "North Point Creative — live homepage"
[2]: https://northpointcreative.co.uk/robots.txt "North Point Creative robots.txt"
[3]: https://northpointcreative.co.uk/sitemap.xml "North Point Creative XML sitemap"
[4]: https://developers.google.com/search/docs/fundamentals/creating-helpful-content "Google Search Central: Creating helpful, reliable, people-first content"
[5]: https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing "Google Search Central: Mobile site and mobile-first indexing best practices"
[6]: https://developers.google.com/search/docs/appearance/page-experience "Google Search Central: Understanding page experience in Google Search results"
[7]: https://developers.google.com/search/docs/appearance/title-link "Google Search Central: Influencing title links in search results"
[8]: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data "Google Search Central: Introduction to structured data markup"
[9]: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap "Google Search Central: Build and submit a sitemap"

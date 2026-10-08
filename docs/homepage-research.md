# Homepage research sections

The site retains the original Wowchemy theme, blue, fonts, and all original information.
Biography and opportunity text live in `content/authors/admin/_index.md`.
The public research narrative lives at `content/research/index.md`; it uses current
manuscript statuses instead of publishing the older application statement PDF.

`data/research_publications.json` controls selected order, published/manuscript groups,
takeaways, personal contributions, reviewer-rating disclosures and paper recognition.
All Publications includes every native publication, including the antithetic
manuscript at `content/publication/antithetic/`. Its former project URL redirects
to the publication page; its existing slides URL remains unchanged. The listing
date is page metadata, while the publication status is "Submitted to AISTATS".
Submission labels use venue abbreviations without a conference year or a redundant
preprint year. Published papers retain their venue years; the IEEE TIT manuscript
retains its revised-after-R&R status, and work in preparation is labeled separately.
Authors, summaries, abstracts, images, and resources remain in native content pages.
Author lists retain their original order and highlight Zhankun. The website omits
equal-contribution markers at the owner's request; original paper PDFs remain intact.
The antithetic paper's native title and author list are also used in the homepage
listings. Its `author_order_note` is shown beneath the authors on listings and the
publication page to explain the alphabetical-by-surname convention, without implying
equal contribution or contribution-ranked authorship.
The page_links partial adds an optional `url_project_label` without changing URLs.

Each manuscript uses a native publication folder under `content/publication/`.
The `distributed_alm/` and `federated_switch_vr/` folders each contain `index.md`
with full ordered authors, submission status, abstract, and summary, plus `cite.bib`
with an unpublished-manuscript citation. Their titles in Selected and All Publications
link to individual publication pages, where the full abstracts and Cite buttons appear.
Summaries describe the work without assigning unconfirmed personal contributions.
Private OpenReview URLs are omitted, and resource fields remain empty until public
manuscripts or code are available. No placeholder PDFs or figures are published.

News is in `content/home/news.md`, with upcoming travel kept separate from completed
events. UAI June 2026 and CVPRW April 2022 acceptance months use the linked official
notification schedules. Selected presentations are in `content/home/presentations.md`.
MMLS participation has no confirmed matching poster file, so only its event is linked.
ETIE mentoring is undated in Services because the CV provides no dates.

The original summaries remain available in disclosures. ICML has a separate
plain-language explanation and figure below its unchanged abstract. Smart Ladle
recognition is attributed to the coauthored paper, with the Hunt-Kelly third place
distinguished from its 2021 technology best-paper award. Editorial corrections retain
old filenames and URLs. The original backgrounds below the new presentations section
are preserved explicitly in the scoped custom stylesheet.

The blue ZL source is `assets/images/zl-monogram.svg` / `assets/images/icon.png`.
Stable public icons: `/favicon.png` (96px), `/favicon-32x32.png`, `/favicon.ico`
(16–256px), `/apple-touch-icon.png` (180px). `custom_head.html` advertises them in
addition to the theme's generated blue icons. Keep these public URLs stable.
Google must recrawl the homepage and favicon before its search result can refresh;
deployment does not control the search cache. No robots restrictions are added.

Netlify continues using the pinned Hugo 0.80 build and the existing master branch.


## Research cards and posts

Three compact cards in the biography use `data/research_themes.json` and the
`research-themes` shortcode. They link to actual selected/all-publication anchors;
the existing bibliography remains in rows. No JavaScript fetch is needed.

The middle card groups variance reduction and stochastic optimization, including
state-dependent heavy-tailed noise. Its related-work labels omit manuscript-status
suffixes; publication listings and pages retain their status labels. The research
overview describes the heavy-tailed work as ongoing and preserves its section's
previous anchor for shared links.

The original Posts pages widget, compact listing, and navigation anchor are restored.
All four original posts remain in the homepage section and at `/post/`, which also
links to the earlier personal blog. `/notes/` redirects to `/post/` for existing links.
Course material appears in the existing Courses section; all 14 collections and their
original references remain unchanged.

Optional `url_note` links remain supported on publications and projects, but none are
currently set. The three standalone research notes were removed at the owner's request.
The original ICML explanation and figure remain directly on the publication page.

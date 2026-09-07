# Homepage research sections

The site retains the original Wowchemy theme, blue, fonts, and all original information.
Biography and opportunity text live in `content/authors/admin/_index.md`.
The public research narrative lives at `content/research/index.md`; it uses current
manuscript statuses instead of publishing the older application statement PDF.

`data/research_publications.json` controls selected order, published/manuscript groups,
takeaways, personal contributions, reviewer-rating disclosures and paper recognition.
All Publications includes every native publication plus the antithetic project.
Authors, summaries, abstracts, images, and resources remain in native content pages.
Author lists retain their original order and highlight Zhankun. The website omits
equal-contribution markers at the owner's request; original paper PDFs remain intact.
The page_links partial adds an optional `url_project_label` without changing URLs.

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


## Research cards and notes

Three compact cards in the biography use `data/research_themes.json` and the
`research-themes` shortcode. They link to actual selected/all-publication anchors;
the existing bibliography remains in rows. No JavaScript fetch is needed.

The Posts navigation anchor is unchanged. Its `research_notes` widget presents
selected course collections and expandable earlier writing. Research-note headings
appear only when research notes are present.
`/notes/` is the complete categorized archive; `/post/` and all old post URLs remain.
All 14 original course pages and four original posts are retained. Course collections
include third-party references with their existing attribution; they are not relabeled
as original research. Earlier month-only dates are displayed without inventing a day.

To publish a research note, add `content/post/<slug>/index.md` with a real publication
date, `writing_kind: research`, title, short summary, author, and topic tags. The note
automatically appears in the archive; the homepage shows the latest three research notes. Keep the distinction between
an illustrative example and a reported result, and link the source paper.

Set `url_note` on the related publication or project to show its Research note button.
It may point to a local article or a public external note such as a Notion page.
Only existing notes get buttons. The three standalone research notes were removed
at the owner's request. The original ICML explanation and figure remain directly
on the publication page, preserving its existing anchor.

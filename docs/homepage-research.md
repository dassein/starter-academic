# Homepage research sections

The homepage keeps the existing Wowchemy theme, fonts, primary blue, and content.
Biography is maintained in `content/authors/admin/_index.md`; full background uses
a native details disclosure. CV navigation is in `config/_default/menus.toml`.

Selected and all-publication sections use the local `research_publications` widget.
Edit `data/research_publications.json` to change selected order, status labels,
contribution sentences, or antithetic manuscript metadata. Existing publication
pages remain the source of their titles, authors, summaries, images and resource
buttons. All Publications automatically includes every publication page plus the
antithetic project. The antithetic project page and its original content are intact.

News is maintained in `content/home/news.md`. UAI's June 2026 and CVPRW's April 2022
acceptance months are inferred from linked official notification schedules.
TMLR was accepted December 2025 and published January 2026. The 2021 AIST award
entry uses the documented November 2020 notification. NeurIPS 2025 attendance in
San Diego and its travel grant are separate from planned 2026 attendance.

Styles in `assets/scss/custom.scss` apply only to the biography, news and publication
sections. The original Projects, Services, Posts, Courses and Contact remain intact.
Experience adds only the two YouTube links supplied in the CV. No preview-only
URL rewriting, no-index metadata, React stack, or Sites deployment configuration
is included. Netlify continues to use the existing pinned Hugo 0.80 build.

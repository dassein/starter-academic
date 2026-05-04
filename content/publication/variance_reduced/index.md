---
title: "Unified High-Probability Analysis of Stochastic Variance-Reduced Estimation"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- Zhankun Luo
- Antesh Upadhyay
- Mehmet Berk Sahin
- Sang Bin Moon
- Anuran Makur
- Abolfazl Hashemi

# Author notes (optional)
# author_notes:
# - "Equal contribution"
# - "Equal contribution"

date: "2026-05-01T00:00:00Z"
# url_preprint: https://arxiv.org/pdf/2205.03947.pdf
doi: "" # "https://doi.org/10.1109/CVPRW56347.2022.00174" # "https://doi.org/10.48550/arXiv.2205.03947"

# Schedule page publish date (NOT publication's date).
publishDate: "2026-04-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: Submitted to *Conference on Neural Information Processing Systems (NeurIPS)*
# In preparation
publication_short: Submitted to *NeurIPS*
# In preparation
abstract: | 
  Stochastic estimators are fundamental to large-scale optimization, where population quantities must be inferred from noisy oracle observations. Although influential methods such as momentum, SPIDER, STORM, and PAGE have been highly successful, their analyses are largely estimator-specific and expectation-based, obscuring the structural tradeoffs that determine reliability. In this paper, we develop a unified framework for stochastic variance-reduced estimation based on a recursion with three components: memory retention, reset probability, and a correction term for iterate movement. This framework recovers several classical estimators, motivates new second-order variants, and yields a bias-variance decomposition of estimation error. Our main result is a unified high-probability bound proved using a new dimension-free vector-valued Freedman inequality, valid for smooth normed spaces involving random sums of vector martingales. The result applies in both Euclidean and non-Euclidean settings, including the analysis of mirror-descent-based methods in Banach spaces. As applications, we obtain high-probability oracle complexities for unconstrained optimization with mirror descent, establishing the logarithmic dependence on the confidence level. We also derive the first $\tilde{\mathcal{O}}(\varepsilon^{-3})$ oracle-complexity bounds for stochastic optimization with expectation constraints, improving upon the existing $\mathcal{O}(\varepsilon^{-4})$ complexity by leveraging variance-reduced estimation for the first time in this setting.

# Summary. An optional shortened abstract.
summary: | 
  We present a unified variance-reduction framework and a novel Freedman inequality that establishes sharp logarithmic confidence dependence for unconstrained optimization with mirror descent in Banach spaces.
  We also improve the oracle complexity from $\mathcal{O}(\varepsilon^{-4})$ to $\tilde{\mathcal{O}}(\varepsilon^{-3})$ by integrating variance reduction into the expectation-constrained setting.
tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_preprint: '' #'https://arxiv.org/abs/2603.05774'
url_pdf: '' # 'publication/softmax_switchgd/arxiv_softmax_switchgd.pdf'
url_code: '' # 'https://github.com/dassein/cycloid_em_mlr'
url_dataset: ''
# url_poster: 'publication/smart_ladle/Poster_Zhankun_Luo.pdf'
url_project: '' # 'https://icml.cc/virtual/2024/poster/33762' # 'https://engineering.purdue.edu/~sorghum/'
# url_slides: 'publication/smart_ladle/intro_senior_design.pdf'
url_source: '' # 'https://openaccess.thecvf.com/content/CVPR2022W/AgriVision/html/Cai_High-Resolution_UAV_Image_Generation_for_Sorghum_Panicle_Detection_CVPRW_2022_paper.html'
url_video: '' # "https://www.youtube.com/watch?v=nl2x2SE4PnU&list=PLPtQK8rJZ9HzX9kzDPRf2mc0L7NcOsNzP&index=10" # 'https://www.youtube.com/watch?v=nl2x2SE4PnU'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: '' # '[](publication/variance_reduced/featured.png)' # 'Image credit: [**Unsplash**](publication/multi_ransac1/featured.png)'
  # focal_point: "" # put png on top
  focal_point: Smart # put png on right
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

---
title: "Connecting Score Matching, Maximum Likelihood, and Expectation-Maximization in Mixed Linear Regression"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- Zhankun Luo
- Abolfazl Hashemi

# Author notes (optional)
# author_notes:
# - "Equal contribution"
# - "Equal contribution"

date: "2026-09-01T00:00:00Z"
# url_preprint: https://arxiv.org/pdf/2205.03947.pdf
doi: "" # "https://doi.org/10.1109/CVPRW56347.2022.00174" # "https://doi.org/10.48550/arXiv.2205.03947"

# Schedule page publish date (NOT publication's date).
publishDate: "2026-09-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: Submitted to *Transactions on Machine Learning Research(TMLR)*
# In preparation
publication_short: Submitted to *TMLR*
# In preparation
abstract: | 
  We study variance-preserving diffusion of the response in mixed linear regression (MLR) with unknown mixing weights. Our analysis separates the statistical guarantees of score matching from the loss geometry and optimization signal at a fixed diffusion noise level. The KL divergence links the denoising score matching objective integrated over the diffusion path with the likelihood and a terminal discrepancy. Under mild regularity conditions and terminal schedule, the resulting estimator converges up to the ground truth parameters of MLR, and its scaled error converges to the Gaussian limit of the maximum-likelihood estimator. At a fixed scale of the diffusion noise level, we derive a decomposition linking the score matching loss to cross-entropy and Expectation-Maximization (EM) operators. This decomposition yields an EM-related low-noise gradient expansion with additional correction terms of latent variance. In the high-noise limit, we further characterize gradient descent on this limiting loss under isotropic covariance. Along fixed high signal-to-noise ratio rays, the score matching imbalance gradient and the latent-variance term tend to zero pointwise. Numerical experiments illustrate our theoretical findings and statistical guarantees.

# Summary. An optional shortened abstract.
summary: | 
  We connect score matching, maximum likelihood, and expectation-maximization in mixed linear regression with unknown mixing weights. Score matching integrated over the diffusion path consistently recovers model parameters matches the asymptotic distribution of maximum likelihood. At a fixed noise level, exact decompositions relate the loss and its gradients to EM operators and latent variance. We further characterize optimization dynamics in the high-noise limit and establish pointwise blindness to mixing imbalance as the ground-truth signal grows along a fixed direction. Numerical experiments illustrate our theoretical findings.
tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_preprint: 'publication/diffusion_2mlr/TMLR_diffusion_2MLR_arxiv.pdf'
url_pdf: 'publication/diffusion_2mlr/TMLR_diffusion_2MLR_arxiv.pdf'
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

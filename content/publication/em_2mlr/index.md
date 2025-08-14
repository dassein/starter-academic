---
title: "Unveiling the Cycloid Trajectory of EM Iterations in Mixed Linear Regression"

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

date: "2024-01-19T00:00:00Z"
# url_preprint: https://arxiv.org/pdf/2205.03947.pdf
doi: "" # "https://doi.org/10.1109/CVPRW56347.2022.00174" # "https://doi.org/10.48550/arXiv.2205.03947"

# Schedule page publish date (NOT publication's date).
publishDate: "2024-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: Accepted by *International Conference on Machine Learning (ICML)*
publication_short: Accepted by *ICML*

abstract: We study the trajectory of iterations and the convergence rates of the Expectation-Maximization (EM) algorithm for two-component Mixed Linear Regression (2MLR). The fundamental goal of MLR is to learn the regression models from unlabeled observations. The EM algorithm finds extensive applications in solving the mixture of linear regressions. Recent results have established the super-linear convergence of EM for 2MLR in the noiseless and high SNR settings under some assumptions and its global convergence rate with random initialization has been affirmed. However, the exponent of convergence has not been theoretically estimated and the geometric properties of the trajectory of EM iterations are not well-understood. In this paper, first, using Bessel functions we provide explicit closed-form expressions for the EM updates under all SNR regimes. Then, in the noiseless setting, we completely characterize the behavior of EM iterations by deriving a recurrence relation at the population level and notably show that all the iterations lie on a certain cycloid. Based on this new trajectory-based analysis, we exhibit the theoretical estimate for the exponent of super-linear convergence and further improve the statistical error bound at the finite-sample level. Our analysis provides a new framework for studying the behavior of EM for Mixed Linear Regression.

# Summary. An optional shortened abstract.
summary: In this paper, we derived closed-form expressions for the EM updates in the 2MLR problem. Notably, in the noiseless setting  we first showed and then analyzed the cycloid trajectory of EM updates. Additionally, we demonstrated the quadratic convergence rate for regression parameters, which is independent of mixing weights. We emphasized that errors in mixing weights primarily arise from the angle formed between true and estimated regression parameters. Finally, we conducted a detailed analysis of the statistical errors in the estimation of regression parameters and mixing weights.

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_preprint: 'https://arxiv.org/pdf/2405.18237'
url_pdf: '' # 'publication/panicle/Zhankun_CVPRW2022.pdf'
url_code: 'https://github.com/dassein/cycloid_em_mlr'
url_dataset: ''
# url_poster: 'publication/smart_ladle/Poster_Zhankun_Luo.pdf'
url_project: 'https://icml.cc/virtual/2024/poster/33762' # 'https://engineering.purdue.edu/~sorghum/'
# url_slides: 'publication/smart_ladle/intro_senior_design.pdf'
url_source: '' # 'https://openaccess.thecvf.com/content/CVPR2022W/AgriVision/html/Cai_High-Resolution_UAV_Image_Generation_for_Sorghum_Panicle_Detection_CVPRW_2022_paper.html'
url_video: '' # "https://www.youtube.com/watch?v=nl2x2SE4PnU&list=PLPtQK8rJZ9HzX9kzDPRf2mc0L7NcOsNzP&index=10" # 'https://www.youtube.com/watch?v=nl2x2SE4PnU'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: '[](publication/em_2mlr/featured.png)' # 'Image credit: [**Unsplash**](publication/multi_ransac1/featured.png)'
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

---
title: "First-Order Softmax Weighted Switching Gradient Method for Distributed Stochastic Minimax Optimization with Stochastic Constraints"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- Zhankun Luo
- Antesh Upadhyay
- Sang Bin Moon
- Abolfazl Hashemi

# Author notes (optional)
# author_notes:
# - "Equal contribution"
# - "Equal contribution"

date: "2026-01-19T00:00:00Z"
# url_preprint: https://arxiv.org/pdf/2205.03947.pdf
doi: "" # "https://doi.org/10.1109/CVPRW56347.2022.00174" # "https://doi.org/10.48550/arXiv.2205.03947"

# Schedule page publish date (NOT publication's date).
publishDate: "2026-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: Submitted to *Conference on Uncertainty in Artificial Intelligence (UAI)*
publication_short: Submitted to *UAI*

abstract: | 
  This paper addresses the distributed stochastic minimax optimization problem subject to stochastic constraints. We propose a novel first-order Softmax-Weighted Switching Gradient method tailored for federated learning. Under full client participation, our algorithm achieves the standard oracle complexity to satisfy a unified bound $\epsilon$ for both the optimality gap and feasibility tolerance. We extend our theoretical analysis to the practical partial participation regime by quantifying client sampling noise through a stochastic superiority assumption. Furthermore, by relaxing standard boundedness assumptions on the objective functions, we establish a strictly tighter lower bound for the softmax hyperparameter. We provide a unified error decomposition and establish a sharp high-probability convergence guarantee. Ultimately, our framework demonstrates that a single-loop primal-only switching mechanism provides a stable alternative for optimizing worst-case client performance, effectively bypassing the hyperparameter sensitivity and convergence oscillations often encountered in traditional primal-dual or penalty-based approaches. We verify the efficacy of our algorithm via experiment on the Neyman-Pearson (NP) classification and fair classification tasks.

# Summary. An optional shortened abstract.
summary: | 
  This research introduces a novel Softmax-Weighted Switching Gradient method to address distributed stochastic minimax optimization with stochastic constraints in federated learning environments. By utilizing a single-loop, primal-only switching mechanism, the approach provides a stable alternative for optimizing worst-case client performance without relying on complex dual variables. The work establishes robust convergence guarantees for both full and partial client participation by relaxing standard boundedness assumptions. The analysis culminates in a unified error decomposition that provides a remarkably sharp logarithmic high-probability convergence guarantee for these constrained problems.
tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_preprint: '' # 'https://arxiv.org/pdf/2405.18237'
url_pdf: 'publication/softmax_switchgd/arxiv_softmax_switchgd.pdf'
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
  caption: '[](publication/softmax_switchgd/featured.png)' # 'Image credit: [**Unsplash**](publication/multi_ransac1/featured.png)'
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

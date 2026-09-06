---
title: "Structural Properties, Cycloid Trajectories and Non-Asymptotic Guarantees of EM Algorithm for Mixed Linear Regression"

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

date: "2025-01-19T00:00:00Z"
# url_preprint: https://arxiv.org/pdf/2205.03947.pdf
doi: "" # "https://doi.org/10.1109/CVPRW56347.2022.00174" # "https://doi.org/10.48550/arXiv.2205.03947"

# Schedule page publish date (NOT publication's date).
publishDate: "2025-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: Submitted to *IEEE Transactions on Information Theory (IT)*
publication_short: Submitted to *IT*

abstract: | 
  This work investigates the structural properties, cycloid trajectories, and non-asymptotic convergence guarantees of the Expectation-Maximization (EM) algorithm for two-component Mixed Linear Regression (2MLR) with unknown mixing weights and regression parameters.
  Recent studies have established global convergence for 2MLR with known balanced weights and super-linear convergence in noiseless and high signal-to-noise ratio (SNR) regimes.
  However, the theoretical behavior of EM in the fully unknown setting remains unclear, with its trajectory and convergence order not yet fully characterized.
  We derive explicit EM update expressions for 2MLR with unknown mixing weights and regression parameters across all SNR regimes and analyze their structural properties and cycloid trajectories.
  In the noiseless case, we prove that the trajectory of the regression parameters in EM iterations traces a cycloid by establishing a recurrence relation for the sub-optimality angle, while in high SNR regimes we quantify its discrepancy from the cycloid trajectory.
  The trajectory-based analysis reveals the order of convergence: linear when the EM estimate is nearly orthogonal to the ground truth, and quadratic when the angle between the estimate and ground truth is small at the population level.
  Our analysis establishes non-asymptotic guarantees by sharpening bounds on statistical errors between finite-sample and population EM updates, relating EM's statistical accuracy to the sub-optimality angle, and proving convergence with arbitrary initialization at the finite-sample level.
  This work provides a novel trajectory-based framework for analyzing EM in Mixed Linear Regression.


# Summary. An optional shortened abstract.
  # In this paper, we derive explicit expressions for the EM updates in the two-component Mixed Linear Regression (2MLR) model
  # with unknown mixing weights and regression parameters across all SNR regimes.
  # We then characterize the properties of EM updates based on the explicit expressions, establishing their structural behavior and boundedness, 
  # and showing that in the noiseless setting, they follow a cycloid trajectory derived via a recurrence relation for the sub-optimality angle.
  # In finite high-SNR regimes, we further bound the deviation of the EM updates from this cycloid trajectory.
  # At the population level, the trajectory-based analysis reveals the order of convergence: linear convergence when the EM estimate is nearly orthogonal to the ground truth regression parameters, 
  # and quadratic convergence when the angle between the estimate and the ground truth is small.
  # Furthermore, our work provides a novel trajectory-based framework that establishes non-asymptotic guarantees by tightening bounds of the statistical errors between the finite-sample and population EM updates, 
  # revealing the connection between EM's statistical accuracy and the sub-optimality angle, 
  # and establishing convergence guarantees with arbitrary initialization at the finite-sample level.
summary: | 
  We derive explicit EM updates for the 2MLR model across all SNR regimes and characterize their properties. We show the updates follow a cycloid trajectory in the noiseless setting and bound the deviation from this trajectory in finite high-SNR regimes. This trajectory-based analysis reveals the population-level convergence orders: linear when near-orthogonal and quadratic when the angle is small. Our novel framework provides non-asymptotic guarantees by tightening statistical error bounds between finite-sample and population updates, linking statistical accuracy to the sub-optimality angle and establishing finite-sample convergence from arbitrary initialization.

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_preprint: 'https://arxiv.org/abs/2511.04937' # 'https://arxiv.org/pdf/2405.18237'
url_pdf: 'https://arxiv.org/pdf/2511.04937' # 'publication/panicle/Zhankun_CVPRW2022.pdf'
url_code: 'https://github.com/dassein/cycloid_em_tit' # 'https://github.com/dassein/cycloid_em_mlr'
url_dataset: ''
# url_poster: 'publication/smart_ladle/Poster_Zhankun_Luo.pdf'
url_project: '' # 'https://icml.cc/virtual/2024/poster/33762' # 'https://engineering.purdue.edu/~sorghum/'
# url_slides: 'publication/smart_ladle/intro_senior_design.pdf'
url_source: '' # 'https://openaccess.thecvf.com/content/CVPR2022W/AgriVision/html/Cai_High-Resolution_UAV_Image_Generation_for_Sorghum_Panicle_Detection_CVPRW_2022_paper.html'
url_video: '' # "https://www.youtube.com/watch?v=nl2x2SE4PnU&list=PLPtQK8rJZ9HzX9kzDPRf2mc0L7NcOsNzP&index=10" # 'https://www.youtube.com/watch?v=nl2x2SE4PnU'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: '[Figure](/publication/em_2mlr_structural/featured.png)' # 'Image credit: [**Unsplash**](publication/multi_ransac1/featured.png)'
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


## My contribution

I extended the trajectory analysis to jointly unknown regression parameters and mixing weights, including population convergence and finite-sample guarantees.

---
title: "Characterizing Evolution in Expectation-Maximization Estimates for Overspecified Mixed Linear Regression "

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
publication: Submitted to *Transactions on Machine Learning Research (TMLR)*
publication_short: Submitted to *TMLR*

abstract: Estimating data distributions using parametric families is crucial in many learning setups, serving both as a standalone problem and an intermediate objective for downstream tasks. Mixture models, in particular, have attracted significant attention due to their practical effectiveness and comprehensive theoretical foundations. A persisting challenge is model misspecification, which occurs when the model to be fitted has more mixture components than those in the data distribution. In this paper, we develop a theoretical understanding of the Expectation-Maximization (EM) algorithm's behavior in the context of targeted model misspecification for overspecified two-component Mixed Linear Regression (2MLR) with unknown $d$-dimensional regression parameters and mixing weights. In Theorem 5.1 at the population level, with an unbalanced initial guess for mixing weights, we establish linear convergence of regression parameters in $\mathcal{O}(\log (1/\epsilon))$ steps. Conversely, with a balanced initial guess for mixing weights, we observe sublinear convergence in $\mathcal{O}(\epsilon^{-2})$ steps to achieve the $\epsilon$-accuracy at Euclidean distance. In Theorem 6.1 at the finite-sample level, for mixtures with sufficiently unbalanced fixed mixing weights, we demonstrate a statistical accuracy of $\mathcal{O}((d/n)^{1/2})$, whereas for those with sufficiently balanced fixed mixing weights, the accuracy is $\mathcal{O}((d/n)^{1/4})$ given $n$ data samples. Furthermore, we underscore the connection between our population level and finite-sample level results: by setting the desired final accuracy $\epsilon$ in Theorem 5.1 to match that in Theorem 6.1 at the finite-sample level, namely letting $\epsilon = \mathcal{O}((d/n)^{1/2})$ for sufficiently unbalanced fixed mixing weights and $\epsilon = \mathcal{O}((d/n)^{1/4})$ for sufficiently balanced fixed mixing weights, we intuitively derive iteration complexity bounds $\mathcal{O}(\log (1/\epsilon))=\mathcal{O}(\log (n/d))$ and $\mathcal{O}(\epsilon^{-2})=\mathcal{O}((n/d)^{1/2})$ at the finite-sample level for sufficiently unbalanced and balanced initial mixing weights, respectively. We further extend our analysis in the overspecified setting to the finite low SNR regime, providing approximate dynamic equations that characterize the EM algorithm's behavior in this challenging case. Our new findings not only expand the scope of theoretical convergence but also improve the bounds for statistical error, time complexity, and sample complexity, and rigorously characterize the evolution of EM estimates.

# Summary. An optional shortened abstract.
summary: In this paper, we thoroughly investigated the EM's behavior in overspecified two-component Mixed Linear Regression (2MLR) models. 
We rigorously characterized the EM estimates for both regression parameters and mixing weights by providing the approximate dynamic equations for the evolution of EM estimates and establishing the convergence guarantees for the final accuracy, time complexity, and sample complexity at population and finite-sample levels, respectively. 
Notably, with an unbalanced initial guess for mixing weights, we showed linear convergence of regression parameters in $\mathcal{O}(\log (1/\epsilon))$ steps. Conversely, with a balanced initial guess, sublinear convergence occurs in $\mathcal{O}(\epsilon^{-2})$ steps to achieve $\epsilon$-accuracy. 
For mixtures with sufficiently imbalanced fixed mixing weights $\|\pi^t-\frac{\mathds{1}}{2}\|_1\gtrsim \mathcal{O}((d/n)^{1/4})$, we establish statistical accuracy $\mathcal{O}((d/n)^{1/2})$, whereas for those with sufficiently balanced fixed mixing weights $\|\pi^t-\frac{\mathds{1}}{2}\|_1\lesssim \mathcal{O}((d/n)^{1/4})$, the accuracy is $\mathcal{O}((d/n)^{1/4})$.
Additionally, our novel analysis sharpens bounds for statistical error, time complexity, and sample complexity needed to achieve a final statistical accuracy of $\mathcal{O}((d/n)^{1/4})$ with fixed sufficiently balanced mixing weights.
Furthermore, we discussed the differences between results of 2MLR and 2GMM, and extended our analysis from the overspecified setting to the finite low SNR regime. 

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_preprint: '' # 'https://arxiv.org/pdf/2405.18237'
url_pdf: '' # 'publication/panicle/Zhankun_CVPRW2022.pdf'
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
  caption: '[](publication/em_2MLR_nosepara/featured.png)' # 'Image credit: [**Unsplash**](publication/multi_ransac1/featured.png)'
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

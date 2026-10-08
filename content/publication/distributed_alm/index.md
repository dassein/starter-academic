---
title: "A Communication-Efficient Distributed Augmented Lagrangian Method for Nonsmooth Regularized Learning"
authors:
- Runxiong Wu
- Zhankun Luo
- Abolfazl Hashemi
- Andi Wang

# Submission date, not a publication date.
date: "2026-09-28T00:00:00Z"
publishDate: "2026-10-08T00:00:00Z"
doi: ""

# 3 = Preprint / Working Paper; the status distinguishes submitted work.
publication_types: ["3"]
publication: "Submitted to AISTATS"
publication_short: "Submitted to AISTATS"

abstract: |
  We study distributed regularized empirical risk minimization in which both the loss and the regularizer may be nonsmooth. We adopt the augmented Lagrangian method (ALM): unlike consensus ADMM, it minimizes the augmented Lagrangian jointly, so each iteration is a proximal-point step, which underlies its fast convergence in the non-distributed setting. In distributed settings, however, this joint minimization couples all clients, and existing distributed ALMs either need many communication rounds per multiplier update or freeze the variables of the other clients and of the regularizer. Working on the dual, our method eliminates the regularizer's auxiliary variable through a Moreau envelope and splits the coupling via Jensen's inequality into independent client subproblems solved to a relative accuracy, so each multiplier update needs one communication round and is an inexact proximal-point step whose error is controlled by the client updates. Under inexact local solves and random partial participation, we prove almost-sure convergence for convex problems with smooth or Lipschitz losses and linear convergence for strongly convex objectives with smooth losses. Experiments on $\ell_1$-regularized learning show that the method needs fewer communication rounds to reach high accuracy than existing distributed methods, especially when few clients participate in each round, and a heuristic extension to federated policy optimization is competitive.

summary: |
  A distributed augmented Lagrangian method for learning with nonsmooth losses and regularizers uses one communication round per multiplier update. The analysis allows inexact local solves and random partial participation, with almost-sure convergence for convex problems with smooth or Lipschitz losses and linear convergence for strongly convex objectives with smooth losses.

featured: true
tags:
- Distributed Optimization
- Nonsmooth Optimization

# Add public resources when available. Do not expose private submission links.
url_preprint: ""
url_pdf: ""
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
url_video: ""

image:
  caption: ""
  focal_point: Smart
  preview_only: false

projects: []
slides: ""
---

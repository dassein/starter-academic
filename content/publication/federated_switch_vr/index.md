---
title: "Variance Reduction for Stochastic Switching in Functionally Constrained Federated Optimization"
authors:
- Antesh Upadhyay
- Sang Bin Moon
- Zhankun Luo
- Abolfazl Hashemi

# Submission date, not a publication date.
date: "2026-09-29T00:00:00Z"
publishDate: "2026-10-08T00:00:00Z"
doi: ""

# 3 = Preprint / Working Paper; the status distinguishes submitted work.
publication_types: ["3"]
publication: "Submitted to AISTATS"
publication_short: "Submitted to AISTATS"

abstract: |
  Federated learning (FL) is increasingly used in safety-critical and fairness-sensitive applications, where learning objectives must be optimized subject to functional constraints. This setting is challenging due to costly projection onto the resulting feasible set, stochastic constraint information, partial client participation, and limited communication at edge devices. We propose a federated stochastic switching framework based on primal-only updates, avoiding dual-variable tuning for functionally constrained federated optimization. For convex objectives, the framework further supports compression with error feedback to control compression-induced bias. We establish high-probability convergence and feasibility guarantees under stochastic gradients and partial client participation, and extend the analysis to weakly convex objectives through proximal-stationarity guarantees. Our bounds isolate the effects of stochastic gradients, constraint-evaluation noise, and partial participation, and show that direct switching can retain a nonvanishing constraint-estimation error even with exact local constraint evaluations. To overcome this limitation, we develop variance-reducing constraint estimators that yield vanishing feasibility and stationarity guarantees with fixed per-round client participation and constraint-evaluation batch sizes. Experiments on Neyman-Pearson classification, fairness-constrained learning on the ADULT dataset, and constrained deep reinforcement learning demonstrate the effectiveness of the proposed framework.

summary: |
  A primal-only stochastic switching framework for functionally constrained federated optimization provides high-probability guarantees under partial client participation. Variance-reducing constraint estimators address the persistent estimation error in direct switching, yielding vanishing feasibility and stationarity guarantees with fixed per-round participation and constraint-evaluation batch sizes.

featured: true
tags:
- Federated Learning
- Constrained Optimization
- Variance Reduction

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

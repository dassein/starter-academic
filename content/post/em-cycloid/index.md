---
title: "Why EM updates trace a cycloid"
summary: "A geometric view of noiseless population EM, and what it reveals about convergence in mixed linear regression."
date: "2026-09-06T00:00:00Z"
lastmod: "2026-09-06T00:00:00Z"
writing_kind: research
authors:
- Zhankun Luo
categories:
- Research notes
tags:
- EM geometry
- Statistical learning
draft: false
math: true
share: false
commentable: false
---

How does an iterative learning algorithm move toward the right answer? In mixed linear regression, observations come from different regression models, but their assignments are hidden. EM repeatedly estimates these assignments and updates the regression parameters.

Our ICML 2024 result exposes a geometric structure in those nonlinear updates: **in the noiseless population setting, the regression estimates lie on a cycloid after the first update**. This is for a two-component model with opposite regression vectors and standard Gaussian covariates; the mixture weights need not be equal.

<figure class="research-figure">
<img src="/publication/em_2mlr/cycloid-explained.svg" width="760" height="710" loading="lazy" alt="Five exact noiseless population EM updates on a blue cycloid branch approach the true parameter. Both coordinates are normalized by the true parameter norm and plotted on equal scales.">
<figcaption>The blue curve is the exact locus of population updates; the numbered points are discrete EM iterations from one nonorthogonal initial direction. The horizontal coordinate follows the true regression vector, and the vertical coordinate is orthogonal to it. Source: Propositions 4.3–4.4 of our ICML 2024 paper.</figcaption>
</figure>

**Why it matters.** The geometry reduces the convergence analysis to an angle. It explains how estimates from a nonorthogonal initialization eventually enter a quadratic convergence regime, and supports an analysis of statistical error when only finite data are available.

**Scope.** The exact curve describes noiseless population EM. Noisy or finite-sample iterates need not lie exactly on it. The later [structural-properties manuscript](/publication/em_2mlr_structural/) studies extensions and non-asymptotic guarantees.

[Read the official paper](https://proceedings.mlr.press/v235/luo24c.html) · [Run the experiments](https://github.com/dassein/cycloid_em_mlr) · [View the poster](https://icml.cc/media/PosterPDFs/ICML%202024/33762.png) · [Research overview](/research/)

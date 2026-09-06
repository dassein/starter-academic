---
title: "Research overview"
summary: "Reliable iterative algorithms through geometry, stochastic estimator design, and constrained optimization."
date: "2026-09-06T00:00:00Z"
url: "/research/"
draft: false
share: false
commentable: false
editable: false
math: true
---

I develop and analyze iterative algorithms for statistical learning and optimization. My research asks **what makes a learning algorithm reliable when its updates are nonlinear, its information is noisy, and its resources are limited?** I study the structure governing an algorithm's trajectory, design estimators that control its errors, and establish guarantees that account for finite data and practical constraints.

My doctoral work at Purdue University with [Prof. Abolfazl Hashemi](https://abolfazlh.github.io/) connects three directions: understanding latent-variable learning, controlling stochastic estimation error, and optimizing under distributed constraints. They share a method: identify the mechanism that limits an algorithm, use that structure to improve its updates, and quantify the resulting accuracy and computational cost.

## Understanding the dynamics of latent-variable learning

Expectation-maximization (EM) alternates between estimating hidden assignments and updating model parameters. Although it is widely used, its nonlinear updates can obscure why an algorithm initially moves slowly, later accelerates, or behaves differently under model misspecification.

In [Unveiling the Cycloid Trajectory of EM Iterations in Mixed Linear Regression](/publication/em_2mlr/) (**ICML 2024**), we derived explicit population updates for two-component mixed linear regression across signal-to-noise regimes. In the noiseless setting, the iterates trace a cycloid. Analyzing this trajectory reveals convergence behavior and improves finite-sample error bounds. Our [extended trajectory analysis with unknown mixing weights and regression parameters](/publication/em_2mlr_structural/) characterizes linear-to-quadratic population convergence and finite-sample guarantees; the revised manuscript has been submitted to **IEEE Transactions on Information Theory** following a revise-and-resubmit decision.

Our [TMLR 2026 paper on overspecified mixed linear regression](/publication/em_2mlr_nosepara/) studies what changes when the fitted mixture has more components than the data-generating model. It identifies distinct convergence and statistical-accuracy regimes, showing that initialization can change more than the speed of an otherwise identical process. A [related preprint on score matching, maximum likelihood, and EM](/publication/diffusion_2mlr/), **submitted to TMLR**, connects diffusion-path score matching to likelihood-based statistical guarantees and derives fixed-noise decompositions involving EM operators. Its consistency and asymptotic-distribution results require the stated regularity and diffusion-schedule conditions.

**Next questions.** Which low-dimensional variables explain the dynamics of more complex latent models? How can these descriptions guide initialization, stopping rules, and inference methods when symmetry or misspecification changes the geometry?

## Designing stochastic estimators with controlled bias and variance

Randomness can reduce computation, but it also introduces error. I study how the distribution and dependence of random queries can be designed together with an algorithm, and how to obtain guarantees that hold with high probability.

In [RAMPAGE](/publication/rampage/), a **preprint submitted to AISTATS**, we view gradient extrapolation as integration along a path. Randomized midpoint sampling removes discretization bias in nonlinear extrapolation; the RAMPAGE+ variant couples antithetic samples to cancel internal first-order variance terms. The analysis covers several classes of root-finding problems, constrained variational inequalities, and smooth convex-concave games.

Our [Unified High-Probability Analysis of Stochastic Variance-Reduced Estimation](/publication/variance_reduced/) is a **preprint** that organizes estimators through memory retention, resets, and corrections for iterate movement. A dimension-free, vector-valued Freedman inequality supports analysis in Euclidean and non-Euclidean settings. For expectation-constrained stochastic optimization, one application improves the high-probability oracle-complexity bound from $\widetilde O(\varepsilon^{-4})$ to $\widetilde O(\varepsilon^{-3})$ for target accuracy $\varepsilon$, under the paper's assumptions. Here, $\widetilde O$ suppresses logarithmic factors.

My ongoing project, [Generalized Antithetic Variance Reduction: an Optimal Transport Approach](/project/antithetic/), is a **manuscript in preparation**. It studies how to pair samples while preserving their target distribution, using connections between negative dependence and optimal transport. [Earlier project slides](https://zhankunluo.com/files/project/Zhankun_GroupMeet_251118.pdf) introduce the antithetic-map perspective.

**Next questions.** When can a coupling cancel an estimator's leading error without adding bias? How can concentration guarantees remain useful when an algorithm adapts its sampling or stopping decisions to the data?

## Optimizing under distributed and stochastic constraints

In federated learning, a strong average can conceal poor performance for individual clients. Partial participation and uncertain constraints add another difficulty: an update must improve the objective while maintaining feasibility.

Our [Softmax-Weighted Switching Gradient method](/publication/softmax_switchgd/) (**UAI 2026**) addresses distributed stochastic minimax optimization with stochastic constraints. It smooths the worst-client objective and switches between objective and feasibility steps in a single-loop, primal-only method. We establish guarantees for full participation and extend the analysis to partial participation under a condition controlling client-sampling noise, with logarithmic dependence on the confidence parameter. Experiments examine Neyman-Pearson classification, fair classification, and federated safe reinforcement learning. The [implementation](https://github.com/sangbinM/SoftmaxSGM) and [poster](/publication/softmax_switchgd/poster_UAI26_softmaxgd.pdf) accompany the paper.

**Next questions.** How should an algorithm allocate computation and communication when participation and constraints change over time? Can improved stochastic estimators strengthen feasibility guarantees while reducing the resources needed to obtain them?

These directions connect optimization, probability, and statistics with the systems in which learning algorithms run. I am interested in collaborations that turn an explanation of algorithmic behavior into a better method, together with a clear account of its assumptions and limits.

[All publications](/#publications) · [Selected presentations](/#presentations) · [Contact me](mailto:luo333@purdue.edu)

---
title: "Why randomizing an extrapolation step can help"
date: "2026-09-06T00:00:00Z"
lastmod: "2026-09-06T00:00:00Z"
slug: "randomized-midpoint-antithetic"
summary: "Why randomized midpoint evaluations remove a specific approximation bias, and how antithetic pairs cancel first-order fluctuations."
categories:
- Research notes
tags:
- Stochastic optimization
- Variance reduction
draft: false
writing_kind: research
authors:
- Zhankun Luo
math: true
share: false
commentable: false
---

An optimization method makes decisions from a limited number of evaluations. Where those evaluations occur can matter as much as how many we take. Our work on randomized extrapolation asks whether carefully chosen randomness can improve the information in an update.

## From a midpoint to a segment average

The extragradient method first looks ahead from the current estimate, evaluates an update direction there, and uses that direction to take a step. In the RAMPAGE formulation, this look-ahead evaluation can be understood as a midpoint approximation to an average of the vector field along an extrapolation segment.

For a nonlinear field, the midpoint value need not equal that average. RAMPAGE instead chooses a uniformly random location along the segment. Averaging over this randomness recovers the segment average exactly. The unbiasedness here is with respect to this segment average.

**Illustrative example.** Suppose the quantity along a unit-length segment is $q(u)=u^2$. Evaluating only at the midpoint gives $1/4$, while the segment average is $1/3$. A uniform random point $U$ gives a noisy value $q(U)$ whose expectation is $1/3$. Randomness removes the midpoint approximation bias, but introduces variation between evaluations.

## Pairing samples to control that variation

RAMPAGE+ evaluates at both $U$ and $1-U$ and averages the results. Each location is uniformly distributed, so the pair preserves the same expected value. Their positions are deliberately coupled: when one is near one end, the other is near the opposite end.

**Illustrative example.** For a locally linear quantity $q(u)=a+bu$, the paired average is always $a+b/2$, regardless of the sampled location. Opposite deviations cancel. For a nonlinear quantity, curvature leaves residual variation. The RAMPAGE+ analysis formalizes this cancellation of first-order variance terms under the paper's assumptions.

The variance benefit depends jointly on the function, the pairing, and the setting.

## Beyond the unit interval

Our ongoing antithetic work studies how to construct paired samples for more general distributions. The pair must preserve the target distribution while creating useful negative dependence. Optimal transport provides a way to formulate the choice of such a coupling.

This connects a simple sampling trick to a broader algorithm-design question: which randomness should an estimator keep, reuse, or cancel? Convergence guarantees still require the operator, smoothness, and other conditions stated in the relevant analysis.

## Sources and related work

- [RAMPAGE: RAndomized Mid-Point for debiAsed Gradient Extrapolation](/publication/rampage/) — **submitted to AISTATS**. See the [manuscript](/publication/rampage/arxiv_rampage.pdf), Section 1.2 and Appendix A, for the estimator and variance analysis.
- [Generalized Antithetic Variance Reduction: an Optimal Transport Approach](/project/antithetic/) — **manuscript in preparation**. [Project slides](/files/project/Zhankun_GroupMeet_251118.pdf) introduce the underlying antithetic ideas.

[Browse all research notes](/notes/#research-notes)

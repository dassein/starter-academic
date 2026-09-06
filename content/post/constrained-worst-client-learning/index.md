---
title: "Improving the worst client while respecting constraints"
date: "2026-09-06T00:00:00Z"
lastmod: "2026-09-06T00:00:00Z"
slug: "constrained-worst-client-learning"
summary: "How softmax-weighted switching balances worst-client performance with stochastic constraints."
categories:
- Research notes
tags:
- Federated learning
- Constrained optimization
draft: false
writing_kind: research
authors:
- Zhankun Luo
math: true
share: false
commentable: false
---

A shared model can perform well on average while serving one client poorly. An average constraint can also conceal a violation at an individual client. Our UAI 2026 paper studies a formulation that makes both concerns explicit: minimize the largest client loss while requiring every client's expected constraint value to remain below its threshold.

Here, a client might represent a participating device or a data-holding organization. A constraint expresses a particular numerical requirement, such as a bound on a false-positive rate.

## Deciding which problem to work on

**Illustrative example.** Imagine several sites training a classifier. Each site wants low prediction loss and a false-positive rate below a chosen limit. Improving average accuracy could leave one site above its limit. A useful update must sometimes concentrate on reducing that violation before concentrating on prediction loss.

The switching-gradient method follows this logic. At each round, it estimates the constraint values and checks a softmax-weighted constraint estimate against a prescribed tolerance. If that estimate passes the check, clients take local steps using objective gradients. Otherwise, they use constraint gradients. The server combines their updates to obtain the next shared model.

The method updates the model parameters directly, without maintaining a separate set of dual variables. This primal-only structure enforces constraints through the switching rule.

## Why use softmax weights?

Selecting only the client with the largest estimated value can be sensitive to noise, especially when several clients have similar values. Softmax gives larger weights to larger values while distributing weight smoothly among participating clients. Objective and constraint updates use their corresponding sets of weights.

The weighted constraint estimate approximates the maximum; it is not identical to it. The softmax parameter and the switching tolerance must therefore account for this approximation and for noisy measurements. Passing a sampled check is not, by itself, proof that every true client constraint is satisfied at that round.

## What changes when clients are absent?

With full participation, each round uses information from all clients. With partial participation, the algorithm restricts its weights and measurements to the sampled subset. If the most difficult client is missing, the subset can underestimate the problem.

The partial-participation analysis explicitly accounts for this sampling error. It assumes independent, uniformly sampled subsets and additional control of the gap between sampled client values and the population maximum. This is stronger than merely assuming that individual gradient estimates have bounded noise. Additional sampling terms enter the guarantees, including the feasibility bound.

The convergence results also rely on conditions such as convex objectives and constraints, a bounded parameter domain, and controlled stochastic estimation error. They concern the algorithm's returned averaged solution. They do not establish exact feasibility at every intermediate step or universal guarantees for arbitrary neural networks.

## Sources and related work

[First-Order Softmax Weighted Switching Gradient Method for Distributed Stochastic Minimax Optimization with Stochastic Constraints](/publication/softmax_switchgd/) — **UAI 2026**. See [official proceedings](https://proceedings.mlr.press/v337/luo26a.html), [manuscript](/publication/softmax_switchgd/arxiv_softmax_switchgd.pdf) Sections 3–4, and [implementation](https://github.com/sangbinM/SoftmaxSGM).

[Browse all research notes](/notes/#research-notes)

---
title: ECE 64100 Model-Based Image and Signal Processing
subtitle: 

# Summary for listings and search engines
abstract: ""

summary: ""

# Link this post with a project
projects: []

# Date published
date: "2020-12-13T00:00:00Z"

# Date updated
lastmod: "2020-12-13T00:00:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: '' # for example, 'Image credit: [**Unsplash**](https://unsplash.com/photos/CpkOjOcXdUY)'
  focal_point: ""
  placement: 2
  preview_only: false

authors:
- Zhankun Luo

tags:
- machine learning

categories: []

---
<!--more-->
Course Description: [ECE 64100 Model-Based Image and Signal Processing](https://engineering.purdue.edu/~bouman/ece641/)

Textbook: [Model Based Imaging](https://engineering.purdue.edu/~bouman/publications/pdf/MBIP-book.pdf)
Notes: [course notes](https://engineering.purdue.edu/~bouman/ece641/notes/)

Labs: [instruction](https://cabouman.github.io/grad_labs/)
* [maximum a posteriori (MAP) image restoration](ECE694_Zhankun_Luo_lab1.pdf)
The lab explores the use of maximum a posteriori (MAP) estimation of images from
noisy and blurred data using both Gaussian Markov random field (GGMRF) and non-Gaussian Markov random field (MRF) prior models (Generalized Gaussian MRF (GGMRF) and q-Generalized GMRF(QGGMRF)). We solved the high dimensional optimization problem of MAP estimation with iterative coordinate descent (ICD) techniques.
* [expectation-maximization (EM) algorithm](ECE694_Zhankun_Luo_lab3.pdf), [API docs for source code](apidocs.pdf)
This lab explores the use of the expectation-maximization (EM) algorithm for the
estimate of parameters. In particular, we will use the EM algorithm to estimate the parameters of Gaussian mixture distribution, and implement the method for automaticaly determining the number of
clusters in a Gaussian mixture model by minimizing the minimum description length (MDL) estimator.

Homeworks:
* [probability, Gaussian random variables](ECE641_hw1_Zhankun.pdf)
* [MAP, ML and MMSE Estimators, conditional distribution of Gaussian, time-reversibility of Gaussian processes](ECE641_hw2_Zhankun.pdf)
* [Gaussian autoregressive (AR) models](ECE641_hw3_Zhankun.pdf)

Topics:
* [Alternating Direction Method of Multipliers (ADMM)](https://stanford.edu/~boyd/admm.html), [paper](https://stanford.edu/~boyd/papers/admm_distr_stats.html), [slides](https://web.stanford.edu/~boyd/papers/pdf/admm_slides.pdf)
* [MCMC - CMU slides](http://www.cs.cmu.edu/~epxing/Class/10708-16/slide/lecture16-MCMC.pdf), 

Blogs:
* [an ADMM based framework for AutoML pipeline configuration](https://arxiv.org/pdf/1905.00424.pdf), [blog](https://www.zhihu.com/question/510170303/answer/2300184152)
* [applications of ADMM](https://zhuanlan.zhihu.com/p/86826985), [ADMM explanation](https://zhuanlan.zhihu.com/p/448289351), [introduction to ADMM](https://zhuanlan.zhihu.com/p/21112618)
* [optimization techniques](https://zhuanlan.zhihu.com/p/421560203)
* [L1, L2 regularizations and Laplace, Gaussian priors](https://zhuanlan.zhihu.com/p/116079663)
* [MCMC: Metropolis Hastings, Hamiltonian Monte Carlo](https://zhuanlan.zhihu.com/p/463673039), [MCMC explanation](https://zhuanlan.zhihu.com/p/376074545), [MCMC](https://zhuanlan.zhihu.com/p/21112618). [MCMC methods](https://zhuanlan.zhihu.com/p/109978580)


References:
* [Convex Optimization: CMU Fall 2019](https://www.stat.cmu.edu/~ryantibs/convexopt/)
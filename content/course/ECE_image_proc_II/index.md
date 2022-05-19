---
title: ECE 63700 Digital Image Processing II
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

# url_pdf: "files/post/Van_der_Pol.pdf"
# (course/MA_intro_applied_math/Zhankun Luo_homework01.pdf)
---
Course Description: [ECE 64100 Model-Based Image and Signal Processing](https://engineering.purdue.edu/~bouman/ece641/)

Textbook: [Model Based Imaging](https://engineering.purdue.edu/~bouman/publications/pdf/MBIP-book.pdf)
Notes: [course notes](https://engineering.purdue.edu/~bouman/ece641/notes/)

Labs: [instruction](https://cabouman.github.io/grad_labs/)
* [maximum a posteriori (MAP) image restoration](ECE694_Zhankun_Luo_lab1.pdf)
The lab explores the use of maximum a posteriori (MAP) estimation of images from
noisy and blurred data using both Gaussian and non-Gaussian Markov random field (MRF)
prior models (GGMRF and q-Generalized GMRF(QGGMRF)). We solved the high dimensional
optimization problem of MAP estimation with iterative coordinate descent (ICD) techniques.
* [expectation-maximization (EM) algorithm](ECE694_Zhankun_Luo_lab3.pdf), [API docs for source code](apidocs.pdf)
This lab explores the use of the expectation-maximization (EM) algorithm for the
estimate of parameters. In particular, we will use the EM algorithm to estimate the parameters of Gaussian mixture distribution, and implement the method for automaticaly determining the number of
clusters in a Gaussian mixture model by minimizing the minimum description length (MDL) estimator.

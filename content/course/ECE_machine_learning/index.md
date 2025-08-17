---
title: ECE 59500 Machine Learning
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
<!--more-->
Course Description: [ECE 59500 Machine Learning](https://engineering.purdue.edu/ECE/Academics/Online/Courses/machine-learning)

Textbook: 
* [Pattern Recognition and Machine Learning](https://link.springer.com/book/9780387310732)
* [Machine Learning: A Probabilistic Perspective](https://mitpress.mit.edu/books/machine-learning-1)
* [Pattern Recognition, 4th Edition](https://www.elsevier.com/books/pattern-recognition/koutroumbas/978-1-59749-272-0)

Topics:
* [Expectation-Maximization algorithm](EM_algo.html)
* [Gaussian mixture model](GMM_understandmd.html)
By maximizing the probability of the current state with the EM algorithm, we can estimate the parameters of our Gaussian mixture model.
* [Capsule networks and EM rounting](GMM_em_routing.html)
By introducing the weight coefficients and rewriting the initial distribution formula, we can derive Hinton's Capsules with EM routing.
* [hidden Markov model](HMM_understand.html)
By maximizing the probability of the current state with the EM algorithm, we can estimate the parameters of our Hidden Markov Model. To prevent underflow of the estimated parameter values, we introduce intermediate parameters.
* [backpropagation](backpropagation.pdf), [codes](https://github.com/dassein/backpropagation)
Derive the backpropagation rule in matrix form, then implement the backpropagation with both MATLAB and python. Furthermore, the backpropagation rule is integrated in the simple Deep Learning Framwork library (see codes).
* [Quasi-Newton optimization methods](Quasi_Newton_method.pdf), [codes](Quasi_Newton_report.pdf)
Derive the formula of Quasi-Newton, such as DFP and BFGS. DFP may fail when the condition number of hessian lambda_max / lambda_min is very big, BFGS is more stable than DFP but someone gave an example that BFGS couldn't work for non-convex problems. In addition, we implemented the limit memory BFGS Quasi-Newton method.
* [Wasserstein GAN](Wasserstein_GAN.pdf)
When the discriminator is well-trained and there is a huge gap be between the real image distribution && the fake image distribution, the gradient for the generator loss would vanish, thus the generator learns nothing from the optimization. To address the problem, Wasserstein GAN (WGAN) introduces the Wasserstein distance whose gradient does not vanish when the distribution of the real image and that of the fake image are far away from each other. Furthermore, the improved model WGAN-GP added the gradient penalty in the loss function. The experimental results demonstrate an improvement in the learning stability comparing to DCGAN whereas WGAN-GP convergence speed outcompetes WGAN.

References: 
* [Convex Optimization – Boyd and Vandenberghe](https://stanford.edu/~boyd/cvxbook/), [pdf](https://stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)
* [The Elements of Statistical Learning: (ESL)](https://hastie.su.domains/ElemStatLearn/), [pdf](https://www.sas.upenn.edu/~fdiebold/NoHesitations/BookAdvanced.pdf)

Solution to ESL:
* [online solution (python) to ESL](https://yuhangzhou88.github.io/ESL_Solution/)
* [online solution (R) to ESL](https://waxworksmath.com/Authors/G_M/Hastie/hastie.html)


Math foundations for ML:
* [Understanding Machine Learning: From Theory to Algorithms](https://www.cambridge.org/core/books/understanding-machine-learning/3059695661405D25673058E43C8BE2A6), [pdf](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf)
* [Mathematical Analysis of Machine Learning Algorithms](https://www.cambridge.org/core/books/mathematical-analysis-of-machine-learning-algorithms/EB9BABB05A5C312F19C38E5A01A5ECFC), [pdf](https://tongzhang-ml.org/lt-book/lt-book.pdf), [slides](https://tongzhang-ml.org/lt-book.html)
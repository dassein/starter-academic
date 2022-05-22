---
title: STAT 528 Introduction to Mathematical Statistics
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
Course Description: [STAT 528 Introduction to Mathematical Statistics](https://www.math.purdue.edu/academic/courses/coursepage?subject=MA&course=51100)


Textbook: 
[Probability for Statisticsand Machine Learning: Fundamentals and Advanced Topics](https://link.springer.com/book/10.1007/978-1-4419-9634-3), [pdf](https://link.springer.com/content/pdf/10.1007/978-1-4419-9634-3.pdf)

Notes: 
* [problems of inference](https://www.stat.purdue.edu/~dasgupta/528-1.pdf)
* [statistical models: distributions of Exponential family, heavy tails and kewness](https://www.stat.purdue.edu/~dasgupta/528-2.pdf)
* [decision theory: evaluating an estimator and risk function, maximum risk and minimaxity](https://www.stat.purdue.edu/~dasgupta/528-3.pdf)
* [Exponential families, moments and moment generating function](https://www.stat.purdue.edu/~dasgupta/528-4.pdf)
* [point estimations](https://www.stat.purdue.edu/~dasgupta/528-5.pdf)
    * likelihood function and MLE, score function
    * Fisher information, sufficient statistics and factorization theorem, 
    * minimal sufficient statistics
    * ancillary statistics and MLE in curved Exponential families, Basu’s theorem
    * Rao-Blackwell theorem and uniformly minimum variance unbiased estimate (UMVUE) 
    * completeness and Lehmann-Scheffe theorem, 
    * asymptotic unbiasedness
    * Cramer-Rao inequality
* [asymptotic approximations](https://www.stat.purdue.edu/~dasgupta/528-6.pdf)
    * consistency of estimator sequence 
    * Cramer-Rao Conditions for consistency of MLE
    * asymptotic distribution of MLE and Fisher information matrix
    * pivot and Wald confidence intervals
    * Delta theorem of Cramer and variance stabilizing transformations (VST)
    * Rao's score intervals, Wald confidence intervals and Slutsky’s theorem
* [testing of hypotheses and confidence regions](https://www.stat.purdue.edu/~dasgupta/528-7.pdf)
    * type I and type II error probabilities
    * randomized and nonrandomized Tests
    * most powerful tests and Neyman-Pearson lemma

References: 
* [Fundamentals of Probability: A First Course](https://link.springer.com/book/10.1007/978-1-4419-5780-1), [pdf](https://link.springer.com/content/pdf/10.1007/978-1-4419-5780-1.pdf)
* [Statistical Inference notes, Robert L. Wolpert](http://www2.stat.duke.edu/courses/Spring07/sta215/)
    * [course schedule and outline](http://www2.stat.duke.edu/courses/Spring07/sta215/732syl.html)
    * [distributions](http://www2.stat.duke.edu/courses/Spring07/sta215/etc/pdf.pdf), [wk01](http://www2.stat.duke.edu/courses/Spring07/sta215/lec/wk01.pdf), [wk02](http://www2.stat.duke.edu/courses/Spring07/sta215/lec/wk01.pdf), [wk03](http://www2.stat.duke.edu/courses/Spring07/sta215/lec/wk01.pdf), [wk04](http://www2.stat.duke.edu/courses/Spring07/sta215/lec/wk01.pdf), [wk05](http://www2.stat.duke.edu/courses/Spring07/sta215/lec/wk01.pdf), [wk07](http://www2.stat.duke.edu/courses/Spring07/sta215/lec/wk01.pdf), [wk08](http://www2.stat.duke.edu/courses/Spring07/sta215/lec/wk01.pdf), [wk11](http://www2.stat.duke.edu/courses/Spring07/sta215/lec/wk01.pdf), [wk12](http://www2.stat.duke.edu/courses/Spring07/sta215/lec/wk01.pdf), [wk13](http://www2.stat.duke.edu/courses/Spring07/sta215/lec/wk13.pdf), [wk14](http://www2.stat.duke.edu/courses/Spring07/sta215/lec/wk14.pdf), [wk15](http://www2.stat.duke.edu/courses/Spring07/sta215/lec/wk15.pdf)
* [Mathematical Statistics: Exercises and Solutions](https://link.springer.com/book/10.1007/0-387-28276-9), [pdf](https://link.springer.com/content/pdf/10.1007/0-387-28276-9.pdf)
* [An Introduction to Probability Theory and Its Applications, Volume 1, William Feller]()
* [An Introduction to Probability Theory and Its Applications, Volume 2, William Feller](https://www.wiley.com/en-us/An+Introduction+to+Probability+Theory+and+Its+Applications%2C+Volume+2%2C+2nd+Edition-p-9780471257097)

Blogs:
* [LU](https://math.ecnu.edu.cn/~jypan/Teaching/NA/slides_02A_LU.pdf), [Cholesky](https://math.ecnu.edu.cn/~jypan/Teaching/NA/slides_02B_MD.pdf), [QR](https://math.ecnu.edu.cn/~jypan/Teaching/NA/slides_03B_QR.pdf), [SVD decompositions](https://math.ecnu.edu.cn/~jypan/Teaching/NA/slides_03C_SVD.pdf), [Python implementation](https://zhuanlan.zhihu.com/p/462433659)
* [Jocobi, Gauss-Seidel, Successive Over Relaxation (SOR), Conjugate Gradient methods to solve a system of linear equations](https://math.ecnu.edu.cn/~jypan/Teaching/MNA/slides_ch06_iter.pdf), [Python implementation](https://zhuanlan.zhihu.com/p/462428215)
* [Householder, Givens transform](https://math.ecnu.edu.cn/~jypan/Teaching/NA/slides_03A_Transformation.pdf)
* [tensor decomposition/factorization 1](https://zhuanlan.zhihu.com/p/24798389), [2](https://zhuanlan.zhihu.com/p/24824550), [tensor CP decomposition](https://zhuanlan.zhihu.com/p/383058483)
* [matrix factorization in PyTorch: source codes](https://github.com/EthanRosenthal/torchmf), [blog](https://www.ethanrosenthal.com/2017/06/20/matrix-factorization-in-pytorch/)
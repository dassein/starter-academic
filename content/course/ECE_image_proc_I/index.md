---
title: ECE 63700 Digital Image Processing I
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
Course Description: [ECE 63700 Digital Image Processing I](https://engineering.purdue.edu/~bouman/ece637/)

Notes: [course notes](https://engineering.purdue.edu/~bouman/ece637/notes/)

Labs: [instruction](https://cabouman.github.io/grad_labs/)
* [image filtering](ECE637_Zhankun_Luo_lab1.pdf)
* [2-D random processes](ECE637_Zhankun_Luo_lab2.pdf)
* [neighborhoods and connected components](ECE637_Zhankun_Luo_lab3.pdf)
* [pointwise operations and gamma](ECE637_Zhankun_Luo_lab4.pdf)
* [eigen-image analysis](ECE637_Zhankun_Luo_lab5.pdf)
* [introduction to colorimetry](ECE637_Zhankun_Luo_lab6.pdf)
* [image restoration](ECE637_Zhankun_Luo_lab7.pdf)
* [image halftoning](ECE637_Zhankun_Luo_lab8.pdf)
* [deep learning and CNNs](DL_Lab_Exercises.pdf)

Codes: [source code](https://github.com/dassein/image_processing_algo)
We implemented the image processing method both in the spatial domain and frequency domain. For instance, we developed the codes not only for auto-contrast, histogram matching, spatial filters such as Gauss, Laplace, LoG, the weighted median in the spatial domain; but also for 2d DFT, 2d DCT based on FFT, filters in the frequency domain. We also applied morphological operations, Ostu, watershed, Hough transform for line detection, Canny edge detection, Harris corner dectcttion, and scale-invariant feature transform (SIFT) methods in Python and C++ for image processing.
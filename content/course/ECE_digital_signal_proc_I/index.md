---
title: ECE 53800 Digital Signal Processing I 
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
- signal processing

categories: []

# url_pdf: "files/post/Van_der_Pol.pdf"
# (course/MA_intro_applied_math/Zhankun Luo_homework01.pdf)
---
Course Description: [ECE 53800 Digital Signal Processing I](https://engineering.purdue.edu/ECE/Academics/Undergraduates/UGO/CourseInfo/courseInfo?courseid=108.0)

Textbook: [Digital Signal Processing: Fundamentals and Applications, 3rd Edition](https://www.elsevier.com/books/digital-signal-processing/tan/978-0-12-815071-9), [pdf](https://www-elec.inaoep.mx/~jmram/Digital_Signal_Processing__LI_TAN.pdf)

Projects:
* [speech enhancement with FIR filter](FIR_speech_enhance.pdf)
  * input [nspeech.wav](nspeech.wav)
  * ouput [nspeech_filtered.wav](nspeech_filtered.wav)
* [digital speech and audio equalizer](speech_equalize.pdf)
  * input [No9seg.wav](No9seg.wav)
  * output [no equalization](No9seg_no%20equal.wav), [low-pass filtered](No9seg_low%20pass.wav), [band-pass filtered](No9seg_band%20pass.wav), [high-pass filtered](No9seg_high%20pass.wav)
* [adaptive filters: LMS and RLS](adaptive_filter.pdf)
* [downsampling and upsampling](downup_sample.pdf)

Codes: [DSP_method](https://github.com/dassein/DSP_method) 
* implementation of DFT & FFT, conversion between Laplace transforma and Z-transform, FIR & IIR filters, adaptive LMS & RLS filters

Topics:
* [FT, DTFT and DFT](DTFT_DFT.pdf)
* [DFT and DCT](DCT.pdf)
* [Laplace transform and Z-transform](Z_transform.pdf)
* [Least Mean Squares and Recursive Least
Squares](LMS.pdf)

Homeworks:
* [homework 1](ZhankunLuo_hw1.pdf)
* [homework 2](ZhankunLuo_hw2.pdf)
* [homework 3](ZhankunLuo_hw3.pdf)
* [homework 4](ZhankunLuo_hw4.pdf)
* [homework 5](ZhankunLuo_hw5.pdf)
* [homework 6](ZhankunLuo_hw6.pdf)
* [homework 7](ZhankunLuo_hw7.pdf)
* [homework 8](ZhankunLuo_hw8.pdf)
* [homework 9](ZhankunLuo_hw9.pdf)

Exams:
* [midterm exam 2](ZhankunLuo_Exam2.pdf)
* [final exam](ZhankunLuo_FinalExam.pdf)

References:
* [Lecture Notes for EE 261: The Fourier Transform and its Applications](https://see.stanford.edu/materials/lsoftaee261/book-fall-07.pdf)
* [Fourier Analysis and Its Applications](https://link.springer.com/book/10.1007/b97452), [pdf](https://iujfk.files.wordpress.com/2013/04/fourier-analysis-and-its-applications.pdf)
* [Adaptive Filters: Theory and Applications, 2nd Edition](https://www.wiley.com/en-us/Adaptive+Filters%3A+Theory+and+Applications%2C+2nd+Edition-p-9781119979548), [pdf](https://abrarhashmi.files.wordpress.com/2016/02/behrouz-farhang-boroujeny-adaptive-filters_-theory-and-applications-wiley-2013.pdf)
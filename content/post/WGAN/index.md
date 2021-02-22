---
title: WGAN
subtitle: 

# Summary for listings and search engines
summary: When the discriminator is well-trained and there is a huge gap be between the real image distribution && the fake image distribution, the gradient for the generator loss would vanish, thus the generator learns nothing from the optimization. To solve the problem, Wasserstein GAN (WGAN) introduces the Wasserstein distance whose gradient does not vanish when the distribution of real image and that of the fake image are far away from each other. Furthermore, the improved model WGAN-GP added the gradient penalty in the loss function. The experimental results demonstrate an improvement in the learning stability comparing to DCGAN whereas WGAN-GP convergencespeed outcompetes WGAN.

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
- deep learning

categories: []

url_pdf: "files/post/Wasserstein_GAN.pdf"
---



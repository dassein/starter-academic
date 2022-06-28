---
title: "High-Resolution UAV Image Generation for Sorghum Panicle Detection"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- Enyu Cai
- Zhankun Luo
- Sriram Baireddy
- Jiaqi Guo
- Changye Yang
- Edward J. Delp

# Author notes (optional)
# author_notes:
# - "Equal contribution"
# - "Equal contribution"

date: "2022-06-01T00:00:00Z"
# url_preprint: https://arxiv.org/pdf/2205.03947.pdf
doi: "https://openaccess.thecvf.com/content/CVPR2022W/AgriVision/html/Cai_High-Resolution_UAV_Image_Generation_for_Sorghum_Panicle_Detection_CVPRW_2022_paper.html" # "https://doi.org/10.48550/arXiv.2205.03947"

# Schedule page publish date (NOT publication's date).
publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In Proceedings of *the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Workshop on Agriculture-Vision*
publication_short: In Proceedings of *CVPRW*

abstract: The number of panicles (or heads) of  Sorghum plants is an important phenotypic trait for plant development and grain yield estimation. The use of Unmanned Aerial Vehicles (UAVs) enables the capability of collecting and analyzing Sorghum images on a large scale. Deep learning can provide methods for estimating phenotypic traits from UAV images but requires a large amount of labeled data. The lack of training data due to the labor-intensive ground truthing of UAV images causes a major bottleneck in developing methods for Sorghum panicle detection and counting. In this paper, we present an approach that uses synthetic training images from generative adversarial networks (GANs) for data augmentation to enhance the performance of Sorghum panicle detection and counting. Our method can generate synthetic high-resolution UAV RGB images with panicle labels by using image-to-image translation GANs with a limited ground truth dataset of real UAV RGB images. The results show the improvements in panicle detection and counting using our data augmentation approach.

# Summary. An optional shortened abstract.
summary: In this paper, we presented the use of GAN generated synthetic images to augment the training data for panicle detection and counting. We examined two image-to-image translation GANs and showed that their use can improve the performance of panicle detection and counting. We did not use the temporal information available in our real Sorghum UAV dataset during training due to the limitation of the network structures. Future work includes developing multi-temporal methods that can generate synthetic plant images in a temporally consistent style. This will also us to estimate phenotypic traits as the plant grows. We will also examine our approach for estimating traits of other plant such as maize tassels.

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'publication/panicle/Zhankun_CVPRW2022.pdf'
url_code: ''
url_dataset: ''
# url_poster: 'publication/smart_ladle/Poster_Zhankun_Luo.pdf'
url_project: 'https://engineering.purdue.edu/~sorghum/'
# url_slides: 'publication/smart_ladle/intro_senior_design.pdf'
url_source: ''
url_video: 'https://www.youtube.com/watch?v=nl2x2SE4PnU'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: '[](publication/panicle/featured.png)' # 'Image credit: [**Unsplash**](publication/multi_ransac1/featured.png)'
  # focal_point: "" # put png on top
  focal_point: Smart # put png on right
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

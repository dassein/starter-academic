---
title: “Structured Light Vision Systems Using a Robust Laser Stripe Segmentation Method“
authors:
- Zhankun Luo

date: "2021-05-04T00:00:00Z"
doi: "https://doi.org/10.25394/PGS.14536011.v1"

# Schedule page publish date (NOT publication's date).
publishDate: "2021-05-04T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["7"]

# Publication name and optional abbreviated publication name.
publication: Master thesis, Purdue University Graduate School, May 2021
publication_short: Master thesis, Purdue University Graduate School, May 2021

abstract: In the thesis, we propose a structured light vision system equipped with multi-cameras and multi-laser emitters for object height measurement or 3D reconstruction. The proposed method offers a better accuracy performance over a single camera system. The structured light method may fail the interference of reflection and scattering of light. We use U-Net to extract the laser region, obtain the laser stripe center after erosion and dilation, and finally reconstruct the point cloud corresponding to the laser stripe. Our experiments demonstrate that our structured light system with the U-Net can perform effectively and robustly in a complex environment. 

# Summary. An optional shortened abstract.
summary: In this paper, we have derived a framework for 3D reconstruction and object height measurement using multiple cameras and multiple laser emitters. We have developed a U-Net based approach to tackle the problem cased by the refection and scattering of light in complex environment. Our experiments demonstrate that the system with multiple cameras and U-Net laser stripe extraction method improves the accuracy of height measurement over the single camera and strengthen the stability of system. For the future work, we can collect more images from different perspectives with reflected light and scattering light. Thus, we are able to further improve the accuracy of our model for segmentation task with sufficient information. Besides, we may replace the U-Net architecture with the UNet++ architecture which has more skip pathways to reduce the semantic disparity between the encoder feature maps and that of the decoder.

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'publication/extract_laser/thesis_Zhankun Luo_final.pdf'
url_code: "https://drive.google.com/drive/folders/1KOeHdyQizS38OfvXFcmv0OtI9VmDzwKv"
url_dataset: "https://drive.google.com/drive/folders/1KSiMZagB2AexFeS68O3yuOUTNnIyuo8L?usp=sharing"
url_poster: ''
url_project: ''
url_slides: 'publication/extract_laser/Zhankun_thesis_defense.pdf'
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption:  '' # 'Image credit: [**Unsplash**](publication/extract_laser/featured.png)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

---



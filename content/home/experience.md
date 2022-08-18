---
# An instance of the Experience widget.
# Documentation: https://wowchemy.com/docs/page-builder/
widget: experience

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 60

title: Experience
subtitle:

# Date format for experience
#   Refer to https://wowchemy.com/docs/customization/#date-format
# date_format: Jan 2021

# Experiences.
#   Add/remove as many `experience` items below as you like.
#   Required fields are `title`, `company`, and `date_start`.
#   Leave `date_end` empty if it's your current employer.
#   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.

# * Worked on improving the hierarchical method by incorporating the nutrient and visual information of food

experience:

  - title: Teaching Assitant
    company: ECE department, Purdue University West Lafayette
    company_url: https://engineering.purdue.edu/ECE
    location: West Lafayette, IN
    date_start: '2022-05-22' # '2022-08-23'
    date_end: '' # '2022-08-06' #  and help sessions
    description: |2-
        Teaching Assistant for [ECE69500 Optimization for Deep Learning](https://engineering.purdue.edu/ECE/Academics/Undergraduates/UGO/CourseInfo/courseInfo?courseid=818) (Fall 2022)
        * Hold office hours and help sessions, grade homeworks and exams
        * The course discusses the optimization algorithms that have been the engine that powered the recent rise of machine learning (ML) and deep learning (DL)
        

        Teaching Assitant for [ECE20001 Electrical Engineering Fundamentals I](https://engineering.purdue.edu/ECE/Academics/Undergraduates/UGO/CourseInfo/courseInfo/UGO?courseid=716) (Summer 2022)
        * Hold office hours, grade exams and compose [Collection of Practice Problems](files/post/ECE_20001_Collection_of_Practice_Problems.pdf) of homeworks
        * The course covers the basic concepts of current and voltage, devices, theorems, and applications of direct-current (DC), 1st order, alternating-current (AC) and basic electronic components including diodes and transistors

    
  - title: Research Assistant
    company: Video and Image Processing Laboratory (VIPER), Purdue University West Lafayette
    company_url: 'https://engineering.purdue.edu/~ips/'
    location: West Lafayette, IN
    date_start: '2021-08-23'
    date_end: '2022-05-31'
    description: |2-
        Worked on the project [Image Based Plant Phenotyping: The PhenoSorg Project](https://engineering.purdue.edu/~sorghum/)

        * Generated 1 thousand synthetic high-resolution UAV RGB images with panicle labels by using image-to-image translation GANs with a ground truth dataset of 400 real UAV RGB images
        * Improved mean average precision with Intersection over Union from 0.5 to 0.95 (mAP[.5, .95]) for panicle detection task from 72\% to 79\%, and reduced Mean Absolute Percent Error (MAPE) for panicle counting task from 11.6\% to 7.2\%
        * Created labels for panicles in PhenoRover RGB images to test our approach on PhenoRover data

        Worked on the project [Technology Assisted Dietary Assessment (TADA)](http://tadaproject.org/)

        * Investigated reliable and effective methods for Fine-Grained Visual Classification (FGVC)
        * Re-implemented a hierarchy-based embedding method for encoding of categories to decrease average hierarchical distance at top 1 by 3\%, and that at top 5 by 10\% on our [VIPER-FoodNet](https://lorenz.ecn.purdue.edu/~vfn/) dataset with 82 food categories, 15 thousand images
        * Corrected the incorrect labels and bounding boxes of our VIPER-FoodNet dataset
  
  - title: Research Assistant
    company: Center for Innovation through Visualization and Simulation (CIVS), Purdue University Northwest
    company_url: 'https://www.pnw.edu/civs/'
    location: Hammond, IN
    date_start: '2020-02-01'
    date_end: '2021-05-01'
    description: |2-
        Worked on the project [Smart Ladle: Al-Based Tool for Optimizing Casting Temperature](https://www.pnw.edu/civs/2021/05/18/civs-presented-smart-ladle-at-aist-digital-transformation-forum-2021/)
  
        * Developed a machine learning application using DNN, lightGBM to provide steel casting temperature predictions
        * Reduced Root Mean Square Error (RMSE) of predicted casting temperature to 3 degrees Fahrenheit
        * Collaborated application with SQL database and GUI using Unity (C\#) to display predictions and parameters
        * Tested and deployed this tool at Steel Dynamics Inc (SDI) Butler Division, awarded [AIST 2022 Hunt-Kelly Outstanding Paper Award -- third place (AIME)](https://www.pnw.edu/civs/2022/03/17/smart-ladle-won-aist-hunt-kelly-outstanding-paper-award/) and [AIST 2021 Digitalization Applications Technology Best Paper Award](https://www.pnw.edu/civs/2020/12/01/civs-paper-selected-for-2021-aistech-best-paper-award/)
---
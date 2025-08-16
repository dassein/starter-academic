---
# An instance of the Services widget.
# Documentation: https://wowchemy.com/docs/page-builder/
widget: services

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 35

title: Services
subtitle: Professional Services & Memberships

# Content.
# Choose your content from the following options:
#   - `content`: A markdown file content that will be displayed in the widget
#   - `items`: A list of services items
#   - `design`: A custom design for the widget

# Uncomment the following line and select a file to display a markdown file:
# content:
#   filename: services.md

# Choose the following options:
#   - `icon`: A Font Awesome icon name (without fa prefix)
#   - `icon_pack`: Name of the icon pack, in this case `fa` for font-awesome
#   - `name`: Title of the service
#   - `description`: Description of the service

items:
  - icon: fa-graduation-cap
    icon_pack: fa
    name: Conference Reviewer
    description: |
      **[International Conference on Machine Learning (ICML)](https://icml.cc/)**  
      **[Conference on Uncertainty in Artificial Intelligence (UAI)](https://www.auai.org/)**  
      **[International Conference on Artificial Intelligence and Statistics (AISTATS)](https://aistats.org/)**  
      **[IEEE International Conference on Multimedia and Expo (ICME)](https://www.ieee-icme.org/)**  
      **[Annual Conference on Vision and Intelligent Systems (CVIS)](https://uwcvis.github.io/)**

  - icon: fa-journal-whills
    icon_pack: fa
    name: Journal Reviewer
    description: |
      **[IEEE Transactions on Signal Processing (TSP)](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=78)**  
      **[Plant Methods](https://plantmethods.biomedcentral.com/)** - Online journal for the plant research community

  - icon: fa-users
    icon_pack: fa
    name: Professional Memberships
    description: |
      **[IEEE Young Professionals](https://yp.ieee.org/)**  
      **[IEEE Signal Processing Society](https://signalprocessingsociety.org/)**  
      **[IEEE Computer Society](https://www.computer.org/)**  
      **[Association for Iron & Steel Technology (AIST)](https://www.aist.org/)** - Former member  
      **[Material Advantage](https://materialadvantage.org/)** - Former member

design:
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns: '2'
  # Toggle between the standard `card` view and a more professional `bordered` view.
  card_style: 'bordered'
  # Background color
  background:
    # Name of a pre-defined color palette to use (see `assets/scss/palettes/`)
    color: palette_1
    # Uncomment to use a custom color, if you have defined it in `assets/scss/palettes/_custom.scss`
    # color_custom: '#f4f4f4'
  # Text color (true=light or false=dark)
  text_color_light: false 
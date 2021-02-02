---
title: Python Fundamentals
date: 02/02/2021
level: Basics
mentors: 
  - TimSando
  - ghandic
---

# {{ title }}

{{ config.site_url }}

| Key | Info |
|-----|-------|
| Created date | {{ date }} |
| Level | {{ level }} |
| Mentor{% if mentors|length > 1%}s{% endif %} | {% for mentor in mentors %}<a href="{{ config.site_url }}/contributing/#mentor-{{ mentor }}"><img style="border-radius:50%;width:50px;height:50px;margin-right:8px;" src="https://github.com/{{ mentor }}.png"></a>{% endfor %} |
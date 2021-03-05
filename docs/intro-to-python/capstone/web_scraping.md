---
title: Application - 🕸️ Web scraping
date: 06/02/2021
mentors: 
  - LungLung123
tags:
  - Web scraping
links:
  - '[Capstone template code](https://github.com/CapgeminiInventIDE/PyCap/tree/main/src/intro-to-python/capstone/web_scraping){target=_blank}'
---

{{ course_summary(title, date, mentors=mentors, links=links) }}

# PyCap Intro to Python Capstone - Scraping the web for data

Capstone example of applying the learnings from PyCap intro to Python and create a web scraper to programmatically gather information 
## Problem
### Introduction to Web Scraping 
Create a basic commandline application using Python 3.6+ that allows a user scrap an information from various website. 
In this exercise we will scrape 2 website, stock information from ASX and job postings on indeed.
#### Starting point for Web Scraping
The starting step for webscraper is to familiarise yourself with the website you want to gather information from. These steps can include examining the website's URL
and inspecting the website (Press F12 on your keyboard) for the element you're interested in.
##### Example
![indeed's URL](../../assets/imgs/indeed_url.png)

As it can be observe that some of the information can already be pick up such as the query for data scientist and location of Sydney, NSW

![indeed's element](../../assets/imgs/indeed_inspected.png)

We can also observe from inspecting the page, we found out that the salary information is under a class "SalaryText", which we can use to implement our scraper. 
### Basic Data Analysis
We will also introduce some basic data analysis on the the scraped data as well. 
- With ASX data, we will see if we could determine the change in stock price based on the ASX Today Annoucement. 
- With Indeed data, we will see if we can filter our scraped data and display jobs within our specified salary.    
## Coding Standard and Practice
Your code should be well documented with a docstrings, comments and a README describing how your program works, unit tests to ensure it works as expected and type annotations and finally well formatted using Black. This is so other developers can understand how to help build upon your program.

You should add a summary to your README that includes the next steps (dot points) and also the strengths and weaknesses of your program in its current state.
A list of operations that your app should support, as well as how we expect them to show up can be found in the table below.


| Operation                                            | Usage | Description |
|------------------------------------------------------|-------|-------------|
| Start a scaping from the provided link | `"python3 webscraper.py "<Site URL>""` |
| Begin Scraping | | `"Starting Scraping"` |
| Finish Scraping | | `"Successfully Scraped the "<Site URL>""` |

## Suggested URL for Webscraping

- https://www2.asx.com.au/markets/trade-our-cash-market/todays-announcements
- ASX URL of the companies you are interested in (Hint, you can store a list of company in a list)
- https://au.indeed.com/jobs?q=data+scientist&l=Sydney+NSW
- Indeed URL with your job and city queried (Hint, you can store a list of job in a list)

## Suggested Library

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) 
- [Scrapy](https://scrapy.org/)
- [Selenium](https://selenium-python.readthedocs.io/)
- When in doubt, **Research** and **Google** are your friends :sunglasses:

## Discliamer
Certain websites do impose restrictions and on scraping/gathering their data and information programmically. 
Due to the simplicity of our scraper, if the script doesn't work and your code looks fine, it could mean that the sites contain levels of security to prevent
scraping.

These sites can also have Term and Conditions impose restriction on the automation data gathering tool. 
Since you are not using them for commercial purpose, you should be in a clear. However always check for TOCs in the future
### Example of TOCs:
![Seek's TOCs](../../assets/imgs/web_scrap_TOS.jpg)

## Optional Extras

- Enhance the scaper further and save the information out into csv file
- Analyse and utilise the data and create an application from it 
- Example for Advance usage: Algorithm Trading on stock information or Resume Skill Matching for job posting
# PyCap Intro to Python Capstone - Scraping the web for data

Capstone example of applying the learnings from PyCap intro to Python and create a web scraper to programmatically gather information 

## Problem

Create a basic commandline application using Python 3.6+ that allows a user scrap an information from various website. In this exercise we will scrape
2 website, stock information from ASX and job postings on indeed.

Your code should be well documented with a docstrings, comments and a README describing how your program works, unit tests to ensure it works as expected and type annotations and finally well formatted using Black. This is so other developers can understand how to help build upon your program.

You should add a summary to your README that includes the next steps (dot points) and also the strengths and weaknesses of your program in its current state.
A list of operations that your app should support, as well as how we expect them to show up can be found in the table below.


| Operation                                            | Usage | Description |
|------------------------------------------------------|-------|-------------|
| Start a scaping from the provided link | `"python3 webscraper.py "<Site URL>""` |
| Begin Scraping | | `"Starting Scraping"` |
| Finish Scraping | | `"Successfully Scraped the "<Site URL>""` |

## Discliamer
Certain websites due impose restrictions and on scraping/gathering their data and information programmically. 
Due to the simplicity of our scraper, if the script doesn't work and your code looks fine, it could mean that the sites contain levels of security to prevent
scraping.

These sites can also have Term and Conditions impose restriction on the automation data gathering tool. 
Since you are not using them for commercial purpose, you should be in a clear. However always check for TOCs in the future
### Example of TOCs:
![Seek's TOCs](images/web_scrap_TOS.jpg)

## Optional Extras

- Enhance the scaper further and save the information out into csv file
- Utilise the data and create an application from it 
- Example for Advance usage: Algorithm Trading on stock information or Resume Skill Matching for job posting

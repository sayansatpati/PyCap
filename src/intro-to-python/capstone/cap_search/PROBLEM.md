# PyCap Intro to Python Capstone - 🕵️ Building a basic search engine

## Problem

Create a command line application using Python 3.6+ that allows you to create and search a database of documents using TF-IDF. The TF-IDF should be created using native python with no external libraries for the logic.
Your code should be well documented with docstrings, comments and a README describing how your program works, unit tests to ensure it works as expected, type annotations to allow other developers to understand how to help build upon your program and finally well formatted code (using Black).

You should add a summary to your README that includes the next steps (dot points) and also the strengths and weaknesses of your program in its current state.
A list of operations that your program should support, as well as how we expect them to be called can be found in the table below.

| Operation                                            | Usage | Required |
|------------------------------------------------------|-------|----------|
| Upload a document to the search engine database. | `python cap_search.py upload "/path/to/document.txt"` | TRUE |
| Upload all .txt documents in a directory to the search engine database. | `python cap_search.py upload-directory "/path/to/directory"` | TRUE |
| Upload a newer version of an existing document to the search engine database. | `python cap_search.py update "/path/to/document.txt"` | TRUE |
| Get a document from the search engine database to the current directory. | `python cap_search.py get "document_name"` | TRUE |
| Get a document from the search engine database to the specified directory. | `python cap_search.py get "document_name" --path /path/to/output/document.txt` | TRUE |
| Delete a document from the search engine database. | `python cap_search.py delete "document_name"` | TRUE |
| Search the database for a document using the given terms. | `python cap_search.py search "terms to search"` | TRUE |
| Search the database for a document and return it using the given terms and path. | `python cap_search.py search "terms to search" --return-path /path/to/output/document.txt` | TRUE |

## Optional Extras

Implement stop word removal and stemming to increase the quality of the TF-IDF estimates. You may use external libraries for this if you wish.

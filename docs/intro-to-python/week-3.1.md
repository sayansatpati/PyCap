---
title: Workflow - Formatting
description: Formatting is critical to the readability of code repositories and we'll cover off what formatting means for Python code and how to apply it to your coding
prev_know: None
skills:
  - Formatting
  - Linting
  - MyPy
date: 08/02/2021
mentors: 
  - TimSando
  - ghandic
links:
  - '[Index of Python Enhancement Proposals (PEPs)](https://www.python.org/dev/peps/){target=_blank}'
  - '[PEP8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/){target=_blank}'
  - '[Flake8 Documentation](https://flake8.pycqa.org/en/latest/){target=_blank}'
  - '[Black Github Repo](https://github.com/psf/black){target=_blank}'

---

{{ course_summary(title, date, description=description, prev_know=prev_know, skills=skills, mentors=mentors, links=links) }}

## Why do we want to write readable code?

Writing code that works is important to meet specifications and is often the main focus when delivering a project. However, one the most important and often overlooked aspects of writing good code is writing good **readable** code. Focusing on the readability of code has the following benefits:

- Easier to understand and follow for other developers
- Better explainability when someone wants to know what a particular function does
- Simpler to maintain and improve existing code when people know what's happening

All of the above results in code that will have fewer bugs, better uptake and improved growth potential whether it's a personal project that you're open sourcing or a piece of work you're handing over to a client to implement within their own systems. If someone else can't understand your code then why would they want to use it?

## How should I format my code?

Formatting and you, how to improve your code's readability

Python has a subset of Python Enhancement Proposals (PEPs) dedicated to formatting guidelines to promote a standardised approach to python coding and formatting within the python community. We've previously touched on one of the more widely quoted formatting PEPs, **PEP 20 -- The Zen of Python**, which provides some broad tenets to apply when writing python code.

```python
import this

"""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
```

Other PEPs commonly referenced when determining how to format code include:

- '[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/){target=_blank}'
- '[PEP 216 -- Docstring Format](https://www.python.org/dev/peps/pep-0216/){target=_blank}'
- '[PEP 3101 -- Advanced String Formatting](https://www.python.org/dev/peps/pep-3101/){target=_blank}'

Reading through all these formatting standards and ensuring you apply them consistently throughout your can be an absolute nightmare and takes many years of experience to get completely right. Luckily we have some methods to avoid all this manual work and automatically format our code.

## Applying a formatter

Some of the more popular code formatters for python include:

- Black
- isort
- autopep8
- YAPF

which are all viable and a lot comes down to personal preference or professional coding standards. At Capgemini Invent we use isort to order package imports followed by Black as our primary formatter with a line length of 120 (--line-length=120 is the argument to apply this when running Black). To apply these functions you need to ensure they're installed:

Isort

```bash
pip3 install isort
```

Black

```bash
pip3 install black
```

and then run the following to apply the formatting:

Isort

```bash
isort -rc myproject_dir
```

Black

```bash
black src --line-length=120
```

If you are using an IDE (VSCode is the IDE of choice for Capgemini Invent) then you can generally set the IDE to format on save in the settings. This will format your file whenever you save (which should be all the time!).

## Linting, what is it?

When focusing on writing readable code, one other aspect to consider alongside formatting is linting, which is the act of using a linter program to automatically identify syntactical and stylistic problems within your code. Using a linter helps you identify errors in your code and calls out unconventional coding practices which might lead to errors.

## Linters

Python has a number of linters that you can use to help lint your code. In VSCode by default, the available linters include:

- Pylint (the default for VSCode)
- Flake8 (Capgemini Invent's recommended linter)
- MyPy (Used by Capgemini Invent for type annotation checking)
- Pydocstyle
- Pydocstyle (pep8)
- prospector
- pylama
- bandit

## Applying a linter

If you want to install and run a linter across your code to call out any potential errors, then you can do the following:

```bash
# installing flake8 in your python dev environment
pip3 install flake8
```

```bash
# apply flake8 to your project directory
flake8 myproject_dir
```

Running a linter in the manner above will print out any errors it has identified in the terminal for you to investigate.

Linters can also be installed as separate extensions within your IDE of choice rather than installed through python. When you have chosen what linter you want to use for development, it will automaticaly identify potential errors in your code through visial indicators (red lines under your code) and hovering above these should give you a more detailed description of what it has called out.

Because they are simply a program looking through your code and comparing it against installed libraries, dependencies and a range of other factors, they can be prone to identifying false positives, especially if you're working on remote development in containers where they're unable to access what libraries you have installed. However, linters are still are an incredibly important and valuable tool to support writing understandable and explainable code.

To help you when working on your capstone project, we've included a simple script *`coverage.sh`* that will go through and run autoflake, flake8, isort and black to format the code and use pytest, mypy and interrogate to generate code, type annotations and docstring coverage. You can look further into that file for more information around specific arguments.

## Adding TODO comments

We've touched on how adding comments to your code can help other developers understand what a specific line of code does. Another use of comments is to identify areas for future development that you might not have time for right now, don't want to forget about and want to easiy find later on. The most common method of doing this is by adding a TODO comment.

```python
# TODO: Look into why this is taking so long
```

This allows a developer to search through the code for TODO to quickly locate areas that have previously been identified for improvement. Which can be especially handy if you're handing off the code to someone else who isn't as comfortable with the code as you are.
---
title: Workflow - Type Hints
description: We've gone through formatting your code and applying linting to detect errors throughout your code, in this section we'll cover off type hinting and how it can be useful to futher improve the readability of your code.
prev_know: None
skills:
  - Type hints
date: 08/02/2021
mentors: 
  - TimSando
  - ghandic
links:
  - '[Python Type Hint Documentation](https://docs.python.org/3/library/typing.html){target=_blank}'
---

{{ course_summary(title, date, description=description, prev_know=prev_know, skills=skills, mentors=mentors, links=links) }}

## What is type hinting?

Type hinting was introduced as part of Python 3.5 whereby declared variables in a function can have their data type defined. This doesn't change how the function operates because Python won't check whether the varible sent to the function is the appropriate type based on the type hint at runtime. However, type hints are valuable for type checkers, linters, IDEs etc. to help you code faster and identify errors before they occur.

## Input type hinting

If we look at a basic function:

```python
def type_hunt(var, var_i):
  total_var = var[0] + str(var_i)
  return total_var
```

we have defined a function that has two input variables var and var_i and both of them are required (they don't have a default value). However, we have no idea what format/type the function is expecting var and var_i to be as var_i. If we write the same function with type hinting, we'd get the following:

```python
from typing import List

def type_hunt_(var: List[str], var_i: int = 2):
  total_var = var[0] + str(var_i)
  return total_var
```

By defining that var is expected to be a list of strings, and var_i is expected to be an integer, the function itself becomes a lot easier to understand for someone reading through your code. We have also set var_i to default to 2 when no argument is provided so we're clear that it's optional and neither python or the IDE will raise an error that not enough arguments are provided when the function is called without var_i.
Type hinting in this way also allows an IDE or type hinter to visually alert you when you try to to pass in a variable of the incorrect type (usually denoted by a red underline within your code).

## Output type hinting

The other aspect of type hinting is defining what is being returned.

```python
def type_hunt_(var: List[str], var_i: int) -> str:
  total_var = var[0] + str(var_i)

  return total_var
```

In this function we have defined that we're expecting total_var to be returned as a string so any functions that take in total_var as in input can then be coded and appropriately.

Some other examples of different types commonly seen in functions and declared using type hinting:

```python
def examples_typing(is_it: bool = True, coords: tuple, multiple: float, options: list, option_info: dict) -> float:
  pass
```
---
title: Using User Defined, Internal and External Libraries
description: Desc...
prev_know: None
skills:
  - import
  - Packages
  - User Defined Packages
  - Pip
  - Standard Library
date: 02/02/2021
mentors: 
  - TimSando
  - ghandic
links:
  - '[Coursera follow along course (Weeks 1, 2, 3)](https://www.coursera.org/learn/python?specialization=python#syllabus){target=_blank}'
  - '[Real Python - Introduction](https://realpython.com/python-introduction/){target=_blank}'

---

{{ course_summary(title, date, description=description, prev_know=prev_know, skills=skills, mentors=mentors, links=links) }}

## Importing functionality

Now we have covered off how to define our own functions we may want to use these throughout our python program. We may also want to make use of external python packages and the functionality they offer. This can be done using the `import` keyword at the beginning of the python file. It will look for user defined modules, installed modules and standard library modules and bring in the functionality of that script.

### External and standard library modules

When using any packages you haven't written it is generally best to look online for documentation on how to make use of the library's functionality. For example, if we look for the documentation of the `pathlib` library we can see that we can make use of `Path` by using `from pathlib import Path`. Likewise for a package we may have installed, such as `Pillow` we can see that we can import the `Image` functionality as `from PIL import Image`. These would be added to the beginning of our program if we wish to make use of them in our script.

Note that it is best practice to group your import statements into the following sequence:

1. Standard libraries (functionality you haven't installed)
2. External libraries (functionality you have installed into your system)
3. User defined modules (functionality you have created in your filesystem)

So far our file is looking like this:

```python
from pathlib import Path

from PIL import Image
```

### User defined modules

If we want to make use of our functionality between files and folders then this is where user-defined modules comes into play. Lets make a file called `main.py` and a file called `welcome.py` and add our welcome user function into `welcome.py`.

If we are now working on `main.py` and want to make use of the functionality inside `welcome.py` we can do this as follows:

```python
import welcome

print(welcome.welcome_user("Andy"))
```

We could also import it using `import` and `from` to indicate that we just want to import the specific functionality proceeding the `import` keyword. This will also remove the `welcome` namespace

```python
from welcome import welcome_user

print(welcome_user("Andy"))
```

Finally we can also make use of folders to subdivide our work into, lets copy the `welcome.py` file into a folder called `utils`. We will also look at the `as` keyword, which lets us define what it will be called from in our script.

```python
from utils.welcome import welcome_user as wu

print(wu("Andy"))
```

This `as` keyword is often used with libraries such as `numpy` and `pandas` (`import numpy as np` or `import pandas as pd`) and it just saves us typing out the full name.

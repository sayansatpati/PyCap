---
title: Object Oriented Programming
description: In this session we will be looking at Python and the filesystem and file structures, how and when they can be used within your Python programs.
prev_know: None
skills:
  - Object Oriented Programming
  - OOP
  - Encapsulation
  - Polymorphism
  - 
date: 02/02/2021
mentors: 
  - TimSando
  - ghandic
links:
  - '[Coursera follow along course](https://www.coursera.org/learn/python-data?specialization=python#syllabus){target=_blank}'
  - '[Coursera follow along course 2](https://www.coursera.org/learn/python-databases?specialization=python#syllabus){target=_blank}'
  - '[Real Python - Object Oriented Programming](https://realpython.com/python3-object-oriented-programming/){target=_blank}'
  - '[Article - Forgotten History of OOP](https://medium.com/javascript-scene/the-forgotten-history-of-oop-88d71b9b2d9f){target=_blank}'

---

{{ course_summary(title, date, description=description, prev_know=prev_know, skills=skills, mentors=mentors, links=links) }}

## Object Oriented programming in Python - Classes

### Reflection on inbuilt Python classes

If we look back to the first session we did on data types in Python we can recall that there are inbuilt data types such as strings, lists, dictionaries, etc. All of these are examples of classes and they have their own methods and attributes. For example, we can make a string and the split the string on spaces to give a list of strings.

```python
demo_string = "Hello world"
print(demo_string.split(" ")) # => ['Hello', 'world']
```

This is an example of a method that the string class has. Note this method is not available for integers, dictionaries, lists etc.

#### Instantiating, Attributes and Methods

We can see what attributes and methods a instance has access to by using the built in function `dir()` if we use `dir("")` then we get the following:

```json
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', 
'__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 
'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 
'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 
s'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

This shows all of the normal methods/attributes (indicated by no prefixed underscores) as well as "private" methods/attributes (indicated by prefixed underscores) that the class has access to. Their are also special methods called **dunder methods** (double underscore methods) and these are methods that Python will use in special ways. So for instance the `__add__` method seen above will concatenate strings in this instance. The `__init__` method will initialise an object so will be the first thing that is ran when making an object of that class.

### Making our own classes

We can make our own classes in Python using the `class` keyword, note that a class does not need to do anything by itself. We can instantiate a object of a given class by using the class name followed by parenthesis.

```python
class Demo:
    pass

d = Demo()
```

This is a relatively useless class though so lets make a more useful class called `Square`, it will inherit from the Python base class which is called `object` (essentially meaning it inherits form no other class). We will also instantiate it with `x` which is the side length of the square. `x` is now an attribute of Square and can be accessed by using the `.` and the attribute name

We have also added a method `area` which will return the area of the given square. Notice the keyword `self` which means that we are accessing information from the current object to use the method.

```python
class Square(object):

    def __init__(self, x):
        self.x = x

    def area(self):
        return self.x ** 2

s = Square(5)
print(s.x) # => 5
print(s.area()) # => 25
```

In Python version 3.7 onwards there is some extra convenience methods for building your classes. These are called `dataclass`es, we will compare side by side the difference

=== "Python < 3.7"

    ```python
    class Square(object):
        def __init__(self, x, name, color, rounded):
            self.x = x
            self.name = name
            self.color = color
            self.rounded = rounded
        
        def area(self):
            return self.x ** 2
    ```

=== "Python >= 3.7"

    ```python
    from dataclasses import dataclass

    @dataclass
    class Square(object):
        x: float
        name: str
        color: str
        rounded: bool
        
        def area(self):
            return self.x ** 2
    ```

### Using dunder methods to define our own operator functionality

We have already used one dunder method, namely the `__init__` method. Lets also use the `__add__` and `__repr__` dunder methods to define what it means to add two Squares

```python
class Square(object):
    
    def __init__(self, x):
        self.x = x

    def area(self):
        return self.x ** 2

    def __add__(self, other):
        return Square(self.x + other.x)

    def __repr__(self):
        return f"Square of length {self.x}"

s1 = Square(5)
s2 = Square(10)

s3 = s1 + s2
print(s3) # => Square of length 15
```

### Building a context manager

We can make use of two more dunder methods, `__enter__` and `__exit__` which will make our object able to use the keywords `with X as:` similar to the `with open(filename, mode) as file:`

```python
class Square(object):
    def __init__(self, x):
        print("Initializing")
        self.x = x

    def __enter__(self):
        print("Entering")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting")

    def area(self):
        return self.x ** 2
        
    def __add__(self, other):
        return Square(self.x + other.x)

    def __repr__(self):
        return f"Square of length {self.x}"

with Square(5) as s:
    print(s)

# => Initializing
# => Entering
# => Square of length 5
# => Exiting
```

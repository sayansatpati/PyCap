---
title: Functions
description: In this session we will be looking at functions. We will discuss how and when they can be used within your Python programs.
prev_know: Data Structures
skills:
  - Functions
date: 02/02/2021
mentors: 
  - TimSando
  - ghandic
links:
  - '[Coursera follow along course (Weeks 4, 5, 6)](https://www.coursera.org/learn/python?specialization=python#syllabus){target=_blank}'
  - '[Real Python - Functions](https://realpython.com/defining-your-own-python-function/){target=_blank}'
  - '[CodeWars - Is he gonna survive?](https://www.codewars.com/kata/59ca8246d751df55cc00014c){target=_blank}'
  - '[CodeWars - Remove First and Last Character](https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0){target=_blank}'
  - '[CodeWars - Name Shuffler](https://www.codewars.com/kata/559ac78160f0be07c200005a){target=_blank}'
  - '[CodeWars - Vowel remover](https://www.codewars.com/kata/5547929140907378f9000039){target=_blank}'
  - '[CodeWars - Total amount of points](https://www.codewars.com/kata/5bb904724c47249b10000131){target=_blank}'
  - '[CodeWars - DNA to RNA Conversion](https://www.codewars.com/kata/5556282156230d0e5e000089){target=_blank}'
  - '[CodeWars - Can we divide it?](https://www.codewars.com/kata/5a2b703dc5e2845c0900005a){target=_blank}'
  - '[CodeWars - HQ9+](https://www.codewars.com/kata/591588d49f4056e13f000001){target=_blank}'
  - '[CodeWars - Chuck Norris Approved](https://www.codewars.com/kata/570669d8cb7293a2d1001473){target=_blank}'
  - '[CodeWars - Drink About](https://www.codewars.com/kata/56170e844da7c6f647000063){target=_blank}'
  - '[CodeWars - Sort & Transform](https://www.codewars.com/kata/57cc847e58a06b1492000264){target=_blank}'

---

{{ course_summary(title, date, description=description, prev_know=prev_know, skills=skills, mentors=mentors, links=links) }}

## Functions

### Why use functions

- Readable - Reading lots of blocks of code that do the same thing is hard to follow.
- Writeable - When using functions, you're saving yourself time from copy pasting or typing ou the same thing
- Reuseable - You can reuse your functions in any other program as long as they are *encapsulated*

### How to make functions in Python

In Python we can **def**ine a function using the keyword **def** followed by the function name, parenthesis and any arguments (sometimes called parameters from mathematics). A function can run pieces of code for us and optionally return a given value. If you do not give a **return** value then the function will return `None`.

```python
def my_function_name(argument_1, argument_2):
    return argument_1 + argument_2
```

This function can now be called later on in our script as follows:

```python
x = 1
y = 2
answer = my_function(argument_1=x, argument_2=y)
print(answer)
```

### Scope of variables

The scope of a variable is referring to where it is stored and whether it is accessible from a certain point. There are two kinds of scope in Python `local` and `global` scope. Lets take a look at an example.

```python
x = 5

def do_something():
    x = 10
    print(x)

print(x) # => 5
do_something() # => 10
print(x) # => 5
```

As you can see from the printed output when we use the variable x in the function it is not effecting the x outside of the function. This is what is meant my scope, the x in the function is part of the `local` scope and the x outside is part of the `global` scope. We can access the global scoped variable using the `global` keyword. However, this is generally not a best practice as if you want to alter a global variable you should do this by returning a new variable.

```python
x = 5

def do_something():
    global x
    x = 10
    print(x)

print(x) # => 5
do_something() # => 10
print(x) # => 10
```

As a quick tip, try using the functions `globals()` and `locals()` while inside a function. This will show you what variables are currently in scope.

```python
x = 5

def do_something():
    x = 10
    print(globals())
    print(locals())

do_something()
# {'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'do_something': <function do_something at 0x10b25e140>, 'x': 5, '__name__': '__main__', '__doc__': None}
# {'x': 10}
```

### Passing in arguments/parameters

We can pass in different arguments (sometimes called parameters from mathematics) into our functions to make use of them from within the local scope. We did this before with the `my_function_name` function.

#### Positional arguments

When calling (using) a function we can make use of the position of which the arguments were givne in when declaring (writing) the function. For example in `my_function_name(argument_1, argument_2)` we could call the function with positional arguments as follows:

```python
x, y = 1, 2
answer = my_function_name(x, y)
print(answer)
```

This means that `argument_1` is given by `x` which is `1` and `argument_2` is given by `y` which is `2`.

#### Keyword arguments

Similarly we can use keyword arguments to call a function, this is where we explicitly say which argument we are using.

```python
x, y = 1, 2
answer = my_function_name(argument_2=x, argument_1=y)
print(answer)
```

Notice that now we can add these in in any order, so we can reverse the order as seen above.

> Note: when using a combination of keyword and positional arguments you must use the positional arguments first and the keyword arguments at the end (see below for an example)

```python
x, y = 1, 2
answer = my_function_name(x, argument_2=y)
print(answer)
```

#### Default arguments

When declaring a function we can set default arguments, this way we can change them if we like, or we can just use what the developer has suggested as default. For example:

```python
def my_function_name(argument_1, argument_2=5):
    return argument_1 + argument_2

answer = my_function_name(2)
print(answer)
```

Or we can use the function just as before

```python
def my_function_name(argument_1, argument_2=5):
    return argument_1 + argument_2

answer = my_function_name(2, 10)
print(answer)
```
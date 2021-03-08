---
title: Data Structures
description: In this session we will be looking at data structures. We will discuss how and when they can be used within your Python programs.
prev_know: None
skills:
  - Booleans
  - Strings
  - Integers
  - Floats
  - Lists
  - Sets
  - Dictionaries
date: 02/02/2021
mentors: 
  - TimSando
  - ghandic
links:
  - '[Coursera follow along course (Weeks 4, 5, 6)](https://www.coursera.org/learn/python?specialization=python#syllabus){target=_blank}'
  - '[Real Python - Data Types](https://realpython.com/python-data-types/){target=_blank}'
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

## Facts for the session

- The etymology of the word "string" dates back to the days of the printing press, where characters or "font" as they were called back then were assembled to put together to form a stamp that could be pressed against paper with ink to form a page for a book. When the printing press companies charged for their services, they would charge in the length of characters in feet. To do this they would string together the characters required. Hence the use of "string" for multiple characters put together! This is also where the words "uppercase, lowercase and font" come from, both upper and lowercase from the position where the fonts were stored - in the top or bottom cases and "font" comes from the french word "fonte" which means "something that has been melted; a casting".
- Python's mantra, otherwise called the "Zen of Python" is below, the most important part is the first 4 lines. Python aims to be simple for you to read and write, code that follows this mantra is called "Pythonic".

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

## Comments

A comment in Python is given by a preceding `#` sign and it will be ignored by Python. They can either be inline or have their own line.

```python
# Creating a variable with the string "Andy"
name = "Andy" # An inline comment about this line
```

## Useful inbuilt functions to deal with types

The built-in function `type` allows us to check what type an object is

```python
type(True) # This gives - bool
type(1) # This gives - int
type(1.0) # This gives - float
type("Hello") # This gives - str
type([]) # This gives - list
type({}) # This gives - dict
type(set()) # This gives - set
```

We can also use the built-in function `isinstance` which will do a logical check if the object we give it is what we are expecting.

```python
isinstance(False, bool) # This gives - True
isinstance(1, int) # This gives - True
isinstance(1.0, float) # This gives - True
isinstance("Hello", str) # This gives - True
isinstance([], list) # This gives - True
isinstance({}, dict) # This gives - True
isinstance(set(), set) # This gives - True

isinstance(False, dict) # This gives - False
isinstance(1, str) # This gives - False
isinstance(1.0, int) # This gives - False
isinstance("Hello", bool) # This gives - False
isinstance([], dict) # This gives - False
isinstance({}, set) # This gives - False
isinstance(set(), float) # This gives - False
```

## Operators

- `+` is the **add**ition operator
- `-` is the **sub**traction operator
- `/` is the **div**ision operator
- `*` is the **mul**tiplication operator
- `**` is the **pow**er operator
- `//` is the **floor div**ision operator
- `%` is the **mod**ulo operator

These are the basic operators in Python and they will do different things depending on the types of values you have on either side of the operator. Let's look at a few examples:

**Example 1**: Integer + Integer

```python
print(4 + 5) # This gives 9, so uses normal arithmetic.
```

**Example 2**: String + String

```python
print("Hello " + "World") # This gives "Hello World", so uses concatenation.
```

**Example 3**: Int + String

```python
print(1 + "World") # This gives an error as it is not defined how an integer can add a string.
```

The aim of the above examples are to show that operators on their own don't mean anything, it is dependant only on what the operator means to that data type.

Later on in the series we will explore "dunder" methods, short for double underscore methods. These are special methods that an object can have to implement different python operators. For example `__add__` implements the **add**ition operator for a class.

## Numbers

### Integers, Floats

For the most part, integers and floats are interchangeable and you can treat any operators that they use to be just like using a calculator. However, there will be times when you will need to make sure the number is an integer or a float. To do this we can convert between the types.

```python
int(2.2) # This gives - 2
float(2) # This gives - 2.0

int(2.8) # This gives - 2
float(-1) # This gives -1.0
```

One reason why we must have an integer rather than a float would be in a list. If we have a shopping list of groceries, what would it mean to get the 2.5'th item in the list? It wouldn't make sense, but to get the 2nd item would.

## Booleans

Booleans are just logical values and can either be `True` or `False`, if we use these in mathematical operations they will equate to 1 and 0 respectively. Later on in the session we will look at conditional statements and how we can control the flow of our program based on logic.

## Strings

As mentioned in the beginning strings are just a series of characters put together. There are many things we can do with strings that are helpful to building custom programs. For example, using someones name we can make a custom dashboard for them where they feel like it was tailored to themselves.

A string can be represented using single or double quotes (`'` or `"`) these will allow a string to be made all in one line. There is also a multiline string which is given by triple-single or triple-double quotes (`'''`, or `"""`) For example:

```python
name = "Andy Challis"
weather = 'Sunny'

poem = """Do not stand at my grave and weep
I am not there; I do not sleep.
I am a thousand winds that blow,
I am the diamond glints on snow,
I am the sun on ripened grain,
I am the gentle autumn rain.
When you awaken in the morning's hush
I am the swift uplifting rush
Of quiet birds in circled flight.
I am the soft stars that shine at night.
Do not stand at my grave and cry,
I am not there; I did not die."""

second_poem = '''Hold fast to dreams
For if dreams die
Life is a broken-winged bird
That cannot fly.
Hold fast to dreams
For when dreams go
Life is a barren field
Frozen with snow.'''
```


### String formatting

One should avoid using the string concatenation technique as shown earlier, as it can lead to code that is hard to read, eg: `"Hello " + name + ", the outlook for the weather today looks like it will be " + weather`. Instead we can make use of string formatting and there are a few ways to do this in Python.

**Example 1** - Using the f-string, this is the best practice at the time of writing and I would suggest making use of this as much as possible as it allows you to write expressions inside the string.

```python
name = "Andy Challis"
weather = "Sunny"
f"Hello {name}, the outlook for the weather today looks like it will be {weather}"
```

**Example 2** - Using the `.format()` this was the previous best practice before Python 3.6, it is still able to be used. However, if you read the string you need to go to the end to understand what is being added into the formatted string. You can use the second example but this is more terse that using f-strings.

```python
name = "Andy Challis"
weather = "Sunny"
"Hello {}, the outlook for the weather today looks like it will be {}".format(name, weather)
# OR
"Hello {name}, the outlook for the weather today looks like it will be {weather}".format(name=name, weather=weather)
```

**Example 3** - Using the `%` this is old school Python string formatting syntax you may still see around, `%s` stands for string to come in, `%d` means a number will be coming in

```python
name = "Andy Challis"
weather = "Sunny"
"Hello %s, the outlook for the weather today looks like it will be %s" % (name, weather)

age = 99
"You are %d years old" % age
```

## Lists, Sets and Tuples

### Lists

A list is just like you imagined, you can have a list of items each having their own position in the list which you can "index" by a number eg the 3rd item of the list. In Python we use a zero index, therefor the "2nd item" of a list would be index 1 as the first would be index 0.

A list can be defined using square brackets `[]`, this is an empty list and has no items inside it. we can add in other data types into our list and in Python it doesn't matter what is in the list! You can have floats, integers, strings, whatever you want! Lets make a shopping list as an example.

```python
shopping_list = ["Apple", "Apple", "Apple", "Milk", "Pear"]
```

Notice that you can have the same string in there like our apples, in this shopping list we could see that we need to get 3 apples, one milk and one pear. We can add items to the list using `.append` and we can remove items from the list with `.remove`

```python
shopping_list = ["Apple", "Apple", "Apple", "Milk", "Pear"]

shopping_list.remove("Apple")
print(shopping_list) # This gives ['Apple', 'Apple', 'Milk', 'Pear']

shopping_list.append("Banana")
print(shopping_list) # This gives ['Apple', 'Apple', 'Milk', 'Pear', 'Banana']
```

### Tuples

Now if we are to look at tuples which look like a list but are denoted with a rounded bracket `()`, we cannot do these kind of operations as tuples are **immutable** meaning we cannot change them

```python
info = ("Andy Challis", "Male")
```

### Sets

Again sets are much like lists, except you can only have at most one of each item. For example the shopping list given before if it were converted to a set would be `['Pear', 'Apple', 'Milk']`. This is great if we only care about storing unique items.

```python
shopping_list = ["Apple", "Apple", "Apple", "Milk", "Pear"]
print(set(shopping_list)) # This gives ['Pear', 'Apple', 'Milk']
```

## Dictionaries

Dictionaries are a data type that allows us to store something in that we can quickly look up, much like the oxford english dictionary. If we want to find out the meaning of a word then we find that word in the dictionary and look at its meaning. Notice how fast it is to find meanings of words once you know how to use a dictionary! This is the same in programming, under the hood it uses something called a hash table where is associates a hash key with some value. Lets make our own corporate dictionary.

Dictionaries are given by the curly braces `{}` and have keys and values separated by a colon `:`

```python
CORP = {
    "IDE": "Insight Driven Enterprise",
    "I&D": "Insights and Data",
    "P&O": "People and Organization",
    "APAC": "Asia Pacific",
}
```

We can look up information from out dictionary using the keys as an index like so

```python
print(CORP["IDE"]) # This gives "Insight Driven Enterprise"
```

We can store any data type as the values in a dictionary too

```python
profile = {
    "name": "Insight Driven Enterprise",
    "age": 99,
    "male": True,
}
```

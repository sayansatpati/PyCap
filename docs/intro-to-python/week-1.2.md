---
title: Control Flow
description: In this session we will be looking at control flow. We will discuss how and when it can be used within your Python programs.
prev_know: Data Structures
skills:
  - If, Elif, Else
  - For Loops
  - While
date: 02/02/2021
mentors: 
  - TimSando
  - ghandic
links:
  - '[Coursera follow along course (Weeks 4, 5, 6)](https://www.coursera.org/learn/python?specialization=python#syllabus){target=_blank}'
  - '[Real Python - Conditional Statements](https://realpython.com/python-conditional-statements/){target=_blank}'
  - '[Real Python - For Loops](https://realpython.com/python-for-loop/){target=_blank}'
  - '[Real Python - While Loops](https://realpython.com/python-while-loop/){target=_blank}'
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

## Control Flow

Control flow is the order in which individual statements, instructions or function calls of a program are executed or evaluated. We can change the flow of the program so that we get a different outcome, in this  next section we will look into some of the most common ways to do this.

### Conditionals

#### Operators

These operators differ from the arithmetic operators defined earlier as they would return different data types depending on what was used, for example `2 * 2.5` would return `5.0`. However, with conditional operators we will always get back a `bool` (Boolean - True/False) result as we are comparing two values.

- "==" is the **eq**uality operator
- "!=" is the **n**ot **eq**uality operator
- "<", "<=" are the **l**ess **t**than and the **l**ess **t**than or **e**qual to operators
- ">", ">=" are the **g**reater **t**than and the **g**reater **t**than or **e**qual to operators
- "is" is the identity operator
- "is not" is the negated identity operator
- "in" is the membership operator
- "not in" is the negated membership operator

#### If, else if, else

Using the above operators, we can combine them with our data structures we discussed earlier to form boolean values, as a result we can then act on those and only run a piece of code **if** the preceding value was `True`. 

**Remember Python is sensitive to indents and you  must indent  your code blocks**

```python
if 5 < 10:
    print("Only runs if 5 is less than 10")
```

This example makes more sense when we use variables as they will change throughout our program

```python
apples = 5
if apples > 10:
    print("You have too many apples")

apples = 20
if apples > 10:
    print("You have too many apples")

```

If we want to execute some other piece of code when the expression evaluated to `False`, then we can make use of `if/else`

```python
apples = 5
if apples > 10:
    print("You have too many apples")
else:
    print("Get more apples... An apple a day keeps the doctor away")
```

Finally, if you have multiple comparisons that you want to make you can use `elif`.

```python
apples = -1
if apples > 10:
    print("You have too many apples")
elif apples < 0:
    print("You cant go into debt with apples!")
else:
    print("Get more apples... An apple a day keeps the doctor away")
```

### Loops

Another way you can control out programs execution is to perform a series of actions over and over again on repeat. This could be for a fixed number of loops, or indefinitely.

#### For loops

If you want to loop over a piece of code for a fixed number of loops then we would make use of a `for` loop. To use a `for` loop, you will need to have an iterable (not irritable) data structure, such as a list, dictionary, string or tuple. Lets take the example of a list.

```python
shopping_list = ["Apple", "Apple", "Apple", "Milk", "Pear"]
for item in shopping_list:
    print(item)
```

Notice we assigned each value in turn to the variable `item`, we can call this variable whatever we like, but you should always make it make sense, for example, `for bird in birds:`

If we also need to have access to the index of the item in the iterable then we should make use of the inbuilt function `enumerate`, which will give you a tuple of the position in the iterable and the item itself.

```python
shopping_list = ["Apple", "Apple", "Apple", "Milk", "Pear"]
for index_with_item in enumerate(shopping_list):
    print("Item:", index_with_item[1])
    print("Index:", index_with_item[0])
```

This is starting to look a little messy, Python has a better way to handle tuple assignment which is called **unpacking**, which allows you to write the same expression as follows

```python
shopping_list = ["Apple", "Apple", "Apple", "Milk", "Pear"]
for index, item in enumerate(shopping_list):
    print("Item:", item)
    print("Index:", index)
```

#### While loops

A `while` loop is similar to a `for` loop in that we can loop over a block of code. However, normally we use `while` for times when we dont have a fixed number of actions to take.

In this example we do not know how many loops we will need to take in our program since it is controlled by the users `input`, so a `while` loop would be better than a `for` loop

```python
apple_stock = 10
while apple_stock > 0:
    bought = input(f"How many apples would you like to buy? We have {apple_stock} left in stock")
    bought = int(bought)
    if bought > apple_stock:
        print(f"I know you  asked for {bought} apples, but we only have {apple_stock} apples left. Have a nice day")
        apple_stock = apple_stock - bought
    else:
        print(f"Thanks for buying {bought} apples!")
        apple_stock = apple_stock - bought

print("We are out of apple stock")
```

#### Controlling the loop

There are a few ways to control a loop; we can exit through exhaustion or by `break`ing out of it. We can also skip over some of the cycles, `continue` with our loops but not run the rest of the code block.

```python
shopping_list = ["Apple", "Apple", "Lollies", "Apple", "Milk", "Pear"]
for item in shopping_list:
    if item == "Lollies":
        print("You're not allowed to have lollies Jimmy!")
        continue
    print(item)
```

```python
shopping_list = ["Apple", "Apple", "Lollies", "Chocolate", "Apple", "Milk", "Pear"]
for item in shopping_list:
    if item == "Lollies":
        print("You're not allowed to have lollies Jimmy!")
        continue
    if item == "Chocolate":
        print("Jimmy! I said, NO chocolate")
        break
    print(item)
```

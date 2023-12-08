<!--

author:   Meredith Lee
email:    leemc@chop.edu
version: 1.2.0
current_version_description: Replaced SageMathCells with Pyodide cells for better usability
module_type: standard
docs_version: 1.2.0
language: en
narrator: UK English Female
mode: Textbook

title: Python Basics: Loops and Conditionals

comment: Learn how to use loops and conditional statements in Python. 

long_description: Before using Python for data analysis, there are some basics to learn that will set the foundation for more advanced Python coding. This module will teach you about how to loop through sequences and use conditional statements. 

estimated_time_in_minutes: 20

@pre_reqs
Learners should be familiar with using [functions and methods](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#1) and [collections](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_lists_dictionaries/python_basics_lists_dictionaries.md#1) at a beginner level. 
@end

@learning_objectives

After completion of this module, learners will be able to:

- Iterate through lists using loops
- Utilize conditional statements

@end

good_first_module: false
collection: learn_to_code
sequence_name: python_basics
previous_sequential_module: python_basics_lists_dictionaries
coding_required: true
coding_level: basic
coding_language: python

@sets_you_up_for

- python_basics_exercise
- pandas_transform

@end

@depends_on_knowledge_available_in

- demystifying_python
- python_basics_variables_functions_methods
- python_basics_lists_dictionaries

@end


@version_history

Previous versions: 

- [1.0.1](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/5e1bbae6792dc5adc7cfcc99860b0f9e1447daa6/python_basics_loops_conditionals/python_basics_loops_conditionals.md#) Initial version
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_python.md
import: https://raw.githubusercontent.com/arcus/education_modules/pyodide_testing/_module_templates/macros_python.md
import: https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md
-->

# Python Basics: Loops and Conditional Statements

@overview

## Lesson Preparation

@sage

@lesson_prep_python_pyodide

## Introduction

In programming, we often need to perform a task repeatedly (or **iteratively**), or only if certain conditions are met. Iterating over an series of inputs and performing a specified task on each input is accomplished using **loops**. In some cases though, we only want to perform a task sometimes (either within a loop or not); for this, we use **conditional statements**. Loops and conditional statements are not unique to Python-- they appear in almost every language! This module will discuss how these concepts work in Python. 

## Loops

In Python, [lists and dictionaries](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_lists_dictionaries/python_basics_lists_dictionaries.md#1) are examples of **iterable** objects, or objects whose members can be returned one at a time. This is important in **loops**, which repeat (or iterate) the same operation for each element in an iterable object like a list.

For a sense of how loops work in Python, here is a simple example. Let's say there are five children at a party, and they each start with a certain number of pieces of candy. Next, let's say that we give each child 5 more pieces of candy. Using a simple loop, we can get a list of how many total pieces of candy each child has now using the `for` and `in` keywords.

```python
starting_candy = [3, 10, 11, 6, 7]
candy_day1 = [] #Here we are initiating an empty list, so that we can add elements to it later
for i in starting_candy: #In the loop, i will take on the value of each list element in turn
  j = i + 5
  candy_day1.append(j)
print(candy_day1)
```
@Pyodide.eval

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Did you notice the explanatory text in the above code cell that started with a pound sign (or hash mark)? The pound sign / hash mark ( # ) in a code cell indicates the start of a **comment**. Comments aren't recognized as code and won't be run. Each line of a comment must be marked with a new pound sign. Comments are an excellent way to add brief explanations and clarifications about your code.

</div>

This example loops through the list of numbers, adds 5 to each number one at a time, and adds the sum to a new list using the `.append()` method for lists. Finally, we printed the new list to our screen. This kind of loop is sometimes called a **for loop**; there is another kind of loop called a **while loop**, which is often used when we don't know the number of times we'll have to iterate through a block of code before we start ([check out this page for more information about while loops](https://www.geeksforgeeks.org/python-while-loop/)).


### Indentation

```python
starting_candy = [3, 10, 11, 6, 7]
candy_day1 = [] #Here we are initiating an empty list, so that we can add elements to it later
for i in starting_candy: #In the loop, i will take on the value of each list element in turn
  j = i + 5
  candy_day1.append(j)
print(candy_day1)
```
@Pyodide.eval

The code cell above is exactly the same as the one on the previous page. Notice that the two lines of code after the `for` statement are **indented**. This indentation is important in Python, and not just for readability! Indents indicate blocks of code, or lines of code that do a specific thing. In this case, the two lines after the `for` statement are in a different code block than the rest; they comprise the body of the loop. Indentation tells Python what statements to evaluate in what order. You also may have noticed a colon (:) at the end of the `for` statement. This tells Python that the following lines are a new code block and should be indented. All of the lines of a code block need to be indented the same number of spaces.

Try changing the code cell above by removing the indentation before `candy_day1.append(j)` in line 5. How does the output change? Why do you think it changes the way that it does?

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Indentation is tricky, especially for complex nested loops; experienced Python programmers sometimes struggle with this, so don't worry if it takes some trial and error to figure out! If you end up struggling with a tricky loop, try isolating the individual pieces, get those working, and then build outward. [Drawing a flowchart of the problem](https://problemsolvingwithpython.com/09-Loops/09.04-Flowcharts-Describing-Loops/) can also help!

</div>


### Range
The built-in function `range()` is frequently used in loops. The `range()` function returns a range object.

```python
print(range(1, 20))
```
@Pyodide.eval

This is not terribly interesting on its own, but is very useful if you want to loop through a sequence of numbers, such as 1 to 20, without having to manually build a list of all of those numbers. If you create a list from the range object and then print that list, you'll see what's going on behind the scenes. What do you think this code will do? Run the code cell below and find out.

```python
print(list(range(1, 20)))
```
@Pyodide.eval

Notice that the last number listed is 19, not 20. Just like in subsetting, the first number passed to `range()` is **inclusive**, and the second is **exclusive**. And don't forget that the first position is index 0!

**Your Turn**: Before running the code cell below, try to predict what number will be returned. Got a number in mind? Run the code and see if your hypothesis is correct! (**Hint**: the bracket notation below (`[ ]`) allows Python to access an element in a collection object, like a list; for a refresher take a look at this [introduction to lists in Python](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_lists_dictionaries/python_basics_lists_dictionaries.md#4).)

```python
print(list(range(1, 20))[7])
```
@Pyodide.eval


### Quiz: Loops


```python
for i in range(0, 6):
  j = i*i
```
@Pyodide.eval

The loop in the code cell above is missing a `print()` statement to show us the output. How would you include a `print()` statement such that all of the squares of `i` in `range(0,6)` are displayed? Feel free to edit the code cell above and experiment to find the answer.

[( )] `print(i)`, indented so that it **inside** the loop
[(X)] `print(j)`, indented so that it **inside** the loop
[( )] `print(i)` with no indentation, so that it is **outside** of the loop
[( )] `print(j)` with no indentation, so that it is **outside** of the loop
***
<div class = "answer">

According to our code, we know that `j` is the square of `i`, so that's the number we need to print. If we put the `print(j)` statement **outside** of the loop, we only see the last number, 25, because that is the value that `j` had once the loop was completed. If we place the `print(j)` statement **inside** the loop, each value of `j` is printed before the next iteration of the loop. Therefore, the second option is correct.

</div>
***

## Conditional statements: If-else

Sometimes when you're working with Python, you might want your code to do different things in different circumstances. You handle this with an `if-else`, or **conditional**, statement.

Conditional statements often make use of **comparison operators**. Comparison operators compare values and return a `True` or `False` (also known as a [**boolean value**](https://www.geeksforgeeks.org/boolean-data-type-in-python/)), depending on the outcome of the comparison. Some important comparison operators include:

* `==`: In Python, this is used to test **equality** (be sure not to use  the single equals sign `=`, which is used for assigning values to variables). So `9 == 18` asks the questions "is 9 equal to 18?", which would evaluate to `False`.

* `!=`: not equal to.

* `<`: less than.

* `>`: greater than.

* `<=`: less than or equal to.

* `>=`: greater than or equal to.

Let's look at a simple example of some code that utilizes conditionals.

```python
name = "Pythonista"
if type(name) == str: # We're testing here to see if the value of name is a string.
                                    # This will either evaluate to True or False.
    print("Welcome, "+ name+"!")
else:
    print("Please enter a name.")
```
@Pyodide.eval

**Your Turn**: Try changing the value assigned to `name` from "Pythonista" to a number, and see what happens! What happens if you remove the quotation marks?

### Multiple conditions


You also aren't confined to a single "if-else" statement! You can have multiple conditions and define multiple results. The simplest way to do this is with the keyword `elif`. Run the following code cell, and then change the number assigned to `num` and see how the output changes.

```python
num = 1
if num < 10:
    print("This number is less than 10")
elif 10 < num < 100:
    print("This number is more than 10 but less than 100")
elif num >= 100:
    print("This number is greater than or equal to 100")
else:
    print("This number equals 10")
```
@Pyodide.eval

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

When coding in Python, it is important to remember that lines and blocks of code are run **in order**. This means that if your instructions aren't in logical order, you can get outputs that are "wrong."

</div>

**Your Turn**: Before you run the following code cell, predict what the outcome will be.

```python
num = 1
if num < 100:
    print("This number is less than 100")
elif num < 10:
    print("This number is less than 10")
elif num >= 100:
    print("This number is greater than or equal to 100.")
else:
    print("This number equals 10")
```
@Pyodide.eval

Was your prediction correct?

Because the conditional statements are run in order, and in the code above the first statement returns `True`, Python never gets to the second statement, even though it is also `True`! This behavior is important to remember when you're creating multiple conditional statements.

### Conditionals in loops

Python becomes very powerful when you start combining conditionals and loops.

Remember when we looped through a list of pieces of candy that some children started with and calculated the number they would have if we gave each child 5 more pieces? Let's suppose that the next day instead of giving all of the children more candy, only the children who have fewer than 10 pieces of candy get another piece. We can still calculate how many pieces of candy each child has now (even though we're making the very unlikely assumption that none of the children have eaten any of their candy from before!).

```python
candy1 = [8, 15, 16, 11, 12]
candy2 = []
for i in candy1:
    if i < 10: #tests to see if each student has fewer than 10 pieces of candy
        j = i + 1
    else:
        j = i
    candy2.append(j)
print(candy2)
```
@Pyodide.eval

In the case above, we've used an if-else statement within our `for` loop! These loops can actually get quite complex for some tasks, but breaking down the loop and testing out the various pieces is often a good strategy.

### Quiz: Conditional statements

The following quiz questions are about the following code:

```python
candy1 = [8, 15, 16, 11, 12]
candy2 = []
for i in candy1:
    if i < 10: #tests to see if each student has fewer than 10 pieces of candy
        j = i + 2
    #Missing code here
    else:
        j = i
    candy2.append(j)
print(candy2)
```
@Pyodide.eval

1. If we wanted to add another conditional statement at line 6 of the code cell above that would give 1 piece of candy to children who start with between 10 to 15 pieces (inclusive), what keyword would we use to start that line?

    [( )] `for`
    [( )] `if`
    [(X)] `elif`
    [( )] `else`
    ***
    <div class = "answer">

    Because we're checking for multiple conditions, we use the `elif` keyword. We use `if` for the first condition that we are testing; `else` is used at the end to catch anything that hasn't been explicitly handled by our preceding conditions. And we know that `for` is the keyword to begin a loop!

    </div>
    ***


2. How could you write the comparison at line 6 so that each child gets the correct number of pieces of candy? Select all that apply.

    [[X]] `10 <= i <= 15`
    [[ ]] `10 < i < 15`
    [[ ]] `i >= 10`
    [[X]] `10 <= i < 16`
    ***
    <div class = "answer">

    Because we want to give an additional piece of candy to any student who started with between 10 and 15 pieces, we want to test if `i` is greater than or equal to 10, but less than or equal to 15 (which could also be expressed as less than 16, since we're working with integers). So the first and last choices are correct.

    </div>
    ***

## Additional Resources

* There are many helpful resources on [python.org](https://www.python.org/), including a [Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide) and [FAQs](https://docs.python.org/3/faq/).

* The Python documentation also has [more details and examples about loops and conditional statements](https://docs.python.org/3/tutorial/controlflow.html). 

## Feedback

@feedback
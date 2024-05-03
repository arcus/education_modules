<!--
module_id: python_basics_variables_functions_methods
author:   Meredith Lee
email:    leemc@chop.edu
version: 1.1.3
current_version_description: Implemented code blocks in pyodide; make liascript link(s) point to first page
module_type: standard
docs_version: 1.2.0
language: en
narrator: UK English Female
mode: Textbook

title: Python Basics: Functions, Methods, and Variables

comment: Learn the foundations of writing Python code, including the use of functions, methods, and variables.

long_description: Before using Python for data analysis, there are some basics to learn that will set the foundation for more advanced Python coding. This module will teach you about how to define variables and how to use functions and methods. 

estimated_time_in_minutes: 20

@pre_reqs
Learners should be familiar with [Python as a programming language](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_python/demystifying_python.md#1), but experience with writing Python code is not required.
@end

@learning_objectives

- Assign values to variables
- Identify and use functions 
- Identify and use methods

@end

good_first_module: false
collection: learn_to_code
sequence_name: python_basics
coding_required: true
coding_level: basic
coding_language: python

@sets_you_up_for
- python_basics_dictionaries
- python_basics_loops_conditionals
- python_basics_exercise
@end

@depends_on_knowledge_available_in
- demystifying_python
@end


@version_history
Previous versions: 

- [1.0.1](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/5e1bbae6792dc5adc7cfcc99860b0f9e1447daa6/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#1): Initial version
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_python.md
import: https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md
-->

# Python Basics: Functions, Methods, and Variables

@overview

## Lesson Preparation

@lesson_prep_python_pyodide

## Introduction to Python code

Python is a flexible, multi-purpose programming language that has applications in web development, software engineering, and data analysis. Part of its power and much of its popularity comes from the fact that it is **human-readable**, with a relatively simple syntax compared to many other programming languages. 

However, just like any language, there are some grammar rules (**syntax**) to learn in order to use Python. In this module, we'll go through a few of the basics of Python that will build a foundation for your learning and practice. 

We'll introduce **functions** and **methods**, the way that things happen in python, about **variables**, ways of storing information for later use. 

## Functions and methods: Getting stuff done

In Python, there are two basic ways of taking something (such as text, a number, or a sequence) and performing some action on it: functions and methods. Functions and methods are similar in many ways, but are not exactly the same. In this module we'll discuss the syntax of each and go through some examples. 

### Functions

**Functions** in Python take the syntax `function(arguments)`: the name of the function, and then information we want to give the function (called **arguments**) in parentheses; arguments can include the thing that we want to perform the action of the function on, as well as other information that specifies exactly how a function does what it does. 

A simple (but very useful) example of this is the `print()` function:

```python
print("Hello World!")
```
@Pyodide.eval

The `print()` function takes an object (in this case the phrase "Hello World!") and displays it as output. The object that you want to display is the "required" argument, meaning that you must provide this value in the parentheses for the function to work; however, the `print()` function has several other "optional" arguments that can modify how the function behaves. If you're curious about what these other arguments are, [take a look at this very brief tutorial about the `print() function`](https://www.w3schools.com/python/ref_func_print.asp). 

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

Some functions can even be called on their own without any arguments, though this isn't common. The documentation for the function will tell you which, if any, arguments are required for that function. To call a function without any arguments, just leave the parentheses empty.

</div>

There are many [built-in functions in Python](https://docs.python.org/3/library/functions.html), which means that you can perform many tasks by calling the relevant function without downloading anything other than Python itself. A couple of examples are `abs()`, which takes a number as its required argument and returns the absolute value of that number, and `len()`, which returns the length of its argument (which can be a word, a phrase, a sequence, or a collection of items).

### Methods

**Methods** in Python are very similar to functions, but are not precisely the same. The precise technical differences are not important to us right now; however, it is important to note that the syntax is a little different. Methods cannot be called by themselves; they are always associated with an object, with the syntax `object.method()`.

Let's look at an example and try applying the `.lower()` method:

```python
print("Hello World!".lower())
```
@Pyodide.eval

As you might have suspected, the `.lower()` method made all of the letters of the phrase "Hello World!" lowercase. The `.lower()` method is a **string method**, or a method that *must* be called on a string object, of which "Hello World!" is an example. (There is also a string method called `.upper()`, can you guess what it does?) The Python documentation has [more information about string methods](https://docs.python.org/2.5/lib/string-methods.html). Other kinds of objects in Python (like lists and dictionaries, for example, which we'll discuss later in this module) have their own associated methods. 

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Notice that we nested the code `"Hello World!".lower()` within the function `print()`, meaning that the output of `"Hello World!".lower()`, which is `hello world!`, is passed as an argument to the `print()` function, so that when you run the code cell above, you can see the output. This kind of nesting is common in Python, but isn't always required. 

</div>

Additionally, similar to function arguments, some methods can have **parameters**, or additional input that gives Python more information about what you want to do. Not all methods have parameters (`.lower()` and `.upper()` are examples of methods that have no parameters), but some do. These parameters may be required or optional, and they go in the parentheses following the method name. 

An example of a string method with both required and optional parameters is `.count()`, which counts the number of times a specified substring occurs within the string object it is used on. The `.count()` method requires that you include a *value* parameter, which is the substring you're searching for, but you can optionally add *start* and *end* parameters, which specify where in the string you want to start and stop looking. In this case, the syntax would look like this: `"string".count("value", start, end)`. You'll always need to add the *value* parameter, but you can leave out the *start* and *end* parameters if you want to search the whole string.

Let's look at an example of the `.count()` method in action:

```python
print("Mississippi".count("is"))
```
@Pyodide.eval

In the code cell above, we are searching the whole string "Mississippi" for number of times the substring "is" occurs (the answer is 2).


<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

It can be hard to remember what parameters are required or optional for a particular method. If you don't remember, looking up the documentation for that method is a great place to start! Finding that documentation is often as simple as searching "Python" and the method you're looking for. 

</div>

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

At this point, you may be wondering exactly when you should use functions vs. methods, and that can be a tricky question to answer! It depends on whether the thing you want to do was written as a function or a method, and even folks with a lot of Python experience can forget and need to look things up! A good approach is to use your favorite search engine to search for the task you want to do combined with "Python." For example, if you want to figure out how to make a string completely lower case, you might search "make string lower case in Python." That will lead you to the string method `.lower()`. 

</div>

### Data Types

So we've talked quite a bit about strings, but what are they? A **string** is an example of a **data type** in Python. Knowing what data type you're working with is very important, because certain functions and methods will only work on certain data types, or will behave differently depending on the data type. The built-in function `type()` will return as output the data type of its argument.

```python
print(type("Hello World!"))
```
@Pyodide.eval

When we pass the phrase "Hello World!" to the `type()` function, we get the output `<class 'str'>`, "str" being short for "string". A **string** is a sequence of characters; you tell Python that a sequence is a string by surrounding it in quotation marks. You can use either single or double quotes, but it's a good idea to be consistent. 

Strings are not the only data type in Python! Other data types include integers, floats (or decimal numbers), lists, and boolean (like True or False, which may look like strings but are a special data type and don't require quotation marks), but there are many more. Try editing the code cell above, replacing "Hello World" with different inputs (for example "Hi", 9.8, 10, or False) and run the cell again to see how the output changes.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Notice that in the above example, we have passed the `type("Hello World!")` function call as an argument to `print()`, just like we did with the output of our methods previously. Again, this is fairly common, but there is another option that we'll discuss in the next section-- using variables!

</div>

### Quiz: Functions and methods

1. Which of the following are valid examples of Python code? Select all that apply.

    [[X]] `len("Python is awesome!")`
    [[X]] `"python".upper()`
    [[X]] `type("4.3")`
    [[X]] `type(True)`
***
<div class = "answer">

These are all examples of valid Python code! 

- `len("Python is awesome!")` uses the `len()` function to return the length of the argument `"Python is awesome!"` (which is 18-- spaces and punctuation count!) and print that output to the screen. 
- `"python".upper()` uses the string method `.upper()` to make the string "python" all uppercase. 
- `type("4.3")` might be a little tricky, since 4.3 is a decimal number (or **float**), but it's also in quotation marks, which means that "4.3" is a string in this case! 
- `type(True)` might also be tricky, since at first it looks like a string that doesn't have the required quotation marks. However, `True` and `False` are special in Python, and have the type `boolean`.  

</div>
***

**Hint:** If you get stuck, try replacing the `x` argument in the `print()` function below with the code examples above. Running code you're unsure about and seeing what output you get can be a useful troubleshooting tool!

```python
print(x)
```
@Pyodide.eval

2. To check that the string "Python is awesome!" ends in an exclamation point, we can use the code ` "Python is awesome!".endswith("!")`. In this case, the boolean value `True` will be returned, since "Python is awesome!" does indeed end in an exclamation point. What is `.endswith()` an example of?

    [(X)] A method
    [( )] A function
    [( )] A string
    [( )] A float
***
<div class = "answer">

You can tell `.endswith()` is a method because it has the syntax `object.method()`, with `"Python is awesome!"` being the object (a string, in this case) the `.endswith()` method is called on. 

A function would have the syntax `function(argument)`. A float (short for "floating point number") is a numeric data type containing a decimal point. 

</div>
***

## Variables

Rather than using a method directly on a value (like a string or a number) or passing that value directly to a function, we can also **assign** values to variables and use *those* with our functions and methods. **Variables** are ways to store values and objects for use later.

```python
my_num = 17
print(my_num)
```
@Pyodide.eval

While the above example may seem trivial, variables are extremely useful for re-using values and objects. They make your code easier to edit (if you store a value in a variable and then need to change it later, you only need to change the value in the variable definition, rather than every time in your code you've used that value). Variables also make your code more **readable**, or easier for humans to understand.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

It's a good idea to use descriptive names for your variables! Python won't care if you decide to assign a value to the variable `x`, but it's helpful to anyone reading your code (including yourself in 6 months!) to have your variable names describe the values that they hold.

</div>

```python
dogs = 3
cats = 5
all_pets = dogs + cats
print(all_pets)
```
@Pyodide.eval

In the above example, we have defined variables to contain the number of dogs and the number of cats, and then used these variables in a calculation to get the total number of pets, which is itself assigned to a variable. The `all_pets` variable can then be used repeatedly later (maybe we want to calculate costs associated with feeding and housing all of these pets, for example, or how many collars we'll need). Now, if the number of dogs or cats changes, we can just change the value in the variable statement and re-run our code!

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

While strings in Python need to be in quotation marks, variable names do not. The reason that strings require quotation marks is so that Python knows that when you type "abc", you mean the **literal characters** "abc", and not some variable with the **name** `abc`.  

Numbers and boolean values like `True` and `False` do not need quotation marks either, but you also cannot use numbers or boolean values by themselves as variable names (but naming a variable using a mix of letters and number is okay).

If, for example, you typed `dogs` without first defining it as a variable, you would get an error message that looks like this: `NameError: name 'dogs' is not defined`. Variables are defined (or declared) when you assign a value to them.  

</div>


### Quiz: Variables

True or False: Once you assign a value to a variable, you can never change the value of that variable.

[( )] True
[(X)] False
***
<div class = "answer">

Changing the value of a variable is as simple as editing the value in the assignment statement and re-running the code; alternatively, you can write a new assignment statement assigning the updated value to the variable.

</div>
***


## Additional Resources

* There are many helpful resources on [python.org](https://www.python.org/), including a [Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide) and [FAQs](https://docs.python.org/3/faq/).

* [W3 Schools has bite-sized explanations and examples of writing code in Python](https://www.w3schools.com/python/) if you want more clarity on how anything works.

* Jupyter notebooks are a great option for doing data analysis with Python-- [check out this Jupyter notebook demo](https://jupyter.org/try-jupyter/lab/), then open "notebooks" and look at "Intro.ipynb" to see how they work.

## Feedback

@feedback
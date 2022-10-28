<!--

author:   Meredith Lee
email:    leemc@chop.edu
version:  1.0.1
module_template_version: 2.0.0
language: en
narrator: UK English Female
code_language: Python
topic: Learn to Code
title: Python Basics: Writing Python Code
comment: Learn the foundations of writing Python code.
long_description: Before using Python for data analysis, there are some basics to learn that will set the foundation for more advanced Python coding. This module will teach you about functions and methods, how to define and use variables, how to create and edit lists and dictionaries, and how use loops and conditional statements to perform tasks with these basic data structures.
estimated_time: 1 hour

@learning_objectives

After completion of this module, learners will be able to:

- Identify and use functions and methods
- Assign values to variables
- Create and edit lists
- Iterate through lists using loops
- Utilize conditional statements
- Create and edit dictionaries

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

script: https://sagecell.sagemath.org/static/embedded_sagecell.js

@sage
<script input="hidden">
// Make *any* div with class 'python' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python',
                       evalButtonText: 'Run python',
                       languages: ["python"],
                       hide: ['fullScreen', 'permalink'],
                       });
// Make *any* div with class 'python_run' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python_run',
                      evalButtonText: 'Run python',
                      languages: ["python"],
                      hide: ['fullScreen', 'permalink'],
                      autoeval: 'true'
                      });
// Make *any* div with class 'python_link' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python_link',
                      evalButtonText: 'Run python',
                      languages: ["python"],
                      hide: ['fullScreen', 'permalink'],
                      autoeval: 'false',
                      linked: 'true'
                      });
// Make *any* div with class 'python_data_init' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python_data_init',
                      evalButtonText: 'Run python',
                      languages: ["python"],
                      editor: 'codemirror-readonly',
                      hide: ['fullScreen', 'permalink','output','evalButton'],
                      autoeval: 'true',
                      linked: 'true',
                      linkKey: "data"
                      });       
// Make *any* div with class 'python_data' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python_data',
                      evalButtonText: 'Run python',
                      languages: ["python"],
                      hide: ['fullScreen', 'permalink'],
                      autoeval: 'false',
                      linked: 'true',
                      linkKey: "data"
                      });                

// Make *any* div with class 'r' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.r',
                      evalButtonText: 'Run R',
                      languages: ["r"],
                      hide: ['fullScreen', 'permalink'],
                      });
// Make *any* div with class 'r_run' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.r_run',
                      evalButtonText: 'Run R',
                      languages: ["r"],
                      hide: ['fullScreen', 'permalink'],
                      autoeval: 'true'
                      });
</script>
@end

-->

# Python Basics: Writing Python Code

<div class = "overview">

## Overview
@comment

**Is this module right for me?:** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites:** Learners should be familiar with [Python as a programming language](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_python/demystifying_python.md), but need not have any experience with actually writing Python code.

**Learning Objectives**:

@learning_objectives

</div>

## Lesson Preparation
@sage

You will have opportunities for hands-on coding as you work your way through this module using interactive python cells.
The interactive python cells are powered by [SageMathCell](https://sagecell.sagemath.org/). For the most part, these will appear with some code already in them, and you can run that code by clicking the **Run python** button. You can also edit the code in these cells and run your own code.


**Give it a try:**
<div class="python">
<lia-keep>
<script type="text/x-sage">
print(7+2)
</script>
</lia-keep>
</div>

Code will not persist from one page to the next, and you can always refresh the page to return the code (and the stored memory of the cell) to its initial state.

<div class = "important">
These cells will compute everything you ask them to, but will only display what you explicitly request using the `print()` command.

</div>

<div class = "warning">
**Navigating with arrow keys**

You can navigate the pages of this course using left and right arrow keys. This means that you **cannot** use left and right arrow keys to navigate **within** a code cell.
</div>

## Introduction to Python code

Python is a flexible, multi-purpose programming language that has applications in web development, software engineering, and data analysis. Part of its power and much of its popularity comes from the fact that it is **human-readable**, with a relatively simple syntax compared to many other programming languages. However, just like any language, there are some grammar rules (**syntax**) to learn in order to use Python. In this module, we'll go through a few of the basics of Python that will build a foundation for your learning and practice.

### Functions and methods: Getting stuff done

In Python, there are two basic ways of taking something (such as text, a number, or a sequence) and performing some action on it: functions and methods.

Functions
======

**Functions** take the syntax `function(arguments)`: the name of the function, and then whatever you want to perform that function on (called **arguments**) in parentheses. A simple (but very useful) example of this is the `print()` function.

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

print("Hello World!")
</script>
</lia-keep>
</div>

The `print()` function takes an argument (in this case the phrase "Hello World!") and displays it as output.

<div class = "important">
Tip: Some functions can be called on their own without any arguments, though this isn't common. The documentation for the function will tell you which, if any, arguments are required for that function. To call a function without any arguments, just leave the parentheses empty.
</div>

There are many [built-in functions in Python](https://docs.python.org/3/library/functions.html), which means to perform many tasks, you only need to call the function without downloading anything other than Python itself. A couple of examples are `abs()`, which takes a number as its argument and returns the absolute value of that number and `len()`, which returns the length of its argument (which can be a word, a phrase, a sequence, or a collection of items)

Methods
======

**Methods** in Python are very similar to functions, but are not precisely the same. The exact differences are not important to us right now, except that the syntax is a little different. Methods cannot be called by themselves; they are always called on an object, with the syntax `object.method()`.

Let's look at an example and try applying the `lower()` method:

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

print("Hello World!".lower())

</script>
</lia-keep>
</div>

As you might have suspected, the `.lower()` method made all of the letters of the phrase "Hello World!" lowercase. The `.lower()` method is a **string method**, or a method that must be called on a string, of which "Hello World!" is an example. (There is also a string method called `.upper()`, can you guess what it does?) The Python documentation has [more information about string methods](https://docs.python.org/2.5/lib/string-methods.html).

Let's talk more about strings and other data types next.

### Data Types

Strings are an example of a **data type** in Python. Knowing what data type you're working with is important, because certain functions and methods will only work on certain data types, or will behave differently depending on the data type. The built-in function `type()` will return as output the data type of its argument.

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

print(type("Hello World!"))

</script>
</lia-keep>
</div>

When we pass the phrase "Hello World!" to the `type()` function, we get the output `<class 'str'>`, "str" being short for "string". A **string** is a sequence of characters; you tell Python that a sequence is a string by surrounding it in quotation marks. You can use either single or double quotes, but it's a good idea to be consistent. Strings are a specific data type in Python; other data types include integers, floats (or decimal numbers), lists, and boolean (like True or False, which may look like strings but are a special data type and don't require quotation marks), but there are many more. Try editing the code cell above, replacing "Hello World" with different inputs (for example "Hi", 9.8, 10, or False) and run the cell again to see how the output changes.

<div class = "important">
Notice that in the above example, we have passed the `type("Hello World!")` function call as an argument to `print()`. Nesting functions like this is common (you can do the same with methods), but there is another option we'll discuss in the next section-- using variables!
</div>

### Quiz: Functions and methods

Which of the following are valid examples of Python code? Select all that apply.

[[X]] `len("Python is awesome!")`
[[X]] `"python".upper()`
[[X]] `type("4.3")`
[[X]] `type(True)`
***
<div class = "answer">

These are all examples of valid Python code! `print(type(4))` returns the type of the argument `4` (which is `int`, short for integer) and prints that output to the screen. `"python.upper()"` makes the string "python" all uppercase. `type("4.3")` might be a little tricky, since 4.3 is a decimal number (or **float**) but it's in quotation marks-- but those quotation marks just mean that, in this case, "4.3" is a string! `type(True)` might also be tricky, since at first it looks like a string that doesn't have the required quotation marks. However, `True` and `False` are special in Python, and have the type `boolean`.  

</div>
***

**Hint:** If you get stuck, try replacing the `x` argument in the `print()` function below with the code examples above. Running code you're unsure about and seeing what output you get can be a useful troubleshooting tool!

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

print(x)

</script>
</lia-keep>
</div>

## Variables

Rather than passing a value (like a string or a number) directly to a function, we can also **assign** values to variables and pass those to functions. **Variables** are ways to store values and objects for use later.

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

my_num = 17
print(my_num)

</script>
</lia-keep>
</div>

While the above example may seem trivial, variables are extremely useful for re-using values and objects, for making your code easier to edit (if you store a value in a variable and then need to change it later, you only need to change the value in the variable definition, rather than every time in your code you've used that value), and making your code more readable.

<div class = "important">
Tip: It's a good idea to use descriptive names for your variables! Python won't care if you decide to assign a value to the variable `x`, but it's helpful to anyone reading your code (including yourself in 6 months!) to have your variable names describe the value that it holds.
</div>

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

dogs = 3
cats = 5
all_pets = dogs + cats
print(all_pets)
</script>
</lia-keep>
</div>

In the above example, we have defined variables to contain the number of dogs and the number of cats, and then used these variables in a calculation to get the total number of pets, which is itself assigned to a variable. The `all_pets` variable can then be used repeatedly later (maybe we want to calculate costs associated with feeding and housing all of these pets, for example, or how many collars we'll need). Now, if the number of dogs or cats changes, we can just change the value in the variable statement and re-run our code!

<div class = "important">
While strings in Python need to be in quotation marks, variable names do not. The reason that strings require quotation marks is so that Python knows that when you type "abc", you mean the **literal characters** "abc", and not some variable with the **name** `abc`.  

Numbers and boolean values like `True` and `False` do not need quotation marks either, but you also cannot use numbers or boolean values by themselves as variable names (but naming a variable using a mix of letters and number is okay).

If, for example, you typed `dogs` without defining it as a variable, you would get an error message that looks like this: `NameError: name 'dogs' is not defined`. Variables are defined (or declared) when you assign a value to them.  

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

## Lists

**Lists** in Python are objects that contain a collection of multiple items. They are surrounded by square brackets [ ] and the items in the list are separated by commas:

@sage
<div class="python_link">
<lia-keep>
<script type="text/x-sage">

produce = ["tomato", "squash", "apple", "cucumber", "peach", "spinach"]
print(produce)

</script>
</lia-keep>
</div>

There are a few important characteristics of lists:

* Lists can have duplicate values. An example might be the list `[3, 1, 4, 1, 5, 9]`, where the number 1 appears twice.

* List items don't all have to be of the same type (you can have a mix of strings and numbers, for example, or even a list of lists). `[3.14, "pi", False, ["number", "string", "boolean"]]` is an example of a list that contains a float, a string, a boolean value, and a list as its elements.

* Lists are **ordered**: List items remain in the position that they are entered into the list, and you can access any item by its position, or **index**.

  <div class = "important">
  An **index** in Python refers to a value's position in a sequence. The sequence can be a collection object like a list or even a string (which you can think of as a sequence of characters). The important thing to remember is that in Python, **indices start at 0**. This means that the index of the first item in a sequence is `0`! This is not always the case in other programming languages.

  To access an item by its index, you use **subsetting notation**, `sequence[index]`. To get the first letter of the string "Hello", for example, you would use the code `"Hello"[0]`.
  </div>

* Lists are **changeable**; you can add, remove, and edit items in a list. There are a few ways to do this:

    * `.pop()` removes a specific element by **index**).

     @sage
     <div class="python_link">
     <lia-keep>
     <script type="text/x-sage">

     print(produce.pop(0))

     </script>
     </lia-keep>
     </div>

   * `.remove()` removes a specific element by **value**.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    produce.remove("apple")
print(produce)

    </script>
    </lia-keep>
    </div>

  * `del` deletes objects, and can be used as another way to remove elements of a list by index. The syntax will be a little different, because it is a keyword, not a list method. It is useful because it allows you to delete list elements in a **slice**. Slicing uses subsetting notation to indicate where the slice begins and ends. The first index listed is **inclusive**, or included in the slice; this is followed by a colon; the second index listed is **exclusive**, or excluded from the slice; finally, these numbers are surrounded by square brackets.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    del produce[1:3]
print(produce)

    </script>
    </lia-keep>
    </div>

  * `.clear()` removes everything from the list.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    produce.clear()
print(produce)

    </script>
    </lia-keep>
    </div>

  * `.append()` adds an element to the end of a list.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    produce.append("pear")
print(produce)

    </script>
    </lia-keep>
    </div>

  * `.insert()` adds an element to a specific position.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    produce.insert(0, "kale")
print(produce)

    </script>
    </lia-keep>
    </div>

  * `.extend()` adds another list to your list (or another iterable object, but don't worry about that for now).

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">
    berries= ["strawberry", "blueberry", "raspberries"]
produce.extend(berries)
print(produce)

    </script>
    </lia-keep>
    </div>


You'll notice that with each step, our list `produce` has been permanently changed-- in order to "start over" with the original list, we simply need to re-run the first code chunk.

<div class = "warning">
The code cells above are linked, meaning that all of the cells "remember" the code that has been run previously (as they would be in a [notebook](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_python/demystifying_python.md#jupyter-notebooks)). Because of this, if you run them out of order, you can get unexpected results or even errors! If things aren't working like they should, re-run the first code cell on the page or hit your refresh button.
</div>

### Quiz: Lists

1. While of the following is FALSE about lists? Select all that apply.

    [( )] Lists are changeable; items can be added, removed, or replaced after the list is created.
    [( )] Lists can be assigned to variables.
    [( )] Lists can contain a mix of data types.
    [(X)] Lists are unordered; you cannot access an item in the list by its position.
    ***
    <div class = "answer">

    Lists are chanageable, can be stored in varibles for later use, can contain a mix of data types, and they are **ordered**, meaning that items remain in the position that they were put into the list, and you can access or edit list items by value **or** position (also called the **index**).

    </div>
    ***

2. Given the following list of numbers, what is the **index** of the number **15**?

    `[2, 14, 9, 101, 15, 37]`

    [( )] 5
    [(X)] 4
    [( )] 15
    [( )] 6
    ***
    <div class = "answer">

    Indexing in Python begins with **0**, not 1, and so the index of 15, which is the fifth item in the list, is **4**.  

    </div>
    ***

## Loops

A Python list is an **iterable** object, or an object whose members can be returned one at a time. This is important in **loops**, which repeat (or iterate) the same operation for each element in an iterable object like a list.

For a sense of how loops work in Python, here is a simple example. Let's say there are five children at a party, and they each start with a certain number of pieces of candy. Next, let's say that we give each child 5 more pieces of candy. Using a simple loop, we can get a list of how many total pieces of candy each child has now using the `for` and `in` keywords.

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

starting_candy = [3, 10, 11, 6, 7]
candy_day1 = [] #Here we are initiating an empty list, so that we can add elements to it later
for i in starting_candy: #In the loop, i will take on the value of each list element in turn
  j = i + 5
  candy_day1.append(j)
print(candy_day1)

</script>
</lia-keep>
</div>

<div class = "important">
Did you notice the explanatory text in the above code cell that started with a pound sign (or hash mark)? The pound sign / hash mark ( # ) in a code cell indicates the start of a **comment**. Comments aren't recognized as code and won't be run. Each line of a comment must be marked with a new pound sign. Comments are an excellent way to add brief explanations and clarifications about your code.
</div>

This example loops through the list of numbers, adds 5 to each number one at a time, and adds the sum to a new list using the `append()` method for lists. Finally, we printed the new list to our screen. This kind of loop is sometimes called a **for loop**; there is another kind of loop called a **while loop**, which is often used when we don't know the number of times we'll have to iterate through a block of code before we start (check out this page for more information about while loops).


### Indentation

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

starting_candy = [3, 10, 11, 6, 7]
candy_day1 = [] #Here we are initiating an empty list, so that we can add elements to it later
for i in starting_candy: #In the loop, i will take on the value of each list element in turn
  j = i + 5
  candy_day1.append(j)
print(candy_day1)

</script>
</lia-keep>
</div>

The code cell above is exactly the same as the one on the previous page. Notice that the two lines of code after the `for` statement are **indented**. This indentation is important in Python, and not just for readability! Indents indicate blocks of code, or lines of code that do a specific thing. In this case, the two lines after the `for` statement are in a different code block than the rest; they comprise the body of the loop. Indentation tells Python what statements to evaluate in what order. You also may have noticed a colon (:) at the end of the `for` statement. This tells Python that the following lines are a new code block and should be indented. All of the lines of a code block need to be indented the same number of spaces.

Try changing the code cell above by removing the indentation in the line `candy_day1.append(j)`. How does the output change? Why do you think it changes the way that it does?

<div class = "help">
Indentation is tricky, especially for complex nested loops; experienced Python programmers sometimes struggle with this, so don't worry if it takes some trial and error to figure out! If you end up struggling with a tricky loop, try isolating the individual pieces, get those working, and then build outward. [Drawing a flowchart of the problem](https://problemsolvingwithpython.com/09-Loops/09.04-Flowcharts-Describing-Loops/) can also help!
</div>


### Range
The built-in function `range()` is frequently used in loops. The `range()` function returns a range object.

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

print(range(1, 20))

</script>
</lia-keep>
</div>

This is not terribly interesting on its own, but is very useful if you want to loop through a sequence of numbers, such as 1 to 20, without having to manually build a list of all of those numbers. If you create a list from the range object and then print that list, you'll see what's going on behind the scenes. What do you think this code will do? Run the code cell below and find out.

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

print(list(range(1, 20)))

</script>
</lia-keep>
</div>

Notice that the last number listed is 19, not 20. Just like in subsetting, the first number passed to `range()` is **inclusive**, and the second is **exclusive**. And don't forget that the first position is index 0!

**Your Turn**: Before running the code cell below, try to predict what number will be returned. Got a number in mind? Run the code and see if your hypothesis is correct! (**Hint**: the bracket notation below (`[ ]`) allows Python to access an element in a collection object, like a list; you saw it before when indexing and subsetting).

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

print(list(range(1, 20))[7])

</script>
</lia-keep>
</div>


### Quiz: Loops


@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

for i in range(0, 6):
  j = i*i
</script>
</lia-keep>
</div>

The loop in the code cell above is missing a `print()` statement to show us the output. How would you include a `print()` statement such that all of the squares of `i` in `range(0,6)` are displayed? Feel free to edit the code cell above and experiment to find the answer.

[( )] `print(i)`, indented so that it **inside** the loop
[(X)] `print(j)`, indented so that it **inside** the loop
[( )] `print(i)` with no indentation, so that it is **outside** of the loop
[( )] `print(j)` with no indentation, so that it is **outside** of the loop
***
<div class = "answer">

According to our code, we know that `j` is the square of `i`, so that's the number we need to print. If we put the `print()` statment **outside** of the loop, we only see the last number, 25, because that is the value that `j` had once the loop was completed. If we place the `print()` statement **inside** the loop, each value of `j` is printed before the next interation of the loop. Therefore, the second option is correct.

</div>
***

## Conditional statements: If-else

Sometimes when you're working with Python, you might want your code to do different things in different circumstances. You handle this with an `if else`, or **conditional**, statement.

Conditional statements often make use of **comparison operators**. Comparison operators compare values and return a `True` or `False`, depending on the outcome of the comparison. Some important comparison operators include:

* `==`: In Python, this is used to test **equality** (be sure not to use  the single equals sign `=`, which is used for assigning values to variables). So `9 == 18` asks the questions "is 9 equal to 18?", which would evalulate to `False`.

* `!=`: not equal to.

* `<`: less than.

* `>`: greater than.

* `<=`: less than or equal to.

* `>=`: greater than or equal to.

Let's look at a simple example of some code that ultilizes conditionals.

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

name = "Pythonista"
if type(name) == str: # We're testing here to see if the value of name is a string.
                                    # This will either evaluate to True or False.
    print("Welcome, "+ name+"!")
else:
    print("Please enter a name.")

</script>
</lia-keep>
</div>

**Your Turn**: Try changing the value assigned to `name` from "Pythonista" to a number, and see what happens! What happens if you remove the quotation marks?

Multiple conditions
======

You also aren't confined to a single "if-else" statement! You can have multiple conditions and define multiple results. The simplest way to do this is with the keyword `elif`. Run the following code cell, and then change the number assigned to `num` and see how the output changes.

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

num = 1
if num < 10:
    print("This number is less than 10")
elif 10 < num < 100:
    print("This number is more than 10 but less than 100")
elif num >= 100:
    print("This number is more than 100")
else:
    print("This number equals 10")

</script>
</lia-keep>
</div>

<div class = "warning">
When coding in Python, it is important to remember that lines and blocks of code are run **in order**. This means that if your instructions aren't in logical order, you can get outputs that are "wrong."
</div>

**Your Turn**: Before you run the following code cell, predict what the outcome will be.

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

num = 1
if num < 100:
    print("This number is less than 100")
elif num < 10:
    print("This number is less than 10")
else:
    print("This number equals 10")

</script>
</lia-keep>
</div>

Was your prediction correct?

Because the conditional statements are run in order, and in the code above the first statement returns `True`, Python never gets to the second statement, even though it is also `True`! This behavior is important to remember when you're creating multiple conditional statements.

### Conditionals in loops

Python becomes very powerful when you start combining conditionals and loops.

Remember when we looped through a list of pieces of candy that some children started with and calculated the number they would have if we gave each child 5 more pieces? Let's suppose that the next day instead of giving all of the children more candy, only the children who have fewer than 10 pieces of candy get another piece. We can still calculate how many pieces of candy each child has now (even though we're making the very unlikely assumption that none of the children have eaten any of their candy from before!).

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

candy1 = [8, 15, 16, 11, 12]
candy2 = []
for i in candy1:
    if i < 10: #tests to see if each student has fewer than 10 pieces of candy
        j = i + 1
    else:
        j = i
    candy2.append(j)
print(candy2)

</script>
</lia-keep>
</div>

In the case above, we've used an if-else statement within our `for` loop! These loops can actually get quite complex for some tasks, but breaking down the loop and testing out the various pieces is often a good strategy.

### Quiz: Conditional statements

The following quiz questions are about the following code:

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

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

</script>
</lia-keep>
</div>

1. If we wanted to add another conditional statement at line 6 of the code cell above that would give 1 piece of candy to children who start with between 10 to 15 pieces (inclusive), what keyword would we use to start that line?

    [( )] `for`
    [( )] `if`
    [(X)] `elif`
    [( )] `else`
    ***
    <div class = "answer">

    Because we're checking for multiple conditions, we use the `elif` keyword. We use `if` for the first condition that we are testing; `else` is used at the end to catch anything that hasn't been explictly handled by our preceding conditions. And we know that `for` is the keyword to begin a loop!

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

## Dictionaries

Another kind of collection object in Python is a **dictionary**. Dictionaries are similar to lists in some ways, in that they are ordered (in recent versions of Python; in older versions, dictionaries are unordered) and changeable. However, there are some important distinctions:

* Dictionaries are collections of **key-value pairs**. For example if you had a dictionary of demographic information for an individual, the **keys** might be the type of information stored (address, telephone number, etc.) and the **values** would be the actual values of those data (123 Puppydog Lane, 987-654-3210).

* They do not allow duplicate key-value pairs.

* Dictionaries use curly brackets { }.

Let's build an example dictionary:

@sage
<div class="python_link">
<lia-keep>
<script type="text/x-sage">

contact_info = {"address" : "123 Puppydog Lane",
                "telephone" : "987-654-3210",
                "email" : "myname@email.com"}
print(contact_info)

</script>
</lia-keep>
</div>

Like lists, dictionaries have some useful methods you can use to access or alter their data:

* `.keys()` returns a list of the dictionary's keys.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    print(contact_info.keys())

    </script>
    </lia-keep>
    </div>

* `.values()` returns a list of the dictionary's values.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    print(contact_info.values())

    </script>
    </lia-keep>
    </div>

* `.items()` returns a list of the dictionary's key-value pairs as tuples (an object that holds multiple values, similar to a list, except that they are unchangeable). This may seem not very useful at first glance, but since different collection objects have different properties, there could be circumstances in which it is more useful to have the data in a different kind of object.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    print(contact_info.items())

    </script>
    </lia-keep>
    </div>

* `.pop()` works similarly for dictionaries as it does for lists, except that it removes an element by its key.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    print(contact_info.pop("email"))
print(contact_info)

    </script>
    </lia-keep>
    </div>

    <div class="warning">
    Note that this change is permanent! If you want to keep the original dictionary as-is, you should make a copy of the dictionary (using the `.copy()` method and assigning the copy to a new variable), and then using `.pop()` on the copy:

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    contact_info_copy = contact_info.copy()
contact_info_copy.pop("telephone")
print(contact_info)
print(contact_info_copy)

    </script>
    </lia-keep>
    </div>

    In this example though, all you need to do to restore the dictionary to its original form is re-run the first code cell or refresh the page.
    </div>

* There isn't a method to add items to a dictionary, but it can be done! You can give the dictionary a new key and assign a value to it (notice that we're using bracket notation again). This is another example of a permanent change to our dictionary.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    contact_info["work_email"] = "myname@company.com"
print(contact_info)

    </script>
    </lia-keep>
    </div>

  You can also use the same syntax with an existing key to assign a new value (note that the new value will **replace** the previous value).

### Quiz: Dictionaries

True or False: Duplicate key-value pairs are allowed in dictionaries.

[( )] True
[(X)] False
***
<div class = "answer">

While **values** can be repeated in a dictionary, each **key** must be unique. However, you can have multiple values for a key by putting those values in a list.

</div>
***

## Challenge Problem

<div class = "important">
Below is an example of a problem that can be solved using many of the concepts presented in this module. The next few pages will show you how to work through one possible solution, but feel free to give it a try on your own first!
</div>

A teacher friend of yours can never remember what the grade ranges are for letter grades. They have requested that you write some code that will take their students' final scores and return the letter grades corresponding to those scores. After doing some research, you know that:

90-100 = "A"

80-89 = "B"

70-79 = "C"

60-69 = "D"

< 60 = "F"

Your friend also sends you the class's final grades, along with the student identifiers:

st1: 88, st2: 78, st3: 34, st4: 97, st5: 64, st6: 89, st7: 56, st8: 83, st9: 92

Using a `for` loop and `if-else` statements, can you write some code that returns a dictionary with the student identifiers as the keys and the letter grades that the students should be awarded as the values?

**Hint:** To loop through the items (the keys and values) of a dictionary that we'll call `my_dict`, you can use the code `for k,v in my_dict.items()`.

If you do come up with a solution before looking at the answer, note that your code might look a little different; as long as you get the output you're looking for, that's okay!

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

#Hint: You'll need the identifiers and the scores in your loop.
#If you get stuck, try googling something like "Python looping through items in a dictionary".

</script>
</lia-keep>
</div>

### Possible solution: Part 1

Since we were given the student identifiers and each student's grades, the first thing we could do is build a dictionary, using the identifiers as the keys and the scores as the values.

We also know that we want our output to be a dictionary with the student identifiers as the keys and the **letter grades** as the values, so let's initialize an empty dictionary that we can add to later (the code below shouldn't have any output).

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

final_scores_dict = {"st1": 88, "st2": 78, "st3": 34, "st4": 97, "st5": 64,"st6": 89, "st7": 56, "st8": 83, "st9": 92}
letter_grades_dict = {}

</script>
</lia-keep>
</div>

### Possible solution: Part 2

Next, since we need to look at each student's final score and assign a letter grade based on it, we'll want to loop through the items in `final_scores_dict`. We can use a `for` loop for this. To make sure we are looping through the dictionary correctly, we can add a `print()` statement at the end that will display each item in turn (we can remove this line of code later, once we don't need it anymore).

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

final_scores_dict = {"st1": 88, "st2": 78, "st3": 34, "st4": 97, "st5": 64,"st6": 89, "st7": 56, "st8": 83, "st9": 92}
letter_grades_dict = {}
for k,v in final_scores_dict.items():
  print(k,v)

</script>
</lia-keep>
</div>

### Possible solution: Part 3

Now we need to use conditional statements to assign the correct letter grade to each student based on their final score. Here, we'll want to use the ranges presented in the problem and several `if-else` statements to look at each score and assign the letter that corresponds to it. We can add another `print()` statement at the end that will display the letter grades as they're assigned, to make sure our `if-else` statements are working like we think they are.

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

final_scores_dict = {"st1": 88, "st2": 78, "st3": 34, "st4": 97, "st5": 64,"st6": 89, "st7": 56, "st8": 83, "st9": 92}
letter_grades_dict = {}
for k,v in final_scores_dict.items():
    if v >= 90:
        grade = "A"
    elif 89 >= v >= 80:
        grade = "B"
    elif 79 >= v >= 70:
        grade = "C"
    elif 69 >= v >= 60:
        grade = "D"
    else:
        grade = "F"
    print(grade)

</script>
</lia-keep>
</div>

### Possible solution: Final

Finally, we need to build a dictionary where the keys are the student identifiers and the values are the newly-assigned letter grades. Since we've looped through the items in `final_scores_dict`, we can use the keys from `final_scores_dict` as the keys in our new `letter_grades_dict`, and then assign the letter grade for that student to that key as we loop through. The last thing is then to display our dictionary using one last `print()` statement. Note that we've moved it **outside** the loop now, so that it only prints once it's completely built and not every time we add a new key-value pair.

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

final_scores_dict = {"st1": 88, "st2": 78, "st3": 34, "st4": 97, "st5": 64,"st6": 89, "st7": 56, "st8": 83, "st9": 92}
letter_grades_dict = {}
for k,v in final_scores_dict.items():
    if v >= 90:
        grade = "A"
    elif 89 >= v >= 80:
        grade = "B"
    elif 79 >= v >= 70:
        grade = "C"
    elif 69 >= v >= 60:
        grade = "D"
    else:
        grade = "F"
    letter_grades_dict[k] = grade
print(letter_grades_dict)

</script>
</lia-keep>
</div>

Congratulations! You can now send the letter grades off to your teacher friend.

<div class = "care">
If this process seemed intimidating, that's understandable! Learning to code takes time, and there will be moments where things don't work. Things will come easier as you practice! And don't feel like failure if you have to Google how to do certain things over and over-- lots of people who write code for a living do the same thing!
</div>

## Additional Resources

* There are many helpful resources on [python.org](https://www.python.org/), including a [Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide) and [FAQs](https://docs.python.org/3/faq/).

* [W3 Schools has bite-sized explanations and examples of writing code in Python](https://www.w3schools.com/python/) if you want more clarity on how anything works.

* Jupyter notebooks are a great option for doing data analysis with Python-- [check out this Jupyter notebook demo](https://jupyter.org/try-jupyter/lab/), then open "notebooks" and look at "Intro.ipynb" to see how they work.

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Python+Basics+:+Writing+Python+Code%22)!

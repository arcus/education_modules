<!--

author:   Meredith Lee
email:    leemc@chop.edu
version:  0.0.1
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Module Title
comment: Learn the basics of writing Python code.
long_description: Before using Python for data analysis, there are some basics to learn that will set the foundation for more advanced Python coding. This module will teach you how to define and use variables, how to create and edit lists and dictionaries, and how use loops and conditional statements to perform tasks with these basic data structures.
estimated_time: 1 hour

@learning_objectives

After completion of this module, learners will be able to:

- Assign values and objects to variables
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

**Pre-requisites:** Learners should be familiar with [Python as a programming language](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/update-intro-to-python/intro_to_python/intro_to_python.md#1), but need not have any experience with actually writing Python code.

**Learning Objectives**:

@learning_objectives


</div>

## Lesson Preparation

For the hands-on activity in this module, we will be using an online environment containing a Jupyter notebook. To load the environment, open the link below in a new tab:

<div class = "important">
Please read over both options before you start performing any actions, to make sure you pick the right option for you.
</div>

Option 1: Work in the Cloud
=======

This might work well for you if you either can't or don't want to install Python and Jupyter on your computer, or are not familiar with working with directories or Github. The benefit is that you don't have to install anything, but one negative is that this option requires a bit of waiting for your environment to come online.

**First**, we need to create a small container in the cloud for you to work in just using your web browser.  **Click "Launch binder" below.**  It might take a couple of minutes to create, depending on how recently it was created (when it's being used more, it's quicker!).

<a href = "https://mybinder.org/v2/gh/arcus/education_modules/update-intro-to-python?labpath=intro_to_python%2Fnotebooks%2Fintro-to-python.ipynb" target = "_blank"> <img src = "https://mybinder.org/static/images/badge_logo.svg" alt="Launch binder."></a> **← Click the "launch binder" button!**

<div class = "hint" style = "align-items: center; display: flex;">

<div style = "margin: 1rem; max-width: 45%; float:left;"> If you're the first person to fire up this environment in a while, you might see this loading screen for a few minutes.  Be patient!</div>
<div style = "margin: 1rem auto; max-width: 45%; float:left;"> ![Binder loading screen.](media/binder_loading.gif)<!--
style = "border: 1px solid rgb(var(--color-highlight));"-->
</div>
</div>

Option 2: Work on Your Computer
=======

If you have [Python](https://www.python.org/) and [Jupyter](https://jupyter.org/) installed already on your local computer, and have some familiarity working with file directories or Github, you might be interested in simply downloading our sample code to your computer. If you haven't downloaded Python or Jupyter to your computer but would like to, you'll learn how in the [Next Steps](#next-steps) section of this module. Then you can come back here when you're done and follow these steps to download the code (If you already completed this work for a previous module, and it's been a while since you downloaded this project to your computer, you may want to get any new and improved files that have been placed there in the meantime):

* Go to the [GitHub repository](https://github.com/arcus/education_modules) where the materials for this lesson are located.
* You can use Git to **clone**, or download, a repository (or "repo", as it is sometimes called). Here are the steps to follow:

  * It is likely that Git is already installed on your computer, even if you've never used it before. Open the Terminal application (if you're using a Mac/Linux machine) or the Windows Powershell (if you're using Windows 10 or later -- here is [more information about finding the Windows Powershell](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_scripting_101/bash_scripting_101.md#5). Then run the code `git --version`. If Git is installed, you should see a version number. If not, check out [these instructions for installing git on Mac or PC](https://carpentries.github.io/workshop-template/#git).

  * You can also use GitHub Desktop, which you can use to interact with GitHub repositories. The [GitHub Desktop documentation](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/overview/getting-started-with-github-desktop) for download instructions and getting started.
  * If you are using Git in a command line interface, go to the [education_modules repository on GitHub.com](https://github.com/arcus/education_modules) and then follow [these instructions to clone the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository).

  <div class = "important">
  It's often useful to have a folder called `GitHub` on your computer for storing repositories that you clone. To navigate to a specific directory in the command line, use the `cd` command (check out the [Command Line 101 module](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_scripting_101/bash_scripting_101.md#1) for more information).
  </div>

  * If you are using GitHub desktop, follow [these instructions for cloning a repository from GitHub to GitHub Desktop](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop).

<div class = "options">
If you don't want to wait for the binder environment to load, but don't want to use git to clone the repository, you can also view the [rendered Jupyter notebook on GitHub](https://github.com/arcus/education_modules/blob/main/intro_to_python/notebooks/intro-to-python.ipynb). You will not be able to interact with the code, but if you have Jupyter installed you can copy and paste the code into code cells that you create in your own notebook.
</div>

## Introduction to Python code

Python is a flexible, multi-purpose programming language that has applications in web development, software engineering, and data analysis. Part of its power comes from the fact that it is **human-readable**, with a relatively simple syntax compared to many other programming languages. However, just like any language, there are some grammar rules to learn in order to use Python. In this module, we'll go through a few of the basics of Python that will build a foundation for your learning and practice.

### Functions and methods: Getting stuff done

In Python, there are two basic ways of taking something (such as text, a number, or even a collection of numbers or pieces of text) and performing some action on it: functions and methods. **Functions** take the syntax `function(arguments)`-- the name of the function, and then whatever you want to perform that function on (called **arguments**) in parentheses. A simple (but very useful) example of this is the `print()` function.

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
Tip: Some functions can be called on their own without any arguments, though this isn't common. The documentation for the function will tell you which, if any, arguments are required for a function. To call a function without any arguments, just leave the parentheses empty.
</div>

**Methods** in Python are very similar to functions, but are not precisely the same. The exact differences are not important to us right now, except that the syntax is a little different. Methods cannot be called by themselves; they are always called on an object, with the syntax `object.method()`.

Let's look at an example:

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

print("Hello World!".lower())

</script>
</lia-keep>
</div>

As you might have suspected, the `.lower()` method made all of the letters of the phrase "Hello World!" lowercase. The `.lower()` method is a **string method**, or a method that must be called on a string, of which "Hello World!" is an example. Let's talk more about strings and other data types next.

### Data Types

Strings are an example of a **data type** in Python; other data types include integers, floats (or decimal numbers), lists, and boolean (like True or False), but there are many more. Knowing what data type you're working with is important, because certain functions and methods will only work on certain data types, or will behave differently depending on the data type. The built-in function `type()` will return as output the data type of its argument.

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

print(type("Hello World!"))

</script>
</lia-keep>
</div>

When we pass the phrase "Hello World!" to the `type()` function, we get the output `<class 'str'>`, "str" being short for "string". A **string** is a sequence of characters; you tell Python that a sequence is a string by surrounding it in quotation marks. You can use either single or double quotes, but it's a good idea to be consistent. Strings are a specific data type in Python; other data types include integers, floats (or decimal numbers), lists, and boolean (like True or False), but there are many more. Try editing the code above, replacing "Hello World" with different inputs (for example "Hi", 9.8, 10, or False) and run the cell again to see how the output changes.

<div class = "important">
Notice that in the above example, we have passed the `type("Hello World!")` function call as an argument to `print()`. Nesting functions like this is common (you can do the same with methods), but there is another option we'll discuss in the next section-- using variables!
</div>

## Variables

Rather than passing a value (like a string or a number) directly to a function, we can also assign values to variables and pass those to functions. **Variables** are ways to store values and objects for use later.

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

### Quiz: Variables

## Lists

**Lists** in Python are objects that contain multiple items. They are surrounded by square brackets [ ] and the items in the list are separated by commas:

@sage
<div class="python_link">
<lia-keep>
<script type="text/x-sage">

produce = ["tomato", "squash", "apple", "cucumber", "peach", "spinach"]
print(produce)

</script>
</lia-keep>
</div>


Notice that the strings that we put into our list, like "tomato" or "squash", are in quotation marks, while the name of our list (`produce`) is not. In Python, variable names don't need quotation marks, but strings that aren't variables do, so that Python knows that they aren't variables. If, for example, you typed `squash` without defining it as a variable, you would get an error message that looks like this: `NameError: name 'squash' is not defined`. Variables are defined (or declared) when you assign a value to them.

There can be duplicate values in Python lists, and lists are changeable; you can add, remove, and edit items in a list. There are a few ways to do this, depending on exactly what you're trying to do:

* .pop( ) removes a specific element by index. The index is the element's position in the list, and in Python, indices start at 0. So the first element is at index 0, the second is at 1, and so on (this is not necessarily the case in other programming languages).

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    print(produce.pop(0))

    </script>
    </lia-keep>
    </div>

* .remove( ) removes a specific element by value.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    produce.remove("apple")
print(produce)

    </script>
    </lia-keep>
    </div>

* del deletes objects, and can be used as another way to remove elements of a list by index. The syntax will be a little different, because it is a keyword, not a list method. It is useful because it allows you to delete list elements in a slice.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    del produce[1:3]
print(produce)

    </script>
    </lia-keep>
    </div>

* .clear( ) removes everything from the list.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    produce.clear()
print(produce)

    </script>
    </lia-keep>
    </div>

* .append( ) adds an element to the end of a list.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    produce.append("pear")
print(produce)

    </script>
    </lia-keep>
    </div>

* .insert( ) adds an element to a specific position.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    produce.insert(0, "kale")
print(produce)

    </script>
    </lia-keep>
    </div>

* .extend( ) adds another list to your list (or another iterable object, but don't worry about that for now).

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
The code chunks above are linked, meaning that all of the chunks "remember" what the code that has been run previously (as they would be in a [notebook](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/update-intro-to-python/intro_to_python/intro_to_python.md#8)) and so if you run them out of order, you can get unexpected results or even errors! If things aren't working like they should, re-run the first code chunk on this page, or refresh the whole page.
</div>

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
Did you notice the explanatory text in the above code cell that started with a pound sign? The pound sign ( # ) in a code cell indicates the start of a **comment**. Comments aren't recognized as code and won't be run. Each line of a comment must be marked with a new pound sign. Comments are an excellent way to add brief explanations and clarifications about your code.
</div>

This example loops through the list of numbers, adds 5 to each number one at a time, and adds the sum to a new list using the append() method for lists. Finally, we printed the new list to our screen. This kind of loop is sometimes called a for loop; there is another kind of loop called a while loop, which is often used when we don't know the number of times we'll have to iterate through a block of code before we start (check out this page for more information about while loops).


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

**Your Turn**: Before running the code cell below, try to predict what number will be returned. Got a number in mind? Run the code and see if your hypothesis is correct! (**Hint**: the bracket notation below (`[ ]`) allows Python to access an element in a collection object, like a list; you saw it before when subsetting).

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

print(list(range(1, 20))[7])

</script>
</lia-keep>
</div>


### Quiz: Loops

## Conditional statements: If-else

Sometimes when you're working with Python, you might want your code to do different things in different circumstances. You handle this with an `if else`, or **conditional**, statement. Let's look at a simple example:

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

name = "Pythonista"
if type(name) == str: #We're testing here to see if the value of name is a string. This will either evaluate to True or False.
    print("Welcome, "+ name+"!")
else:
    print("Please enter a name.")

</script>
</lia-keep>
</div>

**Your Turn**: Try changing `name` in the code cell above to a number and see what happens! What happens if you remove the quotation marks?

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

Remember when we looped through a list of pieces of candy that some students started with and calculated the number they would have if we gave each student 5 more pieces? Let's suppose that the next day instead of giving all of the students in the class more candy, only the students who have fewer than 10 pieces of candy already get another piece. We can still calculate how many pieces of candy each student has now (even though we're making the very unlikely assumption that none of the students have eaten any of their candy from before!).

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

candy_day1 = [8, 15, 16, 11, 12]
candy_day2 = []
for i in candy_day1:
    if i < 10: #tests to see if each student has less than 10 pieces of candy
        j = i + 1
    else:
        j = i
    candy_day2.append(j)
print(candy_day2)

</script>
</lia-keep>
</div>

In the case above, we've used an if-else statement within our `for` loop! These loops can actually get quite complex for some tasks, but breaking down the loop and testing out the various pieces is often a good strategy.

### Quiz: Conditional statements

## Dictionaries

Another kind of collection object in Python is a **dictionary**. Dictionaries are similar to lists in some ways, in that they are ordered (in recent versions of Python; in older versions, dictionaries are unordered) and changeable. However, there are some important distinctions:

* Dictionaries are collections of key-value pairs. For example if you had a dictionary of demographic information for an individual, the **keys** might be the type of information stored (address, telephone number, etc.) and the **values** would be the actual values of those data (123 Puppydog Lane, 987-654-3210).

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

Like lists, dictionaries have some useful methods you can use to access or alter its data:

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

* `.items()` returns a list of the dictionary's key-value pairs as tuples (this may seem not very useful at first glance, but since different collection objects have different properties, there could be circumstances in which it is more useful to have the data in a different kind of object).

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
    Note that this change is permanent! If you want to keep the original dictionary as-is, you should make a copy of the dictionary by assigning it to a new variable, and then using `.pop()` on the copy. In this example though, all you need to do to restore the dictionary to its original form is re-run the first code cell or refresh the page.
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

### Quiz: Dictionaries

## It's Your Turn!

Ready to practice what you've learned?

A teacher friend of yours can never remember what the grade ranges are for letter grades. They have requested that you write some code that will take a list of final grades and return the letter grades corresponding to the score. After doing some research, you know that:

90-100 = "A"

80-89 = "B"

70-79 = "C"

60-69 = "D"

< 60 = "F"

Your friend also sends you the class's final grades, along with the student identifiers:

st1: 88, st2: 78, st3: 34, st4: 97, st5: 64, st6: 89, st7: 56, st8: 83, st9: 92

Using a for loop and if-else statements, can you write some code that returns a dictionary with the student identifiers as the keys and the letter grades that the students should be assigned as the values? If you get stumped, look at the next page for one possible approach.

If you do glance at the answer, note that your code might look a little different; as long as you get the output you're looking for, that's okay!

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

#Hint: You'll need the identifiers and the scores in your loop.
#If you get stuck, try googling something like "Python looping through items in a dictionary".

</script>
</lia-keep>
</div>

### Possible solution

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

## Additional Resources

The last section of the module content should be a list of additional resources, both ours and outside sources, including links to other modules that build on this content or are otherwise related.

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Module+Template%22)!

Remember to change the redcap link so that the module name is correct for this module!

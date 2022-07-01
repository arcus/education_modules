<!--

author:   Elizabeth Drellich
email:    drelliche@chop.edu
version:  0.0.1
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Bash: Conditionals and Loops
comment:  This module teaches you how to iterate through "for" loops and write conditional statements in Bash.
long_description: This lesson teaches the basics of loops (for all x, do y) and conditional statements (if x is true, do y) in Bash. Since the grammar of Bash can be non-intuitive this module is appropriate both for learners who have experience with conditionals and loops in other languages, as well as learners who are learning about these kinds of commands for the first time.

@learning_objectives  

After completion of this module, learners will be able to:

- Understand how a "for loop" works
- Write simple "for loop"s in Bash  
- Understand how an "if/then" statement works
- Recognize and reuse "if/then" statements in Bash

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Bash: Conditionals and Loops

<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

List any skills and knowledge needed to do this module here. When available, include links to resources, especially other modules we've made (to show learners where this falls within our catalog).

* navigate within CLI
* read and write files: `echo` `>>` `>`
* one skill we have [another module for, linked here](https://education.arcus.chop.edu)
* some familiarity with [a topic](https://education.arcus.chop.edu)
* understanding of [one thing](https://education.arcus.chop.edu) and [another](https://education.arcus.chop.edu)

If relevant, you can include recommendations for somewhere else to start if the learner doesn't have these prereqs. For example: If you are brand new to R or python (or want a refresher) consider starting with [Intro to R](link) or [Intro to python](link) first and then coming back here.

**Learning Objectives**

@learning_objectives

</div>

## Lesson Preparation

You will get the most out of this lesson if you follow along with the examples and try out the commands. In order to do that you need to have a bash shell open on your computer. Please follow the instructions appropriate for the computer you are using.

**Open a bash shell.**
If you are using a computer with running iOS (i.e. a Mac) you can use the **Terminal** program. If you are on a computer using Windows, open either **WLS** (Windows Linux Subsytem) or **Git Bash**. If you don't have these programs there are instructions for how to download and set them up in the [Bash / Command Line 101](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_101/bash_command_line_101.md) module.

<div class = "important">
We want to be able to search, move, and rename files during this module, but don't want to do that with your important files. Therefore we will set up a little directory with a few files to experiment with. You can safely delete the whole thing afterwards if you want.
</div>

**Download the files.**

Download the [`learning_bash` directory](https://github.com/arcus/learning_bash) from GitHub. Once you go to the link:

1. Click on the green **Code** button.
2. Select **Download ZIP**
3. Once the Zip file has downloaded, un-zipping it will create a folder titled `learning_bash-main`.
4. Place this new folder `learning_bash-main` somewhere you can easily find it. In the examples we will assume that `learning_bash-main` is in the Downloads directory, but you are welcome to move it somewhere else that is convenient for you to navigate to in your command line interface.

<div class = "warning">

Please download a fresh copy of these files. If you have downloaded them for a previous module, you have likely moved and changed some of them while working through that module and the examples in this module assume that no changes have already been made to the directory.

</div>

## Loops

**Iterating**

To **iterate** an action or command is the run it again and again. A common thing you might want to iterate if you have lots of files could be adding an appropriate file extension to the file name. You could iterate this action by hand, individually adding the extension to each file name, but that could be quite time-consuming and frustrating.

**Loops**

A **loop** is a bit of code that allows you to run the same command again and again. The loop gives instructions for how many times to run your code, and if it requires input, what that input should be.  With loops, you get to write your command once and then tell it to run as many times as you want!


<div class = "learnmore">

There are two kinds of loops: "for loops" and "while loops." In this lesson we will focus on "for loops" which are generally easier to create. "While loops" can be more powerful than for loops in [certain situations](https://betterprogramming.pub/how-to-pick-between-a-while-and-for-loop-14ef217c3776), so once you understand "for loops" they are worth checking out in your preferred programming languages.

</div>

### Structure of For Loops

**For loops** are a type of coding structure that exist across many programming languages. Once you understand how for loops work in theory, you can look up the specifics of running one in any language.

**For A in B do C**

A for loop needs some command (C) that it is looping, or doing over and over again. This command can be as simple or as complicated as you need it to be.

A for loop also needs some collection (B) to "iterate over" or "iterate through." This is the collection of objects for which the command (C) will be repeated. In our examples we will use lists, but there are several "iterable" data types. An object is iterable if there is a way to list out the individual elements of it.

For loops also need a way to refer elements in the collection B. This variable is how the command C will refer to the particular element it is acting on.

**General example**

Suppose B is the collection of numbers 2,3,4. If we want the square of each of those numbers we could write a for loop that says

```
for each number in the collection B, print the square of that number
```

This will have the same result as

```
print the square of 2, then print the square of 3, then print the square of 4
```

The code blocks above are written in **pseudocode**. Pseudocode is a description of code that shows humans its structure but isn't actually written in any programming language.

### Bash grammar of for loops

In Bash the structure "for A in B do C" is coded:

```
for A in B
do C
done
```

The line breaks are mainly to help us read the code we have written. Each line break could be removed as long as we add a semicolon `;` after each the first two clauses like this:

```
for A in B; do C; done
```

You might also see for loops displayed like this for better human-readability:

```
for A in B
do
   C
done
```

Indentation doesn't impact the code at all, (unlike in some other languages like Python), so indenting the command C is purely to help make it easier for humans to read the code.

Let's try out an example with our files. Make sure you `cd` into the `learning_bash-main` directory that you downloaded in the [lesson preparation section](#lesson-preparation). Try copying this code into your command line interface and see what happens:

```
for file in *.dat
do
  echo $file is a data file
done
```

The collection `*.dat` is a list all of the files in the directory that end with the `.dat` file extension. We could have listed them using `ls *.dat` but that wouldn't have allowed us to add the extra text "is a data file" to each line.

<div class = "important">

**`file` versus `$file`**

In the first line `for file in *.dat` we are telling Bash that the variable "file" will refer to the elements in the list `*.dat`. However when we want to actually use the variable, we need to start with the dollar sign `$` to tell Bash that it should treat `$file` as a variable and not as the string of characters. To see the importance of the `$` when calling the variable, try omitting it  from the third line. What do you think the output will be?

</div>

**Variable names**

You can name your variable anything you want as long as there are no spaces in the name, but the best practice is to name it something informative that helps you understand what your code is doing. For example both of  these have the same output as the code block above:

```
for z in *.dat; do echo $z; done
```

```
for swivel_chair in *.dat; do echo $swivel_chair; done
```
The first one doesn't give any context for what the variable `$z` represents, and the second will be extra confusing to you and anyone else who wants to know what your code does later!

### More complicated loops

Any command or sequence of commands can be repeated using a for loop.

Maybe you to see all of the data files and all of their contents, and also want that information displayed with an empty line between each animal's data:

```
for file in *.dat
do
  echo $file
  cat $file
  echo
done
```

Maybe you want to create a new file called `my_data` that contains all of that output you just printed. The best way to do that is to redirect each line of output to be appended to `my_data`:

```
for file in *.dat
do
  echo $file >> my_data
  cat $file >> my_data
  echo >> my_data
done
```

There isn't any output because you redirected it all, so use `cat my_data` to check that it worked!

You can also create loops that redirect some output but while also showing you output. This can be a way to check that your code is working if you have a loop that takes a long time to run.

```
for file in *.txt
do
  echo $file >> my_animals
  cat $file >> my_animals
  echo >> my_animals
  echo $file was processed
done
```

This runs very quickly, but you can see that you got the output that each file was processed, and check that it appeared as you wanted in `my_animals`.

### Nesting Loops

You can even put a loop inside of another loop! This is called **nesting** and nested loops can allow you to iterate over two (or more!) collections of objects.

Perhaps you want to make some empty files for giant squid, elephant, and albatross. You just want each of these animals to have an empty `.txt` file and and empty `.dat` file. A nested loop can be a good way to do this:

```
for animal in giant_squid elephant albatross
do
  for filetype in .txt .dat
  do
    touch $animal$filetype
    echo $animal$filetype has been created
  done
done
```

Now use `ls` to check the files in your directory. You should have just created six new files!

<div class = "warning">

Make sure when you are nesting loops that you give your variables different names!

</div>

### Quiz: Loops

## Conditional Statements

Loops are great for doing the same thing over and over again, but what if you only want to run the command sometimes? Maybe you want to record the filename in a list, but only if the file is non-empty.

This is where conditional statements come in! A conditional evaluates if a statement is true, and if it is true, executes a command. The most basic conditional statements take the form "if/then."

"**If** the file is empty, **then** delete the file."

Using a conditional clause like this can automate the process so that the computer checks whether the file is true rather than you having to do it!

That said, the Bash language does not make it easy to write conditional statements. Over the next few pages you will learn

* how conditionals work in general (not specific to the Bash language)
* how to recognize conditionals in Bash
* how to make small changes to existing code.

If you find that you need to use conditionals a lot in Bash, you will probably settle on a favorite cheat sheet, of which there are many. (links here and in additional resources)

### Statements

A statement (or mathematical statement) is something that can be evaluated as either true or false. Here are some examples:

- 5 = 7
- 100 is greater than 50
- The string "blue" appears in this file's name
- This file is empty
- The contents of these two files are identical

The first statement is false, the second one is true, and the last three can be determined to be true or false as soon as "this file" or "these two files" are identified.

Opinions, questions, and instructions are among the many things that we can say that do not fall into the category of mathematical statements.


### If / Then Structure

The basic structure of an if / then statement in Bash is:

```
if STATEMENT
then RUN THIS COMMAND
fi
```
The three lines together make up the conditional statement.

* `if` tells the computer to check whether the statement following it is true or false
* `then` tells the computer what to do if the statement is true
* `fi` tells the computer that the conditional statement is completed.

Let's see a working example:

```
if [ 5 -eq 05 ]
then echo "integer equality"
fi
```

<div class = "important">

In Bash, statements are surrounded by square brackets with a space after the opening `[` and before the closing `]`. A Bash statement looks like this:

`[ statement here ]`

</div>
The statement `[ 5 -eq 05 ]` is checking if the numbers `5` and `05` are equal to each other. The command `echo "integer equality"` only runs if the numbers are equal. If you change the `05` to `04`, this code will not return any output.

**`else`**

You can also give instructions for what to do if the statement evaluates as false by adding a line starting with `else` after your `then` statement:

```
if [ 5 -eq 05 ]
then echo "integer equality"
else echo "these numbers are not equal"
fi
```

Running this code exactly as is will give you the same output you got before. But now if you change the `5` or `05` so that the integers are not equal, you will get a message telling you that!

**`elif`**

The command `elif` is a shortening of the words "else if". This allows you to tell the computer to check another statement if the first statement is false. The `elif` line is followed by its own instance of `then` with instructions for what to do if that statement is true:

```
a=5
b=6
if [ $a -eq $b ]
then echo "integer equality"
elif [ $a -lt $b ]
then echo "$a is smaller than $b"
else echo "$a is greater than $b"
fi
```

The statement `[ $a -lt $b ]` tests whether the variable `$a` is less than the variable `$b`. Similarly, `[ $a -gt $b ]` tests whether `$a` is greather than `$b`.

<div class = "important">

**Assigning Variables in Bash**

Variables in Bash are assigned values using the equals symbol `=` with **no spaces** around it. When you want to refer to a variable later, use the dollar symbol `$` followed by the variable name, again with no spaces separating them.

</div>

You can have as many `elif` and `then` pairs as you want, but as soon as one is statement is true, the code will do that action and not continue to check the remaining statements. Try to think about what this code will output, then run it and check if you were right:

```
c=100
if [ $c -lt 10 ]
then echo "$c is a single digit number"
elif [ $c -gt 99 ]
then echo "$c is a big number"
elif [ $c -eq 100 ]
then echo "$c is one hundred"
fi
```


### Bash examples



<div class = "help">

**Bash is not designed for humans**

Don't worry about trying to memorize these statements. Even people who are writing this kind of code daily regularly have to look up these statements.

It is more important to know what types of commands are possible so that you can envision what you want your code to do. You can always return to this page or type something like "Bash file is empty statement" into a search engine to quickly find what you need.

</div>

In Bash, statements are written surrounded by square brackets: `[ statement here ]`

To get us started, here are some useful Bash statements:

|Code| Meaning|
|:-:| :-|
| `[ -e FILE ]` | FILE exists |
| `[ -s FILE ]` | FILE exists and is non-empty|
|`[ STRING1 = STRING2 ]` | STRING1 is equal (identical) to STRING2 |
|`[ INTEGER1 -eq INTEGER2 ]` | INTEGER1 is equal (numerically) to INTEGER2|
|`[ INTEGER1 -gt INTEGER2 ]` | INTEGER1 is greater than  INTEGER2|
|`[ INTEGER1 -lt INTEGER2 ]` | INTEGER1 is less than INTEGER2|


<div class = "learnmore">

Under the hood, these statements are using Bash's `test` utility. You can see all of the possible ways to use `test` by running the command `man test` to see it's documentation.

</div>

As you use them more, you will learn more and more ways to combine and mix mathematical statements to make new ones. The basic ways to combine expressions are:

|Code| Meaning|
|:-:| :-|
| `[EXPRESSION1] && [EXPRESSION2]` | Both EXPRESSION1 and EXPRESSION2 are true |
| `[EXPRESSION1] || [EXPRESSION2]` | One or both are true |

### Quiz: Conditional Statements


## Additional Resources

The last section of the module content should be a list of additional resources, both ours and outside sources, including links to other modules that build on this content or are otherwise related.

https://swcarpentry.github.io/shell-novice/

https://swcarpentry.github.io/shell-novice/05-loop/index.html


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

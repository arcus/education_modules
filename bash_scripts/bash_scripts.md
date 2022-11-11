<!--

author:   Nicole Feldman and Elizabeth Drellich
email:    feldmanna@chop.edu and drelliche@chop.edu
version:  1.0.0
module_template_version: 2.0.0
language: en
narrator: UK English Female
title:  Bash: Scripting Basics
comment:  This module will teach you how to create and use simple bash scripts so to make repetitive tasks as simple as possible. If you have some experience with bash and want to learn how to save and reuse bash processes, this lesson is for you.
estimated_time: 30 minutes

@learning_objectives

After completion of this module, learners will be able to:

- Identify the structure of a bash script
- Call bash scripts
- Write simple bash scripts
@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js
-->

# Bash: Scripting Basics

<div class = "overview">

## Overview

@comment

**Is this module right for me?**

@long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

Learners should be familiar with using a bash shell to navigate a directory system. Learners will get the most out of this lesson if they can also create directories and files, write text to files, and read files from their bash shell command line interface.



**Learning Objectives**

@learning_objectives

</div>


## Lesson Preparation

You will get the most out of this lesson if you follow along with the examples and try out the commands.

**Open a bash shell.**

If you are using a computer with running iOS (i.e. a Mac) you can use the **Terminal** program. If you are on a computer using Windows, open either **WLS** (Windows Linux Subsytem) or **Git Bash**. If you don't have these programs there are instructions for how to download and set them up in the [Bash 101](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_101/bash_command_line_101.md) module.

<div class = "important">
We want to be able to search, move, and rename files during this module, but don't want to do that with your important files. Therefore we will set up a little directory with a few files to experiment with. You can safely delete the whole thing afterwards if you want.
</div>

**Download the files.**

We will be using a directory called `learning-bash` that is publicly available on GitHub. If you have already downloaded this directory for use in another bash module, you do not need to download a fresh copy.

Navigate in your browser to the [`learning_bash` directory](https://github.com/arcus/learning_bash) on GitHub. Once you follow the link:

1. Click on the green **Code** button.
2. Select **Download ZIP**
3. Once the Zip file has downloaded, un-zipping it will create a folder titled `learning_bash-main`.
4. Place this new folder `learning_bash-main` somewhere you can easily find it. In the examples we will assume that `learning_bash-main` is in the Downloads directory, but you are welcome to move it somewhere else that is convenient for you to navigate to in your command line interface.

## What is a script?

A **script** is a small program that you can run on your computer.

A **bash script** is a small program that automates bash commands and lets you run the same sequence of commands as many times as you want. It might be as simple as a program that takes a file you have downloaded and standardizes the file name, or as complicated as creating new files based on information stored in several other files in other locations or doing complex tasks based on a user's typed responses to questions.

You might have heard the terms "script" and "bash scripting" and "shell script" used interchangeably. This is probably because the Bash language is most powerful when you use it to write short scripts that do exactly what you want. Once you get the hang of writing scripts, you can automate almost any work that you expect to need to use multiple times!

<div class = "learnmore">
A **scripting language** is a type of programming language that, like bash or python, does not need to be compiled in order for your code to run.
</div>


### Recognizing a Bash script

You don't have to be able to write a script in order to use one, but you do need to know how to recognize one. Any file could in theory be a Bash script, but there are a few conventions that good scripts frequently use to help you, and your computer, know that they file is a script.

**File name**

The standard file ending for a script is `.sh`. Usually a script will be informatively named, for example `fibonacci.sh` might be a script that computes the numbers in the Fibonacci sequence. Even though scripts don't have to use the file ending `.sh`, this is the most common way to name them so that you and your collaborators can locate all of the scripts quickly and easily (i.e. `find *.sh`).

**First line**

Sometimes scripts contain a special first line that looks something like this:

```
#! /usr/bin/bash
```

This first line tells your computer that it should run the rest of the file as Bash code. If you are in a Bash shell, the script will run even without this line. However as you use scripting to speed up more and more processes, you may want to run a Bash script from a different place, say inside of an R program, where telling your computer the following code is Bash is necessary. On the other hand you might see a script that starts with the first line `#! /usr/bin/python`. This would tell both you and your computer that the following code is not in Bash, but in the programming language Python.

The two symbol sequence `#!` is called a [**shebang**](https://en.wikipedia.org/wiki/Shebang_(Unix) and without it your computer wouldn't know that it is expected to run what follows as code.

<div class = "learnmore">

The symbol `#` has [many names](https://en.wikipedia.org/wiki/Number_sign#). You might be most familiar with it as a "hashtag," "number sign," or the "pound sign." In the context of coding it is usually called either a "hash" or, borrowing from musical notation, a "sharp."

In the context of coding, the symbol `!` is called a "bang." The word shebang is a shortening of either ha**sh**-bang or **sh**arp-bang.

</div>

**The example scripts in this module will not start with `#! /usr/bin/bash` for two reasons:**

1. Since we will be running all scripts from inside of a Bash shell, your computer will assume that the code is Bash without being told.
2. The path `usr/bin/bash` may not be exactly where the Bash language lives on your computer. If you start combining scripts of different languages or running Bash scripts from outside of the Bash shell, you will need to find out where Bash is stored on your computer and use that path in the first line of any scripts. That, however, is outside the scope of this module.



### Quiz: Scripts

Which of the following statements about scripts are TRUE?


[[ ]] A script isn't very useful because you could just as easily run code by typing it in line by line.
[[X]] The standard file ending for a script file is `.sh`.
[[ ]] Every bash command is a script.
[[X]] If you are going to want to do a particular sequence of commands many times, a script can help you by automating that sequence.
***
<div class = "answer">

**A script isn't very useful because you could just as easily run code by typing it in line by line.** FALSE: You can speed up the process a lot, and avoid typos, but using a script to automate procedures you want to do multiple times!

**The standard file ending for a script file is `.sh`.** TRUE: Although the file ending doesn't impact what the script does, ending the file name with `.sh` is standard practice.

**Every bash command is a script.** FALSE: Even though bash is a "scripting language," the word "script" refers to a small program, not an individual bash command.

**If you are going to want to do a particular sequence of commands many times, a script can help you by automating that sequence.** TRUE

</div>
***

## Calling an existing script

In this section we will learn how to use the pre-written scripts in the `scripts` folder inside your `learning_bash-main` directory.

Navigate to the `scripts` folder and use `ls` to take a look at the example scripts there.

```
count_mammals.sh
count_type.sh
interactive_count_type.sh
```

The `.sh` file extension tells us these are scripts, but they are also just plain text files so we can look at the contents with `cat`. Try `cat count_mammals.sh` and see what it contains.

The first lines starting with `#`s are a description of what the code does. The `#` symbol (not followed by a `!`) tells the computer that what follows is a **comment** for human readers of this file, not code that the computer should try to read. While every script _should_ include a commented out section explaining its function, not every script does.

<div class = "warning">

Using a script written by a trusted colleague can help you streamline your work without replicating their effort! But running a script you downloaded off of the internet isn't a good idea unless you can look at the code and verify that it does what you think it should, and nothing else.

</div>

### Running a script with `bash`

The command `bash` takes a file as its argument and executes all of the commands in that file. Every line in the file that is not commented out with a `#` will be automatically entered into the command line, in order.

The `count_mammals.sh` script contains two lines of code:

```
count=`grep mammal Animals.csv | wc -l`

echo There are $count mammals on the list.
```

Entering these two lines into the command line by hand will give you the exact same output as running the script.

Where are you?
---
The first line of code above assumes that there is a file called `Animals.csv` in your present working directory. If you try to run that command from somewhere else, like inside the `scripts` directory, you will get an error message.

Give it a try:

```
count=`grep mammal Animals.csv | wc -l`
```

If you are in `scripts` you will get the message:

```
No such file or directory
```

But if you are in `learning_bash-main` you won't get any output at all. This is because the code is defining a variable, `count`. Try running the second line and see what happens:

```
echo There are $count mammals on the list.
```

Where is the script?
---
The commands inside of the `count_mammals.sh` script need to be run from the `learning_bash-main` directory, but that is not where the script itself is. You can use the relative path `scripts/count_mammals.sh` to refer to the file from that main directory.

Try it yourself
---
Use `pwd` to check that you are currently in the `learning_bash-main` directory, and if not, navigate there. Now you can call the script with the `bash` command:

```
bash scripts/count_mammals.sh
```

### Scripts that take arguments

The `bash` command takes only one argument, the name of a file, but that file may itself take one or more arguments. These arguments follow the name of the file.

The `count_type.sh` script takes one argument. Give it a try:

```
bash scripts/count_type.sh mammal
```

Try running the command again but replacing the argument `mammal` with `fish`, `red`, `bear`, or `alien`. What happens?

### Interactive scripts

The third script also takes an argument, but instead of getting that argument from the entry into the command line, this script prompts you (the user) to enter the argument it needs.

Try running it:

```
bash scripts/interactive_count_type.sh
```

You will get a message asking you what string you want to search for. Type a string (e.g. `mammal` or `fish` or `red`) and press the `enter` or `return` key.

Each time you run this interactive script, you can enter a different string to search for in the `Animals.csv` file.

### Quiz: Calling scripts


## Writing a script

### Location

Setting up a User/Home Directory

- As you get comfortable in bash, it is important to create a default home directory in an easily accessible place.
- It is recommended that you use the native user directory in the home directory on your computer. Your user directory contains a folder named “bin” which is the root directory of any unix like operating system.
- Bin is short for “binary” and is where you can store any configuration or executable files for programs you run on the CLI. This will be a good place to store bash scripts (.sh files) once you have become comfortable executing commands and learning syntax.


`/bin` folder?

### Basic commands
### Bash syntax

- `~` shortcut for your home directory
- `.` shortcut for your current directory
- `..` shortcut for your previous directory
  The above three shortcuts are highly useful for executing scripts in the proper location once you are collaborating in an active project with multiple files and folders.

  - `echo`: prints out text in the terminal window- especially useful for declaring environment variables which reveal both permissions and what strings can be passed.

    ![Echo variable example demonstrating how to print and set the price of a pint.](media/echo_example_large.png)


#### Writing output to a file with `>`
- `>` takes the output of the command you executed in the terminal and places it in a new file

#### Linking commands with `|`

- `|` takes the output of one command and passes it to the next command in the sequence. Allows for integrating of commands

#### Defining variables with `$`
- `$` used to define a variable expression as used in the echo example above.


### Quiz: Writing scripts




## Additional Resources

- [Brief Illustration of the Difference between Shell and Kernel](https://www.geeksforgeeks.org/difference-between-shell-and-kernel/)
- [Exhaustive Wiki of Linux Filesystem Hierarchy](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/index.html)
- [Reinforce Your New Knowledge through this Learing the Shell Page](https://linuxcommand.org/lc3_learning_the_shell.php)
- [Unix Command Line I Arcus Education Webinar](https://digitalrepository.chop.edu/commandline_computingtools/3/)
- [Unix Command Line II Arcus Education Webinar](https://digitalrepository.chop.edu/commandline_computingtools/2/)
- [Intermediate Bash Scripting Arcus Education Webinar](https://digitalrepository.chop.edu/commandline_computingtools/1/)

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work. Thank you in advance for [filling out our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Bash+Scripting+Basic%22)!

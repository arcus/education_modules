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

You will get the most out of this lesson if you follow along with the examples and try out the commands. In order to do that you need to have a bash shell open on your computer.





## What is a script?

A **script** is a small program that you can run on your computer.

A **bash script** is a small program that automates bash commands and lets you run the same sequence of commands as many times as you want. It might be as simple as a program that takes a file you have downloaded and standardizes the file name, or as complicated as creating new files based on information stored in several other files in other locations or doing complex tasks based on a user's typed responses to questions.

You might have heard the terms "script" and "bash scripting" and "shell script" used interchangeably. This is probably because the bash language is most powerful when you use it to write short scripts that do exactly what you want. Once you get the hang of writing scripts, you can automate almost any work that you expect to need to use multiple times!

### Recognizing a script

You don't have to be able to write a script in order to use one, but you do need to know how to recognize one.

The conventional file ending for a script is `.sh`. Usually a script will be informatively named, for example `fibonacci.sh` might be a script that computes the numbers in the Fibonacci sequence. Even though scripts don't have to use the file ending `.sh`, this is the most common way to name them so that you and your collaborators can locate all of the scripts quickly and easily (i.e. `find *.sh`).

 and Title, shebang start line, end in `.sh`

<div class = "warning">
Using a script written by a trusted colleague can help you streamline your work without replicating their effort! But downloading a script off of the internet isn't a good idea unless you can look at the code and verify that it does what you think it should, and nothing else.
</div>



### Quiz: Scripts


## Calling a script
downloadable examples?
### Basic examples

### Scripts that take arguments

### Interactive scripts


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

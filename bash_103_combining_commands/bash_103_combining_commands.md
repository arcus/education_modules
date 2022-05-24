<!--

author:   Nicole Feldman and Elizabeth Drellich
email:    feldmanna@chop.edu and drelliche@chop.edu
version:  1.0.0
module_template_version: 2.0.0
language: en
narrator: UK English Female
title:  Bash: Combining Commands
comment:  This module will teach you how to combine two or more commands in bash to create more complicated pipelines.
long_description: This module is for learners who can use some basic bash commands and want to learn to how to combine multiple commands to make full use of the power of the bash language.
estimated_time: 30 minutes

@learning_objectives

After completion of this module, learners will be able to:

- Write the output of a command to a file using `>` and `>>`
- Chain commands using the pipe `|`
@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js
-->

# Bash: Combining Commands

<div class = "overview">

## Overview

@comment

**Is this module right for me?**

@long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

Learners should be familiar with using a bash shell and a few basic commands. This module will assume that learners have encountered bash the commands `find` and `grep`.


**Learning Objectives**

@learning_objectives

</div>


## Lesson Preparation

You will get the most out of this lesson if you follow along with the examples and try out the commands.

**Open a bash shell.**

If you are using a computer with running iOS (i.e. a Mac) you can use the **Terminal** program. If you are on a computer using Windows, open either **WLS** (Windows Linux Subsytem) or **Git Bash**. If you don't have these programs there are instructions for how to download and set them up in the [Bash 101](link/here) module.

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

## Writing output to a file

### Overwriting a file

### Appending output to the end of a file

### Quiz: writing output to files

## Linking commands

### Using the pipe `|`

### Quiz: linking with `|`


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

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
- Write "if/then" statements
- Combine loops and conditional statements to create powerful code.

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


## Loops

Why would you want to iterate? do the same thing a whole bunch of times!

### Structure of for loops
Components of a loop: for A in B do C done.

### Examples

### Examples: Nesting loop


### Quiz: Loops

## Conditional Statements

Why do you want to check if/then?

### if
If D is true, then E.

### elif
If D is true, then E, elif F then G

### else
If D is true, then E, elif F then G, else H

### Examples

### Quiz: Conditional Statements

## Combining Loops and Conditional Statements
for A in B do if D then E else H.

### Quiz


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

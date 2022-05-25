<!--

author:   Nicole Feldman and Elizabeth Drellich
email:    feldmanna@chop.edu and drelliche@chop.edu
version:  1.0.0
module_template_version: 2.0.0
language: en
narrator: UK English Female
title:  Bash: Combining Commands
comment:  This module will teach you how to combine two or more commands in bash to create more complicated pipelines.
long_description: This module is for learners who can use some basic bash commands and want to learn to how to use the output of one command as the input for another command.
estimated_time: 30 minutes

@learning_objectives

After completion of this module, learners will be able to:

- Write the output of a command to a file using `>` and `>>`
- Chain commands directly using the pipe `|`
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

Learners should be familiar with using a bash shell and [navigating a file system from the command line](link/to/bash101).
This module will assume that learners have encountered bash the commands [`find` and `grep`](link/to/search/and/organize/module).


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

## Inputs and Outputs

The purpose of any command is to take some input and do something with it. The input might a file, a folder, or something you typed in. In the case of `ls` and `pwd` the input is your location in your file system.

Some commands also return output based on the input. For example `grep` returns a list of lines that contain a given regular expression, but doesn't make any changes to any files.

As your bash scripting progresses, you may find or create commands that simultaneously change files and return and output, but the commands we will see in this lesson return output without modifying their input.

### Examples

In your command line interface, use `cd` to navigate to the directory `learning_bash-main` that you downloaded in the [lesson preparation](#lesson-preparation) section. Since the commands we are learning in this section don't make any changes to your files, definitely try them out on some of your own files too!

**Word count**
`wc`

**First and last lines of a file**
`head`
`tail`

**Sorting**
`sort`

**Unique occurrences**
`uniq`

### Writing output to a file

The commands we just saw give us information and insight through their outputs, but that output isn't actually preserved anywhere. If we want to see it again, or use it for something later without re-running the command, we need to save that output in a file. This process is called "writing output to a file" or "redirecting output to a file" because instead of the output being shown to us in the command line interface, it is instead going to be written and saved to the file we name.

The "greater than" symbol
Create a new file `>`

Append to an existing file `>>`

### Quiz: inputs and outputs


## Linking commands

We could link commands by writing the output of one command to a file, and then running another command on that file. However if we don't actually need that intermediate file it is possible to speed up the process by passing the output of one command directly to another using a "pipe."

With smaller files, the benefits of using pipes over making intermediate files are mostly from having fewer commands to type and run. But if you start working with really large datasets, maybe you are working in an "omics" field like genomics or metabolomics, creating and saving intermediate files, as well as writing and reading them, can use significant time and energy.  

### Using the pipe `|`

### Quiz: linking with `|`


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

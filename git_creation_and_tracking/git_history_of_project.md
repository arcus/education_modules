<!--

author:  Elizabeth Drellich
email:    drelliche@chop.edu
version:  0.0.1
language: en
narrator: UK English Female
title: Exploring the History of your Git Repository
comment:  This module will teach you how to look at past versions of your work on Git, compare versions, and return to former versions.
long_description: You know that version control is important. You know how to save your work to your Git repository. Now you are ready to look at and compare different versions of your work. In this module you will you will learn how to navigate through the commits you have made to Git. You will also learn how to compare current code with past code, and, if necessary, revert to an earlier version of your work.

@learning_objectives  
After completion of this module, learners will be able to:

- Identify and use the HEAD of a repository.
- Identify and use Git commit numbers.
- Compare various versions of tracked files.
- Restore old versions of files.

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Exploring the History of your Git Repository


<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:**

**Pre-requisites**

This module is for you if:

* You know that version control is important. (See [module](module) to learn why version control is important.)
* You know how to save your work to your Git repository. (See [module](module) to learn how to create a Git repository and put your work into it.)
* You want to learn how to see and compare different versions of your work.


**Learning Objectives**

@learning_objectives

</div>

## Lesson Preparation

*We need some sort of virtual box here, probably the best way (if possible) would be to have virtual box that can come preloaded with all of the commands from the previous module so that learners can explore the history without having to go through that entire module, especially if they did it a while back, or already know that stuff.*

If you are coming to this module directly from the [previous one](link) and still have that console open, you can continue using that console instead.

## Seeing prior commits
Keeping track of all versions and being able to see and compare them is the entire point of using version control on a project you are working on alone. It is also a huge part of working on a project with others, but we will get to that part in [module](module).

There are generally two ways to refer to past commits:

- Using HEAD to see the latest `commit` and or the commit that was $n$ steps earlier.
- Using the commit number assigned to a particular `commit`.

*This needs a really good picture; the stack of disks that swcarpentry has is pretty meh... but once a good picture is made, we can easily refer to the two different ways to access a particular*`commit`.

### Using HEAD

Example of `git show HEAD` and `git show HEAD~1`

Update and commit, then `git show HEAD` and `git show HEAD~1` AND `git show HEAD~2`

### Using the commit number

Knowing how far back a commit was could be very easy if it was one or two back, but maybe you don't remember how many commits you want to go back, but you do know what change you want to look at.

Using `git log` to find the right commit message (hey, good reason to write good messages!) and identify the commit number, then use the commit number to show that change. Also `git log -n 5` for only the last 5 commits.

### Knowledge Check 1

How would you look at a particular commit?
Which two commands could you use to look at the most recent commit?

## Comparing prior commits

Using `diff` command to compare current version with HEAD and earlier HEADs.

### Knowledge Check 2

compare a file at two different times

## Undoing changes with Git

One big reason we save older versions of our work is so that we can go back to an earlier version if something we did doesn't work out.

### Changes not yet committed

Using the git checkout command, big warnings about including the file name so you don't lose things you didn't want to lose.

### Revert to an earlier version

Big warnings around this part!!

### Knowledge Check 3

quiz!

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

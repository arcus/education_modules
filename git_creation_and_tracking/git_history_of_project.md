<!--

author:  Elizabeth Drellich
email:    drelliche@chop.edu
version:  0.0.1
language: en
narrator: UK English Female
title: Module Title
comment:  This is a short, focused description of the module.
long_description: This is a longer description, which should be understandable for a lay audience. It will print under "Is this module right for me?" in the overview.

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

List any skills and knowledge needed to do this module here. When available, include links to resources, especially other modules we've made (to show learners where this falls within our catalog).

* one skill we have [another module for, linked here](https://education.arcus.chop.edu)
* some familiarity with [a topic](https://education.arcus.chop.edu)
* understanding of [one thing](https://education.arcus.chop.edu) and [another](https://education.arcus.chop.edu)

If relevant, you can include recommendations for somewhere else to start if the learner doesn't have these prereqs. For example: If you are brand new to R or python (or want a refresher) consider starting with [Intro to R](link) or [Intro to python](link) first and then coming back here.

**Learning Objectives**

@learning_objectives

For help articulating learning objectives, see [this guide to learning objectives, including lots of example verbs](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/).

</div>

## Lesson Preparation

If your module includes code learners may want to run, then give links to a pangeo binder here so they can start it up now. Also provide a link to the raw code so learners can download the code itself and run it on their own machines or copy it into a cloud server.

This module makes use of [pangeo binder](https://binder.pangeo.io/) for interactive code examples in R and python. You don't need to install anything or set up an account, but you need a modern web browser like Chrome and a moderately good wifi connection. If you have R and/or python already installed on your computer and you prefer to work through code examples there, you can <a href="https://raw.githubusercontent.com/arcus/education_modules/main/data_visualization_in_ggplot2/data_visualization_ggplot2.r" download>download the code for this module to run offline</a>.

If you intend to do the hands-on activities in this module with pangeo binder, we have a bit of preparation for you to do now. Because it can take a few minutes for the environment to be created, we suggest you click the link below to start up the activity. We recommend using right-click to open it in a new tab or window, and then returning here to continue learning while the environment finishes loading. Here is the link:

[![Link to start Binder environment](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/arcus/education_r_environment/main?urlpath=rstudio) **Click the "launch binder" button!**

You don't have to do anything except come back here once the link opens in a new tab or window.

## Seeing prior commits
Keeping track of all versions and being able to see and compare them is the entire point of using version control on a project you are working on alone. It is also a huge part of working on a project with others, but we will get to that part in [module](module).

There are generally two ways to refer to past commits:

- Using HEAD to see the latest `commit` and or the commit that was $n$ steps earlier.
- Using the commit number assigned to a particular `commit`.

### Using HEAD
swcarpentry stuff
### Using the commit number
swcarpentry stuff
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

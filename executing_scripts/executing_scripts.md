<!--

author:   Elizabeth Drellich
email:    drelliche@chop.edu
version:  1.0.0
module_template_version: 3.0.0
language: en
narrator: UK English Female
title: Module Title
comment:  This modules will teach you what you need to know about permissions and your PATH to make scripts executable.
long_description: A very common frustration in programming is getting a script that does the task you need done, but doesn't run on your computer. This module will teach you how to change permissions and add programming languages to your path so that you can actually run those scripts.
estimated_time: This is rough guess of how long it might take a learner to work through the module. It will print under "Estimated time to completion" in the overview

@learning_objectives  

After completion of this module, learners will be able to:

- check and change a file's permissions
- add a directory to the PATH
- execute a script.

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Executing Scripts

<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

In order to complete this module you will need:

* access to a command line console on your computer
* some familiarity with [navigating from command line](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_101/bash_command_line_101.md)

It will be helpful, but not strictly necessary, for you to have some familiarity with [writing bash scripts](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_scripts/bash_scripts.md).

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

## What is an Executable Script?

description, warning, script vs executable script

### Why are they wonderful?

### Why isn't it working?!?!

## File Permissions and Ownership

### Changing Permissions with `chmod`

### Changing Ownership with `chown`

### Quiz: Permissions

## Your `PATH`

### Finding your `PATH`

`which bash` etc.

### Adding to your `PATH`

### Quiz: `PATH`

## Executing Scripts

let's actually execute a script!! get the joy of making it work.
### Hands on Practice

### Quiz: Executing Scripts


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

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Executing+Scripts%22)!

Remember to change the redcap link so that the module name is correct for this module!

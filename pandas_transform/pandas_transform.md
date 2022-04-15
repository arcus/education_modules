<!--

author:   Elizabeth Drellich
email:    drelliche@chop.edu
version:  0.0.1
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Module Title
comment:  This is a short, focused description of the module.
long_description: This is a longer description, which should be understandable for a lay audience. It will print under "Is this module right for me?" in the overview.
estimated_time: This is rough guess of how long it might take a learner to work through the module. It will print under "Estimated time to completion" in the overview

@learning_objectives  

After completion of this module, learners will be able to:

- Navigate the row and column structure of a `pandas` DataFrame
- Locate data using the `.loc` method
- Filter data using conditional statements
- Create new DataFrames from existing DataFrames
- Edit data in a `pandas` DataFrame.

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Transforming Data in Python using Pandas

(Note that the title is the only level-1 header in the document)

To see how to use this template, you'll need to look at this file in its [raw format](https://raw.githubusercontent.com/arcus/education_r25/main/working_documentation/template_modules.md?token=ACEVZUTXZ6BTRFIIBXPN4SDBD3FR6).
To see what it looks like rendered via LiaScript, [click here](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_r25/main/working_documentation/template_modules.md?token=ACEVZUTXZ6BTRFIIBXPN4SDBD3FR6#1) or go to [https://liascript.github.io/](https://liascript.github.io/) and paste the link to the **raw** file into the box on that page and click "load course".

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

For help articulating learning objectives, see [this guide to learning objectives, including lots of example verbs](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/).

</div>

## Lesson Preparation

If your module includes code learners may want to run, then give links to a pangeo binder here so they can start it up now. Also provide a link to the raw code so learners can download the code itself and run it on their own machines or copy it into a cloud server.

This module makes use of [pangeo binder](https://binder.pangeo.io/) for interactive code examples in R and python. You don't need to install anything or set up an account, but you need a modern web browser like Chrome and a moderately good wifi connection. If you have R and/or python already installed on your computer and you prefer to work through code examples there, you can <a href="https://raw.githubusercontent.com/arcus/education_modules/main/data_visualization_in_ggplot2/data_visualization_ggplot2.r" download>download the code for this module to run offline</a>.

If you intend to do the hands-on activities in this module with pangeo binder, we have a bit of preparation for you to do now. Because it can take a few minutes for the environment to be created, we suggest you click the link below to start up the activity. We recommend using right-click to open it in a new tab or window, and then returning here to continue learning while the environment finishes loading. Here is the link:

[![Link to start Binder environment](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/arcus/education_r_environment/main?urlpath=rstudio) **Click the "launch binder" button!**

You don't have to do anything except come back here once the link opens in a new tab or window.

## The `pandas` Package

When and why would `pandas` and programming in python be preferable to doing similar things in `R`?

What is this `import`, `as pd` and `import numpy as np`?

## `DataFrame`s

Tabular data! Tidy tabular data! Use `.head()` to see it!

Always indexed by `[row,column]`

## Filter specific rows and columns

Identify an entry with `loc` and `iloc`

## Creating new columns

### Logical and mathematical functions in Python

## Chaining Methods

## Additional Resources

The last section of the module content should be a list of additional resources, both ours and outside sources, including links to other modules that build on this content or are otherwise related.

The creators of the pandas package have [great tutorials](https://pandas.pydata.org/docs/getting_started/index.html) with very thorough examples.

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Transform+Data+with+Pandas%22)!

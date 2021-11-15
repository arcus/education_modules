<!--

author:   Joy Payton
email:    paytonk@chop.edu
version:  1.0.0
language: en
narrator: US English Female
title: Introduction to R and RStudio
comment:  Learn about the statistical programming language R and a very helpful tool for working with R called RStudio.
link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/modules.css

-->
# Introduction to R and RStudio

<div class = "overview">

## Overview

This module provides learners with an approachable introduction to the R language and the RStudio IDE, including hands-on practice appropriate for someone who has never used R or RStudio.

### Is this module right for me?

If you're interested in working with data (that could be many things, such as bringing data into your system, cleaning and reshaping data, making statistical discoveries, creating graphs and figures, or many other types of work) and you want to try using a programming language, R is a good place to start.   This will also be a good course for you if you are joining a team or project where R is used.

### Details

**Estimated time to completion**: 1 hour

**Pre-requisites**: It is helpful if learners have used data in a tabular (table-shaped) format, with rows and columns.  Examples of this kind of data include comma separated values files (.csv) and spreadsheets (for example, Microsoft Excel).  Learners do *not* need to have access to R or RStudio on their own computers.  

**Format**: This module uses text, still images, hands-on activities, and video.  Audio is optional.

**Learning Objectives**:  After completion of this module, learners will be able to:

* Describe what R is and what RStudio is
* Understand what a script is and how using a script can improve research
* Execute given R code within RStudio
* Explain what a data frame is
* Use the Environment tab within RStudio to examine a data frame

</div>

**Contents**
====

* [Lesson Preparation](#Lesson-Preparation)
* [What is R?](#What-is-R)
* [What is RStudio?](#What-is-RStudio)
* [Starting RStudio](#Starting-RStudio)
* [Using a File](#Using-a-File)
* [Why Use R and RStudio?](#Why-Use-R-and-RStudio)
* [RStudio Features](#rstudio-features)
* [Terminology](#Terminology)
* *Optional* [Additional Resources](#Additional-Resources)

  - [Hands-On Activities Demo](#Hands-On-Activities-Demo).  This is a video demo of the hands-on activities we've asked you to do in this module.  
  - [Researchers: Why R?](https://www.youtube.com/watch?v=Ids4FO5nTBE&t=07m19s) (section of interest is around 4 minutes).  This is a clip from a longer presentation given to learners at the Children's Hospital of Philadelphia.
* [Feedback](#Feedback)

## Lesson Preparation

*2 minute hands-on*

If you intend to do the hands on activity in this module, we have a bit of preparation for you to do now.

Because it can take a few minutes for the environment to be created, we suggest you click on the link that will start up the activity.

It will open in a new tab or window, and you can simply return here to continue learning, while the environment finishes loading.

Here's the link.  You don't have to do anything except come back here once the link opens in a new tab or window.

<a href = "https://binder.pangeo.io/v2/gh/arcus/education_r_environment/main?urlpath=rstudio" target = "_blank"><img src="https://binder.pangeo.io/badge_logo.svg"></a> **← Click the "launch binder" button!**

[Go back to the table of contents](#Contents)

## What is R?

*5 minute read*

R is a statistical programming language.  As a programming language, R requires that you write **code** that instructs a computer in what to do.  It's not point-and-click software like Excel or SPSS.

R code looks something like this (you can scroll over to see the long url in the second line of code):

```r
library(tidyverse)
breast_cancer_data <- read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00451/dataR2.csv")
hist(breast_cancer_data$Resistin)
summary(breast_cancer_data$HOMA)
```

Ideally, R code includes helpful hints along the way to help readers understand what's happening.  We can do that using **comments**, which are lines that the computer knows to ignore and not treat as code.

For example, the following may be a bit easier to understand, even if you are brand new to R.

<div class = "question" style = "min-height: 5rem;">
What distinguishes a comment from code in the sample below?</div>

```r
# tidyverse has helpful functions we'll use throughout the analysis

library(tidyverse)

# bring in the data from UCI.

breast_cancer_data <- read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00451/dataR2.csv")

# Create a histogram of resistin values

hist(breast_cancer_data$Resistin)

# Show quartiles / mean of HOMA values

summary(breast_cancer_data$HOMA)
```

You can write R code and execute it in many ways, including using the command line, the R console, and in a Jupyter notebook.  Here, however, we're going to concentrate on using RStudio.

[Go back to the table of contents](#Contents)

## What is RStudio?

*10 minute read*

RStudio is an **IDE**, or **Integrated Development Environment**, which pulls together (integrates) useful tools like help files, image viewers,  data previews, and version control for people writing (developing) code, and it puts all these tools together in a visually pleasing and helpful environment.  It's an add-on tool that makes working with R easier because it gives extra help and context.


<div class = "question">

Which of these correctly describes the relationship between R and RStudio?

[[ ]] R is a free, open source language used for data analysis, while RStudio is a related language that costs money but comes with a support agreement
[[X]] R is a free, open source language used for data analysis, and RStudio is software that makes R easier to use by adding tools and scaffolding
[[ ]] R is a mathematical and statistical system of notation, and RStudio is a free, open source language used for data analysis that uses R for statistics
[[ ]] R is a mathematical and statistical system of notation, and RStudio converts software like Stata or SPSS to use R as the underlying paradigm

<div class = "answer">
<details><summary>Click to see an explanation of the answer.</summary>

R is a language that was specifically designed for the statistical analysis of data.  It's free and open source, and while you can use it alone, it's much easier to use RStudio software to help you write R code more quickly.  RStudio also comes with additional bells and whistles that will help you create documentation of your data analysis and statistical thinking.
</details>
</div>
</div>

### Without RStudio

We could run the code above in a simple **R console**, which is what you get when you install R by itself without using RStudio.  This isn't the most user friendly experience! In the screen recording shown below, we are **not** using RStudio, but rather the R Console.

|![R.app, or the R Console](https://github.com/arcus/education_modules/blob/intro_to_r_rstudio/intro_to_r_rstudio/media/r_console.gif?raw=true)|
|--|

Above, you can see that the R console had to open a new program (in a Mac, it's the Quartz viewer) to display the histogram.  You can't tell much about the `breast_cancer_data` datset and you don't get tips and support around using R.  For example, here are some questions you may have after watching the animation above.

* What does my data look like?  How can I get a sneak peek?  
* How many rows are in the data?  
* How can I get more information on how to use the `hist` command?
* How can I save my work for later re-use and expansion?

Using the R.app or R console tool means very basic, bare-bones support for you as someone who is trying to write code.

### With RStudio

On the other hand, you could run the same code in RStudio and see something like this:

|![Running code in RStudio](https://github.com/arcus/education_modules/blob/intro_to_r_rstudio/intro_to_r_rstudio/media/rstudio.gif?raw=true)|
|--|

Using RStudio, you:

* Can easily create a script to save your code for reuse later (it's currently "Untitled1")
* Get a sneak peek at the data to help you to decide what to do next (here we have 116 rows of 10 columns)
* See the plot in the same window as everything else
* Can use other helpful tools, like
  - File browser
  - Help tab
  - History of commands you've run recently
  - Operating system terminal
  - And much more!  

RStudio is the preferred method for most uses of R, and it's generally what we use to teach.

[Go back to the table of contents](#Contents)

## Starting RStudio

*10 minutes hands-on*

You don't have to have R and RStudio installed on your local computer to learn how to use them.  We've provided a simple environment you can use.  It will probably take a few minutes to load up, especially if it's "cold" (hasn't been used by anyone lately).  

If you already clicked on the "launch binder" button as the first activity, you can simply open that tab on your browser.

Didn't click it before?  No worries! Click below and an RStudio environment will open in your browser window.  We suggest using Chrome for this.  

While you wait for RStudio to load, come back here and read a bit more.

<a href = "https://binder.pangeo.io/v2/gh/arcus/education_r_environment/main?urlpath=rstudio" target = "_blank"><img src="https://binder.pangeo.io/badge_logo.svg"></a> **← Click the "launch binder" button!**

<div class = "hint">

### While You're Waiting...

Do you wonder where you can install R and RStudio, and how much they'll cost?

R and RStudio are free, open source software (**FOSS**), and both can be installed in a number of different kinds of systems.

You can run R and RStudio:

* From your local computer (download a Windows, Mac, or linux version of R](https://cran.rstudio.com/) and [RStudio](https://www.rstudio.com/products/rstudio/download/#download))
* On a cloud service provider like [RStudio.cloud](https://rstudio.cloud)
* On a server that your workplace provides
* On a temporary environment someone prepares for you, like our Pangeo Binder environment

A to-do list for you to consider:

* Try installing [R](https://cran.rstudio.com/) and [RStudio](https://www.rstudio.com/products/rstudio/download/#download) to your computing device.
* Not ready to commit to downloading R and RStudio yet?  Create a free [RStudio.cloud](https://rstudio.cloud) account!
* Ask your colleagues who use R and RStudio where they do their work in R, and if there are any steps you need to take to get access (like request access to a server at your lab or workplace)
* [Cloud Tools for the Unconvinced](https://education.arcus.chop.edu/r-python-cloud/).  This brief article (2 minute read) introduces [RStudio.cloud](https://rstudio.cloud) and includes a link to a project you can look at, copy, and learn from.

</div>

### Still waiting?

While things are loading, you might see an image like this, and it might stay this way for a few minutes.  Be patient!  If you have a few friends to do this together with, it can help speed things up, since the environment will have been recently used and ready to deploy more quickly.

|![Pangeo Load Screen](https://github.com/arcus/education_modules/blob/intro_to_r_rstudio/intro_to_r_rstudio/media/pangeo.png?raw=true)|
|--|

### Finally Loaded!

Once your environment has loaded, you will be able to see something like the following:

![RStudio Environment](https://github.com/arcus/education_modules/blob/intro_to_r_rstudio/intro_to_r_rstudio/media/rstudio_pangeo.png?raw=true)

Take a look around.  What do you see?  How would you describe the layout of panes and tabs to another person?  What do you think the different parts do?

Try describing RStudio's appearance out loud to yourself.  This may seem silly but it is another way to consolidate your learning.

## Using a File

*10 minutes hands-on*

Before you are ready to write your own code, you might find it useful to work with an existing file.

There are several ways to write R code using RStudio.  We'll start with an R **script**.  An R script is a text file that includes all the R code and any comments that you want to save in a file so you don't lose track of a process.  For example, let's say that we know we'll want to work on some data stored in a .csv file, and it will take us several days or weeks to slowly write the code.  We can use an R script to store what we've figured out so far.

<div class = "hint">

Pro tip:  You'll recognize an R script because it ends in `.R`!</div>

In the lower right of your RStudio window, you should see a pane that has tabs marked "Files", "Plots", "Packages", "Help", and "Viewer".  Click on the "Files" tab, open the name of this course (`intro_to_r_rstudio`) and find the R script.  Remember that R scripts end with the file extension `.R`.

Did you find it?  It's called `intro_to_R.R`.  Click on the file name and it will open in a new "Source" pane which will appear as the upper left pane.  You should see something similar to the graphic below.

![RStudio source pane displays R script](https://github.com/arcus/education_modules/blob/intro_to_r_rstudio/intro_to_r_rstudio/media/source_pane.png?raw=true)

### Running Code in RStudio

Use your mouse to add a cursor (be careful not to highlight text) somewhere in lines 1-8.  These lines make up our first comments.  Then, click "Run" in the upper right corner of the Source pane:

![Running code in the Source pane using the Run button](https://github.com/arcus/education_modules/blob/intro_to_r_rstudio/intro_to_r_rstudio/media/rstudio_run.gif?raw=true)

What do you see now in the Console (the bottom left pane)?  Remember that comments are ignored by R, so the first line of actual R code that could be run was line 10.  That's what ends up running (or executing) in the console!

Click to move the cursor to a point in line 15 and click the "Run" button again.  

![Running code in the Source pane using the Run button](https://github.com/arcus/education_modules/blob/intro_to_r_rstudio/intro_to_r_rstudio/media/rstudio_run_line_15.gif?raw=true)

It may take a while to execute, and you might see a red "Stop Sign" emblem appear in the upper right of your console pane.  When you see the stop sign, you know that something is still running and you have the option of stopping it (but don't, this time).

### Data Frames

By running line 15, you have instructed the computer to read in a csv using `read_csv` and to add that data to a new **data frame** object, which will be called `breast_cancer_data`.  

Data frames consist of data arranged into rows and columns, like a spreadsheet.  Each row is an observation (in our case, a patient) and each column is a measurement (like age and insulin values).

The new object, `breast_cancer_data`, appears in your "Environment" tab in the upper right pane.  You can click on the small blue icon beside the name of the object to see the structure of the data frame (column names and data types stored in the columns).

You can also click on the name of the object to open a view of the data in the Source pane.  Or, in your R code, you can do the same thing using the `View` command.

### On your own

Now run the next few lines of code.  You can:

* Run them one by one, using the Run button, or
* Use a keyboard shortcut (command or control + the enter key) to run code one line at a time, or
* Highlight several complete lines of code (don't start in the middle of a line!) and click the Run button to run all of them.

It won't hurt to run these lines several times, so try various methods!

What does the `hist` command accomplish?  The `summary` command? `View`?  

## Why Use R and RStudio?

*5 minutes*

Fine, you now know a bit more about R and RStudio, but why does this matter?  You may already know how to conduct statistical data analysis in tools like SPSS, Excel, or other software.  Why, then, learn R?  Is R only for professional data scientists?

R and RStudio are great tools for professional data scientists, but they are also increasingly part of the research tool kit, much like other lab equipment that researchers have to learn to use.  This is because the **reproducibility crisis** of studies that cannot be reproduced or fail to reproduce can be ameliorated in part by the use of scripted data analysis.

R and other free, open source, and scripted (code-based) methods of data analysis are widely considered more reproducible because:

* Anyone can obtain the software needed to use R scripts, with no license cost.
* Operations you perform to data are recorded in a script, which means they are not lost to history in the same way you might forget to precisely record a step you took in, say, Excel.
* Scripted languages can do multiple stages of data analysis in a single tool, such as downloading data, cleaning and reshaping data, performing statistical tests, displaying data visualizations, and more.  

There are many reasons why the research community is pivoting to languages like R.  While learning a new technical skill can be time consuming, working with R will pay off in the long run, because it makes it easier for you to re-run your analyses, describe your methods precisely, share your work with colleagues, and meet the requirements of funders and publications when it comes to reproducible research.

Want to hear more?  Watch around 4 minutes of one of our optional additional resources:

- [Researchers: Why R?](https://www.youtube.com/watch?v=Ids4FO5nTBE&t=07m19s) (section of interest is around 4 minutes).  This is a clip from a longer presentation given to learners at the Children's Hospital of Philadelphia.

## RStudio Features

*5 minute hands-on*

We're only going to touch on three of many useful tools here.  When time permits, you may want to explore more.  In the meantime, however, let's consider what we've learned so far about R scripts:


<div class = "question">

Which of the following are accurate descriptions of R scripts?  Check all that apply!

[[X]] R scripts allow you to capture each step you do in data ingestion, data cleaning and preparation, and statistical analysis.
[[X]] R scripts make it easier for you to re-run your analysis if more data comes in or you need to check your work.
[[ ]] R scripts allow you to avoid writing code entirely and just describe what you want to happen in regular English.  The translator engine of R converts your instructions into code.
[[X]] R scripts usually open in the upper left pane of RStudio unless you decide to rearrange the panes.
[[ ]] R scripts can only contain code, never any extra helper text that contextualize or explain the code for humans.
[[ ]] R scripts can only be created in the R app or in command line, not in RStudio.
[[?]] Hint: Three of these things are accurate descriptions!


<div class = "answer">
<details><summary>Click to see an explanation of the answer.</summary>

R scripts do in fact allow you to record not only the concrete steps you do, but also allow you to include comments that give human-readable explanations of what you're doing.  This makes it much easier for you to re-run your analysis or share your methods with others.

You do still have to learn how to write code, because there's no "magic wand" just yet that will allow you do describe what you want in English and have software translate that into R code.

R scripts work great in the RStudio software and generally will appear (once opened) in the upper left pane of RStudio.   
</details>
</div>
</div>


### Help

Within RStudio, click on the "Help" tab in the lower right pane.  Choose one promising help topic to click on.  It appears as a new tab or window in your browser.

![Search boxes in RStudio Help tab](https://github.com/arcus/education_modules/blob/intro_to_r_rstudio/intro_to_r_rstudio/media//search_boxes_rstudio.png?raw=true)

There are two search boxes related to help.  The one on the left, just above the help text, includes the phrase "Find in Topic".  This is for searching within the help article you're looking at currently.

The other search box is in the upper right part of the pane and can be used for searching across all available help.  For example, search for "hist" in this search box.  

### History

Within RStudio, click on the "History" tab in the upper right pane.  The commands that have been executed during your current session are listed.

Choose one of the commands by clicking on it, and choose the "To Console" button.  The code should now appear in the console in the lower left pane, ready for you to hit enter and run that command anew.

![History Tab](https://github.com/arcus/education_modules/blob/intro_to_r_rstudio/intro_to_r_rstudio/media/history_rstudio.png?raw=true)

### Display

Use the "Tools" menu at the top of RStudio, choose "Global Options", then  "Appearance".

Experiment with editor settings (font size and theme), and if you want to try it out, choose "Apply".

## Terminology

*5 minute read*

* code: computer instructions written with specific syntax rules: `summary(patients$age)`
* comment: text within a script that is intended for humans and will not be run by the computer: `# print summary stats here`
* data frame: data that is organized into rows (observations) and columns (measures / fields)
* FOSS (Free, Open Source Software): software that can be used free of charge and has very open intellectual property policies
* IDE (Integrated Development Environment): software that helps people who write code to do so more easily
* R: a statistical programming language
* R Console: a bare-bones desktop interface for the R language that comes when you install the R language software
* Reproducibility crisis: the problem in peer-reviewed research in which studies *cannot* be reproduced or replicated because of insufficient information, or in which studies *fail* to be reproduced or replicated because of problems in the initial research
* RStudio: a fully featured IDE that helps R users write and work with R code more easily
* script: code and comments saved in a file, useful for saving one's work

## Additional Resources

*10 minutes watch, optional*

- [Hands-On Activities Demo](#Hands-On-Activities-Demo).  This is a video demo of the hands-on activities we've asked you to do in this module.
- [Researchers: Why R?](https://www.youtube.com/watch?v=Ids4FO5nTBE&t=07m19s) (stop after this section, around 4 minutes long).  This is a clip from a longer presentation given to learners at the Children's Hospital of Philadelphia.

### Hands-On Activities Demo

<iframe width="560" height="315" src="https://www.youtube.com/embed/O8rKGHXSXlc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Researchers: Why R?

You can stop this video after around 4 minutes.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ids4FO5nTBE?start=439" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Feedback

*5 minute feedback*

In the beginning, we stated some goals.

**Learning Objectives**:  After completion of this module, learners will be able to:

* Describe what R is and what RStudio is
* Understand what a script is and how using a script can improve research
* Execute given R code within RStudio
* Explain what a data frame is
* Use the Environment tab within RStudio to examine a data frame

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Intro+to+R+and+RStudio%22)!

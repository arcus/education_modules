<!--

author:   Rose Hartman
email:    hartmanr1@chop.edu
version:  0.0.1
language: en
narrator: UK English Female
title: Data visualizations in seaborn

comment:  This module includes code and explanations for several popular data visualizations, using python's seaborn package. It also includes examples of how to modify seaborn plots to customize them for different uses (e.g. adhering to journal requirements for visualizations).  

-->

# Overview

Include text here describing the point of the module. 

Estimated time to completion:
----

Pre-requisites
----

This module assumes some familiarity with principles of data visualizations as applied in the seaborn library. If you've used seaborn (or R's ggplot2) a little already and are just looking to extend your skills, this module should be right for you. If you are brand new to ggplot2 and seaborn, start with the overview of [data visualizations in open source software](link) first, and then come back here. 

This module also assumes some basic familiarity with python, including 

* [installing and importing libraries](link)
* [reading in data](link)
* manipulating data frames, including [calculating new columns](link), and [pivoting from wide format to long](link)
* some [statistical tests](link)

If you are brand new to python (or want a refresher) consider starting with [Intro to python](link) first. 

Learning Objectives
----

After completion of this module, learners will be able to:

* identify key elements 
* do a task
* articulate the rationale for something

# Module Content

Note that liascript will create a new page at each level 1, 2, or 3 header, so to avoid a page with only a header and no content, include text after each header before the next. Text after level 1 headers provides a good opportunity to give a sentence or two of overview, explain the structure of the coming content, and/or get preliminaries out of the way. You can provide visual structure to your content without starting a new page by using `===` or `---` to define subsequent header levels (note that these won't show up in the table of contents, though!), as for the sub-sections in the [Overview](#overview). 

## Lesson Preparation

If your module includes code learners may want to run, then give links to a pangeo binder here so they can start it up now. Also provide a link to the raw code so learners can download the code itself and run it on their own machines, or copy it into a cloud server, whatever they want. 

This module makes use of [pangeo binder](https://binder.pangeo.io/) for interactive code examples in R and python. You don't need to install anything or set up an account, but you need a modern web browser like Chrome and a moderately good wifi connection. If you have R and/or python already installed on your computer and you prefer to work through code examples there, you can [download all the code for this module to run offline](https://github.com/arcus/r25_data_visualization_in_open_source_tools). 

If you intend to do the hands-on activities in this module with pangeo binder, we have a bit of preparation for you to do now. Because it can take a few minutes for the environment to be created, we suggest you click one of the links below (for either R or python) to start up the activity. It will open in a new tab or window, and you can simply return here to continue learning, while the environment finishes loading. Here are the links: 

[![Link to start Binder environment](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/arcus/education_r_intensive/main?urlpath=rstudio) **Click the "launch binder" button!**

You don't have to do anything except come back here once the link opens in a new tab or window.

## Section 1


![A valueable image, and this will be its caption](https://upload.wikimedia.org/wikipedia/commons/0/0f/Grosser_Panda.JPG)


You can link to images online with their url, or locally with the file path, e.g. `![image caption](img/my_image.png)`

If you want to provide several images in a gallery, just make a "paragraph" of image links and LiaScript will render it as a gallery:

![img1](https://upload.wikimedia.org/wikipedia/commons/6/68/Ailuropoda_melanoleuca_%28Panda_g%C3%A9ant%29_-_445.jpg) ![img2](https://upload.wikimedia.org/wikipedia/commons/2/2d/Panda_giganti_al_Giant_Panda_Breeding_Research_Base_Chengdu.jpg) ![img3](https://upload.wikimedia.org/wikipedia/commons/1/12/BabyPandaAtSDZ.jpg)

More text

> Include special notes with different formatting. 

I want to include a math statement here: $ 1 + \beta = 2 $

!?[This video is hosted on youtube](https://www.youtube.com/watch?v=iIAO4Htzn8M)

You can also embed local videos, just as with images: `!?[An embedded video, and this will be its alt text](vid/intro.mp4)`

In theory, you should be able to embed just about anything. Read more [here](https://liascript.github.io/course/?https://raw.githubusercontent.com/LiaScript/docs/master/README.md#24)

You can also include movies, audio, and any other embedded content in galleries just by putting the links for them all in a paragraph.

Next comes some code. This code won't do anything (it's not interactive).

```r
# You only need to install it once
install.packages("ggplot2")

# You'll need to load the library anew for each R session
library("ggplot2")
```
You don't have to specify the programming language, but you can, and it should help you get appropriate syntax highlighting.  

```python
print("This is python code")
```

It is possible to include interactive code, too! See [the Rextester template for LiaScript](https://github.com/LiaTemplates/Rextester).

## Quiz 1

Quizzes are just more markdown text, so if you want it to show up on its own page, put a new header before it. Otherwise you can include quiz questions at the end of a section, or even interspersed with the rest of your content. 

Quizzes should connect directly to your learning objectives. Each quiz question should connect to one learning objective, and every learning objective should have at least one quiz question associated with it somewhere in the module. 

Here is the first question. It's multiple choice.

[(X)] This answer is right
[( )] This is wrong
[( )] Also wrong
[[?]] Hint: Provide a hint here if you like. Hints are marked with the ?
[[?]] Hint: You can include as many hints as you want. 

You can have questions with multiple correct answers. Select all of the following correct choices:

[[ ]] Not this one
[[X]] This is one of the correct ones
[[X]] Here's another correct one
[[ ]] This one is wrong, though
[[?]] Hint: Remember to select ALL of the correct choices. 

True or False: This statement is NOT true. ;)

[( )] TRUE
[(X)] FALSE

Short answer/text response. Note that, without any additional script, to get it marked "correct" the learner has to enter it exactly as you do. 

[[right answer]]
[[?]] Hint: Provide a hint here if you like. 
    ***********************************************************************

This is extra text that will show up after the learner clicks to have the correct answer revealed. 
It can be as long as you like, and allows any markdown formatting (you can embed pictures or videos, links, etc.). 

    ***********************************************************************

We can allow some flexibility in what we accept as correct answers for text by adding a little script after the answer, though. For the following, either "right answer" or "correct answer" (not case sensitive) will be accepted: 

[[right answer]]
<script>
  let input = "@input".trim().toLowerCase();
  input == "right answer" || input == "correct answer";
</script>
    ***********************************************************************

For this question, either "right answer" or "correct answer" (not case sensitive) counts as correct. 

    ***********************************************************************

There are also questions that allow you to select from a drop down, but I don't know why that would be preferable over regular multiple choice. [Read more about quiz syntax here.](https://liascript.github.io/course/?https://raw.githubusercontent.com/andre-dietrich/e-Learning-2019/master/README.md#10)

Note that you can use any markdown formatting you want in quizzes, including bold, links, math, etc. 

## Additional Resources

The last section of the module content should be a list of additional resources, both ours and outside sources, including links to other modules that build on this content or are otherwise related. 

# Feedback

The last section in the module is for feedback. Restate the learning objectives here and then provide a link to the feedback survey, like this:

In the beginning, we stated some goals.

Learning Objectives:  
---

After completion of this module, learners will be able to:

* identify key elements 
* do a task
* articulate the rationale for something

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Intro+to+R+and+RStudio%22)!

Remember to change the redcap link so that the module name is correct for this module!

<!--

author:   Your Name
email:    email@chop.edu
external_resources:
  resource1: First External Resource
  resource2: Second External Resource
version:  0.0.0
wrapper_template_version: 1.0.0
language: en
narrator: UK English Female
title: Module Title
comment:  This is a short, focused description of the module.
long_description: This is a longer description, which should be understandable for a lay audience. It will print under "Is this module right for me?" in the overview.
estimated_time: This is rough guess of how long it might take a learner to work through the module. It will print under "Estimated time to completion" in the overview

@learning_objectives  

After completion of this module, learners will be able to:

- identify key elements
- create a product
- do a task
- articulate the rationale for something

For help articulating learning objectives, see [this guide to learning objectives, including lots of example verbs](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/).

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

This template should be used when a module is more than 50% content that is embedded or linked to.
If more than half of the module content is in the LiaScript markdown itself, then the other template should be used, even if that content is primarily adapted from a single CC source.

To see how to use this template, you'll need to look at this file in its [raw format](https://raw.githubusercontent.com/arcus/education_r25/main/working_documentation/template_modules.md?token=ACEVZUTXZ6BTRFIIBXPN4SDBD3FR6).
To see what it looks like rendered via LiaScript, [click here](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_r25/main/working_documentation/template_modules.md?token=ACEVZUTXZ6BTRFIIBXPN4SDBD3FR6#1) or go to [https://liascript.github.io/](https://liascript.github.io/) and paste the link to the **raw** file into the box on that page and click "load course".

# Title
Note that the title is the only level-1 header in the document

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

This module will direct you to external educational content.
---

Many topics have great content written by others! We chose this content for you based on how well it meets our criteria.

Not all selected materials will meet all of these criteria, but selected materials should meet as many as possible.
Write a short sentence about how this material meets, or does not meet, each criterion.

**Resource 1 Name**

Short optional summary sentence about resource 1.

<ul style="list-style-type: none">
   <li><i class="fa-solid fa-circle-check" style="color: #158d0c;" title="Checked"></i> Expert Authors / Well-Vetted: _who are the expert authors? or what institutional authority guarantees accuracy?_</li>
   <li><i class="fa-solid fa-circle-minus" style="color: #f0bc00;" title="Unchecked"></i> Maintained: _who is in charge of implementing regular updates to this material, important in fast-changing fields._</li>
   <li><i class="fa-solid fa-circle-check" style="color: #158d0c;" title="Checked"></i> Stable Support: _who hosts this material so it won't disappear? If it does, please let us know in a feedback form ASAP!_</li>
   <li><i class="fa-solid fa-circle-minus" style="color: #f0bc00;" title="Unchecked"></i> Accessibility: _Does this meet our high standards for accessibility? What do we know it lacks?_</li>
</ul>

**Resource 2 Name**

Short optional summary sentence about resource 2.

<ul style="list-style-type: none">
   <li><i class="fa-solid fa-circle-check" style="color: #158d0c;" title="Checked"></i> Expert Authors / Well-Vetted: _who are the expert authors? or what institutional authority guarantees accuracy?_</li>
   <li><i class="fa-solid fa-circle-minus" style="color: #f0bc00;" title="Unchecked"></i> Maintained: _who is in charge of implementing regular updates to this material, important in fast-changing fields._</li>
   <li><i class="fa-solid fa-circle-check" style="color: #158d0c;" title="Checked"></i> Stable Support: _who hosts this material so it won't disappear? If it does, please let us know in a feedback form ASAP!_</li>
   <li><i class="fa-solid fa-circle-minus" style="color: #f0bc00;" title="Unchecked"></i> Accessibility: _Does this meet our high standards for accessibility? What do we know it lacks?_</li>
</ul>

The structure of this module:
---
Give learners a short, concrete, description of what they will do. This might look like:

Example Structure 1:

1. Read about how this topic fits into some bigger picture here in this LiaScript course.
2. Do the activities embedded in this module (using iFrames).
3. Answer a few questions to make sure you understood the key parts.

Example Structure 2:

1. Open this external resource in a new browser window.
2. Read Chapter 1 and do the activities at the end.
3. Return to this LiaScript course to answer a few questions to make sure you understood the key parts.

Example Structure 3:

1. Open this external resource in a new browser window.
2. Read Section 2.1 and 2.2.
3. Return to this LiaScript course to do an activity.
4. Answer a few questions (again in the LiaScript course) to make sure you understood the key parts.
These are just some examples of possible structures. The specific structure will depend greatly on the particular external module/educational resource you are using.


## Module Content

Note that liascript will create a new page at each level 1, 2, or 3 header, so to avoid a page with only a header and no content, include text after each header before the next.

Text after level 2 headers provides a good opportunity to give a sentence or two of overview, explain the structure of the coming content, and/or get preliminaries out of the way.

## Including Media


![A valuable image, and this is its alt text.](https://upload.wikimedia.org/wikipedia/commons/0/0f/Grosser_Panda.JPG "Here is a subtitle that will display beneath the image.")


You can link to images online with their url, or locally with the file path, e.g. `![image caption](media/my_image.png)`

If you want to provide several images in a gallery, just make a "paragraph" of image links and LiaScript will render it as a gallery:

![img1 alt text.](https://upload.wikimedia.org/wikipedia/commons/6/68/Ailuropoda_melanoleuca_%28Panda_g%C3%A9ant%29_-_445.jpg) ![img2 alt text.](https://upload.wikimedia.org/wikipedia/commons/2/2d/Panda_giganti_al_Giant_Panda_Breeding_Research_Base_Chengdu.jpg) ![img3 alt text.](https://upload.wikimedia.org/wikipedia/commons/1/12/BabyPandaAtSDZ.jpg)


!?[This video is hosted on youtube.](https://www.youtube.com/watch?v=iIAO4Htzn8M)

You can also embed local videos, just as with images: `!?[An embedded video.](vid/intro.mp4 "This is its subtitle")`

In theory, you should be able to embed just about anything. Read more [here](https://liascript.github.io/course/?https://raw.githubusercontent.com/LiaScript/docs/master/README.md#24).

You can also include movies, audio, and any other embedded content in galleries just by putting the links for them all in a paragraph.

## Including highlight boxes

Include special notes with different formatting.

Note: There's an additional style of highlight not listed here, "answer", that is used in [quizzes](#quiz-quizzes).


### behind-the-scenes

The style "behind-the-scenes" is for giving a little more technical detail about how something does what it does.
It has a gears icon and always begins with the text "Behind the scenes".
For example:

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

The commit number is a hash and associated details

</div>

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

In R the `<-` and `=` can both be used for assignment because...

</div>

### care

The style "care" is for content related to compassion, self-care, and motivation. For more technical help or troubleshooting, use "help" instead.
It has a hand-holding-heart icon and always begins with the text "A little encouragement..."
For example:

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

This is a topic with a tremendous amount of jargon, which can make resources you may find online hard to understand for folks new to the field. When that happens it's easy to feel like there's something wrong with you if you don't get it, but that's not the case! Those kinds of gatekeeping explanations are a failure on the part of the writer, not the learner.

</div>

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Feeling overwhelmed? It takes a long time to learn git, so don't be disheartened if it doesn't click initially. Just focus on stage, commit, and push. Ignore the rest for now, until you've had a chance to practice just the stage-commit-push process several times.

</div>

### cool-fact

The style "cool-fact" is for any cool fact that really doesn't fit into any of our other categories.
It has a brain icon and always begins with the text "Did you know?"
For example:

<div class = "cool-fact">
<b style="color: rgb(var(--color-highlight));">Did you know?</b><br>

Functions like this are sometimes called "syntactic sugar" because they don't change anything about how the code runs, they just make it easier for humans to read, the way that sugar makes food sweeter without adding any nutrition.

</div>


<div class = "cool-fact">
<b style="color: rgb(var(--color-highlight));">Did you know?</b><br>

This is a box showing how images work in a highlight box.

![Carebear team.](https://media.giphy.com/media/W256ghnG9iV8I/giphy.gif)


</div>


### help

The style "help" is for troubleshooting help, common errors, and specific technical problems. If you want to emphasize a very serious potential problem, use "warning" instead. For support that is more psycho/emotional or meta-learning in nature, use "care" instead.
It has a circle-question icon and always begins with the text "Troubleshooting help".
For example:

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

A common mistake when using `filter` is to write = when you mean ==. Remember that = is for argument assignment, and == is for testing equality in conditions. If you get them mixed up, your code won't run!

</div>

### history

The style "history" is for more historical context about how/when/why something came to be the way it currently is.
It has a clock-rotate-left icon and always begins with the text "Historical context".
For example:

<div class = "history">
<b style="color: rgb(var(--color-highlight));">Historical context</b><br>

The reason this command is named grep is...

</div>

<div class = "history">
<b style="color: rgb(var(--color-highlight));">Historical context</b><br>

The first README file was from 1971, etc.

</div>


### important

The style "important" is for important points and key ideas.
It has a star icon and always begins with the text "Important note".
For example:

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

It's generally much easier to make any necessary changes to the dataframe, such as mutating variables, before sending it to the plotting command.

</div>

### learn-more

The style "learn-more" alerts users resources for further learning, especially links to a more in-depth discussion of an issue that might be touched on only briefly in the module. It can link to outside sources, or other modules by us.
It has a book icon and always begins with the text "Learning connection".
For example:

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To learn more about the theory behind ggplot2, read [Hadley Wickham's article, "A Layered Grammar of Graphics"](http://vita.had.co.nz/papers/layered-grammar.pdf).

</div>


<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To do this in R instead of python, see [this other module](example.com).

</div>


### options

The style "options" is for an aside to let learners know there's another possible approach. This is for short explanations rather than linked resources; to link to another approach (e.g. here's a tutorial for another way to do this), use "learn-more" instead.
It has a left-right arrow icon and always begins with the text "Another option".
For example:

<div class = "options">
<b style="color: rgb(var(--color-highlight));">Another option</b><br>

You could also skip setting up an OSF account completely and just use github to publish and share your research products, but many people prefer to have OSF links available.

</div>

<div class = "options">
<b style="color: rgb(var(--color-highlight));">Another option</b><br>

You can run this in the cloud or download all of the files locally and run it on your computer. If you run it on your computer, be sure to make note of which directory you save the files in and update your working directory accordingly.

</div>

### warning

The style "warning" alerts users to potential pitfalls, and should be reserved for serious problems only. For less serious problems, use "help" instead.
It has a ! triangle icon and always begins with the text "Warning!".
For example:

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

Double check your working directory before running this code. If you're in the wrong directory, you risk overwriting your files and losing all of your work with no way to recover it.

</div>

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

Files uploaded to this account will be **publicly visible**. Be very careful not to upload anything with sensitive information like passwords or private data.

</div>

## Including math

I want to include a math statement here: $ 1 + \beta = 2 $

## Including code

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

## Quiz: Quizzes

Quizzes are just more markdown text, so if you want it to show up on its own page, put a new header before it. Otherwise you can include quiz questions at the end of a section, or even interspersed with the rest of your content.

Quizzes should connect directly to your learning objectives. Each quiz question should connect to one learning objective, and every learning objective should have at least one quiz question associated with it somewhere in the module.

Quizzes should always be navigable from the sidebar, meaning they should be labeled with a level 2 or 3 header. If there is only one quiz in the module, it should be labelled as "Quiz". If there is more than one each header should be structured as "Quiz: label" where "label" is a short (ideally 1-2 words) description of the content covered in the question(s). E.g., "Quiz: Scatterplots"

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
[[?]] Hint: The answer is "right answer"
***
<div class = "answer">

This is extra text that will show up after the learner clicks to have the correct answer revealed. It can be as long as you like, and allows any markdown formatting (you can embed pictures or videos, links, etc.).

Use `<div class = "answer">` to mark these sections with special styling, so that they're visually distinct from the rest of the quiz. The style for `"answer"` is defined in the css file.

For this context to show up automatically when the learner answers the question correctly or clicks to have the right answer revealed, it needs to be surrounded by `***` (at least three, but you can use more if you want a more visually distinct horizontal marker in your md file).

</div>
***

We can allow some flexibility in what we accept as correct answers for text by adding a little script after the answer, though. For the following, either "right answer" or "correct answer" (not case sensitive) will be accepted:

[[right answer]]
<script>
  let input = "@input".trim().toLowerCase();
  input == "right answer" || input == "correct answer";
</script>
***
<div class = "answer">

For this question, either "right answer" or "correct answer" (not case sensitive) counts as correct.

</div>
***

This question accepts any of several items from a list of possible correct answers. It is not case sensitive (that's the little `i` at the end of the regex).

[[this text will never show up if they type a right answer and click "Check", only if they click the checkmark button to reveal the answer]]
[[?]] Hint: The answers are like "item1", "item2", etc.
<script>
  let input = "@input".trim();
  /item1|item2|item3|item4/i.test(input);
</script>
***
<div class = "answer">

With flexible answers like this, it's definitely a good idea to include a follow-up to help the learner put their answer in context.

For example, if the question was "Name one or more colors" with acceptable answers including red, orange, yellow, green, blue, and purple, and they wrote "red, green, and the center of a black hole" that would be marked as correct because it contains at least one string from the acceptable list. Similarly, "hammered metal" would be marked as correct because it contains the string "red" ([you can prevent this if you want](https://www.w3schools.com/jsref/jsref_regexp_begin.asp)). On the other hand "teal, scarlet, indigo" would be marked wrong.

Reiterate what the correct answer or answers should be, and try to anticipate likely wrong answers so you can explain why they're not correct.

</div>
***

There are also questions that allow you to select from a drop down, but I don't know why that would be preferable over regular multiple choice. [Read more about quiz syntax here.](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md#quizzes)

Note that you can use any markdown formatting you want in quizzes, including bold, links, math, etc.

Surveys (ungraded questions)
---

You can ask questions with no graded answer as well. LiaScript calls these [surveys](https://liascript.github.io/course/?https://raw.githubusercontent.com/LiaScript/docs/master/README.md#111).

Here's an ungraded question with a text box three lines long:

[[___ ___ ___]]

Here's one that's just one line long:

[[___]]

Here's a multiple choice with no correct answer. What is your favorite Beatles album?

[(rev)] Revolver
[(wa)] The While Album
[(ar)] Abbey Road
[(sgtp)] Sgt. Pepper's Lonely Hearts Club Band

Here's a survey multiple choice that lets you select more than one response. Which Beatles albums do you love super hard?

[[rev]] Revolver
[[wa]] The While Album
[[ar]] Abbey Road
[[sgtp]] Sgt. Pepper's Lonely Hearts Club Band

Hints and follow-up explanations don't work for survey questions.


## Additional Resources
The last section of the module content should be a list of additional resources, both ours and outside sources, including links to other modules that build on this content or are otherwise related.

To learn more about one topic, check out these great things:

- [one thing](https://education.arcus.chop.edu)
- [another thing](https://education.arcus.chop.edu)

For more background on something else, try [a different thing](https://education.arcus.chop.edu).

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Module+Template%22)! <!-- Remember to change the redcap link so that the module name is correct for this module!

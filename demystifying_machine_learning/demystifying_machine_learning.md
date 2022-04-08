<!--

author:   Rose Hartman
email:    hartmanr1@chop.edu
version:  0.0.1
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Demystifying Machine Learning
comment:  This is a short, focused description of the module.
long_description: This is a longer description, which should be understandable for a lay audience. It will print under "Is this module right for me?" in the overview.
estimated_time: This is rough guess of how long it might take a learner to work through the module. It will print under "Estimated time to completion" in the overview

@learning_objectives  

After completion of this module, learners will be able to:

- list three potential applications of machine learning in biomedical science
- describe three different statistical problems models can address and how they differ (e.g. prediction, anomoly detection, clustering, dimension reduction)
- explain the bias-variance tradeoff
- describe how biases inherent in the data can affect model outcomes and perpetuate inequalities

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Demystifying Machine Learning

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

## Machine learning and its uses

### Potential applications in biomedical science

- [predict which tests a patient entering the emergency department might need](https://healthitanalytics.com/news/machine-learning-model-helped-streamline-22-of-pediatric-ed-visits) so they can be ordered automatically and care delivered more quickly
- [more accurately estimate severity of osteoarthritis from knee X-ray images](https://www.nature.com/articles/s41591-020-01192-7), reducing unexplained racial disparities in pain that occur when images are graded by human physicians
- [assess the feasibility of allocating Medicare funds based on predicted mortality](http://ziadobermeyer.com/wp-content/uploads/2019/09/eolspend.pdf), addressing the question of whether Medicare spending during what turns out to be the last year of life is wasteful from a policy perspective
- [automatic extraction of things like symptoms and history from unstructured notes](https://arxiv.org/pdf/2107.02975.pdf)


### Quiz: Machine learning and its uses

Which of the following would be examples of machine learning? Select all that apply.

[[X]] Using ultrasound images, automatically flag potentially high-risk patient files for closer inspection by a clinician
[[ ]] Estimate the difference 
[[X]] Based on a large sample of electronic health records, build a model to give the probability that a given patient will be readmitted within a week of hospital discharge
[[ ]] 
****
<div class = "answer">
</div>
****


## Different questions need different kinds of models

### Prediction

### Anomoly detection

### Clustering

### Dimension reduction

### Quiz: Machine learning models

## Big data does not mean good data: Bias and inequality

Although there are unfortunately many examples of explicit bias in data intentionally used to maintain inequalities (e.g. [the Home Owners Loan Corporation assessments during the New Deal era](https://dsl.richmond.edu/panorama/redlining/#loc=4/41.212/-109.995&text=intro)), 

[racial disparities in the distribution of COVID-19 reflief funding](https://www.statnews.com/2020/08/07/racial-bias-in-government-covid19-hospital-aid-formula/)

<div class = "learnmore">
To learn more about one particularly salient example of this problem, read ["Dissecting racial bias in an algorithm used to manage the health of populations"](https://www.science.org/doi/full/10.1126/science.aax2342). From the abstract:

> The U.S. health care system uses commercial algorithms to guide health decisions. Obermeyer et al. find evidence of racial bias in one widely used algorithm, such that Black patients assigned the same level of risk by the algorithm are sicker than White patients (see the Perspective by Benjamin). The authors estimated that this racial bias reduces the number of Black patients identified for extra care by more than half.

</div>

### Quiz: Bias and inequality

True or False: Big data sets are generally higher quality than smaller data sets

[( )] TRUE
[(X)] FALSE
****
<div class = "answer">
</div>
****



## Including highlight boxes

Include special notes with different formatting. The style "important" is for important points and key ideas. For example:

<div class = "important">
Tip: It's generally much easier to make any necessary changes to the dataframe, such as mutating variables, before sending it to the plotting command.
</div>

The style "care" is for content related to compassion, self-care, and motivation. For example:

<div class = "care">
This is a topic with a tremendous amount of jargon, which can make resources you may find online hard to understand for folks new to the field. When that happens it's easy to feel like there's something wrong with you if you don't get it, but that's not the case! Those kinds of gatekeeping explanations are a failure on the part of the writer, not the learner.
</div>


The style "help" is for educational first aid --- "help I'm lost!" suggestions. For example:

<div class = "help">
Feeling overwhelmed? It takes a long time to learn git, so don't be disheartened if it doesn't click initially. Just focus on stage, commit, and push. Ignore the rest for now, until you've had a chance to practice just the stage-commit-push process several times.
</div>

The style "warning" alerts users to potential pitfalls. For example:

<div class = "warning">
A common mistake when using `filter` is to write = when you mean ==. Remember that = is for argument assignment, and == is for testing equality in conditions. If you get them mixed up, your code won't run!
</div>

The style "learnmore" alerts users resources for further learning, especially links to a more in-depth discussion of an issue that might be touched on only briefly in the module.

<div class = "learnmore">
To learn more about the theory behind ggplot2, read [Hadley Wickham's article, "A Layered Grammar of Graphics"](http://vita.had.co.nz/papers/layered-grammar.pdf)
</div>

The style "options" is for an aside to let learners know there's another possible approach. For example:

<div class = "options">
You could also skip setting up an OSF account completely and just use github to publish and share your research products, but many people prefer to have OSF links available.
</div>
or
<div class = "options">
To do this in R instead of python, see this other module.
</div>

There's an additional style of highlight, "answer", that is used in [quizzes](#quiz).

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

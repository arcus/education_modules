<!--

author:   Rose Hartman
email:    hartmanr1@chop.edu
version:  0.0.1
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Data Types in R
comment:  This is a short, focused description of the module.
long_description: This is a longer description, which should be understandable for a lay audience. It will print under "Is this module right for me?" in the overview.
estimated_time: This is rough guess of how long it might take a learner to work through the module. It will print under "Estimated time to completion" in the overview

@learning_objectives  

After completion of this module, learners will be able to:

- identify key elements
- create a product
- do a task
- articulate the rationale for something

@end

script:  https://code.jquery.com/jquery-3.6.0.slim.min.js

@gifPreload
<script>
(function($) {

  // Get the .gif images from the "data-alt".
	var getGif = function() {
		var gif = [];
		$('img').each(function() {
			var data = $(this).data('alt');
			gif.push(data);
		});
		return gif;
	}

	var gif = getGif();

	// Preload all the gif images.
	var image = [];

	$.each(gif, function(index) {
		image[index]     = new Image();
		image[index].src = gif[index];
	});

	// Change the image to .gif when clicked and vice versa.
	$('figure').on('click', function() {

		var $this   = $(this),
				$index  = $this.index(),

				$img    = $this.children('img'),
				$imgSrc = $img.attr('src'),
				$imgAlt = $img.attr('data-alt'),
				$imgExt = $imgAlt.split('.');

		if($imgExt[1] === 'gif') {
			$img.attr('src', $img.data('alt')).attr('data-alt', $imgSrc);
		} else {
			$img.attr('src', $imgAlt).attr('data-alt', $img.data('alt'));
		}

		// Add play class to help with the styling.
		$this.toggleClass('play');

	});

})(jQuery);
</script>
@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css
script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Data Types in R

<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

**Learning Objectives**

@learning_objectives

</div>


## Lesson Preparation: Our RStudio Environment

Please do this step now, because we're going to ask you to follow along throughout and try out code as you go.  

Please read over both options before you start performing any actions, to make sure you pick the right option for you.

<h3>Option 1: Work in the Cloud</h3>

This might work well for you if you either can't or don't want to install R and RStudio on your computer.  The benefit is that you don't have to install anything, but one negative is that this option requires a bit of waiting for your environment to come online.

**First**, we need to create a small container in the cloud for you to work in just using your web browser.  **Click "Launch binder" below.**  It might take a while (5 minutes) to create, depending on how recently it was created (when it's being used more, it's quicker!).  We're looking for a faster way to get you off and running in RStudio without downloads and without creating accounts, but for now this is a great, free way for us to get you working with no extra work on your part.

  <a href = "https://mybinder.org/v2/gh/arcus/education_r_environment/main?urlpath=rstudio" target = "_blank"><img src="https://mybinder.org/static/images/badge_logo.svg"></a> **← Click the "launch binder" button!**

<div class = "hint" style = "align-items: center; display: flex;">

<div style = "margin: 1rem; max-width: 45%; float:left;"> If you're the first person to fire up this environment in a while, you might see this loading screen for up to five minutes.  Be patient!</div>
<div style = "margin: 1rem auto; max-width: 45%; float:left;"> ![Binder loading screen.](media/binder_loading.gif)<!--
style = "border: 1px solid rgb(var(--color-highlight));"-->
</div>
</div>

**Then**, once you have access to RStudio and you see something like the image below, you'll need to open the sample data for this course.  In the file area to the lower right, you'll see, among multiple choices, the folder called "r\_reshape\_long\_wide".  That's the code for this module!

![RStudio as shown in the cloud platform Binder.](media/binder_rstudio.png)<!--
style = "border: 1px solid rgb(var(--color-highlight)); max-width: 800px;"-->

<h3>Option 2: Work on Your Computer</h3>

If you have [R](https://www.r-project.org/) and [RStudio](https://www.rstudio.com/products/rstudio/download/#download) installed already on your local computer, you might be interested in simply downloading our sample code to your computer. Here's how.  Note -- if you've already done this step in another module, you might have the material for this module already!

* In RStudio, open a new project (File, New Project)
* Select Version Control, then Git
* Drop this link into the "Repository URL": https://github.com/arcus/education_r_environment
* Change the "Project directory name" and "Create project as a subdirectory of" boxes to suit your needs (where will this code be stored on your computer?).
* Click to select the "Open in new session" checkbox
* Click "Create Project"
* In the file area to the lower right, you'll see, among multiple choices, the folder called "r\_data\_types".  That's the code for this module!

**Want to watch this process?  Click on the image below to play an animated gif.  It will continue to loop and you can re-start it by clicking again.**

<div style="display:none">@gifPreload</div>

<figure>
  <img src="https://github.com/arcus/education_modules/blob/main/r_data_types/media/rstudio_new_project.png?raw=true" height="384" width="512" alt="RStudio can create a new project that gets its contents from a git repository." data-alt="https://github.com/arcus/education_modules/blob/main/r_data_types/media/rstudio_new_project.gif?raw=true" style = "border: 1px solid rgb(var(--color-highlight));">

<figcaption style = "font-size: 1em;">Click on the image to play the demo of the above steps!</figcaption>
</figure>

If you already completed this work for a previous module, and it's been a while since you downloaded this project to your computer, you may want to get any new and improved files that have been placed there in the meantime:

* Open your project.
* In the Version Control menu, choose "pull branches".  There are two places to do this, as shown below:

![Git button menu with choices to pull and push branches.](media/pull_branches.png)<!-- style = "border: 1px solid rgb(var(--color-highlight)); max-width:400px;" -->  
![Tools menu with choices to pull and push branches.](media/pull_branches_2.png)<!-- style = "border: 1px solid rgb(var(--color-highlight)); max-width:400px;" -->

<div class = "warning">
If you're pulling branches after having worked in other R modules, you might have made local changes (for example, when you filled in exercise code) that will be overwritten by pulling the latest version.  If you want to save your changes, consider making a copy of any exercise files and naming them something new.  For example, if you have already worked in the `r_basics_transform_data` exercise files, you might want to save your version of `transform_exercises.Rmd` to `my_transform_exercises.Rmd`.  That way, you can pull down the latest version of code, overwriting `transform_exercises.Rmd` while holding on to your changes in the new file.
</div>

## Common data types in R

R has several basic data types, and several more that are for special situations.
The most commonly used basic data types in R are:

- character
- numeric
- integer
- logical

Of these, the first two (character data and numeric data) are used most in dataframes. The most useful extra data types for researchers are:

- factors
- dates and datetimes

We'll explore each of these data types in more detail in the sections that follow.
But first, we'll go over some general information about how data types work in R and why you need to pay attention to them.

<div class = "help">
**Confusing terminology:**

As you learn more about R, you'll see references to "types", "classes", and "modes", all of which seem very similar.
There are some real (but subtle) [differences between them](https://stats.stackexchange.com/questions/3212/mode-class-and-type-of-r-objects), but for the most part those differences exist for historical reasons only --- from a practical standpoint, type, class, and mode all work pretty similarly.

To help cut through the confusion, we'll stick to recommending functions that work well for all three, rather than functions that are designed to work with only one.
In general, most high-level functions (e.g. any statistical or plotting functions) don't require you to distinguish between type, class, and mode.
</div>

### Why different data types?

Computers are very good at what they do, but humans are still much smarter about many things.

One thing people are very good at but computers struggle with is quickly and accurately classifying information by type ---
for example, a person can browse through a column of data with entries like "Elif", "Clara", and "Kansia" and know those are words (more specifically, probably names), whereas a column with entries like "1.2", "0.45", and "3.1" is numbers.
And being able to distinguish those different kinds of columns means if you ask a human to summarize those data, they might do something like take the average of number column, but they wouldn't try to get the average of a list of words.
Computers, on the other hand, are very likely to make exactly that kind of mistake.

To help computers process data effectively, dataframes in R include **metadata** that tell R what type of information is stored in each column.
That makes it possible for R to avoid silly mistakes like trying to get the average of a list of words, but it also means we can have useful defaults like [automatically dummy-coding any categorical variables you enter as predictors in a linear model](link), and providing helpful error messages when you try to use a variable of one type in a function that requires a different data type.

When you're working with data in R, you'll want to check your dataframes to make sure R is thinking about the variables they way you intend it to.  

### Vectors and data types

A vector is a sequence of R objects, for example, each of the entries in a list, or each of the observations in a column of data.
An atomic vector (usually shortened to just "vector") is a sequence of objects that are all the same type.
In contrast, a "list" in R is a sequence that allows entries to be different data types.

<div class = "important">
Technically, "vector" is a general term in R that includes both atomic vectors and lists.
In practice, when most people talk about vectors in R, they mean atomic vectors only, and they will specify lists if they want to talk about lists instead.
</div>

Vectors are the main workhorse of most R analyses, including anything with dataframes --- each of the columns in a dataframe is an atomic vector.
That means that a single column in an R dataframe must have just one data type.
If you try to put elements of different types into the same column, you'll either get an error or R will [coerce](https://www.oreilly.com/library/view/r-in-a/9781449358204/ch05s08.html) it all into the same data type. 

The function `c()` (short for "combine") in R is used to create an atomic vector.
R will try to guess the correct data type for the vector based on what you enter.
Although it usually does a good job, it can get hung up on some common issues.

Try to guess what data type each of the following vectors will be:

```r
v1 <- c(2, 4, 3, "2kg")
v2 <- c("June 10, 2020", "July 1, 2020", "March 13, 2020")
v3 <- c("treatment", "control", "control", "treatment")
```

## Data types in R

### Numeric

Technically integer and numeric data are two different types, but for most purposes they behave the same way.
If your data read as integer (which will some times be the case when it is all whole numbers, with no decimal points), it's generally safe to just think of that as numeric.


`Inf` and `NaN` are two kinds of special numbers in R.
`Inf` and `-Inf` stand for infinity and negative infinity, respectively.
`NaN` stands for "Not a Number" and shows up when a numeric calculation is undefined, such as `0/0`.

### Factors

https://r4ds.had.co.nz/factors.html

https://swcarpentry.github.io/r-novice-inflammation/12-supp-factors/index.html

heads up: stringsAsFactors=FALSE https://www.r-bloggers.com/2018/03/r-tip-use-stringsasfactors-false/

https://forcats.tidyverse.org/

### Dates and times

https://r4ds.had.co.nz/dates-and-times.html

https://lubridate.tidyverse.org/

### Strings

Also called "character" data.

https://r4ds.had.co.nz/strings.html

https://stringr.tidyverse.org/

### Other data types

Logical data has only two possible options: `TRUE` or `FALSE`.
It usually shows up as a result of a test or comparison, rather than as a type of data you would save in a dataframe.

Although it is possible to store a binary variable in logical form, it's often easier and cleaner to use factors instead.
Consider the following made-up example that includes a variable `private_ins`, which indicates whether each patient had private insurance or not.
First, we'll look at a dataframe that stores `private_ins` as logical:

Now let's look at the same dataframe, but this time with `private_ins` stored as a factor:




R also supports a data type called "complex" which is for [numbers with a real and imaginary component](https://en.wikipedia.org/wiki/Complex_number).
If you don't work with imaginary numbers (as is the case for nearly all researchers), feel free to ignore this data type completely.

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

<!--
author:   Joy Payton
email:    paytonk@chop.edu
version: 1.0.7
language: en
module_template_version: 2.0.0
narrator: US English Female
title: R Basics: Visualizing Data With ggplot2
comment:  Learn how to visualize data using R's `ggplot2` package.
long_description: Do you want to learn how to make some basic data visualizations (graphs) in R?  In this module you'll learn about the "grammar of graphics" and the base code that you need to get started.  We'll use the basic ingredients of a tidy data frame, a geometric type, and some aesthetic mappings (we'll explain what all of those are).  This module teaches the use of the `ggplot2` package, which is part of the `tidyverse` suite of packages.
estimated_time: 1 hour

@learning_objectives  

After completion of this module, learners will be able to:

- Write R code that creates basic data visualizations
- Identify geometric plot types available in `ggplot2`
- Map columns of data to visual elements like color or position

@end

@version_history
1.0.1: revision to correct image links referring to wrong branch + small changes to environment setup language to be exactly mirrored across all 3 R basics modules.
1.0.5: add information about Posit Cloud
1.0.6: remove second attribution location

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
# R Basics: Visualizing Data With `ggplot2`

<div class = "overview">

## Overview

@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

Minimal experience of using the RStudio IDE and writing R code (specifically, within an R Markdown document) is necessary to understand and use this material.  If you can understand and do the following, you'll be able to complete this course:

* Run a command that's provided to you in the console
* Use the Environment tab to find a data frame and learn more about it
* Insert a new code chunk in an R Markdown document

One potential way to get these basic skills is to take our [R Basics: Introduction](https://liascript.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_introduction/r_basics_introduction.md) course.

This course is designed for R beginners with minimal experience and it is not an advanced course in `ggplot2`.  If you have experience with `ggplot2` already, you may find our ["Data Visualization in ggplot2"](https://liascript.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/data_visualization_in_ggplot2/data_visualization_in_ggplot2.md), which is more advanced, a better fit for your needs.

**Learning Objectives**

@learning_objectives

</div>

Material for this module was adapted, with permission, from [Stephan Kadauke's R for Clinical Data workshop materials](https://skadauke.github.io/intro-to-r-for-clinicians-chop/).  We owe special thanks to Dr. Kadauke as well as the R User Group at Children's Hospital of Philadelphia for their generosity in sharing these materials.


## Lesson Preparation

Let's start by taking a peek at the data we'll be using.

The data we will use in this module is a data frame called `covid_testing`, which consists of fabricated (completely fake) demographic and testing data for Covid tests early in the Covid-19 pandemic.

This is what that data looks like:

![The `covid_testing` data frame in the RStudio data viewer.  The first 13 rows of over fifteen thousand rows are shown.  The first eight columns are shown.  The columns are: `mrn`, `first_name`, `last_name`, `gender`, `pan_day`, `test_id`, `clinic_name`, and `result`.](media/covid_testing_df.png)<!--
style = "max-width:800px;"-->

On the next page, you'll learn how to get access to the sample code.  

### Our RStudio Environment

Please do this step now, because we're going to ask you to follow along throughout and try out code as you go.  

Please read over all the options before you start performing any actions, to make sure you pick the right option for you.

<h3>Option 1: Work Anonymously in the Cloud</h3>

This might work well for you if you either can't or don't want to install R and RStudio on your computer.  The benefit is that you don't have to install anything or have any account set up with an online cloud provider.  This solution is completely anonymous.  However, there are some drawbacks.  One negative is that this option requires a bit of waiting for your environment to come online.  Another is that your changes aren't saved anywhere, and your environment will time out and disappear forever.  

**First**, we need to create a small container in the cloud for you to work in just using your web browser.  **Click "Launch binder" below.**  It might take a while (5 minutes) to create, depending on how recently it was created (when it's being used more, it's quicker!).  We're looking for a faster way to get you off and running in RStudio without downloads and without creating accounts, but for now this is a great, free way for us to get you working with no extra work on your part.

<a href = "https://mybinder.org/v2/gh/arcus/education_r_environment/main?urlpath=rstudio" target = "_blank"><img src="https://mybinder.org/static/images/badge_logo.svg"  alt="Launch Binder"></a> **← Click the "launch binder" button!**


<div class = "hint" style = "align-items: center; display: flex;">

<div style = "margin: 1rem; max-width: 45%; float:left;"> If you're the first person to fire up this environment in a while, you might see this loading screen for up to five minutes.  Be patient!</div>
<div style = "margin: 1rem auto; max-width: 45%; float:left;"> ![Binder loading screen](media/binder_loading.gif)<!--
style = "border: 1px solid rgb(var(--color-highlight));"-->
</div>
</div>

**Then**, once you have access to RStudio and you see something like the image below, you'll need to open the sample data for this course.  In the file area to the lower right, you'll see, among multiple choices, the folder called "r\_basics\_visualize\_data".  That's the code for this module!

![RStudio as shown in the cloud platform Binder. The left side of the screen displays the "Console" tab. On the right there is a split between an "upper" and "lower" section. The upper section is the "Environment", which is empty. The lower section, "files", shows one file (environment.yml) and three folders (r_basics_introduction, r_basics_transform_data, r_basics_visualize_data)](media/binder_rstudio.png)<!--

style = "border: 1px solid rgb(var(--color-highlight)); max-width: 800px;"-->


<h3>Option 2: Use Posit Cloud</h3>

Posit (the company formerly known as RStudio) provides a multi-tiered cloud environment for using RStudio.  Unlike option 1 above, this option does require you to have an account with Posit Cloud, their online RStudio server.  The good news is that the base level of Posit Cloud is free!

First, you'll need to [create a (free!) Posit cloud account](https://posit.cloud/plans).  

Then, once you're logged in at [https://posit.cloud](https://posit.cloud), open the "education\_r\_environment" project at [https://posit.cloud/content/5273350](https://posit.cloud/content/5273350).  That will give you a temporary copy so you can run our code, but not make any changes to it.

In the file area to the lower right, you'll see, among multiple choices, the folder called "r\_basics\_visualize\_data".  That's the code for this module!

Click on "Save a Permanent Copy" if you want to save any changes to your version of this code. 

![Posit menu bar with "Make Permanent Copy"](media/make_copy.png)<!--
style = "border: 1px solid rgb(var(--color-highlight)); clear:both;"-->

Now you can not only work in the cloud, but also save your work.

<h3>Option 3: Work on Your Computer</h3>

If you have [R](https://www.r-project.org/) and [RStudio](https://www.rstudio.com/products/rstudio/download/#download) installed already on your local computer, you might be interested in simply downloading our sample code to your computer. Here's how.  Note -- if you've already done this step in another module, you might have the material for this module already!

<div class = "warning">
Do you use Microsoft OneDrive?  

Knitting files can sometimes be problematic with some versions of Microsoft OneDrive, so if you are working from your local computer and get strange errors when you try to knit, try to use a directory that's not within a OneDrive folder to see if that helps.  Newer versions of OneDrive seem to be less buggy, so you may also want to update your OneDrive software.
</div>

* In RStudio, open a new project (File, New Project)
* Select Version Control, then Git
* Drop this link into the "Repository URL": https://github.com/arcus/education_r_environment
* Change the "Project directory name" and "Create project as a subdirectory of" boxes to suit your needs (where will this code be stored on your computer?).
* Click to select the "Open in new session" checkbox
* Click "Create Project"
* In the file area to the lower right, you'll see, among multiple choices, the folder called "r\_basics\_visualize\_data".  That's the code for this module!

**Want to watch this process?  Click on the image below to play an animated gif.  It will continue to loop and you can re-start it by clicking again.**

<div style="display:none">

@gifPreload

</div>

<figure>

  <img src="https://github.com/arcus/education_modules/blob/main/r_basics_visualize_data/media/rstudio_new_project.png?raw=true" height="384" width="512" alt="RStudio can create a new project that gets its contents from a git repository." data-alt="https://github.com/arcus/education_modules/blob/main/r_basics_visualize_data/media/rstudio_new_project.gif?raw=true" style = "border: 1px solid rgb(var(--color-highlight));">

<figcaption style = "font-size: 1em;">

Click on the image to play the demo of the above steps!

</figcaption>

</figure>

If you already completed this work for a previous module, and it's been a while since you downloaded this project to your computer, you may want to get any new and improved files that have been placed there in the meantime:

* Open your project.
* In the Version Control menu, choose "pull branches".  There are two places to do this, as shown below:

![Version control button in RStudio menu at top of window drops down with choices to pull and push branches.](media/pull_branches.png)<!-- style = "border: 1px solid rgb(var(--color-highlight)); max-width: 400px;"-->

![Tools tab in the highest level menu bar drops down with with a Version Control option. Under version control, there are choices to pull and push branches.](media/pull_branches_2.png)<!-- style = "border: 1px solid rgb(var(--color-highlight)); max-width: 400px;"-->


<div class = "warning">
If you're pulling branches after having worked in other R modules, you might have made local changes (for example, when you filled in exercise code) that will be overwritten by pulling the latest version.  If you want to save your changes, consider making a copy of any exercise files and naming them something new.  For example, if you have already worked in the `r_basics_transform_data` exercise files, you might want to save your version of `transform_exercises.Rmd` to `my_transform_exercises.Rmd`.  That way, you can pull down the latest version of code, overwriting `transform.Rmd` while holding on to your changes in the new file.
</div>

### How to Follow Along

Open the "r\_basics\_visualize\_data" directory in whichever RStudio environment you're working in. Then, open the "visualize_exercises.Rmd" which we'll use for our first hands-on activity in just a bit!


![`RStudio showing the visualize_exercises.Rmd file`](media/visualize_exercises.png)<!-- style = "border: 1px solid rgb(var(--color-highlight)); max-width: 800px;" -->

## Thinking Graphically From Data

Let's try to imagine some **data visualizations** (also known as **plots** and **graphs** interchangeably).  


Consider the `covid_testing` data frame shown below.  Think about what the columns mean and which columns you might like to see represented on a data visualization.


![The first 8 columns of the `covid_testing` data frame are shown: `mrn`, `first_name`, `last_name`, `gender`, `pan_day`, `test_id`, `clinic_name`, and `result`.](media/covid_testing_df.png)<!-- style = "max-width:800px;"-->

What do you think a plot would look like in which:

* the x-axis represents `pan_day` (day of the pandemic), and
* the y-axis represents the number of tests that were performed on that day?

Take a few seconds and try to visualize this graph in your mind or doodle it on a piece of paper in front of you.

### Thinking Graphically From Data, Part 2

What we've asked you to imagine is a plot in which we have the **count** or the **frequency** of a test on the y axis, plotted against the pandemic day, represented by the x axis. Do you know the name of that type of plot that has the count of a thing on the y axis and the distribution of those counts along the x axis?

Here's another example of that kind of plot:

![A normally distributed or bell-shaped curve.  The x axis ranges from -3 to 3 while the y axis goes from 0 to 200](media/small_histogram.png)<!-- style = "max-width:800px;"-->

In the box below, write what you think the name of this is (all lowercase, please).

[[histogram]]
[[?]] Hint: this word ends in "gram"
***
<div class = "answer">

"histogram" is the right answer!  A histogram plots the frequency of something in terms of some other thing (for instance, a time value like days).  In our next section, we're going to build a histogram.

</div>
***

### Building Your First Histogram

To get started, let's first load up our fabricated data.  In the `visualize_exercises.Rmd` file, run the first code chunk by clicking the green "play" button (look at line 10).  This gives you the data frame with fake Covid testing data.


For the next step, we'd like for you to go into the **console** to practice running some code there.  The console is usually in the lower left pane (or it might take up the whole left side, if you don't have any files open yet).

Don't panic if the code we ask you to input seems incomprehensible right now or you get an error message.  We'll walk you through what it all means!

In the console, please type in the following.  While you can certainly cut and paste, there is sometimes an advantage to typing the code by hand, because it helps you develop "muscle memory" about how to construct code.  Pay attention to the spelling, capitalization, and parentheses!  

```r

ggplot(data = covid_testing) +
  geom_histogram(mapping = aes(x = pan_day))

```

And yes, you can hit "Enter" after that plus sign and keep typing on the next line.  There will be a little plus sign on the second line that lets you know that the console is accepting the second line as a continuation of the first.  When you're finished, just hit "Enter" to run that code.  

When you run the code, you'll  see a graph open up in the lower right pane, and your console should look something like this:

![R console showing code and a red message that reads "`stat_bin()` using `bins = 30`. Pick better value with `binwidth`"](media/r_console.png)<!-- style = "border: 1px solid rgb(var(--color-highlight)); max-width:700px;" -->

When you run this code, you get what looks like an error in the console but is actually just a message (even though it's in a scary red color).

R lets you know that when you ask it to draw a histogram, you should probably tell it how wide each bin should be, because this affects the granularity of the data displayed.  You can either set the number of bins (say, 10 bins or 100 bins) or you can set the bin width (like 1 to make a bin 1 day wide, 7 to make a bin one week wide, etc.)

### The Power of Data Visualizations

![Histogram of covid tests by day of pandemic from Day 0 to Day 125. In the first 30 days, the number of tests being run slowly ramps up to around 625 tests. After 30 days, the number of tests stays fairly high with some oscillation over time between about 375 and 825.](media/covid_histogram.png)<!-- style = "max-width: 800px;"  -->


When we asked you to imagine what this plot might look like - the number of Covid tests that were performed on a given day over time – you might have imagined something like this. Initially you have very few tests that are being run, maybe because the pandemic hasn't hit this area much yet or because the test isn't yet broadly available. And at some point the number of tests increases and remains at a high level. But this simple visualization tells you so much more than that general shape. You can see that by 30 days, the testing ramp-up settles. And there appear to be some interesting things going on after day 60 that you might want to look into further.


Even though this graph isn't publication-perfect (at least not yet), it's still very useful for honing your knowledge about the data.

## Introducing `ggplot2`

<div style = "align-items: center; display: flex;">

<div style = "margin: 1rem; max-width: 65%; float:left;">


We'll be using the `ggplot2` package for creating graphics. `ggplot2` is part of the tidyverse so it will get loaded when you load the tidyverse package.

`ggplot2` (and its main function, plain old `ggplot` without the 2) provides a "**grammar of graphics**" for data visualization. The idea of having a "grammar" for something is actually pretty common in R. Essentially, there should be a consistent way to build any type of "thing" in R, in this case, any type of graph. This makes it easier to learn and also easier to for humans to read the code later and make sense of it. And that's super important because most people who use R are not programmers.


The idea of the grammar of graphics is that you should be able to specify any type of graph by specifying the data that goes into it, the type of graph that you want to make, and a mapping that describes how the data should be represented as visual marks on that graph.


Having a consistent grammar means that once you learn how to make a histogram that knowledge can be applied to make a scatter plot with little extra effort. This makes it easy to generate lots of different graphs quickly which helps you understand your data more quickly.

Also, `ggplot2` graphs look great and the package can be used to generate publication-quality plots.
</div>
<div style = "margin: 1rem auto; max-width: 30%; float:left;">

![""](media/ggplot2_hex.png)


</div>
</div>

### The ggplot() Function

Here is a quick analysis of how we just used ggplot to make that histogram a few pages ago.


![""](media/ggplot_analysis.png)<!-- style = "max-width: 600px;" -->


<lia-keep>
<table style = "width = 100%">
<tr><th style = "width: 45%;"></th><th style = "width: 45%;"></th></tr>
<tr style="padding: 3em; border: 1px solid rgb(var(--color-text));"><td>1) We always start with <code>ggplot()</code>.</td>
<td><pre style = "color: rgba(var(--color-text), 0.5); margin:1em; font-size:0.8em;">
<span style = "color: rgb(var(--color-text)); font-weight: bold;">ggplot(</span>data = covid_testing<span style = "color: rgb(var(--color-text)); font-weight: bold;">)</span> +
  geom_histogram(mapping = aes(x = pan_day))
</pre>
</td></tr>
<tr style="padding: 3em; border: 1px solid rgb(var(--color-text));"><td>2)In the parentheses just after ggplot, give it a <b>data frame</b> to start with, in this case, our <code>covid_testing</code> data frame.</td>
<td><pre style = "color: rgba(var(--color-text), 0.5); margin:1em; font-size:0.8em;">
ggplot(<span style = "color: rgb(var(--color-text)); font-weight: bold;">data = covid_testing</span>) +
  geom_histogram(mapping = aes(x = pan_day))
</pre>
</td></tr>
<tr style="padding: 3em; border: 1px solid rgb(var(--color-text));"><td>3) We build our plot across several different lines, so we include a plus sign (<code>+</code>) at the end of the line to say "wait, we're not done yet!"
</td>
<td><pre style = "color: rgba(var(--color-text), 0.5); margin:1em; font-size:0.8em;">
ggplot(data = covid_testing) <span style = "color: rgb(var(--color-text)); font-weight: bold;">+ </span>
  geom_histogram(mapping = aes(x = pan_day))
</pre>
</td></tr>
<tr style="padding: 3em; border: 1px solid rgb(var(--color-text));"><td>4) In the second line, we describe what kind of geometric representation we want -- a histogram, which we communicate to R using  <code>geom_histogram()</code>.
</td>
<td><pre style = "color: rgba(var(--color-text), 0.5); margin:1em; font-size:0.8em;">
ggplot(data = covid_testing) +
  <span style = "color: rgb(var(--color-text)); font-weight: bold;">geom_histogram(</span>mapping = aes(x = pan_day)<span style = "color: rgb(var(--color-text)); font-weight: bold;">)</span>
</pre>
</td></tr>
<tr style="padding: 3em; border: 1px solid rgb(var(--color-text));"><td>5)  We also add some mappings inside the parentheses of `geom_histogram`, explaining which data from the data frame should be displayed in the histogram.  We use `aes()` (short for "aesthetic" or "aesthetic mapping") to tell ggplot how to draw the visualization.
</td>
<td><pre style = "color: rgba(var(--color-text), 0.5); margin:1em; font-size:0.8em;">
ggplot(data = covid_testing) +
  geom_histogram(<span style = "color: rgb(var(--color-text)); font-weight: bold;">mapping = aes(</span>x = pan_day<span style = "color: rgb(var(--color-text)); font-weight: bold;">)</span>)
</pre>
</td></tr>
<tr style="padding: 3em; border: 1px solid rgb(var(--color-text));"><td>6) Inside the parentheses of "aes" we specify the x-axis by including "x = variable". In this case, we write "x = pan_day". We only have to specify the <b>x axis</b>, because a histogram assumes that you're counting rows of data and will map that to the y axis.

</td>
<td><pre style = "color: rgba(var(--color-text), 0.5); margin:1em; font-size:0.8em;">
ggplot(data = covid_testing) +
  geom_histogram(mapping = aes(<span style = "color: rgb(var(--color-text)); font-weight: bold;">x = pan_day</span>))
</pre>
</td></tr>
</table>
</lia-keep>

### A 3-Step Template


We just provided a high level of detail on the specific use case of working with the `covid_testing` data frame, but once you have the pattern in mind, you mostly have to think about three main tasks.  We'll explain each step in the following sections.


1) Pick a **tidy data frame** (this contains the data you want to plot, organized in a tidy way) and add it to the first line, where we see `ggplot(data = )`

2) Pick a **geom function** (this is the type of plot you want to make), and add it as a new line (like we did with `geom_histogram`)

3) Write **aesthetic mappings** (which columns of the data you want to see added to the plot, and how you want them visualized)

Here's a visual of what that a template looks like, with those three tasks:

![`ggplot code follows a general template: the ggplot function with data = some_data_frame in its parentheses; a plus sign; some geom_function with mapping = aes function inside its parentheses; and inside the aes function parentheses are some aesthetic mappings. This general template is constant. The data frame, chosen geom_function, and the mappings vary depending on the situation.`](media/ggplot_template.png)<!-- style = "max-width:700px;" -->

And here is the template in case you want to copy and paste it.  The first task, of picking a data frame, would change the first line of the template, and the second and third tasks would change the second line.  You don't have to indent the second line, but it's a good idea, because it visually reminds you that it's the continuation of an earlier line of code.

```
ggplot(data = data_frame) +
  geom_function(mapping = aes(mappings))
```

In the next section, we'll talk in more detail about the first step, selecting a tidy data frame.


### Step 1: Tidy Data Frame

Let's get started. The first detail is a "tidy" data frame which contains the data you want to plot.  It replaces the generic `data_frame` in our template (shown again below).

![`ggplot code follows a general template.  Here we begin with the ggplot() function with data = some_data_frame in its parentheses.`](media/ggplot_template.png)<!-- style = "max-width:400px;" -->

A data set can take on a lot of different shapes with different styles of organizing data. The one method or shape that is best suited for data analysis is known as "tidy".

![Table with rows and columns.  The data is not visible, although headers are, and include mrn, gender, `test_id`, and result. In each row and column, an arrow spans the entire row or entire column.](media/tidy_data.png)<!-- style = "max-width: 400px;" -->

We won't cover "tidy" data in detail in this module.  It's sufficient at this point to know that tidy data is in a rectangular shape with rows and columns, and:

* Columns each measure just one thing (so, no "doubling up" with first and last name or race and gender) and
* Rows each constitute a single observation (like a single patient, or a single vial, or a single city block)
* Each value is in its own cell (again, no doubling up values or merging of cells)

The sample data we're going to work with in this module, the `covid_testing` data, is already "tidy".  So our first step is easy: we are going to choose the `covid_testing` data frame and put that as our tidy data frame.


### Step 2: geom Function


As a reminder, we put forth three steps in our `ggplot` template:

1) Pick a **tidy data frame** (this contains the data you want to plot, organized in a tidy way) and add it to the first line, where we see `ggplot(data = )`

2) Pick a **geom function** (this is the type of plot you want to make), and add it as a new line (like we did with `geom_histogram`)

3) Write **aesthetic mappings** (which columns of the data you want to see added to the plot, and how you want them visualized)

![`ggplot code follows a general template.  In the second line of code we add some geom_function with mapping = aes function inside its parentheses.`](media/ggplot_template.png)<!-- style = "max-width:600px;" -->

Let's take on the second step: selecting a **geom function**.

We'll go into more detail about what geom functions are, but for now, just know that you need to tell ggplot what type of graph you want, and you do that by picking the right `geom_` function.  RStudio makes code completion suggestions, son when you start typing `geom_`, you'll see a long list of possible ways to finish that term:


![`RStudio autocomplete suggestions for geom_  include possibilities like geom_abline, geom_area, geom_bar, and so forth.  Hovering over one of the choices provides a contextual help window that describes how to use the geom.`](media/geom_autocomplete.png)


Here are a few useful geom functions for visualizing clinical data, but there are many more. With these six you can make histograms, bar plots, scatter plots, dot plots, boxplots, and line graphs.

| Visual depiction | ggplot geom function |
| --- | --- |
| ![unlabeled histogram](media/geom_histogram_mini.png)<!-- style = "max-width:100px;" --> | geom_histogram() |
| ![unlabeled bar chart](media/geom_bar_mini.png)<!-- style = "max-width:100px;" --> | geom_bar() |
| ![unlabeled scatter plot with points](media/geom_point_mini.png)<!-- style = "max-width:100px;" --> | geom_point() |
| ![unlabeled dot plot](media/geom_dotplot_mini.png)<!-- style = "max-width:100px;" --> | geom_dotplot() |
| ![unlabeled box plot](media/geom_boxplot_mini.png)<!-- style = "max-width:100px;" --> | geom_boxplot() |
| ![unlabeled line graph](media/geom_line_mini.png)<!-- style = "max-width:100px;" --> | geom_line() |

### Step 3: Aesthetic Mappings




As a reminder, we put forth three steps in our `ggplot` template:

1) Pick a **tidy data frame** (this contains the data you want to plot, organized in a tidy way) and add it to the first line, where we see `ggplot(data = )`

2) Pick a **geom function** (this is the type of plot you want to make), and add it as a new line (like we did with `geom_histogram`)

3) Write **aesthetic mappings** (which columns of the data you want to see added to the plot, and how you want them visualized)

![`ggplot code follows a general template.  In the second line of code we add some geom_function with mapping = aes function inside its parentheses.`](media/ggplot_template.png)<!-- style = "max-width:400px;" -->

Let's take on the third step: writing aesthetic mappings.  This is where you tell R how you want the columns of the data frame represented as graphical markings on the plot.  It's important to start with a couple of important distinctions:

* An **aesthetic** is something that you can see about a data element on a graphic, such as its **position** on an x/y grid, but also other features such as for example its **color**.
* An **aesthetic mapping** is a rule that tells ggplot how to draw the data from a specific column of the data set on the plot. These are elements that would result in a different looking visualization if you were to change the data being provided. For example, the height of a bar changes depending on the data, and the x and y position of a point on a scatter plot changes depending on the data).

Of course, there are other visual elements of a data visualization that **wouldn't** automatically change if you change the data you provide. For example, the color of the background of the graph and the label of the axes won't change even if new data is added. R gives us a lot of control over these elements as well. Please note, however: since they aren't "mapped" to a specific quality of the data, we **"set"** them, rather than "map" them, which means we don't put these assignments inside `aes()`.

<div class = "care">
Don't worry if this distinction seems a bit fuzzy at first -- it can be tricky to grapple with, and will become clearer over time as you gain more experience manipulating visualizations in R. Even advanced coders sometimes set an aesthetic they meant to map, and vice versa.
</div>

Let's consider an example in a data frame with three columns, called "a", "b", and "c".  
We can imagine mapping the values in column "a", which are numerical values, to the x axis.  With column "b", also numerical, we can map those values to the y axis.  And for column "c", which has categorical data with "M" and "F" values, we can imagine mapping that to colors.  

We may also want to set the size of the points on the graph to a certain value. While I'm sure you've seen visualizations where the size of a dot corresponds to something about the data, that's not what we want to do here -- we just want to customize the size of the dot to be a little bit bigger than the default, which is why this wouldn't be one of our "mappings" in this particular instance.


The mapping in ggplot would be within an **aes()**, or aesthetic mapping, and looks like this:

`aes(x = a, y = b, color = c)`

Note that R automatically figures out reasonable axis limits and a color scale, but you can fine tune this manually.

Here's a visual that might help:

![Small table of data with columns a, b, and c next to a blank x-y coordinate plane. An arrow is drawn from column a to the x-axis, and an arrow from column b to the y-axis. Rows that have a "M" in column C have blue dots, and rows that have an "F" get green dots.](media/abc_aesthetics.png)


### Quiz: Aesthetic Mappings


Let's do a quick check of your understanding of aesthetic mappings.  As a reminder:

* Data visualization visual elements that **don't change** according to the data are **set** , not mapped.  (for example, the color of the background of the graph, which doesn't vary based on the data).
* Data visualization elements that **do change** with the data are **mapped** (for example, the height of a bar changes depending on the data, and the x and y position of a point on a scatter plot changes depending on the data).

Here are some aesthetic mappings to consider:

![6 aesthetic options: position, shape, size, color, line width, and line type.](media/aesthetic_mappings.png)<!-- style = "max-width:700px" -->


From *Fundamentals of Data Visualization*, by Claus Wilke, licensed under CC-BY-NC-ND

Which of the following elements of a graph could reasonably form part of an aesthetic mapping? Check all that apply!

[[ ]] The size of font used in the title of a plot
[[X]] The size of a point on a scatterplot
[[X]] The location of a point on a scatterplot
[[ ]] The location of the caption on a graph
[[ ]] The color of the font for the x-axis title
[[ ]] The color of gridlines in the background of a graph
[[X]] The color of a line that connects data points in a line graph
[[X]] The color of paired bars in a bar chart
[[X]] The line style (solid, dotted) in a line graph
[[?]] There are multiple correct answers!
***
<div class = "answer">

Elements that don't get their value from data don't form part of an aesthetic **mapping**.  For example, the size of the font I want for the title of a plot is based on what looks good, what is readable, and what my publisher asks for.  I can set that without looking at any of the actual data.  The same thing is true of the location of a caption.  I might left-justify it, or center it, or put it above or below the graph, but that's an aesthetic choice that doesn't have any relationship (or mapping) to the data I want to display.

Out of the list above, these are the visual elements that could be reasonably mapped back to the data I want to display:

* The size of a point on a scatterplot (for example, more cases = a bigger dot, fewer cases = a smaller dot)
* The location of a point on a scatterplot (the x value could be the day of the pandemic and the y value could be the number of tests)
* The color of a line that connects data points in a line graph (imagine a blue line that shows invalid tests over time, and a purple line that shows valid tests, both positive and negative, over time)
* The color of paired bars in a bar chart (perhaps we have the number of male and female patients being tested each week, and use different colors to indicate the sex in a paired bar chart)
* The line style (solid, dotted) in a line graph (we could have actual number of tests administered in a solid line and a machine learning prediction of number of tests in a dotted line)

</div>
***

There are actually a lot of aesthetic mapping possibilities, and they depend on the kind of plot you're making. For example, for a line graph you can define line width and line type, and for scatter plots you can define the shape of the dots.

Picking the best aesthetics for your graph is as much an art as it is a science. Claus Wilke's *[Fundamentals of Data Visualization](https://serialmentor.com/dataviz)* is a great introduction to this topic.

### Hands-On: Mapping Aesthetics


Using your RStudio file browser (one of the tabs that usually appears in the lower right pane of RStudio), please find and open the `r_basics_visualize_data` directory, and then open `visualize_exercises.Rmd`, which will allow you to work alongside the sections of this module.

![`RStudio window showing visualize_exercises.Rmd`](media/visualize_exercises.png)<!-- style = "max-width: 600px; border: 1px solid rgb(var(--color-highlight))" -->

To get started, load the fabricated data by running the first code chunk by clicking the green "play" button (look at line 10).  This gives you the data frame with fake Covid testing data. You may have already done this a few sections ago, but it won't hurt to do it again.


Then, work through the exercises in the `visualize_exercises.Rmd` file, adding and updating code as indicated.

Stop when it says "Stop here", and return to this page.  We'll go over the solutions in the next section.


### Solutions

If you like, you can open the solutions version of `visualize_exercises.Rmd` by using your RStudio file browser to open `visualize_solutions.Rmd`.

You had three tasks to complete.  We'll go through them one at a time.

In your first task, you were asked to do what we already did once in this module: create a histogram of Covid tests as a function of `pan_day`.  There were three blanks to fill in, and three numbered instructions.

![`Lines 18-31 of visualize_exercises.Rmd`](media/task_1.png)<!-- style = "max-width:700px; border: 1px solid rgb(var(--color-highlight))" -->

Here's the solution that you should place in that code chunk:

``` r
ggplot(data = covid_testing) +
  geom_histogram(mapping = aes(x = pan_day))
```


In the second task, you were asked to rework that code with a bin width ("binwidth" in code) that corresponded to daily counts:

![`Lines 44-50 of visualize_exercises.Rmd`](media/task_2.png)<!-- style = "max-width:700px; border: 1px solid rgb(var(--color-highlight))" -->

Here's the solution that you should place in that code chunk:

``` r
ggplot(data = covid_testing) +
  geom_histogram(mapping = aes(x = pan_day), binwidth = 1)
```

Finally, for the third task, you had to create a new code chunk by using copy and paste, **and** you had to add an aesthetic mapping using "fill".


![`Lines 58-60 of visualize_exercises.Rmd`](media/task_3.png)<!-- style = "max-width:700px; border: 1px solid rgb(var(--color-highlight))" -->


And here's the solution:

```
ggplot(data = covid_testing) +
  geom_histogram(mapping = aes(x = pan_day, fill = result), binwidth = 1)
```

### Setting vs. Mapping Aesthetics

In the third task you just completed, you **mapped** the fill aesthetic to the **result** variable, by writing "fill = result" inside the **aes()** function:

<div style = "align-items: center; display: flex;">

<div style = "margin: 1rem; max-width: 35%; float:left;"> ![Histogram of Covid tests as a function of `pan_day`.  The bars forming the histogram have three colors: a small blue section at the bottom, representing positive results, a much larger green section in the middle for negative results, and a tiny red section at the top for invalid test results.](media/multicolor_histogram.png)
</div>
<div style = "margin: 1rem auto; max-width: 55%; float:left;">
<lia-keep>
<pre>
ggplot(data = covid_testing) +
  geom_histogram(mapping = aes(x = pan_day, fill = result))
</pre>
</lia-keep>
</div>
</div>

In contrast, consider this plot. It's the same as the one you've created at the beginning of the session, except the bars are blue, not black. So the difference is the "fill" aesthetic. But we're not really mapping the fill aesthetic to a variable here, because all bars are the same fill color. They don't represent the values of a column (or variable) of a data frame. Instead, we're setting it to a constant value, the color blue.

![Histogram of Covid tests as a function of `pan_day`.  The bars forming the histogram are blue.](media/blue_histogram.png)<!-- style = "max-width: 800px;" -->

To do this in ggplot, you can still use "fill", but:

* Instead of setting it equal to a column / variable, you'll set it to a color, like "blue" or "#1111FF" (if you use "hex" or "hexidecimal" RGB values)
* Instead of placing the "fill = " inside `aes()`, you'll move it outside of `aes()`.

This is how you'd get an all-blue histogram:

```
ggplot(data = covid_testing) +
  geom_histogram(mapping = aes(x = pan_day), fill = "blue")
```

Notice **where** the `fill =` appears and what it it set equal to!

Importantly, R knows a lot of different colors by their English names.  To see them, you can use a [great cheat sheet](http://www.stat.columbia.edu/~tzheng/files/Rcolor.pdf) that shows the color and the color name, or perhaps [this one](http://derekogle.com/NCGraphing/resources/colors).  For "hex" colors, there are a number of "color pickers" out there, like [Google's](https://g.co/kgs/hv1JrX).

## Working With Geoms

Consider: how are these two plots similar?  How are they different?

<div style = "align-items: center; display: flex;">

<div style = "margin: 1rem; max-width: 45%; float:left;"> ![histogram of covid data](media/mini_histogram.png)
</div>
<div style = "margin: 1rem auto; max-width: 45%; float:left;"> ![frequency polygon of covid data](media/mini_freqpoly.png)
</div>
</div>

These two graphs share the same data, plotted on the same x and y axes.  What's different? What's different is that on the left, the data is shown as a histogram, and on the right, it's shown as what's called a frequency polygon.

A geom function is a function that, given the data and aesthetic mappings, generates the **geometric object** used to represent the data.

In the next exercise, you're going to work hands-on with geom functions.

### Hands-On: Geom functions


In your RStudio environment, you should already have `visualize_exercises.Rmd` open.  If not, please reopen it.  Scroll down to `### Your Turn: Geom functions`, which should be around line 90 or so.

![`Lines 91-106 of visualize_exercises.Rmd`](media/ex_2_task_1.png)<!-- style = "max-width:700px; border: 1px solid rgb(var(--color-highlight))" -->

Then, work through the exercises from that point forward, running, adding, and updating code as indicated.  Hint: take advantage of code completion suggestions in RStudio to help you make an educated guess as to how to proceed, especially in the first task.

We'll go over the solutions in the next section, and you can also look in the RStudio file browser and open `visualize_solutions.Rmd` to see the solution!

### Solutions

If you like, you can open the solutions version of `visualize_exercises.Rmd` by using your file browser to open `visualize_solutions.Rmd`.

You had three tasks to complete.  We'll go through them one at a time.

Your first task invited you to run a code chunk that creates a histogram and use that code as the basis of a new code chunk that creates a frequency polygon.  

![`Lines 91-106 of visualize_exercises.Rmd`](media/ex_2_task_1.png)<!-- style = "max-width:700px; border: 1px solid rgb(var(--color-highlight))" -->

This is the solution code:

```
ggplot(data = covid_testing) +
  geom_freqpoly(mapping = aes(x = pan_day))
```

In your second task, you were asked to set the color of the line to "blue".  Note that lines have "color" and shapes have "fill" (for the inside) as well as optional "color" (for the edges).

![`Lines 110-115 of visualize_exercises.Rmd`](media/ex_2_task_2.png)<!-- style = "max-width:700px; border: 1px solid rgb(var(--color-highlight))" -->

This is the proper code:

```
ggplot(data = covid_testing) +
  geom_freqpoly(mapping = aes(x = pan_day), color = "blue")
```

Finally, you were asked to predict what the output of `ggplot` code using two different `geom_` functions would be:

![`Lines 122-131 of visualize_exercises.Rmd`](media/ex_2_task_3.png)<!-- style = "max-width:700px; border: 1px solid rgb(var(--color-highlight))" -->

Run that code, and you should see something like this!

![greyscale graph that shows both a histogram and a frequency polygon of the same covid data, overlaid](media/two_geoms.png)<!-- style = "max-width:700px; border: 1px solid rgb(var(--color-highlight))" -->

## Saving Your Plot

To save a plot you've created in the console, you can go to the **Plots** pane on the bottom right of the RStudio window, click "Export", and select "Save as Image".

To save a plot you've created by running some code inside an R Markdown file, you can **right-click** the plot and select "Save image as".


![""](media/saving_images.png)<!-- style = "max-width:700px;" -->



## More Visualization Options

This section briefly presents additional information to show you some of the possibilities for visualizations in R.  Don't worry about trying to memorize or fully understand how the code works -- this is just to give you some insight into what other things are possible with ggplot2.

<h3>Position Adjustments</h3>

We've only barely scratched the surface of what you can do with ggplots. For example, you can change how overlapping objects are arranged.  For example, instead of a stacked histogram, you can request side-by-side bars.

```
ggplot(covid_testing) +
  geom_histogram(
    mapping = aes(x = pan_day, fill = result),
    position = position_dodge()
  )
```

![A histogram. Instead of a single bar for each bin, there are three: one for invalid tests, one for negative tests, and one for positive tests.  Each is in a distinct color.](media/position_dodge.png)<!-- style = "max-width:700px;" -->


<h3>Themes</h3>

You can use different themes which affect how non-data elements such as axes, gridlines, and background appear.

```
ggplot(covid_testing) +
  geom_histogram(
    mapping = aes(x = pan_day, fill = result),
    position = position_dodge()
  ) +
  theme_light()
```

![The same histogram as above, but now with a white background instead of a gray one.](media/theme_light.png)<!-- style = "max-width:700px;" -->


<h3>Scales</h3>

You can customize color scales.

```
library(colorspace)

cols <- c(
  "invalid" = "grey80",
  qualitative_hcl(2, palette = "dark3")
)

ggplot(covid_testing) +
  geom_histogram(
    mapping = aes(x = pan_day, fill = result),
    position = position_dodge()
  ) +
  theme_light() +
  scale_fill_manual(values = cols)
```

![The same histogram as before, but with differently colored bins now.](media/color_scales.png)<!-- style = "max-width:700px;" -->


<h3>Facets</h3>

You can facet your plot. That means breaking it into sub-plots by another variable, for example, gender or location in the hospital.

```
ggplot(covid_testing) +
  geom_histogram(
    mapping = aes(x = pan_day, fill = result)
  ) +
  theme_light() +
  scale_fill_manual(values = cols) +
  facet_wrap(~demo_group)
```

![Five small histograms, one for each demographic group represented in the data.  ](media/facets.png)<!-- style = "max-width:700px;" -->

<h3>Titles and Captions</h3>

And you can add titles, subtitles, or annotations, and change the axis labels or the appearance.

```
ggplot(covid_testing) +
    geom_histogram(
        mapping = aes(x = pan_day, fill = result)
    ) +
    theme_light() +
    facet_wrap(~demo_group) +
    ggtitle(label = "COVID19 Test Volume",
         subtitle = "Faceted by Demographic Group") +
    xlab("Day of Pandemic") +
    ylab("Number of Tests")
```

![Faceted histogram with improved axis labels, title, and subtitle](media/titles_captions.png)<!-- style = "max-width:700px;" -->

### Adding New elements

All of these elements, like position adjustments, themes, color scales, facets, coordinate systems, and text can be added to a ggplot command in the same way that we added a second geom layer – by writing a plus sign followed by a theme function, a scale function, a facet function, etc.

```
ggplot(data = data_frame) +                     # Required
  geom_function(mapping = aes(mappings)) +      # Required
  theme_function +                              # Optional
  scale_function +                              # Optional
  facet_function +                              # Optional
  coordinate_function +                         # Optional
  ...
```

## Recap

| ![""](media/ggplot2_hex.png)<!-- style = "max-width:200px;" --> | **ggplot2** is a package that provides a **grammar of graphics**. You can create any type of plot using a simple template to which you provide: |

| ![""](media/tidy_data.png)<!-- style = "max-width:200px;" --> | 1. A **tidy data frame**, in which each variable is in its own column, each observation is in its own row, and each value is in its own cell; |

| ![""](media/mini_histogram.png)<!-- style = "max-width:200px;" -->  ![frequency polygon of covid data](media/mini_freqpoly.png)<!-- style = "max-width:200px;" --> | 2. A **geom function**, which tells R what kind of plot to make; and |

| ![""](media/positions.png)<!-- style = "max-width:200px;" -->  ![""](media/colors.png)<!-- style = "max-width:200px;" -->  | 3. **Aesthetic mappings**, which tell R how to represent data as graphical markings on the plot. |

| ![""](media/multicolor_histogram.png)<!-- style = "max-width:200px;" -->   ![""](media/blue_histogram.png)<!-- style = "max-width:200px;" -->   | Aesthetics can be **mapped** to a variable or **set** to a constant value. |

| | Additionally, you can do things like change theme, color palette, coordinate systems, facet your graph, and more! |

## Additional Resources

![""](media/fundamentals.png)<!-- style = "max-width:400px;" -->

If you'd like to learn more about which graphics are most effective in specific situations, we recommend taking a look at *Fundamentals of Data Visualizations* by Claus Wilke. This is a very readable and recent primer on data visualization and figure design, and it's [available for free!](https://serialmentor.com/dataviz).  Note that this is not a book about how to code in R.  Rather, it explains visual communication of data insights in a way that will help you regardless of the language you use.

<h4>R for Data Science</h4>

<div style = "align-items: center; display: flex;">
<div style = "margin: 1rem; max-width: 60%; float:left;">
*R for Data Science* is a free text that provides lots of helpful explanation and examples.  The [section on data visualization](https://r4ds.had.co.nz/data-visualisation.html) goes into much more detail than we were able to do in this brief module.  It also provides a number of exercises, if you enjoy learning by doing!

The entire text is available [in English](https://r4ds.had.co.nz/) and [in Spanish](https://es.r4ds.hadley.nz/).

There's also an [unofficial solutions guide](https://jrnold.github.io/r4ds-exercise-solutions/index.html) (only available in English) to allow you to check your work.
</div>
<div style = "margin: 1rem; max-width: 20%; float:left;">
![""](media/r4ds.png)<!-- style = "max-width: 90%" -->

</div>
</div>

<h4>Articles</h4>

Other potentially useful resources include articles written by the team that authored this module:

* [ggplot Overview](https://education.arcus.chop.edu/ggplot-overview/) gives a few sample plots and the code used to generate them.
* [Customizing ggplot2 Visualizations With ggThemeAssist](https://education.arcus.chop.edu/ggthemeassist/) explains how to use the `ggThemeAssist` "add-on" package within RStudio.
* [R 4 Beginners Chapter 3 - Data Visualization with ggplot2](https://education.arcus.chop.edu/r-4-beginners-chapter-3/) and [R 4 Beginners Chapter 4 - Data Visualization with ggplot2, Part II](https://education.arcus.chop.edu/r-4-beginners-chapter-4/) are intended to accompany your use of [R for Data Science](https://r4ds.had.co.nz/), the book we mentioned in the previous page.

### Cheat Sheet!

The ggplot Cheat Sheet is great to have on hand as you're exploring your data. It reviews the basic template for building any plot and also lists the most useful geom functions.

To find official cheat sheets, go to the Help menu and choose "Cheat Sheets".  There are many to choose from!

![RStudio help menu, with Cheat Sheets selected and the submenu option "Data Visualization with ggplot2" selected](media/cheat_sheets.png)<!-- style = "max-width:700px;" -->

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22R+Basics+Visualize+Data%22&version=1.0.7)!

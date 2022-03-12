<!--
author:   Joy Payton
email:    paytonk@chop.edu
version:  1.0
language: en
narrator: US English Female
title: R Basics: Introduction
comment:  Learn how to visualize data using R's `ggplot2` package.
long_description: Are you brand new to R, and ready to get started?  This module teaches the basics of R, RStudio, and R Markdown.

@learning_objectives  

After completion of this module, learners will be able to:

- Define "R", "RStudio", and "R Markdown"
- Create a simple R Markdown file and its associated output document


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
# R Basics: Introduction

<div class = "overview">

## Overview

@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** 1 hour

**Pre-requisites**

No prior experience of using R, RStudio, or R Markdown is required for this course.   

This course is designed for brand new beginners with zero, or minimal, experience working with R.

**Learning Objectives**

@learning_objectives

</div>

Material for this module was adapted, with permission, from [Stephan Kadauke's R for Clinical Data workshop materials](https://skadauke.github.io/intro-to-r-for-clinicians-chop/).  We owe special thanks to Dr. Kadauke as well as the R User Group at Children's Hospital of Philadelphia for their generosity in sharing these materials.

## Terminology: The Three "R"s of This Module

We begin by presenting three terms that may be new to you, or you may have heard about without understanding the distinction between them

<div style = "align-items: center; display: flex;">

<div style = "margin: 1rem; max-width: 45%; float:left;"> ![](media/r_logo.png)
</div>
<div style = "margin: 1rem auto; max-width: 45%; float:left;">

**R**

The first is **R**. R is a statistical programming language that's great for doing data analysis. There are a lot of features that make R great:  

* R is **open source**, which means that it is "free" in two ways -- in the meaning of having **no cost** and also in that can be used widely **without intellectual property concerns or licensing restrictions**.
* R makes it possible to **wrangle** (arrange, reshape, and organize) complex data sets, and
* R can produce publication-quality visualizations.

There is also an open and welcoming community of R users, which is just as important, if not more important, as the actual underlying details of the language.


</div>
</div>

<div style = "align-items: center; display: flex;">

<div style = "margin: 1rem; max-width: 45%; float:left;"> ![](media/rstudio_logo.png)
</div>
<div style = "margin: 1rem auto; max-width: 45%; float:left;">

**RStudio**

Then, there's **RStudio**. RStudio is the name of a company and also the name of a piece of software this company makes (and makes available for free). You can think of RStudio as a fancy text editor for writing R code. The technical term for a fancy text editor for writing code is "Integrated Development Environment", or IDE (you pronounce each letter, eye-dee-ee). You can run RStudio on Mac, Windows, or Linux. It can run on a local computer like your laptop, or on a server that users can access using a web browser.

</div>
</div>

<div style = "align-items: center; display: flex;">

<div style = "margin: 1rem; max-width: 45%; float:left;"> ![](media/r_markdown_logo.png)
</div>
<div style = "margin: 1rem auto; max-width: 45%; float:left;">

**R Markdown**

Finally there's **R Markdown**. R Markdown is a **computational document**, an example of **literate programming**. A computational document is a document that has executable code inside of it, and as we'll discuss shortly, it's a great way to perform data analysis in a reproducible fashion. You'll also hear this called "literate programming" or "literate statistical programming", because an R Markdown document contains both human language (it's literate) as well as computer code (programming).  With R Markdown, we will usually write that executable code using the R language. I say usually because it's actually possible to write code in Python, C++, SQL, and other languages inside of an R Markdown document.  That goes beyond the scope of this module, but it's helpful to remember that R Markdown is quite flexible.

</div>
</div>

So we have R, Rstudio, and R Markdown. For the remainder of this module, we'll show you how these three R's come together to form the infrastructure for performing state of the art data analysis.

### RStudio

There are two versions of RStudio.

<div style = "align-items: center; display: flex;">

<div style = "margin: 1rem; max-width: 45%; float:left;"> ![](media/rstudio_cloud.png)
</div>
<div style = "margin: 1rem auto; max-width: 45%; float:left;">

RStudio Server – a version of the RStudio IDE that can be accessed from a web browser. It's hosted on a server that could be on premises or in the cloud. We'll offer a version of RStudio in the cloud for use, in case you can't or don't want to download R and RStudio to your computer just yet.
</div>
</div>

<div style = "align-items: center; display: flex;">

<div style = "margin: 1rem; max-width: 45%; float:left;"> ![](media/rstudio_desktop.png)
</div>
<div style = "margin: 1rem auto; max-width: 45%; float:left;">

RStudio Desktop – a version of the RStudio IDE that is installed on a personal device like your desktop or laptop. This is what you should use after the course to continue learning R and working on R projects. On the course website, I posted videos that show you how to install RStudio Desktop on a Mac or Windows computer.  

</div>
</div>

Here's what the RStudio window looks like.

![](media/rstudio_desktop.png)<!-- style = "max-width:900px;" -->

On the top left is the **Editor**. This is where you enter code.

On the bottom left is the **Console**. The console allows you to quickly run an individual R command, like for installing a package. We won't use the console very much in this course.

On the top right is the **Environment** tab set. The environment (first and most frequently used tab in the set of tabs in this pane) allows you to look at the data that's loaded into R's memory. Interacting with data in the environment tab can be a little bit like working in Excel, and we'll look at that in an upcoming exercise.

Finally, on the bottom right is where you find your **Files** and related tabs. We'll be using an R Markdown files for coding exercises.

### Quiz: The Three "R"s


<div class = "question">
In the box below, write what you think the name of this is (all lowercase, please).

[[histogram]]
[[?]] Hint: this word ends in "gram"

<div class = "answer">
<details><summary>Click to see an explanation of the answer.</summary>

"histogram" is the right answer!  A histogram plots the frequency of something in terms of some other thing (for instance, a time value like days).  In our next section, we're going to build a histogram.
</details>
</div>
</div>


## Lesson Preparation: Our RStudio Environment

Please do this step now, because we're going to ask you to follow along throughout and try out code as you go.  

Please read over both options before you start performing any actions, to make sure you pick the right option for you.

<h3>Option 1: Work in the Cloud</h3>

This might work well for you if you don't want to, or can't, install R and RStudio on your computer.  The benefit is that you don't have to install anything, but one negative is that this option requires a bit of waiting for your environment to come online.

**First**, we need to create a small container in the cloud for you to work in just using your web browser.  **Click "Launch binder" below.**  It might take a while (5 minutes) to create, depending on how recently it was created (when it's being used more, it's quicker!).  We're looking for a faster way to get you off and running in RStudio without downloads and without creating accounts, but for now this is a great, free way for us to get you working with no extra work on your part.

  <a href = "https://mybinder.org/v2/gh/arcus/education_r_environment/main?urlpath=rstudio" target = "_blank"><img src="https://mybinder.org/static/images/badge_logo.svg"></a> **← Click the "launch binder" button!**

<div class = "hint" style = "align-items: center; display: flex;">

<div style = "margin: 1rem; max-width: 45%; float:left;"> If you're the first person to fire up this environment in a while, you might see this loading screen for several minutes.  Be patient!</div>
<div style = "margin: 1rem auto; max-width: 45%; float:left;"> ![Binder loading screen](media/binder_loading.gif)<!--
style = "border: 1px solid rgb(var(--color-highlight));"-->
</div>
</div>

**Then**, once you have access to RStudio and you see something like the image below, you'll need to open the sample data for this course.  In the file area to the lower right, you'll see, among multiple choices, the folder called "r\_basics\_visualize\_data".  That's the code for this module!

![RStudio as shown in the cloud platform Binder](media/binder_rstudio.png)<!--
style = "border: 1px solid rgb(var(--color-highlight)); max-width: 800px;"-->


<h3>Option 2: Work on Your Computer</h3>

If you have [R](https://www.r-project.org/) and [RStudio](https://www.rstudio.com/products/rstudio/download/#download) installed already on your local computer, you might be interested in simply downloading our sample code to your computer. Here's how.  Note -- if you've already done this step in another module, you might have the material for this module already!

* In RStudio, open a new project (File, New Project)
* Select Version Control, then Git
* Drop this link into the "Repository URL": https://github.com/arcus/education_r_environment
* Change the "Project directory name" and "Create project as a subdirectory of" boxes to suit your needs (where will this code be stored on your computer?).
* Click to select the "Open in new session" checkbox
* Click "Create Project"
* In the file area to the lower right, you'll see, among multiple choices, the folder called "r\_basics\_visualize\_data".  That's the code for this module!

**Want to watch this process?  Click on the image below to play an animated gif.  It will continue to loop and you can re-start it by clicking again.**

<div style="display:none">@gifPreload</div>

<figure>
  <img src="https://github.com/arcus/education_modules/blob/r_basics_visualize_data/r_basics_visualize_data/media/rstudio_new_project.png?raw=true" height="384" width="512" alt="RStudio can create a new project that gets its contents from a git repository." data-alt="https://github.com/arcus/education_modules/blob/r_basics_visualize_data/r_basics_visualize_data/media/rstudio_new_project.gif?raw=true" style = "border: 1px solid rgb(var(--color-highlight));">

<figcaption style = "font-size: 1em;">Click on the image to play the demo of the above steps!</figcaption>
</figure>

If you already completed this work for a previous module, and it's been a while since you downloaded this project to your computer, you may want to get any new and improved files that have been placed there in the meantime:

* Open your project.
* In the Version Control menu, choose "pull branches".  There are two places to do this, as shown below:

![Git button menu with choices to pull and push branches](media/pull_branches.png)<!-- style = "border: 1px solid rgb(var(--color-highlight))" -->  ![Tools menu with choices to pull and push branches](media/pull_branches_2.png)<!-- style = "border: 1px solid rgb(var(--color-highlight))" -->

<div class = "warning">
If you're pulling branches after having worked in previous modules, you might have made local changes (for example, when you filled in exercise code) that will be overwritten by pulling the latest version.  If you want to save your changes, consider making a copy of any exercise files and naming them something new.  For example, if you have already worked in the `r_basics_transform_data` exercise files, you might want to save your version of `transform.Rmd` to `my_transform.Rmd`.  That way, you can pull down the latest version of code, overwriting `transform.Rmd` while holding on to your changes in the new file.
</div>

## Reproducible Data Analysis and R Markdown

<div style = "align-items: center; display: flex;">

<div style = "margin: 1rem; max-width: 65%; float:left;">
Before we jump into coding, we want to talk about **reproducibility**. One of the most powerful aspects of working in the R environment is that it makes it straightforward to produce **reproducible data analyses**.

Consider the following case study.

In the mid-2000s, researchers at Duke University tried to use microarray gene expression data of tumor cells to predict sensitivity to chemotherapeutic agents. This approach generated a lot of excitement at the time, and the resulting work was published in high-profile journals.

Unfortunately, there were a number of **serious errors** in the data analysis.

Even more unfortunately, patients were enrolled in clinical trials and allocated based on **flawed models**. It's likely that some patients were actually treated not with the chemo they are **most likely** to respond to, but with the chemo that's **least likely to** work.

In the end, 18 papers were retracted, and Duke settled more than 10 lawsuits for an undisclosed amount of money.
</div>
<div style = "margin: 1rem; max-width: 30%; float:left;">
![Journal covers and the number 18](media/duke_journals.png)
</div>
</div>

### Off-By-One

Two biostatisticians at MD Anderson uncovered these mistakes in painstaking work. Let's look at one of the errors they found.

What you see here are the names of are a few of the hundreds of microarray probe sets – each roughly corresponds to a gene – that the Duke investigators reported tp predict sensitivity to 5-fluorouracil. ![ List of codes that are a combination of letters and numbers](media/duke_probes.png)

And here are the probe sets that the MD Anderson team got. You can see that they're not the same.
![List of codes that are a combination of letters and numbers, but the number is one higher than the Duke list](mdanderson_probes.png)

You might notice a pattern: the number of the probe set that Duke reported is always one less than the number of the probe that MD Anderson found when they re-did the analysis.

This is what's called an **off-by-one indexing error** and is what happens when you use a tool like Excel and accidentally miss one row; or you have one dataset that has a header and another one that doesn't.  The result is that all the values in the affected column are shifted by one. This is a simple error to make, but it completely invalidates all downstream results.

### Simple Errors

The off-by-one indexing error was just one of many simple errors the MD Anderson team discovered.

Another type of error that was pervasive in the study was label reversal so that cell lines were labeled sensitive to a drug when they actually were resistant, and vice versa. That type of error can lead to a scenario where a patient gets the chemotherapy that would be predicted to be least beneficial.

Other problems they identified were confounding, inclusion of data from sources that were not reported in the paper, and wrong figure shown.

These are all simple errors – people who make them aren't necessarily incompetent or negligent.

Because these errors are so easy to make and because without good documentation or a reproducible workflow it's hard to catch them, they are also very common.

A key issue in this case study is that the Duke investigators used "point and click" tools like Excel.

This prevented peers and independent investigators from catching errors in the analysis, until it was too late.


![Logo of Microsoft Excel](media/excel_logo.png)

And the Duke case study is only one example where the barrier to reproducibility was that people used graphical user interface "point-and-click" type tools for analyzing large and complicated sets of data. Excel doesn't record user actions and because of this, is fundamentally not reproducible.

## Reproducible Research

Reproducibility doesn't only help people **outside** a study understand how things were done.  They also help the initial conduct of research as well.  Consider the following 3 statements and ask yourself if they sound familiar.

- Can we redo the analysis with this month's data?
- Why do the data in Table 1 not seem to agree with Figure 2?
- Why did I decide to omit these six samples from my analysis?

**Your closest collaborator is you from 6 months ago...**
...  but they don't answer your emails.

Additionally, we've already seen how irreproducibility can cause real harm to human subjects, something we all want to avoid.

### R Markdown

Now that we have convinced you (we hope) that reproducibility is important, how do you undertake a reproducible analysis? One answer to this is **R Markdown**.

R Markdown lets you write computer code mixed in with English (or other human language) narrative annotation that documents the purpose of the code and details about the decisions you made in your analysis.

R Markdown is quickly becoming the standard for reproducible data analysis. A primary aim of this module is to teach you to use R Markdown and to encourage you to start working it into your day to day data workflows.
 ![Logo of R Markdown](media/r_markdown_logo.png)


R Markdown documents are composed of 3 basic types building blocks.

The first is the Header which includes information about the document, such as its title, author, and the desired output format when the document is rendered. A lot of this information is optional so a header can be pretty short, as this one here, or much longer.

The second type of building block is text. Text can include special kinds of marks that add styling, such as for example hashtags that turn a line of text into a header, and others.

The third is code chunks.  Code chunks contain R code that can be executed to output results.

So how do you execute the code in the code chunks? Basically, there are two ways.

The first is to run the code in a single code chunk. And you do this by clicking the green right-pointing triangle on the top right of the chunk. I think it's supposed to look like a “play” symbol.

When you do this ** immediately below the code chunk it will show you the results, in this case some statistics about a normal distribution.

The second way to execute code is to convert the entire R Markdown document into HTML - or another target format, but for now we'll stick to HTML because it's the default and usually what you want. This process of converting R Markdown into a target format is called “rendering” or ”knitting” – the mental model here is that you're knitting together marked up text, code, and results into a nicely formatted document that you can then present or share with others.

** To knit a document, click the button that says “Knit” next to a blue ball of yarn on the top of the Editor pane.

Let's look at this R Markdown document in a little more detail.

Again the first block is the header section. We're telling R Markdown that the title should be “My Markdown Document” and that when the document is rendered, we want to output to be an “html_document”. That's the default. You can see that in the resulting HTML document there's the title “My Markdown Document” in large type letters.

** Here we have some narrative text with marks such as hashtags and asterisks. You can see that having a hashtag at the beginning of a line makes this line a header, and the more hashtags you write, the smaller the header. Also, you can see that, depending on where you write it, with an asterik you can make bulleted lists or text that is italics or bold.

** Then we get to the code chunks. Don't worry about the contents of the code for now - in brief, this code asks R to generate 100 random values and then print out some summary statistics. The knitted document shows us our code **, tidily placed into a gray box to make it visually distinct from the text; and then immediately after, the results of that code after it was executed.

** Here we have one more code chunk, and what this is showing is that (1) in addition to text output, you can also make R create graphical plots, and (2) you can tweak the behavior of a code chunk – note that this code chunk has a chunk option of echo=FALSE, and this tells R that you don't want it to repeat, or “echo” the code in the rendered document.

So let's practice creating an R Markdown document, running a code chunk, and knitting.





Go to File > New File > R Markdown. Click OK.

Run each chunk by clicking    . Note what happens.

Knit the document (         ). Type test and click Save to save the HTML file. Inspect the HTML document



It's your turn again.

Follow the instructions in Your Turn #2 to
- create a new R Mardown document
- run all of the code chunks
- knit the document

When you knit the document, it will ask you for a filename to save to – just enter “test”

We will meet back in 3 minutes to review this exercise together.

// Points to make during live coding:
Header starts with 3 dashes, ends with 3 dashes
Code chunk starts with 3 backticks and r in curly braces, ends with 3 backticks. Editor makes code chunks gray.
Note that we saved test.Rmd (R Markdown file) and test.html (knitted HTML file). You might wonder why you want to deal with two files. Rmd is source code document – makes things reproducible, can share with an analyst; HTML is presentation – share with your boss.
Why is the gray code box missing in the rendered document? echo=FALSEs


Now that we are familiar with how to create R Markdown documents we can begin the process of performing data analysis in R in earnest by importing a clinical data set.

The first step in the data analysis pipeline is to load or ** import the data into your environment, which for the purposes of this course is R.

In today's workshop we will be using a de-identified data set consisting of COVID-19 laboratory test results from CHOP's infectious disease diagnostics lab (IDDL). This data is stored as a CSV file.

So what's a CSV file? CSV stands for comma-separated values.

** A CSV file is a plain text file, which means you can open it in a text editor and look at it.

Here we have a CSV file with the names, medical record numbers, and dates of birth for three fictional “patients”

** This data structure is called rectangular because it falls into rows and columns, where each row has the same # of columns, and each columns has the same # of rows.

** Also note that this particular CSV file has a header row that instead of data, has a descriptor of what kinds of data are found in each column. CSV files often but not always have such a header row.







<div class = "question">
In the box below, write what you think the name of this is (all lowercase, please).

[[histogram]]
[[?]] Hint: this word ends in "gram"

<div class = "answer">
<details><summary>Click to see an explanation of the answer.</summary>

"histogram" is the right answer!  A histogram plots the frequency of something in terms of some other thing (for instance, a time value like days).  In our next section, we're going to build a histogram.
</details>
</div>
</div>

## Recap

To recap what we have covered in this session--

We started by defining and differentiating ** R (the programming language) from ** RStudio (the integrated development environment or editor) and ** R Markdown (the document format we use for reproducible data analysis). Then we explored RStudio and R Markdown.

We then looked at how

Packages extend the functionality of R. Install with install.packages() and load with library().
Functions do stuff. They accept Arguments as input and return an Output. Capture an output in an Object using the assignment operator ( <- ).
Importing Data is the first step of data analysis. Use read_csv() from the tidyverse package to import data stored in a CSV file.



## Additional Resources

<h3>Cheat Sheets</h3>

RStudio the company publishes a number of cheat sheets which come in handy for data analysis.

Relevant to this session, the Data Import cheat sheet helps with importing data from file types similar to CSV but with other delimiters.


### More Data Types

<h3>File Formats</h3>

Not all data is in CSV files, and fortunately R supports a huge number of other file formats, and here are some of the packages that help import or export them:

* Readxl: Microsoft Excel
* Haven: SPSS, Stata, and SAS files
* Googlesheets: Google Sheets
* Rvest: web scraping
* Jsonlite: JSON data and many APIs on the web

![Hexagonal logos of the five packages listed above](media/file_types.png)<!-- style = "max-width:600px;" -->

<h3>Databases</h3>

You can also connect to a large number of **databases** directly in R to pull your data. For example, you can connect to SQL databases including MySQL and Oracle, as well as using APIs (application programming interfaces) for data collection applications like REDCap and websites with API access like PubMed or the New York Times.

![Logos of many different database solutions](media/databases.png)

### Additional Features

<h3>Output Document Options</h3>

<div style = "align-items: center; display: flex;">
In addition to HTML, R Markdown documents can be “knitted” into a number of additional formats including PDF, Microsoft Word, PowerPoint, and even interactive dashboards.
<div style = "margin: 1rem; max-width: 50%; float:left;">
</div>
<div style = "margin: 1rem; max-width: 50%; float:left;">
![R Markdown logo surrounded by the logos of output document options, including HTML5, .pdf, and others.](media/document_output.png)
</div>
</div>

<h3>Language Support</h3>

Finally, in addition to R, R Markdown supports many other programming languages, including Python.

So you can mix code chunks written in R with code chunks written in, say, Python:

<div style = "align-items: center; display: flex;">

<div style = "margin: 1rem; max-width: 50%; float:left;">
![R logo with cartoon snake](media/r_python.png)
</div>
<div style = "margin: 1rem; max-width: 50%; float:left;">

<lia-keep>
<pre>
```{python}
import pandas
covid_testing.info()
```
</pre>
</lia-keep>
</div>
</div>

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22R+Basics+Visualize+Data%22)!

Material for this module was adapted, with permission, from [Stephan Kadauke's R for Clinical Data workshop materials](https://skadauke.github.io/intro-to-r-for-clinicians-chop/).  We owe special thanks to Dr. Kadauke as well as the R User Group at Children's Hospital of Philadelphia for their generosity in sharing these materials.

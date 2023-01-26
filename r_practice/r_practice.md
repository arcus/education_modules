<!--

author:   Meredith Lee
email:    leemc@chop.edu
version:  1.0.0
module_template_version: 3.0.0
language: en
narrator: UK English Female
title: R Practice
comment: Use the basics of R coding, data transformation, and data visualization to work with real data. 
long_description: When learning R for data science, the ultimate goal is to be able to put all of the pieces together to analyze a dataset. This module aims to provide a data science task in order to help learners practice R skills in a real-world context. 
estimated_time: 1 hour

@learning_objectives

After completion of this module, learners will be able to:

- Import a dataset from an online database
- Recode data and change variable types in a dataframe
- Use exploratory data visualization to identify trends in data and generate hypotheses

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# R Practice

<div class = "overview">

## Overview
@comment

**Is this module right for me?:** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites:** Learners should be familiar with [the basics of R coding](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_introduction/r_basics_introduction.md#1), including [data transformation with dplyr](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_transform_data/r_basics_transform_data.md#1) and [data visualization with ggplot2](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/data_visualization_in_ggplot2/data_visualization_in_ggplot2.md#1). Learners should also have access to R, either on their own computer or in the cloud. 

**Learning Objectives**:

@learning_objectives

</div>

## Lesson Preparation

For this module, you'll need access to R, either on your own computer or in the cloud. For details about how to download R, you can take a look at the [preparation section of our R Basics: Introduction module](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_introduction/r_basics_introduction.md#5). If you'd prefer to work in the cloud, [posit.cloud](https://posit.cloud/) is a cloud-based R notebook environment. 

## Topics to Review

- Loading libraries 
- Reading a CSV and creating a data frame
- Editing/recoding data
- Exploratory data visualization

Stretch topics
=====

There are a couple of additional skills that haven't been introduced in a module yet, but that might come in handy solving this data science problem: 

- Correlation matrices
- Heat maps

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Finding correlations and creating heat maps are not topics that you have learned in preceding modules or in other prior learning -- which means you might need to do some searching to figure out how to do them! This is an important step in your development as a programmer and a data scientist, but don't worry if it seems difficult in the beginning; it'll get easier with practice. To start, try googling "R" and "correlations" and see where it takes you.

</div>

## The Data

For this practice module we will be using real, publicly-available cervical cancer data from [UC Irvine's machine learning data repository](http://archive.ics.uci.edu/ml/index.php); you can download those data here: [http://archive.ics.uci.edu/ml/machine-learning-databases/00383/risk_factors_cervical_cancer.csv](http://archive.ics.uci.edu/ml/machine-learning-databases/00383/risk_factors_cervical_cancer.csv). If you have done the [Python Practice Module](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_practice/python_practice.md, this dataset might be familiar! 

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

The second link above will attempt to download a CSV file to your computer-- if you don't want to do that, or if your institution's permissions don't allow it, you can also access the dataset here: [https://archive.ics.uci.edu/ml/datasets/Cervical+cancer+%28Risk+Factors%29](https://archive.ics.uci.edu/ml/datasets/Cervical+cancer+%28Risk+Factors%29). If you want to download the CSV from there, just click the "Data Folder" link at the top of the page. 

</div>

## Practice Problem

According to the UCI Machine Learning database, the Cervical Cancer (Risk Factors) dataset "focuses on the prediction of indicators/diagnosis of cervical cancer. The features cover demographic information, habits, and historic medical records." 
 
Your Task
-----

1. Explore [the Cervical Cancer (Risk Factors) dataset](http://archive.ics.uci.edu/ml/machine-learning-databases/00383/risk_factors_cervical_cancer.csv) and 
2. Use the R skills that you've learned to **develop a hypothesis about some likely risk factors** for a diagnosis of cervical cancer.  

Remember that there are several ways to approach this task; there is no one right answer! So have fun, and good luck!

### Stuck? 

If this practice problem was challenging, [here is a link to an example notebook](https://github.com/arcus/education_r_environment/blob/main/r_practice/r_practice.Rmd) where we go through one possible solution to the practice problem. 

To work with our sample solution, you could do any of the three possibilities below:

* Copy / paste the code from [the link above](https://github.com/arcus/education_r_environment/blob/main/r_practice/r_practice.Rmd) 
  
  * You can use the "Copy" button which looks like two pieces of paper in the menu bar across the top of the file: 
  ![Copy raw contents button](media/copy_raw_contents.png)<!--
style = "border: 1px solid rgb(var(--color-highlight));"-->
  
  * Or you can just use your mouse and highlight all the code, and use the "copy" keyboard shortcut
  * Paste the sample code into your own R Markdown file

* Make a clone of the "education\_r\_environment" repository:
  
  * In RStudio, open a new project (File, New Project)
  * Select Version Control, then Git
  * Drop this link into the "Repository URL": https://github.com/arcus/education_r_environment
  * Change the "Project directory name" and "Create project as a subdirectory of" boxes to suit your needs (where will this code be stored on your computer?).
  * Click to select the "Open in new session" checkbox
  * Click "Create Project"
  * In the file area to the lower right, you'll see, among multiple choices, the folder called "r\_practice". That's the code for this module!

* Use Posit.Cloud:
  
  * [Create a (free!) Posit Cloud account](https://posit.cloud/plans)
  * Open the "education\_r\_environment" project at https://posit.cloud/content/5273350.  That will give you a temporary copy so you can run our code, but not make any changes to it.
  * Click on "Save a Permanent Copy" if you want to save any changes to your version of this code. 
  ![Posit menu bar with "Make Permanent Copy"](media/make_copy.png)<!--
style = "border: 1px solid rgb(var(--color-highlight));"-->


We encourage you to spend some time playing around with the data before you look at the example! And remember, just because your solution doesn't look exactly like the example doesn't mean it's wrong-- there are a variety of ways you might have approached the task we gave you.  

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Feeling overwhelmed? Learning data science in R take time and practice. Don't worry if you feel like you have to go back and look and the modules over and over, or google lots of things-- folks who do this for a living Google things every day! You don't have to memorize everything. Just keep your favorite resources close at hand so you remember what tools you have access to. 

</div>

## Additional Resources

The best way to continue learning R for data science is to **do data science with R**! Here are some sources of publicly-available data that you can download and start practicing with today:

- [Kaggle.com](https://www.kaggle.com/) has a lot datasets to practice with, and even competitions and short courses! 
- [World Bank Data](https://data.worldbank.org/)-- this repository has many global development datasets
- [Data.gov](https://data.gov/)
- And so many more! Try searching "open" or "public" data and see what you can find!

A great way to keep resources close at hand is to use cheat sheets:

- [Posit.co](https://posit.co/) has many cheat sheets available to download, including one for [data transformation with dplyr](https://posit.co/wp-content/uploads/2022/10/data-transformation-1.pdf), [data visualization with ggplot2](https://posit.co/wp-content/uploads/2022/10/data-visualization-1.pdf).

And as always, [R for Data Science](https://r4ds.had.co.nz/) is always a great resource!

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22R+Practice%22)!



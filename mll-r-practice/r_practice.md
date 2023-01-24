<!--

author:   Meredith Lee
email:    leemc@chop.edu
version:  1.0.0
module_template_version: 3.0.0
language: en
narrator: UK English Female
title: R Practice
comment: Use the basics of R coding, data transformation, and data visualization to work with real data. 
long_description: When learning R for data science, the ultimate goal is to be able to put all of the pieces together to analyze a dataset. This module aims to present a data science task in order to help learners practice R skills in a real-world context. 
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

# Python Practice

<div class = "overview">

## Overview
@comment

**Is this module right for me?:** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites:** Learners should be familiar with [the basics of R coding](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_introduction/r_basics_introduction.md#1), including [data transformation with dplyr](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_transform_data/r_basics_transform_data.md#1) and [data transformation with ggplot2](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/data_visualization_in_ggplot2/data_visualization_in_ggplot2.md#1). Learners should also have access to R, either on their own computer or in the cloud. 

**Learning Objectives**:

@learning_objectives

</div>

## Lesson Preparation

For this module, you'll need access to R, either on your own computer or in the cloud. For details about how to download R, you can take a look at the [preparation section of our R Basics: Introduction module](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_introduction/r_basics_introduction.md#5). If you'd prefer to work in the cloud, [posit.cloud](https://posit.cloud/) is a cloud-based R notebook environment. 

## The Data

For this practice module we will be using real, publicly-available cervical cancer data from [UC Irvine's machine learning data repository](http://archive.ics.uci.edu/ml/index.php); you can download those data here: [http://archive.ics.uci.edu/ml/machine-learning-databases/00383/risk_factors_cervical_cancer.csv](http://archive.ics.uci.edu/ml/machine-learning-databases/00383/risk_factors_cervical_cancer.csv). If you have done the Python Practice Module (**link required**), this dataset might be familiar! 

## Topics to Review

- Loading libraries 
- Reading a CSV and creating a data frame
- Editing/recoding data
- Exploratory data visualization

Stretch topics
=====

- Correlations and heat maps

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Finding correlations and creating heat maps are not topics that we have taught you in the preceding modules, but that might come in handy in solving the practice problem-- which means you might need to do some searching to figure out how to do these! This is an important step in your development as a programmer and a data scientist, but don't worry if it seems difficult in the beginning! It'll get easier with practice. To start, try googling "R" and "correlations" and see where it takes you.

</div>

## Practice Problem

According to the UCI Machine Learning database, the Cervical Cancer (Risk Factors) dataset "focuses on the prediction of indicators/diagnosis of cervical cancer. The features cover demographic information, habits, and historic medical records." Your tasks are to explore this dataset ad use the R tools that you've learned so far to develop a hypothesis about some likely risk factors for a diagnosis of cervical cancer.  

Remember that there are several ways to approach this task; there is no one right answer! So have fun, and good luck!

### Stuck? 

If this practice problem was challenging, [here is a link to an example notebook]() where we go through one possible solution to the practice problem. If you'd like to download the R Markdown notebook to work with on your own computer, you can do that in RStudio Cloud. 

We encourage you to spend some time playing around with the data before you look at the example! And remember, just because your solution doesn't look exactly like the example doesn't mean it's wrong-- there are a variety of ways you might have approached the task we gave you.  

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Feeling overwhelmed? Learning data science in Python take time and practice. Don't worry if you feel like you have to go back and look and the modules over and over, or google lots of things-- folks who do this for a living google things every day! You don't have to memorize everything. Just keep your favorite resources close at hand so you remember what tools you have access to. 

</div>



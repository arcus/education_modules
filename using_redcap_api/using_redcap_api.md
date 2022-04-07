<!--
author:   Joy Payton
email:    paytonk@chop.edu
version:  1.0.0
module_template_version: 2.0.0
language: en
narrator: US English Female
title: Using the REDCap API
comment:  REDCap is a research data capture tool used by many researchers in basic, translational, and clinical research efforts.  Learn how to use the REDCap API in this module.
long_description: If your institution provides access to REDCap, this module is right for you.  REDCap is a convenient and powerful way to collect and store research data.  This module will teach you how to interact with the REDCap API, or "Application Programming Interface", which can help you automate your data analysis. This will also help you understand APIs in general and what makes their use so appealing for reproducible research efforts.
estimated_time: 1 hour

@learning_objectives  

After completion of this module, learners will be able to:

- Define what an API is and why it's useful to researchers
- Enable API usage on REDCap projects
- Use the REDCap API to pull data into an R or Python data analysis


@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Using the REDCap API

<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

This module assumes that learners have access to the REDCap application at their institution.  Learners will benefit from having used REDCap in the past, and those with no experience will be asked to watch some training videos on their institution's REDCap home page.  Some experience with either R or Python is necessary to use these languages to interact with the REDCap API, but code will be provided.

**Learning Objectives**

@learning_objectives

</div>


## REDCap

What is REDCap?

### Advantages of REDCap

### Learn More About REDCap at your Institution

### Quiz:

Which of the following are accurate statements about tidy data?

[[X]] An observation is a single thing with measurable characteristics (like a mouse or a city)
[[ ]] Observations should each be in their own column
[[ ]] It's often a good idea to combine related data in a single cell, for instance, by encoding "4 year old female" as 4yf
[[X]] "Height in meters" is an example of a variable.
[[X]] Observations should each be in their own row
[[?]] There are multiple correct answers!
************

<div class = "answer">
An observation is a single thing with measurable characteristics, and each observation should be in its own row.  Variables, on the other hand, are things being measured, like height, color, score, count, and so on.  Variables should each be in their own column.  Values belong in cells, the intersection of rows and columns, and each cell should have one and only one value -- no combining!
</div>

**************

## The REDCap API

### What is an Application Programming Interface (API)?

### Tokens, Keys, Passwords, and other Secrets

### Advantages of APIs

### Quiz:

## Hands-On Practice

### Sample Project

### Enabling the API

### API Token

### API Playground

### R, or Python?

### Quiz:

Which of the following are ways to make this dataset "tidy"?  Check all that apply!

[[X]] move "depression" status into a column instead of using it in a cell combined with other descriptors
[[ ]] remove sex as a variable, since there's no way to detangle it from other variables
[[ ]] ensure that each number has the same number of significant digits after the decimal point
[[X]] make "timepoint" into a new column, with possible values including "pre" and "post"
[[X]] increase the rows so that there are 16 rows representing 16 distinct cohorts
[[?]] There are multiple correct answers!
***************

<div class = "answer">
Depression status and timepoint should each become a column.  In fact, we suggest the following columns:

</div>

**************

## Recap

## Additional Resources

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Using+the+REDCap+API%22)!

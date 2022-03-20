<!--
author:   Joy Payton
email:    paytonk@chop.edu
version:  1.0.0
module_template_version: 2.0.0
language: en
narrator: US English Female
title: Tidy Data
comment:  Tidy is a technical term in data analysis and describes an optimal way for organizing data that will be analyzed computationally.
long_description: Are you concerned about how to organize your data so that it's easier to work with in a computational solution like R, Python, or other statistical software?  This module will explain the concept of "tidy data", which will help make analysis and data reuse a bit simpler.
estimated_time: 45 minutes

@learning_objectives  

After completion of this module, learners will be able to:

- Describe the three tenets of tidy data
- Describe how messy data could be transformed into tidy data
- Describe the three tenets of tidy analysis


@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Tidy Data

<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

Experience working with rectangular data (data in rows and columns) will be helpful.  For example, experience working in Excel, Google Sheets, or other software that helps organize data into rows and columns is sufficient expertise to take this module.

**Learning Objectives**

@learning_objectives

For help articulating learning objectives, see [this guide to learning objectives, including lots of example verbs](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/).

</div>


## Tidy Data

What do we mean by "tidy" data frame?

A data set can take on a lot of different shapes with different styles of organizing data. The one method or shape that is best suited for data analysis is known as "tidy".

![Table with rows and columns.  The data is not visible, although headers are, and include mrn, gender, `test_id`, and result. In each row and column, an arrow spans the entire row or entire column.](media/tidy_data.png)<!-- style = "max-width: 400px;" -->

A data set is tidy if:

* Each variable is in its own column
* Each observation is in its own row, and
* Each value is in its own cell.

The opposite of "tidy" is often called "messy." Often, much of the data analysis work is to convert "messy" data into "tidy data." But for now, fortunately for us, the `covid_testing` data set is tidy already.

Here's one simple example of tidy versus messy. If a column is called "name" and includes first names and last names, that's messy.  It can be difficult to extract just the first names or just the last names, since some people have more than one word forming their first name (José María, Leigh Ann) and some people have more than one word forming their last name (de la Cruz, Bonham Carter).  A "tidy" approach would be to have one column for first names and one column for last names.

[Hadley Wickham](https://www.jstatsoft.org/article/view/v059i10) (a statistician who is prominent in the R world -- you'll likely become familiar with his name as you continue your R journey) suggests that there are five common problems that occur to make data "messy":

* Column headers are values, not variable names.
* Multiple variables are stored in one column.
* Variables are stored in both rows and columns.
* Multiple types of observational units are stored in the same table.
* A single observational unit is stored in multiple tables.

To see a "messy" data frame and its "tidy" alternative, see [a brief 2018 article](https://education.arcus.chop.edu/tidyverse/) for a brief read, or, if you want a deeper dive,  there really isn't a better article than [Hadley Wickham's classic work](https://www.jstatsoft.org/article/view/v059i10).

### Quiz: Tidy Data

Let's see what you remember about tidy datasets!  Take a look at the sample table provided below.  It's similar to what you might see in a publication, and it's in a great format for humans... but it's not tidy enough to work with easily in a computational way.  This table shows the results of the "QPT" psychometric (something we made up) and shares pre- and post-treatment means and standard deviations for different kinds of research cohorts.

<table border="1" cellpadding="0.5em" cellspacing="0"><tbody><tr><td style="padding: 0.5em;">
            </td>
            <td colspan="2" style="padding: 0.5em;">
            <p>Mean QPT - pretreatment</p>
            </td>
            <td colspan="2" style="padding: 0.5em;">
            <p>SD QPT -- pretreatment</p>
            </td>
            <td colspan="2" style="padding: 0.5em;">
            <p>Mean QPT - post-treatment</p>
            </td>
            <td colspan="2" style="padding: 0.5em;">
            <p>SD QPT -- post-treatment</p>
            </td>
        </tr><tr><td style="padding: 0.5em;">
            </td>
            <td style="padding: 0.5em;">
            <p>m</p>
            </td>
            <td style="padding: 0.5em;">
            <p>f</p>
            </td>
            <td style="padding: 0.5em;">
            <p>m</p>
            </td>
            <td style="padding: 0.5em;">
            <p>f</p>
            </td>
            <td style="padding: 0.5em;">
            <p>m</p>
            </td>
            <td style="padding: 0.5em;">
            <p>f</p>
            </td>
            <td style="padding: 0.5em;">
            <p>m</p>
            </td>
            <td style="padding: 0.5em;">
            <p>f</p>
            </td>
        </tr><tr><td style="padding: 0.5em;">
            <p>Depression alone</p>
            <p>(n=9m, 7f)</p>
            </td>
            <td style="padding: 0.5em;">
            <p>122</p>
            </td>
            <td style="padding: 0.5em;">
            <p>137</p>
            </td>
            <td style="padding: 0.5em;">
            <p>28.1</p>
            </td>
            <td style="padding: 0.5em;">
            <p>27.0</p>
            </td>
            <td style="padding: 0.5em;">
            <p>109</p>
            </td>
            <td style="padding: 0.5em;">
            <p>140</p>
            </td>
            <td style="padding: 0.5em;">
            <p>26.0</p>
            </td>
            <td style="padding: 0.5em;">
            <p>39.5</p>
            </td>
        </tr><tr><td style="padding: 0.5em;">
            <p>Depression with Anxiety (n=12m,8f)</p>
            </td>
            <td style="padding: 0.5em;">
            <p>130</p>
            </td>
            <td style="padding: 0.5em;">
            <p>145</p>
            </td>
            <td style="padding: 0.5em;">
            <p>25.0</p>
            </td>
            <td style="padding: 0.5em;">
            <p>19.8</p>
            </td>
            <td style="padding: 0.5em;">
            <p>103</p>
            </td>
            <td style="padding: 0.5em;">
            <p>142</p>
            </td>
            <td style="padding: 0.5em;">
            <p>24.9</p>
            </td>
            <td style="padding: 0.5em;">
            <p>40.1</p>
            </td>
        </tr><tr><td style="padding: 0.5em;">
            <p>Controls / Neither Depression nor Anxiety (n=10m, 10f)</p>
            </td>
            <td style="padding: 0.5em;">
            <p>107</p>
            </td>
            <td style="padding: 0.5em;">
            <p>110</p>
            </td>
            <td style="padding: 0.5em;">
            <p>15.8</p>
            </td>
            <td style="padding: 0.5em;">
            <p>13.9</p>
            </td>
            <td style="padding: 0.5em;">
            <p>88</p>
            </td>
            <td style="padding: 0.5em;">
            <p>95</p>
            </td>
            <td style="padding: 0.5em;">
            <p>21.8</p>
            </td>
            <td style="padding: 0.5em;">
            <p>20.6</p>
            </td>
        </tr><tr><td style="padding: 0.5em;">
            <p>Anxiety Alone (n=13m, 15f)</p>
            </td>
            <td style="padding: 0.5em;">
            <p>124</p>
            </td>
            <td style="padding: 0.5em;">
            <p>119</p>
            </td>
            <td style="padding: 0.5em;">
            <p>20.7</p>
            </td>
            <td style="padding: 0.5em;">
            <p>18.3</p>
            </td>
            <td style="padding: 0.5em;">
            <p>100</p>
            </td>
            <td style="padding: 0.5em;">
            <p>110</p>
            </td>
            <td style="padding: 0.5em;">
            <p>24.2</p>
            </td>
            <td style="padding: 0.5em;">
            <p>20.5</p>
            </td>
        </tr></tbody></table>

Which of the following are ways to make this dataset "tidy"?  Check all that apply!

[[X]] move "depression" status into a column instead of using it in a cell combined with other descriptors
[[ ]] remove sex as a variable, since there's no way to detangle it from other variables
[[ ]] ensure that each number has the same number of significant digits after the decimal point
[[X]] make "timepoint" into a new column, with possible values including "pre" and "post"
[[X]] increase the rows so that there are 16 rows representing 16 distinct cohorts
[[?]] There are multiple correct answers!
<lia-keep>
<div class = "answer">
</lia-keep>
<details><summary>Click to see an explanation of the answer.</summary>

Depression status and timepoint should each become a column.  In fact, we suggest the following columns:

* Depression +/- dx
* Anxiety +/- dx
* Sex
* Timepoint (pre- vs post- treatment)
* Mean QPT value
* SD QPT value
* n (count of participants in this group)

There's no need to remove the sex variable, and the numerical values don't necessarily need to have the same number of significant digits to be considered "tidy".  Here's one way to make the table above into a tidy dataset ready for computational analysis:

| Depression status | Anxiety status | Sex | Count | Timepoint | Mean QPT | SD QPT |
| --- | --- | --- | --- | --- | --- | --- |
| pos | pos | m | 12 | pre | 130 | 25 |
| pos | pos | f | 8 | pre | 145 | 19.8 |
| pos | pos | m | 12 | post | 103 | 24.9 |
| pos | pos | f | 8 | post | 142 | 40.1 |
| pos | neg | m | 9 | pre | 122 | 28.1 |
| pos | neg | f | 7 | pre | 137 | 27.0 |
| pos | neg | m | 9 | post | 109 | 26.0 |
| pos | neg | f | 7 | post | 140 | 39.5 |
| neg | pos | m | 13 | pre | 124 | 20.7 |
| neg | pos | f | 15 | pre | 119 | 18.3 |
| neg | pos | m | 13 | post | 100 | 24.2 |
| neg | pos | f | 15 | post | 110 | 20.5 |
| neg | neg | m | 10 | pre | 107 | 15.8 |
| neg | neg | f | 10 | pre | 110 | 13.9 |
| neg | neg | m | 10 | post | 88 | 21.8 |
| neg | neg | f | 10 | post | 95 | 20.6 |

</div>

## The Tidyverse

<div style = "align-items: center; display: flex;">
<div style = "margin: 1rem; max-width: 75%; float:left;">
To import our CSV data, we need some additional data analysis tools.  In this course, we will be leveraging the **tidyverse**.

The tidyverse is a set of tools that has become the de facto standard for doing data science with R.  It relies on the use of "tidy" data and "tidy" data analysis techniques.
</div>
<div style = "margin: 1rem; max-width: 25%; float:left;">
![""](media/tidyverse_logo.png)<!-- style = "max-width:300px;" -->
</div>
</div>

The basic tenets of "tidy" data analysis include:

* Data should be organized in a consistent, standardized way. Each row is an observation, and each column is a variable. This is a very common way to organize data in a spreadsheet and might sound familiar from how you may already organize data in tools like Excel.
* Programming code that acts on the data should be consistent, concise, and sound like human language as much as possible.
* Each data analysis can be broken down into a series of atomic steps, such as "select this column" or "arrange the data by the values in that column". An arbitrarily complex data analysis can be broken down as a pipeline of atomic steps.


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

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Tidy+Data%22)!

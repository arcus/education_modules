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

</div>


## Data Shape

What do we mean by "tidy" data?

To begin with, we're talking specifically about **"rectangular" data**.  Rectangular data (or "tabular" data, from the word "table") has rows and columns.  This is a very typical kind of data for many disciplines, but it's not the only data out there.  Here's a few examples of data that are incredibly important but are not rectangular / tabular:

* Wave form data, such as electrocardiogram data
* Recordings of audio and/or video, such as videorecordings of babies at play
* Text used in textual analysis or natural language processing (NLP), such as clinical notes or the text of Senate bills
* Genomic data such as FASTQ or BAM files

Rectangular data is by no means the only data that matters to biomedical researchers.  This module, however, is limited in scope to only rectangular data.  Here are some common examples of rectangular data:

* Demographic data about patients stored in an electronic health record, in which each row represents a patient, and each column stores a specific demographic fact, such as the date of birth.
* Biosample data in a lab management system, in which each row represents a specific sample and each column represents information about what the sample is and how and when it was obtained.
* Questionnaire data in which each row represents a test taker, with one column for the subject id, one column for the date and time of administration, and each column thereafter representing a question which is answered on a Likert scale (say, from 1-5).

You can probably come up with many examples of rectangular data in your own research.  If you've ever worked with data in rows and columns, as in a .csv file, Excel spreadsheet, or Google Sheet, you know what rectangular data looks like.

### Data Organization

A rectangular data set can take on a lot of different rectangular shapes with different styles of organizing data. Some disciplines have specific types of summary tables, for example, that customarily appear in published manuscripts.  The one method or shape that is best suited for data analysis is known as "tidy".

A data set is tidy, [according to Hadley Wickham and Garrett Grolemund](https://r4ds.had.co.nz/tidy-data.html#tidy-data-1), if:

* Each variable is in its own column
* Each observation is in its own row, and
* Each value is in its own cell

The words "variable", "observation", and "value" are common words to researchers, but let's look closely at them regardless.

* A *variable* is a characteristic being measured, like

  - weight in grams
  - amount of rain in inches
  - homeroom paint color
  - whether a subject has a history of pulmonary embolism

* Each *observation* (thing with measurable characteristics) is in its own row, such as:

  - individual newborn wombat
  - specific day of history
  - elementary school class
  - individual human subject

* Each *value* (a number or category or word that provides the measurement) is in its own cell

  - an integer
  - a decimal numbers
  - a category like "blue", "green", or "yellow"
  - a True/False value

The three rules of tidy data may seem to apply to almost every rectangular data set, but these three requirements are more rigorous than they appear at first glance.  

<h4>Variables in Columns</h4>

For example, is "blood pressure" a single variable?  It consists of two numerical values representing arterial pressure at two different stages in the heart's cycle of pumping blood.  Maybe we should think about that as two measurements, each with its own column.

What about name?  Well, in most cultures, names consist of a family name (in the U.S., the last name or names) and a given name or names.  

Giving each variable, each piece of data that you're measuring, its own column, requires some forethought.  It's not always clear what a single, atomic measurement is, and it can depend on context.  

<h4>Observations in Rows</h4>

If we think about "observation", that can also be a bit tricky.  Do measurements of a single human subject constitute a single observation?  What if the measurements are taken over the span of 30 years?  Is it better to say that an observation is a single human on a single day?  A single hospital encounter?  Knowing whether data is tidy in terms of its rows can be complex.

<h4>Values in Cells</h4>

What about cells?  Is it at least easy to tell if each value is in its own cell?  Well, sometimes.  But consider the case where a mouse identification code is composed of a few letters that indicate its genetic lineage, a number that represents where it was bred, and another series of letters and numbers indicating where it was housed and its type of diet.  A single identifier can hold lots of information.  Also, if you've ever used Excel, you might have used text colors or highlighting to indicate values that seem surprising or possibly mistaken.  For example, a gestational age in weeks of 50 that's in a bright red color might be two actual values: the recorded value of gestational age and a marker that points out its data quality or trustworthiness.

### Data Collection

The opposite of "tidy" is often called "messy." That isn't intended to be pejorative, just descriptive.  We often start with messy data, and as we've described, it's not always obvious what the correct "tidy" approach is. It's often said that **around 80% of the time we spend in data analysis** consists of cleaning up and rearranging messy data and getting it in a format that is helpful for analysis.  That can be surprising to people who are beginning to learn data analysis, and it indicates why it's so important to think about how data is structured long before trying to perform statistical tests or creating figures for manuscripts.  Even well-structured, tidy data often has to be reshaped for specific purposes, and it's much more complicated when you add messy data into the mix.

It's much easier to begin with a tidy structure when data collection begins, rather than tidying up messy data later.  Here's one simple example of that. If a column is called "name" and includes first names and last names, that's messy.  It can be difficult to extract just the first names or just the last names, since some people have more than one word forming their first name (José María, Leigh Ann) and some people have more than one word forming their last name (de la Cruz, Bonham Carter).  If you know your subjects or patients well, you might be able to use your knowledge of their families or cultures to make a row-by-row separation, but what if you have 500 subjects? Fifty thousand subjects?

A "tidy" approach would be to begin data collection with, at the minimum, one column for first names and one column for last names.  In case you do need the entire name (for example, to address an envelope), remember that it's much easier to re-unite two or more fields that are stored separately than to try to define the rules of separating tangled-up data.  

<div class = "hint">
This point is crucial enough that we want to make it stand out:

**Uniting values is simpler than separating them.**

It's impossible to tease out individual grades from an average, but if you have the individual grades, it's straightforward to calculate the average.  Names from two columns can be united by adding a space between them.  Values from a "systolic" and "diastolic" column can be united with a slash between them.  It is better to err on the side of being overly careful in separating out variables.

</div>

Another mistake that commonly occurs in human subjects research is the collection of race data with an assumption that a single value adequately captures race, such as "Asian", "Black", and so forth.  If a subject identifies with multiple races, "multiracial" could be added, for example.  But what if you want to study a genetic variant that occurs disproportionately in people of sub-sarahan African descent, and you're interested in all subjects with Black racial heritage, regardless of whether they identify with other races as well?  "Multiracial" does not answer your question about race, and unless you can track down your subject, there's no way to disentangle the wealth of information in the word "multiracial".

<div class = "warning">
An aside about race: in addition to making for more difficult use of race data, collecting data as a single value does not comply with federal standards.  Human subjects (or their representatives) should be able to endorse any race they identify as their own.  Therefore, it's much more helpful to begin right away with a True / False endorsement column for each race, so that you can identify easily who fits into various categories based on particular race identification, counts, or specific combinations:

* White only
* Indigenous and one other race
* Non white, single race
* Number of races 3 or higher
* etc.

An additional, important question that can be a source of disagreement in demographic and disparity research is what specific groups constitute races that can be endorsed.
</div>

## Sources of Messy Data

Hadley Wickham, one of the authors mentioned in the last section, suggests in his [landmark work on tidy data](https://www.jstatsoft.org/article/view/v059i10) that there are five common problems that occur to make data "messy":

* Column headers are values, not variable names.
* Multiple variables are stored in one column.
* Variables are stored in both rows and columns.
* Multiple types of observational units are stored in the same table.
* A single observational unit is stored in multiple tables.

Let's take a look at each of these problems in turn.

### Column Headers as Values

Let's consider an example from section 3.1 of [Hadley's article](https://www.jstatsoft.org/index.php/jss/article/view/v059i10/772).  

<div class = "hint"> Note that in the world of R users, Hadley Wickham is considered such a singularly important and yet friendly figure that he is often referred to, simply, as "Hadley".
</div>

| religion | <lia-keep><$10k</lia-keep> | <lia-keep>$10–20k</lia-keep> | <lia-keep>$20–30k</lia-keep> | <lia-keep>$30–40k</lia-keep> | <lia-keep>$40–50k</lia-keep> | <lia-keep>$50–75k</lia-keep> |
| -------- | ----- | ------- | ------- | ------- | ------- | ------- |
| Agnostic | 27 | 34 | 60 | 81 | 76 | 137 |
| Atheist | 12 | 27 | 37 | 52 | 35 | 70 |
| Buddhist | 27 | 21 | 30 | 34 | 33 | 58 |
| Catholic | 418 | 617 | 732 | 670 | 638 | 1116 |
| Don't know/refused | 15 | 14 | 15 | 11 | 10 | 35 |
| Evangelical Prot | 575 | 869 | 1064 | 982 | 881 | 1486 |
| Hindu | 1 | 9 | 7 | 9 | 11 | 34 |
| Historically Black Prot | 228 | 244 | 236 | 238 | 197 | 223 |
| Jehovah's Witness | 20 | 27 | 24 | 24 | 21 | 30 |
| Jewish | 19 | 19 | 25 | 25 | 30 | 95 |

The column headers in this table, taken from Pew Forum, contain values -- income values.  This table is readable for humans, and takes advantage of horizontal space on a page.  It makes sense that it would appear in a report for human consumption.  This data is "messy", however, because it violates one of the important rules about tidy data.

While humans can make sense of this data, remember that computers must be told in sometimes agonizing detail what to do.  If we were to ask "which is the largest group?" using the table above, we'd have to say (in code, of course) something along the lines of "look inside each row, at columns 2-7, and take the largest value of all of those cells, and then take the value of the first column of the row with that largest-valued cell, and the column header of that cell, and that's your group".  

What would a tidy format look like?  Consider this, which is the start of a tidy table:

| religion | income | freq |
| -------- | ------ | ---- |
| Agnostic | <lia-keep><$10k</lia-keep> | 27 |
| Agnostic | $10–20k | 34 |
| Agnostic | $20–30k | 60 |
| Agnostic | $30–40k | 81 |
| Agnostic | $40–50k | 76 |
| Agnostic | $50–75k | 137 |
| Agnostic | $75–100k | 122 |
| Agnostic | $100–150k | 109 |
| Agnostic | <lia-keep>>150k</lia-keep> | 84 |
| Agnostic | Don't know/refused | 96 |

You can tell that this table would be quite tall and narrow, not the most lovely on a journal page, but for computational purposes, it's more direct to find the largest group: "look in the 'freq' column, and find the largest number, then the two cells to the left of that value give the group identity."

Again, the "messy" table isn't bad per se, but it's optimized for "looks good to people when viewed on a journal page", not optimized for computation.

### Multiple Variables in One Column

In section 3.2 of his article, Hadley shows data from the World Health Organization.  In this dataset, related to tuberculosis, there's a column named, simply "column".  This "column" is a hybrid: it contains sex (m or f) and age (0-14 years, 15-24 years, and so on, to 65+).  It is in a condensed form that we would judge "messy".  See a shortened version of this messy data below:


| country | year | column | cases |
| ------  | ---- | -----  | ----- |
| AD | 2000 | m014 | 0 |
| AD | 2000 | m1524 | 0 |
| AD | 2000 | m2534 | 1 |
| AD | 2000 | m3544 | 0 |
| AD | 2000 | m4554 | 0 |
| AD | 2000 | m5564 | 0 |
| AE | 2000 | f014 | 3 |

Again, consider the difficulty of asking the question "what's the sum of all the cases for 15-24 year olds?".  In the "messy" version, you'd have to start off by identifying which cases are for 15-24 year olds.  In English, you'd say something like "look for 1524 inside the value of 'column'", and then you'd have to figure out how to write that in code, using some sort of string comparison.  That's not trivial code, and it requires you to understand the pattern of a letter followed by two, three, or four numbers, and understand where one number in the range given ends and another begins.  For example, you can't just say "put a dash after the first two numbers" to indicate the range.  That would mean 014 would be read as the range 01-4.  While you as a human might be able to make quick work of intepreting the data, what's happening cognitively is actually rather complex and hard to translate to computer code.

In the "tidy" version proposed below, you can begin much more simply: "find all the rows with a value of 15-24 in 'age'".  Computationally, finding an exact match is very simple, when compared to the complex pattern interpretation that would be required in the messy version of the data. Additionally, we would argue that the data below is much more "self documenting".  If you stumbled across this data with no additional information or codebook, it would be much more intuitive to have separate columns marked "sex" and "age", and you'd almost certainly interpret this data correctly.


| country | year | sex | age | cases |
| ------  | ---- | --- | --- | ----- |
| AD | 2000 | m | 0–14 | 0 |
| AD | 2000 | m | 15–24 | 0 |
| AD | 2000 | m | 25–34 | 1 |
| AD | 2000 | m | 35–44 | 0 |
| AD | 2000 | m | 45–54 | 0 |
| AD | 2000 | m | 55–64 | 0 |
| AE | 2000 | f | 0-14 | 3 |



### Variables Stored in Both Rows and Columns

This kind of messy data is exceptionally messy!

The table below is an example of data in which values are stored not in cells but:

* in columns (such as day of the month d1, d2 ... d31)
* in rows (tmin and tmax indicating what's measured, the minimum or maximum temperature)

id year month element d1 d2 d3 d4 d5 d6 d7 d8
MX17004 2010 1 tmax — — — — — — — —
MX17004 2010 1 tmin — — — — — — — —
MX17004 2010 2 tmax — 27.3 24.1 — — — — —
MX17004 2010 2 tmin — 14.4 14.4 — — — — —
MX17004 2010 3 tmax — — — — 32.1 — — —
MX17004 2010 3 tmin — — — — 14.2 — — —
MX17004 2010 4 tmax — — — — — — — —
MX17004 2010 4 tmin — — — — — — — —
MX17004 2010 5 tmax — — — — — — — —
MX17004 2010 5 tmin — — — — — — — —



To see a "messy" data frame and its "tidy" alternative, see [a brief 2018 article](https://education.arcus.chop.edu/tidyverse/) for a brief read, or, if you want a deeper dive,  there really isn't a better article than [Hadley Wickham's classic work].

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

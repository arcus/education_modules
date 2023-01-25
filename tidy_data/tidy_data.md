<!--
author:   Joy Payton
email:    paytonk@chop.edu
version:  1.1.0
module_template_version: 3.0.0
language: en
narrator: US English Female
title: Tidy Data
comment:  Tidy is a technical term in data analysis and describes an optimal way for organizing data that will be analyzed computationally.
long_description: Are you concerned about how to organize your data so that it's easier to work with in a computational solution like R, Python, or other statistical software?  This module will explain the concept of "tidy data", which will help make analysis and data reuse a bit simpler.
estimated_time: 45 minutes

@learning_objectives  

After completion of this module, learners will be able to:

- Describe the three characteristics of tidy data
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

To begin with, we're talking specifically about **"rectangular" data**.  Rectangular data (or **"tabular"** data, from the word "table") has rows and columns.  This is a very typical kind of data for many disciplines, but it's not the only data out there.  Here are a few examples of data that are incredibly important but are not rectangular / tabular:

* Wave form data, such as electrocardiogram data
* Recordings of audio and/or video, such as videorecordings of babies at play
* Text used in textual analysis or natural language processing (NLP), such as clinical notes or the text of Senate bills
* Genomic data such as FASTQ or BAM files
* Image data like photos of skin lesions

Rectangular data is by no means the only data that matters to biomedical researchers -- we could have added many more bullet points above describing non-rectangular data that is critical for our research.  This module, however, is limited in scope to **only rectangular data**.  Here are some common examples of rectangular data:

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

<div class = "history">
<b style="color: rgb(var(--color-highlight));">Historical context</b><br>

In a [previous work by Hadley Wickham](https://www.jstatsoft.org/article/view/v059i10), a different third characteristic appears, and we think it's useful to mention here as another consideration.  This original third characteristic, however, is less critical to success than the three mentioned above, and we would argue it has been supplanted by the one listed above.  Still, it's something to keep in mind.  We'll touch on it a bit later in the module.

* Each observational unit (topic) forms its own table
</div>

The words "variable", "observation", and "value" are common words to researchers, but let's look closely at them regardless.

* A **variable** is a characteristic being measured, like

  - weight in grams
  - amount of rain in inches
  - homeroom paint color
  - whether a subject has a history of pulmonary embolism

* Each **observation** (thing with measurable characteristics) is in its own row, such as:

  - individual newborn wombat
  - specific day of history
  - elementary school class
  - individual human subject

* Each **value** (a number or category or word that provides the measurement) is in its own cell and could be something like:

  - an integer
  - a decimal number
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

### Start at Data Collection

The opposite of "tidy" is often called "messy." That isn't intended to be pejorative, just descriptive.  We often start with messy data, and as we've described, it's not always obvious what the correct "tidy" approach is. It's often said that **around 80% of the time we spend in data analysis** consists of cleaning up and rearranging messy data and getting it in a format that is helpful for analysis.  That can be surprising to people who are beginning to learn data analysis, and it indicates why it's so important to think about how data is structured long before trying to perform statistical tests or creating figures for manuscripts.  Even well-structured, tidy data often has to be reshaped for specific purposes, and it's much more complicated when you add messy data into the mix.

It's much easier to begin with a tidy structure when **data collection** begins, rather than tidying up messy data later.  Here's one simple example of that. If a column is called "name" and includes first names and last names, that's messy.  It can be difficult to extract just the first names or just the last names, since some people have more than one word forming their first name (José María, Leigh Ann) and some people have more than one word forming their last name (de la Cruz, Bonham Carter).  If you know your subjects or patients well, you might be able to use your knowledge of their families or cultures to make a row-by-row separation, but what if you have 500 subjects? Fifty thousand subjects?

A "tidy" approach would be to begin data collection with, at the minimum, one column for first names and one column for last names.  In case you do need the entire name (for example, to address an envelope), remember that it's much easier to re-unite two or more fields that are stored separately than to try to define the rules of separating tangled-up data.  

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

This point is crucial enough that we want to make it stand out:

**Uniting values is simpler than separating them.**

It's impossible to tease out individual grades from an average, but if you have the individual grades, it's straightforward to calculate the average.  Names from two columns can be united by adding a space between them.  Values from a "systolic" and "diastolic" column can be united with a slash between them.  It is better to err on the side of being overly careful in separating out variables.

</div>

Another mistake that commonly occurs in human subjects research is the collection of race data with an assumption that a single value adequately captures race, such as "Asian", "Black", and so forth.  If a subject identifies with multiple races, "multiracial" could be added, for example.  But what if you want to study a genetic variant that occurs disproportionately in people of sub-sarahan African descent, and you're interested in all subjects with Black racial heritage, regardless of whether they identify with other races as well?  "Multiracial" does not answer your question about race, and unless you can track down your subject, there's no way to disentangle the wealth of information in the word "multiracial".

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

An aside about race: in addition to making for more difficult use of race data, collecting data as a single value does not comply with federal standards.  Human subjects (or their representatives) should be able to endorse any race they identify as their own.  Therefore, it's much more helpful to begin right away with a True / False endorsement column for each race, so that you can identify easily who fits into various categories based on particular race identification, counts, or specific combinations:

* White only
* Indigenous and one other race
* Non white, single race
* Number of races 3 or higher
* etc.

An additional, important question that can be a source of disagreement in demographic and disparity research is what specific groups constitute races that can be endorsed.

</div>

### Quiz: Three Characteristics of Tidy Data


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


## Sources of Messy Data

Hadley Wickham, one of the authors mentioned in the last section, suggests in his [landmark work on tidy data](https://www.jstatsoft.org/article/view/v059i10) that there are five common problems that occur to make data "messy":

* Column headers are values, not variable names.
* Multiple variables are stored in one column.
* Variables are stored in both rows and columns.
* Multiple types of observational units are stored in the same table.
* A single observational unit is stored in multiple tables.

Let's take a look at each of these problems in turn.

<div class = "history">
<b style="color: rgb(var(--color-highlight));">Historical context</b><br>

*Tidy Data* was published in 2014, and covers both the concepts around tidy data as well as the then state of the art code solutions in R for data reshaping.  In this module, we're not going to delve into the code examples provided by the article, for two reasons:

* This module is intended to be code-free, making it useful for users of any programming language or none at all (this module can be useful just in terms of setting up data collection instruments well)
* Since 2014, Hadley Wickham and others have developed new methods for data tidying

So, if you choose to [read along in the article](https://www.jstatsoft.org/article/view/v059i10), concentrate on the principles, not the implementation details or code jargon.

</div>

### Column Headers as Values

Let's consider an example from section 3.1 of [Hadley's article](https://www.jstatsoft.org/index.php/jss/article/view/v059i10/772).  The column headers in this table, taken from Pew Forum, contain values -- income values.  This table is readable for humans, and takes advantage of horizontal space on a page.  It makes sense that it would appear in a report for human consumption.  This data is messy, however, because it violates one of the important rules about tidy data.

<div class = "cool-fact">
<b style="color: rgb(var(--color-highlight));">Did you know?</b><br>

Note that in the world of R users, Hadley Wickham is considered such a singularly important and yet friendly figure that he is often referred to simply as "Hadley".

</div>

<!-- data-type="none" -->
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


While humans can make sense of this data, remember that computers must be told in sometimes agonizing detail what to do.  If we were to ask "which is the largest group?" using the table above, we'd have to say (in code, of course) something along the lines of "look inside each row, at columns 2-7, and take the largest value of all of those cells, and then take the value of the first column of the row with that largest-valued cell, and the column header of that cell, and that's your group".

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

![Rubber duck.](media/rubber_duck.png)<!-- style = "max-width: 200px;" -->

Thinking in computer-ese, giving very detailed instruction, is a kind of **algorithmic thinking**.  An **algorithm** is simply a well-specified process that solves a problem.  It takes practice to think like a computer instead of like a person, and one of the fun things that many programmers like to do to help this process along is called "rubber duck debugging".  This involves explaining to, yes, a rubber duck (or other friendly yet not very smart collaborator, like your cat) exactly what you're trying to do and how to get there, following detailed rules.  It may seem silly, but give it a try!

<figcaption style = "font-size: 0.8em;">Image courtesy Steve Webel, https://www.flickr.com/photos/webel/306290032 </figcaption>

</div>

What would a tidy format look like?  Consider this, which is the start of a tidy table.  In the interest of space, only the first handful of rows are shown.

<!-- data-type="none" -->
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

You can tell that this table would be quite tall and narrow, and not the most lovely on a journal page.  However, for computational purposes, this table layout makes it much simpler to find the largest group: "look in the 'freq' column, and find the largest number, then the two cells to the left of that value give the group identity."

Again, the messy table isn't bad *per se*, but it's optimized for "looks good to people when viewed on a journal page", not optimized for computation.

### Multiple Variables in One Column

In section 3.2 of his article, Hadley shows data from the World Health Organization.  In this dataset, related to tuberculosis, there's a column named, simply "column".  This is not original WHO data, but represents an interim step in transforming the original data to a more tidy form.  This interim step (called "molten" data) has made some important improvements in the data, but more work needs to be done. The column entitled "column" is hybrid: it contains sex (m or f) and age (0-14 years, 15-24 years, and so on, to 65+).  It is in a condensed form that we would judge "messy".  See a shortened version of this messy data below:

<!-- data-type="none" -->
| country | year | column | cases |
| ------  | ---- | -----  | ----- |
| AD | 2000 | m014 | 0 |
| AD | 2000 | m1524 | 0 |
| AD | 2000 | m2534 | 1 |
| AD | 2000 | m3544 | 0 |
| AD | 2000 | m4554 | 0 |
| AD | 2000 | m5564 | 0 |
| AE | 2000 | f014 | 3 |

Again, consider the difficulty of asking the question "what's the sum of all the cases for 15-24 year olds?".  In the messy version, you'd have to start off by identifying which cases are for 15-24 year olds.  

In English, you'd say something like "look for 1524 inside the value of 'column'", and then you'd have to figure out how to write that in code, using some sort of string comparison.  That's not trivial code, and it requires you to understand the pattern of a letter followed by two, three, or four numbers, and understand where one number in the range given ends and another begins.  For example, you can't just say "put a dash after the first two numbers" to indicate the range.  That would mean 014 would be read as the range 01-4.  

While you as a **human** might be able to make quick work of intepreting the data, what's happening cognitively is actually rather complex and hard to translate to **computer code**.

In the "tidy" version proposed below, you can begin much more simply: "find all the rows with a value of 15-24 in 'age'".  Computationally, finding an exact match is very simple, when compared to the complex pattern interpretation that would be required in the messy version of the data.

Additionally, we would argue that the data below is much more "self documenting".  If you stumbled across this data with no additional information or codebook, it would be much more intuitive to have separate columns marked "sex" and "age", and you'd almost certainly interpret this data correctly.

<!-- data-type="none" -->
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

The weather data below (note that only a handful of the three dozen columns are shown here) is an example of data in which values are stored not in cells but instead:

* in columns (such as day of the month d1, d2 ... d31)
* in rows (tmin rows and tmax rows indicating what's measured, the minimum or maximum temperature)

As you look over this table, see if you can describe the algorithm (rule-based process) by which you could ask for the maximum temperature on March 13, 2010, at the MX17004 station.  It's complicated and requires looking at column headers and multiple cells.

<!-- data-type="none" -->
| id | year | month | element | d1 | d2 | d3 | d4 | d5 | d6 | d7 | d8 |
| -- | ---- | ----- | ------- | -- | -- | -- | -- | -- | -- | -- | -- |
| MX17004 | 2010 | 1 | tmax | — | — | — | — | — | — | — | — |
| MX17004 | 2010 | 1 | tmin | — | — | — | — | — | — | — | — |
| MX17004 | 2010 | 2 | tmax | — | 27.3 | 24.1 | — | — | — | — | — |
| MX17004 | 2010 | 2 | tmin | — | 14.4 | 14.4 | — | — | — | — | — |
| MX17004 | 2010 | 3 | tmax | — | — | — | — | 32.1 | — | — | — |
| MX17004 | 2010 | 3 | tmin | — | — | — | — | 14.2 | — | — | — |
| MX17004 | 2010 | 4 | tmax | — | — | — | — | — | — | — | — |
| MX17004 | 2010 | 4 | tmin | — | — | — | — | — | — | — | — |
| MX17004 | 2010 | 5 | tmax | — | — | — | — | — | — | — | — |
| MX17004 | 2010 | 5 | tmin | — | — | — | — | — | — | — | — |

A tidy version of this data is shown below.  Is it simpler now to ask for the maximum temperature on March 13, 2010?

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Notice how the date field is united in the tidy data below, which may seem to go against some of the principles we've argued for.  Dates are so frequently used, however, that it's very easy to extract, from a given date, the year, month, day, and even the day of the week, using computational methods.  Whether to break out a date into year, month, and day depends a lot on your use case.  For example, are you planning on obtaining temperature averages across all of June, and comparing June low temperature averages across years?

</div>

<!-- data-type="none" -->
| id | date | tmax | tmin |
| -- | -- | -- | --  |
| MX17004 | 2010-01-30 | 27.8 | 14.5 |
| MX17004 | 2010-02-02 | 27.3 | 14.4 |
| MX17004 | 2010-02-03 | 24.1 | 14.4 |
| MX17004 | 2010-02-11 | 29.7 | 13.4 |
| MX17004 | 2010-02-23 | 29.9 | 10.7 |
| MX17004 | 2010-03-05 | 32.1 | 14.2 |
| MX17004 | 2010-03-10 | 34.5 | 16.8 |
| MX17004 | 2010-03-16 | 31.1 | 17.6 |
| MX17004 | 2010-04-27 | 36.3 | 16.7 |
| MX17004 | 2010-05-27 | 33.2 | 18.2 |

### Multiple Types in One Table (Optional)

Remember that the original third rule of tidy data was replaced in later writings by Hadley Wickham?  Well, briefly, it's useful to bring up the original rule.  That original third rule asserts that each observational unit (or topic) forms its own table.  

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

This section may be considered optional for people working with .csv documents or spreadsheets, but the topic we're going to cover is important in the world of SQL databases, so we want to explain it.  Feel free to skip if it seems unhelpful!

</div>

<h4>"Normalized" Data</h4>

If you've ever worked with SQL databases, you know that in SQL, it is very common to divide data into very specific topics.  For example, demographic information about patients may be stored in a table called "demographics", while a table called "medication\_order" leaves out any mention of demographic information and concerns itself solely with information about the medication order (drug id number, prescribed dose, id of provider, etc.).  Patient details like age and sex are important for prescribers.  But rather than reiterate what is already known about the patient and add it anew in the medication\_order table, a patient identifier is used, which can then allow for linking across tables.

This division of data so that the minimum amount of data is reiterated in multiple places is called "normalization", and it's very useful, especially in large, complex data sets.  In these kinds of datasets (like Electronic Medical Records), it could be prohibitively costly (because of disk space and processing requirements) and error prone (because of the need to track down multiple copies for updated data) to continually add the data that exists in one table into new places.

<h4>A Sample demographics table</h4>

<!-- data-type="none" -->
| patient_id | date\_of\_birth | sex | last_name | first_name |
| -------    | -----------   | -   | ------    | ----- |
| ABC123     | 1970-03-15    | M   | Bird      | Big |
| TRSH789    | 1985-08-20    | M   | the Grouch | Oscar |
| SMLE321    | 1990-12-12    | F   | Dawn      | Prairie |

<h4>A Sample medication_order table</h4>

<!-- data-type="none" -->
| patient_id | provider_id | med_id | order_date |
| -------    | -----------   | --- | ------    | ----- |
| ABC123     | 491272    | 8000412   | 2021-05-15 |  
| ABC123     | 491272  | 7960004   | 2022-02-01 |
| SMLE321    | 223618    | 8000412 | 2020-08-19 |

That brings us to what sometimes happens when people try to squeeze too much data into a single spreadsheet or .csv file: multiple topics treated in a single table.  When this happens we often see lots of repeated data, as Hadley points out in his example taken from Billboard.  The data below represents the state of the Billboard data **after** some initial tidying has taken place, but we can see that there is rather a lot of repeating data, even once the data has been reorganized.  This isn't a completely tidy dataset:

<!-- data-type="none" -->
| year | artist | time | track | date | week | rank |
| ---- | -----  | ---- | ----  | ---  | ---  | ---- |
| 2000 | 2 Pac  | 4:22 | Baby Don't Cry | 2000-02-26 | 1 | 87 |
| 2000 | 2 Pac  | 4:22 | Baby Don't Cry | 2000-03-04 | 2 | 82 |
| 2000 | 2 Pac  | 4:22 | Baby Don't Cry | 2000-03-11 | 3 | 72 |
| 2000 | 2Ge+her | 3:15 | The Hardest Part of ... | 2000-09-02 | 1 | 91 |
| 2000 | 2Ge+her | 3:15 | The Hardest Part of ... | 2000-09-09 | 2 | 87 |
| 2000 | 2Ge+her | 3:15 | The Hardest Part of ... | 2000-09-16 | 3 | 92 |
| 2000 | 3 Doors Down | 3:53 | Kryptonite | 2000-04-08 | 1 | 81 |
| 2000 | 3 Doors Down | 3:53 | Kryptonite | 2000-04-15 | 2 | 70 |
| 2000 | 3 Doors Down | 3:53 | Kryptonite | 2000-04-22 | 3 | 68 |

The songs keep repeating because we're really tracking two different topics here:

* Basic information about songs (these characteristics don't change over time)
* Song popularity / top charts data

If we were to abide by the suggestion that each topic belongs in its own table, we could instead have two tables, one for songs and one for ranking, using the id to connect data from the two tables.

<h4>Song Data</h4>

<!-- data-type="none" -->
| id | artist | track | time |
| -- | ----- | ----- | ----- |
| 1 | 2 Pac   | Baby Don't Cry | 4:22 |  
| 2 | 2Ge+her | The Hardest Part of ... | 3:15 |
| 3 | 3 Doors Down | Kryptonite | 3:53 |


<h4>Ranking Data</h4>

<!-- data-type="none" -->
| id | date | week | rank |
| ----  | ---  | ---  | ---- |
| 1 | 2000-02-26 | 1 | 87 |
| 1 | 2000-03-04 | 2 | 82 |
| 1 | 2000-03-11 | 3 | 72 |
| 2 | 2000-09-02 | 1 | 91 |
| 2 | 2000-09-09 | 2 | 87 |
| 2 | 2000-09-16 | 3 | 92 |
| 3 | 2000-04-08 | 1 | 81 |
| 3 | 2000-04-15 | 2 | 70 |
| 3 | 2000-04-22 | 3 | 68 |

This means that we only have to correct a misspelled artist name or incorrect track duration in one place, rather than multiple locations.  This is especially important in SQL databases.  Still, this is more an issue of data storage and ease of updating, rather than cleaning up data for computation.  Consider this advice completely optional!

### One Type in Multiple Tables

Occasionally we also have data that treat the same topic but are stored in separate tables.  For example, if you're participating in a multi-site study, you may have data that is structured identically but arrive in your inbox in separate files. Logically, you could imagine "stacking" this data vertically, and perhaps adding a new column that gives the data collection site:

<h4>Clinic A</h4>

<!-- data-type="none" -->
| subject_id | dob | abc_score | xyz_score |
| ---------- | --- | --------- | --------- |
| 4123691    | 2009-08-12 | 87 | 4 |
| 4296120    | 2005-10-04 | 82 | 5 |
| 2934218    | 2008-03-28 | 70 | 4 |
| 2098821    | 2008-12-10 | 88 | 3 |

<h4>Clinic B</h4>

<!-- data-type="none" -->
| subject_id | dob | abc_score | xyz_score |
| ---------- | --- | --------- | --------- |
| 3396811    | 2010-12-29 | 78 | 4 |
| 0129681    | 2010-01-02 | 80 | 3 |
| 9766728    | 2007-07-10 | 77 | 3 |
| 6382922    | 2008-03-20 | 90 | 5 |

<h4>Combined Data</h4>

<!-- data-type="none" -->
| subject_id | dob | abc_score | xyz_score | collection_site |
| ---------- | --- | --------- | --------- | -- |
| 4123691    | 2009-08-12 | 87 | 4 | A |
| 4296120    | 2005-10-04 | 82 | 5 | A |
| 2934218    | 2008-03-28 | 70 | 4 | A |
| 2098821    | 2008-12-10 | 88 | 3 | A |
| 3396811    | 2010-12-29 | 78 | 4 | B |
| 0129681    | 2010-01-02 | 80 | 3 | B |
| 9766728    | 2007-07-10 | 77 | 3 | B |
| 6382922    | 2008-03-20 | 90 | 5 | B |

### Quiz: Tidying Data


Now that we've looked at several examples of messy data and ways to rearrange the data to make it tidy, let's look at a fabricated example and try to diagnose some of its problems.

<div>
Take a look at the sample table provided below.  It's similar to what you might see in a publication, and it's in a great format for humans... but it's not tidy enough to work with easily in a computational way.  This table shows the results of the "QPT" psychometric (something we made up) and shares pre- and post-treatment means and standard deviations for different kinds of research cohorts.

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
</div>

[[X]] move "depression" status into a column instead of using it in a cell combined with other descriptors
[[ ]] remove sex as a variable, since there's no way to detangle it from other variables
[[ ]] ensure that each number has the same number of significant digits after the decimal point
[[X]] make "timepoint" into a new column, with possible values including "pre" and "post"
[[X]] increase the rows so that there are 16 rows representing 16 distinct cohorts
[[?]] There are multiple correct answers!
***************

<div class = "answer">

Depression status and timepoint should each become a column.  In fact, we suggest the following columns:

* Depression +/- dx
* Anxiety +/- dx
* Sex
* Timepoint (pre- vs post- treatment)
* Mean QPT value
* SD QPT value
* n (count of participants in this group)

There's no need to remove the sex variable, and the numerical values don't necessarily need to have the same number of significant digits to be considered "tidy".  Here's one way to make the table above into a tidy dataset ready for computational analysis:

<!-- data-type="none" -->
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

**************



## Tidy Data Analysis

In addition to data being tidy, data analysis itself has some tidy principles.  Tidy data analysis follows general principles that allow for research reproducibility, code readability, and the development of patterns of coding that are transferable from use case to use case.  We won't go into implementation detail here, but it's useful to keep in mind some tenets of tidy data analysis.  If you already use code to analyze data, consider whether your approaches adhere to these tenets.  If you don't use code yet, it might be helpful to jot these down to remind you of some guideposts as you learn.

The basic tenets of "tidy" data analysis include:

<h4>Data should be organized in a tidy way</h4>

Tidy data organization includes everything we've covered so far in this module!  If your data is in a tidy format (hopefully you get to handle data collection and can make it tidy from the start), it's possible to rearrange it in almost any number of ways, including making intentionally "messy" formats for publication.  Also, it's easier to write code on tidy data, because the algorithm (process) for analyzing data will be simpler.  Of course, here we've glossed over the hard work of getting messy data that you inherited transformed and cleaned up into tidy data.  This is hard work and you'll spend lots of time doing data cleanup to transform messy data into tidy data.  But once you've done that, the analysis portion of your work is much easier.

<h4>Programming code that acts on the data should be consistent, concise, with predictable inputs and outputs, and sound like human language as much as possible.</h4>

This is a dense topic that we won't explain in detail here, as the best way to demonstrate tidy code is through code examples, which we're intentionally avoiding here.  But it's helpful to point out that the shortest code isn't always the best code!  Some people like to play "code golf" - solving a problem in clever, obscure ways with as few lines of code as possible.  We urge you to consider that concise code doesn't mean "as short as possible", but rather "as long as needed to explain things well".  After all, data analysis code is intended for two audiences: the computer running the code and the people reading the code.  That's different than, say, the code that runs your operating system, which isn't designed to be read by people.  Consistency is also helpful for humans.  Naming data columns with the same case convention (such as camelCase or snake_case) is one way to be consistent and reduce the cognitive load on your reader.

<h4>Each data analysis can be broken down into a series of atomic steps, such as "select this column" or "arrange the data by the values in that column". An arbitrarily complex data analysis can be broken down as a pipeline of atomic steps.</h4>

Again, here it's important to highlight that clever, brief code that accomplishes three complex maneuvers by using a little-known command might be rewarding to discover and write, but often a headache to read and understand.  A great way to break things down into atomic text is to start off by writing "pseudocode", in which you write a series of operations that aren't in any computer code but instead in a sort of human language that is influenced by code.  Then, try running your pseudocode past your rubber duck for extra clarity!  For example:

* create an empty table to hold aggregated results
* separate the rows from our raw tidy data into groups by research arm (intervention\_1, intervention\_2, ... , intervention\_7)
* for each group:

  * find the median abc\_score
  * count the number of observations that fall outside the interquartile range for xyz\_score
  * divide that count by the total number of observations for the group to find the proportion of extreme xyz scores
  * store the group name (intervention_1, etc.), median abc\_score, and proportion of extreme xyz\_score as a row in our aggregated results table
* with the new table, calculate the correlation between median abc\_score and proportion of extreme\_xyz score.

### Quiz: Tidy Data analysis

Which of these are accurate suggestions with regard to making data analysis more tidy?  

[[ ]] Tidy data analysis includes code that is as brief as possible in order to reduce computational processing time
[[X]] It can be helpful to break down complex analysis into small steps in human language before starting computation
[[X]] Naming things and writing code in a consistent way makes for tidy data analysis
[[ ]] Pseudocode should be avoided, as it results in badly written data analysis
[[X]] Data analysis should be conducted so that both humans and computers can use the code effectively
[[?]] There are multiple correct answers!
*********

<div class = "answer">

Data analysis should be concise.  For example, if you're doing a lot of cut-and-paste and nearly identical lines of code, it might be useful to make a function.  But that doesn't mean that it should be as short as possible.  After all, both computers **and** humans will consume the code, so writing inscrutable, genius level code that is difficult for average users to read is a bad idea.  In order to make data analysis more understandable and more tidy, habits like naming things and composing code in a consistent way can be very helpful.  Finally, pseudocode is a very useful tool that helps you understand the process that you want to carry out in small, atomic steps.

</div>

***********



## Additional Resources

* The article we've been discussing is Hadley Wickham's [Tidy Data](https://www.jstatsoft.org/article/view/v059i10)
* [Chapter 12 of *R for Data Science*](https://r4ds.had.co.nz/tidy-data.html) is specific to the R language, but does a good job of presenting the topic.  Feel free to gloss over the code-heavy parts if they don't serve you.
* [Tidy Data and How to Get It](https://www.measureevaluation.org/news/tidy-data-and-how-to-get-it.html) briefly discusses tidy data in the context of global health.
* [Introduction to Tidy Data in R](https://stat2labs.sites.grinnell.edu/Handouts/rtutorials/IntroTidyData.html) is mostly a code tutorial that gets very detailed in code.  What makes it interesting as a supplemental resource is that it presents five, not three, rules for tidy data -- and I agree with these tidy data rules!
* Karl Broman gives a great overview of [Data Organization in Spreadsheets](https://peerj.com/preprints/3183.pdf).  If Excel is part of your toolkit, please read this article.


## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Tidy+Data%22)!

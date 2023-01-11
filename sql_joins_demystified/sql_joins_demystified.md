<!--
author:   Joy Payton
email:    paytonk@chop.edu
version:  1.0.0
module_template_version: 3.0.0
language: en
narrator: US English Female
title: SQL Joins Demystified
comment: Learn about SQL joins in a non-coding module.
long_description: Usually, data in a SQL database is organized into multiple interrelated tables.  This means you will often have to bring data together from two or more tables into a single dataset to answer your research questions.  This is accomplished using JOIN commands.  This module explains the type of joins, without going into detail about the SQL code itself.
estimated_time: 40 minutes 

@learning_objectives  
After completion of this module, learners will be able to:

- Explain what "join criteria" are and give an example of what makes "matching" data in two separate tables
- Describe the various "shapes" of SQL JOIN: inner, left, right, and full


@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css
script: https://kit.fontawesome.com/83b2343bd4.js


-->

# SQL Joins

<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**   Learners should have experience writing SQL code on single tables.  If you have successfully used a "SELECT... FROM... WHERE" SQL statement on a single table, and have at least seen "GROUP BY" commands in action, even if you would need help writing the GROUP BY code, you have enough code ability.  We also highly recommend that you understand the concepts of one-to-many data relationships and database normalization to get the most out of this module. 

If you need to develop basic SQL fluency we recommend our module [SQL Basics](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/sql_basics/sql_basics.md).  For more intermediate topics, we suggest our module [SQL Intermediate](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/sql_intermediate/sql_intermediate.md).  Finally, to learn about one-to-many data relationships and database normalization, consider our [SQL Normalization](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/sql_normalization/sql_normalization.md) module.

**Learning Objectives**

@learning_objectives

</div>

## Multiple Tables

Most SQL queries require something more complex than referencing data from a single table. This is where SQL join functionality and the `JOIN` command come into play.

SQL joins are used to combine rows from two tables, based on some set of columns they have in common.  For example, consider the case where you have data about a multi-site study's research subjects. One table holds depression scores for subjects and a different table holds subject addresses.  Your hypothesis is that people who live in certain zip codes have higher rates of depression.  

To see if your hypothesis has evidence to back it, you need to combine data, taking the subject ID and depression score from one table, and the subject ID and zip code from another table, and combining them, so that you get matching information in the same table row.

Maybe your source tables look something like the tables below:

**Table 1: depression\_scale**

<!-- data-type="none" class="tight-table" style="font-size:80%"-->
| subj_id  | date  | dep_q1  | dep_q2   | dep_q3  | dep_q4  | dep_total   |
| :--------- | :--------- | :--------- | :--------- | :--------- | :--------- | :--------- |
| 11234   | 2021-05-15   | 3    | 3  | 2    | 4    | 12    |
| 86234   | 2021-06-01   | 4    | 4  | 3    | 4    | 15    |
| 32660   | 2021-06-10   | 1    | 1  | 2    | 1    | 5   |
| 86234   | 2022-01-13   | 2    | 2  | 1    | 3    | 8    |
| 41356   | 2022-02-10   | 1    | 3  | 2    | 3    | 10   |

**Table 2: subject\_address**

<!-- data-type="none" class="tight-table" style="font-size:80%"-->
| subj_id  | street_address  | city  | state   | zip  | date_start  | date_end   |
| :--------- | :--------- | :--------- | :--------- | :--------- | :--------- | :--------- |
| 11234   | 123 Main Street   | Smithtown    | PA  | 19000    | 2022-01-01   | `NULL`    |
| 11234   | 123 Oak Lane   | Old Towne    | PA  | 18000   | 2000-01-01    | 2021-12-31    |
| 93452   | 123 Green Blvd  | Kirby    | TN  | 37000    | 2020-05-01    | `NULL`   |

What you want to eventually end up with will be a single table of results that might only have three columns: "subj\_id", "dep\_total", and "zip".  That way you can look at the relationship between depression inventory scale and zip code.

## Forming a JOIN 

There are two basic pieces of information you need to know to write successful joins:

* What **join criteria** would you like your join evaluated against?  In other words, how are you linking rows from one table to rows from another table?  What constitutes a "match" of data from one table to data from another?  If you're joining data that holds student grades, for example, you probably want to only join data together where the student ID matches.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

It can be surprisingly tricky to figure out what makes data "match" or "go together" in your join criteria.  For example, go back to the previous page and see if you can decide what data should be considered "matching" between the "depression\_scale" table and the "subject\_address" table.  Is it as simple as just matching on the subject id ("subj_id")?  Why or why not?

</div>

* What **type of join** do you want to use?  Let's say you have some students with math grades and some students with language grades.  Some students are in only the math table, some are only in the language table, and some are in both.  What part of the overlapping data do you want?  Only the data on students with both kinds of grades?  Or some other, larger set of student data?

We'll address each of these in the next few sections.

### Join Criteria

Join criteria are conditions that mean that rows from two different tables belong together.  Your criteria might be something like:

* Join the rows from "depression\_scale" with rows from "subject\_address" **... but only if the subject id field matches**
* Join the rows from "items" with the rows from "orders" **... but only if the item id field matches**
* Join the rows from "math\_grades" with the rows from "english\_grades" **... but only if the student id is the same and the semester is the same**

When the conditions in your join criteria evaluate as TRUE for a row then a join will be performed for those rows, and when the join criteria are evaluated as FALSE no join for those rows will take place.

**Data Relationships**

As a reminder, SQL is a **relational database**, so it's not surprising that we talk about data relationships in this module.  Equality is one kind of relationship, when two data points are identical, but other relationships, like "less than" or "between" will also prove useful when we set up our join criteria.

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

This isn't a coding module, but we're going to show some code snippets here.  This is to help you recognize the code and help set you up for learning how to practically **do** SQL joins.  Don't worry if you feel a bit intimidated by the code you see, you won't have to use it in this module.

</div>

Join criteria will be some sort of relationship statement referencing shared information (data that occurs in both tables you want to join) that you would like evaluated to TRUE or FALSE when resolving your join.  Often, the relationship is equality -- you're looking for a perfect match.  We'll start with equality, the most frequently used condition, on the next page. 

#### Equality, Example 1

Do you have subject identifiers or student id numbers in two different tables?  This shared information can be used to connect (join) data from these tables, based on the identifier being equal.  

For example, if the subject id matches, a row from table A and a row from table B will be joined.  If the subject id doesn't match, these rows won't be joined.  Maybe we're trying to line up lung cancer occurrence and smoking exposure in the same row:

**disease**

<!-- data-type="none" class="tight-table"-->
| subject\_id  | lung\_cancer |
| :--------- | :--------- | 
| 3  | TRUE |
| 5 | FALSE  |
| 8  | FALSE |

**smoking**

<!-- data-type="none" class="tight-table"-->
| subject\_id  | smoking\_pack\_years |
| :--------- | :--------- | 
| 2  | 10 |
| 3 | 10  |
| 4  | 0 |


In code, we usually use an **ON** statement:

```sql

...
ON disease.subject_id = smoking.subject_id
```

In this case, we're comparing the equality of two fields that **have the same name**, so we could also use **USING**.  This special word only applies when you're looking for a perfect match between fields that have matching names, too.  It's okay if you never use `USING` and prefer to always stick with `ON`, which is more multi-purpose.

```sql
...
USING(subject_id)
```

With either of the above code snippets:

* subject 3 from disease lines up with subject 3 from smoking <i class="fa fa-check" aria-hidden="true"></i>
* subject 5 from disease doesn't line up with anyone in smoking <i class="fa-solid fa-xmark" aria-hidden="true"></i>
* subject 8 from disease doesn't line up with anyone from smoking <i class="fa-solid fa-xmark" aria-hidden="true"></i>
* subject 2 from smoking doesn't line up with anyone from disease <i class="fa-solid fa-xmark" aria-hidden="true"></i>
* subject 4 from smoking doesn't line up with anyone from disease <i class="fa-solid fa-xmark" aria-hidden="true"></i>


#### Equality, Example 2

Sometimes the data that appears in the two tables has the same field name, as we just saw on the previous page.  Sometimes, however, the data might be stored under different names.  Let's consider this example:

**math\_grades**

<!-- data-type="none" class="tight-table"-->
| student\_id  | math\_grade | semester |
| :--------- | :--------- | :------ |
| 11  | A | Jan-May 2023 |


**language\_grades**

<!-- data-type="none" class="tight-table"-->
| student\_id  | language\_grade | term |
| :--------- | :--------- | :------ |
| 11 | C | Sep-Dec 2022 |
| 14 | B | Jan-May 2023 |

Here, "semester" is used in math\_grades and term is used in "language\_grades".  So you might also see something like:

```sql
...
ON math_grades.semester = language_grades.term
```

In this example:

* The A grade for Jan-May 2023 from math\_grades lines up with the B grade for Jan-May 2023 in language\_grades (whoops, even though the student_id doesn't match!)<i class="fa fa-check" aria-hidden="true"></i>
* The C grade for Sep-Dec 2022 in language\_grades does not line up with any row in math\_grades <i class="fa-solid fa-xmark" aria-hidden="true"></i>

This highlights the importance of documenting your data so you can tell which fields hold which data in order to use them properly for joins.  If `semester` and `term` are  different things, not just the same thing with two different names, the result of your join will be disappointing.  

This also shows that figuring out your join criteria requires close attention -- we probably don't mean to match student 11's math grades with student 14's language grades!

#### Non-Equality and More

Sometimes you don't need equality as your condition.  For example, in our example from our multi-site mental health research, let's say we want to associate a particular depression score with a particular address only if the depression inventory was given between the start and end dates of residency at that address. In a case like that, you might see something like:

```sql
...
ON depression_scale.date BETWEEN 
   subject_address.date_start AND 
   subject_address.date_end
```

**Multiple conditions**

Of course, in the example of the depression inventory, we'd also want to make sure that there was a match on subject identifier (you don't want to match Lakshmi's depression score with Larry's address, just because the dates worked!).  You can combine conditions too.  Here, we look for an exact match on subject id and a date match that's between the correct dates:

```sql
ON depression_scale.subj_id = subject_address.subj_id AND
   depression.date BETWEEN 
      subject_address.date_start AND 
      subject_address.date_end
```

#### Getting Really Complicated

Let's keep thinking about our depression inventories and our goal of matching depression scores to addresses in our study. What if some addresses don't have end dates?  This could be because the subject is currently still living there.  There are some addresses with `NULL` end dates in our data, so this isn't an academic question.

You can create arbitrarily complex **boolean logic** (or **boolean algebra**), using AND, OR, NOT, and parentheses as needed.  Much as in math, there's an order of operations in this kind of logic, and you might need several sets of parentheses to make sure you're applying the conditions correctly.  For example, see below.  We've added comments to help illustrate the logic.

```sql
ON depression.subj_id = subject_address.subj_id AND 
-- subject id must match... AND...

-- either:
   ((depression.date BETWEEN          
      subject_address.date_start AND 
      subject_address.date_end) OR
-- the depression date is between a start and end, OR...

   (depression.date > subject_address.date_start AND 
   subject_address.date_end IS NULL))                 
-- the depression date is after the start date,
-- and there's no end date.
```

Let's take this more comprehensive example and look at the example tables from the first page of this module:

**depression\_scale**

<!-- data-type="none" class="tight-table" style="font-size:80%"-->
| subj_id  | date  | dep_q1  | dep_q2   | dep_q3  | dep_q4  | dep_total   |
| :--------- | :--------- | :--------- | :--------- | :--------- | :--------- | :--------- |
| 11234   | 2021-05-15   | 3    | 3  | 2    | 4    | 12    |
| 86234   | 2021-06-01   | 4    | 4  | 3    | 4    | 15    |
| 32660   | 2021-06-10   | 1    | 1  | 2    | 1    | 5   |
| 86234   | 2022-01-13   | 2    | 2  | 1    | 3    | 8    |
| 41356   | 2022-02-10   | 1    | 3  | 2    | 3    | 10   |

**subject\_address**

<!-- data-type="none" class="tight-table" style="font-size:80%"-->
| subj_id  | street_address  | city  | state   | zip  | date_start  | date_end   |
| :--------- | :--------- | :--------- | :--------- | :--------- | :--------- | :--------- |
| 11234   | 123 Main Street   | Smithtown    | PA  | 19000    | 2022-01-01   | `NULL`    |
| 11234   | 123 Oak Lane   | Old Towne    | PA  | 18000   | 2000-01-01    | 2021-12-31    |
| 93452   | 123 Green Blvd  | Kirby    | TN  | 37000    | 2020-05-01    | `NULL`   |

With this most recent join criteria:

* The depression score (dep\_total) for subject 11234, measured on 2021-05-15, matches with the address 123 Oak Lane for the same subject and time period. <i class="fa fa-check" aria-hidden="true"></i>
* The depression score (dep\_total) for subject 11234, measured on 2021-05-15, will **not** match with the address 123 Main Street for the same subject, because the time period doesn't match. <i class="fa-solid fa-xmark" aria-hidden="true"></i>
* The other rows in the depression\_scale don't match with any rows in the subject\_address table. <i class="fa-solid fa-xmark" aria-hidden="true"></i>
* The first and third rows of the subject\_address table don't have a match with any rows in the depression\_scale table. <i class="fa-solid fa-xmark" aria-hidden="true"></i>

#### Using Other SQL Commands

Especially for one-to-many data relationships, you might want to create a simplified table temporarily in order to have that be part of a join.  This means you may have to also do some complicated things like using GROUP BY with aggregation, using WHERE and/or HAVING, or creating subqueries.  

For example, let's say you want to only use the earliest depression inventory for each subject, not any subsequent depression inventories, for your analysis of the correlation between depression score and zip code.  Then you want to join that earliest depression inventory with the address of the subject at the time of administration of that earliest inventory.  That's a lot of logic!  The easiest way to do that is to first create a simplified table that only contains the earliest depression inventory for each subject id.  This is a great place to use `GROUP BY` and the aggregation function `MIN()` to find the earliest date of administration.  Then you can use that simpler table to join to subject addresses.  

We won't show the code for this in this module, but be aware that you can think about complex joins by first planning how you can simplify a table to make the logic easier to work with!

#### Quiz: Join Criteria

True or False: a matching id (like student\_id or patient\_id) is generally sufficient as a join criterion.

[( )] True
[(X)] False
****
<div class = "answer">

Often, a matching identifier is part of what makes up good join criteria, but it may not be sufficient on its own.  For example, consider trying to link patient diagnoses with medication orders.  Patients can appear dozens or hundreds of times across decades, so to correctly link diagnoses with medications, it's not sufficient to rely just on patient id.  You might need to use an "encounter id", a date range, or another join criteria to make sure you're matching data that really belongs together (instead of joining Mary's diagnosis of diaper rash when she was 3 months old to her prescription of Ritalin at age 9).

</div>
****


### Join Types 

Let's consider the gradebook example we mentioned earlier.  You are assembling grade reports for students.  You have two tables, one called "math\_grades" and one called "language\_grades".  Some students appear in "math\_grades", some in "language\_grades", and some students have rows in both tables.  Depending on your purposes, you might want any one of several types of joins, each with its own SQL keyword combination.  Let's imagine a Venn diagram, as shown below:

<lia-keep>

<style>
#infographic {
 width: 40em;
 height: 24em;
  margin: 1em auto;
  padding: 1em;
  position: relative;
}

.circle {
  border: .2em solid #000;
  border-radius: 50%;
  width: 24em;
  height: 24em;
  text-align: center;
  vertical-align: center;
  position: absolute;
}

.circle p {
  height: 24em;
  width: 14em;
  display: table-cell;
  vertical-align: middle;
}

#c1 {
  top: 0;
  left: 0;
  background-color: rgba(255,0,0,.25);
}

#c2 {
  top: 0;
  left: 12em;
  background-color: rgba(0,255,0,.25);
}

#c1 p{
  padding-right: 2em;
}
#c2 p {
    padding-left: 12em;
    width: 22em;
}


#j12 {
    position: absolute;
    left: 12em;
    width: 11em;
    height: 22em;
    padding: 1em;
    text-align: center;
}

#j12 p {
  height: 22em;
  width: 10em;
  display: table-cell;
  vertical-align: middle;
}
</style>
<div id="infographic">
  <div id="c1" class="circle">
    <p>Left Side: <br/>Only Math Grades</p>
  </div>

  <div id="c2" class="circle">
    <p>Right Side: <br/>Only Language Grades</p>
  </div>

  <div id="j12" class="joined">
    <p>
      Overlap: <br/>Both Math and Language Grades
    </p>
  </div>
</div>

</lia-keep>

There are 4 basic join types that can be used.  We'll go into more detail about how each one works in practice in the next few pages.

* **`INNER JOIN`**.  ![Overlapping circles with only the inner, overlapping part highlighted](media/inner.png) 
An `INNER JOIN` (and this is the default behavior of `JOIN` without any modifying words) would only include grade data falling in the "Both Math and Language Grades" overlap section.  This is often the data you want to capture.  If you're conducting research on the correlation between math and language grades, this is the JOIN you want.  If a student lacks one or the other grade, their data isn't useful to you, so you don't want it. 

* **`LEFT JOIN`**.  ![Overlapping circles with the left circle, including the overlapping part of the left circle, highlighted](media/left_outer.png) 
A `LEFT JOIN` (or a `LEFT OUTER JOIN` as you'll sometimes see it) includes the data in "Only Math Grades" -- that's the "outer" part on the left -- and in "Both Math and Language Grades" -- the overlap section.  It would exclude student data in the "Only Language Grades" section (which is on the right).  Maybe you want this data because as the chair of the mathematics department, you want to see what students are strongest, in math, and also in language if known, in order to select who to award a math prize to. 

* **`RIGHT JOIN`**.  ![Overlapping circles with the right circle, including the overlapping part of the right circle, highlighted](media/right_outer.png) 
A `RIGHT JOIN` (or a `RIGHT OUTER JOIN`) would include the data in "Only Language Grades" -- that's the "outer" part on the right -- and for students with "Both Math and Language Grades" -- the overlap section.  It would exclude student data in the "Only Math Grades" section (which is on the left).  Maybe you want this data to create a graph of language grade distribution, and want to enrich it with some statistics about math grades where available, but it doesn't matter if some students lack math grades. 

* **`FULL JOIN`**.  ![Overlapping circles with both circles highlighted](media/full_outer.png) 
A `FULL JOIN` (or sometimes you'll see `FULL OUTER JOIN`) will capture all the data -- all of the outer data on the right and left as well as the inner (overlapping) data.  This is important if you want to create a grade book that shows student grades for each student, including their math grades and/or their language grades. 

#### `INNER JOIN`

![Overlapping circles with only the inner, overlapping part highlighted](media/inner.png) 

An `INNER JOIN` shows up in code like this:

```sql
...
FROM math_grades INNER JOIN language_grades
ON ...
```

or

```sql
...
FROM math_grades JOIN language_grades
ON ...
```

Note that the word `JOIN` by itself means `INNER JOIN`.

To understand what this means practically, let's go to a simple example of two tables we used earlier in this module:

**disease**

<!-- data-type="none" class="tight-table"-->
| subject\_id  | lung\_cancer |
| :--------- | :--------- | 
| 3  | TRUE |
| 5 | FALSE  |
| 8  | FALSE |

**smoking**

<!-- data-type="none" class="tight-table"-->
| subject\_id  | smoking\_pack\_years |
| :--------- | :--------- | 
| 2  | 10 |
| 3 | 10  |
| 4  | 0 |

And let's combine our join criteria (subject\_id matching) with our join type (inner).  We won't show the whole query here, just the pertinent parts that describe the join:

```sql
...
FROM disease JOIN smoking
ON disease.subject_id = smoking.subject_id
```

This is the result we would get.  It only includes data for subjects appearing in both tables:

<!-- data-type="none" class="tight-table"-->
| subject\_id  | lung\_cancer | smoking\_pack\_years |
| :--------- | :--------- | :--------- | 
| 3  | TRUE | 10 |



#### `LEFT JOIN`

![Overlapping circles with the left circle, including the overlapping part of the left circle, highlighted](media/left_outer.png) 

A `LEFT JOIN` shows up in code like this.  Note that one table is listed first, and is therefore on the left, and the other table is listed second, and is therefore on the right (because English is written left to right).

```sql
...
FROM math_grades LEFT JOIN language_grades
ON ...
```

or

```sql
...
FROM math_grades LEFT OUTER JOIN language_grades
ON ...
```

To understand what a `LEFT JOIN` means practically, let's again go to a simple example of two tables we used earlier in this module:

**disease**

<!-- data-type="none" class="tight-table"-->
| subject\_id  | lung\_cancer |
| :--------- | :--------- | 
| 3  | TRUE |
| 5 | FALSE  |
| 8  | FALSE |

**smoking**

<!-- data-type="none" class="tight-table"-->
| subject\_id  | smoking\_pack\_years |
| :--------- | :--------- | 
| 2  | 10 |
| 3 | 10  |
| 4  | 0 |

And let's combine our join criteria (subject\_id matching) with our join type (left).  We won't show the whole query here, just the pertinent parts that describe the join:

```sql
...
FROM disease LEFT JOIN smoking
ON disease.subject_id = smoking.subject_id
```

This is the result we would get.  We would have a row for each item of data in the left table, enriched where possible with data from the right table.

<!-- data-type="none" class="tight-table"-->
| subject\_id  | lung\_cancer | smoking\_pack\_years |
| :--------- | :--------- | :--------- | 
| 3  | TRUE | 10 |
| 5 | FALSE  | `NULL` |
| 8  | FALSE | `NULL` |

When there's no matching data from the right table to join to the data you included from the left, `NULL` values (empty cells) are added.

#### `RIGHT JOIN`

![Overlapping circles with the right circle, including the overlapping part of the right circle, highlighted](media/right_outer.png) 

A `RIGHT JOIN` shows up in code like this.  Recall that "left" and "right" refer to the order in which the table names are typed in the `FROM` statement.


```sql
...
FROM math_grades RIGHT JOIN language_grades
ON ...
```

or

```sql
...
FROM math_grades RIGHT OUTER JOIN language_grades
ON ...
```

To understand what a `RIGHT JOIN` means practically, let's again use our example tables:

**disease**

<!-- data-type="none" class="tight-table"-->
| subject\_id  | lung\_cancer |
| :--------- | :--------- | 
| 3  | TRUE |
| 5 | FALSE  |
| 8  | FALSE |

**smoking**

<!-- data-type="none" class="tight-table"-->
| subject\_id  | smoking\_pack\_years |
| :--------- | :--------- | 
| 2  | 10 |
| 3 | 10  |
| 4  | 0 |

And let's combine our join criteria (subject\_id matching) with our join type (right).  We won't show the whole query here, just the pertinent parts that describe the join:

```sql
...
FROM disease RIGHT JOIN smoking
ON disease.subject_id = smoking.subject_id
```

This is the result we would get.  We're including all the data from the right table, enriched where possible with data from the left table.

<!-- data-type="none" class="tight-table"-->
| subject\_id  | lung\_cancer | smoking\_pack\_years |
| :--------- | :--------- | :--------- | 
| 2  | `NULL` | 10 |
| 3 | TRUE | 10  |
| 4  | `NULL` | 0 |

When there's no matching data from the left table to join to the data you included from the right, `NULL` values (empty cells) are added.

#### `FULL JOIN`

A `FULL JOIN` shows up in code like this:

```sql
...
FROM math_grades FULL JOIN language_grades
ON ...
```

or

```sql
...
FROM math_grades FULL OUTER JOIN language_grades
ON ...
```

To understand what a `FULL JOIN` means practically, let's go, one last time, to our example tables:

**disease**

<!-- data-type="none" class="tight-table"-->
| subject\_id  | lung\_cancer |
| :--------- | :--------- | 
| 3  | TRUE |
| 5 | FALSE  |
| 8  | FALSE |

**smoking**

<!-- data-type="none" class="tight-table"-->
| subject\_id  | smoking\_pack\_years |
| :--------- | :--------- | 
| 2  | 10 |
| 3 | 10  |
| 4  | 0 |

And let's combine our join criteria (subject\_id matching) with our join type (full).  We won't show the whole query here, just the pertinent parts that describe the join:

```sql
...
FROM disease FULL JOIN smoking
ON disease.subject_id = smoking.subject_id
```

This is the result we would get.  Each subject is represented here, both the ones who appear in the left table and in the right table.

<!-- data-type="none" class="tight-table"-->
| subject\_id  | lung\_cancer | smoking\_pack\_years |
| :--------- | :--------- | :--------- | 
| 3  | TRUE | 10 |
| 5 | FALSE  | `NULL` |
| 8  | FALSE | `NULL` |
| 2  | `NULL` | 10 |
| 4  | `NULL` | 0 |

When there's no matching data from the one of the tables to join to the data you included from the other table, `NULL` values (empty cells) are added.

#### Quiz: Types of Joins

Consider the scenario of a table of math grades for 9th grade students and a table of language grades for 9th grade students.  Some 9th graders appear in both tables, but some appear only in one of them.  Fatima appears in the math\_grades table, but not in the language\_grades table.  When you perform a full outer join on these two tables, what will happen to Fatima's data in the resulting joined table?

[( )] Her data will not appear, since she's not represented in both tables.
[(X)] Her math grade will appear and she'll have a blank for her language grade.
[( )] The join command will fail, because a full join can only take place on fully overlapped tables.
[( )] The join command will fail because there's no such type of join as a full outer join.

****
<div class = "answer">

A full outer join is indeed a type of join, and it can take place on any two tables, whether they have a full or partial overlap or even no overlap at all.  In this example case, Fatima's data will appear in the results table, because regardless of whether the math\_grades table was written on the left or the right, a full outer join includes both the left and right tables' data.  We know her math grade, so that will appear, but since there's no matching data for Fatima in the language\_grades table, she'll have empty cells with `NULL` values for any columns that come from the language\_grades table.

</div>
****

## Additional Resources

* Want to understand the basics of boolean algebra?  Check out a good tutorial at https://ryanstutorials.net/boolean-algebra-tutorial/boolean-algebra.php.
* The second part of that tutorial covers some of the rules (like commutativity) of boolean algebra: https://ryanstutorials.net/boolean-algebra-tutorial/boolean-algebra-laws.php 
* Finally, to understand the order of operations in boolean algebra a bit more intuitively, we recommend the third part of the same tutorial: https://ryanstutorials.net/boolean-algebra-tutorial/boolean-algebra-expressions.php
* A great page to practice joins and visualize them in the form of Venn diagrams is at https://www.w3schools.com/sql/sql_join.asp.

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22SQL+Joins%22Demystified)!

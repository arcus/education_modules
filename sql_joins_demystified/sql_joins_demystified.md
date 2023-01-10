<!--
author:   Joy Payton
email:    paytonk@chop.edu
version:  1.0.0
module_template_version: 3.0.0
language: en
narrator: US English Female
title: SQL Joins Demystified
comment: Learn about SQL joins in a non-coding module.
long_description: Usually, data in a SQL database is organized into multiple interrelated tables.  This means you will often have to bring data together from two or more tables into a single dataset to answer your research questions.  This is accomplished using JOIN commands.  This module teaches underlying data considerations and explains the type of JOINS, without going into detail about the SQL code itself.
estimated_time: 1 hour

@learning_objectives  
After completion of this module, learners will be able to:

- Explain the significance of "one to many" data relationships and data normalization
- Describe the various "shapes" of SQL JOIN: inner, left, right, and full
- Explain how data can be linked between tables and define "primary keys" and "foreign keys"

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

**Pre-requisites**  A moderate level of experience writing basic SQL code (SELECT, FROM, WHERE) and intermediate SQL code (CASE, LIKE, GROUP BY, WITH, etc.) on single tables is expected in this module. If you need to develop basic SQL fluency we recommend our module [SQL Basics](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/sql_basics/sql_basics.md).  For more intermediate topics, we suggest our module [SQL Intermediate](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/sql_intermediate/sql_intermediate.md).

**Learning Objectives**

@learning_objectives

</div>

## Multiple Tables

Most SQL queries require something more complex than referencing data from a single table. This is where SQL JOIN functionality comes into play.

SQL JOINs are used to combine rows from two tables, based on some set of columns they have in common.  For example, consider the case where you have data about a multi-site study's research subjects. One table holds depression scores for patients and a different table holds patient addresses.  Your hypothesis is that people who live in certain zip codes have higher rates of depression.

To see if your hypothesis has evidence to back it, you need to combine data, taking the patient ID and depression score from one table, and the patient ID and zip code from another table, and combining them.  

Maybe your source tables look something like the tables below:

**Table 1: `depression_scale`**

<!-- data-type="none" class="tight-table" style="font-size:80%"-->
| subj_id  | date  | dep_q1  | dep_q2   | dep_q3  | dep_q4  | dep_total   |
| :--------- | :--------- | :--------- | :--------- | :--------- | :--------- | :--------- |
| 11234   | 2021-05-15   | 3    | 3  | 2    | 4    | 12    |
| 86234   | 2021-06-01   | 4    | 4  | 3    | 4    | 15    |
| 32660   | 2021-06-10   | 1    | 1  | 2    | 1    | 5   |
| 86234   | 2022-01-13   | 2    | 2  | 1    | 3    | 8    |
| 41356   | 2022-02-10   | 1    | 3  | 2    | 3    | 10   |

**Table 2: `subject_address`**

<!-- data-type="none" class="tight-table" style="font-size:80%"-->
| subj_id  | street_address  | city  | state   | zip  | date_start  | date_end   |
| :--------- | :--------- | :--------- | :--------- | :--------- | :--------- | :--------- |
| 11234   | 123 Main Street   | Smithtown    | PA  | 19000    | 2022-01-01   | `NULL`    |
| 11234   | 123 Oak Lane   | Old Towne    | PA  | 18000   | 2000-01-01    | 2021-12-31    |
| 93452   | 123 Green Blvd  | Kirby    | TN  | 37000    | 2020-05-01    | `NULL`   |

What you end up with after your successful JOIN will be a single table of results that might just have three columns: `subj_id`, `dep_total`, and `zip`.  That way you can look at the relationship between depression inventory scale and zip code.

You may be asking yourself, "Why not just put all the information together in one table to start with?"  After all, getting one row per subject is how we usually prepare to apply statistical tests. If we could just **start** with one row per subject in SQL, we'd be ready to jump into the science and not have so much data preparation work. 

The reason why this usually doesn't happen in a SQL database, and you instead see lots of different tables that you have to join together is because of a concept known as **normalization**.  To explain normalization, we'll first explain **one-to-many** data relationships.

## One-to-many

Data often has one-to-many relationships. What does one-to-many mean? Consider two use cases, a hospital and a retail website.  Each organization has one-to-many data relationships:

**Hospital one-to-many examples**

* One patient has multiple encounters on different dates
* One encounter may include multiple orders for different procedures and medications
* One medication order can give rise to multiple medication administrations

**Retail website one-to-many examples**

* One customer may have several associated addresses for shipping, billing, or both
* One customer will probably have multiple orders 
* Each order will have one or many associated items

One-to-many data relationships (one X is related to more than one Y) can be very hard to accommodate in a single table with all the data.  Imagine having a table of order information from an online website, in which a single row contained every item included in that order. 

It would be impossible to know ahead of time how many columns would be needed.  What if we provided enough columns for 100 items in an order to start?  Then, maybe someone orders 110 items.  What do we do?  Also, most orders are much smaller, which means we have many empty cells with no data in them.  It's not an efficient way to store data.  

### Quiz: One-to-Many 

Which of the following relationships are likely to be one-to-many?  Select all the correct answers.

[[X]] Gym member to workout
[[ ]] Street address to corresponding congressional district
[[X]] Patient to medical provider
[[X]] Medical provider to patient
[[ ]] Baseball team to mascot
[[?]] There are multiple correct answers!
*********

<div class = "answer">

We hope that any gym member will have more than one recorded workout, so that relationship is one-to-many.  However, a particular street address will only have one congressional district representing residents at that address.  That's not a one-to-many relationship.  A patient can have multiple providers, so that's one-to-many, and providers can have many patients, so that's also one-to-many.  In fact you could more accurately call this relationship many-to-many!  Finally, a baseball team (we argue) should have only one mascot, so that's not a one-to-many relationship.

</div>

***********

### One-to-many Data in Research

Let's consider again the data from our fictional multi-site research study on mental health and consider how its one-to-many relationships make it very unwise to try to store all of our research data in a single table.

**Table 1: `depression_scale`**

<!-- data-type="none" class="tight-table" style="font-size:80%"-->
| subj_id  | date  | dep_q1  | dep_q2   | dep_q3  | dep_q4  | dep_total   |
| :--------- | :--------- | :--------- | :--------- | :--------- | :--------- | :--------- |
| 11234   | 2021-05-15   | 3    | 3  | 2    | 4    | 12    |
| 86234   | 2021-06-01   | 4    | 4  | 3    | 4    | 15    |
| 32660   | 2021-06-10   | 1    | 1  | 2    | 1    | 5   |
| 86234   | 2022-01-13   | 2    | 2  | 1    | 3    | 8    |
| 41356   | 2022-02-10   | 1    | 3  | 2    | 3    | 10   |

**Table 2: `subject_address`**

<!-- data-type="none" class="tight-table" style="font-size:80%" -->
| subj_id  | street_address  | city  | state   | zip  | date_start  | date_end   |
| :--------- | :--------- | :--------- | :--------- | :--------- | :--------- | :--------- |
| 11234   | 123 Main Street   | Smithtown    | PA  | 19000    | 2022-01-01   | `NULL`    |
| 11234   | 123 Oak Lane   | Old Towne    | PA  | 18000   | 2000-01-01    | 2021-12-31    |
| 93452   | 123 Green Blvd  | Kirby    | TN  | 37000    | 2020-05-01    | `NULL`   |

Notice the one-to-many aspects of this data.  The subject with id 86234 has two different administrations of the depression inventory, on different dates.  The subject with id 11234 has two different addresses for two different date ranges.

**Column Conundrums**

Imagining how to consolidate this data into one single table with one row per subject is challenging.  Would we provide two sets of columns for addresses?  Maybe the column names would be "street\_address\_1", "city\_1", etc., and "street\_address\_2", "city\_2", and so on.  But this is a longitudinal study and people might move 3, 5, even 10 times! The same problem emerges with multiple administrations of the depression inventory.  If we try to combine data that can repeat into a "one row per subject" model, we don't know how many columns to create.

**Row Woes**

And it gets worse.  We don't just have to worry about columns, but also rows.  Consider the fact that we also have other, unchanging data about subjects that we'd need to include, like their demographic information (date of birth, sex, race, etc.).  If someone has four administrations of the depression inventory, do we list their sex, race, and date of birth on all four of those administrations?  That's a lot of data repetition which takes up disk space and also opens up more possibilities for errors.

**One Table?  Not a Good Idea!**

In short, if we try to force all the data we care about into a single table, we have a problem of rapidly multiplying columns and data repetition in rows.  This makes maintaining, cleaning, correcting, and understanding data very tricky.

We're much better off collecting various groups of facts about our research subjects into distinct, separate tables, like a "demographics" table, a "depression" table, an "anxiety" table, an "address" table, and so on, including a "subj\_id" column to link rows back to the subject in question.  This realization, of how we can separate data into concepts that each get a table, leads us to the idea of **normalization**.

## Normalization

When data is normalized, we organize data to reduce the possibility of needless data duplication and empty cells.  Normalization is a complex information science topic and has different degrees of completeness, so here we'll talk about what normalization **looks like** more than what it **is**.  

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>
In this module, we're discussing a kind of normalization called "third normal form", often abbreviated 3NF.  The theory behind normalization has its own challenging jargon, like "cardinality", "atomicity", "decomposition", etc.  If you get excited by database optimization and information science, you might enjoy a deep dive into normalization.  But for most of us, we only need to develop a casual understanding of how normalization affects our databases. 
</div>

**Entities: What Kinds of Things Exist?**

In a normalized database, we separate data into tables representing different logical **entities**, like "address", "procedure", "medication", "device", etc., and give each of these entities an identifier (like "device\_id" or "medication\_id") to identify a particular instance of the entity.  

This id number can also be a **primary key** if it will only appear once in the entity table (say, for an item identifier that you don't want to be duplicated).  Imagine a "medication" table with rows that include a medication id and information about that medication (like its brand name, generic name, and whether it requires a prescription).  Or think of an "item" table which includes an item id, along with details about that item like the manufacturer and description.  Each row is unique, and the id as a primary key won't repeat (SQL enforces this and won't let you add a new row with the same primary key).

We tend to only include in these entity tables the data elements that have a single value that is relatively stable (like medication generic name, device bar code, patient date of birth, or procedure CPT code).  We may exclude things from entity tables that could have multiple values or change frequently (for example, we would probably exclude patient insurance provider from the patient table).

**Interactions: How do Entities Interact?**

Then, we make tables that represent **interactions** between entities.  For example, interactions between patients and medications might be stored in a "prescriptions" or "medication\_orders" table. Interactions between addresses and devices might be in a "device\_shipment" table.  These record relationships by including the id numbers of the entities involved, along with other data like the date of the interaction and other details.  A table called "medication\_orders", for example, will include a field for the patient id, a field for the medication id, a field for the prescribing provider id, the date and time of the medication order, the dose and duration of the order, the mode of medication delivery, and other important details such as any notes made by the prescriber.

Whether these tables of interactions have primary keys and their own identifiers depends, but they often will.  For example, a "device_shipment" table might have a primary key called "device_shipment_id".

**Why Bother With Normalization?**

To show why organizing data in a normalized way is helpful, let's use an example.

Which of the following is more efficient to correct, if we want to change "orane juice" to "orange juice"? Is it easier to correct with the data stored in one table, or with the data in two tables, where items are given an id number?

**One Table Option**

**`order_and_items`**

<!-- data-type="none" class="tight-table" -->
| order_num   | item_1   | item_2  | ...  | item_50  |
| :--------- | :--------- | :--------- | :--------- | :--------- |
| 23125    | orane juice     | pistachios     | ...    | `NULL`    |
| 41320    | peanut butter    | plain bagels     | ...    | orane juice    |
| 53011    | napkins    | distilled water     | ...    | `NULL`    |
| 14123    | pistachios    | orane juice     | ...    | peanut butter    |

In the one table option, we have to look for the phrase "orane juice" anywhere in 50 columns across all rows (consider that there could be thousands of rows).

**Two Table Option**

**`items`**

*Note: here we are using the `item_id` field as a primary key as well, which is why we include `(PK)`.* 

<!-- data-type="none" class="tight-table" -->
| item_id (PK)  | item_name  |
| :--------- | :--------- |
| 15 | distilled water |
| 178 | napkins |
| 210 | orane juice |
| 97 | peanut butter |
| 108 | pistachios  |
| 233 | plain bagels  |

**`orders`**

*Note: here we want to allow the `order_id` to repeat as many times as necessary to include all items, so it's not a primary key.* 

<!-- data-type="none" class="tight-table" -->
| order_id | item_id |
| :--------- | :--------- |
| 23125 | 210 |
| 23125 | 108 |
| 41320 | 97 |
| 41320 | 233 |
| 41320 | 210  |
| 53011 | 178 |
| 53011 | 15 |
| 14123 | 108 |
| 14123 | 210 |
| 14123 | 97 |

In the two table option, we only have to find "orane juice" in a single column, "item\_name", and it occurs once only (this is because this id number is a primary key, which means it can only occur once).

The theory of how to separate data for top speed and efficiency is complex. However, it's enough for now to understand that data in SQL databases are fragmented in a process called normalization, to help reduce needless repetition, simplify data, and improve performance.

### Quiz: Why is SQL Data In So Many Tables?

Why is data normalized (carefully fragmented to reduce repetition and inefficiency) in SQL?  Select all the correct answers.

[[ ]] SQL has a limit on number of columns permitted in a table, and must break up data in order to keep tables smaller
[[X]] Because data is often one-to-many, storing data in a single table is inefficient
[[X]] Normalizing data makes correcting or changing data simpler and less prone to error
[[ ]] Normalization is a holdover from when most databases were business-related, but it not necessary in biomedical research
[[?]] There are multiple correct answers!
*********

<div class = "answer">

The reason for normalization isn't that SQL lacks the capacity for very wide tables with lots of columns.  Rather, the kind of rich data that is stored in SQL databases simply isn't right for storage in a single table.  There are many one-to-many relationships in data, and this means that using multiple tables, one for each kind of concept (like "address" or "order" or "encounter") makes sense.  There is also a lot of repetition in data.  For example, multiple patients might live at the same address, and multiple patients are prescribed the same medication.  Multiple orders each contain the same popular product.  This repetition means that it's much easier to correct or change data if we try to put as much data as possible into a single table. However, when a normalized model is used, and data is fragmented into concepts, things get easier.  Instead of correcting a product name thousands of times, once for each order that product appears on, we only have to correct it once, in the "product" table.

</div>

***********

## Forming a JOIN 

As we established earlier, JOINS are used to combine rows from two (or more) tables, based on some set of columns they have in common.

There are two basic pieces of information you need to know to write successful joins:

* What **join criteria** would you like your join evaluated against?  In other words, how are you linking rows from one table to rows from another table?  What constitutes a "match" of data from one table to data from another?  If you're joining data that holds student grades, for example, you probably want to only join data together where the student ID matches.
* What **type of join** do you want to use?  Let's say you have some students with math grades and some students with language grades.  Some students are in only the math table, some are only in the language table, and some are in both.  What part of the overlapping data do you want?  

We'll address each of these in the next few sections.

### Join Criteria

Join criteria are conditions that mean that rows from two different tables belong together.  Your criteria might be something like:

* Join the rows from "depression\_scale" with rows from "subject\_address" **... but only if the subject id field matches**
* Join the rows from "items" with the rows from "orders" **... but only if the item id field matches**
* Join the rows from "math\_grades" with the rows from "english\_grades" **... but only if the student id is the same and the semester is the same**

When the conditions in your join criteria evaluate as TRUE for a row then a join will be performed for those rows, and when the join criteria are evaluated as FALSE no join for those rows will take place.

**Data Relationships**

As a reminder, SQL is a **relational database**, so it's not surprising that we talk a lot about relationships in this module.

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

This isn't a coding module, but we're going to show some code snippets here.  This is to help you recognize the code and help set you up for learning how to practically **do** SQL JOINs.  Don't worry if you feel a bit intimidated by the code you see, you won't have to use it in this module.

</div>

Join criteria will be some sort of relationship statement referencing shared information (data that occurs in both tables you want to join) that you would like evaluated to TRUE or FALSE when resolving your join.  Often, the relationship is equality -- you're looking for a perfect match. 

For example, do you have subject identifiers in two different tables?  This shared information can be used to connect (join) data from these tables, based on the subject id being equal.  If the subject id matches, a row from table A and a row from table B will be joined.  If the subject id doesn't match, these rows won't be joined.  In code, we usually use an **ON** statement:

```sql
...
ON table_a.subject_id = table_b.subject_id
```

In this case, we're comparing the equality of two fields that have the same name, so we could also use **USING**.  This special word only applies to when you're looking for a perfect match between fields that have matching names, too.

```sql
...
USING(subject_id)
```

Sometimes the data that appears in both tables has the same field name (it's "subj\_id" in both the "depression\_scale" and "subject\_address" tables).  Sometimes the data might be stored under different names (for instance, if "semester" is used in "math\_grades" and "term" is used in "language\_grades").  So you might also see something like:

```sql
...
ON red_table.itm_num = blue_table.item_id
```
This highlights the importance of documenting your data so you can tell which fields hold which data in order to use them properly for JOINs. 

**Non-equality**

Sometimes you don't need equality exactly.  For example, in our example from our multi-site mental health research, let's say we want to associate a particular depression score with a particular address only if the depression inventory was given between the start and end dates of residency at that address. In a case like that, you might see something like:

```sql
...
ON depression_scale.date BETWEEN 
   subject_address.date_start AND 
   subject_address.date_end
```

**Multiple conditions**

Of course, in the example of the depression inventory, we'd also want to make sure that there was a match on subject identifier.  You can combine conditions too:

```sql
ON depression_scale.subj_id = subject_address.subj_id AND
   depression.date BETWEEN 
      subject_address.date_start AND 
      subject_address.date_end
```

**Getting Really Complicated**

But what if some addresses don't have end dates, because the subject is currently still living there?  You can create arbitrarily complex **boolean logic** (or **boolean algebra**), using AND, OR, NOT, and parentheses as needed.  Much as in math, there's an order of operations in this kind of logic, and you might need several sets of parentheses to make sure you're applying the conditions correctly.  For example:

```sql
ON depression.subj_id = subject_address.subj_id AND 
   ((depression.date BETWEEN 
      subject_address.date_start AND 
      subject_address.date_end) 
      OR
   (depression.date > subject_address.date_start AND 
   subject_address.date_end IS NULL))
```

**Using other tools along with JOIN**

Especially for one-to-many data relationships, you might want to create a simplified table temporarily in order to have that be part of a JOIN.  This means you may have to also do some complicated things like using GROUP BY with aggregation, using WHERE and/or HAVING, or creating subqueries.  

For example, let's say you want to only use the earliest depression inventory for each subject, not any subsequent depression inventories, for your analysis of the correlation between depression score and zip code, and then join that earliest depression inventory with the address of the subject at the time of administration.  The easiest way to do that is to first create a simplified table that only contains the earliest depression inventory for each subject id.  This is a great place to use GROUP BY and the aggregation function MIN().  Then you can use that simpler table to join to subject addresses.  

We won't show the code for this in this module, but be aware that you can think about complex JOINS by first planning how you can simplify a table to make the logic easier to work with!

### A Bit of Vocab 

Fields that appear in SQL tables which are used in your join criteria are also sometimes called **join keys**. Two categories of join keys are primary keys (which we talked about earlier) and **foreign keys**.

A primary key, you'll recall, is a column (occasionally a set of columns) that contain a unique value for each row in your table.  For example, our "item\_id" is a primary key for the "items" table in our earlier example.  There will be no repeats of the "item\_id" in the "items" table.

A foreign key is a column (or set of columns) in a table that make reference to a primary key in some other table.  For example, in our "orders" table earlier, we had a column called "item\_id", which contained numbers that corresponded to the "item\_id" column in the "items" table.  If we saw a row in the "orders" table that had "order\_id" of 34219 and "item\_id" of 15, the "item\_id" is a foreign key (*foreign* in this case meaning "not from here, originated elsewhere") that originated in the "items" table.  We could look up in that table to discover that "item\_id" 15 indicates that the order included the item "distilled water".

### Quiz: Keys

Consider the following fictional snippet of data from a table:

**medication\_order**

<!-- data-type="none" -->
| med\_ord\_id   | patient\_id   | date  | provider\_id  |
| :--------- | :--------- | :--------- | :--------- |
| 3411904326   | 834014     | 2020-01-30    | 56024     |
| 3411904329   | 320092     | 2020-01-30    | 56024     |
| 3411904330   | 612311     | 2020-01-31    | 99123     |

Which of the fields in this table is likely to be a primary key?  Select all that apply.

[[X]] med\_ord\_id
[[ ]] patient\_id
[[ ]] date
[[ ]] provider\_id
*********

<div class = "answer">

Because this table is about medication orders, and there's an identifier that looks like it uniquely identifies each of these interactions, we can guess that "med\_ord\_id" is probably a primary key.  On the other hand, we know for sure that "date" and "provider\_id" can't be primary keys, because they have repeating values.  That makes sense -- the same provider can write many different medication orders, and on any given date, there are likely to be many medication orders.  By that same logic, we also know that "patient\_id" can't be a primary key... it needs to be possible for a patient to have more than one medication order!

</div>

***********

Consider the same table.

Which of the fields in this table is likely to be a foreign key?  Select all that apply.

[[ ]] med\_ord\_id
[[X]] patient\_id
[[ ]] date
[[X]] provider\_id
*********

<div class = "answer">

A foreign key is an identifier that originates in another table.  It certainly seems likely that there is a "patient" table and a "provider" table that the "patient\_id" and "provider\_id", respectively, originated in.  These are the two foreign keys.  The "med\_ord\_id" seems to originate here, in the "medication_order" table, so it's not a foreign key, and the "date" just seems like, well, a date, not an identifier at all!

</div>

***********

### JOIN Types 

Let's consider the gradebook example we mentioned earlier.  You are assembling grade reports for students.  You have two tables, one called "math\_grades" and one called "language\_grades".  Some students appear in "math\_grades", some in "language\_grades", and some students have rows in both tables.  Depending on your purposes, you might want any one of several types of JOINs.  Let's imagine a Venn diagram, as shown below:

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

There are 4 basic JOIN types that can be used:

* **INNER JOIN**.  An **INNER JOIN** (and this is the default behavior of JOIN without any modifying words) would only include grade data falling in the "Both Math and Language Grades" overlap section.  This is often the data you want to capture.  If you're conducting research on the correlation between math and language grades, this is the JOIN you want.  If a student lacks one or the other grade, their data isn't useful to you, so you don't want it.  This shows up in code like this:

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

* **LEFT JOIN**.  A LEFT JOIN (or a LEFT OUTER JOIN as you'll sometimes see it) includes the data in "Only Math Grades" -- that's the "outer" part on the left -- and in "Both Math and Language Grades" -- the overlap section.  It would exclude student data in the "Only Language Grades" section (which is on the right).  Maybe you want this data because as the chair of the mathematics department, you want to see what students are strongest, in math, and also in language if known, in order to select who to award a math prize to. This shows up in code like this:

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
* **RIGHT JOIN**.  A RIGHT JOIN (or a RIGHT OUTER JOIN) would include the data in "Only Language Grades" -- that's the "outer" part on the right -- and for students with "Both Math and Language Grades" -- the overlap section.  It would exclude student data in the "Only Math Grades" section (which is on the left).  Maybe you want this data to create a graph of language grade distribution, and want to enrich it with some statistics about math grades where available, but it doesn't matter if some students lack math grades. This shows up in code like this:

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

* **FULL JOIN**.  A FULL JOIN (or sometimes you'll see FULL OUTER JOIN) will capture all the data -- all of the outer data on the right and left as well as the inner (overlapping) data.  This is important if you want to create a grade book that shows student grades for each student, including their math grades and/or their language grades. This shows up in code like this:

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

## Additional Resources

* A brief, very readable article that talks about one-to-many relationships and several kinds of normalization (including our normalization in this module, which is third normal form, or 3NF) can be found at <https://www.lifewire.com/one-to-many-relationships-1019756>.
* On the same site, you can read in a bit more technical detail about the various levels of normalization: <https://www.lifewire.com/database-normalization-basics-1019735>
* A great page to practice JOINS and visualize them in the form of Venn diagrams is at <https://www.w3schools.com/sql/sql_join.asp>.

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22SQL+Joins%22)!

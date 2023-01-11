<!--
author:   Joy Payton
email:    paytonk@chop.edu
version:  1.0.0
module_template_version: 3.0.0
language: en
narrator: US English Female
title: Database Normalization
comment: Learn about the concept of normalization and why it's important for organizing complicated data in relational databases.
long_description: Usually, data in a relational database like SQL is organized into multiple interrelated tables with as little data repetition as possible. This concept can be useful to apply in other areas as well, such as organizing data in .csvs or in data frames in R or Python.  This module teaches underlying data considerations and explains how data can be efficiently organized by introducing the concepts of one-to-many data relationships and normalization.
estimated_time: 40 minutes

@learning_objectives  
After completion of this module, learners will be able to:

- Explain the significance of "one to many" data relationships and how these relationships affect data organization
- Describe how a normalized database is typically organized
- Explain how data can be linked between tables and define "primary keys" and "foreign keys"

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js
-->

# Database Normalization

<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**  Learners should have experience working with data in tables.  This could included working with .csv files, SQL databases, R data frames, REDCap instruments, or other ways that data can be collected in tables. 

**Learning Objectives**

@learning_objectives

</div>

## Multiple Tables

Most data analysis tasks require something more complex than referencing data from a single table. 

For example, consider the case where you have data about a multi-site study's research subjects. One table holds depression scores for subjects and a different table holds subject addresses.  Your hypothesis is that people who live in certain zip codes have higher rates of depression.

To see if your hypothesis has evidence to back it, you need to combine data, taking the subject ID and depression score from one table, and the subject ID and zip code from another table, and combining them.  

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

You may be asking yourself, "Why don't the people collecting the data or designing the database just put all the information together in one table to start with?"  After all, getting one row per subject (or per sample, etc.) is how we usually prepare to apply statistical tests. If we could just **start** with one row per research subject in our source data, we'd be ready to jump into the science and not have so much data preparation work. 

The reason why this usually doesn't happen in a database, and you instead see lots of different tables that you have to join together is because of a concept known as **normalization**.  To explain normalization, we'll first explain **one-to-many** data relationships.

## One-to-Many

Data often has one-to-many relationships. What does one-to-many mean? Consider two use cases, a hospital and a retail website.  Each organization has one-to-many data relationships:

**Hospital one-to-many examples**

* One patient has multiple encounters on different dates.
* One encounter may include multiple orders for different procedures and medications.
* One medication order can give rise to multiple medication administrations.

**Retail website one-to-many examples**

* One customer may have several associated addresses for shipping, billing, or both.
* One customer will probably have multiple orders.
* Each order will have one or many associated items.

One-to-many data relationships (one X is related to more than one Y) can be very hard to accommodate in a single table with all the data.  Imagine having a table of order information from an online website, in which a single row contained every item included in that order. 

It would be impossible to know ahead of time how many columns would be needed.  What if we provided enough columns for 100 items in an order to start?  Then, maybe someone orders 110 items.  What do we do?  Also, most orders are much smaller, which means we have many empty cells with no data in them.  It's not an efficient way to store data.  

### Quiz: One-to-Many 

Which of the following relationships are likely to be one-to-many?  Select all the correct answers.

[[X]] Gym member to workout
[[ ]] Street address to latitude and longitude coordinates
[[X]] Patient to medical provider
[[X]] Medical provider to patient
[[ ]] Baseball team to mascot
[[?]] There are multiple correct answers!
*********

<div class = "answer">

We hope that any gym member will have more than one recorded workout, so that relationship is one-to-many.  However, a particular street address will only be related to a single latitude and longitude. That's not a one-to-many relationship.  A patient can have multiple providers, so that's one-to-many, and providers can have many patients, so that's also one-to-many.  In fact you could more accurately call this relationship many-to-many!  Finally, a baseball team (we argue) should have only one mascot, so that's not a one-to-many relationship.

</div>

***********

### One-to-Many Data in Research

Let's consider again the data from our fictional multi-site research study on mental health and consider how its one-to-many relationships make it very unwise to try to store all of our research data in a single table.

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

<!-- data-type="none" class="tight-table" style="font-size:80%" -->
| subj_id  | street_address  | city  | state   | zip  | date_start  | date_end   |
| :--------- | :--------- | :--------- | :--------- | :--------- | :--------- | :--------- |
| 11234   | 123 Main Street   | Smithtown    | PA  | 19000    | 2022-01-01   | `NULL`    |
| 11234   | 123 Oak Lane   | Old Towne    | PA  | 18000   | 2000-01-01    | 2021-12-31    |
| 93452   | 123 Green Blvd  | Kirby    | TN  | 37000    | 2020-05-01    | `NULL`   |

Notice the one-to-many aspects of this data.  The subject with subj_id 86234 has two different administrations of the depression inventory, on different dates.  The subject with subj_id 11234 has two different addresses for two different date ranges.

**Column Conundrums**
-----

Imagining how to consolidate this data into one single table with one row per subject is challenging.  Would we provide two sets of columns for addresses?  Maybe the column names would be "street\_address\_1", "city\_1", etc., and "street\_address\_2", "city\_2", and so on.  But this is a longitudinal study and people might move 3, 5, even 10 times! The same problem emerges with multiple administrations of the depression inventory.  If we try to combine data that can repeat into a "one row per subject" model, we don't know how many columns to create.

**Row Woes**
-----

And it gets worse.  We don't just have to worry about columns, but also rows.  Consider the fact that we also have other, unchanging data about subjects that we'd need to include, like their demographic information (date of birth, sex, race, etc.).  If someone has four administrations of the depression inventory, do we list their sex, race, and date of birth on all four of those administrations?  That's a lot of data repetition which takes up disk space and also opens up more possibilities for errors.

**One Table?  Not a Good Idea!**
-----

In short, if we try to force all the data we care about into a single table, we have a problem of rapidly multiplying columns and data repetition in rows.  This makes maintaining, cleaning, correcting, and understanding data very tricky.

We're much better off collecting various groups of facts about our research subjects into distinct, separate tables, like a "demographics" table, a "depression" table, an "anxiety" table, an "address" table, and so on, including a "subj\_id" column to link rows back to the subject in question.  This realization, of how we can separate data into concepts that each get a table, leads us to the idea of **normalization**.

## Normalization

When data is normalized, we organize data to reduce the possibility of needless data duplication and empty cells. 
Normalization is a complex information science topic and there are various levels of normalization that can be performed.  Here, we won't go into details about various forms of normalization, rather, we'll talk about what normalization  **looks like** more than what it **is**.  

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>
In this module, we're discussing a kind of normalization called "third normal form", often abbreviated 3NF.  The theory behind normalization has its own challenging jargon, like "cardinality", "atomicity", "decomposition", etc.  If you get excited by database optimization and information science, you might enjoy a deep dive into normalization.  But for most of us, we only need to develop a casual understanding of how normalization affects our databases. 
</div>

**Entities: What Kinds of Things Exist?**
-----

In a normalized database, we separate data into tables representing different logical **entities**, like "address", "procedure", "medication", "device", etc., and give each of these entities an identifier (like "device\_id" or "medication\_id") to identify a particular instance of the entity.  

This ID number can also be a **primary key** if it will only appear once in the entity table (say, for an item identifier that you don't want to be duplicated).  Imagine a "medication" table with rows that include a medication ID and information about that medication (like its brand name, generic name, and whether it requires a prescription).  Or think of an "item" table which includes an item ID, along with details about that item, like the manufacturer and description.  Each row is unique, and the ID as a primary key won't repeat.  If you're using a SQL database, it's very helpful to know that SQL enforces this and won't let you add a new row in a table with a primary key that already exists.

We tend to only include in these entity tables the data elements that have a single value that is relatively stable (like medication generic name, device bar code, patient date of birth, or medical procedure billing code).  We may exclude things from entity tables that could have multiple values or change frequently (for example, in the United States we would probably exclude patient insurance provider from the patient table).

**Interactions: How do Entities Interact?**
-----

Then, we make tables that represent **interactions** between entities.  For example, interactions between patients and medications might be stored in a "prescriptions" or "medication\_orders" table. Interactions between addresses and devices might be in a "device\_shipment" table.  These record relationships by including the ID numbers of the entities involved, along with other data like the date of the interaction and other details.  A table called "medication\_orders", for example, will include a field for the patient ID, a field for the medication ID, a field for the prescribing provider ID, the date and time of the medication order, the dose and duration of the order, the mode of medication delivery, and other important details such as any notes made by the prescriber.

Whether these tables of interactions have primary keys and their own identifiers depends, but they often will.  For example, a "device\_shipment" table might have a primary key called "device\_shipment\_id".

### Why Bother With Normalization?

To show why organizing data in a normalized way is helpful, let's use an example.

Consider the following example of a typo in a database. Is it easier to correct "orane juice" to "orange juice" with the data stored in one table, or with the data in two tables, where items are given an id number?

**One Table Option**
-----

**orders**

<!-- data-type="none" class="tight-table" -->
| order_num   | item_1   | item_2  | ...  | item_50  |
| :--------- | :--------- | :--------- | :--------- | :--------- |
| 23125    | orane juice     | pistachios     | ...    | `NULL`    |
| 41320    | peanut butter    | plain bagels     | ...    | orane juice    |
| 53011    | napkins    | distilled water     | ...    | `NULL`    |
| 14123    | pistachios    | orane juice     | ...    | peanut butter    |

In the one table option, we have to look for the phrase "orane juice" anywhere in 50 columns across all rows (consider that there could be thousands of rows).

**Two Table Option**
-----

**items**

*Note: here we are using the "item\_id" field as a primary key as well, which is why we include (PK) in the table header.  Often, database tools will do something similar and display a special symbol (like <span class="fa-solid fa-key"></span>) or the letters "PK" to draw your attention to the fact that a particular field is a primary key.* 

<!-- data-type="none" class="tight-table" -->
| item_id (PK)  | item_name  |
| :--------- | :--------- |
| 15 | distilled water |
| 178 | napkins |
| 210 | orane juice |
| 97 | peanut butter |
| 108 | pistachios  |
| 233 | plain bagels  |

**order_items**

*Note: here we want to allow the "order\_id" to repeat as many times as necessary to include all items, so it's not a primary key.* 

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

In the two table option, we only have to find "orane juice" in a single column, "item\_name", and it occurs once only (this is because this ID number is a primary key, which means it can only occur once).

The theory of how to separate data for top speed and efficiency is complex. However, it's enough for now to understand that data in relational databases are fragmented in a process called normalization, which 
- helps reduce needless repetition, 
- simplifies data, 
- and improves system speed and performance.

### Quiz: Normalization

Why is data normalized (carefully fragmented to reduce repetition and inefficiency) in relational databases?  Select all the correct answers.

[[ ]] Relational database systems have a limit on number of columns permitted in a table, and must break up data in order to keep tables smaller.
[[X]] Because data is often one-to-many, storing data in a single table is inefficient.
[[X]] Normalizing data makes correcting or changing data simpler and less prone to error.
[[ ]] Normalization is a holdover from when most databases were business-related, but it is not necessary in biomedical research.
[[?]] There are multiple correct answers!
*********

<div class = "answer">

The reason for normalization isn't that relational database software lacks the capacity for very wide tables with lots of columns.  Rather, the kind of rich data that is stored in relational databases simply isn't right for storage in a single table.  There are many one-to-many relationships in data, and this means that using multiple tables, one for each kind of concept (like "address" or "order" or "encounter") makes sense.  There is also a lot of repetition in data.  For example, multiple patients might live at the same address, and multiple patients are prescribed the same medication.  Multiple orders each contain the same popular product.  This repetition means that it's much easier to correct or change data if we try to put as much data as possible into a single table. However, when a normalized model is used, and data is fragmented into concepts, things get easier.  Instead of correcting a product name thousands of times, once for each order that product appears on, we only have to correct it once, in the "product" table.

</div>

***********

## Key Vocabulary <span class="fa-solid fa-key"></span>

Fields that appear in two or more tables within a database are also sometimes called **join keys**, because they can be used to join data from the two tables into one set of interrelated data.  Two categories of join keys are primary keys (which we talked about earlier) and **foreign keys**.

A **primary key**, you'll recall, is a column (occasionally a set of columns) that contain a unique value for each row in your table.  For example, the "item\_id" is a primary key for the "items" table in our earlier example.  There will be no repeats of the "item\_id" in the "items" table.

**items**

<!-- data-type="none" class="tight-table" -->
| item_id (PK)  | item_name  |
| :--------- | :--------- |
| 15 | distilled water |
| 178 | napkins |
| 210 | orane juice |
| 97 | peanut butter |
| 108 | pistachios  |
| 233 | plain bagels  |


A **foreign key** is a column in a table that make reference to a primary key in some other table.  For example, in our "order\_items" table earlier, we had a column called "item\_id", which contained numbers that corresponded to the "item\_id" column in the "items" table.  If we saw a row in the "order\_items" table that had "order\_id" of 34219 and "item\_id" of 15, the "item\_id" is a foreign key (*foreign* in this case meaning "not from here, originated elsewhere") that originated in the "items" table.  We could look up in that table to discover that "item\_id" 15 indicates that the order included the item "distilled water".

**order_items**

*The second column here is a foreign key.  Sometimes (but not always!) you will see this noted in database diagrams as (FK) or a symbol like <span class="fa-solid fa-key"></span>.*

<!-- data-type="none" class="tight-table" -->
| order_id | item_id (FK) |
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


## Additional Resources

* A brief, very readable article that talks about one-to-many relationships and several kinds of normalization (including our normalization in this module, which is third normal form, or 3NF) can be found at https://www.lifewire.com/one-to-many-relationships-1019756.
* On the same site, you can read in a bit more technical detail about the various levels of normalization: https://www.lifewire.com/database-normalization-basics-1019735.


## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Database+Normalization%22)!

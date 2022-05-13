<!--
author:   Peter Camacho
email:    camachop@chop.edu
version:  1.0.0
module_template_version: 2.0.0
language: en
narrator: US English Male
title: Demystifying SQL
comment:  SQL is a relational database solution that has been around for decades.  Learn more about this technology at a high level, without having to write code.
long_description: Do you have colleagues who use SQL or refer to "databases" or "the data warehouse" and you're not sure what it all means?  This module will give you some very high level explanations to help you understand what SQL is and some basic concepts for working with it.  There is no code or hands-on application in this module, so it's appropriate for people who have zero experience and want an overview of SQL.
estimated_time: 40 minutes

@learning_objectives  

After completion of this module, learners will be able to:

- Define the acronym "SQL"
- Explain the basic organization of data in relational databases
- Explain what "relational" means in the phrase "relational database"
- Give an example of what kinds of tasks SQL is ideal for

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Demystifying SQL

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


## SQL: A Definition

To put it simply, **SQL** (**S**tructured **Q**uery **L**anguage) is a programming language used to interact with "**Relational Databases**".  You can pronounce it as "sequel" or just say the letters S-Q-L.

That definition above itself introduces a new term.  So, what's a **relational database**?

Let's start with the word "**database**".  A database is a data storage solution that stores data in objects called tables.  Tables are objects comprised of columns (sometimes called 'fields') and rows (similar to data in an Excel spreadsheet or .csv file).

When we add "**relational**" as a modifier, we mean that tables within the database are **related** to one another by columns they have in common (like a customer or patient id column that appears in several different tables).  

Consider, for example, these three sample tables.  They are rectangular (or tabular) in shape and organize data in rows and columns.  Can you identify the column in common?  How could you figure out how many times Prairie Dawn had an encounter with `ed_ind` equal to 1?

<h4>A Sample `demographics` table</h4>

<!-- data-type="none" -->
| patient_id | date\_of\_birth | sex | last_name | first_name |
| -------    | -----------   | -   | ------    | ----- |
| ABC123     | 1970-03-15    | M   | Bird      | Big |
| TRSH789    | 1985-08-20    | M   | the Grouch | Oscar |
| SMLE321    | 1990-12-12    | F   | Dawn      | Prairie |

<h4>A Sample `encounters` table</h4>

<!-- data-type="none" -->
| patient_id | encounter_id | encounter_date | ed_ind |
| ---------- | ------------ | -------------- | ------ |
| SMLE321    | 8827371048   |  2020-03-10    | 1      |
| SMLE321    | 8829502289   |  2020-09-05    | 0      |
| TRSH789    | 8837498101   |  2020-11-29    | 0      |
| TRSH789    | 8871386401   |  2021-04-01    | 0      |
| SMLE321    | 8901861569   |  2021-11-22    | 1      |
| ABC123     | 8927551899   |  2021-12-30    | 0      |
| ABC123     | 8954998113   |  2022-03-19    | 1      |


<h4>A Sample `medication_order` table</h4>

<!-- data-type="none" -->
| patient_id | provider_id | med_id | order_date |
| -------    | -----------   | --- | ------    | ----- |
| ABC123     | 491272    | 8000412   | 2021-05-15 |  
| ABC123     | 491272  | 7960004   | 2022-02-01 |
| SMLE321    | 223618    | 8000412 | 2020-08-19 |

The primary benefit of the **relational database** model is the ability to use columns containing the same data (things like patient IDs) to create complex reports combining information from multiple tables.  This enables users of the data to derive specific information from the data in highly customizable ways.

Now that you have that background, you can think of SQL as the computer code (the "Language" in Structured Query Language) that you can use to ask explicit questions (the "Query" in SQL) about the information in your Relational Database.

<div class = "hint">

Where did SQL come from?  SQL was created in the early 1970's by IBM as a method for more easily accessing information from their internal database system.

By 1979 Relational Software, Inc. (now Oracle Corporation) released the first commercially available implementation of SQL as a part of their Oracle V2 database application.

Today SQL is the most common programming language for extracting and organizing data in relational database systems.

</div>


### Quiz: SQL and Relational Databases

<div class = "question">

What does "SQL" stand for?

[[ ]] Sequential Query Language
[[X]] Structured Query Language
[[ ]] Simple Question Language
[[ ]] Syntactic Question Language
[[ ]] Structured Questing Language
*********

<div class = "answer">
SQL, which can be pronounced "sequel" or S-Q-L, stands for Structured Query Language!
</div>

***********
</div>

<div class = "question">

Which of these correctly describe relational databases?  Choose all the correct options.

[[ ]] Relational databases are an alternative to SQL
[[X]] Relational databases organize data into tables
[[ ]] Tables in relational databases are organized into ranks and files
[[X]] Relational databases permit the extraction of highly specific data
[[X]] The "relational" in "relational database" refers to data that occurs in multiple places and allows for linking, or "relating" data
*********

<div class = "answer">
Relational databases are a data storage solution and they store data in tables, which are in turn organized into rows and columns.  Relational databases use SQL as a way to access data, search for data meeting particular conditions, and connect related data, using columns that tables have in common.  This allows for extracting data in very specific and customized way.
</div>

***********

</div>

### When to Use SQL

SQL should be used any time you need to access data stored within a relational database and select data that meets your requirements.

Usually, SQL is used for getting custom datasets for export and downstream analysis.  For example, you might use SQL to export data for doing statistical analysis and visualization in other languages like R, Python, or Stata.

If your source data comes from a relational database (like a data warehouse), your major data transformations (like selecting just the columns you care about or selecting only certain rows) should be done using SQL. This ensures that the dataset you export from the relational database is pretty close to the final data you will analyze or visualize.

This is because, especially for large datasets, SQL is a much more efficient tool for large-scale data transformations than your traditional scripting or analytic packages.

<div class = "hint">
If you think about carving a sculpture out of stone or wood, you can imagine that the rough work of getting rid of big slabs of material that aren't needed can be done with powerful instruments like chainsaws or jackhammers.  Then, when an artist gets close to the shape of the final product, they might switch to smaller tools to give the sculpture its final form.  In this analogy, SQL is the heavy duty tool that gets your data close to its final form.
</div>

It's a good idea to document your SQL queries and save them, because this allows you to show your steps and give data provenance.  This helps with reproducibility and standardization of your work, and might help provide a place to start for future projects.

### When SQL Isn't the Right Tool

Although SQL is a great tool for organizing your data into meaningful datasets for extraction, it is usually not a great tool to use for your actual analysis work.

Despite having many functions for simple text parsing, SQL is not the tool/language you want to use for advanced NLP (Natural Language Processing) work.  Similarly, SQL has some basic statistical functions, but isn't intended to provide statistical analysis at the level of a statistical programming language like R.

SQL also doesn't have any capabilities to directly support data visualization work.

For all of these "downstream analytics" use cases, you will want to use an actual analytical programing language or tool like R or Python.

### SQL Implementations

Although all SQL implementations have a similar structure, and the same basic syntax, each different SQL database product often has its own minor variations in dialect.

Colloquially people often refer to the different SQL dialects as different "flavors" of SQL.

Some popular "flavors" of SQL:

* [**MySQL**](https://www.mysql.com/) (open source)
* [**SQLite**](https://www.sqlite.org) (open source)
* [**PostgreSQL**](https://www.postgresql.org/) (open source)
* [**Oracle**](https://www.oracle.com/database/technologies/appdev/sql.html) (proprietary)
* [**BigQuery**](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax) (proprietary)

The most common difference between different SQL "flavors" are the availability of different functions that users can use for data manipulation, as well as the types of error messages that will be returned to the user when running code with syntax issues.

That said, knowing the specific "flavor" of SQL your database uses is especially useful when first getting started writing queries and troubleshooting errors.

## SQL Queries

A SQL **query** is essentially a question or request for data, written in a specific structure.  Let's take a closer look at how to compose a SQL query!

<div class = "care">
If you feel anxious when you see code, you have a great opportunity in this module.  We're going to give some simple examples of SQL code to help build your intuition about SQL.  You **won't** have to run any code and we're only going to barely scratch the surface of SQL **syntax** (supported commands and how to write them -- the grammar and vocabulary of SQL).  This will help build your intuition about what SQL is good at (picking out just the right data).
</div>

At a high level, we generally provide three pieces of information when constructing SQL "**queries**":

 1. The name of the **table(s)** where the data is stored.
 2. The **column name(s)** you want to look at from the table(s) you specified.  Want all the columns?  You can use an asterisk!
 3. Any **filtering condition(s)** you want to apply to your data pull.  This part is optional but is often used.

You put these basic pieces of information together using the syntax shown below to create a SQL query:

```sql
SELECT _2_ FROM _1_ WHERE _3_;
```

For example, here are some sample queries, each of which take place on just a single table.

```sql
SELECT price FROM products WHERE product_type = "FRUIT";

SELECT mpg, transmission_type FROM cars;

SELECT * FROM patients WHERE age < 20;
```

### SELECT and FROM

A **select statement** is used to specify which columns you would like to have returned as output from your SQL query.

The basic components of a select statement are the `SELECT` and `FROM` keywords. The `FROM` keyword is used to specify the table or tables that hold the data you're interested in, and the `SELECT` keyword is used to provide a list of columns within those table(s) that you would like returned as output.  

<div class = "hint">
Many people choose write SQL keywords in all capital letters, but that's so that they stand out clearly in SQL code, not because it's a language requirement.  
</div>

**Select All Columns**

If you would like to return **all** of the columns from the table(s) specified in your SQL query, you can use the `*` wild card character as shown in the example below.  You'll notice that we put a line break between the asterisk and the `FROM` keyword.  Spaces and line breaks, or **whitespace**, don't really matter for SQL.  You can run your code together on a single line, or (preferably) add intendation and spaces that help human readers understand your code more easily.

```sql
SELECT *
FROM patient;
```

**Select Specific Columns**

If you would only like to return a specific set of columns in your select statement you will need to explicitly list out each of those columns after the `SELECT` keyword, with each separate column name separated by a comma:

```sql
SELECT last_name, first_name, date_of_birth, sex
FROM patient;
```

### WHERE

The **where clause**, using the `WHERE` keyword, is the section of your query used to specify any "filtering logic" that should be applied to your query before returning any output.  It's optional but very useful.

The below example uses the where clause to filter output on only those records that represent female patients.

```sql
SELECT *
FROM patient
WHERE sex = "F";
```

Although the above example lists only one constraint for the dataset, the **where clause** can contain any number of filtering arguments needed.

Here's a more complex example:

```sql
SELECT *
FROM patient
WHERE sex = "F" AND date_of_birth >= '2019-01-01';
```

### Quiz: SQL Tasks

<div class = "question">

Which of these correctly describe the strengths of SQL?

[[X]] SQL is particularly well suited to finding data that meets your requirements
[[ ]] SQL is often used for data visualization purposes
[[X]] SQL can pick just the columns you want as well as only the rows that meet some conditions
[[ ]] SQL is a good solution for complex language processing
[[X]] SQL is a good choice for storing data that can be organized in tables with rows and columns.
[[?]] There are multiple correct answers!
*********

<div class = "answer">
SQL is great at working with rectangular data, data that is stored in tables with rows and columns.  Its powerful SELECT / FROM / WHERE syntax makes SQL an ideal tool for isolating just the data you care about, whether that's specifying the columns you're interested in or limiting your data to just those rows that meet certain conditions.  However, it's not great for fine-tuned statistical, linguistic, or data visualization purposes.  
</div>

***********

</div>

## Recap

In this module, you learned about the language SQL, which is an acronym for "Structured Query Language".  It's a powerful tool for requesting specific subsets of data from a relational database, and has been around since the 1970's because of its efficiency and utility.  

We also introduced you to two important elements of the language:

* The "select" statement, which uses `SELECT` and `FROM`
* The "where" statement, which uses `WHERE`

We also discussed what SQL doesn't provide, like robust language and statistical processing and data visualization.  SQL is a tool that ordinarily is used in concert with other tools, each one used in its area of greater strength.

Finally, you learned about the structure of relational databases: data stored in tables, which are comprised of rows and columns.  Columns may contain identifers that allow data from different tables to be related to one another, and that's why the word "relational" appears.

## Additional Resources

* Khan Academy's [Introduction to SQL](https://www.khanacademy.org/computing/computer-programming/sql) is high quality and easy to learn from.

* [What is SQL?](https://education.arcus.chop.edu/sql-intro/) is a brief introduction to SQL similar to the material in this module.

* If you are interested in the history of technology, [Early History of SQL](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6359709) is a comprehensive look into how SQL has evolved.  It's very jargon-dense!

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Demystifying+SQL%22)!

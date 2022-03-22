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
estimated_time: 45 minutes

@learning_objectives  

After completion of this module, learners will be able to:

- Explain the basic organization of data used by SQL
- Explain what "relational" means in the phrase "relational database"

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

To put it simply, SQL (**S**tructured **Q**uery **L**anguage) is a programming language used to interact with "**Relational Databases**".  You can pronounce it as "sequel" or just say the letters S-Q-L.

That definition above itself introduces a new term.  So, what's a **relational database**?

Let's start with the word "**database**".  A database is a data storage solution that stores data in objects called tables.  Tables are objects comprised of columns and rows (similar to data in an Excel spreadsheet or .csv file).

When we add "**relational**" as a modifier, we mean that tables within the database are **related** to one another by columns they have in common (like a customer or patient id column that appears in several different tables).  These columns in common are sometimes referred to as "join keys".

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

The primary benefit of the **relational database** model is the ability to use columns containing the same data ("join keys") to create complex reports combining information from multiple tables.  This enables users of the data to derive specific information from the data in highly customizable ways.

Now that you have that background, you can think of **SQL** as the computer code (the "Language" in **S**tructured **Q**uery **L**anguage) that you can use to ask explicit questions (the "Query" in SQL) about the information in your Relational Database.

### SQL Implementations

Although all **SQL** implementations have a similar structure, and the same basic syntax, each different **SQL** database product often has its own minor variations in dialect.

Colloquially people often refer to the different **SQL** dialects as different "flavors" of **SQL**.

Some Popular "Flavors" of **SQL**:

* [**MySQL**](https://www.mysql.com/) (open source)
* [**SQLite**](https://www.sqlite.org) (open source)
* [**PostgreSQL**](https://www.postgresql.org/) (open source)
* [**Oracle**](https://www.oracle.com/database/technologies/appdev/sql.html) (proprietary)
* [**BigQuery**](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax) (proprietary)

The most common difference between different **SQL** "flavors" are the availability of different functions that users can use for data manipulation, as well as the types of error messages that will be returned to the user when running code with syntax issues.

That said, knowing the specific "flavor" of **SQL** your database uses is especially useful when first getting started writing queries and troubleshooting errors.

###

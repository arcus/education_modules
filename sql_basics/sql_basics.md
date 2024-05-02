<!--
module_id: sql_basics
author: Peter Camacho; Joy Payton
email: camachop@chop.edu; paytonk@chop.edu
version: 1.3.0
current_version_description: Add three new additional resources
module_type: standard
docs_version: 3.0.0
language: en
narrator: US English Male
mode: Textbook
title: SQL Basics
comment:  Structured Query Language, or SQL, is a relational database solution that has been around for decades.  Learn how to do basic SQL queries on single tables, by using code, hands-on.
long_description: Do you want to learn basic Structured Query Language (SQL) either to understand concepts or prepare for access to a relational database?  This module will give you hands on experience with simple queries using keywords including SELECT, WHERE, FROM, DISTINCT, and AS.  We'll also briefly cover working with empty (NULL) values using IS NULL and IS NOT NULL.  This module is appropriate for people who have little or no experience in SQL and are ready to practice with real queries.
estimated_time_in_minutes: 60

@pre_reqs
Experience working with rectangular data (data in rows and columns) is required, as is some exposure to the idea of SQL and its use of tables with rows and columns.  No experience writing SQL code is expected or required for this module.  If you would like a code-free overview to SQL we recommend our module [Demystifying SQL](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_sql/demystifying_sql.md#1).
@end

@learning_objectives  
After completion of this module, learners will be able to:

- Use SELECT, FROM, and WHERE to do a basic query on a SQL table
- Use IS NULL and IS NOT NULL operators to work with empty values
- Explain the use of DISTINCT and how it can be useful
- Use AS and ORDER BY to change how query results appear
- Explain why the LIMIT keyword can be useful
@end

good_first_module: false
data_domain: ehr
data_task: data_wrangling
collection: learn_to_code
coding_required: true
coding_level: basic
coding_language: sql
sequence_name: sql

@sets_you_up_for

@end

@depends_on_knowledge_available_in

@end

@version_history
Previous versions: 

- [1.2.2](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/3607dfd4824bc9fe39edbdc62a47e28d0a863c7a/sql_basics/sql_basics.md#1): Improve large table display with collapsible sections
- [1.1.1](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/1181e69889461e8a1cb887c9e7887c77c61d5a9d/sql_basics/sql_basics.md#1): Add solutions and definitions; update challenge solutions, after code blocks, highlight boxes, and metadata; fix typos.
- [1.0.2](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/a4ea7a7f1f9264dabe952b68941fc9f0f656c9fc/sql_basics/sql_basics.md#1): Initial version.
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_sql.md
-->

# SQL Basics
@overview

## SQL: A Brief Refresher

**SQL** (**S**tructured **Q**uery **L**anguage) is a language that for more than four decades has been used to interact with **relational databases**.  You can pronounce it as "sequel" or just say the letters S-Q-L.

A relational database is a data storage solution that stores data tables, which are comprised of columns (also called 'fields') and rows.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Sometimes we'll use the word "column" and sometimes we'll use the word "field".  These refer to the same thing!

</div>

SQL is great at working with rectangular data, data that is stored in tables with rows and columns / fields.  Its powerful SELECT - FROM - WHERE syntax makes SQL an ideal tool for isolating just the data you care about, whether that's specifying the columns you're interested in or limiting your data to just those rows that meet certain conditions.  However, it's not great for fine-tuned statistical, linguistic, or data visualization purposes.  SQL is therefore a tool that is often partnered with other tools like R or Python, which are better suited for work like statistical analysis.

If you want to review SQL at a high level, consider our [Demystifying SQL](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_sql/demystifying_sql.md#1) module.

## Lesson Preparation
@lesson_prep_sql

## SQL Implementations

Although all SQL implementations have a similar structure, and the same basic syntax, each different SQL database product often has its own minor variations in dialect.

Colloquially people often refer to the different SQL dialects as different "flavors" of SQL.

Some popular "flavors" of SQL:

* [**MySQL**](https://www.mysql.com/) (open source)
* [**SQLite**](https://www.sqlite.org) (open source)
* [**PostgreSQL**](https://www.postgresql.org/) (open source)
* [**Oracle**](https://www.oracle.com/database/technologies/appdev/sql.html) (proprietary)
* [**BigQuery**](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax) (proprietary)

The most common difference between different SQL "flavors" are the availability of different functions that users can use for data manipulation, as well as the types of error messages that will be returned to the user when running code with syntax issues.

That said, knowing the specific flavor or dialect of SQL your database uses is especially useful when first getting started writing queries and troubleshooting errors.  

In the hands-on portion of this module, we'll be using a form of SQL that actually runs in your web browser as you look at these pages.  This lightweight SQL engine is called "AlaSQL".  We pre-populated some tables for you to experiment with in this module.  These tables are filled with fabricated data meant to look a little like an electronic health record (EHR).  Rest assured that this data was completely invented, although it might look realistic!

## SQL Queries

A SQL **query** is essentially a question or request for data, written in a specific structure.  Let's take a closer look at how to compose a SQL query!

At a high level, we generally provide three pieces of information when constructing SQL queries:

 1. The name of the **table(s)** where the data is stored.
 2. The **column name(s)** you want to look at from the table(s) you specified.  Want all the columns?  You can use an asterisk!
 3. Any **filtering condition(s)** you want to apply to your data pull.  This part is optional but is often used.

You put these basic pieces of information together using the syntax shown below to create a SQL query:

```sql
SELECT _2_ FROM _1_ WHERE _3_;
```

For example, here are some sample queries, each of which take place on just a single table.  To be extra clear, we're ending each query with a semicolon, which tells SQL you're done with a query.  If you're working interactively with SQL, one query at a time, you can sometimes get away with not ending your query with a semicolon.  Still, one of the things we're interested in doing in this module is instilling good practices from the start, so we encourage you to always end your queries with proper punctuation.

<!-- data-readOnly="true" -->
```sql
SELECT price FROM products WHERE product_type = "FRUIT";

SELECT mpg, transmission_type FROM cars;

SELECT * FROM patients WHERE age < 20;
```

Please note that while we write these queries all on a single line to show you a few examples in just a little space, that's the last time you'll see that kind of SQL in this module.  We have some strong opinions about SQL style here that we'll share in the next section.

### An Aside About Style

Style is how we choose to write SQL or other languages, within the confines of syntax.  

All of the following queries are valid and would work.  What distinguishes them?  Style.  

<!-- data-readOnly="true" -->
```sql
select price, best_by_date, sale_pct, quantity from products where product_type = "FRUIT";
```

<!-- data-readOnly="true" -->
```sql
SELECT price, best_by_date, sale_pct,
quantity from products WHERE
product_type = "FRUIT";
```

<!-- data-readOnly="true" -->
```sql
SELECT
  price
  ,best_by_date
  ,sale_pct
  ,quantity
FROM products
WHERE product_type = "FRUIT";
```
There's nothing to stop you from writing a long query on a single line -- a line that might not wrap around and instead go "off the screen", depending on how you are looking at the query.  There is no SQL-level enforcement of line breaks or indentation.  You are free to write SQL as you see fit, but we encourage you to adopt specific conventions and hold yourself to them.

You may be working with a group that has an established SQL style guide, either in written form or as oral tradition.  If so, great!  Ignore the style suggestions we offer and do what they suggest.  Style is nothing more than a convention to help humans read and write code more easily, and it's a good idea to go along with what is already broadly understood within your team.  Everyone agreeing on conventions like when to start a new line and how and where to comment means it's easier for other people to help you with your code or for you to copy / paste from existing examples your peers share with you.

But if you don't have anyone to guide you in style, we'll do our best to instill some basic principles. It might seem silly to start talking about style now with very short queries, but we encourage you to develop good habits now.  We are going to advocate for some style conventions that not everyone will share.  As they say, there's no accounting for taste, and if you depart from our suggestions, that's fine -- but do start to develop your own standards for style, because it will help you immensely once your SQL queries get to be 5, 10, or 100 lines long and the number of queries you write increases.

Here are our (opinionated but not necessarily "right") style suggestions.  These might not make sense right now, but once you see them in actual queries, we think you'll understand them more intuitively.

1) **Put keywords in CAPITAL LETTERS so they stand out.**  Examples of keywords are SELECT, LIKE, AS, WHERE, JOIN, DISTINCT, MEAN, ORDER BY, and many more.  While most code editors and SQL clients (software that lets you query a database) do a good job of color-coding these special words, you might end up seeing a SQL query in monochrome, and having keywords stand out helps you figure out where each part of your query is.  

2) **Put members of a list on separate lines.**  This usually means the list of fields you're requesting.  Putting each item on its own line is easier on the eyes and allows for much easier cut-and-paste to rearrange things.  It also means you have space after each item of the list to add a comment if necessary.

3) **Use indentation to clarify the various sections of your query.**  Indenting the list of columns below a SELECT statement is a way of subordinating those lines to the SELECT, subtly indicating that those lines are a continuation of the SELECT statement.  A new line that isn't indented (say, a FROM statement) shows that the SELECT part of the query is over.

4) **Use "dot notation"**, which we'll talk about in the next section.  Dot notation means adding more information about your data, for example, by including the table name the column comes from.  This practice will prepare you for using multiple data sources in your queries.

5) **Use a comma-first style.**  This one can be a little jarring at first, but it does have real advantages, especially if you end up doing SQL for more than a few hours a week.  In a list of length n, don't put the comma **after** items 1 through n-1.  Rather, put the comma **before** items 2 through n.  

<div class = "options">
<b style="color: rgb(var(--color-highlight));">Another option</b><br>

As long as you put a comma between the columns you are requesting (but not after the last column), your syntax is valid.  However, we propose a "comma-first" syntax.  To explain what comma-first syntax looks like, here are two shopping lists.  One is in comma-first style, where the first item is lacking a comma, and the other is comma-last, where the last item is missing a comma:


| comma-first (or leading comma) | comma-last (or trailing comma) |
| --- | ---- |
| apples | apples, |
| ,oranges | oranges, |
| ,lettuce | lettuce, |
| ,olives  | olives |


A comma-first stance is not uncontroversial, and some people find this style distracting or hard to understand.  If you hate it, you don't have to use it.  But first, allow us to share our rationale. Our thinking behind proposing a "comma-first" notation is based in ease of editing and improving your code as you go:

* **Commas line up.** In the comma-first example, it's easy to spot if you've left a comma out, because they all line up on the same character.  Not so in the comma-last version.  A missing comma will cause your SQL to not execute, and that's annoying and costs you extra time to track down which is the offending line.
* **It's easy to rearrange columns 2-n.** In SQL we often try a short query with just a few fields, then add a few more, then maybe rearrange their order, and finally delete the columns we don't need.  Usually, the first item in a list of columns is something of central importance, while the others in the list have a higher likelihood to be ones you may decide you don't need, or will change the order of.  Because you rarely touch the first item in a list but more frequently change the last item, it's less likely that you'll introduce a missing (or extra) comma using a comma-first paradigm as compared to the comma-last style.
* **You won't accidentally add a comma after your last item.** The reasoning is the same as above.  Anyone who's done SQL for very long has accidentally added a comma after the last item and spent a few minutes scratching their head trying to figure out what the error is.

</div>

Now that we've got you thinking about style, let's move on to the substance of SQL and work with SELECT and FROM.

### SELECT and FROM

A **SELECT statement** is used to specify which columns (or fields, we use both terms interchangeably here) you would like to have returned as output from your SQL query.

The basic components of a select statement are the `SELECT` and `FROM` keywords. The `FROM` keyword is used to specify the table or tables that hold the data you're interested in, and the `SELECT` keyword is used to provide a list of columns within those table(s) that you would like returned as output.  

**Select All Columns**

If you would like to return **all** of the fields from the table(s) specified in your SQL query, you can use the `*` wild card character as shown in the example below.  You'll notice that we put a line break between the asterisk and the `FROM` keyword.  Spaces and line breaks (together, called **whitespace**) don't really matter for SQL.  You can run your code together on a single line, or (as we strongly suggest) use styled whitespace such as predictable line breaks and indentation.

Notice that the `FROM` line of this query is followed by 2 words separated by a period. This format is known as "**dot notation**".  Dot notation is usually something like `dataset_name.table_name.column_name`.  Some dialects of SQL might require some special notation, like backticks (`\``) around part of the dot notation, but we don't need that for your hands on work here.

So the first word in the dot notation below is "alasql", which is the name of the **schema** or **catalog** or **dataset** that your data is stored in (terms differ according to the dialect of SQL that you're using), and the second word, "patients", is the name of the specific table you would like to reference as the base of your query.

Ready to try this?  Hit the execute button below the SQL code to run this query.  Because the results here are large on the screen, we've put the results in a collapsible section that you can close when you're finished looking at them!

```sql
SELECT *
FROM alasql.patients;
```
@AlaSQL.eval("#dataTable7a")

<details open>

<summary>**Results of Query (click to collapse or expand this section)**</summary>

<table id="dataTable7a" border="1"></table>

</details><br/><br/>

Now, complete the code below.  How would you get all the fields from the table `alasql.allergies`?  

It might help to hide the query results from the query above, by clicking beside "Results of Query."  That way you can see the SQL query we used, and model your code on the query above!

When you think you have it, add the code in the box below and try running the query to see if you get it right.


```sql
SELECT
FROM  ;
```
@AlaSQL.eval("#dataTable7b")


<details open>

<summary>**Results of Query (click to collapse or expand this section)**</summary>

<table id="dataTable7b" border="1"></table>

</details><br/><br/>
<div style = "display:none;">

@AlaSQL.buildTable_patients
@AlaSQL.buildTable_allergies

</div>

<details>
<summary style = "margin-bottom: 1rem;">*If you have given it a good try and are stuck trying to show all of the `allergies` table ... click here to show/hide an answer!*</summary>

Try:

```sql
SELECT * 
FROM alasql.allergies;
```

</details>

**Select Specific Columns**

If you would only like to return a specific set of columns in your select statement you will need to explicitly list out each of those columns after the `SELECT` keyword, with each separate column reference separated by a comma.  Note that this time, our dot notation is in the form `table_name.column_name` for our columns, and `dataset_name.table_name` for our table.  We do this to be very explicit about which data we mean.  

It may seem obvious that if we're getting data from the `patients` table (after all, we have that information in the FROM statement), that all of our columns come, well, from `patients`.  Why, then, do we use dot notation to specify that in the list of columns in the SELECT statement?  Why say `patients.id` when `id` alone would work just as well?  

This is an example of forming a good habit early.  You will eventually need to do queries that involve multiple tables, which may each have identical column names.  In that case, you **do** have to indicate which table you're referring to, in order to disambiguate which `date` column you mean -- do you mean `date` in `encounters`, or `date` in `medication_administration`?  Rather than learn dot notation later, we want to introduce you to it now, even if it feels unnecessary.

Go ahead and run this code by clicking the execute button.  How are your results different from the `SELECT *` query you ran previously?

```sql
SELECT
  patients.id
  ,patients.sex
  ,patients.race
  ,patients.ethnicity
  ,patients.state
FROM alasql.patients;
```
@AlaSQL.eval("#dataTable7c")


<details open>

<summary>**Results of Query (click to collapse or expand this section)**</summary>

<table id="dataTable7c" border="1"></table>

</details><br/><br/>


<div style = "display:none;">

@AlaSQL.buildTable_patients

</div>

### DISTINCT

The `DISTINCT` clause in **SQL** can be placed directly after the `SELECT` key word, and can be used to limit your result set to only the unique row values.  

This can be especially useful when exploring a dataset for the first time and trying to become familiar with the data in each column of a given table.  For example, perhaps you want to see all the possible values for `sex` or `race` in the `patients` table, to understand a bit more about the data collection options.  If you were to use `SELECT` by itself to get just the `race` field from the `patients` table, you'd get the race of every patient, with lots of repeats.  If you used `SELECT DISTINCT` instead, you'd get a much shorter list of every possible value for `race`, each listed just once.  

You can also explore using `SELECT DISTINCT` on more than one field.  The code block below provides an example of using this syntax to investigate the unique combinations of values from the `sex` and `ethnicity` columns from the `patient` table.  As you can see, the `DISTINCT` clause will work on any number of columns.  Go ahead and execute this code to see the results.  

Then, if you're up for a challenge, change the code to find out what unique combinations there are of race and ethnicity!


```sql
SELECT DISTINCT
  patients.sex
  ,patients.ethnicity
FROM alasql.patients;
```
@AlaSQL.eval("#dataTable8a")

<table id="dataTable8a" border="1"></table>


<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Here's a pro tip!  The `DISTINCT` keyword is especially useful for removing duplicates rows from the result set of your SQL queries.  If you suspect that there may be duplicate data, you can use `SELECT DISTINCT` to make sure you only get one copy of any identical rows of results.  

However, if you notice an increasing reliance on `SELECT DISTINCT` to eliminate troublesome duplication, you might want to ask the deeper question of what is creating duplicate records.  This could be a symptom of a poorly written query further up in your analysis, or a problem with the underlying data.  Because `SELECT DISTINCT` requires each row of output to be compared with every other row, it is computationally expensive.  This doesn't matter much when you're looking at a field or two (like we did to see the possible combinations of sex and ethnicity), but can cause slowness when you are using `SELECT DISTINCT` across many fields (like a `SELECT DISTINCT *` query).

</div>

<div style = "display:none;">
@AlaSQL.buildTable_patients
</div>


<details>
<summary style = "margin-bottom: 1rem;">*Click here to show/hide challenge answer.*</summary>

Try:

```sql
SELECT DISTINCT
  patients.race
  ,patients.ethnicity
FROM alasql.patients;
```

</details>

### Quiz: SELECT, FROM, DISTINCT

Which of the following is **not** true about DISTINCT?  Select all that apply!

[[ ]] `DISTINCT` returns rows that are unique, with no duplicated rows in the result set
[[ ]] `DISTINCT` is a handy tool for seeing what possible values, or value combinations, exist in various columns (or sets of columns)
[[X]] `DISTINCT` is computationally inexpensive and doesn't use much in the way of resources
[[X]] `DISTINCT` immediately follows FROM in a query
[[ ]] `DISTINCT` immediately follows SELECT in a query
***************

<div class = "answer">

`DISTINCT` is a powerful tool that allows you to retrieve a unique set of rows with no duplication.  This is great for eliminating duplicated data or finding out what the possible values for a single column are (or the possible combinations of values across two or more columns). The `DISTINCT` keyword appears directly after the `SELECT` keyword in a query.  It's useful, but it can also be computationally expensive, so if you end up using DISTINCT across many columns of data in order to eliminate duplicate rows, consider doing a bit of investigation about why there's so much duplication!

</div>

**************

In the code block below, write a query that will return the unique combinations of `county` and `state` from the `patients` table.  Then we'll ask you a question about your findings!

```sql
SELECT ... 
```
@AlaSQL.eval("#dataTable9a")
<table id="dataTable9a" border="1"></table>


How many rows do you have in your results? 

[[9]]
<script>
  let input = "@input".trim().toLowerCase();
  input == "9" || input == "nine";
</script>
***************

<div class = "answer">

You should have 9 rows displayed!  If you don't, we'll share the query we used in the explanation of the next question.

</div>

**************

Which of the following statements are true about your data?  Select all that apply!

[[X]] There are no patients with a `state` value of Pennsylvania
[[X]] There are no patients from Hampshire county
[[ ]] There are four counties represented from Massachusetts
[[ ]] Bristol County appears twice, once for Massachusetts and once for New Jersey
[[ ]] Connecticut appears with four counties
***************

<div class = "answer">

Wondering how we got these answers?

Run the following query:

```sql
SELECT DISTINCT
	county
	,state
FROM alasql.patients;
```
@AlaSQL.eval("#dataTable9b")
<table id="dataTable9b" border="1"></table>



</div>

**************

<div style = "display:none;">
@AlaSQL.buildTable_patients
</div>

### Adding Comments

**Comments** are explanatory or helpful bits of text that you can add to your code as documentation for yourself or other reviewers of your code.  Comments don't actually affect the execution of the SQL code in any way and are simply there for humans.

In **SQL** there are 2 different techniques that can be used for adding comments, **single-line** and **multi-line** comments.

Single-line comments can be created by typing 2 minus signs in a row (i.e. `--`).

Once added to your code, anything that appears to the right of the `--` comment delimiter will be treated as comment text.

Multi-line comments can be started by adding the `/*` characters to your code, and the multi-line comment can be closed by adding the `*/` characters.

Once created, any text that appears between the `/*` and `*/` "tags" will be treated as comment text.

The code block below provides an example of each of these styles of commenting:

```sql
/* This is a simple demographics query*/
SELECT
  patients.id         --unique patient identifier.
  ,patients.sex       --patient sex {'M', 'F'}
  ,patients.race      --patient race
  ,patients.ethnicity --patient ethnicity {'hispanic', 'nonhispanic'}
  ,patients.state     --full name of patients state of residence.
FROM alasql.patients;


/*
    Aren't Comments Great!
*/
```
@AlaSQL.eval("#dataTable10a")

<table id="dataTable10a" border="1"></table>


<div style = "display:none;">

@AlaSQL.buildTable_patients

</div>

### WHERE

The **WHERE clause**, using the `WHERE` keyword, is the section of your query used to specify any "filtering logic" that should be applied to your query before returning any output.  It's optional but very useful.

The below example uses `WHERE` to filter output on only the records for a specific county.

```sql
SELECT *
FROM alasql.patients
WHERE
	patients.county = "Suffolk County";
```
@AlaSQL.eval("#dataTable11a")

<table id="dataTable11a" border="1"></table>

<br/><br/>
Although the above example lists only one constraint for the dataset, the WHERE clause can contain any number of filtering arguments needed.

Check out the code block below for an example of a where clause that includes multiple constraints, and makes use of both **comparison** operators like `=` and `<=` and **logical** operators including `AND` and `OR`.  Also take a look at the useful comments!  The queries are getting a bit more complex, so it's worth trying to describe this query to yourself in plain English (or another natural language).

```sql
SELECT *
FROM alasql.patients
WHERE 
	( -- looking just in Suffolk or Barnstable counties
		patients.county = "Suffolk County"
		OR patients.county = "Barnstable County"
	)
	AND
	( -- patients who are hispanic or non-white
	  patients.ethnicity = "hispanic"
	  OR patients.race != "white"
	);
```
@AlaSQL.eval("#dataTable11b")

<table id="dataTable11b" border="1"></table>


<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

When you mix `AND` and `OR`, you have to be careful.  It's easy to make a logical order-of-operations mistake.  That's why it's crucial to include parentheses to show the scope of your `AND` and `OR` logical operators.  To see this in action, remove the second set of parentheses, around the `race` and `ethnicity` comparisons, and re-run the query.  What happens?  Why?  

</div>

Ready to try your luck at a complex WHERE statement?

Get every field from `patients` for all male patients who were born on or after January 1, 2001.  Not sure about the field name that holds sex, or whether male is coded "Male", "male", "M", or some other way?  Look at the results of other queries to get this information!


```sql
SELECT
FROM
WHERE

```
@AlaSQL.eval("#dataTable11c")

<table id="dataTable11c" border="1"></table>


<div style = "display:none;">
@AlaSQL.buildTable_patients
</div>


<details>
<summary style = "margin-bottom: 1rem;">*If you have given it a good try and are stuck... click here to show/hide an answer!*</summary>

Try:

```sql
SELECT *
FROM alasql.patients
WHERE 
	patients.birthdate >= "2001-01-01" AND
	patients.sex = "M";
```

</details>


### Dealing with Null Values

Like many programming languages, **SQL** deals with "blank" values in a very specific way.

**SQL** uses the concept of **null** to represent "blank" row values.

If you ever find yourself in a situation where you need to filter on null values you can use the `IS NULL` or `IS NOT NULL` operators as shown below.

Here, we're asking to see rows from the `allergies` table where the `stop` value (the date at which the presumed allergy was considered no longer applicable, resolved, a mistake, or not an allergy) isn't missing.  In other words, the allergy has a date at which it was ruled to not exist.

Because the results here are large on the screen, we've put the results in a collapsible section that you can close when you're finished looking at them!

```sql
SELECT *
FROM alasql.allergies
WHERE
    allergies.stop IS NOT NULL; -- there is some value here, it's not empty
```
@AlaSQL.eval("#dataTable12a")

<details open>

<summary>**Results of Query (click to collapse or expand this section)**</summary>

<table id="dataTable12a" border="1"></table>

</details><br/><br/>

It's also worth noting that null values are treated very differently from actual data.  Note that you cannot use operators like `=` to ask if something is null, because null values are inherently unknowable, so we can't know what a null value is equal to.  You can't do math with a null value and you can't compare to a null value.  To illustrate this point, we can look at an example below.  

Consider the options with regards to the `stop` column of `allergies`.  The `stop` column will meet, for each row, one of the conditions below.  Here we're using an arbitrary date to illustrate the categories.

1. A date less than (earlier than) March 1, 2020,
2. A date equal to March 1, 2020,
3. A date greater than (after) March 1, 2020,
4. No date at all (null)

Run the code cell below.  It's important to realize that the code below returns rows that belong to **only** the first case.  Rows that meet the second or third condition are in direct violation of the WHERE clause and are not included.  Rows that fall into the fourth condition (null) cannot be evaluated with a comparison operator, and are left out as well.

```sql
SELECT *
FROM alasql.allergies
WHERE
    allergies.stop < '2020-03-01';
```
@AlaSQL.eval("#dataTable12b")


<details open>

<summary>**Results of Query (click to collapse or expand this section)**</summary>

<table id="dataTable12b" border="1"></table>

</details>

<br/>
<br/>

Why is this interesting?  Because sometimes we want to return a mix of null and non-null values.  For example, maybe you're aware that allergies with a `stop` date prior to March 1, 2020 have data quality issues and need to be checked -- these could be real allergies that should not have a `stop` date.  And to that group of possible allergies you want to add the cases where there is no `stop` date at all, where we can presume that the allergy wasn't ruled out.  In order to make sure that records where the `stop` date is null are also included in our output we will need to add another line to  the select statement to explicitly include them, as shown below.  

```sql
SELECT *
FROM alasql.allergies
WHERE
    (
        allergies.stop < '2020-03-01'
        OR allergies.stop IS NULL
    );
```
@AlaSQL.eval("#dataTable12c")


<details open>

<summary>**Results of Query (click to collapse or expand this section)**</summary>

<table id="dataTable12c" border="1"></table>

</details><br/><br/>

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

The fact that nulls aren't included in comparisons is a very subtle distinction that can drastically alter the output of your SQL statements.  This can be very important when writing inclusion and exclusion logic and thinking about what cases belong in your data set.  Always keep in mind that you might have missing values, and consider what that might mean for your selection of rows.  

</div>

Sometimes you want to evaluate missing data patterns.  For example, maybe there's a discernible pattern in patients who are missing sex or race data.  Write and run a query in the code box below that will give you all the fields for rows in `patients` where either the sex or race data is missing.   (Hint: there might not be any rows that have missing data in those two fields).

```sql
SELECT ...
```
@AlaSQL.eval("#dataTable12d")

<table id="dataTable12d" border="1"></table>


<div style = "display:none;">
@AlaSQL.buildTable_allergies
@AlaSQL.buildTable_patients
</div>

<details>
<summary style = "margin-bottom: 1rem;">*If you have given it a good try and are stuck... click here to show/hide an answer!*</summary>

Try:

```sql
SELECT * 
FROM alasql.patients
WHERE 
	patients.sex IS NULL OR
	patients.race IS NULL;
```

</details>

### Quiz: Comments, WHERE, Null Values

What has to change to make this code work?  Select all that apply. 

```sql
SELECT
FROM alasql.patients
WHERE
  patients.race = NULL OR
  patients.sex = NULL.
```

[[X]] ` = NULL ` should be changed to ` IS NULL `
[[ ]] `OR` should be in lowercase
[[X]] A column selection should be made after the `SELECT` keyword
[[X]] The period at the end of the query should be replaced with a semicolon
[[ ]] The two conditions in the `WHERE` clause should be enclosed by parentheses
***************

<div class = "answer">

First things first, what are you `SELECT`ing?  Also, you do need to replace the ` = NULL` to ` IS NULL `, and end the query with a semicolon, not a period.

`OR` isn't case sensitive, but we suggest leaving it in CAPITAL letters so it stands out as a keyword.  And since there's no nesting and no mixing of `AND` and `OR`, the use of parentheses around the `WHERE` clauses is totally optional.  You only really **have** to add parentheses when you're mixing operations (just as you do in math, to make sure things get added before they're multiplied).

</div>

***************

What has to change to make this code work?  Select all that apply. 

```sql
SELECT *             # we want all the fields/columns
FROM alasql.patients # note that this uses dot notation
WITH
  sex = M;
```

[[ ]] `alasql.patients` should be changed to just `patients`
[[ ]] The semicolon should be omitted
[[X]] The `M` in the last line should have quotes around it
[[X]] The hash marks (`#`) on the first two lines should be replaced with `--`
[[X]] `WITH` should be replaced by `WHERE`
***************

<div class = "answer">

While you **could** omit `alasql`, it certainly isn't hurting things, and it's often useful to add the additional context that dot notation provides.  Similarly, while in this module page, you can get away without typing a semicolon, that doesn't mean it's a good idea.  Here's what needs to change to make this code run:

* Comments need to be corrected -- the right way to do end-of-line comments like this is using a double dash (`--`), not a hash mark.
* `WITH` should be replaced by `WHERE`.  
* When you compare something to a string, you need to put that string in quotes.  So try `"M"` instead of `M`.

</div>

**************



### ORDER BY Statement

Another useful piece of SQL syntax for exploring datasets is the `ORDER BY` statement, which (as its name suggests) is used to order your result set by a given set of one or more columns.

When listing columns in the `ORDER BY` statement you can specify that they be sorted in either ascending (`ASC`) or descending (`DESC`) order. If you list more than one column in `ORDER BY`, items will be sorted first by the first column you provide, and then, within "ties", by the second, then third, etc., column.  For instance, the code below first sorts by `county`, and then within each possible value of `county` sorts by `ethnicity`.  Run it to see the results!

```sql
SELECT DISTINCT
  patients.county
  ,patients.ethnicity
FROM alasql.patients
ORDER BY
  patients.county ASC
  ,patients.ethnicity DESC;
```
@AlaSQL.eval("#dataTable14a")

<table id="dataTable14a" border="1"></table>


Some things to think about:

* What does the query above help you understand about your patient population?
* How could you switch the sorting so that all the counties with a Latino / Hispanic patient population were at the top, followed by all the counties without a Latino / Hispanic patient population?  Try it!

<details>
<summary style = "margin-bottom: 1rem;">*Click here to show/hide a code suggestion for the second bullet point above.*</summary>

Try:

```sql
SELECT DISTINCT
  patients.county
  ,patients.ethnicity
FROM alasql.patients
ORDER BY
  patients.ethnicity ASC
  ,patients.county ASC;
```

</details>

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

By default, all items in the `ORDER BY` clause will be sorted in `ASC` (ascending) order if no explicit ordering direction is provided.

</div>

<div style = "display:none;">

@AlaSQL.buildTable_patients

</div>

### LIMIT

The `LIMIT` clause can be used to limit the result set of your select statement to (at most) a pre-defined number of rows.

To do this all you need to do is add the word `LIMIT` as the last line of your query, followed by the number of rows you would like your result set truncated at. This is a great bit of syntax to use for exporting a quick peek at tables you might be unfamiliar with.  Showing just the first three or five or ten rows of a table can give you a quick intuitive grasp of the contents of the whole table and will come back very quickly.  Without a `LIMIT`, large tables can take a long time to return all their results.

The example below pulls all columns from the `patients` table, and limits the result set to only 3 rows.

```sql
SELECT *
FROM alasql.patients
LIMIT 3;
```
@AlaSQL.eval("#dataTable15a")

<table id="dataTable15a" border="1"></table>


<div style = "display:none;">

@AlaSQL.buildTable_patients

</div>


### Aliasing with AS

In SQL, it is possible to assign a custom name (usually a kind of shortened name) to a table or column in your query using a technique called **aliasing**.

* Aliasing **tables** can be helpful for long or complex queries involving multiple tables because it allows you to avoid typing out the full name of a table each time you refer to it.  For example, in a long query involving the `patients` table, the `encounters` table, and the `diagnosis` table, you might prefer to use the shorthand terms `pt`, `enc`, and `dx` or even `p`, `e`, and `d`.

* Aliasing **columns** can be helpful as well by assigning clearer, more comprehensible names for a given column than the name that might be assigned to it in the database.  For example, you might want to see the results from the `stop` column in the `allergies` table returned to you not as `stop`, but rather as `ruled_out_date`.

Aliases are assigned by placing the `AS` key word directly after the item (table/column) you would like to alias, followed by the name you would like to assign as its **alias**.

In the example below, we can see aliasing being used to rename the `patient` table to `p`, and renaming the `id` and `state` columns to `unique_patient_id` (because there are other id fields you're working with elsewhere) and `state_name` (because you want to point out that this isn't the state abbreviation).

```sql
SELECT
  p.id AS unique_patient_id
  ,p.sex
  ,p.race
  ,p.ethnicity
  ,p.state AS state_name
FROM alasql.patients AS p;
```
@AlaSQL.eval("#dataTable16a")

<table id="dataTable16a" border="1"></table>


In the SQL code block below, try writing a query that accomplishes the following.  Because there are several constraints, try starting with a simple query (something like a `SELECT * ...`) and gradually changing it so that you knock out one bullet point at a time.

* Retrieves the patient identifier, sex, ethnicity, state, and zip
* Aliases the `patients` table as `pt`
* Aliases the `sex` field as `sex_assigned_at_birth`
* Aliases `zip` as `postal_code`
* Orders the result by zip/postal code

```sql


```
@AlaSQL.eval("#dataTable16b")

<table id="dataTable16b" border="1"></table>


<div style = "display:none;">
@AlaSQL.buildTable_patients
</div>

<details>
<summary style = "margin-bottom: 1rem;">*If you have given it a good try and are stuck... click here to show/hide an answer!*</summary>

Try:

```sql
SELECT 
	pt.id
	,pt.sex as sex_assigned_at_birth
	,pt.ethnicity
	,pt.state
	,pt.zip as postal_code
FROM alasql.patients as pt
ORDER BY postal_code;
```

</details>

### Quiz: ORDER BY, LIMIT, AS

What does `ORDER BY` accomplish?

[[ ]] `ORDER BY` changes the order of columns, so you can rearrange columns to be more helpful to your use case
[[X]] `ORDER BY` changes the order of rows, putting them in order according to the value in one or more columns
***************

<div class = "answer">

If you want to change the order of columns, the best thing to do is change the order you type things in after `SELECT`.  That's not the job of `ORDER BY`!  No, what `ORDER BY` does is permit you to organize your **rows**.  You can put rows in order according to one or more column values.

</div>

**************

Which of the following are true about the `AS` keyword?

[[X]] `AS` indicates an alias -- a temporary command to "please call this by a different name".
[[X]] `AS` can be useful for making queries easier to type
[[X]] `AS` can be helpful for giving columns more accurate names
***************

<div class = "answer">

All of these are true!  Aliasing uses the `AS` keyword.  You can alias table names, which often means less typing (for instance, you could use `pt` instead of `patient`) in long queries.  Aliasing column names can be helpful when you're making the alias something more understandable than the column name in the table.

</div>

**************

What does `LIMIT` accomplish?


[[X]] `LIMIT` controls the maximum number of rows output.  You will not get more rows than what your `LIMIT` value is.  
[[ ]] `LIMIT` puts a limit on number of identical rows that can be output as the result of a query.
***************

<div class = "answer">

`LIMIT` controls the maximum number of rows output.  You will not get more rows than what your `LIMIT` value is.  Of course, if the total number of rows a query outputs is **less** than `LIMIT`, you'll get that value.  `LIMIT` doesn't have anything to do with ensuring that rows are unique, so it won't do anything about identical rows.  You need to think about `DISTINCT` for that use case!

</div>

**************

## Recap

In this module, you learned about the language SQL, which is an acronym for "Structured Query Language".  It's a powerful tool for requesting specific subsets of data from a relational database, and has been around since the 1970's because of its efficiency and utility.  

We also introduced you to important functions, in terms of **keywords**.  You got a chance to read about and practice these keywords:

* `SELECT`: used to indicate which fields (columns) you want to retrieve
* `FROM`: used to indicate which table you want to retrieve data from
* `DISTINCT`: used to ask for only a single example of each possible unique value
* `WHERE`: used to give a condition which filters the data retrieved
* `IS NULL`: used to compare a value to *NULL* (an empty/missing value)
* `IS NOT NULL`: used to compare a value to not *NULL* (a value that is not missing and not empty)
* `ORDER BY`: used to display results organized by the values in one or more columns
* `LIMIT`: used to truncate (cut off) the number of result rows retrieved at a given number
* `AS`: used to alias (rename) columns or tables

We also learned about comparison operators, comments, and style -- how to write code in a specific way that promotes reusability and readability.

You also got to practice hands on, which probably meant you got to see some error messages, too, which is helpful experience.

## Additional Resources

* Khan Academy's [Introduction to SQL](https://www.khanacademy.org/computing/computer-programming/sql) is high quality and easy to learn from.

* Tutorials Point has some helpful documentation you may want to check out [about the basic types of operators available for use in a SQL query](https://www.tutorialspoint.com/sql/sql-operators.htm).

* Enjoy learning with real-life, consequential examples?  You might enjoy [Select Star SQL](https://selectstarsql.com/), a free interactive book that allows you to run queries against real-world death row data.

* Prefer a game?  The fun and engaging [SQL Murder Mystery](https://mystery.knightlab.com/) or [Lost at SQL](https://lost-at-sql.therobinlord.com/) might help you hone your skills.

## Feedback
@feedback

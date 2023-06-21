<!--

author:   Joy Payton
email:    paytonk@chop.edu
version:  1.0.0
current_version_description: Initial version
module_type: standard
docs_version: 1.1.0
language: en
narrator: US English Female
mode: Textbook

title: Regular Expressions in SQL

comment:  Learn to use regular expressions in SQL

long_description: Ready to use regular expressions (regex) in SQL?  This module will help you put what you know about regular expressions into action in SQL.

estimated_time_in_minutes: 30

@pre_reqs
Some experience writing basic SQL code (SELECT, FROM, WHERE) is expected in this module.  If you need to develop basic SQL fluency we recommend our module [SQL Basics](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/sql_basics/sql_basics.md).  Additionally, some experience using regular expressions is necessary, as this module does not teach the syntax of regular expressions.  If you need an introduction to regular expressions, we suggest our [Introduction to Regular Expressions](https://example.com).
@end

@learning_objectives  
After completion of this module, learners will be able to:

- identify key elements
- create a product
- do a task
- articulate the rationale for something
@end

@version_history 

Previous versions: 

- [x.x.x](link): that version's current version description
- [x.x.x](link): that version's current version description
- [x.x.x](link): that version's current version description
@end



import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md

import: https://raw.githubusercontent.com/arcus/education_modules/regex_sql_rmh/_module_templates/macros_sql.md 

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_sql_table_allergies.md 


-->

# Module Title

@overview

## Lesson Preparation

@lesson_prep_sql

## A Brief Refresher

These concepts should seem familiar to you.  If this brief refresher seems to be new information, consider reviewing [SQL Basics](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/sql_basics/sql_basics.md) or 

**SQL** (**S**tructured **Q**uery **L**anguage) is a language that for more than four decades has been used to interact with **relational databases**, which store rectangular data in rows and columns (also known as fields).  A common pattern for SQL queries is `SELECT ... FROM ... WHERE`.

A **regular expression** (also known as **regex**) is a specific way to express a rule for a pattern, such as the pattern you expect for an email address, or the pattern for a credit card number.  An example regular expression is `\d{4}`, which describes a four digit number, such as year. 

These two technologies can intersect, and this module will go into how to use regular expressions in your SQL queries.

## The Intersection of SQL and Regex

Why would you use regular expressions in SQL?  Well, perhaps you want to `SELECT`  email addresses that end in ".edu", or want to exclude from your search lab values that have non-numeric characters such as `>` or `+`.  Being able to use patterns in your SQL code will allow you to be more precise in the query results you obtain.

In order to work with regular expressions in SQL, you need to know how to work with:

* Regular expression operators in SQL (`REGEXP`, `NOT REGEXP`)
* Special regular expression syntax in SQL
* Posix operators

We'll cover each of these topics in the next few sections.

### Regular Expressions Operators

We'll start two regular expression operators in SQL which are inverses of each other.

`REGEXP` accepts a pattern and a text to compare to the pattern and will return `True` if the text matches the pattern and `False` if the text does not match the pattern.

`NOT REGEXP` is the opposite: it accepts a pattern and a text to compare to the pattern, and it returns `True` if there is no match, and `False` if there is a match.

How might you use these operators?


```sql
SELECT
  birthdate
  ,sex
FROM patients
LIMIT 10;
```
@AlaSQL.eval("#dataTable2a")

<table id="dataTable2a" border="1"></table><br>

<div style = "display:none;">

@AlaSQL.buildTable_patients

</div>




## Feedback

@feedback

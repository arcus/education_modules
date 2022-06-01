<!--

author:   Elizabeth Drellich
email:    drelliche@chop.edu
version:  1.0.0
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Transform Data with pandas
comment:  This is an introduction to transforming data using a Python library named pandas.
long_description: This module is for learners who have some familiarity with Python, and want to learn how the pandas library can handle large tabular data sets. No previous experience with pandas is required, and only an introductory level understanding of Python is assumed.
estimated_time: 1 hour

@learning_objectives  

After completion of this module, learners will be able to:

- Import `pandas` and use functions from the `pandas` package.
- Load data into a `pandas` DataFrame.
- Use the `.loc` method to explore the contents of a DataFrame
- Filter a DataFrame using conditional statements.
- Transform data in a DataFrame.

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

script: https://sagecell.sagemath.org/static/embedded_sagecell.js

@sage
<script input="hidden">
// Make *any* div with class 'python' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python',
                       evalButtonText: 'Run python',
                       languages: ["python"],
                       hide: ['fullScreen', 'permalink'],
                       });
// Make *any* div with class 'python_run' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python_run',
                      evalButtonText: 'Run python',
                      languages: ["python"],
                      hide: ['fullScreen', 'permalink'],
                      autoeval: 'true'
                      });
// Make *any* div with class 'python_link' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python_link',
                      evalButtonText: 'Run python',
                      languages: ["python"],
                      hide: ['fullScreen', 'permalink'],
                      autoeval: 'false',
                      linked: 'true'
                      });
// Make *any* div with class 'python_data_init' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python_data_init',
                      evalButtonText: 'Run python',
                      languages: ["python"],
                      editor: 'codemirror-readonly',
                      hide: ['fullScreen', 'permalink','output','evalButton'],
                      autoeval: 'true',
                      linked: 'true',
                      linkKey: "data"
                      });       
// Make *any* div with class 'python_data' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python_data',
                      evalButtonText: 'Run python',
                      languages: ["python"],
                      hide: ['fullScreen', 'permalink'],
                      autoeval: 'false',
                      linked: 'true',
                      linkKey: "data"
                      });                
</script>
@end
persistent: true
-->

# Transform Data with pandas

<div class = "overview">
## Overview

@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

Before starting this module it is useful for you to:

* have some familiarity with tabular data: data stored in an array of rows and columns.

* have an introductory level exposure to coding in [Python](intro/to/python/module)

**Learning Objectives**

@learning_objectives

</div>

## Lesson Preparation
@sage

You will have opportunities for hands-on coding as you work your way through this module using interactive python cells.
The interactive python cells are powered by [SageMathCell](https://sagecell.sagemath.org/). For the most part, these will appear with some code already in them, and you can run that code by clicking the **Run python** button. You can also edit the code in these cells and run your own code.


**Give it a try:**
<div class="python_link">
<lia-keep>
<script type="text/x-sage">
m = 3
print(m+2)
</script>
</lia-keep>
</div>

The cells in this module are linked, meaning if you run code in two cells on the same page, the second cell will remember anything you defined in the first.

<div class="python_link">
<lia-keep>
<script type="text/x-sage">
n = m**3 + m  # a double asterisk indicates 3 is the exponent of m
print(n)
</script>
</lia-keep>
</div>

You can change anything you want in either cell. Once you run that code using the **Run python** button, both cells will remember it.

Code will not persist from one page to the next, and you can always refresh the page to return the code (and the stored memory of the cell) to its initial state.

<div class = "important">
These cells will compute everything you ask them to, but will only output what you explicitly request using the `print()` command.
</div>


## The `pandas` Package

The `pandas` [package](https://pandas.pydata.org/) lets you store, examine, and manipulate tabular data using python. Since many machine learning tools use python, it can be particularly useful to process tabular data in that same environment.

<div class = "learnmore">
Most people associate "pandas" with the large mammals [Ailuropoda melanoleuca](https://en.wikipedia.org/wiki/Giant_panda). The `pandas` package is actually a shortening of "panel data."
</div>

### Importing `pandas`

**The pandas package**

Because `pandas` isn't part of python, in order to use its tools you will need to **import** the pandas package at the beginning of each session you intend to use it.

The code `import pandas` tells python that you want all of the commands and tools that `pandas` has to be available to you. For example `read_csv` is a  function in `pandas` and regular python will not recognize it! You will have to tell python that a command you are using is a `pandas` command by entering `pandas.read_csv`.

**Rename `pandas` to `pd`**

To make it easier to type out these commands, you can give the `pandas` package a different name when you import it using `as new_name`. While you could in theory pick any name you want, the standard abbreviation is `pd`.

@sage
<div class="python_link">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
</script>
</lia-keep>
</div>

If you click the **Run python** button, the `pandas` package will be imported. There isn't any output from this line of code, but we will be able to see on future pages that is is giving us access to all of the `pandas` tools.

This code, without a "Run python" button, will be at the top of each page in this module. We will run it automatically when you open each page. If you want to run this code on your own computer, make sure to include the line `import pandas as pd` as the first line.

### DataFrames and Series
@sage

The `pandas` package lets you handle two types of data structures that python alone can't: **DataFrames** and **Series**. Before we can start exploring them, let's make sure we have `pandas` imported. You don't have to click anything, this code ran automatically when you opened this page:

<div class="python_data_init">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
</script>
</lia-keep>
</div>


**DataFrames**

**DataFrame** is the name `pandas` gives to its primary data structure. You can think of a DataFrame like a spreadsheet: it has rows and columns, and you can look up the data in it by referencing those rows and columns.

Let's take a look at a basic DataFrame. This one is being built from scratch, but we aren't going to spend any time learning how to do that in this module because you will usually be using `pandas` to analyze data that you import from somewhere else.

**Run this code** to print out the DataFrame `df`.
<div class="python_data">
<lia-keep>
<script type="text/x-sage">
d = {'col1': [1, 5, 7], 'col2': [3, .4, -2], 'col3':["yes", "no","blue"]};
df = pd.DataFrame(data=d);
print(df)
</script>
</lia-keep>
</div>

**Series**

You might have noticed that in the above example, everything in the first column was an integer, everything in the second column had a decimal point, and the third column consisted of words. Each column in a DataFrame is called a **series**. A series is a one-dimensional array in which all of the data has the same **type**.

**Run this code** to print out `col1` from the DataFrame `df`.
<div class="python_data">
<lia-keep>
<script type="text/x-sage">
print(df['col1'])
</script>
</lia-keep>
</div>

Did you notice the `Name` and `dtype` at the bottom? Those tell you the name of the series and its data type. Try changing `col1` to `col2` or `col3` to see what type of data those series contain.


### Quiz: `pandas` package

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">
d = {'col1': [1, 5, 7], 'col2': [3, .4, -2], 'col3':["yes", "no","blue"]};
df = pd.DataFrame(data=d);
print(df)
</script>
</lia-keep>
</div>
<br>
Your friend's code (above) isn't running, which is extremely frustrating because they copied and pasted it from the previous page of this module. What line must they add to make it work?

[[import pandas as pd]]
[[?]] Hint: Run the code. What does the error message say is wrong?
[[?]] Hint: What do we need to include at the top in order to make `pandas` commands available to us?
***
<div class = "answer">
`NameError: name 'pd' is not defined` is a helpful error message because it tells you exactly what you friend forgot: they never defined `pd`!

When you add the line `import pandas as pd` to the top of their code, it runs as it did before.

<div class="python_run">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
d = {'col1': [1, 5, 7], 'col2': [3, .4, -2], 'col3':["yes", "no","blue"]};
df = pd.DataFrame(data=d);
print(df)
</script>
</lia-keep>
</div>

</div>
***

## Tabular Data in `pandas` DataFrames

The tiny DataFrame we saw in the last section was exceptional in several ways. With real data you are likely to have some challenges that just can't be replicated with something that small:

* Real data will almost always be too big to type into a DataFrame.

* Real data frequently has too many rows and columns to look at the whole dataset at once.

* Real data is often missing entries.

<div class = "important">
For this module we will be looking at some fake Covid-19 testing data. Although this data is designed to mimic realistic data with plausible patterns and values, **there is no Protected Health Information in this data**. If you are a fan of the fictional series "Game of Thrones," however, you might recognize some familiar characters.

This data is saved as a [csv file hosted on GitHub](https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv).
</div>

### Loading data
@sage
<div class="python_data_init">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
</script>
</lia-keep>
</div>

The `pandas` package can read most tabular data files and convert them into DataFrames. As long as your data is in a place that the program can locate (either on your computer if you are running code on your computer, or in the cloud) all `pandas` needs to know is what type of file it is reading, and where to find that file.

The fake Covid-19 testing data we will use for the rest of this lesson is saved as a [csv file hosted on GitHub](https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv).

The `read_csv` function from the `pandas` library takes the location of the file as its argument. The path to the file, in this case a url, must be in quotes. Let's create a new DataFrame called `covid_testing` that will contain all of our fake Covid-19 testing data.

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
covid_testing = pd.read_csv('https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv')
</script>
</lia-keep>
</div>

That code didn't have any output because we didn't ask it to print anything, but it did create the `covid_testing` DataFrame. We can take a look at with `print(covid_testing)`:

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
print(covid_testing)
</script>
</lia-keep>
</div>

Unless you have an extremely wide browser window, the output above is broken into as many columns as it can fit at a time. Some interfaces will output the DataFrame and let you scroll right to see more columns, but this interface just prints as many columns as it can fit and then starts again with the next columns. Good thing it didn't print all 15524 rows!

When you print a DataFrame or Series you will see the first five rows and the last five rows of a DataFrame. If, like this one, it has more than 10 rows, the hidden rows will be indicated by ellipses. You can also ask for the first or last 5 rows of data using the methods `.head()` and `.tail()`. Try putting a number in the parentheses to get different numbers of rows.

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
print(covid_testing.head())
</script>
</lia-keep>
</div>
<br>

**Loading your own data**

To create a DataFrame of your data, make sure you use the right command for your file type, and make sure the location of the file is in quotes.
| File type | Read command |
| - | - |
| .csv | pd.read_csv('location')|
| .xlsx | pd.read_excel('location')|
| .ods | pd.read_excel('location')|
| .json| pd.read_json('location')|
| .html| pd.read_html('location')|
| .sql | pd.read_sql('location')|



### Column names and row indices
@sage
From now on we will add the definition of our DataFrame `covid_testing` to the set-up of each page. There is nothing for you to click here, this code ran automatically when you loaded the page:

<div class="python_data_init">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
covid_testing = pd.read_csv('https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv')
</script>
</lia-keep>
</div>

When a DataFrame is displayed it has a row of column names along the top, and a column of indices along the left side. In some environments, like Jupyter notebooks, these names and indices may be bolded.

The methods `.columns` and `.index` will show you all of the column and row names, respectively. **Give it a try:**

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
print(covid_testing.columns)
</script>
</lia-keep>
</div>

The column names were imported with the `.csv` file. Since the original file didn't have labels for the rows, `pandas` automatically labeled them numerically 0 through 15523. If you imported tabular data that didn't have column headers, the column names would be numeric, the way the row indices are in our `covid_testing` DataFrame.

<div class = "help">
**What does that RangeIndex mean?**

The `covid_testing.index` is `RangeIndex(start=0, stop=15524, step=1)`, but on the previous page we saw that the last row of this DataFrame is labeled 15523. Why is that?

Python ranges can be confusing even for people who use them all the time. Some things to keep in mind are:

- Python starts counting at 0.
- Python ranges include their lower bounds.
- Python ranges **do not include their upper bounds**.

For example `range(0,4)` contains 4 elements. Those elements are 0,1,2, and 3.
</div>

### Locating data with `.loc`

@sage

<div class="python_data_init">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
covid_testing = pd.read_csv('https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv')
</script>
</lia-keep>
</div>
<br>

The `.loc` method lets you select a subset of your DataFrame to display.

**Selecting a single entry**

The grammar of the `.loc` method is `dataframe.loc[row(s), column(s)]`. To see the age of the of the very first person to be tested, i.e. extract the data from row `0` (python starts counting with 0) and column `"age"` enter `covid_testing.loc[0,"age"]`.

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
print(covid_testing.loc[0,"age"])
</script>
</lia-keep>
</div>

You need the `"` surrounding `age` because that column header is a string. No quotes are needed around the row index `0` because it is recognized as a known value.

**Selecting multiple rows or columns**

If you want to see the ages of the first 3 patients tested, change the `0` to the list `[0,1,2]`. This indicates that you want to see the data in rows indexed 0,1, and 2. Similarly you can change the single column to be a list of columns.

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
print(covid_testing.loc[[0,1,2],[ "age", "gender"]])
</script>
</lia-keep>
</div>

**Viewing full rows and columns**

If you want to show all of the data in a row or column, instead of a list you can use a colon `:` to indicate that you want to include everything.

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
print(covid_testing.loc[:,["mrn","first_name","last_name"]])
</script>
</lia-keep>
</div>
<br>

A colon before the comma will show you all rows of the columns you selected and a colon after the comma will return all columns of the given rows.

**Your turn:** What do you think will happen if you put colons both before and after the comma? Change the code below to check if you were correct.

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
print(covid_testing.loc[[2,3,4],:])
</script>
</lia-keep>
</div>
<br>

<div class = "options">
If you look at other people's code, you may see columns refered to with `data_frame["column_name"]` instead of `data_frame.loc[:,"column_name"]`. While this will frequently give the same output, i.e. show you the entire column, it can [raise errors if you use it to try to update data](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html). For that reason we are focusing on the `.loc` method.
</div>

### Quiz: DataFrames

@sage

1. Complete the following code by replacing the two `__?__`s with your own code to find out the first and last name of the patient in row 11942.

<div class="python">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
covid_testing = pd.__?__('https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv')

print(covid_testing.__?__[11942, ["first_name","last_name"]])
</script>
</lia-keep>
</div>
<br>

Enter their name below to check your answer:

[[grazdan greyjoy]]
<script>
  let input = "@input".trim().toLowerCase();
  input == "grazdan greyjoy";
</script>
***
<div class = "answer">

On line 2, the command `read_csv` will convert the csv file's data into a DataFrame.

On line 4, the `.loc` method will request the data from row 11942 and columns `"first_name"` and `"last_name"`.

The completed code should look like this:

```
import pandas as pd
covid_testing = pd.read_csv('https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv')

print(covid_testing.loc[11942, ["first_name","last_name"]])

```
</div>
***

## Conditional statements

@sage

<div class="python_data_init">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
covid_testing = pd.read_csv('https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv')
</script>
</lia-keep>
</div>
<br>

Let's say we only care about the positive Covid tests. We could make a new DataFrame consisting only of those tests that came back positive using a **conditional** argument. A condition is a statement that evaluates to either `True` or `False`.

If, for example, we only want to look at instances where the covid test came back positive, we need to use the condition `covid_testing.loc[:,"result"] == "positive"`. This statement checks every row in the `covid_testing` and will be `True` for a given row if the entry in column `result` is equal to the string `positive` and `False` otherwise.

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
print(covid_testing.loc[:,"result"] == "positive")
</script>
</lia-keep>
</div>
<br>

In the example above we used the double equals sign `==` to check whether two objects were the same. This is different from the single equals sign we use at the top of the page to define `covid_testing`.

<div class = "important">
A double equals sign `==` tests for equality, while a single equals sign `=` is for assigning values.

- `a = 7` sets 7 as the value of `a`. It is a declarative statement that from now on `a` is equal to 7. No output will be shown, but from now on if you enter `a`, the output will be `7`.
- `b == 8` is a checking for equality. It is a question "is `b` equal to 8?" You will get an answer back, either `True` or `False`.
</div>

In addition to using `==` to check if two values are the same, we can use other relational conditions to compare values in a DataFrame.

| symbol | meaning |
| :---: | --- |
| `<` | is less than|
| `<=` | is less than or equal to |
| `>` | is greater than|
| `>=` | is greater than or equal to|

### Filtering by a condition

@sage

<div class="python_data_init">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
covid_testing = pd.read_csv('https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv')
</script>
</lia-keep>
</div>
<br>

When we used a column name or list of names as our argument in the row spot of the `.loc` method, we got back all rows in that list. When we put a condition  like `covid_testing.loc[:,"result"] == "positive"` in the row spot, it will return all rows for which that condition is `True`.

If this is a subset of the data that you are likely to want to use again, it is a good practice to create a new DataFrame consisting only of the rows and columns that you want.

**Create a new DataFrame** titled `positive_tests`. How many rows have positive test results?

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
positive_tests = covid_testing.loc[covid_testing.loc[:,"result"] == "positive",:].copy()
print(positive_tests)
</script>
</lia-keep>
</div>
<br>

That is a whole lot of output when we see every column! You can ask to see fewer columns so that the output doesn't need to wrap. Try replacing `print(positive_tests)` with  `print(positive_tests.loc[:,["first_name","last_name"]])` and see if that output is easier to understand.


<div class = "important">
**`.copy()`**

The method `.copy()` at the very end of line one creates a new DataFrame separate from the original. Omitting the `.copy()` method won't change the output in the next code block, but can have consequences if you later want to make changes to your DataFrame.

- `new_name = dataframe.loc[rows,columns].copy()` creates a new DataFrame called `new_name` that you can make changes to without impacting the original `dataframe` and vice versa.

- `new_name = dataframe.loc[rows,columns]` does not create a new DataFrame. Instead every time you type `new_name` after this, it will understand that you mean `dataframe.loc[rows,columns]`.
</div>



### Combining conditions
@sage
<div class="python_data_init">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
covid_testing = pd.read_csv('https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv')
</script>
</lia-keep>
</div>

We can also combine conditions using `&` for **and**, and the vertical "pipe" `|` **or**. The `|` can be found above the forward slash \ on your keyboard. The code below shows us only the rows for patients age 18 or older who tested positive.

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
adult_positive = covid_testing.loc[(covid_testing.loc[:,"result"] == "positive") & (covid_testing.loc[:,"age"] >= 18), :]
print(adult_positive.loc[:,["first_name","last_name", "age"]])
</script>
</lia-keep>
</div>
<br>

Our code is starting to look quite messy. Giving each condition a name is a good way to keep your code from becoming an unreadable tangle of conditional statements.

**Name your conditions**

When working with more complicated conditions it is extremely helpful to define your condition by giving it a name, and then refer to that name, rather than the chain of conditions, inside the `.loc` method. By carefully naming the compound condition, you can also make your code more human-readable. Take a moment to see what this code below is doing:

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
is_positive_infant = (covid_testing.loc[:,"age"]<1) & (covid_testing.loc[:,"result"] == "positive")

infant_positive = covid_testing.loc[is_positive_infant,:].copy()
print(infant_positive.loc[:,["first_name","last_name","age"]])
</script>
</lia-keep>
</div>
<br>

**Use parentheses**

When combining conditions, you should use parentheses around each condition. This isn't just for the benefit of humans reading your code. If you are combining three or more conditions, the placement of parentheses can change the meaning of a condition.

The condition:
`((positive_test) & (older_than_10)) | (younger_than_5)`
is true for all results where a patient was older than 10 and tested positive, as well as all children under five, whether or not they tested positive. By moving the parentheses we can change the condition to test for patients older than 10 or younger than 5, but only return those with positive test results.


### Missing Data
@sage
<div class="python_data_init">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
covid_testing = pd.read_csv('https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv')
</script>
</lia-keep>
</div>

So far we have been treating the `covid_testing` DataFrame as if it has a value in every row of every column, but like most real data sets, some data is missing!

Wherever the original csv file didn't have an entry, you will see `NaN` or `nan`, meaning "Not a Number." For which columns is the patient in row 2 missing data?

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
print(covid_testing.loc[2, :])
</script>
</lia-keep>
</div>
<br>

`NaN`s are special in a couple of ways.

1. They are not strings, you can't type them in directly when setting the value of a cell.
2. Two `NaN`s are **not equal** to each other.

For example we know that patient 2 has no data, i.e. `NaN` in both the column `payor_group` and the column `patient_class`. The double equals sign `==` will tell us if those two entries are the same:

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
are_NaNs_equal = (covid_testing.loc[2,"payor_group"] == covid_testing.loc[2, "patient_class"])

print(are_NaNs_equal)
</script>
</lia-keep>
</div>
<br>

Notice that the above cell uses both of the techniques we learned for combining conditions: there are parentheses surrounding the condition `a == b` and the condition has a short, readable name.

Since using `==` to check if a cell is empty won't work, we have the methods `.isna()` and `.isnull()`. These do exactly the same thing: they return `True` if the cell is empty, and `False` if the cell contains information. You can run these methods on a DataFrame or a series (a column of a DataFrame) but not on a single cell:

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
print(covid_testing.loc[:,"payor_group"].isna())
</script>
</lia-keep>
</div>
<br>

The opposite of `.isna()` is the method `.notna()`.

For example you might want to create a new DataFrame of only patients whose `payor_group` is known:

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
known_payor = covid_testing.loc[:,"payor_group"].notna()

known_payor_tests = covid_testing.loc[known_payor, :].copy()

print(known_payor_tests.loc[:, ["first_name", "last_name"]])
</script>
</lia-keep>
</div>
<br>

### Quiz: Conditional statements

@sage
<div class="python_data_init">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
covid_testing = pd.read_csv('https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv')
</script>
</lia-keep>
</div>
<br>

You come across the following code in which several conditions are defined but not given descriptive names:

<div class="python_data_init">
<lia-keep>
<script type="text/x-sage">

condition_1 = covid_testing.loc[:,"first_name"].isna()

condition_2 = covid_testing.loc[:,"last_name"].isna()

condition_3 = covid_testing.loc[:,"age"]<=18

my_condition = (condition_1 | condition_2) & condition_3
</script>
</lia-keep>
</div>
<br>

<div class="python_data">
<lia-keep>
<script type="text/x-sage">

</script>
</lia-keep>
</div>
<br>

What does `my_condition` test for? You can use the interactive cell above to test the conditions however you want.

[( )] Patients under the age of 18 who are missing data in both the `first_name` and `last_name` columns.
[( )] Patients under the age of 18 who are missing data in either the `first_name` or `last_name` columns.
[( )] Patients ages 18 or younger who are missing data in both the `first_name` and `last_name` columns.
[(X)] Patients ages 18 or younger who are missing data in either the `first_name` or `last_name` columns.
***
<div class = "answer">
* `condition_1` will be TRUE if the patient is missing data in the `first_name` column.

* `condition_2` will be TRUE if the patient is missing data in the `last_name` column.

* `condition_1 | condition_2` will be TRUE if the patient is missing data in the `first_name` column, the `last_name` column, or in both columns.

* `condition_3` will be TRUE if the patient is age 18 or less.

THEREFORE:

* `my_condition` will be TRUE when **both** `condition_1 | condition_2` and `condition_3` are TRUE, when **at least one** of the columns `first_name` and `last_name` are blank, and the patient age is 18 or less.

</div>
***

## Transforming data in a DataFrame

Sometimes the data in a DataFrame isn't in the best form for us to use. Maybe it is a string that is too long or unclear, or maybe the units aren't the unit we will ultimately want to use to analyze the data.

There are two things we can do to make our data more useful.

1. Add a new column with data based on existing columns.

2. Edit the data in an existing column to improve its usefulness.

<div class ="warning">
Reproducibility must always been a priority when doing research, so whenever you are making changes to data, you must ensure that you keep a clear record of the calculations you did and even more importantly that you don't change the original copy of your data.

**Recording calculations**

There are many environments from which you can save Python code. One of the most user-friendly platforms is [Jupyter notebooks](https://jupyter.org/). These notebooks let you write linked cells of code as well as cells of non-code text, so they are a great way to preserve and annotate every step of your data manipulation.

**Preserving orignal data**

If you imported data from another source using `.read_csv()` or another such method, the original file still exists untouched! The best practice is to store your original data in a file that your code reads but does not change.

If your original data is not already in a separate file you can use `.to_csv(data.csv)` to create a new file containing your DataFrame as a csv file. You can also create files in [many other formats](https://pandas.pydata.org/docs/reference/io.html).
</div>

### Create new columns

@sage
<div class="python_data_init">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
covid_testing = pd.read_csv('https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv')
</script>
</lia-keep>
</div>
<br>

In `pandas` you can create a new column by calling your new column with the `.loc[:,"new_column"]` method and using a single equals sign `=` to define its contents.

The next bit of code creates a new column named `new_column` in the DataFrame `covid_testing` in which every entry is the number 1:

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
covid_testing.loc[:,"new_column"] = 1
print(covid_testing.loc[:,"new_column"])
</script>
</lia-keep>
</div>
<br>

Your new column can also depend on data in columns that already exist. Remember that each column, or series, needs to be called using the format `dataframe.loc[:,"column_name"]`.

For example maybe you need to have patient ages recorded in months instead of years:

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
covid_testing.loc[:,"age_months"] = covid_testing.loc[:,"age"]*12
print(covid_testing.loc[:,["age","age_months"]])
</script>
</lia-keep>
</div>
<br>

Or maybe you want a new column that displays the full name of each patient, rather than separate columns for first and last names.

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
covid_testing.loc[:,"full_name"] = covid_testing.loc[:,"first_name"]+" "+covid_testing.loc[:,"last_name"]
print(covid_testing.loc[:,["first_name", "last_name", "full_name"]])
</script>
</lia-keep>
</div>



### Edit existing columns
@sage
<div class="python_data_init">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
covid_testing = pd.read_csv('https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv')
</script>
</lia-keep>
</div>

You can make changes to existing entries using the same method and simply using the key that already exists for that column.

What if you wanted to reformat the gender column to use `M` and `F` instead of spelling out male and female?

**Using `=` to assign values**

One way to approach this is to define a condition testing each row for whether the entry in the `gender` column is `male`. Then we can use that condition to change the entry to `M` if the condition is met.

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
is_male = covid_testing.loc[:, "gender"] == "male"

covid_testing.loc[is_male, "gender"] = "M"

</script>
</lia-keep>
</div>
<br>

**Using `.replace`**

You can also use the `.replace` method to change entries in a column. The grammar required can be a bit tricky, but it is worth learning to use this powerful tool.

Let's take a look a using this method to change the gender `female` to `F`. After the code block we will go through what each part of the code is doing.

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
covid_testing.loc[:, "gender"] = covid_testing.loc[:, "gender"].replace("female","F")

print(covid_testing.loc[:,["first_name", "last_name", "gender"]])

</script>
</lia-keep>
</div>
<br>

* The `.replace()` method takes two arguments: the entry you want to find, and what you want to replace it with.

* Before  `.replace()` goes the DataFrame, or part of the DataFrame on which you want to find and replace the entry.

  * `dataframe.replace("a","b")` will search all columns of `dataframe` for `a` and replace them with `b`.

  * `dataframe.loc[:,"column_1"].replace("a","b")` will only replace `a` with `b` in the column labeled `column_1`. If another column contains the entry `a` that will remain unchanged.

* The `.replace()` method doesn't change the DataFrame, only the way it is shown to you that one time. In order to change the data in the DataFrame you need to use `=` to set the DataFrame equal to the version with the replacements.

  * If you `print(dataframe.replace("a","b"))` you will see that `a` has been replaced by `b`. However if you then `print(dataframe)` the `a` entries will still be there.

  * To change `a` to `b` in your DataFrame, redefine it: `dataframe = dataframe.replace("a","b")`. Now if you `print(dataframe)`, you will see all `a`s have been replaced by `b`.

**Simultaneous replacement**

The `.replace` method lets you replace multiple kinds of entries simultaneously. The same way we could enter lists into `.loc`, `.replace` can also accept two lists.

If we want to replace `positive` and `negative` with `1` and `0` respectively, we can ask for the list `["positive", "negative"]` to be replaced with the list `[1,0]`:


<div class="python_data">
<lia-keep>
<script type="text/x-sage">
covid_testing = covid_testing.replace(["positive","negative"],[1,0])

print(covid_testing.loc[:,["first_name", "last_name", "result"]])

</script>
</lia-keep>
</div>

<div class= "warning">
The order and length of these lists matter! Each element in the first list will be replaced by the element in the **same position** in the second list.
</div>

### Quiz: Transforming DataFrames

@sage
<div class="python_data_init">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
covid_testing = pd.read_csv('https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv')
</script>
</lia-keep>
</div>

You can change the all of the entries in a column to uppercase using the method `.str.upper()`. The code below **prints** the `last_name` column  of `covid_testing`  in uppercase:

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
print(covid_testing.loc[:, "last_name"].str.upper())
</script>
</lia-keep>
</div>
<br>

How would you **change** the the `last_name` column of `covid_testing` to be uppercase?

[( )] `covid_testing.loc[:, "last_name"].str.upper()`
[( )] `covid_testing.loc[:, "last_name"] == covid_testing.loc[:, "last_name"].str.upper()`
[(X)] `covid_testing.loc[:, "last_name"] = covid_testing.loc[:, "last_name"].str.upper()`
***
<div class = "answer">
- `covid_testing.loc[:, "last_name"].str.upper()` This command will change the way the `last_name` column is **displayed**, but will not make any changes to the DataFrame itself.

- `covid_testing.loc[:, "last_name"] == covid_testing.loc[:, "last_name"].str.upper()` The double equals `==` mean that this is a **condition** testing whether or not the entry int the `last_name` column is already uppercase.

- `covid_testing.loc[:, "last_name"] = covid_testing.loc[:, "last_name"].str.upper()` The single equals `=` **assigns** the entry in the `last_name` column to the uppercase version.
</div>
***

<div class = "learnmore">

The method `.str.lower()` will make every entry in a column lower case. There are several [other ways to manipulate the presentation of text](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lower.html) in a pandas series.

</div>

## Additional Resources

The creators of the pandas package have [great tutorials](https://pandas.pydata.org/docs/getting_started/index.html#tutorials) with very thorough examples.


## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work. Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Transform+Data+with+pandas%22)!

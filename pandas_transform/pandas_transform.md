<!--

author:   Elizabeth Drellich
email:    drelliche@chop.edu
version: 2.0.0
current_version_description: Replaced SageMathCells with Pyodide cells for better usability
module_type: standard
docs_version: 2.0.0
language: en
narrator: UK English Female
mode: Textbook

title: Transform Data with pandas

comment:  This is an introduction to transforming data using a Python library named pandas.

long_description: This module is for learners who have some familiarity with Python, and want to learn how the pandas library can handle large tabular data sets. No previous experience with pandas is required, and only an introductory level understanding of Python is assumed.

estimated_time_in_minutes: 60

@pre_reqs
Before starting this module it is useful for you to:

- have some familiarity with tabular data: data stored in an array of rows and columns.

- have an introductory level exposure to coding in Python, which could be acquired in the Python Basics sequence of modules ([Functions, Methods, and Variables](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#1); [Lists and Dictionaries](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_lists_dictionaries/python_basics_lists_dictionaries.md#1); and [Loops and Conditional Statements](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_loops_conditionals/python_basics_loops_conditionals.md#1)).
@end

@learning_objectives  

After completion of this module, learners will be able to:

- Import `pandas` and use functions from the `pandas` package.
- Load data into a `pandas` DataFrame.
- Use the `.loc` method to explore the contents of a DataFrame
- Filter a DataFrame using conditional statements.
- Transform data in a DataFrame.

@end

good_first_module: false
data_task: data_wrangling
coding_required: true
coding_level: intermediate
coding_language: python

@sets_you_up_for

- python_practice

@end

@depends_on_knowledge_available_in 

- python_basics_variables_functions_methods
- python_basics_lists_dictionaries
- python_basics_loops_conditionals

@end

@version_history 

Previous versions: 

- [1.1.1](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/255170ae36834565696b5d7e6e3e6621172a5666/pandas_transform/pandas_transform.md#1): Updated highlight boxes for greater clarity, other minor changes

- [1.0.2](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/4c378ba6d211f8ca852d4df9a550edb249cd3c68/pandas_transform/pandas_transform.md#1): Initial version

@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
import: https://raw.githubusercontent.com/arcus/education_modules/pyodide_testing/_module_templates/macros_python.md
import: https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md

-->

# Transform Data with pandas

@overview

## Lesson Preparation

@lesson_prep_python_pyodide

## The `pandas` Package

The `pandas` [package](https://pandas.pydata.org/) lets you store, examine, and manipulate tabular data using python. Since many machine learning tools use python, it can be particularly useful to process tabular data in that same environment.

<div class = "history">
<b style="color: rgb(var(--color-highlight));">Historical context</b><br>

Most people associate "pandas" with the large mammals [Ailuropoda melanoleuca](https://en.wikipedia.org/wiki/Giant_panda) but the `pandas` package is actually a shortening of "panel data."

</div>

### Importing `pandas`

**The pandas package**

Because `pandas` isn't part of python, in order to use its tools you will need to **import** the pandas package at the beginning of each session you intend to use it.

The code `import pandas` tells python that you want all of the commands and tools that `pandas` has to be available to you. For example `read_csv` is a  function in `pandas` and regular python will not recognize it! You will have to tell python that a command you are using is a `pandas` command by entering `pandas.read_csv`.

**Rename `pandas` to `pd`**

To make it easier to type out these commands, you can give the `pandas` package a different name when you import it using `as new_name`. While you could in theory pick any name you want, the standard abbreviation is `pd`.

```python
import pandas as pd
```
@Pyodide.eval

If you click the **Execute** button <i aria-hidden="true" class="icon icon-compile-circle lia-btn__icon"></i>, you can watch as the `pandas` package, which is also called a **module**, is downloaded. This line of code is giving us access to all of the `pandas` tools.

### DataFrames and Series

The `pandas` package lets you handle two types of data structures that python alone can't: **DataFrames** and **Series**. Before we can start exploring them, let's make sure we have `pandas` imported. 

```python
import pandas as pd
```
@Pyodide.eval

If you just ran this same code importing `pandas` on the previous page, you shouldn't see any output because the package was already available to you. But if you are starting on this page, or didn't run the code on the last page, you will get a message that the module is being downloaded.

DataFrames
---

**DataFrame** is the name `pandas` gives to its primary data structure. You can think of a DataFrame like a spreadsheet: it has rows and columns, and you can look up the data in it by referencing those rows and columns.

Let's take a look at a basic DataFrame. This one is being built from scratch, but we aren't going to spend any time learning how to do that in this module because you will usually be using `pandas` to analyze data that you import from somewhere else.

**Run this code** to print out the DataFrame `df`. 

```python
d = {'col1': [1, 5, 7], 'col2': [3, .4, -2], 'col3':["yes", "no","blue"]};
df = pd.DataFrame(data=d);
print(df)

```
@Pyodide.eval

Series
---

You might have noticed that in the above example, everything in the first column was an integer, everything in the second column had a decimal point, and the third column consisted of words. Each column in a DataFrame is called a **series**. A series is a one-dimensional array in which all of the data has the same **type**.

**Run this code** to print out `col1` from the DataFrame `df`.

```python
print(df['col1'])

```
@Pyodide.eval

Did you notice the `Name` and `dtype` at the bottom? Those tell you the name of the series and its data type. Try changing `col1` to `col2` or `col3` to see what type of data those series contain.


### Quiz: `pandas` package [UPDATE]

```python
d = {'col1': [1, 5, 7], 'col2': [3, .4, -2], 'col3':["yes", "no","blue"]};
df = pd.DataFrame(data=d);
print(df)

```
@Pyodide.eval

You show this code to a friend. They try to run it in a Jupyter notebook on their computer, but it doesn't run, despite being exactly what ran for you on the previous page! 

This is an extremely common and frustrating experience, what are some possible reasons why it isn't working for them?

[[ ]] The code shouldn't have worked for either of you.
[[X]] You had imported a package that they don't yet have.
[[X]] They have defined a variable or module differently than you did.
[[ ]] Their computer doesn't like them.
***
<div class="answer">

When working code is copied to another location and then fails to work, it is usually because of a missing package or a differently defined variable.

</div>
***


Your friend shows you the error message they got when running the code: `NameError: name 'pd' is not defined`. What command should they enter before the first line of code?

[[import pandas as pd]]
***
<div class = "answer">

`NameError: name 'pd' is not defined` is a helpful error message because it tells you exactly what you friend forgot: they never defined `pd`!

You have already told python to import then pandas module and that whenever you enter `pd` you mean `pandas`. But your friend's computer doesn't know that yet. Adding the line `import pandas as pd` to the top of their code, will almost certainly make this run in their notebook.

```python
import pandas as pd
d = {'col1': [1, 5, 7], 'col2': [3, .4, -2], 'col3':["yes", "no","blue"]};
df = pd.DataFrame(data=d);
print(df)

```
@Pyodide.eval

</div>
***

## Tabular Data in `pandas` DataFrames

The tiny DataFrame we saw in the last section was exceptional in several ways. With real data you are likely to have some challenges that just can't be replicated with something that small:

* Real data will almost always be too big to type into a DataFrame.

* Real data frequently has too many rows and columns to look at the whole dataset at once.

* Real data is often missing entries.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

For this module we will be looking at some fake Covid-19 testing data. Although this data is designed to mimic realistic data with plausible patterns and values, **there is no Protected Health Information in this data**. If you are a fan of the fictional series "Game of Thrones," however, you might recognize some familiar characters.

This data is saved as a [csv file hosted on GitHub](https://raw.githubusercontent.com/arcus/education_modules/main/pandas_transform/data/covid_testing.csv).

</div>

### Loading data

The `pandas` package can read most tabular data files and convert them into DataFrames. As long as your data is in a place that the program can locate (either on your computer if you are running code on your computer, or in the cloud) all `pandas` needs to know is what type of file it is reading, and where to find that file.

The fake Covid-19 testing data we will use for the rest of this lesson is saved as a [csv file hosted on GitHub](https://raw.githubusercontent.com/arcus/education_modules/main/pandas_transform/data/covid_testing.csv).

The `read_csv` function from the `pandas` library takes the location of the file as its argument. The path to the file, in this case a url, must be in quotes. Let's create a new DataFrame called `covid_testing` that will contain all of our fake Covid-19 testing data.

```python
covid_testing = pd.read_csv('https://raw.githubusercontent.com/arcus/education_modules/main/pandas_transform/data/covid_testing.csv')
```

``` python   @Pyodide.exec
import pandas as pd
import io
from pyodide.http import open_url

url = "https://raw.githubusercontent.com/arcus/education_modules/main/pandas_transform/data/covid_testing.csv"

url_contents = open_url(url)
text = url_contents.read()
file = io.StringIO(text)

covid_testing = pd.read_csv(file);

"HTML: <a href='" + url + "'>covid_testing</a> has been loaded"
```

@pyodide_readcsv_explainer

If you're running this code on your computer, you didn't have any output after the last command because we didn't ask it to print anything. But it did create the `covid_testing` DataFrame. We can take a look at with `print(covid_testing)`:

```python
print(covid_testing)

```
@Pyodide.eval

Unless you have an extremely wide browser window, the output above will only show as many columns as it can fit at a time. Some interfaces will output the DataFrame and let you scroll right to see more columns, but this interface just prints as many columns as it can fit and then shows you the real dimensions at the bottom. Good thing it didn't print all 15524 rows!

When you print a DataFrame or Series you will see the first five rows and the last five rows of a DataFrame. If, like this one, it has more than 10 rows, the hidden rows will be indicated by ellipses. You can also ask for the first or last 5 rows of data using the methods `.head()` and `.tail()`. Try putting a number in the parentheses to get different numbers of rows.

```python
print(covid_testing.head(4))

```
@Pyodide.eval


Loading your own data
---

If you are trying out this code on your own computer, you can make a DataFrame out of any tabular data you have access to! To create a DataFrame of your data, make sure you use the right command for your file type, and make sure the location of the file is in quotes.

| File type | Read command |
| - | - |
| .csv | pd.read_csv('location')|
| .xlsx | pd.read_excel('location')|
| .ods | pd.read_excel('location')|
| .json| pd.read_json('location')|
| .html| pd.read_html('location')|
| .sql | pd.read_sql('location')|

### Column names and row indices

``` python   @Pyodide.exec
import pandas as pd
```

When a DataFrame is displayed it has a row of column names along the top, and a column of indices along the left side. In some environments, like Jupyter notebooks, these names and indices may be bolded.

The methods `.columns` and `.index` will show you all of the column and row names, respectively. **Give it a try:**

```python
print(covid_testing.columns)
# also try with .index instead of .columns

```
@Pyodide.eval

The column names were imported with the `.csv` file. Since the original file didn't have labels for the rows, `pandas` automatically labeled them numerically 0 through 15523. If you imported tabular data that didn't have column headers, the column names would be numeric, the way the row indices are in our `covid_testing` DataFrame.

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

**What does that RangeIndex mean?**

The `covid_testing.index` is `RangeIndex(start=0, stop=15524, step=1)`, but on the previous page we saw that the last row of this DataFrame is labeled 15523. Why is that?

Python ranges can be confusing even for people who use them all the time. Some things to keep in mind are:

- Python starts counting at 0.
- Python ranges include their lower bounds.
- Python ranges **do not include their upper bounds**.

For example `range(0,4)` contains 4 elements. Those elements are 0,1,2, and 3.

</div>

### Locating data with `.loc`

``` python   @Pyodide.exec
import pandas as pd
```

The `.loc` method lets you select a subset of your DataFrame to display.

Selecting a single entry
---

The grammar of the `.loc` method is `dataframe.loc[row(s), column(s)]`. To see the age of the of the very first person to be tested, i.e. extract the data from row `0` (python starts counting with 0) and column `"age"` enter `covid_testing.loc[0,"age"]`.

```python
print(covid_testing.loc[0,"age"])

```
@Pyodide.eval

You need the `"` surrounding `age` because that column header is a string. No quotes are needed around the row index `0` because it is recognized as a known value.

Selecting multiple rows or columns
---

If you want to see the ages of the first 3 patients tested, change the `0` to the list `[0,1,2]`. This indicates that you want to see the data in rows indexed 0,1, and 2. Similarly you can change the single column to be a list of columns.

```python
print(covid_testing.loc[[0,1,2],[ "age", "gender"]])

```
@Pyodide.eval

Viewing full rows and columns
---

If you want to show all of the data in a row or column, instead of a list you can use a colon `:` to indicate that you want to include everything.

```python
print(covid_testing.loc[:,["mrn","first_name","last_name"]])

```
@Pyodide.eval

A colon before the comma will show you all rows of the columns you selected and a colon after the comma will return all columns of the given rows.

Your turn:
---

What do you think will happen if you put colons both before and after the comma? Change the code below to check if you were correct.

```python
print(covid_testing.loc[[2,3,4],:])

```
@Pyodide.eval

<div class = "options">
<b style="color: rgb(var(--color-highlight));">Another option</b><br>

If you look at other people's code, you may see columns referred to with `data_frame["column_name"]` instead of `data_frame.loc[:,"column_name"]`. While this will frequently give the same output, i.e. show you the entire column, it can [raise errors if you use it to try to update data](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html). For that reason we are focusing on the `.loc` method.

</div>

### Quiz: DataFrames

``` python   @Pyodide.exec
import pandas as pd
import io
from pyodide.http import open_url

url = "https://raw.githubusercontent.com/arcus/education_modules/main/pandas_transform/data/covid_testing.csv"

url_contents = open_url(url)
text = url_contents.read()
file = io.StringIO(text)

covid_testing = pd.read_csv(file);

"HTML: <a href='" + url + "'>covid_testing</a> has been loaded"
```

Complete the following code by replacing the `__?__` with your own code to find out the first and last name of the patient in row 11942.
Assume that the `covid_testing` DataFrame has already been created and the pandas package has been loaded.

```python 
print(covid_testing.__?__[11942, ["first_name","last_name"]])

```
@Pyodide.eval

Enter their name below to check your answer:

[[grazdan greyjoy]]
<script>
  let input = "@input".trim().toLowerCase();
  input == "grazdan greyjoy";
</script>
***
<div class = "answer">

The `.loc` method will request the data from row 11942 and columns `"first_name"` and `"last_name"`.

The completed code should look like this:

```
print(covid_testing.loc[11942, ["first_name","last_name"]])
```

</div>
***

## Conditional statements

``` python   @Pyodide.exec
import pandas as pd
```

Let's say we only care about the positive Covid tests. We could make a new DataFrame consisting only of those tests that came back positive using a **conditional** argument. A condition is a statement that evaluates to either `True` or `False`.

If, for example, we only want to look at instances where the covid test came back positive, we need to use the condition `covid_testing.loc[:,"result"] == "positive"`. This statement checks every row in the `covid_testing` and will be `True` for a given row if the entry in column `result` is equal to the string `positive` and `False` otherwise.

Run the following code to see the results of this conditional test for each row in `covid_testing` (note that we're not yet filtering the DataFrame, just looking at the results of the condition).

```python
print(covid_testing.loc[:,"result"] == "positive")

```
@Pyodide.eval

`False` means the value for `result` for that row is NOT `"positive"` and `True` means it is `"positive"`.

In the example above we used the double equals sign `==` to check whether two objects were the same. This is different from the single equals sign we use to define objects, such as when we created the `covid_testing` DataFrame.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

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

``` python   @Pyodide.exec
import pandas as pd
```

When we used a column name or list of names as our argument in the row spot of the `.loc` method, we got back all rows in that list. When we put a condition  like `covid_testing.loc[:,"result"] == "positive"` in the row spot, it will return all rows for which that condition is `True`.

If this is a subset of the data that you are likely to want to use again, it is a good practice to create a new DataFrame consisting only of the rows and columns that you want.

Your turn:
---

Create a new DataFrame titled `positive_tests`. How many rows have positive test results?

```python
positive_tests = covid_testing.loc[covid_testing.loc[:,"result"] == "positive",:].copy()
print(positive_tests)

```
@Pyodide.eval

There are more columns here than will fit on the page. 
You can ask to see just the columns you want to make the output more useful. 
Try replacing `print(positive_tests)` with  `print(positive_tests.loc[:,["first_name","last_name"]])` and see if that output is easier to understand.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

**`.copy()`**

The method `.copy()` at the very end of line one creates a new DataFrame separate from the original. Omitting the `.copy()` method won't change the output in the next code block, but can have consequences if you later want to make changes to your DataFrame.

- `new_name = dataframe.loc[rows,columns].copy()` creates a new DataFrame called `new_name` that you can make changes to without impacting the original `dataframe` and vice versa.

- `new_name = dataframe.loc[rows,columns]` does not create a new DataFrame. Instead every time you type `new_name` after this, it will understand that you mean `dataframe.loc[rows,columns]`.

</div>

### Combining conditions

``` python   @Pyodide.exec
import pandas as pd
```

We can also combine conditions using `&` for **and**, and the vertical "pipe" `|` **or**. The `|` can be found above the forward slash \ on your keyboard. The code below shows us only the rows for patients age 18 or older who tested positive.

```python
adult_positive = covid_testing.loc[(covid_testing.loc[:,"result"] == "positive") & (covid_testing.loc[:,"age"] >= 18), :]
print(adult_positive.loc[:,["first_name","last_name", "age"]])

```
@Pyodide.eval

Our code is starting to look quite messy. Giving each condition a name is a good way to keep your code from becoming an unreadable tangle of conditional statements.

Name your conditions
---

When working with more complicated conditions it is extremely helpful to define your condition by giving it a name, and then refer to that name, rather than the chain of conditions, inside the `.loc` method. By carefully naming the compound condition, you can also make your code more human-readable. Take a moment to see what this code below is doing:

```python
is_positive_infant = (covid_testing.loc[:,"age"]<1) & (covid_testing.loc[:,"result"] == "positive")

infant_positive = covid_testing.loc[is_positive_infant,:].copy()
print(infant_positive.loc[:,["first_name","last_name","age"]])

```
@Pyodide.eval

Use parentheses
---

When combining conditions, you should use parentheses around each condition. This isn't just for the benefit of humans reading your code. If you are combining three or more conditions, the placement of parentheses can change the meaning of a condition.

The condition:
`((positive_test) & (older_than_10)) | (younger_than_5)`
is true for all results where a patient was older than 10 and tested positive, as well as all children under five, whether or not they tested positive. By moving the parentheses we can change the condition to test for patients older than 10 or younger than 5, but only return those with positive test results.


### Missing Data

``` python   @Pyodide.exec
import pandas as pd
```

So far we have been treating the `covid_testing` DataFrame as if it has a value in every row of every column, but like most real data sets, some data is missing!

Wherever the original csv file didn't have an entry, you will see `NaN` or `nan`, meaning "Not a Number." For which columns is the patient in row 2 missing data?

```python
print(covid_testing.loc[2, :])

```
@Pyodide.eval

`NaN`s are special in a couple of ways.

1. They are not strings, you can't type them in directly when setting the value of a cell.
2. Two `NaN`s are **not equal** to each other.

For example we know that patient 2 has no data, i.e. `NaN` in both the column `payor_group` and the column `patient_class`. The double equals sign `==` will tell us if those two entries are the same:

```python
are_NaNs_equal = (covid_testing.loc[2,"payor_group"] == covid_testing.loc[2, "patient_class"])

print(are_NaNs_equal)

```
@Pyodide.eval

Notice that the above cell uses both of the techniques we learned for combining conditions: there are parentheses surrounding the condition `a == b` and the condition has a short, readable name.

Since using `==` to check if a cell is empty won't work, we have the methods `.isna()` and `.isnull()`. These do exactly the same thing: they return `True` if the cell is empty, and `False` if the cell contains information. You can run these methods on a DataFrame or a series (a column of a DataFrame) but not on a single cell:

```python
print(covid_testing.loc[:,"payor_group"].isna())

```
@Pyodide.eval

The opposite of `.isna()` is the method `.notna()`.

For example you might want to create a new DataFrame of only patients whose `payor_group` is known:

```python
known_payor = covid_testing.loc[:,"payor_group"].notna()

known_payor_tests = covid_testing.loc[known_payor, :].copy()

print(known_payor_tests.loc[:, ["first_name", "last_name", "payor_group"]])

```
@Pyodide.eval

### Quiz: Conditional statements

``` python   @Pyodide.exec
import pandas as pd
```

You come across the following code in which several conditions are defined but not given descriptive names:


```python
condition_1 = covid_testing.loc[:,"first_name"].isna()

condition_2 = covid_testing.loc[:,"last_name"].isna()

condition_3 = covid_testing.loc[:,"age"]<=18

my_condition = (condition_1 | condition_2) & condition_3
```

```python
# test things here

```
@Pyodide.eval

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

``` python   @Pyodide.exec
import pandas as pd
```

Sometimes the data in a DataFrame isn't in the best form for us to use. Maybe it is a string that is too long or unclear, or maybe the units aren't the unit we will ultimately want to use to analyze the data.

There are two things we can do to make our data more useful.

1. Add a new column with data based on existing columns.

2. Edit the data in an existing column to improve its usefulness.

<div class ="warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

Reproducibility must always been a priority when doing research, so whenever you are making changes to data, you must ensure that you keep a clear record of the calculations you did and even more importantly that you don't change the original copy of your data.

**Recording calculations**

There are many environments from which you can save Python code. One of the most user-friendly platforms is [Jupyter notebooks](https://jupyter.org/). These notebooks let you write linked cells of code as well as cells of non-code text, so they are a great way to preserve and annotate every step of your data manipulation.

**Preserving original data**

If you imported data from another source using `.read_csv()` or another such method, the original file still exists untouched! The best practice is to store your original data in a file that your code reads but does not change.

If your original data is not already in a separate file you can use `.to_csv(data.csv)` to create a new file containing your DataFrame as a csv file. You can also create files in [many other formats](https://pandas.pydata.org/docs/reference/io.html).

</div>

### Create new columns

``` python   @Pyodide.exec
import pandas as pd
```

In `pandas` you can create a new column by calling your new column with the `.loc[:,"new_column"]` method and using a single equals sign `=` to define its contents.

The next bit of code creates a new column named `new_column` in the DataFrame `covid_testing` in which every entry is the number 1:

```python
covid_testing.loc[:,"new_column"] = 1
print(covid_testing.loc[:,["first_name", "last_name", "new_column"]])

```
@Pyodide.eval

Your new column can also depend on data in columns that already exist. Remember that each column, or series, needs to be called using the format `dataframe.loc[:,"column_name"]`.

For example maybe you need to have patient ages recorded in months instead of years:

```python
covid_testing.loc[:,"age_months"] = covid_testing.loc[:,"age"]*12
print(covid_testing.loc[:,["age","age_months"]])

```
@Pyodide.eval

Or maybe you want a new column that displays the full name of each patient, rather than separate columns for first and last names.

```python
covid_testing.loc[:,"full_name"] = covid_testing.loc[:,"first_name"]+" "+covid_testing.loc[:,"last_name"]
print(covid_testing.loc[:,["first_name", "last_name", "full_name"]])

```
@Pyodide.eval


### Edit existing columns

``` python   @Pyodide.exec
import pandas as pd
```

You can make changes to existing entries using the same method and simply using the key that already exists for that column.

What if you wanted to reformat the gender column to use `M` and `F` instead of spelling out male and female?

Using `=` to assign values
---

One way to approach this is to define a condition testing each row for whether the entry in the `gender` column is `male`. Then we can use that condition to change the entry to `M` if the condition is met.

```python
is_male = covid_testing.loc[:, "gender"] == "male"

covid_testing.loc[is_male, "gender"] = "M"

print(covid_testing.loc[:,["first_name", "last_name", "gender"]])

```
@Pyodide.eval

Using `.replace`
---

You can also use the `.replace` method to change entries in a column. The grammar required can be a bit tricky, but it is worth learning to use this powerful tool.

Let's take a look a using this method to change the gender `female` to `F`. After the code block we will go through what each part of the code is doing.

```python
covid_testing.loc[:, "gender"] = covid_testing.loc[:, "gender"].replace("female","F")

print(covid_testing.loc[:,["first_name", "last_name", "gender"]])

```
@Pyodide.eval

* The `.replace()` method takes two arguments: the entry you want to find, and what you want to replace it with.

* Before  `.replace()` goes the DataFrame, or part of the DataFrame on which you want to find and replace the entry.

  * `dataframe.replace("a","b")` will search all columns of `dataframe` for `a` and replace them with `b`.

  * `dataframe.loc[:,"column_1"].replace("a","b")` will only replace `a` with `b` in the column labeled `column_1`. If another column contains the entry `a` that will remain unchanged.

* The `.replace()` method doesn't change the DataFrame, only the way it is shown to you that one time. In order to change the data in the DataFrame you need to use `=` to set the DataFrame equal to the version with the replacements.

  * If you `print(dataframe.replace("a","b"))` you will see that `a` has been replaced by `b`. However if you then `print(dataframe)` the `a` entries will still be there.

  * To change `a` to `b` in your DataFrame, redefine it: `dataframe = dataframe.replace("a","b")`. Now if you `print(dataframe)`, you will see all `a`s have been replaced by `b`.

Simultaneous replacement
---

The `.replace` method lets you replace multiple kinds of entries simultaneously. The same way we could enter lists into `.loc`, `.replace` can also accept two lists.

If we want to replace `positive` and `negative` with `1` and `0` respectively, we can ask for the list `["positive", "negative"]` to be replaced with the list `[1,0]`:


```python
covid_testing = covid_testing.replace(["positive","negative"],[1,0])

print(covid_testing.loc[:,["first_name", "last_name", "result"]])

```
@Pyodide.eval

<div class= "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

The order and length of these lists matter! Each element in the first list will be replaced by the element in the **same position** in the second list.

</div>

### Quiz: Transforming DataFrames

``` python   @Pyodide.exec
import pandas as pd
```

You can change the all of the entries in a column to uppercase using the method `.str.upper()`. The code below **prints** the `last_name` column  of `covid_testing` in uppercase:

```python
print(covid_testing.loc[:, "last_name"].str.upper())

```
@Pyodide.eval

How would you **change** the `last_name` column of `covid_testing` to be uppercase?

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

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

The method `.str.lower()` will make every entry in a column lower case. There are several [other ways to manipulate the presentation of text](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lower.html) in a pandas series.

</div>

## Additional Resources

The creators of the pandas package have [great tutorials](https://pandas.pydata.org/docs/getting_started/index.html#tutorials) with very thorough examples.

## Feedback

@feedback

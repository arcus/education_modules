<!--

author:   Elizabeth Drellich
email:    drelliche@chop.edu
version:  0.0.1
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Module Title
comment:  This is an introduction to tabular data in python using `pandas` DataFrames.
long_description: This is a longer description, which should be understandable for a lay audience. It will print under "Is this module right for me?" in the overview.
estimated_time: 1 hour

@learning_objectives  

After completion of this module, learners will be able to:

- Import `pandas` and use functions from the `pandas` package.
- Load data into a `pandas` DataFrame.
- Explore the contents of a DataFrame, including missing data.
- Create new columns in an existing DataFrame.

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
-->

# Transforming Data in Python using Pandas

## Embedded Code Testing:
@sage

Python cell:
<div class="python">
<lia-keep>
<script type="text/x-sage">
1+2
</script>
</lia-keep>
</div>


<div class="python">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
d = {'col1': [1, 2], 'col2': [3, 4]};
df = pd.DataFrame(data=d);
print(df)
</script>
</lia-keep>
</div>


Jupyterlite lab environment:
??[notebook](https://arcus.github.io/jupyterlite/lab/index.html)

Jupyterlite classic notebook:
??[notebook](https://arcus.github.io/jupyterlite/retro/notebooks/?path=p5.ipynb)

<div class = "overview">
## Overview

@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

Before starting this module it is useful for you to:

* have some familiarity with [tabular data](tabular/data/module)
* have an introductory level exposure to coding in [python](intro/to/python/module)
* know how to run a [Jupyter notebook](link/here?).

**Learning Objectives**

@learning_objectives

</div>

## Lesson Preparation
@sage

You will be doing two types of hands-on coding as you work your way through this module. You do not need any particular preparation for the first way, interactive python cells. For the second way, Jupyter notebooks, you can choose to work in your browser where you will not be able to save your work, or in a few other ways where you will.

**Interactive python cells**

The first will be in cells powered by [SageMathCell](https://sagecell.sagemath.org/). For the most part, these will appear with some code already in them, and you can run that code by clicking the **Run python** button. You can also edit the code in these cells and run your own code.

Give it a try:
<div class="python">
<lia-keep>
<script type="text/x-sage">
print(1+2)
</script>
</lia-keep>
</div>

<div class = "important">
These cells will compute everything you ask them to, but will only output what you explicitly request using the `print()` command. Try
</div>

**Jupyter notebooks**

The longer hands-on exercises in this module are in a Jupyter notebook. The notebook is embedded into the module and you are welcome to do the exercises there. However this will not save your work if you want to come back and see what you did in a few days. If you want that ability, you have two options:

1. If you have python on your computer, you can download he notebook and run it yourself.

2. Make and account somewhere to run it in the cloud?



## The `pandas` Package

The `pandas` [package](https://pandas.pydata.org/) lets you store, examine, and manipulate tabular data using python. Since many machine learning tools use python, it can be particularly useful to process tabular data in that same environment.

<div class = "learnmore">
Most people associate "pandas" with the large mammals [Ailuropoda melanoleuca](https://en.wikipedia.org/wiki/Giant_panda). The `pandas` package is actually a shortening of "panel data."
</div>

### Importing `pandas`

**`import pandas`**

Because `pandas` isn't part of python, in order to use its tools you will need to **import** the pandas package at the beginning of each session you intend to use it.

The code `import pandas` tells python that you want all of the commands and tools that `pandas` has to be available to you. For example `read_csv` is a  function in `pandas` and regular python will not recognize it! You will have to tell python that a command you are using is a `pandas` command by entering `pandas.read_csv`.

**`as pd`**

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

<div class = "help">
Did you get an error when you tried to print out a column? Make sure you run the cell above to define `df` before you try to reference it!
</div>

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

When you add the line `import pandas as pd` to their code, it runs as it did before.

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

## Exploring Data with `pandas`

The tiny DataFrame we saw in the last section was exceptional in several ways. With real data you are likely to have some challenges that just can't be replicated with something that small:

* Real data will almost always be too big to type into a DataFrame.

* Real data frequently has too many rows and columns to look at the whole dataset at once.

* Real data is often missing entries.

### Loading data
@sage
<div class="python_data_init">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
</script>
</lia-keep>
</div>

The `pandas` package can read most tabular data files and convert them into DataFrames. As long as your data is in place that the program can locate, either on your computer if you are running code on your computer, or in the cloud, all `pandas` needs to know is what type of file it is reading, and where to find that file.

For this modules we will be looking at some fake Covid-19 testing data. This data is saved as a csv file and is hosted on [GitHub](https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv).

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

Good thing it doesn't print all 15524 rows! Unless you specify a different subset, you will see the first five rows and the last five rows of a DataFrame. If, like this one, it has more than 10 rows, the hidden rows will be indicated by ellipses.

You can also ask for the first or last 5 rows of data using the methods `.head()` and `.tail()`. Try putting a number in the parentheses to get different numbers of rows.

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
print(covid_testing.head())
</script>
</lia-keep>
</div>

<div class = "important">
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

</div>

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
covid_testing.columns
</script>
</lia-keep>
</div>

The column names were imported with the `.csv` file. If you imported tabular data that didn't have column headers, the column names will be numeric, the way the row indices are in our `covid_testing` DataFrame. They let us refer to individual rows and columns.

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
covid_testing.loc[0,"age"]
</script>
</lia-keep>
</div>

You need the `"` surrounding `age` because that column header is a string. No quotes are needed around the row index `0` because it is recognized as a known value.

**Selecting multiple rows or columns**

If you want to see the ages of the first 3 patients tested, change the `0` to the list `[0,1,2]`. This indicates that you want to see the data in rows indexed 0,1, and 2. Similarly you can change the single column to be a list of columns.

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
covid_testing.loc[[0,1,2],[ "age", "gender"]]
</script>
</lia-keep>
</div>

**Viewing full rows and columns**

If you want to show all of the data in a row or column, instead of a list you can use a colon `:` to indicate that you want to include everything.

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
covid_testing.loc[:,["mrn","first_name","last_name"]]
</script>
</lia-keep>
</div>
<br>

A colon before the comma will show you all rows of the columns you selected and a colon after the comma will return all columns of the given rows.

**Your turn:** What do you think will happen if you put colons both before and after the comma? Change the code below to check if you were correct.

<div class="python_data">
<lia-keep>
<script type="text/x-sage">
covid_testing.loc[[2,3,4],:]
</script>
</lia-keep>
</div>
<br>


### Quiz: Exploring datasets

@sage

Complete the following code by replacing the two `__?__`s with your own code to find out the first and last name of the patient in row 11942.

<div class="python">
<lia-keep>
import pandas as pd
covid_testing = pd.__?__('https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv')

print(covid_testing.__?__[11942, ["first_name","last_name"]])
</script>
</lia-keep>
</div>
<br>

Enter their name below to check your answer:
[[grazdan greyjoy]]

***
<div class = "answer">

On line 2, the command `read_csv` will convert the csv file's data into a DataFrame.

On line 4, the `.loc` method will request the data from row 11942 and columns `"first_name"` and `"last_name"`.

<div class="python_run">
<lia-keep>
import pandas as pd
covid_testing = pd.read_csv('https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv')

print(covid_testing.loc[11942, ["first_name","last_name"]])
</script>
</lia-keep>
</div>
</div>
***

## Editing a DataFrame


### Adding new columns

### Editing existing columns

### Logical and mathematical functions in Python
maybe?

### Missing Data
@sage
<div class="python_data">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
covid_testing = pd.read_csv('https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv')
</script>
</lia-keep>
</div>

### Quiz: Editing datasets

Here is some code, multiple choice what did it filter by?

## Hands-On Activity
Do I really have time for this in an hour? I suspect no....

## Additional Resources

The creators of the pandas package have [great tutorials](https://pandas.pydata.org/docs/getting_started/index.html) with very thorough examples.

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work. Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Transform+Data+with+Pandas%22)!

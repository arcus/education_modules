<!--

author:   Elizabeth Drellich
email:    drelliche@chop.edu
version:  0.0.1
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Module Title
comment:  This is a short, focused description of the module.
long_description: This is a longer description, which should be understandable for a lay audience. It will print under "Is this module right for me?" in the overview.
estimated_time: 1 hour

@learning_objectives  

After completion of this module, learners will be able to:

- Navigate the row and column structure of a `pandas` DataFrame
- Locate data using the `.loc` method
- Filter data using conditional statements
- Create new DataFrames from existing DataFrames
- Edit data in a `pandas` DataFrame.

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

Your friend's code isn't running, which is extremely frustrating because they copy and pasted it from the previous page of this module. Can you add a line to make it run correctly?

[[?]] Hint: What does the error message say is wrong?
[[?]] Hint: What do we need to include at the top in order to make `pandas` commands available to us?

<div class="python_run">
<lia-keep>
<script type="text/x-sage">
d = {'col1': [1, 5, 7], 'col2': [3, .4, -2], 'col3':["yes", "no","blue"]};
df = pd.DataFrame(data=d);
print(df)
</script>
</lia-keep>
</div>

<div class = "answer">
`NameError: name 'pd' is not defined` is a helpful error message because it tells you exactly what you friend forgot: they never defined `pd`!

When you add the line `import pandas as pd` to their code, it runs as it did before.
</div>


## Exploring Data with `pandas`

The tiny DataFrame we saw in the last section was exceptional in several ways. With real data you are likely to have some challenges that just can't be replicated with something that small:

* Real data will almost always be too big to type into a DataFrame.

* Real data frequently has too many rows and columns to look at the whole dataset at once.

* Real data is often missing entries.

### Importing data



### Filtering rows and columns

### Missing entries

### Quiz: Exploring datasets


## Creating new columns

### Logical and mathematical functions in Python

## Hands-On Activity

## Additional Resources

The last section of the module content should be a list of additional resources, both ours and outside sources, including links to other modules that build on this content or are otherwise related.

The creators of the pandas package have [great tutorials](https://pandas.pydata.org/docs/getting_started/index.html) with very thorough examples.

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Transform+Data+with+Pandas%22)!

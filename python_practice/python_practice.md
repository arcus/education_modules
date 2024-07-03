<!--
module_id: python_practice
author:   Meredith Lee
email:    leemc@chop.edu
version: 1.0.7
current_version_description: Initial version with updated links and metadata; make liascript link(s) point to first page
module_type: exercise
docs_version: 1.2.0
language: en
narrator: UK English Female
mode: Textbook
title: Python Practice
comment: Use the basics of Python coding, data transformation, and data visualization to work with real data. 
long_description: When learning Python for data science, the ultimate goal is to be able to put all of the pieces together to analyze a dataset. This module aims to provide a data science task in order to help learners practice Python skills in a real-world context. 
estimated_time_in_minutes: 60

@pre_reqs
Learners should be familiar with the basics of Python coding, including [functions, methods, and variables](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#1), [lists and dictionaries](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_lists_dictionaries/python_basics_lists_dictionaries.md#1), [loops and conditionals](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_loops_conditionals/python_basics_loops_conditionals.md#1), [data transformation with pandas](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/pandas_transform/pandas_transform.md#1) and [data visualization with matplotlib and seaborn](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/data_visualization_in_seaborn/data_visualization_in_seaborn.md#1). Learners should also have access to Python, either on their own computer or in the cloud. 
@end

@learning_objectives

- Import a dataset from an online database
- Recode data and change variable types in a dataframe
- Use exploratory data visualization to identify trends in data and generate hypotheses

@end

good_first_module: false
collection: learn_to_code
coding_required: true
coding_level: intermediate
coding_language: python

@sets_you_up_for

@end

@depends_on_knowledge_available_in

- python_basics_variables_functions_methods
- python_basics_lists_dictionaries
- python_basics_loops_conditionals
- pandas_transform
- data_visualization_in_seaborn

@end

@version_history 

No previous versions.
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md

-->

# Python Practice

@overview

## Lesson Preparation

For this module, you'll need access to Python, either on your own computer or in the cloud. For details about how to download Python or use Google Colab (a cloud-based notebook environment), you can take a look at the ["Accessing Python" section of our Demystifying Python module](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_python/demystifying_python.md#9). 

## Topics to Review

- Importing Python libraries 
- Reading a CSV and creating a data frame
- Editing/recoding data
- Exploratory data visualization

Stretch topics
=====

There are a couple of additional skills that haven't been introduced in a module yet, but that might come in handy solving this data science problem: 

- Correlation matrices
- Heat maps

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Finding correlations and creating heat maps are not topics that you have learned in preceding modules or in other prior learning -- which means you might need to do some searching to figure out how to do them! This is an important step in your development as a programmer and a data scientist, but don't worry if it seems difficult in the beginning; it'll get easier with practice. To start, try Googling "Python" and "correlations" and see where it takes you. 

</div>

## The Data

For this practice module we will be using real, publicly-available cervical cancer data from [UC Irvine's machine learning data repository](http://archive.ics.uci.edu/). To download the data file, [follow this link to the cervical cancer risk factors dataset](http://archive.ics.uci.edu/dataset/383/cervical+cancer+risk+factors) and click the "Download" button, which you should see on the right of the page. 

If you have done the [R Practice Module](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_practice/r_practice.md#1), this dataset might be familiar! 


## Practice Problem

According to the UCI Machine Learning database, the Cervical Cancer (Risk Factors) dataset "focuses on the prediction of indicators/diagnosis of cervical cancer. The features cover demographic information, habits, and historic medical records." 

Your Task
=====

1. Explore [the Cervical Cancer (Risk Factors) dataset](http://archive.ics.uci.edu/dataset/383/cervical+cancer+risk+factors) and 
2. Use the Python tools that you've learned so far to **develop a hypothesis about some likely risk factors** for a diagnosis of cervical cancer.  

Remember that there are several ways to approach this task; there is no one right answer! So have fun, and good luck!

### Stuck? 

If this practice problem was challenging, [here is a link to an example notebook](https://colab.research.google.com/github/arcus/education_modules/blob/main/python_practice/python_practice.ipynb) where we go through one possible solution to the practice problem. If you would like to download the notebook to your own computer, you can also do that by selecting "File" and then "Download" in Google Colab. 

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

If you are running this notebook in Google Colab, you may see a warning when you try to run the first code cell that begins "Warning: This notebook was not authored by Google." This is because the notebook is actually on GitHub, and authored by us! It's always a good idea to pause and reflect when you get warnings like this (especially when you are running code that you didn't write), but we assure you that it is safe to run the code in this notebook. 

</div>

We encourage you to spend some time playing around with the data before you look at the example! And remember, just because your solution doesn't look exactly like the example doesn't mean it's wrong-- there are a variety of ways you might have approached the task we gave you.  

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Feeling overwhelmed? Learning data science in Python takes time and practice. Don't worry if you feel like you have to go back and look at the modules over and over, or Google lots of things-- folks who do this for a living Google things every day! You don't have to memorize everything. Just keep your favorite resources close at hand so you remember what tools you have access to.

</div>

## Additional Resources

The best way to continue learning Python for data science is to **do data science with Python**! Here are some sources of publicly-available data that you can download and start practicing with today:

- [Kaggle.com](https://www.kaggle.com/) has a lot datasets to practice with, and even competitions and short courses! 
- [World Bank Data](https://data.worldbank.org/)-- this repository has many global development datasets
- [Data.gov](https://data.gov/)
- And so many more! Try searching "open" or "public" data and see what you can find!

A great way to keep resources close at hand is to use cheat sheets:

- [Python Cheatsheet](https://www.pythoncheatsheet.org/) is a great resource for the basics of base Python.
- [The pandas cheat sheet on pydata.org](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) is good to have available when you are using the pandas library-- a must for data science in Python!
- There is also a good [seaborn cheat sheet](https://images.datacamp.com/image/upload/v1676302629/Marketing/Blog/Seaborn_Cheat_Sheet.pdf) provided by DataCamp. 

## Feedback

@feedback




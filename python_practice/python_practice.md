<!--

author:   Meredith Lee
email:    leemc@chop.edu
version: 1.0.1
module_template_version: 3.0.0
language: en
narrator: UK English Female
title: Python Practice
comment: Use the basics of Python coding, data transformation, and data visualization to work with real data. 
long_description: When learning Python for data science, the ultimate goal is to be able to put all of the pieces together to analyze a dataset. This module aims to provide a data science task in order to help learners practice Python skills in a real-world context. 
estimated_time: 1 hour

@learning_objectives

After completion of this module, learners will be able to:

- Import a dataset from an online database
- Recode data and change variable types in a dataframe
- Use exploratory data visualization to identify trends in data and generate hypotheses

@end

@pre_reqs

Learners should be familiar with [the basics of Python coding](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_writing_python_code/python_basics_writing_python_code.md), including [data transformation with pandas](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/pandas_transform/pandas_transform.md) and [data visualization with matplotlib and seaborn](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/data_visualization_in_seaborn/data_visualization_in_seaborn.md). Learners should also have access to Python, either on their own computer or in the cloud. 

@end

good_first_module: false

coding_required: true
coding_language: Python
coding_level: practice exercise

sequence_name: Python

@sets_you_up_for

@end

@depends_on_knowledge_available_in

- demystifying_python
- python_basics_writing_python_code
- pandas_transform
- data_visualization_in_seaborn

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Python Practice

<div class = "overview">

## Overview
@comment

**Is this module right for me?:** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites:** Learners should be familiar with [the basics of Python coding](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_writing_python_code/python_basics_writing_python_code.md), including [data transformation with pandas](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/pandas_transform/pandas_transform.md) and [data visualization with matplotlib and seaborn](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/data_visualization_in_seaborn/data_visualization_in_seaborn.md). Learners should also have access to Python, either on their own computer or in the cloud. 

**Learning Objectives**:

@learning_objectives

</div>

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

For this practice module we will be using real, publicly-available cervical cancer data from [UC Irvine's machine learning data repository](http://archive.ics.uci.edu/ml/index.php); you can download those data here: [cervical cancer risk factors data](http://archive.ics.uci.edu/ml/machine-learning-databases/00383/risk_factors_cervical_cancer.csv). If you have done the [R Practice Module](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_practice/r_practice.md), this dataset might be familiar! 

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

The second link above will attempt to download a CSV file to your computer-- if you don't want to do that, or if your institution's permissions don't allow it, you can also access the dataset here: [https://archive.ics.uci.edu/ml/datasets/Cervical+cancer+%28Risk+Factors%29](https://archive.ics.uci.edu/ml/datasets/Cervical+cancer+%28Risk+Factors%29). If you want to download the CSV from there, just click the "Data Folder" link at the top of the page. 

</div>


## Practice Problem

According to the UCI Machine Learning database, the Cervical Cancer (Risk Factors) dataset "focuses on the prediction of indicators/diagnosis of cervical cancer. The features cover demographic information, habits, and historic medical records." 

Your Task
=====

1. Explore [the Cervical Cancer (Risk Factors) dataset](http://archive.ics.uci.edu/ml/machine-learning-databases/00383/risk_factors_cervical_cancer.csv) and 
2. Use the Python tools that you've learned so far to **develop a hypothesis about some likely risk factors** for a diagnosis of cervical cancer.  

Remember that there are several ways to approach this task; there is no one right answer! So have fun, and good luck!

### Stuck? 

If this practice problem was challenging, [here is a link to an example notebook](https://colab.research.google.com/github/arcus/education_modules/blob/main/python_practice/python_practice.ipynb) where we go through one possible solution to the practice problem. If you would like to download the notebook to your own computer, you can also do that by selecting "File" and then "Download" in Google Colab. 

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
- There is also a good [seaborn cheat sheet](http://datacamp-community-prod.s3.amazonaws.com/263130e2-2c92-4348-a356-9ed9b5034247) provided by DataCamp. 

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Python+Practice%22&version=1.0.1)!





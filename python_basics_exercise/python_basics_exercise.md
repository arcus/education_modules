<!--
module_id: python_basics_exercise
author:   Meredith Lee
email:    leemc@chop.edu
version:  1.0.2
current_version_description: Initial version. 
module_type: exercise
docs_version: 1.2.0
language: en
narrator: UK English Female
mode: Textbook

title: Python Basics: Exercise

comment: Practice the skills acquired in the Python Basics sequence by working through an exercise. 

long_description: Now that you've learned a bit about the basics of Python programming, it's time to try to put these concepts together! This module presents an exercise that can be solved using the skills you've learned in the Python Basics sequence (using [functions](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#5), [methods](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#6), [variables](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#9), [lists](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_lists_dictionaries/python_basics_lists_dictionaries.md#4), [dictionaries](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_lists_dictionaries/python_basics_lists_dictionaries.md#6), [loops](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_loops_conditionals/python_basics_loops_conditionals.md#4), and [conditional statements](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_loops_conditionals/python_basics_loops_conditionals.md#8)).

estimated_time_in_minutes: 30

@pre_reqs
Learners should be familiar with using functions, methods, variables, lists, dictionaries, loops, and conditional statements in Python. These skills are presented in the Python Basics sequence of modules ([Functions, Methods, and Variables](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#1), [Lists and Dictionaries](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_lists_dictionaries/python_basics_lists_dictionaries.md#1), and [Loops and Conditional Statements](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_loops_conditionals/python_basics_loops_conditionals.md#1)).
@end

@learning_objectives  
After completion of this module, learners will be able to:

- Run their own Python code, either on their own computer or in the cloud.
- Loop through a dictionary and conditionally perform an iterative task based on the values in the dictionary. 

@end
good_first_module: false
collection: learn_to_code
sequence_name: python_basics
previous_sequential_module: python_basics_loops_conditionals
coding_required: true
coding_level: basic
coding_language: python

@sets_you_up_for

@end

@depends_on_knowledge_available_in

- demystifying_python
- python_basics_variables_functions_methods
- python_basics_lists_dictionaries
- python_basics_loops_conditionals

@end
@version_history 

Previous versions: 
None.
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
-->

# Python Basics: Exercise

@overview

## Lesson Preparation

For this module, **you'll need access to Python, either on your own computer or in the cloud**. For details about how to download Python or use Google Colab (a cloud-based notebook environment), you can take a look at the ["Accessing Python" section of our Demystifying Python module](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_python/demystifying_python.md#9). 

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

For this exercise, you'll need all of the concepts covered in the Python Basics sequence of modules ([Functions, Methods, and Variables](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#1), [Lists and Dictionaries](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_lists_dictionaries/python_basics_lists_dictionaries.md#1), and [Loops and Conditional Statements](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_loops_conditionals/python_basics_loops_conditionals.md#1)). If you get stuck, feel free to go back and review! 

</div>

## Exercise

A teacher friend of yours can never remember what the grade ranges are for letter grades. They have requested that you write some code that will take their students' final scores and return the letter grades corresponding to those scores. After doing some research, you know that:

90-100 = "A"

80-89 = "B"

70-79 = "C"

60-69 = "D"

< 60 = "F"

Your friend also sends you the class's final grades, along with anonymous student identifiers:

st1: 88, st2: 78, st3: 34, st4: 97, st5: 64, st6: 89, st7: 56, st8: 83, st9: 92

Using a `for` loop and conditional (`if-else`) statements, can you write some code that returns a **dictionary** with the student identifiers as the **keys** and the letter grades that the students should be awarded as the **values**?

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

While we have looped through lists in a previous module, in this exercise we'll need to loop through a dictionary, which is similar but not exactly the same. To loop through the items (the keys and values) of a dictionary that we'll call `my_dict`, you can use the code `for k,v in my_dict.items()`.

</div>


To help get you started, here are the basic steps required to solve the problem:

1. Build a dictionary of student identifiers and their numerical grades.
2. Loop through the dictionary and assign a letter grade based on the value of the numerical grade.
3. Build a new dictionary of student identifiers and their *letter* grade.

If you do come up with a solution before looking at the answer, note that your code might look a little different; as long as you get the output you're looking for, that's okay!

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

If this process seems intimidating, that's understandable! Learning to code takes time, and there will be moments where things don't work. Things will come easier as you practice! And don't feel like failure if you have to Google how to do certain things over and over-- lots of people who write code for a living do the same thing!

</div>

### Stuck? 

If this practice exercise was challenging, [here is a link to an example notebook](https://colab.research.google.com/github/arcus/education_modules/blob/main/python_basics_exercise/python_basics_exercise.ipynb) where we go through one possible solution to the problem. If you would like to download the notebook to your own computer, you can also do that by selecting "File" and then "Download" in the Colab notebook.

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

The [Google Colab welcome page](https://colab.research.google.com/?utm_source=scs-index) doubles as a tutorial; if you'd like to explore a cloud-based Python notebook environment, that is a good place to start! 

</div>

We encourage you to spend some time trying to find a solution yourself before you look at the example! And remember, just because your solution doesn't look exactly like the example doesn't mean it's wrong-- there are a variety of ways you might have approached the task we gave you.  

## Additional Resources

- [W3 Schools has bite-sized explanations and examples of writing code in Python](https://www.w3schools.com/python/) if you want more clarity on how anything works

- A great way to keep resources close at hand is to use cheat sheets: [Python Cheatsheet](https://www.pythoncheatsheet.org/) is a great resource for the basics of base Python.


## Feedback

@feedback

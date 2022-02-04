<!--

author:   Meredith Lee
email:    leemc@chop.edu
version:  1.0.0
language: en
narrator: UK English Female
title: Introduction to Python
comment:  This module introduces the Python programming language, explores why Python is useful in research, and demonstrates how to write Python code in a Jupyter notebook (and why you might want to).
long_description: Python is a versatile programming language that is frequently used for data analysis, machine learning, web development, and more. If are interested in learning about any of these topics and are new to programming, are joining a team where Python is used, or have just heard about Python and are looking for a general introduction to the language, this module is a good place to start. This is appropriate for someone at the beginner level.

@learning_objectives  

After completion of this module, learners will be able to:

- Describe what Python is and why they might want to use it for research
- Recognize Python code
- Write text and simple code in a Jupyter notebook
- Download Python to their own computers

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script:   https://code.jquery.com/jquery-3.6.0.slim.min.js

@gifPreload
<script>
(function($) {

  // Get the .gif images from the "data-alt".
	var getGif = function() {
		var gif = [];
		$('img').each(function() {
			var data = $(this).data('alt');
			gif.push(data);
		});
		return gif;
	}

	var gif = getGif();

	// Preload all the gif images.
	var image = [];

	$.each(gif, function(index) {
		image[index]     = new Image();
		image[index].src = gif[index];
	});

	// Change the image to .gif when clicked and vice versa.
	$('figure').on('click', function() {

		var $this   = $(this),
				$index  = $this.index(),

				$img    = $this.children('img'),
				$imgSrc = $img.attr('src'),
				$imgAlt = $img.attr('data-alt'),
				$imgExt = $imgAlt.split('.');

		if($imgExt[1] === 'gif') {
			$img.attr('src', $img.data('alt')).attr('data-alt', $imgSrc);
		} else {
			$img.attr('src', $imgAlt).attr('data-alt', $img.data('alt'));
		}

		// Add play class to help with the styling.
		$this.toggleClass('play');

	});

})(jQuery);
</script>
@end
-->

# Introduction to Python

<div class = "overview">

## Overview

@comment

### Is this module right for me?

@long_description

### Details

**Estimated time to completion**: ~ 1 hr

**Pre-requisites**: Learners should be familiar with tabular data (data stored in a rectangular format, like an Excel spreadsheet or a comma separated file). It is helpful to have some familiarly with navigating to specific directories and running programs in the Command Line/Terminal. Learners do not need to have access to Python or Jupyter notebooks on their own computers.

**Learning Objectives**:

@learning_objectives

</div>

### Preparation

For the hands-on activity in this module, we will be using an online environment containing a Jupyter notebook. To load the environment, open the link below in a new tab:

<a href = "https://mybinder.org/v2/gh/arcus/education_modules/intro_to_python?labpath=intro_to_python%2Fnotebooks%2Fintro-to-python.ipynb" target = "_blank"> <img src = "https://mybinder.org/badge_logo.svg"></a> **← Click the "launch binder" button!**


The environment takes a few minutes to load, so be patient. Read through the next couple of sections while you wait! We won't need the online environment until the ["Using a Jupyter Notebook" section](#Using-a-Jupyter-Notebook).


## The Python Programming Language

While the word "python" might immediately make you think of a snake, that's not all it is! Python refers to a programming language. There are a lot of different programming languages that are used for a variety of tasks, but what they all have in common is that they tell your computer what to do. Behind all of your favorite applications is a software developer (or, more often, several developers) who have written the instructions for the computer in a programming language. Python is a particularly versatile language that can be used for web development, data science, machine learning, and more.

So why should you consider Python for your data analysis? There are a few reasons:

- Python is designed to be human-readable. Creating human-readable code is great for research because your analyses will be more reproducible (if you know exactly what you did, you can reproduce it) and transparent (writing the methods section of a paper is much easier when there is clear language about what was done and why).

- Python is **free** to download and use; it is also **open source**, meaning that updates and innovations can happen more quickly than with proprietary software.

- Because Python is quite popular and fairly mature, there are quite a lot of resources out there to help you get started learning, from free online tutorials and cheatsheets to semester-long courses and everything in between.

### Knowledge Check 1

What are some reasons to consider using Python for data analysis? Select all that apply.

[[X]] Python is free and open-source.
[[ ]] Python is simple point-and-click software.
[[X]] Python is human-readable.
[[X]] The Python community has lots of resources to help you get started.
***********************************************************************
<div class = "answer">

While Python is human-readable and free, it is not point-and-click software, and it can take some time and effort to learn how to write Python code. Don't worry, there are lots of resources out there to help you learn!

</div>
***********************************************************************

## Python Code

Python can be written in several ways. You can write Python code interactively using your computer's Terminal program or Command Line, you can write scripts that include Python code, or you can create Python notebooks using [Jupyter](https://jupyter.org/) or [Google Colaboratory](https://colab.research.google.com/?utm_source=scs-index) (or "Colab" for short). In most cases, you'll need to start with downloading Python to your computer (the exception will be if you are using cloud-based solutions like Google Colab). Which you choose will come down to personal preference and your specific goals.

If you have Python installed on your computer, you can use your computer's Command Line or Terminal program to write Python code interactively using a Python **interpreter** by typing `python3`:

<div style="display:none">@gifPreload</div>

<figure>
  <img src="https://github.com/arcus/education_modules/blob/intro_to_python/intro_to_python/media/python_interactive.png?raw=true" height="500" width="800" alt="An example of Python code in the Terminal with the code 7 + 8, print('Hello World!'), and list(range(0,10))." data-alt="https://github.com/arcus/education_modules/blob/intro_to_python/intro_to_python/media/python_interactive.gif?raw=true">

<figcaption>Click on the image to play the demo.</figcaption>
</figure>

Using Python interactively in the terminal can be useful if you want to quickly test out short pieces of code. Most of the time, though, you'll either be creating Python scripts or using a notebook instead.

## Python Scripts

Instead of writing instructions one at a time, for more complex tasks you might want to write a Python **script**, a series of instructions that you can write out ahead of time and then run in order with one command. Scripts are often written using special text editors that are designed for writing code (such as Atom or Sublime) or full-featured integrated development environments, or IDEs for short (IDEs, such as PyCharm or Spyder, have more debugging and automation capabilities than text editors).

Here is a short script written in the Spyder IDE:
<div style = "margin: 1rem; width: 750;">
![An example of Python code written in Spyder with the code name=input("What is your name?") and print("Welcome to Intro to Python, "+name+"!").](media/python_in_spyder.png?raw=true)
</div>

In the above example, our script asks for input of a user's name using the `input()` function, stores that input in a variable we've called `name`, and prints out a welcome message to the screen that includes the name the user entered using the code `print("Welcome to Intro to Python, "+name+"!")`.

In the script above you can also see lines of text marked with a pound sign `#` at the beginning. The pound sign marks a **comment**, which is anything you write in a script that you don't want to run as code. Comments are a good way to briefly describe or explain aspects of your script, and can also be used to "hide" lines of code as you experiment (an alternative to deleting code that you may want to add back later).

The Spyder IDE has a console where you can see the output of your script without having to run it in the Command Prompt/Terminal. As you can see in the screenshot below, all we had to do was create the file one time and then run that file instead of typing in the code interactively. This can save you time and effort if you have a task you know you'll want to perform repeatedly. In the Spyder IDE there is a "run" button (a green arrow in menu at the top) but you could also run the same file in your Terminal/Command Line by typing the command `python` followed by the file name of your Python script.

<div style="display:none">@gifPreload</div>

<figure>
  <img src="https://github.com/arcus/education_modules/blob/intro_to_python/intro_to_python/media/python_spyder_console.png?raw=true" height="500" width="800" alt="Running a Python script in Spyder, showing a user typing 'Pythonista' in response to the prompt and showing the output 'Welcome to Intro to Python, Pythonista!'" data-alt="https://github.com/arcus/education_modules/blob/intro_to_python/intro_to_python/media/python_spyder_console.gif?raw=true">

<figcaption>Click on the image to play the demo.</figcaption>
</figure>

In this case, when you run the code we wrote before in the Spyder console, you'll be asked for an input value (I've supplied the name "Pythonista"). If you hit "Enter", the output of the second line of code will appear: `Welcome to Intro to Python, Pythonista!`.

When you save a Python script, you'll use the file extension .py, and so to run the script in the example above, you would navigate to the correct directory in the Terminal (the folder where you've saved your file) and type `python intro-to-python.py`. If you are in the right place, you should see the output of your code!

## Jupyter Notebooks

If you are interested in using Python for data analysis, you might want to write Python in a [Jupyter notebook](https://jupyter.org/) (which was previously called an IPython notebook). There are a couple of reasons why you should consider using Jupyter notebooks:

- Notebooks provide the best of both worlds between interactive and scripted code: code is written in chunks that can be run individually, with any output displayed beneath the code chunk.

- You can intersperse sections of text, written in Markdown language, that can provide explanations and context for your code. This is especially valuable for data analysis, similar to a scientific notebook.

Interested in learning how to write Python code in a Jupyter notebook? Continue on to the next section for a hands-on activity! You won't need to download anything to your computer.


## Using a Jupyter Notebook

This is a hands-on activity! Feel free to pop over to that tab you opened in the [Preparation section](#Preparation) to get started. Need the link again? Here it is:

<a href = "https://mybinder.org/v2/gh/arcus/education_modules/intro_to_python?labpath=intro_to_python%2Fnotebooks%2Fintro-to-python.ipynb" target = "_blank"> <img src = "https://mybinder.org/badge_logo.svg"></a> **← Click the "launch binder" button!**

### Knowledge Check 2

Which of the following is **not** an example of Python code?

[( )] `print("Python is the best!")`
[(X)] `print Hello World!`
[( )] `list(range(1, 100))`
[( )] `height = input("How tall are you?")`
***********************************************************************

<div class = "answer">

Python uses functions that contain instructions that tell the computer what it is supposed to do, and these functions are the name of the function followed by the **arguments** in parentheses. Arguments are information that the person writing the code (you!) provide to tell the function what data to perform its task on and more specificity on how exactly to perform the task. `print()`, `list()`, `range()`, and `input()` are just a few of Python's built-in functions! [You can read more about Python's built-in functions here](https://docs.python.org/3/library/functions.html).

</div>
***********************************************************************


### Knowledge Check 3

What are the components of a Jupyter notebook? Select all that apply.

[[X]] Code cells
[[X]] Text cells written in Markdown
[[ ]] A console where you can write lines of code interactively
***********************************************************************

<div class = "answer">

Jupyter notebooks contain code cells and text cells. The code cells are written in Python and can contain as much or as little code as you want; the output of the code can be displayed directly beneath the code cell and the code can be edited and re-run at any time. The text cells are written in Markdown language and can provide more context and reasoning than can easily be done using comments. Additionally, using Markdown allows you to add useful formatting to your text. Jupyter notebooks do not have console, but since you can run each code cell independently, you don't really need one!

</div>
***********************************************************************


## Next Steps

Are you interested in learning more about Python, or even starting to work with it? Here are some tips for what you might want to do next!

Installing Python On Your Own Computer
=======

Your computer most likely will not have Python already installed. To check, you can open your Command Line/Terminal and type `python --version`. The version you have will be displayed if you have Python installed. If you don't, you can [visit python.org to download the latest version](https://www.python.org/downloads/).

Alternatively, you can [install Python using Anaconda](https://www.anaconda.com/products/individual), a toolkit that gives you not only Python itself but also many other data science tools to help with coding, analysis, and visualization. The individual version of Anaconda is also free to download!

Once you've downloaded Anaconda, you can open the Anaconda Navigator; when you do, you'll see the the window below. Now you have access to lots of tools for working with Python!
<div style = "margin: 1rem; width: 750;">
![Anaconda Navigator interface.](media/anaconda.png?raw=true)
</div>

### Knowledge Check 4

How can you access Python to begin practicing on your own?

[( )] By downloading the latest version at https://www.python.org/downloads/
[( )] By downloading the latest Anaconda distribution
[( )] By using cloud-based tools, such as Google Colab
[(X)] All of the above
***********************************************************************

<div class = "answer">

You can download Python directly to your computer, use Anaconda to download Python as well as many other data science tools, or use cloud-based notebooks like Google Colab. The choice is yours!

</div>
***********************************************************************

### Additional Resources

For a beginner-friendly walk-through of writing Python scripts, [Hello World! Your Very First Computer Program](https://youtu.be/cV-QwT4fV7M) delivered by Jeff Pennington is an excellent introduction if you've got an hour to spend.

[python.org](https://www.python.org/) is a great resource for documentation, FAQ's, and tutorials for beginners, as well as information about what is happening in the wider Python community. Check it out and explore!

If you're curious about using Python in the cloud, check out this [short article about cloud tools for programming](https://education.arcus.chop.edu/r-python-cloud/) that includes an example of a notebook written in Google Colab.

## Feedback

*5 minute survey*

At the beginning of this module we described the following goals:

**Learning Objectives**:

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for [filling out our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Intro+to+Python%22)!

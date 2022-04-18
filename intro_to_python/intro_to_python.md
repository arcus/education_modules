<!--

author:   Meredith Lee
email:    leemc@chop.edu
version:  1.1.0
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Introduction to Python
comment:  This module introduces the Python programming language, explores why Python is useful in research, and demonstrates how to write Python code in a Jupyter notebook (and why you might want to).
long_description: Python is a versatile programming language that is frequently used for data analysis, machine learning, web development, and more. If you are interested in learning about any of these topics and are new to programming, are joining a team where Python is used, or have just heard about Python and are looking for a general introduction to the language, this module is a good place to start. This is appropriate for someone at the beginner level.
estimated_time: 1 hr
@learning_objectives  

After completion of this module, learners will be able to:

- Describe what Python is and why they might want to use it for research
- Recognize Python code
- Describe the components of a Jupyter notebook
- Write text and simple code in a Jupyter notebook
- Download Python to their own computers

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script:  https://kit.fontawesome.com/83b2343bd4.js

script:  https://code.jquery.com/jquery-3.6.0.slim.min.js

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

**Estimated time to completion**: @estimated_time

**Pre-requisites**: Learners should be familiar with tabular data (data stored in a rectangular format, like an Excel spreadsheet or a comma separated file). It is helpful to have some familiarity with navigating to specific directories and running programs in the Command Line/Terminal. Learners do not need to have access to Python or Jupyter notebooks on their own computers.

**Learning Objectives**:

@learning_objectives

</div>

## Lesson Preparation

For the hands-on activity in this module, we will be using an online environment containing a Jupyter notebook. To load the environment, open the link below in a new tab:

<div class = "important">
Please read over both options before you start performing any actions, to make sure you pick the right option for you.
</div>

Option 1: Work in the Cloud
=======

This might work well for you if you either can't or don't want to install Python and Jupyter on your computer, or are not familiar with working with directories or Github. The benefit is that you don't have to install anything, but one negative is that this option requires a bit of waiting for your environment to come online.

**First**, we need to create a small container in the cloud for you to work in just using your web browser.  **Click "Launch binder" below.**  It might take a couple of minutes to create, depending on how recently it was created (when it's being used more, it's quicker!).

<a href = "https://mybinder.org/v2/gh/arcus/education_modules/update-intro-to-python?labpath=intro_to_python%2Fnotebooks%2Fintro-to-python.ipynb" target = "_blank"> <img src = "https://mybinder.org/static/images/badge_logo.svg" alt="Launch binder."></a> **← Click the "launch binder" button!**

<div class = "hint" style = "align-items: center; display: flex;">

<div style = "margin: 1rem; max-width: 45%; float:left;"> If you're the first person to fire up this environment in a while, you might see this loading screen for a few minutes.  Be patient!</div>
<div style = "margin: 1rem auto; max-width: 45%; float:left;"> ![Binder loading screen.](media/binder_loading.gif)<!--
style = "border: 1px solid rgb(var(--color-highlight));"-->
</div>
</div>

Option 2: Work on Your Computer
=======

If you have [Python](https://www.python.org/) and [Jupyter](https://jupyter.org/) installed already on your local computer, and have some familiarity working with file directories or Github, you might be interested in simply downloading our sample code to your computer. If you haven't downloaded Python or Jupyter to your computer but would like to, you'll learn how in the [Next Steps](#next-steps) section of this module. Then you can come back here when you're done and follow these steps to download the code (If you already completed this work for a previous module, and it's been a while since you downloaded this project to your computer, you may want to get any new and improved files that have been placed there in the meantime):

* Go to the [GitHub repository](https://github.com/arcus/education_modules) where the materials for this lesson are located.
* You can use Git to **clone**, or download, a repository (or "repo", as it is sometimes called). Here are the steps to follow:

  * It is likely that Git is already installed on your computer, even if you've never used it before. Open the Terminal application (if you're using a Mac/Linux machine) or the Windows Powershell (if you're using Windows 10 or later -- here is [more information about finding the Windows Powershell](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_scripting_101/bash_scripting_101.md#5). Then run the code `git --version`. If Git is installed, you should see a version number. If not, check out [these instructions for installing git on Mac or PC](https://carpentries.github.io/workshop-template/#git).

  * You can also use GitHub Desktop, which you can use to interact with GitHub repositories. The [GitHub Desktop documentation](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/overview/getting-started-with-github-desktop) for download instructions and getting started.
  * If you are using Git in a command line interface, go to the [education_modules repository on GitHub.com](https://github.com/arcus/education_modules) and then follow [these instructions to clone the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository).

  <div class = "important">
  It's often useful to have a folder called `GitHub` on your computer for storing repositories that you clone. To navigate to a specific directory in the command line, use the `cd` command (check out the [Command Line 101 module](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_scripting_101/bash_scripting_101.md#1) for more information).
  </div>

  * If you are using GitHub desktop, follow [these instructions for cloning a repository from GitHub to GitHub Desktop](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop).

<div class = "options">
If you don't want to wait for the binder environment to load, but don't want to use git to clone the repository, you can also view the [rendered Jupyter notebook on GitHub](https://github.com/arcus/education_modules/blob/main/intro_to_python/notebooks/intro-to-python.ipynb). You will not be able to interact with the code, but if you have Jupyter installed you can copy and paste the code into code cells that you create in your own notebook.
</div>


## The Python Programming Language

While the word "python" might immediately make you think of a snake, that's not all it is! Python refers to a programming language. There are a lot of different programming languages that are used for a variety of tasks, but what they all have in common is that they tell your computer what to do. Behind all of your favorite applications is a software developer (or, more often, several developers) who have written the instructions for the computer in a programming language. Python is a particularly versatile language that can be used for web development, data science, machine learning, and more.

So why should you consider Python for your data analysis? There are a few reasons:

- Python is designed to be human-readable. Creating human-readable code is great for research because your analyses will be more reproducible (if you know exactly what you did, you can reproduce it) and transparent (writing the methods section of a paper is much easier when there is clear language about what was done and why).

- Python is **free** to download and use; it is also **open source**, meaning that updates and innovations can happen more quickly than with proprietary software.

- Because Python is quite popular and fairly mature, there are quite a lot of resources out there to help you get started learning, from free online tutorials and cheatsheets to semester-long courses and everything in between.

### Quiz: The Python Programming Language

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
  <img src="https://github.com/arcus/education_modules/blob/main/intro_to_python/media/python_interactive.png?raw=true" height="500" width="800" alt="An example of Python code in the Terminal with the code 7 + 8, print('Hello World!'), and list(range(0,10))." data-alt="https://github.com/arcus/education_modules/blob/main/intro_to_python/media/python_interactive.gif?raw=true">

<figcaption>Click on the image to play the demo.</figcaption>
</figure>

To exit the Python interpreter, type the command `exit()` and then press the Enter key. Alternatively, you can also close the interpreter window.

Using Python interactively in the terminal can be useful if you want to quickly test out short pieces of code. Most of the time, though, you'll either be creating Python scripts or using a notebook instead.

## Python Scripts

Instead of writing instructions one at a time, for more complex tasks you might want to write a Python **script**, a series of instructions that you can write out ahead of time and then run in order with one command. Scripts are often written using special text editors that are designed for writing code (such as Atom or Sublime) or full-featured integrated development environments, or IDEs for short (IDEs, such as PyCharm or Spyder, have more debugging and automation capabilities than text editors).

Here is a short script written in the Spyder IDE:
<div style = "margin: 1rem; width: 750;">
![Python code.](media/python_in_spyder.png?raw=true)
</div>

In the above example, our script asks for input of a user's name using the `input()` function, stores that input in a variable we've called `name`, and prints out a welcome message to the screen that includes the name the user entered using the code `print("Welcome to Intro to Python, "+name+"!")`.

In the script above you can also see lines of text marked with a pound sign `#` at the beginning. The pound sign marks a **comment**, which is anything you write in a script that you don't want to run as code. Comments are a good way to briefly describe or explain aspects of your script, and can also be used to "hide" lines of code as you experiment (an alternative to deleting code that you may want to add back later).

The Spyder IDE has a console where you can see the output of your script without having to run it in the Command Prompt/Terminal. As you can see in the screenshot below, all we had to do was create the file one time and then run that file instead of typing in the code interactively. This can save you time and effort if you have a task you know you'll want to perform repeatedly. In the Spyder IDE there is a "run" button (a green arrow in menu at the top) but you could also run the same file in your Terminal/Command Line by typing the command `python` followed by the file name of your Python script.

<div style="display:none">@gifPreload</div>

<figure>
  <img src="https://github.com/arcus/education_modules/blob/main/intro_to_python/media/python_spyder_console.png?raw=true" height="500" width="800" alt="Running a Python script in Spyder, showing a user typing 'Pythonista' in response to the prompt and showing the output 'Welcome to Intro to Python, Pythonista!'" data-alt="https://github.com/arcus/education_modules/blob/main/intro_to_python/media/python_spyder_console.gif?raw=true">

<figcaption>Click on the image to play the demo.</figcaption>
</figure>

In this case, when you run the code we wrote before in the Spyder console, you'll be asked for an input value (I've supplied the name "Pythonista"). If you hit "Enter", the output of the second line of code will appear: `Welcome to Intro to Python, Pythonista!`.

When you save a Python script, you'll use the file extension .py, and so to run the script in the example above, you would navigate to the correct directory in the Terminal (the folder where you've saved your file) and type `python intro-to-python.py`. If you are in the right place, you should see the output of your code!

### Quiz: Python Code

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

## Jupyter Notebooks

If you are interested in using Python for data analysis, you might want to write Python in a [Jupyter notebook](https://jupyter.org/) (which was previously called an IPython notebook). There are a couple of reasons why you should consider using Jupyter notebooks:

- Notebooks provide the best of both worlds between interactive and scripted code: code is written in chunks that can be run individually, with any output displayed beneath the code chunk.

- You can intersperse sections of text, written in Markdown language, that can provide explanations and context for your code. This is especially valuable for data analysis, similar to a scientific notebook.

Interested in learning how to write Python code in a Jupyter notebook? Continue on to the next section for a hands-on activity! You won't need to download anything to your computer.

### Quiz: Jupyter Notebooks

What are the components of a Jupyter notebook? Select all that apply.

[[X]] Code cells
[[X]] Text cells written in Markdown
[[ ]] A console where you can write lines of code interactively
***********************************************************************
<div class = "answer">
Jupyter notebooks contain code cells and text cells. The code cells are written in Python and can contain as much or as little code as you want; the output of the code can be displayed directly beneath the code cell and the code can be edited and re-run at any time. The text cells are written in Markdown language and can provide more context and reasoning than can easily be done using comments. Additionally, using Markdown allows you to add useful formatting to your text. Jupyter notebooks do not have console, but since you can run each code cell independently, you don't really need one!
</div>
***********************************************************************


## Hands-On Activity

This is a hands-on activity! Feel free to pop over to that tab you opened in the [Lesson Preparation section](#Lesson-Preparation) to get started. Need the link again? Here it is:

<a href = "https://mybinder.org/v2/gh/arcus/education_modules/update-intro-to-python?labpath=intro_to_python%2Fnotebooks%2Fintro-to-python.ipynb" target = "_blank"> <img src = "https://mybinder.org/static/images/badge_logo.svg" alt="Launch binder."></a> **← Click the "launch binder" button!**

Don't forget to come back here when you're done!

### Quiz: Hands-On Activity

Which of the following methods adds an element to a list in a specific position?

[( )] `.extend()`
[( )] `.pop()`
[( )] `.append()`
[(X)] `.insert()`
***********************************************************************
<div class = "answer">
While all of the answers given are list methods, `.extend()` adds the elements of one list to the end of another list, `.append()` adds an element to the end of a list, and `.pop()` removes a element from a specific position in a list (and returns that element).
</div>
***********************************************************************

Let's say that we have the following dictionary:

```python3
covid_testing = {"id" : 01010101,
                 "date" : "04/11/2020"
                 "age" : 28,
                 "type" : "pcr"}
```
How would you add an entry called `result` that has the value `negative` to this dictionary?

[[covid_testing["result"] = "negative"]]
[[?]] Hint: Capitalization matters in Python, so make sure you type the key and value exactly as they appear above!
***********************************************************************
<div class = "answer">
Adding a item to a dictionary is a matter of adding a key (in this case "result") and then assigning it a value (such as "negative"). The quotation marks are required because both the and value are strings.
</div>
***********************************************************************

## Next Steps

Are you interested in learning more about Python, or even starting to work with it? Here are some tips for what you might want to do next!

Installing Python On Your Own Computer
=======

Your computer most likely will **not** have Python already installed. To check, you can open your Command Line/Terminal and type `python --version`. The version you have will be displayed if you have Python installed. If Python is not installed, you have a few options:

* You can [install Python using Anaconda](https://www.anaconda.com/products/individual) (recommended), a toolkit that gives you not only Python itself but also many other data science tools to help with coding, analysis, and visualization. The individual version of Anaconda is also free to download!

  Once you've downloaded Anaconda, you can open the Anaconda Navigator; when you do, you'll see the the window below. Now you have access to lots of tools for working with Python!
  <div style = "margin: 1rem; width: 750;">
  ![Anaconda Navigator interface.](media/anaconda.png?raw=true)
  </div>

* You can also download [just the latest version of Python directly at python.org](https://www.python.org/downloads/). If you also want Jupyter or any IDEs, you will need to download those separately as well. [You can install Jupyter here](https://jupyter.org/install) and [here is a list of IDEs where you can write Python code](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments).

  <div class = "help">
  That list of IDEs might seem a bit intimidating! Let's narrow things down to a few good options. If you don't know where to start, [Thonney](https://thonny.org/) is a good option for beginners, and actually comes with Python built in. [Spyder](https://www.spyder-ide.org/) was designed for scientific programming, and is a popular option for data scientists and analysts. [PyCharm](https://www.jetbrains.com/pycharm/) is popular with professional developers and has many features that other IDEs lack, but may come with a steeper learning curve. Both Spyder and PyCharm come with the Anaconda distribution.
  </div>

Using Python in the Cloud
=======

If you don't want to download Python and would instead prefer to continue practicing in the cloud, [Google Colaboratory](https://colab.research.google.com/), or Google Colab, provides an online Jupyter notebook environment that is completely free (though you do need a Google account). The introduction is actually written as a Colab notebook itself, so you can jump right in practicing. While it won't look exactly like the Jupyter notebook we used for this module, it will be a very similar experience, with a mix of code cells and text cells written in Markdown.

You can even see what this module's notebook looks like in Google Colab! Once you've worked through the introduction above:

1. Click "File" in the upper left-hand corner and then "Open notebook" in the drop-down menu:

   ![Opening a notebook in Google Colab](media/google_colab_open_nb.png)

 2. In the window that appears, one of the options at the top is **GitHub**. Click that, and you'll see where you can type in a GitHub URL.
 3. In that space, copy and paste the repository where these modules live: [https://github.com/arcus/education_modules](https://github.com/arcus/education_modules).
 4. Click the magnifying glass to the far right. You should see a list of the Python notebooks in that repository.
 5. When you find the one you want, the button on the far right (an upward-slanting arrow in a box) will open the notebook file as a Colab notebook in another tab.

   <div style="display:none">@gifPreload</div>

   <figure>
     <img src="https://github.com/arcus/education_modules/blob/update-intro-to-python/intro_to_python/media/github_repo_colab.png?raw=true" height="500" width="800" alt="Finding a GitHub repository in Google Colab" data-alt="https://github.com/arcus/education_modules/blob/update-intro-to-python/intro_to_python/media/github_repo_colab.gif?raw=true">

   <figcaption>Click on the image to play the demo.</figcaption>
   </figure>

### Quiz: Next Steps

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

## Additional Resources

* For a beginner-friendly walk-through of writing Python scripts, [Hello World! Your Very First Computer Program](https://youtu.be/cV-QwT4fV7M) delivered by Jeff Pennington is an excellent introduction if you've got an hour to spend.

* [python.org](https://www.python.org/) is a great resource for documentation, FAQ's, and tutorials for beginners, as well as information about what is happening in the wider Python community. Check it out and explore!

* If you're interested in practicing more with Google Colab, check out [this notebook looking at statistics](https://colab.research.google.com/drive/1zkW5Y0SoV3gMU6sQtlgnZsfR2GIXi6F_?usp=sharing).

## Feedback

*5 minute survey*

At the beginning of this module we described the following goals:

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for [filling out our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Intro+to+Python%22)!

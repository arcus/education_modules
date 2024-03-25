<!--
module_id: git_cli_vs_gui
author:   Joy Payton
email:    paytonk@chop.edu
version:  1.0.0
current_version_description: Initial version
module_type: standard
docs_version: 4.0.0
language: en
narrator: US English Female
mode: Textbook
title: Git Command Line Interface versus Graphical User Interface
comment:  Compare the two ways of interacting with Git to decide which is best for you.
long_description: There are two ways of using Git: (1) typing commands on a command line interface (CLI) or (2) clicking through options on a graphical user interface (GUI) software. This module will compare and contrast these two options to help you decide how to use Git in your work.
estimated_time_in_minutes: 30

@pre_reqs
Learners should know what version control is and why it's important and should also understand what a command line interface is and how that's different from a graphical user interface.  

To acquire basic knowledge of version control, we recommend our [Introduction to Version Control](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/git_intro/git_intro.md#1) module. 

To acquire basic knowledge about command line interfaces, we recommend our [Demystifying the Command Line Interface](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_command_line/demystifying_command_line.md#1) module.  

No previous experience with git is required.
@end

@learning_objectives  
After completion of this module, learners will be able to:

- List an advantage and a disadvantage of using Git via a **graphical user interface**
- List an advantage and a disadvantage of using Git via a **command line interface**
- Name one major Git graphical user interface 

@end

good_first_module: false
data_task: data_management
collection: infrastructure_and_technology
coding_required: false
sequence_name: git_basics
previous_sequential_module: git_intro

@sets_you_up_for

- git_setup_mac_and_linux
- git_setup_windows


@end

@depends_on_knowledge_available_in

- git_intro
- demystifying_command_line

@end

@version_history 
Previous versions: 

No previous versions.

@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
-->

# Git Command Line Interface versus Graphical User Interface

@overview

## What is Git?

You may already know what Git is and even use it for version control, but let's review.  We'll take on some of the text that Git uses to describe itself in its official website:

[![The official git website, which states: "Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. Git is easy to learn and has a tiny footprint with lightning fast performance. It outclasses SCM tools like Subversion, CVS, Perforce, and ClearCase with features like cheap local branching, convenient staging areas, and multiple workflows."](media/git_scm_com.png)](https://git-scm.com)

Git describes itself as a **distributed**, **open source** **version control** system. Let's talk about each of those terms:

* Version Control 
* Distributed
* Open Source

Version Control
------

Version control is a way to track changes to files.  In version control, we want to track what changed in a set of one or more interrelated files. 

Not only do we want to track what changed (e.g. a file got deleted or a line of code got changed), but we also want to track when the change was made, who changed it, and the reason the person made the change.

We also want to be able to go back to older versions of these files to rescue anything that we decide we need to bring back after changes or deletions.

If the idea of version control is very new to you, you might be interested in the brief [Introduction to Version Control](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/git_intro/git_intro.md#1) module.

Distributed
---------

Git is **distributed** because Git **repositories** (sets of files you're managing using git) can be stored in many kinds of places. The term *distributed* here is the opposite of *centralized*. 

You don't have to log in to a centralized server at your workplace in order to use Git.  This was novel when Git was created. Older version control systems relied on users checking files in and out of a centralized system that was on a dedicated server.  That meant that if you were away from work, you couldn't use version control.  

In contrast, Git can run on your local computer, on the cloud, in a website, on a server -- in lots of different places according to what's most useful for how you like to work.  Not connected to the internet?  No problem, you can still track changes in your local Git repository that's stored on your laptop.  

In fact, you can have multiple different copies of the same repository, if that's helpful.  For example, every member of your team can have their own copy of a repository that they synchronize with a canonical or official copy that's on a website they can all get to.

Open Source
-----

Git is **FOSS**, or **free and open source software**.  This means that git is "free" in two ways -- in the meaning of having **no cost** and also in that can be used widely **without intellectual property concerns or licensing restrictions**. 

This is important because it means that people around the world use Git.  Students use it, individuals use it, large companies use it, people in highly-resourced projects use it, and people on a shoestring budget use it. 

## Interfaces

You can use Git in two main ways:

* Using a **command line interface**, or **CLI**
* Using **graphical user interface**, or **GUI**

First, a quick review of terms. An **interface** is a way of interacting with a system.  Interfaces can provide **controls**, ways for the user to do something (like change gears, turn on the radio, or close elevator doors), and they can provide **information** (like the current floor, the engine temperature, and the current velocity).  Many interfaces do both -- they provide information and they provide controls.  

A **graphical user interface**, or **GUI** (pronounced "gooey") is an interface that is highly visual and relies on graphics (shapes, images, icons, windows, and other kinds of visual cues), which for many users is helpful.  Usually, some degree of point-and-click and the use of a mouse is involved in the use of a GUI.

A **command line interface**, or **CLI** (you just say the letters, C - L - I), is an interface that depends on typed commands in a program that gives users the ability to give commands directly to the computer system.

In some cases, you have a choice of which interface you want to use to interact with a system.  Git is an example. You can use the CLI or a GUI to work with Git.  

## Graphical User Interfaces and Git

Many people find that GUIs are easier to use.  You don't have to remember a typed command, you can use a visual menu that you select from.  This means you can accomplish a lot without having to memorize a long list of commands.  Additionally, a visual display with rich graphics can pack a lot of information into a single screen, using colors, icons, lines, shapes, text formatting, and more.  A Git graphical user interface can show the same amount of information about a Git repository that would take several screens and a bit of reading to get across in a text-only, command line interface.

With Git, there are many graphical user interfaces available, made by various different companies.  Often, the people who make graphical user interfaces spend a lot of time figuring out the most frequent tasks people want to do, and they design the GUI to make those as easy as possible to do. Some popular Git GUIs (which are also called Git **clients** or **client software**) include:

* The Git GUI that's included in RStudio
* GitKraken
* The source control GUI that's included in VSCode
* SourceTree
* GitHub Desktop
* and many more!

Some of these are free, some are free and open source, and some have a cost (either for everyone, or with a "freemium" model that has a free tier).  Which is the best GUI for Git?  We'd argue that the best Git GUI is the one that your team uses and you'll have friendly support around.  

## Command Line Interface and Git

Many people find that using the command line interface for Git gives them more fine-grained control over their projects.  Also, if you have experience working in the command line, you may be faster and more comfortable using typed commands rather than learning the particular design of a Git GUI.  The Git commands used in a CLI are part of the core Git software, which means you don't have to pay for them, as you might with some GUI software.  Finally, if you're working on a computer system that doesn't use a graphical interface (for example, a Linux server that doesn't use a GUI or desktop), you'll still be able to use Git in the command line.

To use Git in a CLI, you will use a number of commands that start with the word `git`.  For example, you might type `git status` to understand what branch you have checked out and if there are any untracked files to be aware of, or `git commit -m "My useful commit message"` to make a commit with a message you specify that gives more information about that commit.

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

We just threw some Git jargon at you: **branch**, **commit**, **checkout**, **tracked**.  Don't worry if you don't know what these mean.  The important thing we want you to be aware of is what these commands look like when you're using Git in a CLI.

</div>

## Which is Better? 

Which is better when you use Git?  Graphical user interfaces, or a command line interface? It depends!  In the next section, we'll do some direct compare and contrast so you can get an idea of what the two approaches might look like in actual day to day work.  

Generally speaking, for everyday work in Git, you can choose whichever approach appeals to you more, so we'll present both the command line interface as well as a graphical user interface to allow you to see both. However, it's important to note that whichever interface you choose for daily work, you **might end up needing to use a command line interface for complex, out of the ordinary work** in Git.  Let's talk a bit about why this is the case.

Git has lots of features, and designers can't include every possible command in an easy-to-use point and click GUI.  That means some things you may need to do in Git can **only** be done by using the command line, because they're so niche and specific to certain circumstances that graphical software simply hasn't included that task.  Still, there's a good chance that you might end up using a Git GUI for **years** before you run across a situation that requires the command line. 

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

If you have to do something very specific in Git that isn't an everyday activity, you might **have** to use a command line interface to accomplish this.  That's a good reason to get at least a little bit comfortable with using Git on the command line.

However, for most people, your day-to-day work in Git can be done in **either** the command line interface or a graphical interface.

</div>

Let's compare and contrast some things you might need to do in Git, and see how they look different in the two interfaces.  Don't worry if you're not sure what these tasks mean, but just take a look at how the two interfaces look.  Do you prefer one over the other?  We'll look at three different tasks: adding a new repository, looking at the history of a repository, and looking at a specific change more closely.


### Adding a new repository

First, let's create a new repository in an existing directory.  What this means is that we have a directory (folder) of files on our computer, and we realize that we'd like to add version control to this folder.  In our example case, we have a directory called `my_important_directory`, and it is located within the `Documents` folder in a local laptop.

Command Line Interface
----

In a command line, you'd need to navigate to that directory (in the image below, in a MacOS Terminal, this is done using `cd`, which means "change directory"), and type `git init`.

![Terminal window which shows the command `cd my_important_directory` followed by the command `git init`.  The output of the second command reads "Initialized empty Git repository in /Users/paytonk/Documents/my_important_directory/.git/".](media/git_init.png)

Graphical User Interface
-----

In a GUI (here, GitHub Desktop), we have to put in the name of the repository, which is the name of the folder, as well as the name of the parent directory (`Documents`).

**Want to watch this process?  Click on the image below to play an animated gif.  It will continue to loop and you can re-start it by clicking again.**

<div style="display:none">

@gifPreload

</div>

<figure>

  <img src="https://github.com/arcus/education_modules/blob/main/git_cli_vs_gui/media/git_init_gui.png?raw=true" height="756" width="540" alt="Adding a new repository using the GitHub Desktop graphical user interface" data-alt="https://github.com/arcus/education_modules/blob/main/git_cli_vs_gui/media/git_init_gui.gif?raw=true" style = "border: 1px solid rgb(var(--color-highlight));">

<figcaption style = "font-size: 1em;">

Click on the image to play the demo of the above steps!

</figcaption>

</figure>

### Looking at the History of a Project 

Git provides a way to look at a history of changes.  Each time you decide to make a save of the files as a moment in time you'd like to memorialize, you make a **commit**.  The commit history shows who made a change, when they made it, and a message they write to describe the change.

Command Line Interface
----

In the command line, you can use `git log` to show the commit history.  This is a real commit history on a Git repository that holds materials for a workshop on the R language.  Below, you can see that there are six commits, and each commit has some information about who made the commit and a message describing the change made in that commit.

![Terminal window with the command "git log".  The output includes six commit records.  Each record has a commit code made up of letters and numbers, an author name and email address, a date and time stamp, and a short message such as "add presenter and TA pics".](media/git_log_cli.png)

Graphical User Interface
-----

You can use the **history** function of a Git GUI to look at the same information.  Here, we're looking at the same repository, using GitHub Desktop.  On the left side of the window, you can see the same six commits we saw above, but in a prettier format.  There's additional information here on the right side of the screen, too, which we'll explain in a bit.

![GitHub Desktop window shows, in the left side of the window, a history of six commits, each of which has a user name, date, small icon of the user, and short message such as "add presenter and TA pics."  Additionally, the actual changes made during one of the commits are shown on the right of the window. ](media/git_history_gui.png)

### Looking at What Actually Changed in a Given Commit

Git allows you to focus in on one commit in particular and get greater detail.  What changed between the last time the files had a commit and this time?  Were new files added?  Were lines changed in a text file?  Were images swapped out?  Was anything deleted?  Simply knowing that a change happened isn't enough, usually -- we want to know **what** changed.  In the case of the R workshop, a few lines in a presentation slide changed as part of the most recent commit (the one with the long code that starts with `636b27af`).  


Command Line Interface
----

Let's look at that commit more closely via the command line, using `git show`.  We can see that a few lines were deleted (they're shown in red) and that those lines were replaced by new lines (shown in green).  There's also information about which file was changed, who committed the change, and when the commit was made.

![Terminal window with the command git show 636b27af.  The output includes information about the commit, such as the author and the commit message.  It also includes the file name that was changed in this commit, `quarto_slides/index.qmd`, and shows the actual changes made to the file.  Four lines displayed in red and preceded by minus signs indicate lines that were deleted, and four lines displayed in green and preceded by plus signs indicate lines that were added.](media/git_show_cli.png)

Graphical User Interface
-----

In the GUI, on the other hand, we can see both the history of commits **and** the specific changes associated with a given commit in the same window.  Here is the same image we saw when we looked at the history.  Notice how we have selected one commit in particular in the history on the left, and the changes made in that commit are shown to the right.  The same idiom is used of red meaning deleted content and green meaning added content, but for most people, this display is a bit easier to look at than the printout above.

![GitHub Desktop window shows, in the left side of the window, a history of six commits.  On the right, the actual changes made during the most recent commit are shown. The file name `quarto_slides/index.qmd` is shown, and to the right of that, four lines displayed in red and preceded by minus signs indicate lines that were deleted, and four lines displayed in green and preceded by plus signs indicate lines that were added.](media/git_history_gui.png)

## How to Decide

You now know what a command line interface (CLI) is, and what it looks like to work with the CLI to type Git commands.  You also know more about graphical user interfaces (GUIs) and you've seen what one particular GUI, GitHub Desktop, looks like when you need to do the same Git tasks.

How should you proceed?  How can you decide what to use? 

We think that **the best way to use Git is the way that you'll actually be willing to do**! 

There is nothing wrong with using Git using a GUI, and rarely if ever using the command line.  Note that this is not an uncontroversial opinion.  Some Git users and instructors suggest that everyone should learn the command line way of using Git first, because it is the most powerful way to use Git.  The Git website itself includes [online documentation that says, in part](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line):

> For this book, we will be using Git on the command line. For one, the command line is the only place you can run all Git commands — most of the GUIs implement only a partial subset of Git functionality for simplicity. If you know how to run the command-line version, you can probably also figure out how to run the GUI version, while the opposite is not necessarily true.... So we will expect you to know how to open Terminal in macOS or Command Prompt or PowerShell in Windows. 

We think that a CLI-first approach works for **some** people.  After all, if you can drive a car with a manual transmission, it's easy to switch to an automatic transmission, but it's hard to do the reverse.  If you like having lots of control and seeing how things work behind the scenes, you'll enjoy working in the command line.  And then you'll know the commands by name and be able to search online easily for how to do complex things in Git.

We also think there's a very large contingent of users who would be so frustrated or intimidated by using the CLI that a CLI-first approach won't work for them.  If you're not first and foremost a computer programmer, you probably don't have the habit of working in the command line.  It's absolutely acceptable to decide that you don't want to have to learn two skills -- Git and the command line -- at the same time.  Learning to use Git in a GUI is plenty of effort on its own, without the added complexity of getting comfortable using the command line.

In the end, the important thing is **that** you use version control.  The details of **how** you do it, what interface you choose, is a matter of personal taste.

## Quiz 

What are some advantages of using Git via a CLI (command line interface)?

[[X]] Git used in the command line can provide greater power and control than Git GUIs.
[[X]] Using Git in the command line is always free.
[[ ]] Most people find using a CLI to be more intuitive and simple than using a GUI.
[[X]] The command line interface can work on any computer system that you can install Git on, unlike GUIs.
[[ ]] The command line display is more information-dense than a graphical display.
***
<div class = "answer">

It's true that Git used in the command line can provide greater power and control than Git GUIs are able to provide, especially for infrequently used tasks, which may be impossible to perform in a Git GUI.  It's also true that Git commands come with the Git software, so using Git in the command line is always free (because Git is free!).  Additionally, not all computer systems may have a graphical user interface at all, and in those cases, you will need to use Git in the command line.
<br/><br/>
It's not true, however, that most people find using the CLI to be more intuitive.  Since most of us use GUIs in all or almost all of our work with computer systems, most people find working via typed commands in a command line to be a bit more difficult than using point-and-click methods.
<br/><br/>
It's also not true that the command line display is more information-dense than a graphical display.  In fact, the opposite is true.  Graphics can be much more information-dense than text!
</div>
***

------

What are some advantages of using a Git GUI (graphical user interface)?

[[ ]] Git GUIs, like Git itself, are free and open source.
[[X]] Git GUIs will be more familiar and comfortable for many users than using a CLI.
[[ ]] Git GUIs can accomplish anything you need to do in Git.
[[X]] Using a Git GUI means not having to memorize a lot of commands.
***
<div class = "answer">

"Git GUIs, like Git itself, are free and open source" is false.  While some Git GUIs are free, that's certainly not true of all of them!  
<br/><br/>
Also, while it's true that graphical user interfaces will feel much more familiar and easy to use for most users (compared to using a CLI), they can't do everything.  For tasks that are infrequently performed, you might not be able to use a Git GUI to accomplish that task -- you might have to use a Git command to do that work. Therefore, it's not true that Git GUIs can accomplish anything you need to do in Git.
<br/><br/>
Finally, an advantage of a Git GUI is that it depends on menus and suggestions, allowing you to point and click to do your work.  That means not having to memorize a lot of commands!

</div>
***

------

Which of the following is a Git GUI (or Git client) that you've seen used in this module?

[( )] GitDesk 
[( )] DesktopGit
[(X)] GitHub Desktop
[( )] GitToIt
***
<div class = "answer">

That's right!  There are many Git GUIs available, and we showed GitHub Desktop, a popular Git graphical user interface, in our screenshots comparing GUI to CLI use in Git.

</div>
***

## Additional Resources

* The [Pro Git Book](https://git-scm.com/book/en/v2) is incredibly useful and detailed.  It is centered on using the command line interface to use Git.  We particularly suggest:

  - [Getting Started: About Version Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control), which talks about distributed versus centralized version control, and
  - [Appendix A: Git in Other Environments -- Graphical Interfaces](https://git-scm.com/book/en/v2/Appendix-A%3A-Git-in-Other-Environments-Graphical-Interfaces), which talks about point-and-click graphical software to help you use Git.

* If you'd like to learn more about working in a command line interface, our [Bash / Command Line 101](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_101/bash_command_line_101.md#1) module might be helpful!

* GitHub's [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf) is very useful with a number of commands to use in a CLI!

* For some links and comparison pricing for various Git GUI software packages, see [the official git page that lists some of these](https://git-scm.com/downloads/guis).
## Feedback

@feedback
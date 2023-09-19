<!--
author:   Joy Payton
email:    paytonk@chop.edu
version:  1.0.0
current_version_description: Initial version
module_type: standard
docs_version: 2.0.0
language: en
narrator: US English Female
mode: Textbook

title: Git Command Line Interface versus Graphical User Interface

comment:  Compare the two ways of interacting with Git to decide which is best for you.

long_description: You can use Git using a command line interface (CLI) and typing commands, and you can also use Git using graphical user interface software which is optimized for point-and-click.  This module will compare and contrast these two options to help you decide how to use Git in your work.

estimated_time_in_minutes: 45

@pre_reqs
Learners should know what version control is and why it's important.  To acquire basic knowledge of version control, we recommend our [Introduction to Version Control](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/git_intro/git_intro.md#1) module.  No previous experience with git is required.
@end

@learning_objectives  
After completion of this module, learners will be able to:

- Explain what a **graphical user interface** is and the advantages and limitations of a GUI
- Explain what a **command line interface** is and the advantages and limitations of a CLI
- Name one major Git graphical user interface and explain where to obtain it

@end

good_first_module: 
coding_required: 

@sets_you_up_for

@end

@depends_on_knowledge_available_in

@end

@version_history 

Previous versions: 

No previous versions.

@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
-->

# Git Options: Command Line and Client

@overview

## What is Git?

You may already know what Git is and use it at work, but let's review.

Git is a **distributed**, **open source** **version control** system. Let's talk about each of those terms:

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

Git is **FOSS**, or **free and ppen source**.  This means that git is "free" in two ways -- in the meaning of having **no cost** and also in that can be used widely **without intellectual property concerns or licensing restrictions**. 

This is important because it means that people around the world use Git.  Students use it, individuals use it, large companies use it, people in highly-resourced projects use it, and people on a shoestring budget use it. 

## How Does One Use Git?

You can use git in two main ways:

* Using a **command line interface**, or **CLI**
* Using **graphical user interface**, or **GUI**.

First, let's talk about the word **interface**.  An interface is a way of interacting with a system.  A panel of buttons in an elevator is an interface.  You use this interface by pushing the button that has the number of the floor you want to go to.  The dashboard of your car is an interface.  It displays information you will find helpful, like how much fuel you have and how fast the car is going.  Interfaces can provide controls, ways for the user to do something (like change gears, turn on the radio, or close elevator doors), and they can provide information (like the current floor, the engine temperature, and the current velocity).  Many interfaces do both -- they provide information and they provide controls.  

Sometimes the same system will have a couple of different kinds of interfaces.  For example, an elevator will usually have a simple, easy interface for users of the elevator, in the form of buttons inside.  But in an office building, the security desk will have another interface, often using software, that shows where each elevator is, if elevators are going up or down, if they're stuck because someone is holding the doors open, and so forth.  This interface is often a bit more complex and requires a bit of learning what the different symbols and codes mean.  Probably, the security desk has a way to control all the elevators at once, such as in the case of a fire alarm.  This is a level of control that the elevator passenger interface (the buttons inside the elevator car) does not have.

Let's talk about two types of interfaces for working with Git.

## Intro to the Command Line Interface

If you've ever watched a Hollywood film in which the protagonist saves the day by typing commands into the computer (often with tense music in the background and very loud and fast typing), you've seen a depiction of a command line interface, or CLI.  These dramatic depictions often suggest a few false things about using a CLI: 

* You have to be a computer genius to use the command line, 
* The consequences of getting a command wrong are severe, and 
* People who use the command line have all the things they need to type memorized (see also: they are geniuses).

This means that many people who are new to the command line interface might find the idea of working in the CLI intimidating.  We hope we can explain the pros and cons of the command line so you can make a decision based on what's most useful to you, instead of on misconceptions about how difficult or dangerous working in the command line is.

Let's start by going over what the command line interface is.

Before slick graphical interfaces, before there was such a thing as a computer mouse, the usual way to interact with a computer was by typing commands through a keyboard.  The command line was usually at the bottom of the screen, with a prompt (maybe `C:>` or something like that) and a blinking cursor that was waiting for the user to type a command.  The user could type a command, in a special kind of code that the computer could understand, and the computer would do that thing.  For example, in a UNIX or Linux computer (and later in Macs), the user might type `ls` to list the files in a particular location.  In MS-DOS (and later in Windows), a user might type `dir` to do the same thing.

Here's a screenshot of a very common thing you might want to do: list files in a particular directory.  In the image, the user is working in a directory called `bias_variance_tradeoff` and asks the computer to list the files in that directory using the command `ls`.  Three things are listed: two files, and a directory called `media`.  The user then asks for a list of the files in the `media` directory by typing `ls media`, and six file names are shown.

![A terminal window in which the user is working in a directory called `bias_variance_tradeoff`.  The command `ls` is followed by a file listing of two files, and a directory called `media`.  The next command is `ls media`, and six file names are shown.](media/ls.png)

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

You may have never used a CLI, and that's perfectly fine.  It doesn't mean you're less skilled or intelligent than people who do use the command line.  This is important to remember because sometimes in tech there are gatekeepers, people who think their way to do something is the only or best way.  You might run across people who use the command line frequently and act suprised or aghast that you don't.  Please don't let gatekeepers change your understanding of your own competence!  

</div>

While most things you want to accomplish on your computer can be done using multiple interfaces, some of which may be more user-friendly and graphical, there **are some things that can only be done by command line**.  Things that people need to do frequently, like look at a list of files in each directory, may be able to be accomplished through many interfaces -- a file browser that is point-and-click, for example, as well as a command typed into the CLI to list files using `dir` or `ls`.  But very specific or customized tasks that are done more rarely may only be able to be accomplished by command line.  

Git has lots of commands and actions, and some of them can only be done by using the command line, because they're so niche and specific to certain circumstances that graphical software simply hasn't included that command.  There's a good chance that you might end up using Git for years before you run across a situation that requires the command line, but it's important to know that you can do more things in Git using the command line.

## Command Line Interface Common Questions

If you've never used a command line, you might have a few common questions, like:

* How do I get to the command line?  What program do I open to be able to type in commands?
* What do I type into the command line to do things?  How will I know what to type?
* What will happen if I get things wrong?

Where is the Command Line Interface?
----

Most people use a Mac or a Windows operating system on their computer.  To get to the command line, you'll use **Terminal** in macOS or **Command Prompt** or **PowerShell** or **Git Bash** in Windows.  Using the command line can be a little different based on the computer system you use and which program you use. Terminal is a Linux-like environment that uses the bash language, while Command Prompt on Windows is limited to MS-DOS commands without scripting abilities.  PowerShell is an automation engine designed for Microsoft products that you can also run commands from, but we generally don't recommend it for working with Git.  And Git Bash is a Windows add-on that allows Windows users to have the same powerful and industry-standard Linux-like interface that Mac users get by default.

What Do I Type?
---

When it comes to knowing what to do in a computer, the command line interface can feel daunting.  There's no help menu to click on, just a blank space that you're supposed to type into.  But what do you type?  How do you know what to do?  

There are lots of places to learn commands, and learning how to search the internet for someone who has already had the same challenge as you and learned how to do it might help.  For example, if you're not sure how to list the files in a directory, you might search using terms like "command line what files are in my directory" or "CLI show files Windows" or something similar.  It takes practice to learn the vocabulary to create good search terms, but keep in mind that even pros who use the command line many times a day will often search for things rather than rely on their memory!  Another place to learn the basics of working in the command line is in our [Bash / Command Line 101](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_101/bash_command_line_101.md) module.  This is a good place to get some basic practice in so you feel more confident.

There are also `man` (short for *manual*) and `help` documentation pages that you can view within the command line.  For example, in a Linux-like CLI such as the Mac Terminal or Git Bash on Windows, typing `man ls` will give lots of instructions on how to use the `ls` command.

<div class = "history">
<b style="color: rgb(var(--color-highlight));">Historical context</b><br>

If you try typing a `man` command, like `man ls`, chances are that there is a great deal of text, and you will need to keep hitting enter or scrolling to see all of it.  And then, you might run into the problem of not knowing how to exit the page viewer!  If you see a colon as a prompt, that's a good sign that you can type `q` to quit.  

Learning how to quit out of things that are happening in the command line is a very common issue for brand new users, and it's something of a rite of passage.  

There's a text editor that some people use from the command line called `vim` which is notoriously tricky to learn (we don't recommend it, we prefer `nano`).  So many people ask for help getting out of `vim` that ["How do I exit Vim?"](https://stackoverflow.com/questions/11828270/how-do-i-exit-vim) is one of [Stack Overflow's](https://www.stackoverflow.com) most frequently viewed posts! It's a question so popular that it [has its own memes](https://stackoverflow.blog/2017/05/23/stack-overflow-helping-one-million-developers-exit-vim/).  

</div>

And finally, let's talk about getting things wrong.  What will happen if you type the wrong thing?  Probably, literally **nothing** will happen.  The computer will give the equivalent of a shrug and say "I don't understand."  If you type a command that doesn't exist, or do something wrong, like put some words in the wrong order, you'll get an error message that might feel difficult to parse, but doesn't itself mean that anything got harmed.  

Of course, it makes sense to check what a command actually does before typing it.  For example, the command `rm` removes something -- a file, or even a directory and everything in it.  If someone wanted to do a very mean prank they might suggest that you use a command including `rm`.  So after you search online but **before** you type a command in, do a bit of searching about what the command does.  If the command does something like list, show, display, report, or similar terms, it's probably very safe to use.  If the command does something like move, delete, change, remove, truncate, or other similar terms, you might want to understand exactly what the command does, including its **arguments** (other terms you type, which might be things like a text string in quotes or a file name) and its **flags** (options that look like one or two dashes followed by a letter or word, like `-all` or `-a`).


## Graphical User Interface

A graphical user interface, or GUI (pronounced "gooey") is meant to make things easier for a human user -- that's why the word *user* is in the name.  While some interfaces are meant to allow for interactions between two computer programs (that's what an API, or application programming interface, is for), a GUI is intended for human users, not programs.  A GUI is an interface that is highly visual and relies on graphics (shapes, images, icons, windows, and other kinds of visual cues), which for many users is helpful.  

The operating system of your Windows or Mac computer has a highly complex graphical user interface, and so do most of the programs you might purchase as a consumer (things like Microsoft Word or Adobe Photoshop).  You use a mouse, not a keyboard, to click on pictures that represent programs in order to open them.  You use a mouse to click on words like "File" or "Window" to show a menu of options.  You might use a mouse to click and drag to select a portion of an image or a selection of words, and then delete or move your selection.

If you're like many people, all of your computer interactions take place in a GUI.  The benefits of a graphical user interface are clear: it's easier to use.  You don't have to remember a keyboard command for changing an image from color to black and white, you can use a visual menu that you select from.  You don't have to remember the command for renaming a file, you just need to know what to click on to select the "rename" option.  This means you can accomplish a lot without having to memorize a long list of commands.  Often, the people who make graphical user interfaces spend a lot of time figuring out what the most frequent tasks are and they work to make those as easy as possible to do.  

In some cases, a graphical user interface is only one way to interact with a system, and you have a choice of which interface you want to use.  Git is an example.  With Git, there are many graphical user interfaces available, made by various different companies.  While you might choose to use Git by typing commands into the command line, you might also interact with Git with one of these GUIs (which are also called Git **clients** or **client software**):

* The Git GUI that's included in RStudio
* GitKraken
* The source control GUI that's included in VSCode
* SourceTree
* GitHub Desktop
* and many more!

Some of these are free, some are free and open source, and some have a cost (either for everyone, or with a "freemium" model that has a free tier).  Which is the best?  We'd argue that the best Git GUI is the one that your team uses and you'll have friendly support around.  

## Comparing and Contrasting

Let's compare and contrast some things you might need to do in Git, and see how they look different in the two interfaces.  Don't worry if you're not sure what these tasks mean, but just take a look at how the two interfaces look.  Do you prefer one over the other?

Adding a new repository
-----

First, let's create a new repository in an existing directory.  What this means is that we have a directory (folder) of files on our computer, and we realize that we'd like to add version control to this folder.  In our example case, we have a directory called `my_important_directory`, and it is located within the `Documents` folder in a local laptop.

In a command line, you'd need to navigate to that directory (in the image below, in a MacOS Terminal, this is done using `cd`, which means "change directory"), and type `git init`.

![Terminal window which shows the command `cd my_important_directory` followed by the command `git init`.  The output of the second command reads "Initialized empty Git repository in /Users/paytonk/Documents/my_important_directory/.git/".](media/git_init.png)

In a GUI (here, GitHub Desktop), we have to put in the name of the repository, which is the name of the folder, as well as the name of the parent directory (`Documents`).

**Want to watch this process?  Click on the image below to play an animated gif.  It will continue to loop and you can re-start it by clicking again.**

<div style="display:none">

@gifPreload

</div>

<figure>

  <img src="https://github.com/arcus/education_modules/blob/git_cli_vs_gui/git_cli_vs_gui/media/git_init_gui.png?raw=true" height="756" width="540" alt="Adding a new repository using the GitHub Desktop graphical user interface" data-alt="https://github.com/arcus/education_modules/blob/git_cli_vs_gui/git_cli_vs_gui/media/git_init_gui.gif?raw=true" style = "border: 1px solid rgb(var(--color-highlight));">

<figcaption style = "font-size: 1em;">

Click on the image to play the demo of the above steps!

</figcaption>

</figure>

## Additional Resources

* The [Pro Git Book](https://git-scm.com/book/en/v2) is incredibly useful and detailed.  We particularly suggest:
  - [Getting Started: About Version Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control), which talks about distributed versus centralized version control, and
  - [Appendix A: Git in Other Environments -- Graphical Interfaces](https://git-scm.com/book/en/v2/Appendix-A%3A-Git-in-Other-Environments-Graphical-Interfaces), which talks about point-and-click graphical software to help you use Git.

* If you'd like to learn more about working in a command line interface, our [Bash / Command Line 101](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_101/bash_command_line_101.md) module might be helpful!

* For some links and comparison pricing for various Git GUI software packages, see [the official git page that lists some of these](https://git-scm.com/downloads/guis).
## Feedback

@feedback

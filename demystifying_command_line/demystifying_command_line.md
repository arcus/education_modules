<!--
module_id: demystifying_command_line
author:   Joy Payton
email:    paytonk@chop.edu
version:  1.0.0
current_version_description: Initial version
module_type: standard
docs_version: 4.0.0
language: en
narrator: US English Female
mode: Textbook
title: Demystifying the Command Line Interface 
comment:  Understand what the command line interface is and why it's useful!
long_description: The command line interface (CLI) of your computer allows you to type commands to do tasks. This module explains what the command line interface is, how to get to it, and how to learn more about using it.  It's appropriate for brand new beginners.
estimated_time_in_minutes: 30

@pre_reqs
No particular skills or experience are required for this module.  
@end

@learning_objectives  
After completion of this module, learners will be able to:

- Define the term *interface*
- Explain how a computer user interacts with a command line interface 
- Explain how a computer user interacts with a graphical user interface



@end

good_first_module: true
collection: demystifying, infrastructure_and_technology
coding_required: false

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

# Demystifying the Command Line Interface

@overview

## Interfaces

There are two main ways people interact with computers:

* Using a **command line interface**, or **CLI**
* Using **graphical user interface**, or **GUI**

First, let's talk about the word **interface**.  An interface is a way of interacting with a system.  

A panel of buttons in an elevator is an interface.  You use this interface by pushing the button that has the number of the floor you want to go to.  The dashboard of your car is an interface.  It displays information you will find helpful, like how much fuel you have and how fast the car is going.  

Interfaces can provide **controls**, ways for the user to do something (like change gears, turn on the radio, or close elevator doors), and they can provide **information** (like the current floor, the engine temperature, and the current velocity).  Many interfaces do both -- they provide information and they provide controls.  

Sometimes the same system will have a couple of different kinds of interfaces.  For example, an elevator will usually have a simple, easy interface for users of the elevator, in the form of buttons inside.  But in an office building, the security desk will have another interface, often using software, that shows where each elevator is, if elevators are going up or down, if they're stuck because someone is holding the doors open, and so forth.  This interface is often a bit more complex and requires a bit of learning what the different symbols and codes mean.  Probably, the security desk has a way to control all the elevators at once, such as in the case of a fire alarm.  This is a level of control that the elevator passenger interface (the buttons inside the elevator car) does not have.

## A Quick Aside: GUIs

We said on the last page that there are two main computer interfaces for human users:

* The **command line interface**, or **CLI**
* The **graphical user interface**, or **GUI**

This module demystifies the command line interface (CLI), but let's briefly describe what a GUI is.

A **graphical user interface**, or **GUI** (pronounced "gooey") is meant to make things easier for a human user -- that's why the word *user* is in the name.  While some interfaces are meant to allow for interactions between two computer programs (that's what an **API**, or **application programming interface**, is for), a GUI is intended for human users, not programs.  A GUI is an interface that is highly visual and relies on graphics (shapes, images, icons, windows, and other kinds of visual cues), which for many users is helpful.  

The operating system of your Windows or Mac computer has a highly complex graphical user interface, and so do most of the programs you might use as a consumer (things like Microsoft Word, Slack, Google Chrome, or Adobe Photoshop).  You use a mouse, not a keyboard, to click on pictures that represent programs in order to open them.  You use a mouse to click on words like "File" or "Window" to show a menu of options.  You might use a mouse to click and drag to select a portion of an image or a selection of words, and then delete or move your selection.

If you're like many people, almost all of your computer interactions take place in a GUI.  Often, the people who make graphical user interfaces spend a lot of time figuring out the most frequent tasks people want to do, and they design the GUI to make those as easy as possible to do.

What makes a GUI different than a CLI?  A CLI is completely text based and requires typed commands.  Let's learn more in the next few pages!

## Mythology about the Command Line Interface

If you've ever watched a Hollywood film in which the protagonist saves the day by typing cryptic commands into the computer (often with tense music in the background and very loud and fast typing), you've seen a depiction of a **command line interface**, or **CLI**.  These dramatic depictions often suggest a few false things about using a CLI: 

* You have to be a computer genius to use the command line, 
* The consequences of getting a command wrong are severe, and 
* People who use the command line have all the things they need to type memorized (see also: they are geniuses).

This means that many people who are new to the command line interface might find the idea of working in the CLI intimidating.  We hope we can explain the pros and cons of the command line so you can make a decision based on what's most useful to you, instead of on misconceptions about how difficult or dangerous working in the command line is.



## What Is a CLI (Command Line Interface?)

Let's start by going over what the command line interface is.

Before slick graphical interfaces, before there was such a thing as a computer mouse, the usual way to interact with a computer was by typing commands through a keyboard.  The command line was usually at the bottom of the screen, with a prompt (perhaps `C:>`) and a blinking cursor that was waiting for the user to type a command.  The user could type a command, in a special kind of code that the computer could understand, and the computer would do that thing.  


<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

You may have never used a CLI, and that's perfectly fine.  It doesn't mean you're less skilled or intelligent than people who do use the command line.  

This is important to remember because sometimes in tech there are **gatekeepers**, people who think their way to do something is the only or best way, and that if you don't do things their way, you're wrong or undeserving.  For example, you might run across people who use the command line frequently and consider people who don't use the command line to be less talented.  That can be a form of gatekeeping!

**Please don't let gatekeepers change your understanding of your own competence!** 

</div>

## Command Line Interface Common Questions

If you've never used a command line, you might have a few common questions, like:

* How do I get to the command line?  What program do I open in my computer to be able to type in commands?
* What do I type into the command line to do things?  How will I know what to type?
* What will happen if I get things wrong?

Where is the Command Line Interface?
----

Most people use a Mac or a Windows operating system on their computer.  To get to the command line, you'll use **Terminal** in macOS or **Command Prompt** or **PowerShell** or **Git Bash** in Windows.  Using the command line can be a little different based on the computer system you use and which program you use. 

What Do I Type?
---

When it comes to knowing what to do in a computer, the command line interface can feel daunting.  There's no help menu to click on, just a blank space that you're supposed to type into.  But what do you type?  How do you know what to do?  

There are lots of places to learn commands.  One skill that will help is learning to effectively search the internet for a good description of the thing you're trying to do.  Chances are that you'll find someone who has already had the same challenge as you and learned how to solve it.  For example, if you're not sure how to list the files in a directory, you might search using terms like "command line what files are in my directory" or "CLI show files Windows" or something similar.  It takes practice to learn the vocabulary to create good search terms, but keep in mind that even pros who use the command line many times a day will often search for things rather than rely on their memory! Below, see a comic that shows the distress of someone asked to accurately use the command line using the `tar` file compression utility. While this is something that a Unix or Linux user might do with some frequency, most people can't remember it spontaneously.

![A four-panel cartoon. People standing over a bomb with an attached keyboard yell "Rob! You use Unix! Come quick!".  The bomb display reads "To disarm the bomb, simply enter a valid `tar` command on your first try.  No googling.  You have ten seconds."  The group looks on in silence, until one person says, "Rob?".  Rob replies, "I'm so sorry."](https://imgs.xkcd.com/comics/tar.png "[Tar](https://xkcd.com/1168/) comic by xkcd, [CC BY-NC 2.5](https://xkcd.com/license.html).")

One place to learn the basics of working in the command line is in our [Bash / Command Line 101](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_101/bash_command_line_101.md) module.  This is a good place to do some safe, easy command line practice so you feel more confident.

There are also `man` (short for *manual*) and `help` documentation pages that you can view within the command line.  For example, in a Linux-like CLI such as the Mac Terminal or Git Bash on Windows, typing `man ls` will give lots of instructions on how to use the `ls` command.

And finally, let's talk about getting things wrong.  What will happen if you type the wrong thing?  Probably, **nothing** will happen.  The computer will give the equivalent of a shrug and say "I don't understand."  If you type a command that doesn't exist, or do something wrong, like put some words in the wrong order, you'll get an error message that might feel difficult to parse, but doesn't itself mean that anything got harmed.  

Of course, it makes sense to check what a command actually does before typing it.  For example, the command `rm` removes something -- a file, or even a directory and everything in it.  If someone wanted to do a very mean prank they might suggest that you use a command including `rm`.  So after you search online but **before** you type a command in, do a bit of searching about what the command does.  


## The Practical Use of GUIs and CLIs 

Most things you want to accomplish on your computer can be done using multiple interfaces, allowing you to choose which you prefer -- graphical or command line. However, as you get into very specific or customized tasks that are done more rarely, there **are some things that can only be done by command line**.  It might be helpful to get a little comfortable with the command line interface on your computer now, before you discover that you have to use it for a specialized task.  If that's something that interests you, our [Bash / Command Line 101](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_101/bash_command_line_101.md) module might be helpful!



## Quiz

Which of the following could be defined as an interface?

[[X]] A method for two computer systems to interact
[[X]] A series of switches and dials used to control a physical device
[[X]] A point-and-click set of menus in a computer program
[[X]] A set of on-screen information about your progress in a video game
[[X]] A car dashboard
[[?]] Hint: There are several correct answers!
***

<div class = "answer">

All of these are examples of interfaces!  An interface is a way to interact with a system -- to get information from it (as in the displays on a car or video game) or to give information to it (as in a clickable menu, switches and dials, or typed commands).  Some interfaces are for humans (like a car dashboard) and some are intended for use by an automated system (like an API -- a method for two computer systems to interact). 

</div>
***

------

Which of the following is true about graphical user interfaces (GUIs)?  Check all that apply!

[[ ]] GUIs offer the same level of control of a system as command line interfaces (CLIs).
[[X]] Pointing-and-clicking is a frequently used way of interacting with GUIs.
[[X]] GUIs depend principally on visual cues like windows, words, and shapes on a screen.
[[ ]] GUIs depend principally on typing text commands.
[[X]] GUIs are designed with human users in mind.
[[ ]] GUIs are a second-best alternative for people who aren't smart enough to use the command line.
[[?]] Hint: There are several correct answers!
***

<div class = "answer">

Graphical user interfaces don't always offer the same level of control of a system as command line interfaces.  This is why some people strongly advocate that everyone learn to use the command line tools for a system, if possible.

It's true that GUIs depend principally on visual cues like windows, words, and shapes on a screen, and that's why pointing-and-clicking is a frequently used way of interacting with GUIs.

GUIs are designed with **human users** (as opposed to other computer applications) in mind, and there is an entire area of tech devoted to user interface (UI) and user experience (UX) design to make systems and GUIs better.

GUIs do **not** principally rely on typing text commands -- you're thinking of a command line interface!

Finally, and this is important... GUIs are **not** a second best alternative, and using a GUI instead of the command line says nothing about your skills, intelligence, or experience. 

</div>
***

------

Which of the following is true about the command line interface (CLI)?  Check all that apply!

[[ ]] CLIs are best used by people with great memorization skills.
[[ ]] CLIs are inherently more dangerous and can do more harm than GUIs, so novice users should avoid using them.
[[X]] CLIs can feel intimidating to people who are just starting out.
[[ ]] CLIs depend principally on visual cues like windows, words, and shapes on a screen.
[[X]] CLIs depend principally on typing text commands.
[[X]] CLIs can provide greater power and control than GUIs in some systems, like Git.
[[?]] Hint: There are several correct answers!
***
<div class = "answer">

Command line interfaces can indeed feel intimidating to people who are just starting out, in part because some misconceptions about CLIs.  It's not true that CLIs are best used by people with great memorization skills -- many seasoned users of CLIs have to search online for the right command.  It's also not true CLIs are inherently more dangerous and worth avoiding by novice users.  While you can inadvertently do damage with a CLI, you can also inadvertently do damage with any computer interface!  

CLIs depend principally on typing text commands, not on visual cues like windows, words, and shapes on a screen.  And in many cases, CLIs can provide greater power and control than GUIs in some systems.  This is true in the case of Git!

</div>
***



## Additional Resources

* If you'd like to learn more about working in a command line interface, our [Bash / Command Line 101](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_101/bash_command_line_101.md) module might be helpful!

## Feedback

@feedback
<!--

author:   Meredith Lee
email:    leemc@chop.edu
version:  1.1.1
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Directories and File Paths
comment: In this module, learners will explore what a directory is and how to describe the location of a file using its file path.   
long_description: When doing data analysis in a programming language like R or Python, figuring out how to point the program to the file you need can be confusing. This module will help you learn about how files and folders are organized on your computer, how to describe the location of your file in a couple of different ways, and name files and folders in a descriptive and systematic way.
estimated_time: 15m

@learning_objectives  

After completion of this module, learners will be able to:

- Describe what a directory is
- Distinguish between a relative file path and an absolute file path
- Describe the location of a file using its file path
- Describe a few best practices and conventions of naming files and folders

@end
link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Directories and File Paths

<div class = "overview">

## Overview

@comment

**Is this module right for me?**

@long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**: None.

**Learning Objectives**:

@learning_objectives

</div>


## Files and folders

If you've ever saved a file on your computer, you probably have some familiarity with how files and folders work. Maybe you save a file to your Desktop, or in your Documents folder, or perhaps you made a special folder to hold all of your files relating to a specific project. In some ways, it works very similarly to a physical filing system; related files go in labeled folders, which are stored in a known location (a file cabinet in a file room somewhere).

On your computer, you can have a mix of files and folders. This is a hierarchical filing system, where each folder can have both subfolders and files within it, and the subfolders can have more subfolders and files; if you map it out, it looks like a tree. A folder on your computer is also often called a **directory**.

<div style = "margin: 1rem; width: 750;">
![Diagram of a hierarchical file structure, with a mix of files and folders within folders.](media/files_and_folders.png?raw=true)
</div>

Here is another representation, this time of how the file structure might look on your computer:

```
./
├── study_project
│   ├── analysis.R
│   ├── data
│   │   ├── experiment1.csv
│   │   └── experiment2.csv
│   │
│   ├── notebooks
│   │   ├── data_exploration.Rmd
│   │   └── enrollment_report.Rmd
│   │
│   └── output
│       ├──results_20211231.csv
│       └──results_scatterplot.png
└── Documents
    ├── article.pdf
    └── manuscripts
        ├── manuscript1.docx
        └── figures
            ├── fig1.png
            └── fig2.png

```

### Quiz: Directories

Which of the following is a synonym for "directory"?

[( )] Drive
[( )] Volume
[(X)] Folder
[( )] File
********************************
<div class = "answer">

Directories are often called folders, because the file system on your computer is similar to a physical filing systems, where files are contained in folders. A drive is a physical device where information is stored, and a volume is where the user interacts with the stored information (this is where the directory system is located).

</div>
********************************


## File paths

While you are likely comfortable with accessing files using your computer's graphical interface, when you are trying to access a file using a programming language like R or Python, or in the Command Line, it can seem more complicated. In cases like these, you'll need to use a **file path** to point to the location of the file that you need. Every file has a place that it "lives" in your computer's memory, whether it's on your Desktop or in a folder within a folder within another folder! Accessing your file means pointing your computer to that place.

The simplest file paths might just be the name of the file you're trying to access; other times, the file path might be more complicated, containing the names of several folders, or even starting with `/Volume` or `C:\ `. The next sections will talk more about these different kinds of file paths and why you might use one or the other.

### Relative paths

As the name suggests, a **relative file path** is one that points to a location relative to a reference point. An example of a relative file path might be "data/age_data.csv". The important thing to remember when using relative paths is that, for them to work, the language you're programming in needs to have a frame of reference to start from.

It's a bit like giving directions to a brand new coworker about where to find your stapler. You might tell them that it is in the bottom drawer of your desk in your office. This works well if your coworker is in the same building and on the same floor as you are, since they can see that there is an office with your name on it, a desk in that office, and drawers in that desk. If your coworker is in another building, however, these directions aren't very helpful! You'd have to include the name of the building and the floor where your office is.

This illustrates a concept called a **working directory**. A working directory is really just another file path that sets the default location for a process. In our example above, you could say that the working directory would include the floor of the building where your office is and the address of the building. From that frame of reference, you can access all sorts of things on the floor of that particular building with just a few directions.

### Absolute paths

While relative file paths require a frame of reference to start looking for a file, an **absolute file path** does not-- it already includes everything that the computer might need to find the file. Using the example above, the absolute path to your stapler would include not only where in your office it is, but also the floor number, the building name, the street the building is on, the city it's in, the county, the state, and the country. For a coworker who works in the same building that you do, this level of detail might seem unnecessary, or even overwhelming! However, if there was no frame of reference to start from, these directions would let anyone in the world find your stapler.

An example of an absolute file path to our file `age_data.csv` might look something like this:

`/Users/username/Documents/data/age_data.csv` (Unix-like, including Mac operating systems) or `C:\Users\username\Documents\data\age_data.csv`  (Windows)

### So which kind file path should I use?

By now, you may be wondering whether absolute file paths or relative file paths are better, and the answer is, it depends! When referring to a file in an R or Python script, for example, which type of file path you use will depend on the purpose of the script and who will run it in the future.

Absolute file paths can be useful because you don't have to know what working directory you're in-- you just have to know where the file is. However, as you might have noticed, absolute paths include things like the username of the user account and other folders that may exist on your computer, but not necessarily on anyone else's. If you are the only one using a script, and never plan on running it from any other location, you might choose to use an absolute path, since no matter where your program lives on your computer, it can find the file.

However, if you are working with collaborators or have plans to make your script public, using a relative path might be a better choice. If you keep every file that you need in a single project folder (which could have several subfolders) and maintain/share that folder as a single unit, then you can use file paths that are relative to where the script is being run, and it shouldn't matter where a collaborator saves the folder on their own computer. This is the reproducible choice!

<div class = "warning">
When writing a script in a programming language like R or Python, it's possible to write code that sets your working directory to a specific location each time the script is run. While this might be tempting, in general it's not a great idea, especially in scripts you might share. The working directory you set may not exist on any other computer, and hardcoding it can cause problems later.
</div>

### Quiz: Absolute vs. relative file paths

What is the difference between an absolute file path and a relative file path? Select all that apply.

[[ ]] Absolute file paths are better than relative file paths.
[[ ]] Relative file paths are better than absolute file paths.
[[X]] Absolute file paths contain all of the information about the location of the file, while relative file paths are relative to the current location, or working directory.
********************************
<div class = "answer">

Neither absolute nor relative file paths are "better"-- which you choose will depend on how you will be using or sharing your script. With an absolute path, all of the information to find your file **on your own computer** will be included in the file path. With a relative path, the file path will be in relation to a reference point. Often, relative file paths are used in scripts that will be shared or run on multiple computers.

</div>
********************************

### Quiz: Writing a file path

What would be a relative file path pointing to the file `experiment1.csv` in a subfolder called `data` in a project folder called `study_project`, if `study_project` is your current working directory?

[[data/experiment1.csv]]
[[?]] Hint: Remember that a relative file path is in relation to your working directory-- that's your reference point. And don't forget that file paths are case-sensitive!
<script>
  let input = "@input".trim();
  input == "data/experiment1.csv" || input == "data\\experiment1.csv";
</script>
********************************
<div class = "answer">

Why isn't the correct answer `study_project/data/experiment1.csv`? It's because `study_project` is the working directory, and so you are already there! The file path `study_project/data/experiment1.csv` would be pointing to a **subfolder** called `study_project` with the folder `study_project`, which doesn't exist!

Additionally, either `data/experiment1.csv` or `data\experiment1.csv` would be correct for this question, but which you would choose to use in your script depends on whether you are working in a Unix-like or Mac operating system (the first example) or Windows (the second example).

</div>
********************************


## Naming Best Practices and Conventions

![XKCD comic depicting a disorganized documents folder. Captioned "Protip: Never look in someone else's documents folder."](media/documents.png "Image used under a Creative Commons Attribution-NonCommercial 2.5 License.  Original post can be found at [https://xkcd.com/1459/](https://xkcd.com/1459/)")

When you're working with files and folders in a programming language like R or Python, how you name your files and folders is very important, especially for organization; having a well-defined and descriptive system for naming your files and folders will make it much easier to find the files that you need later.

There are a few best practices for file naming:  

* Names should be descriptive, giving information about what the file contains.
* Avoid spaces and special characters; some software can't recognize or work with files that contains spaces or special characters, and in general operating systems don't allow special characters in file names. Some examples of special characters are `! @ # $ % ^ & * ( ) ; : < > ? . , [ ] { } ' "` and `|`.
* File names shouldn't be too long; some operating systems have limits to how many characters a file name can contain.
* If you include dates in your file names, use the unambiguous ISO 8601 standard (YYYYMMDD; see https://www.iso.org/iso-8601-date-and-time-format.html for more details).
* If you are not using versioning software (like git) for version control, consider including a version number in the file name.
* Be consistent! For example, if you decide to use underscores to separate words (like `my_project.Rmd`), use that convention every time.

In particular, spaces in file names can cause problems and should be avoided. Although your computer's file system will likely allow you to have spaces in your file names, it can make referring to your file in a program more difficult, because of the way programming languages interpret **whitespace characters** (spaces and tabs are both examples of whitespace characters).

However, most file names would be hard to read without some way to distinguish the words from each other! To solve that problem, there are a number of common naming conventions that avoid problematic characters but still make it possible to read individual words clearly:

* camelCase: This naming convention separates words in the file name by capitalizing the first letter of every word after the first (like `myAwesomeScript.py`). Sometimes you'll also see the first letter capitalized as well (`MyAwesomeScript.py`), and this is sometimes called UpperCamelCase.
* snake\_case: This convention separates words with an underscore, with all letters being lowercase (`like my_awesome_script.py`). Notably, this is the convention in the Python and tidyverse R style guides (though other naming styles will also work, you are not required to use snake\_case).
* kebab-case: This convention is similar to snake\_case, except words are separated by dashes instead of underscores (like `my-awesome-script.py`)

This is certainly not an exhaustive list, but these are some of the most common naming conventions you'll encounter. Some developers have a strong preference for one versus another; generally, the most important thing is that you and your team are internally consistent. If you're joining a new team, ask about their file naming preferences.

<div class = "important">
Although you can use a dot (`.`) in file names, you shouldn't use them at the beginning of your file name. By convention, a file that starts with a dot (like, for example, `.cache`) is hidden; you won't see it in your file system. There are certain circumstances where you might purposely create a hidden file, but it's uncommon.
</div>

### Quiz: Naming files

Mica has written an R script to extract from a patient cohort some data about all patients that are under 5 years of age. They have decided to name their script `my awesome R script 03/04/21!.R`. What is wrong with this file name? Select all that apply.

[[X]] The file name contains spaces.
[[X]] The file name contains special characters.
[[ ]] You can't run an R script that has "R" in the name.
[[X]] The file name is not descriptive.
[[X]] The file name contains a date that is ambiguous (doesn't use the ISO 8601 standard).
********************************
<div class = "answer">

There are a few things that make Mica's file name unideal! Spaces in file names are not always supported or are painful to deal with in some software. Special characters (in this case "!" and "/") are not allowed in most operating systems. Even though Mica included a date in their file name, generally a good idea, we can't be sure if the format was MM/DD/YYYY or DD/MM/YYYY because they didn't use the ISO 8601 standard, which is always YYYYMMDD. Additionally, `my awesome R script 03/04/21!.R` doesn't tell us anything about what the script actually does! While that might be fine in the short term, in the long term it will likely lead to some confusion. However, there isn't a rule that you can't include "R" in the name of an R script, though with the `.R` file extension, it's not necessary.

Can you think of a few alternative names for the file above that would be more descriptive and follow the best practices we listed previously?

</div>
********************************

## Additional Resources

* [To read a bit more about file paths, check out this article.](https://education.arcus.chop.edu/file-paths/)
* [Check out this PDF from the University of Glasgow with more detail on developing a good file naming convention](https://edshare.gla.ac.uk/807/1/File_Naming_v2_20200608.pdf)

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Directories+and+File+Paths%22)!

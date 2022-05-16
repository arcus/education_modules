<!--

author:   Nicole Feldman and Elizabeth Drellich
email:    feldmanna@chop.edu and drelliche@chop.edu
version:  1.0.0
module_template_version: 2.0.0
language: en
narrator: UK English Female
title:  Bash: Searching and Organizing Files
comment:  This module will teach you how to use the bash shell to search and organize your files.
long_description: This module is for people who have a bit of experience with bash scripting and want to learn to use it's power to organize their file and folders.
estimated_time: 30 minutes

@learning_objectives

After completion of this module, learners will be able to:

- Search existing files for particular character strings.
- Search folders for files with certain titles.
- Move files to new locations in a directory system.
- Rename files.
@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js
-->

# Bash: Searching and Organizing Files

<div class = "overview">

## Overview

@comment

**Is this module right for me?**

@long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

Learners should be familiar with using a bash shell to navigate a directory system. Learners will get the most out of this lesson if they can also create directories and files, write text to files, and read files from their bash shell command line interface.



**Learning Objectives**

@learning_objectives

</div>


## Lesson Preparation

You will get the most out of this lesson if you follow along with the examples and try out the commands. In order to do that you need to have a bash shell open on your computer. Please follow the instructions appropriate for the computer you are using.

**Open a bash shell.**
If you are using a computer with running iOS (i.e. a Mac) you can use the **Terminal** program. If you are on a computer using Windows, open either **WLS** (Windows Linux Subsytem) or **Git Bash**. If you don't have these programs there are instructions for how to download and set them up in the [Bash 101](link/here) module.

<div class = "important">
We want to be able to search, move, and rename files during this module, but don't want to do that with your important files. Therefore we will set up a little directory with a few files to experiment with. You can safely delete the whole thing afterwards if you want.
</div>

**Download the files.**

Download the [`learning_bash` directory](https://github.com/arcus/learning_bash) from GitHub. Once you go to the link:

1. Click on the green **Code** button.
2. Select **Download ZIP**
3. Once the Zip file has downloaded, un-zipping it will create a folder titled `learning_bash-main`.
4. Place this new folder `learning_bash-main` somewhere you can easily find it. In the examples we will assume that `learning_bash-main` is in the home directory, but you are welcome to leave it in your Downloads folder or move it somewhere else that is convenient for you to navigate to in your command line interface.

## Searching files

Before we start searching for specific things in this directory, let's navigate into it and explore a little bit of what it contains.

```
cd ~/learning_bash-main
ls
```
These commands will give you a list of (almost) everything in the folder.

A few things we can see from this list of files:

1. There is a `README.md` file.
2. There are `.txt`, `.dat` and `.csv` files.
3. The `.csv` file is named `Animals.csv` and each of the `.txt` and `.dat` files has the name of an animal.

It is also a good idea to take a look at what each type of file contains. We would expect `Animals.csv` to be some sort of tabular data with rows and columns. You can use `cat` to display the file and confirm this.

If we take a look at the contents of a `.txt` file, we see a few words in Latin.

```
cat dog.txt
Canis lupus familiaris
```

It looks like the `.txt` files contain the scientific names of the animals! Try looking at a few more to confirm this.

What is in the `.dat` files?

```
cat blue_whale.dat
Length: 29.9 m
Weight: 190000 kg
```

It looks like these might have some length and weight data in them.

We could continue to individually look at the contents of each file, but that is a lot of work even with this small folder. Next we are going to learn how to search these files and folders.




<div class ="learnmore">
Files that start with a `.` (period) are hidden when you enter `ls`. These are usually operational files that help navigate the file system or keep track of metadata. To see all of these files, enter `ls -a`. The `-a` flag tells bash to show you all files and folders.

Since you just downloaded this folder from `GitHub`, you should see `.git` which keeps track of changes to this public directory.
</div>

### Search folder and file names with `find`

The `find` command lets you search file and folder names. Since we just looked at `dog.txt`, we could search for it using `find dog.txt`. The output for this is just the file name  `dog.txt`. That isn't very helpful by itself, but with the `*` symbol we can make it extremely powerful.

<div class = "important">
**Character sequence wildcard `*`**

The asterisk `*` is a character sequence wildcard. It allows you to search for strings of characters when you might know only a portion of the string.

Every character sequence matches `*`, even the empty character sequence:

- `anim*` matches `anim`, `animal`, `animal.csv` `anim_132`

The location of the `*` matters:

- `animal*` matches `animals` but not `_animal`

- `*bear` matches `polar_bear` but not `polar_bear.txt`

You can use more than one `*` at a time:

- `*bear*` matches `polar_bear.txt` and `grizzly_bear.dat`




</div>

The `find` function will return a list of **all** files and folders in your current directory that match the criteria you have asked for. **Give it a try!** Follow along with these three examples:

1. Search for all files of a certain type: `find *.dat` will return a list of files with the extension `.dat`.

2. Search for all files and folders that start with a certain sequence of characters: `find blue*` will return all six files that start with the four characters `blue` as well as the folder that starts with `blue` and the file `blue_morpho` inside that folder.

3. Search for all file names containing a particular sequence: `find *_*` will return all of the files and folders that contain an underscore `_` anywhere in their names. In this folder, the files with underscores correspond to the animals whose common names are more than one word long.




### Search file contents with `grep`

Now that we can search file names, we also want to be able to search file contents.

The command `grep` (rhymes with "step") is a search function to locate a string or pattern within a file or in a directory. The `grep` command requires two arguments, first you need to tell it what string or pattern to look for in quotes, and second you have to tell it where to search.

For example if you wanted to search for `bear` in `Animals.csv` you can run the following command:

```
grep 'bear' Animals.csv
```
This will print out each line of `Animals.csv` that contains the string `bear`:

```
brown bear,mammal
grizzly bear,mammal
panda bear,mammal
polar bear,mammal
```

You could also search several files at a time by listing their file names one after another.

```
grep 'Ursus' brown_bear.txt grizzly_bear.txt panda_bear.txt
```

This will return the files containing `Ursus` as well as each of the lines containing the word.

```
brown_bear.txt:Ursus arctos
grizzly_bear.txt:Ursus arctos horribilis
```

We can make `grep` more powerful by combining it with the `*` we used before. You might have noticed that we didn't search `polar_bear.txt` for the word `Ursus`. It would be a lot easier to just search all of the files that contain `bear` for the word `Ursus`. We can do that!

```
grep 'Ursus' *bear*
```
This output will include the files we saw before as well as the previously missing `polar_bear` file.

```
brown_bear.txt:Ursus arctos
grizzly_bear.txt:Ursus arctos horribilis
polar_bear.txt:Ursus maritimus
```

<div class = "learnmore">
There are a lot of other ways to modify your search pattern... more in additional resources.
</div>

<div class = "learnmore">
Grep stands for **g**lobal **r**egular **e**xpression **p**rint.
</div>


### Quiz: Searching files
1. What command will return all of the files with a `.dat` ending?

[[find *.dat]]
***
<div class = "answer">
The `find` function searches the names of all folders and files in the current directory. The asterisk in `*.dat` matches any string, so all files with the `.dat` ending will be returned by this command.
</div>
***


2. What you command will return all files with a `.dat` ending that contain the word `Weight`

[[grep 'Weight' *.dat]]
***
<div class = "answer">
The `grep` function searches the contents of the files, in this case all of the files that end in `.dat` for the pattern `Weight`.
</div>
***


## Organizing files

While it would be great if all of your files came into being in the location you will want them in forever and with the naming conventions you want to keep forever, that simply isn't it works. Even if you put every file you create in the correct location and give it a perfectly formatted name, you will at some point have to interact with files that someone else created.

Just because a file is in one location, doesn't mean it has to stay there forever, nor does it's name need to be permanent. In this section we will learn and practice moving files around, copying files, and renaming files.

<div class = "important">
Since **we will be making changes** to your files in this section, please use the `learning_bash` directory for practice.  

If you have not yet downloaded it, please follow the instructions on the [Lesson Preparation](#Lesson-Preparation) page.
</div>

### Moving files

Inside of `learning_bash`, create a new directory called `numbered_files`:

```
cd ~/learning_bash
mkdir numbered_files
```

The `mv` command will move files from their current location to a new location. This command needs to know **what** you want to move and **where** you want to move it to.

To move `file_1` to `numbered_files` run the command:

```
mv file_1 numbered_files
```

Now you can use `cd` and `ls` to see that `file_1` is now in `numbered_files`.

You can also move multiple files at a time by entering them one after another, as long as the directory you want them to end up in is at the end.

```
mv file_2 file_3 numbered_files
```

### Renaming Files

### Copying Files

### Quiz: Organizing Files


- `cat`: very powerful three-part function that allows a reader to view, combine (concatenate), or create a new version of a file

  - `cat file 1 file 2` will display the contents of both files on separate lines.
  - `cat > file 4` will create a new file named file 4
  - `cat file 1 >> file 2` will append the contents of file 1 at the end of file 2.
  - `cat file 2` will now confirm if the content in file 1 was successfully appended to the end of file 2.

  ![Head output of slightly less basic python script that organizes a picnic gathering menu amongst three friends.](media/head_example_small.png)


## Additional Resources


- [Exhaustive Wiki of Linux Filesystem Hierarchy](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/index.html)
- [Reinforce Your New Knowledge through this Learning the Shell Page](https://linuxcommand.org/lc3_learning_the_shell.php)


## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work. Thank you in advance for [filling out our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Bash+Scripting+101%22)!

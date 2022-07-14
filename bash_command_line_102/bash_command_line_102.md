<!--

author:   Nicole Feldman and Elizabeth Drellich
email:    feldmanna@chop.edu and drelliche@chop.edu
version:  1.1.0
module_template_version: 2.0.0
language: en
narrator: UK English Female
title:  Bash: Searching and Organizing Files
comment:  This module will teach you how to use the bash shell to search and organize your files.
long_description: This module is for people who have a bit of experience with bash scripting and want to learn to use its power to organize their file and folders.
estimated_time: 30 minutes

@learning_objectives

After completion of this module, learners will be able to:

- Search existing files for particular character strings.
- Search folders for files with certain titles.
- Move files to new locations in a directory system.
- Copy files and directories.
- Delete files and directories.
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
If you are using a computer with running iOS (i.e. a Mac) you can use the **Terminal** program. If you are on a computer using Windows, open either **WLS** (Windows Linux Subsytem) or **Git Bash**. If you don't have these programs there are instructions for how to download and set them up in the [Bash / Command Line 101](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_101/bash_command_line_101.md) module.

<div class = "important">
We want to be able to search, move, and rename files during this module, but don't want to do that with your important files. Therefore we will set up a little directory with a few files to experiment with. You can safely delete the whole thing afterwards if you want.
</div>

**Download the files.**

Download the [`learning_bash` directory](https://github.com/arcus/learning_bash) from GitHub. Once you go to the link:

1. Click on the green **Code** button.

2. Select **Download ZIP**

3. Once the Zip file has downloaded, un-zipping it will create a folder titled `learning_bash-main`. Depending on your computer's operating system, you may be able to un-zip the folder by double clicking on it, or may need to right click on it a select "Extract All." This may create an identically named folder inside `learning_bash-main` that contains all of the individual files.

4. [Find out the file path](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/directories_and_file_paths/directories_and_file_paths.md#6) (location on your computer) of the new folder `learning_bash-main` and navigate there in your command line interface.


<div class = "help">

**Where is my folder?**

If you can see the icon for your `learning_bash-main` folder (maybe in a downloads screen) you can open your command line interface directly into the folder by right clicking on the folder and selecting the appropriate option:

| Command Line Interface | Right-click menu option |
| :- | :- |
| Terminal (Mac or Linux) | New Terminal at Folder |
| Git Bash (Windows) | Git Bash Here |
| WLS (Windows Linux Subsystem) | Open Linux shell here |

This will open a command line interface at the correct location. Once there, you can use the command `pwd` to see the path to your present working directory.

</div>
## Searching files

Before we start searching for specific things in this directory, let's navigate into it and explore a little bit of what it contains.

Make sure to replace `~/your/file/path/here/` with the path to `learning_bash-main` on your own computer that you identified on the previous page.

```
cd ~/your/file/path/here/learning_bash-main
ls
```

<div class = "warning">

Make sure to use the file path to `learning_bash-main` that you found for your own computer. If your computer uses Windows OS, make sure you replace the forward slashes ` \ ` in the path with back slashes `/`.

You can also follow the instructions on the previous page to open your command line interface where you want to end up, without having to use the `cd` command to get there.

</div>

If the `ls` command shows you a single directory also titled `learning_bash-main` instead of a list of files, then `cd` into that directory and type `ls` again. This will give you a list of (almost) everything in the folder.

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

### Search names with `find`

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




### Search contents with `grep`

Now that we can search file and folder names, we also want to be able to search file contents.

The command `grep` (rhymes with "step") is a search function to locate a string or pattern within a file or in a directory. The `grep` command requires two arguments, first you need to tell it what string or pattern to look for in quotes, and second you have to tell it where to search.

For example if you wanted to search for `bear` in `Animals.csv` you can run the following command:

```
grep 'bear' Animals.csv
```
This will print out each line of `Animals.csv` that contains the string `bear`:

```
black bear,mammal
grizzly bear,mammal
panda bear,mammal
polar bear,mammal
```

You could also search several files at a time by listing their file names one after another.

```
grep 'Ursus' black_bear.txt grizzly_bear.txt panda_bear.txt
```

This will return the files containing `Ursus` as well as each of the lines containing the word.

```
black_bear.txt:Ursus americanus
grizzly_bear.txt:Ursus arctos horribilis
```

We can make `grep` more powerful by combining it with the `*` we used before. You might have noticed that we didn't search `polar_bear.txt` for the word `Ursus`. It would be a lot easier to just search all of the files that contain `bear` for the word `Ursus`. We can do that!

```
grep 'Ursus' *bear*
```
This output will include the files we saw before as well as the previously missing `polar_bear` file.

```
black_bear.txt:Ursus americanus
grizzly_bear.txt:Ursus arctos horribilis
polar_bear.txt:Ursus maritimus
```

<div class = "learnmore">
The [origin of "grep"](https://en.wikipedia.org/wiki/Grep) is that it is **g**lobally searching for a **r**egular **e**xpression and **p**rinting the matching lines. In the text editor `ed` that was part part of the original Unix operating system from 1969, you could do these action with the command `g/re/p` and the name has stuck.
</div>


### Quiz: Searching files
1. What command will return all of the files with a `.dat` ending?

[[find *.dat]]
***
<div class = "answer">

The `find` function searches the names of all folders and files in the current directory. The asterisk in `*.dat` matches any string, so all files with the `.dat` ending will be returned by this command.

</div>
***


2. What command will return all files with a `.dat` ending that contain the word `Weight`?

[[grep 'Weight' *.dat]]
<script>
  let input = "@input".trim().replace(/\s+/g, ' ');
  input == "grep \'Weight\' *.dat" || input == "grep \"Weight\" *.dat";
</script>
***
<div class = "answer">

The `grep` function searches the contents of the files, in this case all of the files that end in `.dat` for the pattern `Weight`.

</div>
***


## Organizing files

While it would be great if all of your files came into being in the location you will want them in forever and with the naming conventions you want to keep forever, that simply isn't the way it works. Even if you put every file you create in the correct location and give it a perfectly formatted name, you will at some point have to interact with files that someone else created.

Just because a file is in one location, doesn't mean it has to stay there forever, nor does it's name need to be permanent. In this section we will learn and practice moving files around, copying files, and renaming files.

<div class = "important">
Since **we will be making changes** to your files in this section, please use the `learning_bash-main` directory for practice.  

If you have not yet downloaded it, please follow the instructions on the [Lesson Preparation](#Lesson-Preparation) page.
</div>

### Move files with `mv`

Inside of `learning_bash-main`, there is a directory called `blue_animals` which currently only contains one of the many blue animals, the blue morpho butterfly.

The `mv` command will move files from their current location to a new location. This command needs to know **what** you want to move and **where** you want to move it to.

To move `blue_jay.txt` to `blue_animals` run the command:

```
mv blue_jay.txt blue_animals
```

Now you can use `cd` and `ls` to see that `blue_jay.txt` is now in `blue_animals`.

Notice that we used the **relative** locations of `blue_animals` and the `blue_jay.txt` file. We could also have used their global location. Let's see how we would use **global** locations to move the `blue_morpho.txt` file, currently in `blue_animals`, to the same location as the other animals.

**Tip: You can scroll sideways to see all of the text in the code block:**

```
mv ~/your/file/path/here/learning_bash-main/blue_animals/blue_morpho.txt ~/your/file/path/here/learning_bash-main
```

<div class = "warning">
Make sure to replace `~/your/file/path/here/` with the path to `learning_bash-main` on your own computer.
</div>

You can also move multiple files at a time by entering them one after another, as long as the directory you want them to end up in is at the end.

```
mv blue_and_yellow_macaw.txt blue_morpho.txt blue_animals
```

<div class = "help">
Did you get a message informing you that "No such file or directory" exists? Make sure you are in the right directory with `cd ~/your/file/path/here/learning_bash-main`.
</div>

We can also use the `*` to move all files and folders matching a certain pattern to a new location. Let's make a new folder containing all files pertaining to blue whales:

```
mkdir blue_whale_folder
mv blue_whale.* blue_whale_folder
```
This will move both `blue_whale.txt` and `blue_whale.dat` into the folder `blue_whale_folder`.

Similarly we could move all of the files and folders that start with the word blue into `blue_animals`.

```
mv blue* blue_animals
```
You will get an output warning you that one of the things you asked for cannot be done:

```
mv: rename blue_animals to blue_animals/blue_animals: Invalid argument
```

**This is okay!** In fact it is bash being smart enough to know that you can't move a directory to become a sub-directory of itself! Use `cd` and `ls` to check that all of the other files and folders that started with the characters `blue` are now in the `blue_animals` directory.

### Rename files with `mv`

While there is a specific function for renaming files and folders, the easiest way to rename a file is to again use the `mv` function.

Maybe we want to rename `koala.txt` to be `koala_bear.txt`. The `mv` function lets us do this by simply moving the file currently named `koala.txt` to a new file in the same location called `koala_bear.txt`:

```
mv koala.txt koala_bear.txt
```

<div class = "options">
You can also use the global location names for your files or folders. In the example above we could have gotten the same result with

```
mv ~/your/file/path/here/learning_bash-main/koala.txt ~/your/file/path/here/learning_bash-main/koala_bear.txt
```

The benefit to using the global names is that you can run commands with global names from anywhere, you don't have to be in the folder containing the files. The downside is that you have to make sure to type a much longer name correctly.

</div>

### Copy files with `cp`

The copy function `cp` has the same requirements as the `mv` function: **which file** you want to copy, and **where** you want the copy to go. For example maybe we want to make a new folder called `true_bears` for bears in the genus Ursus, and put copies of those files into the folder while keeping the originals.

```
mkdir true_bears
cp black_bear.txt true_bears
```

There are now two files with the name `black_bear.txt` but because they are in different places, that is okay. The original `black_bear.txt` is unchanged, and the copy is `true_bears/black_bear.txt`.

You can also use `cp` to make a copy of a file with a new name. Brown bear is another name for a grizzly bear.

```
cp grizzly_bear.txt brown_bear.txt
```

Now there are two files with the same contents but different names.

You can also use the asterisk `*` to speed copy all files with certain patterns in their names.

```
mkdir red_animals
cp red* red_animals
```

You get a message that bash isn't copying the folder `red_animals` to itself, but with a different message than when we weren't able to move `blue_animals` into itself with `mv`. This is because we need to do something special to use `cp` on a directory.

### Copy folders with `cp -r`

In order to copy a directory using `cp` you need to include the flag `-r` which stands for "recursive." This tells bash to make a copy not just of the directory, but of all of its sub-directories, and all of their sub-directories, and so on.

Let's make a new directory for all of the animals with colors in their names.

```
mkdir color_name_animals
```

If we want to copy the entire directory of `blue_animals` into this new folder, we need to use the `-r` flag:

```
cp -r blue_animals color_name_animals
```

<div class = "important">
Moving a directory with `mv` will move all of its contents to the new location.

Copying a directory with `cp` requires the `-r` flag in order to copy all of its contents.
</div>

### Quiz: Organizing files

1. You create a new folder titled `canines` in `learning_bash-main`. What command would you use to move the files `dog.txt` and `wolf.txt` into the `canines` folder? Use the relative locations of the files and folders.

[[mv dog.txt wolf.txt canines]]
<script>
  let input = "@input".trim().replace(/\s+/g, ' ');
  input == "mv dog.txt wolf.txt canines" || input == "mv wolf.txt dog.txt canines";
</script>
***
<div class = "answer">

The command `mv dog.txt wolf.txt canines` will move both files into the `canines` folder. The order of `dog.txt` and `wolf.txt` doesn't matter, but `mv` must be first and `canines`, the target folder, must be last.

</div>
***

2. Which of these commands would you use to put a copy of the file `coyote.txt` into the `canines` folder?

[[ ]] `mv coyote.txt canines`
[[X]] `cp coyote.txt canines`
[[ ]] `mv -r coyote.txt canines`
[[ ]] `cp -r coyote.txt canines`
***
<div class = "answer">

The command `mv coyote.txt canines` will move the entire file into the `canines` folder.

The command `cp coyote.txt canines` will create a copy of `coyote.txt` in the folder `canines`.

The command `mv -r coyote.txt canines` will raise an error since `-r` is not one of the options of the command `mv`.

The command `cp -r coyote.txt canines` will **also** create a copy of `coyote.txt` in the folder `canines`. However the flag `-r` is not necessary here because `coyote.txt` is a file and not a directory.

</div>
***

## Deleting files

If you are done with a file and sure you won't need it ever again, it might make sense to delete it.

The command `rm` **remove**s files listed after it from your computer. Maybe you don't actually want two different names for the same species of bear and want to delete the `brown_bear.txt` file we made earlier:

```
rm brown_bear.txt
```

<div class = "warning">
Removing files from your command line interface with the `rm` command **removes** them from your computer. It does not move them to your "Trash" folder.

Be completely sure that you want to remove a file before using the `rm` command.
</div>

If you are sure you want to delete a directory, the recursive flag `-r` will recursively delete a folder and all of its contents, and the contents of any subfolders, and on an on until everything is gone.

Maybe you no longer want a `red_animals` folder since all of its contents are available elsewhere:

```
rm -r red_animals
```

### Quiz: Deleting files

Which statements about the remove command `rm` are **TRUE**?

[[ ]] The command `rm` moves files to your "Trash" folder.
[[X]] To remove a folder and all of its contents you need to use `rm -r`.
[[X]] Sometimes you need to remove files in order to keep your projects organized.
[[ ]] If you accidentally remove a file you wanted to keep, it is easy to recover it.
***
<div class = "answer">

**The command `rm` moves files to your "Trash" folder.** FALSE: the command `rm` removes files from your computer without first moving them to you trash folder.

**To remove a folder and all of its contents you need to use `rm -r`.** TRUE: you need to use the `-r` flag in order to recursively remove all subfolders.

**Sometimes you need to remove files in order to keep your projects organized.** TRUE: there are many projects that need to regularly delete intermediary files, especially when analyzing large datasets.

**If you accidentally remove a file you wanted to keep, it is easy to recover it.** FALSE: recovering a file you have removed with `rm` might be possible if you are using a version control system like Git, but if not, removed files are gone forever.

</div>
***


## Additional Resources

You can always use the manual command `man` to read the documentation of any command. Give it a try with `man cp`!

Reading the manual isn't always the easiest way to get more comfortable with a programming language, so here are some other resources:

- Software Carpentries makes all the materials from their [Unix Shell lessons](https://swcarpentry.github.io/shell-novice/) available.

- The Earth Lab at University of Colorado, Boulder has a nice [bash tutorial](https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/bash/bash-commands-to-manage-directories-files/) that can supplement and reenforce the learning you have done here.

- MDN Web Docs, a project that documents a number of Web platform technologies has [a detailed crash course in bash](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Command_line).



## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work. Thank you in advance for [filling out our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Bash+Searching+and+Organizing+Files%22)!

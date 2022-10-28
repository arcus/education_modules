<!--

author:   Elizabeth Drellich and Nicole Feldman
email:    drelliche@chop.edu and feldmanna@chop.edu
version:  1.0.0
module_template_version: 2.0.1
language: en
narrator: UK English Female
code_language: Bash
topic: Learn to Code 
title:  Bash: Combining Commands
comment:  This module will teach you how to combine two or more commands in bash to create more complicated pipelines in Bash.
long_description: This module is for learners who can use some basic Bash commands and want to learn to how to use the output of one command as the input for another command.
estimated_time: 30 minutes

@learning_objectives

After completion of this module, learners will be able to:

- Write the output of a command to a file using `>` and `>>`
- Chain commands directly using the pipe `|`
@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js
-->

# Bash: Combining Commands

<div class = "overview">

## Overview

@comment

**Is this module right for me?**

@long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

Learners should be familiar with using a bash shell and [navigating a file system from the command line and look at the contents of a file](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_101/bash_command_line_101.md).

The only commands that will be assumed are the navigation commands `cd`, `ls`, and `pwd` and `cat`, all of which are explained in the [Bash / Command Line 101](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_101/bash_command_line_101.md) module.

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

<div class = "warning">

Please download a fresh copy of these files. If you have downloaded them for a previous module, you have likely moved and changed some of them while working through that module and the examples in this module assume that no changes have already been made to the directory.

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

## Inputs and Outputs

The purpose of any command is to take some input and do something with it. The input might a file, a folder, or something you typed in. In the case of `ls` and `pwd` the input is your location in your file system.

Some commands also return output based on the input. For example `grep` returns a list of lines that contain a given regular expression, but doesn't make any changes to any files.

As your bash scripting progresses, you may find or create commands that simultaneously change files and return and output, but the commands we will see in this lesson return output without modifying their input.

### Examples

In your command line interface, use `cd` to navigate to the directory `learning_bash-main` that you downloaded in the [lesson preparation](#lesson-preparation) section. Since the commands we are learning in this section don't make any changes to your files, definitely try them out on some of your own files too!

#### Word count

The word count command `wc` takes a file (or files) as input and returns some basic metadata:

```
wc Animals.csv
      20      36     355 Animals.csv
```

The output counts the number of lines (20), the number of words (36), and the number of bytes (355) in the file, followed by the file's name.

Some common options are to ask for only some of this metadata using flags:

- `wc -l` returns the number of lines followed by the file's name.
- `wc -w` returns the number of words followed by the file's name.
- `wc -c` returns the number of bytes followed by the file's name.
- `wc -m` returns the number of characters followed by the file's name.


<div class = "learnmore">

**Words**   

The `wc` command distinguishes words as strings of characters on the same line separated by at least one space, so it counts `wolf,mammal` as a single word and `blue and yellow macaw,bird` as four words.

**Bytes and characters**   

For all of the files in this lesson, the number of bytes is the same as the number of characters. However when a file contains more than simple plain text, the number of bytes and number of characters can differ by quite a bit!

</div>  

You can also pass multiple files to the `wc` command. It will print out the word count for each, and then helpfully total each column for you at the bottom:

```
wc wolf.txt dog.txt
      1       2      12 wolf.txt
      1       3      23 dog.txt
      2       5      35 total
```
#### First and last lines

You might also want to look at the contents of a file. The `cat` command lets you see the entire file, but sometimes only the first few lines are important for your purposes. Maybe your file contains a long article, but the first few lines are the title, author, and date it was published. You may want that information without having to print out the entire article the way that `cat` would.

The command `head` outputs the first 10 lines of a file. You can ask for the first `n` lines by using the flag `-n`:

```
head -3 Animals.csv
```

You should see these first three lines of `Animals.csv`:

```
blue and yellow macaw,bird
blue jay,bird
blue whale,mammal
```

The `head` command is particularly useful when you know a certain type of information is at the beginning of your file.

The `tail` command is similarly used to output the last lines of a file:

```
tail -4 Animals.csv
```

You should see these last four lines of `Animals.csv`:

```
tiger,mammal
wolf,mammal
blue morpho,insect
koala,mammal
```

The `tail` command is particularly useful when you know a certain type of information is at the end of your file, perhaps because you appended it to the end of the file.

#### Sorting

Sorting the contents of a file can be extremely useful. The file `Animals.csv` has animals listed alphabetically, but the blue morpho butterfly was added to the list later and and therefore out of alphabetical order.

The `sort` command outputs the lines of a file in alphabetical order, the same order that the `ls` command uses to output file names.

**Give it a try** in your command line interface:

```
sort Animals.csv
```

You can change how the lines are ordered using flags. The `-r` flag reverses the order. Try it out:

```
sort -r Animals.csv
```
<div class ="learnmore">

There are lots of options for the `sort` command. All of the options are visible in the manual which you can see by typing `man sort`. In addition to reversing the order with `-r`, a few particularly useful ones include:

- `sort -n` which sorts by numerical value
- `sort -b` which ignores leading blanks
- `sort -f` which treats upper and lower case characters as the same while sorting.

</div>

**Unique occurrences**

As soon as we sort a file, we run into the question of what to do if two lines are identical. The `uniq` command will output the lines of the file in order, but if a line is identical to the line above it, it will be printed only once.

We will use this command more in combination with some other commands, but in a file like `Animals.csv` where every line is different, running `uniq Animals.csv` isn't particularly interesting.

### Writing output to a file

The commands we just saw give us information and insight through their outputs, but that output isn't actually preserved anywhere. If we want to see it again, or use it for something later without re-running the command, we need to save that output in a file. This process is called "writing output to a file" or "redirecting output to a file" because instead of the output being shown to us in the command line interface, it is instead going to be written and saved to the file we name.

The "greater than" symbol, also known as an arrow or more specifically "right arrow" lets us redirect output. On a standard American qwerty keyboard, the `>` is located on the same key as the period `.`

Try running the following code:

```
wc Animals.csv > animals.txt
```

You won't see any output because it was redirected to the newly created file `animals.txt`. Use `cat` or another program to check that the file `animals.txt` contains the text:

```
      20      36     355 Animals.csv
```

A single arrow will replace anything that was already in the file with the new content. If we don't want to replace the content in `animals.txt` we can append (add new lines after the existing lines) to the end of the file using double arrows `>>`:

```
sort Animals.csv >> animals.txt
```

Again there is no output shown because it was redirected into the file `animals.txt`. Check that `animals.txt` now contains the word count at the top, followed by a sorted copy of the data from `Animals.csv`.

<div class = "learnmore">

In the Bash language, right arrows `>` redirect output, and left arrows `<` redirect input. You are unlikely to need to redirect input since most of the time just entering the input you want, like `Animals.csv`, is sufficient. However if you end up writing more complicated pipelines in the future it may be useful to [learn more about redirecting input](https://www.gnu.org/software/bash/manual/html_node/Redirections.html)

</div>

### Quiz: inputs and outputs

Suppose you have acquired a new file with the uninformative name `newfile.txt`. You look at its contents and see that `cat newfile.txt` returns

```
Callinectes sapidus

blue crab,crustacean

Source: https://www.fisheries.noaa.gov/species/blue-crab

The blue crab is a highly sought-after shellfish. Blue crabs live up and down the Atlantic Coast and in the Gulf of Mexico and are caught by both commercial and recreational fishermen. Its scientific name—Callinectes sapidus—translated from Latin means 'beautiful savory swimmer.'

Blue crabs are the most valuable fishery in the Chesapeake Bay. They are also major predators of benthic communities and are prey for many other fish species. Blue crabs are so treasured in the region that the blue crab is the Maryland state crustacean.

Length: 9 in
Weight: .33 lbs
```

You want to convert information in this file into a similar format to your other animal files, while avoiding typing the information in by hand.

1. What command would you type to create a new file `blue_crab.txt` that contains only the first line of this file?

[[head -1 newfile.txt > blue_crab.txt]]
<script>
  let input = "@input".trim().toLowerCase();
  input == "head -1 newfile.txt > blue_crab.txt" || input == "head -1 newfile.txt >> blue_crab.txt";
</script>
***
<div class = "answer">

The output of `head -1 newfile.txt` is the first line of `newfile.txt`. Since no file named  `blue_crab.txt` previously existed, overwriting (`>`) and appending (`>>`) that output have the same result.

</div>
***


2. What command would you type to create a new file `blue_crab.dat` that contains only the last two lines of this file?

[[tail -2 newfile.txt > blue_crab.dat]]
<script>
  let input = "@input".trim().toLowerCase();
  input == "tail -2 newfile.txt > blue_crab.dat" || input == "tail -2 newfile.txt >> blue_crab.dat";
</script>
***
<div class = "answer">

The output of `tail -2 newfile.txt` is the last two lines of `newfile.txt`. Since no file named  `blue_crab.dat` previously existed, overwriting (`>`) and appending (`>>`) that output have the same result.

</div>
***

## Linking commands

We could link commands by writing the output of one command to a file, and then running another command on that file. However if we don't actually need that intermediate file it is possible to speed up the process by passing the output of one command directly to another using a "pipe."

The vertical line `|` is called a **pipe**. On American qwerty keyboards symbol `|` is located on the same key as the backslash ` \ ` and can be typed by using the `shift` key with ` \ `.

<div class = "help">
The pipe symbol is located in different places on different keyboards. If you have trouble finding it, try an internet search for "pipe symbol" along with the country or language of your keyboard.
</div>

With smaller files, the benefits of using pipes over making intermediate files are mostly from having fewer commands to type and run. But if you start working with really large datasets, maybe you are working in an "omics" field like genomics or metabolomics, creating and saving intermediate files, as well as writing and reading them, can use significant time and energy.  

### Using the pipe `|`

The pipe symbol `|` is like the arrow symbols `>` and `>>` in that it redirects the output of the command that precedes it. Instead of writing that output to a file, the pipe turns that output into input for the command that follows.

In the previous section we learned how to sort the lines in the file `Animals.csv`. But maybe we only care about the last 3 animals listed alphabetically. With a pipe we can first `sort` and then immediately look at the `tail`. Give it a try:

```
sort Animals.csv | tail -3
```

You get the last three animals of the alphabetically sorted list: red panda, tiger, and wolf.

What do you think will happen if you switch the order of `sort` and `tail`? Try it out:

```
tail -3 Animals.csv | sort
```
Now the blue morpho butterfly is first, instead of the red panda because the last three lines of `Animals.csv` were tiger, wolf, and blue morpho.

### Combining `|` and `>`

You can also pipe commands and then write the final output to a file. For example we could create a new file with just the last three alphabetical animals from `Animals.csv`.

```
sort Animals.csv | tail -3 > last.txt
```

This command doesn't give any output, but take a look at the contents of your new file `last.txt` and confirm that it contains what you expected.

The double arrow `>>` which appends output to a file can also be combined with pipes. Try this line:

```
tail -3 Animals.csv | sort >> last.txt
```

Now the file `last.txt` should contain six lines:

```
red panda,mammal
tiger,mammal
wolf,mammal
blue morpho,insect
koala,mammal
wolf,mammal
```

### `uniq` revisited

Now that the file `last.txt` has some repeated lines in it, we can get useful information out of the command `uniq`. This command outputs the lines of a file, but only those lines that are distinct from the line directly above.

```
uniq last.txt
```

Since all lines in `last.txt` are different from the line immediately preceding them, this isn't particularly useful. However when combined with the `sort` function, we can eliminate repeated lines:

```
sort last.txt | uniq
```

Now there are no repeated lines! They are also in alphabetical order since we first sorted alphabetically.

If we want to know how many copies of each line were in the original file, the option `-c` for "count" will output the lines with each preceded by the number of occurrences:

```
sort last.txt | uniq -c
```

### Chaining multiple pipes

Piping the output of one command into another is extremely powerful, and chaining multiple pipes to get a **pipeline** only increases the number of things you can do with pipes!

Maybe you want to know how many unique animals are in the file `last.txt`. We saw on the last page how to output the list of unique lines using `sort` followed by `uniq`. If we want to know how many (unique) lines there are, we can use the word count function `wc` with the option `-l` for number of lines:

```
sort last.txt | uniq | wc -l
```

This gives us the single numeric output `4`; there are 4 lines corresponding to the 4 unique animals listed in `last.txt`.

What if we want to know which animal has the shortest scientific name? This also becomes a three step process:

1. Count the characters in each `.txt` file with `wc -m *.txt`. For further explanation of how `*.txt` calls all of the `.txt.` files, see the [lesson on searching and organizing files](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_102/bash_command_line_102.md).
2. Sort the output by number with `sort -n`.
3. Output the first line with `head -1`.

Putting these steps together:

```
wc -m *.txt | sort -n | head -1
      10 indian_cobra.txt
```
The Indian cobra, scientific name _Naja naja_ has the shortest character count of any of the animals listed here.

<div class = "learnmore">

**Why is the character count for `Naja naja` 10?**

The character count includes each of the 8 letters, as well as the single blank space and the "newline" character that indicates the end of the line.

</div>

You can chain as many commands as you want into a pipeline, including search commands like `grep` and `find` that we haven't talked about in this lesson.

### Quiz: linking with `|`

Let's return to the uninformatively named `newfile.txt`:

```
Callinectes sapidus

blue crab,crustacean

Source: https://www.fisheries.noaa.gov/species/blue-crab

The blue crab is a highly sought-after shellfish. Blue crabs live up and down the Atlantic Coast and in the Gulf of Mexico and are caught by both commercial and recreational fishermen. Its scientific name—Callinectes sapidus—translated from Latin means 'beautiful savory swimmer.'

Blue crabs are the most valuable fishery in the Chesapeake Bay. They are also major predators of benthic communities and are prey for many other fish species. Blue crabs are so treasured in the region that the blue crab is the Maryland state crustacean.

Length: 9 in
Weight: .33 lbs
```

What command would append the 3rd line, which reads `blue crab,crustacean` to the file `Animals.csv`?

[(X)] `head -3 newfile.txt | tail -1 >> Animals.csv`
[( )] `head -3 newfile.txt | tail -1 > Animals.csv`
[( )] `tail -1 newfile.txt | head -3 >> Animals.csv`
[( )] `tail -1 newfile.txt | head -3 > Animals.csv`
***
<div class = "answer">

The first three lines are returned by `head -3 newfile.txt`:

```
Callinectes sapidus

blue crab,crustacean
```

and the last line of that text is returned by `tail -1`:

```
blue crab,crustacean
```

Since we don't want to overwrite the text already in `Animals.csv` we have to use the double arrow `>>` to append that line to the end of the file.

</div>
***

## Additional Resources

The [Software Carpentries](https://software-carpentry.org) has a series of lessons on the [Unix Shell](https://swcarpentry.github.io/shell-novice/).

These webinars, recorded by Jacob Levernier are a great walk through the command line.

- [Unix Command Line I Arcus Education Webinar](https://digitalrepository.chop.edu/commandline_computingtools/3/)
- [Unix Command Line II Arcus Education Webinar](https://digitalrepository.chop.edu/commandline_computingtools/2/)
- [Intermediate Bash Scripting Arcus Education Webinar](https://digitalrepository.chop.edu/commandline_computingtools/1/)

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work. Thank you in advance for [filling out our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Bash+Combining+Commands%22)!

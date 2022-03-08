<!--

author:  Elizabeth Drellich
email:    drelliche@chop.edu
version:  0.0.1
language: en
narrator: UK English Female
title: Exploring the History of your Git Repository
comment:  This module will teach you how to look at past versions of your work on Git, compare versions, and return to former versions.
long_description: You know that version control is important. You know how to save your work to your Git repository. Now you are ready to look at and compare different versions of your work. In this module you will you will learn how to navigate through the commits you have made to Git. You will also learn how to compare current code with past code, and, if necessary, revert to an earlier version of your work.

@learning_objectives  
After completion of this module, learners will be able to:

- Identify and use the HEAD of a repository.
- Identify and use Git commit numbers.
- Compare versions of tracked files.
- Restore old versions of files.

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Exploring the History of your Git Repository


<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:**

**Pre-requisites**

This module is for you if:

* You know that version control is important. (See [module](module) to learn why version control is important.)
* You know how to save your work to your Git repository. (See [module](module) to learn how to create a Git repository and put your work into it.)
* You want to learn how to see and compare different versions of your work.


**Learning Objectives**

@learning_objectives

</div>

## Lesson Preparation

*We need some sort of emulator here, probably the best way (if possible) would be to have an emulator that can come preloaded with all of the commands from the previous module so that learners can explore the history without having to go through that entire module, especially if they did it a while back, or already know that stuff. Having something just checkout a particular head in the chain of the modules could then be used for later modules, by checking out later or earlier heads.*

If you are coming to this module directly from the [previous one](link) and still have that console open, you can continue using that console instead.

## Seeing prior commits

Keeping track of all versions and being able to see and compare them is the entire point of using version control on a project you are working on alone. It is also a huge part of working on a project with others, but we will get to that part in [module](module).

Each time you `commit` to Git, you are marking the current state of your project as a checkpoint that you can return to. You will hear these states referred to as *commits*.

<div class = "options">
You are going to learn about two ways to refer to past commits:

- Using HEAD to refer to the latest `commit`.
- Using the commit number assigned to a particular `commit`.

</div>

![The Commit Stack: a stack of 3 flat white boxes, stacked on top of each other with open air in between. The top box is labeled "last committed version of repository", the middle box is labeled "next to last version of repository" and the bottom is labeled "previous version of repository". There are three dots below the lowest box indicating that this pattern continues.](./fig/Commit_stack.svg)

### Using HEAD

The `HEAD` refers to the most recently commit to your repository. It won't include any changes that haven't been committed to the repository yet. You can see that most recent commit by entering `git show HEAD`.

The last thing that Dracula committed in the previous module was the `.gitignore` file in which he told Git not to track certain files:

```
$ git show HEAD
commit 65f447e949e53edc0db08b93670d2e2b35fa6c22 (HEAD -> main)
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Mon Feb 28 11:47:17 2022 -0500

    Ignore data files and the results folder.

diff --git a/.gitignore b/.gitignore
new file mode 100644
index 0000000..f451386
--- /dev/null
+++ b/.gitignore
@@ -0,0 +1,2 @@
+*.dat
+results/
```

<div class = "help">
Sometimes a command will output many lines of code that may not be relevant to you. For example the `show` command will output not just the commit message, but also every single change that you made in that commit. If the output of a command is longer than the number of lines your console displays, you can navigate that output using the down and up arrows on your keyboard, or press `q` to skip to the end of that output.
</div>

Maybe you want to look one step further back into your work. By using `HEAD~n` you can look back $n$ checkpoints in your repository. The `~` named "tilde" and pronounced "TIL-duh."

For example, to look back just one commit before the most recent checkpoint, use `git show HEAD~1`. If instead you wanted to look back three checkpoints (the most recent and then two before that) you would enter `git show HEAD~2`.

![IMAGE: The same stack of 3 white flat boxes, now the top box is labeled `HEAD`, the middle box `HEAD~1` and the bottom `HEAD~2`](./fig/Commit_stack_HEAD.svg)

Using `HEAD` to refer to your commits can be great for looking at recent versions of your repository. But be careful, each time you commit to the repository, you are creating a new most-recent-version that is now the `HEAD` and every older version moves one layer down in the stack.

![IMAGE: On the left, the same stack of 3 flat white boxes are labeled `HEAD`, `HEAD~1`,  and `HEAD~2`. An arrow points to a stack on the right made of the same stack of 3 flat white boxes with a 4th red box on top. This red box is labeled `HEAD` and the boxes below it are labeled, in order from top to bottom, `HEAD~1`, `HEAD~2`, `HEAD~3`](./fig/Commit_stack_HEAD2.svg)

### Using the commit number

If there is a particular commit you want to look back on and are not sure how far back it was, having to refer to it as `HEAD~n` could get extremely frustrating, especially since $n$ will continue to change as you work more on your project and make more commits. Luckily there is another way to refer to a particular commit, using its commit number.

When you enter `git commit -m "short descriptive message"` no output appears, but Git gives that commit a unique identifier, its commit number. By typing `git log` we can see ALL of the previous commits. Since that might be a lot of output to deal with, we will just ask for the last 3 commits using `git log -n 3`. The number after `-n` is how many commits you want displayed from the log.

Let's see what that output looks like for Dracula:

```
$ git log -n 3
commit 65f447e949e53edc0db08b93670d2e2b35fa6c22 (HEAD -> main)
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Mon Feb 28 11:47:17 2022 -0500

    Ignore data files and the results folder.

commit 0d4b23c688dbbf87cff3cfa9425a7dfd9a6e6280
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Mon Feb 28 11:42:41 2022 -0500

    Add concerns about effects of Mars' moons of Wolfman

commit 7cd0f422d373516d968c8fe4b90401dfee4d52a6
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Mon Feb 28 11:39:24 2022 -0500

    Start notes on Mars as a base
```

If you forget to include the `-n 3` flag and just type `git log` you can always jump to the end by pressing `q`. If you have been working on this project for a while, using the arrow keys to scroll down may take a prohibitively long time.

The first thing to notice is that **all** of your commit messages are here. This is a good reminder to write clear and concise messages because future you may be very grateful when trying to figure out where exactly past you introduced a particular issue.

The second thing to notice is the structure of each entry in the log: commit, Author, Date, message.
When you identify which commit you want to look at, the commit number is the unique 40 digit string of letters and numbers above it after the word "commit". In Dracula's repository, the unique identifier for the commit in which he "add[ed] concerns about effects of Mars' moons on Wolfman" is `0d4b23c688dbbf87cff3cfa9425a7dfd9a6e6280`.

Now that we have found the unique identifier of the commit we want to examine, we can use it with `git show`. Don't worry, you won't need to type all 40 digits, the first six will suffice.

```
$git show 0d4b23
commit 0d4b23c688dbbf87cff3cfa9425a7dfd9a6e6280
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Mon Feb 28 11:42:41 2022 -0500

    Add concerns about effects of Mars' moons of Wolfman

diff --git a/mars.txt b/mars.txt
index df0654a..315bf3a 100644
--- a/mars.txt
+++ b/mars.txt
@@ -1 +1,2 @@
 Cold and dry, but everything is my favorite color
+The two moons may be a problem for Wolfman
```

The commit number doesn't change as you update your repository.

![IMAGE: On the left, the same stack of 3 white boxes but now each is labeled with its six digit commit number. An arrow points from this stack to the stack On the right where the three white boxes have a new red box on top. The red box also has a commit number, but the commit numbers on the white boxes have not changed from the picture on the left.](./fig/Commit_number.svg)

### Quiz: finding a commit

The output from `git log -n 2`is:

```
$ git log -n 2
commit 65f447e949e53edc0db08b93670d2e2b35fa6c22 (HEAD -> main)
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Mon Feb 28 11:47:17 2022 -0500

    Ignore data files and the results folder.

commit 0d4b23c688dbbf87cff3cfa9425a7dfd9a6e6280
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Mon Feb 28 11:42:41 2022 -0500

    Add concerns about effects of Mars' moons of Wolfman
```

Which of the following commands would show you the *most recent* commit you made?

- [[X]] `git show HEAD`
- [[ ]] `git show HEAD~1`
- [[X]] `git show 65f447`
- [[ ]] `git show fa6c22`
***
<div class ="answer">
The *most recent* commit is the current `HEAD` and its commit number is `65f447`. Either of these commands will give the same output. The command `git show HEAD~1` will show you one checkpoint earlier in your work, while `git show fa6c22` may not show you anything since it is not the first six digits of a known commit number (and likely not the first six digits of any commit number).
</div>
***

<div class = "help">
The error you get from entering a non-existent commit number starts with the word "fatal."  The word may be scary, but, in this case, all it is saying is that it could not execute the command. You did not harm anything!
</div>

### Technical details for the intrigued

When you commit code to Git, it doesn't create a brand new copy of your files from scratch. Instead it records the differences between the version of each file that it already has stored, and the new version. You can think of it as the instructions for transforming the previous version of your repository into the new version.

![The three white boxes are shown with a large green arrow pointing from each box to the box above it. The top box is labeled "Last committed version of repository" and the arrow pointing to it from the middle box is labeled "HEAD." The second box is labeled "Next to last version of repository" and the arrow pointing to it from the box below is labeled "HEAD~1." The bottom box is labeled "Previous version of repository" and the arrow pointing to it is labeled "HEAD~2." There are three dots under the boxes, and another three dots under the arrows indicating that this pattern continues.](./fig/Commits_are_pointers.svg)

You could think of each commit not as a checkpoint, but the instructions on how to get to the next checkpoint. The entire repository can be built by following a series of instructions (commits) in order. Similarly you can determine the precise state of an earlier version by following the instructions backwards.

## Comparing files to prior commits

In order to have some more commits to compare, let's add a few more lines to our notes about Mars.

First add a line to `mars.txt` so that it reads:

```
Cold and dry, but everything is my favorite color
The two moons may be a problem for Wolfman
But the Mummy will appreciate the lack of humidity
```
Let's add and commit this change:

```
$ git add mars.txt
$ git commit -m "Discuss concerns about Mars' climate for Mummy"
```

Next let's add one more line to `mars.txt` so that it reads:
```
Cold and dry, but everything is my favorite color
The two moons may be a problem for Wolfman
But the Mummy will appreciate the lack of humidity
An ill-considered change
```
Notice that we did NOT add or commit that last change to `mars.txt`. When you are working on a large project, it is very easy to lose track in your head of when you last committed, or what changes you have made since. In this section we will see how to ask Git to tell us that information.

### Using `diff`

You might have noticed that `diff` was the first word after your commit message when you entered `git show HEAD`. The lines after that are **all** the changes that you made with that commit. When comparing earlier versions with the current version, you are usually only going to want to look at one file at  a time. By typing `git diff HEAD` you are asking to see all the differences between the current state of your tracked files and the most recently committed version. Let's give it a try:

```console
$git diff HEAD
diff --git a/mars.txt b/mars.txt
index b36abfd..93a3e13 100644
--- a/mars.txt
+++ b/mars.txt
@@ -1,3 +1,4 @@
 Cold and dry, but everything is my favorite color
 The two moons may be a problem for Wolfman
 But the Mummy will appreciate the lack of humidity
+An ill-considered change
```

<div class = 'options'>
Typing `git diff` will give you the same output as `git diff HEAD` because the Git's default is always to compare with `HEAD`.
</div>

There is a lot of information here, let's parse what each part means.

```
diff --git a/mars.txt b/mars.txt
index b36abfd..93a3e13 100644
--- a/mars.txt
+++ b/mars.txt
```
1. The first line tells us that Git is producing output similar to the Unix `diff` command comparing the old and new versions of the file.
2. The second line tells exactly which versions of the file Git is comparing; `b36abfd` and `93a3e13` are unique computer-generated labels for those versions.
3. The third and fourth lines once again show the name of the file being changed and assigns a symbol to each version. Lines that are in version a but not version b will be marked with a `-` and lines that are in version b but not version a will be marked with a '+'.

```
@@ -1,3 +1,4 @@
 Cold and dry, but everything is my favorite color
 The two moons may be a problem for Wolfman
 But the Mummy will appreciate the lack of humidity
+An ill-considered change
```

4. The next line, surrounded by `@@` on both sides, tells you what lines of code you are going to see next. This sequence `@@ -1,3 +1,4 @@` translates to: from version a (`-`) show lines 1 through 3 and from version b(`+`) show lines 1 through 4.

5. The remaining lines are the most interesting, they show us the actual differences and the lines on which they occur. In particular, the `+` marker in the first column shows that that line, "An ill-considered change" is in version b, but not version a.

6. If you changed code in multiple parts of your file, you will see several of these sections, called **chunks**, showing the changes you made.

### Comparing particular files or commits

When you enter `git diff` or `git diff HEAD`  your console will show you all of the differences between your current working directory and the most recent commit. But if you have made several changes in multiple files, the output may be very hard to parse. Your output will contain a `diff` section for each file that changed, and a chunk, starting with `@@` for each section of that file that changed. This could be a huge amount of output to sift through to find the changes you care about!

Helpfully, Git lets you ask for only the changes from a particular file. Let's add and change another file so we can see the power of this. Make sure you are in the planets directory, then enter:

```console
$ echo "Venus is too hot to be a suitable base" > venus.txt              # Add the line in quotes to the file venus.txt
$ git add venus.txt
```

Now `venus.txt` is being tracked by Git, but has not yet been committed to the repository. If we enter `git diff HEAD` now, we will see both the changes we have made to `venus.txt`, and to `mars.txt`.

To look at just the changes to one of them, we can enter `git diff HEAD venus.txt`:

```console
$git diff HEAD venus.txt
diff --git a/venus.txt b/venus.txt
index e69de29..73eca03 100644
--- a/venus.txt
+++ b/venus.txt
@@ -0,0 +1 @@
+Venus is too hot to be a suitable base
```

Now we can look at only the changes to `venus.txt`.

You might also want to look at earlier changes from previous commits. By replacing `HEAD` with either `HEAD~1` or the unique six digit identifier for the previous commit, we can compare the current version in our working directory to that earlier version:

```console
$git diff HEAD~1 mars.txt
diff --git a/mars.txt b/mars.txt
index 315bf3a..93a3e13 100644
--- a/mars.txt
+++ b/mars.txt
@@ -1,2 +1,4 @@
 Cold and dry, but everything is my favorite color
 The two moons may be a problem for Wolfman
+But the Mummy will appreciate the lack of humidity
+An ill-considered change
```

Neither of the last two lines, (starting with the `+`) were present in the `mars.txt` file two commits ago.


### Quiz: using `diff`

After working for a while, we might not remember where our last checkpoints were or what we have done since. What command should we enter to find out how the file `venus.txt` has changed since it was last committed?


[[git diff HEAD venus.txt]]
<script>
  let input = "@input".trim().toLowerCase();
  input == "git diff HEAD venus.txt" || input == "git diff venus.txt";
</script>
***
<div class= "answer">
Both `git diff HEAD venus.txt` and `git diff HEAD venus.txt` will show you the differences between the current working version of `venus.txt` and the last committed version. If you know the commit number of your last commit, you could also use that: `git diff "######" venus.txt`.


Omitting `venus.txt` will show you ALL changes that have been made to any file in the repository since the last commit.
</div>
***

The output from your previous command is below:

```console
diff --git a/venus.txt b/venus.txt
index 73eca03..4e274c9 100644
--- a/venus.txt
+++ b/venus.txt
@@ -1 +1,2 @@
 Venus is too hot to be a suitable base
+No moons on Venus will confuse Wolfman
```

What does this output tell you? Choose all of the the statements that the output tells you are true.

[( )] You already committed the comment about Venus's lack of moons.
[(X)] The current working version of `venus.txt` has two lines.
[(X)] The last committed version of `venus.txt` has one line.
[( )] No files other than `venus.txt` have been changed since the last commit.
***
<div class = "answer">
*You already committed the comment about Venus's lack of moons.* FALSE The output is showing the difference between the most recent commit and the current working version. If you had already committed the comment about Venus's lack of moons, that line would not be marked with `+`.

*The current working version of `venus.txt` has two lines.* TRUE The current working version of `venus.txt` contains all lines marked with a `+` as well as all lines that have no starting symbol.

*The last committed version of `venus.txt` has one line.* TRUE The last committed version contains all unmarked lines. If there were any lines marked with `-`, those would also be in the last committed version of `venus.txt`.

*No files other than `venus.txt` have been changed since the last* FALSE Because we only asked Git to tell us about differences in the `venus.txt` file, it didn't check for differences in other files. They could have been changed and that would not be reflected in the output.

</div>
***

## Undoing changes with Git

One big reason we save older versions of our work is so that we can go back to an earlier version if something we did doesn't work out.

### Changes not yet committed

Using the git checkout command, big warnings about including the file name so you don't lose things you didn't want to lose.

### Revert to an earlier version

Big warnings around this part!!

### Quiz: `checkout`

quiz!

## Additional Resources

The last section of the module content should be a list of additional resources, both ours and outside sources, including links to other modules that build on this content or are otherwise related.

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Module+Template%22)!

Remember to change the redcap link so that the module name is correct for this module!

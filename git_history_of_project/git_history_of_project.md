<!--

author:  Elizabeth Drellich
email:    drelliche@chop.edu
version:  1.0.1
module_template_version: 2.0.0
language: en
narrator: UK English Female
code_language: Git
topic: Version Control
title: Exploring the History of your Git Repository
comment:  This module will teach you how to look at past versions of your work on Git and compare your project with previous versions.
long_description: You know that version control is important. You know how to save your work to your Git repository. Now you are ready to look at and compare different versions of your work. In this module you will you will learn how to navigate through the commits you have made to Git. You will also learn how to compare current code with past code.

estimated_time: 30 minutes

@learning_objectives  
After completion of this module, learners will be able to:

- Identify and use the `HEAD` of a repository.
- Identify and use Git commit numbers.
- Compare versions of tracked files.

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Exploring the History of a Git Repository


<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:**
@estimated_time

**Pre-requisites**

To best learn from this module make sure that you:

* have Git configured on your computer,
* can view and edit `.txt` files, and
* can make changes to a Git repository using `add` and `commit` from a command line interface (CLI).


**Learning Objectives**

@learning_objectives

</div>

## Lesson Preparation

The purpose of this module is to learn how to explore the history of a Git repository that has already been created. We are going to download Dracula's repository in which he started documenting the pros and cons of moving with his friends to Mars.

Open up your command line interface and navigate to a place where you want to put a new repository. This might be your `Desktop` but it can really be anywhere on your computer you choose. Once you are in the location you want to put Dracula's repository, clone the repository from GitHub with this command:

```
$ git clone https://www.github.com/arcus/planets
```

<div class ="important">
The `$` at the beginning of the line is not part of the command. It symbolizes that the following code goes directly into the command line interface (CLI). Output and code that goes into a file (not directly into the CLI) will not start with a `$`.
</div>

This should be a very fast download. Now if you type `ls` within the repository directory, you should see a folder titled `planets`. Navigate into the this directory using `cd`; this is the directory we will be exploring throughout the module.

<div class = "warning">
If you are on a computer running Windows, make sure you are in the Git Bash application. The Command Prompt (cmd) will not recognize the commands we are using in this module.
</div>

<div class = "options">
If you are starting this module after following along with all of Dracula's code in the [Creating your Git Repository](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/git_creation_and_tracking/git_creation_and_tracking.md#1) module, you can follow along here in your own planets directory instead of downloading Dracula's repo.
</div>


## Seeing prior commits

Keeping track of all versions and being able to see and compare them is the entire point of using version control on a project you are working on alone. It is also a huge part of working on a project with others, whether you are collaborating currently or hope to share your work in the future.

Each time you `commit` to Git, you are marking the current state of your project as a checkpoint that you can return to. The records of these changes are referred to as [commits](https://swcarpentry.github.io/git-novice/reference.html#commit).


You are going to learn about two ways to refer to past commits:

- Using `HEAD`, which points to the last thing you were working on.
- Using the commit number assigned to a particular `commit`.

These will let you navigate and explore the previous versions of repositories.

![The Commit Stack: 3 flat white boxes, stacked on top of each other. The top box is labeled "last committed version of repository", the middle box is labeled "next to last version of repository" and the bottom is labeled "previous version of repository". Three dots below the lowest box indicate that this pattern continues.](media/commit_stack_git.svg)

### Using HEAD

The `HEAD` almost always refers to the most recently commit to your repository on your current **branch**. A branch is a version of the repository. Branches are usually created so that a single person can work on a particular issue in a larger project. For example a project might have branches `luisa_update_with_latest_figures` or `jameela_add_lit_review`. When the work on a branch is completed, the changes can be merged into the main branch - `main`.


Dracula's `planets` repository only has one branch, `main`, so that is what `HEAD` refers to. It won't include any changes that haven't been committed to the repository yet. You can see that most recent commit by entering `git show HEAD`.

```
$ git show HEAD
commit 024af1d5d311c5d1a737cca3fb13d1b62c2a29ed (HEAD -> main, origin/main)
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Wed Apr 6 13:17:26 2022 -0400

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

The last thing that Dracula committed to the planets repository was the `.gitignore` file in which he told Git to "Ignore data files and the results folder."

<div class = "care">
Sometimes a command will output many lines of code that may not be relevant to you. For example the `show` command will output not just the commit message, but also every single change that you made in that commit.

The more you see this type of output, the more comfortable you will get with extracting the information you need and ignoring the rest.
</div>

<div class = "important">
If the output of a command is longer than the number of lines your console displays, you can navigate that output using the down and up arrows on your keyboard, or press `Q` or `q` to **quit** the output and return to your command prompt.
</div>

Maybe you want to look one step further back into your work. By using `HEAD~n` you can look back n checkpoints in your repository. The `~` symbol is named "tilde" and pronounced "TIL-duh."

For example, to look back just one commit before `HEAD`, use `git show HEAD~1`. If instead you wanted to look back three checkpoints (two commits before `HEAD`) you would enter `git show HEAD~2`.

![The stack of 3 white flat boxes. Now the top box is labeled `HEAD`, the middle box `HEAD~1` and the bottom `HEAD~2`](media/commit_stack_head0.svg)

Using `HEAD` to refer to your commits can be great for looking at recent versions of your repository. But be careful, each time you commit to the repository, you are creating a new most-recent-version that is now the `HEAD` and every older version moves one layer down in the stack.

![On the left, the stack of 3 flat white boxes are labeled `HEAD`, `HEAD~1`,  and `HEAD~2`. An arrow points to a stack on the right made of the 3 white boxes with a 4th red box now on top. This red box is now the one labeled `HEAD` and the boxes below it are labeled, in order from top to bottom, `HEAD~1`, `HEAD~2`, `HEAD~3`, with all the white boxes having changed labels.](media/commit_stack_head1.svg)

<div class = "learnmore">
Git is a big pile of mixed metaphors, and in the case of `HEAD`, it is referencing the idea of a [recording head](https://en.wikipedia.org/wiki/Recording_head) which writes audio or video input to a tape.

`HEAD` is a "pointer," it doesn't contain any information of its own. `HEAD` points to the commit you are currently working from, and it is possible to change which commit `HEAD` is pointing to. Moving `HEAD` so that it points somewhere else can be useful when you are trying to go back to an earlier version of your work, but is outside the scope of this module.
</div>

### Using the commit number

If there is a particular commit you want to look back on and are not sure how far back it was, having to refer to it as `HEAD~n` could get extremely frustrating, especially since n will continue to change as you work more on your project and make more commits. Luckily there is another way to refer to a particular commit, using its **commit number**.

When you enter `git commit -m "short descriptive message"` no output appears, but Git gives that commit a unique identifier, its commit number. By typing `git log` we can see ALL of the previous commits. Since that might be a lot of output to deal with, we will just ask for the last 3 commits using `git log -n 3`. The number after `-n` is how many commits you want displayed from the log.

Let's see what that output looks like for Dracula:

```
$ git log -n 3
commit 024af1d5d311c5d1a737cca3fb13d1b62c2a29ed (HEAD -> main, origin/main)
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Wed Apr 6 13:17:26 2022 -0400

    Ignore data files and the results folder

commit 656471fa1f38c8b0b9a6a2fafdf3ba68610e61fa
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Wed Apr 6 13:15:24 2022 -0400

    Start files on Jupiter and Mercury

commit 1e587d25f619aa0aa10fce19b44e4e71503fa41e
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Wed Apr 6 13:13:21 2022 -0400

    Add concerns about effects of Mars' moons on Wolfman
```

Use the arrow keys to scroll down if this output is longer than the window you are working in. If that is the case, you can always quit the output by pressing `Q` or `q`. Entering `git log` without the `-n` flag will give you the list of every commit, so if a project has been in progress for a while, this can be a lot of output!

The first thing to notice is that your commit messages are here! This is a good reminder to write clear and concise messages because **future** you may be very grateful when trying to figure out where exactly **past** you introduced a particular issue.

The second thing to notice is the structure of each entry in the log: commit, Author, Date, message.
When you identify which commit you want to look at, the commit number is the 40 digit string of letters and numbers at the top of it after the word "commit". In Dracula's repository, the identifier for the commit in which he "add[ed] concerns about effects of Mars' moons on Wolfman" is `1e587d25f619aa0aa10fce19b44e4e71503fa41e`.

<div class = "learnmore">
**What is this number?**

We are used to seeing numbers in base 10, which are made up of ten digits. Commit numbers are in base 16, called [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal). In this number system, we use the 10 familiar digits `1,2,3,4,5,6,7,8,9` as well as the digits `a,b,c,d,e,` and `f` corresponding to 10,11,12,13,14, and 15 respectively in base 10.

The 40 digit commit number is created by putting the entire repository, along with some metadata, including the commit message and a timestamp, through a function called a **hash**. With $16^{40}$ different numbers (also called **hashes**) you can think of these number as unique!

If you are using the repo you created in an earlier module, your commits might have different commit numbers than the commit numbers in the examples. Be sure to use the commit number in YOUR log if it differs from Dracula's.
</div>

Now that we have found the identifier of the commit we want to examine, we can use it with `git show`. Don't worry, you won't need to type all 40 digits, the first six will suffice.

```
$ git show 1e587d
commit 1e587d25f619aa0aa10fce19b44e4e71503fa41e
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Wed Apr 6 13:13:21 2022 -0400

    Add concerns about effects of Mars' moons on Wolfman

diff --git a/mars.txt b/mars.txt
index df0654a..315bf3a 100644
--- a/mars.txt
+++ b/mars.txt
@@ -1 +1,2 @@
 Cold and dry, but everything is my favorite color
+The two moons may be a problem for Wolfman
```

Unlike `HEAD`, the commit number doesn't change or move as you update your repository.

![On the left is the stack of 3 boxes, each labeled with its six digit commit number. An arrow points from this stack to the stack on the right where the three white boxes have a red box on top. The red box also has a commit number.  The commit numbers on the white boxes have not changed from the picture on the left.](media/commit_numbers.svg)

### Quiz: finding a commit

The output from `git log -n 2` is:

```
$ git log -n 2
commit 024af1d5d311c5d1a737cca3fb13d1b62c2a29ed (HEAD -> main, origin/main)
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Wed Apr 6 13:17:26 2022 -0400

    Ignore data files and the results folder

commit 656471fa1f38c8b0b9a6a2fafdf3ba68610e61fa
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Wed Apr 6 13:15:24 2022 -0400

    Start files on Jupiter and Mercury
```

Which of the following commands would show you the **most recent** commit you made? Select all correct answers.

- [[X]] `git show HEAD`
- [[ ]] `git show HEAD~1`
- [[X]] `git show 024af1`
- [[ ]] `git show 2a29ed`
***
<div class ="answer">

As long as you didn't do anything fancy to move `HEAD`, the **most recent** commit is the current `HEAD`. Its commit number is `584977`. Since both refer to the same commit, you can use either.

The command `git show HEAD~1` will show you one checkpoint earlier in your work, while `git show 081cd9` will give you an error since `081cd9` it is not the **first** six digits of a known commit number.

</div>
***

<div class = "care">
The error you get from entering a non-existent commit number starts with the word "fatal."  The word may be scary, but, in this case, all it is saying is that it could not execute the command. You did not harm anything!
</div>

## Comparing files to prior commits

In order to have some more commits to compare, let's add a few more lines to Dracula's notes about Mars.

First add a line to `mars.txt` so that it reads:

```
Cold and dry, but everything is my favorite color
The two moons may be a problem for Wolfman
But the Mummy will appreciate the lack of humidity
```
Let's add and commit this change:

```
$ git add mars.txt
$ git commit -m "Discuss pros of Martian climate for Mummy"
```

Next let's add one more line to `mars.txt` so that it reads:

```
Cold and dry, but everything is my favorite color
The two moons may be a problem for Wolfman
But the Mummy will appreciate the lack of humidity
An ill-considered change
```

Notice that we did NOT add or commit that last change to `mars.txt`. When you are working on a large project, it is very easy to lose track in your mind of when you last committed, or what changes you have made since. In this section we will see how to ask Git to tell us that information.

<div class = "learnmore">
You can change things in the `planets` directory that you downloaded from GitHub!

Because these files now exist on your computer, you can change them and commit those changes. The author of the new commits will be you, not Vlad Dracula. You can use `git log` to see which of you made which commit.

This is a preview of how Git lets you work with collaborators to create a project together.
</div>

### Using `diff`

You might have noticed that `diff` was the first word after your commit message when you entered `git show HEAD`. The lines after that are **all** the changes that you made with that commit. When comparing earlier versions with the current version, you are usually only going to want to look at one file at  a time. By typing `git diff HEAD` you are asking to see all the differences between the current state of your tracked files and the most recently committed version. Let's give it a try:

```
$ git diff HEAD
diff --git a/mars.txt b/mars.txt
index b296810..7b7a6e9 100644
--- a/mars.txt
+++ b/mars.txt
@@ -1,3 +1,4 @@
 Cold and dry, but everything is my favorite color
 The two moons may be a problem for Wolfman
 But the Mummy will appreciate the lack of humidity
+An ill-considered change
```

There is a lot of information here, so we will go through what each of the parts means.


```
diff --git a/mars.txt b/mars.txt
```
1. The first line tells us that Git is producing output similar to the Unix `diff` command comparing the old and new versions of the file.

```
index b296810..7b7a6e9 100644
```

2. The second line tells exactly which versions of the file Git is comparing; `b296810` and `7b7a6e9` are the computer-generated labels for those versions.

```
--- a/mars.txt
+++ b/mars.txt
```

3. The third and fourth lines once again show the name of the file being changed and assigns a symbol to each version. Lines that are in version `a` but not version `b` will be marked with a `-` and lines that are in version `b` but not version `a` will be marked with a `+`.

```
@@ -1,3 +1,4 @@
```

4. The next line, surrounded by `@@` on both sides, tells you what lines of code you are going to see next. This sequence `-1,3 +1,4` translates to: from version a (`-`) show lines 1 through 3 and from version b (`+`) show lines 1 through 4.

```
Cold and dry, but everything is my favorite color
The two moons may be a problem for Wolfman
But the Mummy will appreciate the lack of humidity
+An ill-considered change
```

5. The remaining lines show us the text of both versions of the file. The `+` marker in the first column shows that that line, "An ill-considered change" is in version `b`, but not version `a`.

6. If you changed code in multiple parts of your file, you will see several of these sections, called **chunks**, showing the changes you made. Each chunk starts with a line surrounded by `@@` telling you which lines of the file come next.

### Comparing particular files and commits

When you enter `git diff HEAD`  your console will show you all of the differences between your current working directory and the the version at HEAD, which, unless you've intentionally moved it, will be the most recent commit. But if you have made several changes in multiple files, the output may be very hard to parse. Your output will contain a `diff` section for each file that changed, and a chunk, starting with `@@` for each section of that file that changed. This could be a huge amount of output to sift through to find the changes you care about!

Helpfully, Git lets you ask for only the changes from a particular file. Let's add and change another file so we can see the power of this. Make sure you are in the planets directory, then enter this code to start a new file `venus.txt` with one line in it:

```
$ echo "Venus is too hot to be a suitable base" > venus.txt
$ git add venus.txt
```

Now `venus.txt` is being tracked by Git, but has not yet been committed to the repository. The file `mars.txt` also has changes that have not yet been committed. If you enter `git diff HEAD` now you will see two `diff` sections, one for `mars.txt` and a second for `venus.txt`.

To look at just the changes to the file about Venus, we can enter `git diff HEAD venus.txt`:

```
$ git diff HEAD venus.txt
diff --git a/venus.txt b/venus.txt
new file mode 100644
index 0000000..73eca03
--- /dev/null
+++ b/venus.txt
@@ -0,0 +1 @@
+Venus is too hot to be a suitable base
```

Now we see only the changes to `venus.txt`. The line "new file mode" and the `/dev/null` line tell us that the file `venus.txt` didn't exist in the last commit.

You might also want to look at earlier changes from previous commits. By replacing `HEAD` with either `HEAD~1` or the unique six digit identifier for the previous commit, we can compare the current version in our working directory to that earlier version:

```
$ git diff HEAD~1 mars.txt
diff --git a/mars.txt b/mars.txt
index 315bf3a..7b7a6e9 100644
--- a/mars.txt
+++ b/mars.txt
@@ -1,2 +1,4 @@
 Cold and dry, but everything is my favorite color
 The two moons may be a problem for Wolfman
+But the Mummy will appreciate the lack of humidity
+An ill-considered change
```

Because they each start with `+`, we know neither of the last two lines of text were present in the `mars.txt` file two commits ago.

### Git compares files line by line

What happens when you change a line in your file?

Dracula originally committed the Jupiter file with the text

```
Jupiter is cheerful and full of energy
```

but if he goes back in and changes it to

```
Jupiter is cheerful but quite stormy
```

how will the `diff` display that change?

Instead of noting that only the last half of the line was changed, Git records this as deleting the line in the first version, and adding the line in the second version:

```
$ git diff HEAD jupiter.txt
diff --git a/jupiter.txt b/jupiter.txt
index 3030335..09c081c 100644
--- a/jupiter.txt
+++ b/jupiter.txt
@@ -1 +1 @@
-Jupiter is cheerful and full of energy
+Jupiter is cheerful but quite stormy
```

Even if the line several sentences long and you only changed a single character, Git records that as removing the old line and adding in the new one.

### Quiz: using `diff`

After working for a while, we might not remember where our last checkpoints were or what we have done since. What command should we enter to find out how the file `venus.txt` has changed since it was last committed?

[[git diff HEAD venus.txt]]
***
<div class= "answer">

The command `git diff HEAD venus.txt` will show you the differences between the current working version of `venus.txt` and the last committed version. If you happen to know that the 6-digit commit number of your last commit, you could also use that. For example if the commit number was `123456`, then `git diff 123456 venus.txt` would give you the same result.


Omitting `venus.txt` will show you ALL changes that have been made to any file in the repository since the last commit.

Omitting both the commit number and `HEAD`, i.e. entering `git diff venus.txt` will give you the same output in this instance, but we don't suggest using it because there are circumstances under which it will give a different output.

</div>
***

Suppose that output from your previous command is below:

```
diff --git a/venus.txt b/venus.txt
index 73eca03..4e274c9 100644
--- a/venus.txt
+++ b/venus.txt
@@ -1 +1,2 @@
 Venus is too hot to be a suitable base
+No moons on Venus will confuse Wolfman
```

What does this output tell you? Choose all of the the statements that the output tells you are true.

[[ ]] You already committed the comment about Venus's lack of moons.
[[X]] The current working version of `venus.txt` has two lines.
[[X]] The last committed version of `venus.txt` has one line.
[[ ]] No files other than `venus.txt` have been changed since the last commit.
***
<div class = "answer">

**You already committed the comment about Venus's lack of moons:** FALSE.  The output is showing the difference between the most recent commit and the current **working** version, which has indeed changed. If you had already committed the comment about Venus's lack of moons, that line would not be marked with `+`.

**The current working version of `venus.txt` has two lines:** TRUE.  The current working version of `venus.txt` contains all lines marked with a `+` as well as all lines that have no starting symbol.

**The last committed version of `venus.txt` has one line:** TRUE. The last committed version contains all unmarked lines. If there were any lines marked with `-`, those would also be in the last committed version of `venus.txt`.

**No files other than `venus.txt` have been changed since the last:** FALSE Because we only asked Git to tell us about differences in the `venus.txt` file, it didn't check for differences in other files. They could have been changed and that would not be reflected in the output.

You can conclude from this output that you must have committed, and then added the last line to `venus.txt`.

</div>
***


## Additional Resources

This module was based on examples from [Software Carpentry](https://software-carpentry.org)'s [lessons on using Git](https://swcarpentry.github.io/git-novice/). The story of Dracula and Wolfman's planned trip to Mars is borrowed from them, and more examples are available in the original lesson:

 - Lesson 5: [Exploring History](https://swcarpentry.github.io/git-novice/05-history/index.html)

<div class = "options">
If you have a repository with at least a few commits in it, such as the one created in the previous module in this series, you can use this module as a framework for exploring the history of that project.

You can also clone any public repository you find on [GitHub](https://github.com) using

```
$ git clone https://www.github.com/RepositoryOwner/RepositoryName
```

and explore how it was created! One repository with particularly good documentation is the [LiaScript project](https://github.com/LiaScript/LiaScript).
</div>

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Exploring+the+History+of+your+Git+Repository%22)!

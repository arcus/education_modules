<!--

author:   Elizabeth Drellich
email:    drelliche@chop.edu
version:  1.0.2
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Creating a Git Repository
comment:  Create a new Git repository and get started with version control.
long_description: If you have Git set up on your computer and are ready to start tracking your files, then this module is for you. This module will teach you how to create a Git repository, add files to it, update files in it, and keep track of those changes in a clear and organized manner.

@estimated_time: 1 hour

@learning_objectives

After completion of this module, learners will be able to:

- Create a Git repository
- Add and make changes to files in the repository
- Write short helpful descriptions, called "commit messages" to track the changes
- Use `.gitignore`
- Understand the `add` and `commit` workflow.


@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Creating a Git Repository

<div class = "overview">

## Overview
@comment

**Is this module right for me?**

@long_description

**Estimated time to completion:**

@estimated_time

**Pre-requisites**

Before you start this module, make sure you

* Know how to access a command line interface (CLI) on your computer.
* Have Git configured on your computer. If Git is not yet configured, see the module on setting up Git on a [Mac, Linux](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/git_setup_mac_and_linux/git_setup_mac_and_linux.md), or [Windows](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/git_setup_windows/git_setup_windows.md) machine.
* Can edit plain text `.txt` documents. A text editor is different from a word processor (i.e. Microsoft Word or Google Docs), in that text editors create files that consist only of text, no formatting at all. Here is a [tutorial on editing text files using `nano`](https://swcarpentry.github.io/shell-novice/03-create/#create-a-text-file), one of many text editors that you can access directly from the command line interface (CLI).

**Learning Objectives**

@learning_objectives
</div>

## Lesson Preparation

Open a new command line interface on your computer. All exercises in this module will be done in this interface.

<div class = "warning">
If you are on computer that uses the Windows operating system, make sure you are using the Git Bash application as your command line interface. The Command Prompt (cmd) will not recognize the commands we are using in this module.  Git Bash is part of the [Windows install of Git](https://git-scm.com/download/win).

![Git Bash logo](media/git_bash.jpeg)<!-- style = "max-width:200px;" border = 5px solid -->
</div>

If you are not sure if Git is configured on your computer, enter `git config user.name` into your command line interface and see if it returns your name. You can also check that it it has the correct email for you with `git config user.email`. If these are correct you are all ready to start the module!

If you need to get Git configured on your computer there is a module to help you get set up.  Depending on what computer you are using, use the instructions for a [Mac or Linux operating system](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/git_setup_mac_and_linux/git_setup_mac_and_linux.md#1), or a [Windows operating system](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/git_setup_windows/git_setup_windows.md#1)

## Creating a Repository

Usually you will use Git to track the progress of a project. As we learn about Git, we will use the story of Wolfman and Dracula who are investigating if it
is possible to send a planetary lander to Mars.

In the examples, we will see code as if it is written by Vlad Dracula. If you are practicing these steps as you move through this module, your name and email address will appear instead of Dracula's.

To copy the code in the examples, enter everything after the dollar sign "$" into the command line, and then press the enter or return key. If the command has any output, it will not start with a dollar sign, but a new line where you can type after a dollar sign will appear.

```console
$logname
vlad
$
```

The **code block** above tells you that when Dracula types `logname` and presses enter, the output is 'vlad', his username. Try entering `logname` in your own console. There will be other code in front of each `$` describing who and where you are. Since the stuff before the `$` will be different for everyone, it is customary to omit it from example code. We will also omit the `$` after the output.

### Initializing the repository

First, let's create a directory folder for our work. Depending on how your computer is organized the `Desktop` on Mac or Linux, or in `C` Drive on Windows machines may be good locations for the new directory folder, but you can put it wherever you like. Dracula's computer has a `Desktop` where he does his work.


```console
$ cd ~/Desktop
$ mkdir planets
$ cd planets
```
The `cd` command means **change directory**.  In our first command, we're changing directory to our home directory. (that's the `~`), and within that, to the directory called `Desktop`.  If you don't have this directory in your file system, you'll get an error.  That's okay -- just navigate to a different directory you'd like to work in (as long as that directory isn't within a Git repository).  The `mkdir` command tells the computer to **make** a **directory** with the name "planets." Once we have a `planets` directory, we use `cd` open that directory.

<div class = "help">
Getting an error message when you type these commands? If you are using the Windows operating system, you need to switch over to Git Bash.  Windows uses a different system of commands than other computers like Linux, Unix, and Mac, and Git Bash makes it possible for you to use the commands common to the other operating systems, even though you're on Windows.
</div>

Next we tell Git to make `planets` a [repository](https://swcarpentry.github.io/git-novice/reference.html#repository) (also called a **repo**)
-- a place where Git can store versions of our files:


```console
$ git init
```

<details>

<summary>What does this `hint` output mean? Click to learn more!</summary>

When you initialize your repository, Git will return the following output:

```
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint: 	git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint: 	git branch -m <name>
```
These instructions on how to change the name of your initial branch are part of GitHub's effort, as part of the larger programming community, to [replace programming terms associated with slavery](https://www.zdnet.com/article/github-to-replace-master-with-alternative-term-to-avoid-slavery-references/).

We will following this hint and changing the default name in the [next section](#Creating-the-`main`-branch)

</details>



It is important to note that `git init` will create a repository that
**includes subdirectories and their files** -- there is no need to create
separate repositories nested within the `planets` repository, whether
subdirectories are present from the beginning or added later. Also, note
that the creation of the `planets` directory and its initialization as a
repository are completely separate processes.

If we use `ls`, the **list** command, to show the directory's contents,
it appears to be empty:

```console
$ ls
```


Like many commands, `ls` can be modified using **flags**, very short bits of code that change some of the options on the command. If we add the `-a` flag to `ls`, we will be asking Git to list **all** files.
Now we can see that Git has created a hidden directory within `planets` called `.git`.  It didn't show up with just plain `ls`, but it shows up now that we use the `-a` flag.  This is because of the initial dot or period in the name of `.git`.

```console
$ ls -a

.	..	.git
```

Git uses this special subdirectory to store all the information about the project,
including all files and sub-directories located within the project's directory.
If we ever delete the `.git` subdirectory,
we will lose the project's history.

<div class = "learnmore">
What are the series of dots preceding `.git`?  The `.` (pronounced "dot") refers to the directory you are currently in, while `..` ("dot dot") refers to the parent of the directory you are currently in. Every directory automatically contains both `.` and `..` as things you can use as quick shorthand if you need to use them to navigate through the file structure.  What we're seeing here, then, is really a list of three things that stay hidden unless you specify that you want to see hidden things: (1)`.`, (2) `..`, and (3) `.git`
</div>

### Creating the `main` branch

The `main` branch is likely to be the default branch depending on your settings and version of Git. But just to be sure, we will change the default branch to be called `main`:

```console
$ git checkout -b main

Switched to a new branch 'main'
```

We can check that everything is set up correctly
by asking Git to tell us the **status** of our project:

```console
$ git status

On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

If you are using a different version of Git, the exact
wording of the output might be slightly different.

<div class ="learnmore">
You will see that the primary branch of some projects, particularly older projects, is called `master` instead of `main`. GitHub has joined the programming community in a concerted effort to [replace programming terms associated with slavery](https://www.zdnet.com/article/github-to-replace-master-with-alternative-term-to-avoid-slavery-references/).
</div>



### Quiz: `git init`

What command Dracula enter in the blank in order to create a new Git repository?

```console
$ cd ~/Desktop      # return to the Desktop directory
$ mkdir planets     # make the planets directory
$ cd planets        # go into the newly created planets directory
$ __________        # make the planets directory a Git repository

```
[[git init]]
***
<div class = "answer">

By initializing the Git repository inside the `planets` directory with the `git init` command, Git will track every file inside `planets`.

</div>
***


Along with tracking information about planets (the project we have already created),
Dracula would also like to track information about moons.
Consider this possible scenario: Dracula creates a `moons` project inside his `planets`
project with the following sequence of commands.  Here we've added comments, the text following the `#`, explaining what each command does.

```console
$ cd ~/Desktop   # return to Desktop directory
$ cd planets     # go into planets directory, which is already a Git repository
$ ls -a          # ensure the .git subdirectory is still present in the planets directory
$ mkdir moons    # make a subdirectory planets/moons
$ cd moons       # go into moons subdirectory
$ git init       # make the moons subdirectory a Git repository
$ ls -a          # ensure the .git subdirectory is present indicating we have created a new Git repository
```

Is the `git init` command, run inside the `moons` subdirectory, required for
tracking files stored in the `moons` subdirectory?

[( )] Yes, running `git init` inside the `moons` subdirectory is necessary.
[( )] It is not necessary to run `git init` inside `moons` but it can't hurt.
[(X)] No, `moons` was already tracked as a subdirectory of `planets` and running `git init` inside `moons` could interfere with version control.
***
<div class = "answer">

No. Dracula does not need to make the `moons` subdirectory a Git repository
because the `planets` repository will track all files, sub-directories, and
subdirectory files under the `planets` directory.  Thus, in order to track
all information about moons, Dracula only needed to add the `moons` subdirectory
to the `planets` directory.

Additionally, Git repositories can interfere with each other if they are "nested":
the outer repository will try to version-control
the inner repository. Therefore, it's best to create each new Git
repository in a separate directory. To be sure that there is no conflicting
repository in the directory, check the output of `git status`. If the output tells you that you are "Not [in] a git repository" then you are clear to create a new repository:

```console
$ git status

fatal:
Not a git repository (or any of the parent directories):
.git
```

If you get a different message, like the "On branch main" message we saw the first time we ran `git status` in the previous section, then you are already in a repository and should not initialize another one.

</div>
 ***

### Fixing a nested `init`

What if you forgot to check `git status` and accidentally created a repository nested in another repository?
You can fix this by removing the `.git` file from the inner repository. Take another look at Dracula's code from our last example:

```console
$ cd ~/Desktop   # return to Desktop directory
$ cd planets     # go into planets directory, which is already a Git repository
$ ls -a          # ensure the .git subdirectory is still present in the planets directory
$ mkdir moons    # make a subdirectory planets/moons
$ cd moons       # go into moons subdirectory
$ git init       # make the moons subdirectory a Git repository
$ ls -a          # ensure the .git subdirectory is present indicating we have created a new Git repository
```

Dracula has created two tracking files, `planets/.git` which he should keep, and `planets/moons/.git` which should be removed.

First he should navigate to the `planets directory`:

```console
$ cd ~/Desktop/planets
```
and then run:

```console
$ rm -rf moons/.git
```
<div class = "warning">
The `rm` command **removes** files, and can be very useful, but the `-rf` flag is very powerful and should used with great caution. The `r` stands for "recursive" and instructs the computer to remove all contents of the file and then remove the file itself.  The `f` is for "force" and means you will not be asked if you are sure you want to delete the files.

Dracula should be absolutely certain he wants to delete `moons/.git` before running this command.
</div>

<div class = "options">
Dracula could have navigated to `~/Desktop/planets/moons` and then run `rm -rf .git` which would have had exactly the same effect. However if you were to run `rm -rf .git` in the `planets` directory, you would lose the history of your project. For that reason he should use the file path `moons/.git` to be sure that only the correct file is removed.
</div>

## Tracking changes

Just like any system that can help back-up or save your work, Git will be most helpful if you use it regularly as you work. In this section we will teach you

 - **how** to make a record of your changes,

 - **where** those records are, and

 - **when** you should be recording that you changed things.

### Tell Git to track a file
Let's follow along with Dracula to add a file to the planets directory with notes about Mars.

First let's make sure we're still in the `planets` directory.
You can check what directory you are in with `pwd` which will show your **present working directory**.

If your present working directory isn't `planets`, use `cd` to navigate there.

Let's create a file called `mars.txt` that contains some notes
about the Red Planet's suitability as a base.
We'll use `nano` to edit the file;
you can use whatever editor you like.
In particular, this does not have to be the `core.editor` you set globally earlier. But remember, the bash command to create or edit a new file will depend on the editor you choose (it might not be `nano`). For a refresher on text editors, check out ["Which Editor?"](https://swcarpentry.github.io/shell-novice/03-create/) in [The Unix Shell lesson](https://swcarpentry.github.io/shell-novice/) by Software Carpentry.

```console
$ nano mars.txt
```

Type the text below into the `mars.txt` file:


```console
Cold and dry, but everything is my favorite color
```

<div class = "help">
Type `control X` or `Ctrl X` to exit `nano`. Your keyboard should have either a `control` or `Ctrl` key in the lower left and possibly other locations as well. When asked if you want to save changes, enter `Y` for yes. Then the "File Name to Write" field should be pre-filled with `mars.txt` so you can press `return` or `Enter`.

When you are in `nano`, you can also refer to the reminders of commands at the bottom of window. The `^` in these commands means `control` or `Ctrl`.
</div>

Let's first verify that the file was properly created by running the list command (`ls`):


```console
$ ls

mars.txt
```



`mars.txt` contains a single line.  The `cat` command will display the contents of the file:


```console
$ cat mars.txt

Cold and dry, but everything is my favorite color
```
The `cat` command is short for **concatenate** and can be used to display the contents of multiple files, one after another. Here we are only asking it for the contents of a single file.

If we check the status of our project again,
Git tells us that it's noticed the new file:

```console
$ git status

On branch main

No commits yet

Untracked files:
   (use "git add <file>..." to include in what will be committed)

  	mars.txt

nothing added to commit but untracked files present (use "git add" to track)
```

The "untracked files" message means that there's a file in the directory that Git isn't keeping track of.
We can tell Git to track a file using `git add`:


```console
$ git add mars.txt
```

and then use `git status` to check that the right thing happened:

```console
$ git status

On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file: mars.txt
```

Git now knows that it's supposed to keep track of `mars.txt`,
but it hasn't recorded these changes as a commit yet.
To get it to do that, we need to run one more command. Enter this into the console:

```console
$ git commit -m "Start notes on Mars as a base"
```
The console output will look like this, though your unique identifiers (f22b25e and 100644) may be different.

```console
[main (root-commit) f22b25e] Start notes on Mars as a base
 1 file changed, 1 insertion(+)
 create mode 100644 mars.txt
```

When we run `git commit`,
Git takes everything we have previously told it to save by using `git add`
and stores a copy permanently inside the special `.git` directory.
This permanent copy is called a **commit**
(or **revision**) and its short identifier is `f22b25e`. Your commit may have another identifier.

We use the `-m` flag (for "message")
to record a short, descriptive, and specific comment that will help us remember later on what we did and why.
If we just run `git commit` without the `-m` option,
Git will launch `nano` (or whatever other editor we configured as `core.editor`)
so that we can write a longer message.

<div class = "important">
**Good commit messages**

Commit messages start with a brief (less than 50 characters) statement in the present tense about the changes made in the commit. Generally, the message should complete the sentence "If applied, this commit will..."


If you want to go into more detail, add a blank line between the summary line and your additional notes. Use this additional space to explain why you made changes and/or what their impact will be.
</div>

If we run `git status` now it tells us everything is up to date.

```
$ git status

On branch main

nothing to commit, working directory clean
```

<div class= "care">
Even, and perhaps especially, those who use Git a lot can have trouble writing good commit messages. We are all just doing our best to document our work!

![XKCD Cartoon, the text of which reads "As a project drags on my Git commit messages get less and less informative."  The first message shown reads "Created main loop & timing control." By the 5th message it reads "more code" followed by messages including "Here have code," "AAAAAAAAA," "my hands are typing words" and finally "haaaaaaaaands."](media/git_commit_2x.png)
(Image used under a Creative Commons Attribution-NonCommercial 2.5 License.  Original post at https://xkcd.com/1296.)
</div>

### Keeping track of your changes

Now that Git is keeping track of the file `mars.txt`, we can keep a record of the changes we make to the file.

Each update to `mars.txt` will use that same `add` and `commit` pair of commands.

If we want to know what we've done recently,
we can ask Git to show us the project's history using `git log`:


```
$ git log
f22b25e3233b4645dabd0d81e651fe074bd8e73b
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Thu Aug 22 09:51:46 2013 -0400

    Start notes on Mars as a base
```

`git log` lists all commits  made to a repository in reverse chronological order.
The listing for each commit includes
the commit's full identifier
(which starts with the same characters as
the short identifier printed by the `git commit` command earlier),
the commit's author,
when it was created,
and the log message Git was given when the commit was created.

<div class = 'help'>
**Where Are My Changes?** If we run `ls` at this point, we will still see just one file called `mars.txt`. That's because Git saves information about files' history in the special `.git` directory mentioned earlier so that our filesystem doesn't become cluttered (and so that we can't accidentally edit or delete an old version).
</div>

Now suppose Dracula adds more information to the file.
(Again, we'll edit with `nano` and then `cat` the file to show its contents;
you may use a different editor, and don't need to `cat`.)

```
$ nano mars.txt
$ cat mars.txt

Cold and dry, but everything is my favorite color
The two moons may be a problem for Wolfman
```

When we run `git status` now,
it tells us that a file it already knows about has been modified:

```
$ git status

On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   mars.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

The last line is the key phrase:
"no changes added to commit".
We have changed this file,
but we haven't told Git we will want to track those changes
(which we do with `git add`)
nor have we recorded them (which we do with `git commit`).
So let's do that now. It is good practice to always review
our changes before recording them. We do this using `git diff`.
This shows us the differences between the current state
of the file and the most recently saved version:

```
$ git diff

diff --git a/mars.txt b/mars.txt
index df0654a..315bf3a 100644
--- a/mars.txt
+++ b/mars.txt
@@ -1 +1,2 @@
 Cold and dry, but everything is my favorite color
+The two moons may be a problem for Wolfman
```

<div class = 'care'>
The output is cryptic because it is meant for a computer, not a human.
It is actually a series of commands for tools like editors and `patch`
telling them how to reconstruct one file given the other. Nevertheless we can gain some useful information
if we break it down into pieces:

  1. The first line tells us that Git is comparing the old and new versions of the file `mars.txt`.
  2. The second line tells exactly which versions of the file Git is comparing; `df0654a` and `315bf3a` are unique computer-generated labels for those versions.
  3. The third and fourth lines once again show the name of the file being changed.
  4. The remaining lines are the most interesting, they show us the actual differences and the lines on which they occur. In particular, the `+` marker in the first column shows where we added a line.
</div>

<div class = 'warning'>
If we immediately commit this change using `git commit` what will happen?

Git won't commit because we didn't use `git add` first! Git will give you a message reminding you to use `git add`.

</div>


Let's try adding the file and then committing the changes:

```
$ git add mars.txt
$ git commit -m "Add concerns about effects of Mars' moons on Wolfman"

[main 34961b1] Add concerns about effects of Mars' moons on Wolfman
 1 file changed, 1 insertion(+)
```

Double check that everything worked by running `git status`:

```
$ git status

On branch main

nothing to commit, working directory clean
```
### Commiting changes to multiple files

Running the `git commit` command will create a record in `.git` of every file we have told Git to track using `git add`. For example Dracula might want to create files for other planets.

He uses `nano` to create a file `jupiter.txt` with contents:

```
Jupiter is cheerful and full of energy
```

Then he creates a file `mercury.txt` which reads:

```
Mercury is swift and unpredictable
```

Now Dracula has two new files, and can tell Git to track both of them.

```
$ git add jupiter.txt mercury.txt
```

This tells Git to track both `jupiter.txt` and `mercury.txt`, and is the same as first adding one, and then using `git add` again to add the other. You can add as many files as you want in a single line by simply typing their names one after another, separated by a space.

Now he can record them with a single commit:

```
$ git commit -m "Start files on Jupiter and Mercury."
```

If you have been following along with Dracula, use `git status` to check that both files have now been recorded!

### How often should you `commit`?

Just like any method of backing up or saving your work, the benefits of using Git for version control are only available if you regularly use them. In our example, we have been committing every time we add or change a line in a single file. That is going to be odious overkill for most projects.  

Often, when we're working in a project, we change several files in the course of a few minutes or hours of work.  For example, you might change the counts of research subjects in a couple of different places across two or three files related to a research project when you update the weekly numbers.  It's helpful to know that with git, you can change a few files in your repository, then use `git add` to include the changed files (as many as you want) you want to include in a commit, and then do a single commit which explains all of the changes as a whole.

- **Commit each chunk of changes** If you add a new section to a file, or change a certain item across multiple files, it is a good practice to commit those changes with a message describing them. If a commit message like `-m "add sections on atmosphere to planet files"` or `-m "reorder paragraphs on moons from smallest to largest moon"` accurately describes your changes, make sure you commit the changes so that you can find them again later!

- **Commit before making any changes that could break your code** If your code currently works are you intend to add something new that may break it, make sure you commit so that you will be able to revert to the working version if needed.

- **Commit regularly** Even if you are only making very small changes, don't forget to commit at regular intervals, like before you switch tasks or end your work day.

<div class="care">
These are our recommendations for how often to commit, but that doesn't mean we are always good at following them. We all do the best we can, and sometimes we still end up committing every few minutes, giving each the commit message `"update file.txt"`. It's not ideal, but it gets the changes recorded even if it will be harder to see what was done later.
</div>


### Quiz: `add` and `commit`

1. What sequence of commands would track the changes you made to `myFile.txt`?

  a. `$ git add myFile.txt`

  b. `$ git commit myFile.txt`

  c. `$ git add -m "my short, descriptive message"`

  d. `$ git commit -m "my short, descriptive message"`

[( )] First run a, then b
[(X)] First run a, then d
[( )] First run c, then b
[( )] First run c, then d
***
<div class = "answer">

You must run the `git add` to tell Git to stage `myFile.txt`, then you can commit the changes and leave your short, descriptive message. We will discuss how to think of these steps in the [Git workflow section](#understanding-the-git-workflow).

</div>
***

2. With each commit, we want to leave a short, descriptive, message describing the changes we make. Which of these would be the **best** commit message?

[( )] "updates"
[( )] "The Martian atmosphere is only 1% oxygen."
[( )] "add a line that the Martian atmosphere is only 1% oxygen"
[(X)] "add comments on Martian atmosphere"
***
<div class = "answer">

The commit message should describe what this commit does. If you want to know the line by line changes you should use the `diff` command. The purpose of the message is so that you know what you changed without having to read all the individual changes, which is especially helpful if you edited many lines or files.

</div>
***

## Telling Git not to track some files

What if we have files that we do not want Git to track for us, like backup files created by our editor or intermediate files created during data analysis?

<div class = "warning">
It is likely that you will eventually share your repository.  This could be sharing it privately with a team, or publicly through [GitHub](github.com). When you do, everything that Git is tracking will become visible to everyone with access to the repository.  If there is an API key, password, sensitive data, or anything that requires any level of secrecy, make sure you tell Git to ignore it as soon as you create the file.

Once information is committed and made public ("pushed" to GitHub), a record of it will persist even if you remove it in a later commit.
</div>

### Creating `.gitignore`

Let's create a few dummy files to practice ignoring:

```
$ mkdir results
$ touch a.dat b.dat c.dat results/a.out results/b.out
```

The `touch` command opens, saves, and closes the files without changing them. Since they didn't previously exist, `touch` is also creating them. Now if we check the status of our repository we see:

```
$ git status


On branch main
Untracked files:
 (use "git add <file>..." to include in what will be committed)

	a.dat
	b.dat
	c.dat
	results/

nothing added to commit but untracked files present (use "git add" to track)
```

In our scenario, these are files we don't want to track.  Putting these files under version control would be a waste of disk space. What's worse, having them all listed could distract us from changes that actually matter, so let's tell Git to ignore them.

We do this by creating a file in the root directory of our project called `.gitignore`.   That dot at the beginning is intentional!  The file must be named this exactly for `.gitignore` to work properly.  Each line in this file is a rule for a type of file Git should ignore. Use your favorite text editor to make `.gitignore` contain the two lines:

```
*.dat
results/
```

These patterns tell Git to ignore any file whose name ends in `.dat` and everything in the `results` directory. (If any of these files were already being tracked, Git would continue to track them.)

<div class = "learnmore">
There are many common file types that people frequently ask Git not to track. For example Mac users usually want Git to ignore `.DS_store`, which is an invisible file that gets created by opening a file in Finder. You can even start with [this collection of common configurations](https://gist.github.com/octocat/9257657) for `.gitignore`.
</div>

Once we have created the `.gitignore` file, the output of `git status` is much cleaner:

```
$ git status

On branch main
Untracked files:
 (use "git add <file>..." to include in what will be committed)

	.gitignore

nothing added to commit but untracked files present (use "git add" to track)
```

The only thing Git notices now is the newly-created `.gitignore` file. You might think we wouldn't want to track it, but if we share the repository, everyone we're sharing with will probably want to ignore the same things that we are ignoring.
Let's add and commit `.gitignore`:

```
$ git add .gitignore
$ git commit -m "Ignore data files and the results folder."
$ git status

On branch main

nothing to commit, working directory clean
```

As a bonus, using `.gitignore` helps us avoid accidentally adding files to the repository that we don't want to track:

```
$ git add a.dat

The following paths are ignored by one of your .gitignore files:

 a.dat

Use -f if you really want to add them.
```

If we really want to override our ignore settings,
we can use `git add -f` to force Git to add something. For example,
`git add -f a.dat`.

We can also always see the status of ignored files if we want:

```
$ git status --ignored

On branch main
Ignored files:
(use "git add -f <file>..." to include in what will be committed)

a.dat
b.dat
c.dat
results/

nothing to commit, working directory clean
```

<div class = "learnmore">
For more details on how to use `.gitignore` to include or exclude particular files or folders check out Software Carpentry's [lesson on Ignoring Things](https://swcarpentry.github.io/git-novice/06-ignore/index.html).
</div>

### Quiz: `.gitignore`

Why might you want to tell Git to NOT track a file? Check all that apply.

[[X]] The file contains secret information like passwords or API keys.
[[X]] The file contains intermediate data that can be recreated by running other code in your repository.
[[X]] The file is automatically generated by your computer and not actually part of your project.
***
<div class = "answer">

All of these are good reasons to include a file in `.gitignore`, but especially the first reason. Keeping secret information like passwords or API keys is essential.

</div>
***

## Understanding the Git workflow
![XKCD Cartoon. Person A: "This is Git. It tracks collaborative work on projects through a beautiful distributed graph theory tree model." Person B: "Cool. How do we use it?" Person A: "No idea. Just memorize these shell commands and type them to sync up. If you get errors, save your work elsewhere, delete the project, and download a fresh copy."](media/git_2x.png)

(Image used under a Creative Commons Attribution-NonCommercial 2.5 License.  Original post at https://xkcd.com/1597.)

There were a lot of steps to getting our changes saved in Git! You could memorize that sequence of steps, and that is what many people do. However you might remember them better if you understand what each is doing.


So far we have encountered files in three states:

- **Working Directory** The working directory refers to the files you are currently working on, regardless of whether Git is tracking them. When you first create a new file, it exists solely in your working directory.

- **Staged Files** When you use the `git add file.txt` command to tell Git to keep track of your file, the file is now staged. Git is paying attention to the file, and knows what is in it, but has not yet created a record of its current state.


- **Committed Files** When you commit using the `git commit -m "short description of changes"` command, every file that had been staged is now committed. In other words, a record of the file is saved and you will be able to come back and see that exact version later on if you wish.

As you work on your project, files will cycle through these different states. When you make a change to a file, that change is in your working directory until you restart the `add` and `commit` cycle.


**Is there a better way to think of this?** Lots of people have favorite metaphors for how Git works. Before checking out the selection on the next page, do you have any ideas for possible ways to understand the `add` and `commit` process in Git?

### A few metaphors for Git
Metaphors for Git abound, and no metaphor has been great enough to become the "standard" example. If you are looking for a good enough metaphor to help you understand what Git is, here are some to consider:

* A [poetry metaphor](https://www.youtube.com/watch?v=BCQHnlnPusY) video on YouTube ~14 minutes

* A [musical metaphor](https://www.youtube.com/watch?v=S9Do2p4PwtE) video on YouTube ~5 minutes

* A [metaphor about building a house](https://towardsdatascience.com/a-simple-story-to-explain-version-control-to-anyone-5ab4197cebbc) blog post

* A [metaphor about photo albums](https://www.freecodecamp.org/news/git-the-laymans-guide-to-understanding-the-core-concepts/) article

Remember a metaphor doesn't need to be perfect to be helpful. If you find or come up with one that helps you understand the workflow, use it!


### Quiz: Git workflow

What does the `git commit` command do?

 [( )] Stages files so that their current version can be recorded.
 [( )] Creates a record of the current version of all files in the repository.
 [(X)] Creates a record of the current version of all of the staged files in the repository.
***
<div class = "answer">

The `git commit` command will only create a record of the files that you have **already staged.**

There are options you can use to automatically stage all files. Entering `git commit -a` or `git commit --all` will automatically stage all files that Git knows about and then commit them. But it will not save any new files that Git doesn't yet know about.

</div>
***

## Additional Resources

This module was based on examples from three of [Software Carpentry](https://software-carpentry.org)'s [lessons on using Git](https://swcarpentry.github.io/git-novice/). The story of Dracula and Wolfman's planned trip to Mars is borrowed from them, and more examples are available in the original lessons:

 - Lesson 3: [Creating a Repository](https://swcarpentry.github.io/git-novice/03-create/index.html)
 - Lesson 4: [Tracking Changes](https://swcarpentry.github.io/git-novice/04-changes/index.html)
 - Lesson 6: [Ignoring Things](https://swcarpentry.github.io/git-novice/06-ignore/index.html)


## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Creating+your+Git+Repository%22)!

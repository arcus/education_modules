<!--

author:  Elizabeth Drellich
email:    drelliche@chop.edu
version:  1.0.0
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Using Git to Time Travel
comment:  This module will teach you how to restore past versions of your project.
long_description: You know how to explore the commit history of your project on Git, but what if you want to revert a file, or even the whole project, to an earlier version? This module will teach you how to do that.

estimated_time:

@learning_objectives  
After completion of this module, learners will be able to:

- a
- b
- c

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Returning to Earlier Versions of your Git Repository


<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:**
@estimated_time

**Pre-requisites**

This module is for you if:

* x
* y
* z


**Learning Objectives**

@learning_objectives

</div>

## Lesson Preparation

The purpose of this module is to learn how to explore the history of a Git repository that has already been created. We are going to download Dracula's repository in which he started documenting the pros and cons of moving with his friends to Mars. Open up your command line interface and type:

```
git clone https://www.github.com/arcus/planets
```

This should be a very fast download. Now if you type `ls` within the repository directory, you should see a folder titled `planets`. Navigate into the planets directory using `cd`. This is the directory we will be exploring throughout the module.

<div class = "warning">
If you are on a computer running Windows, make sure you are in the Git Bash application. The Command Prompt (cmd) will not recognize the commands we are using in this module, including `ls`.
</div>



## Undoing changes with Git

One big reason we save older versions of our work is so that we can go back to an earlier version if something we did doesn't work out. This is also why it is so important to commit your code regularly. You can't return a checkpoint in your work unless you marked it as a checkpoint in the first place!

The file `mars.txt` should now contain four lines:

```
Cold and dry, but everything is my favorite color
The two moons may be a problem for Wolfman
But the Mummy will appreciate the lack of humidity
An ill-considered change
```

Make sure to add and commit the most recent changes:

```
$ git add mars.txt
$ git commit -m "Reject Mars as a base"
```

Lastly let's add one more line at the beginning of `mars.txt` so that it reads:

```
Mars: Planet 4 from the sun
Cold and dry, but everything is my favorite color
The two moons may be a problem for Wolfman
But the Mummy will appreciate the lack of humidity
An ill-considered change
```

You can use `cat mars.txt` to check that all five lines are currently present in the file.

### Changes not yet committed

The command `git checkout` has a number of uses, one of which is to use it to return a file to the state it was after the last commit.

If you enter

```
$ git checkout HEAD mars.txt
```

the file on Mars will return to its last committed state. Let's check what it looks like after that command using `cat`:

```
$ cat mars.txt
Cold and dry, but everything is my favorite color
The two moons may be a problem for Wolfman
But the Mummy will appreciate the lack of humidity
An ill-considered change
```

The file is back to being only four lines long, and if we now check how it differs from the `HEAD` we see that it doesn't differ at all. The command `git diff HEAD mars.txt` has no output!

So what happened to that line about Mars being 4th from the sun? It is gone! Completely gone. It wasn't committed so Git never created a record of its existence. This can be extremely useful if, say, your code was working when you last committed and you just want to throw out all the changes you made since then.

### Committed changes

If you already committed the changes that you no longer want, you can go back to earlier checkpoints in your work too!

The same commit number that lets you see the differences between your current working version of a file and earlier versions will also work with the `checkout` command.

Recall that earlier in this module we investigated the following commit:

```
commit fe532b097861acb8bd3d7f221d6ee741249dc8f0
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Mon Mar 14 14:58:17 2022 -0400

    Add concerns about effects of Mars' moons on Wolfman
```

We have added two lines to `mars.txt` since that commit, which we can check using the `diff` command:

```
$ git diff fe532b mars.txt
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

To get rid of all of those changes, enter the commit number instead of `HEAD` after the `checkout` command:

```
$ git checkout fe532b mars.txt
```

Now use `cat` to examine the contents of `mars.txt`. It only contains the first two lines. You are now working with this version of `mars.txt`. What do you think will happen if you enter `git diff HEAD mars.txt`? When you think you know, enter that into your command line and see if you were right!

Don't forget to `add` and `commit` the "new" version of your file `mars.txt` just like you would do with any changes you made.

### Detached `HEAD`

<div class = "warning">
If you forget to specify which file you want to check out and instead enter `git checkout fe532b` you will get the following message:

```
Note: checking out 'fe532b'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

 git checkout -b <new-branch-name>

HEAD is now at 0d4b23 Add concerns about effects of Mars' moons of Wolfman
```

The "detached HEAD" is like "look, but don’t touch" here, so you shouldn’t make any changes in this state.

If you enjoyed the [Technical Details section](#technical_details_for_the_intrigued), you can think of the `git checkout HEAD` command as changing where the `HEAD` arrow points to.

After investigating your repo’s past state, reattach your `HEAD` with the command `git checkout main`.
</div>

### Quiz: `checkout`

Jennifer has made changes to the Python script that she has been working on for weeks, and the modifications she made this morning "broke" the script and it no longer runs. She has spent ~ 1hr trying to fix it, with no luck…
Luckily, she has been keeping track of her project’s versions using Git! Which commands below will let her recover the last committed version of her Python script called `data_cruncher.py`?

[[ ]] 1. `$ git checkout HEAD`
[[X]] 2. `$ git checkout HEAD data_cruncher.py`
[[ ]] 3. `$ git checkout HEAD~1 data_cruncher.py`
[[X]] 4. `$ git checkout <unique ID of last commit> data_cruncher.py`
[[?]] More than one answer can be correct.
***
<div class = "answer">
The `checkout` command can restore files from the repository, overwriting the files in your working directory, if used with a file name. Answers 2 and 4 both restore the latest version in the repository of the file `data_cruncher.py`. Answer 2 uses `HEAD` to indicate the latest, whereas answer 4 uses the unique ID of the last commit, which is what `HEAD` usually means.


Answer 3 gets the version of `data_cruncher.py` from the commit before `HEAD`, which is NOT what we wanted.


Answer 1 will result in a detached `HEAD`! Use `git checkout main` to reattach `HEAD` before you make any more changes.
</div>
***


## Additional Resources

This module was based on examples from [Software Carpentry](https://software-carpentry.org)'s [lessons on using Git](https://swcarpentry.github.io/git-novice/). The story of Dracula and Wolfman's planned trip to Mars is borrowed from them, and more examples are available in the original lesson:

 - Lesson 5: [Exploring History](https://swcarpentry.github.io/git-novice/05-history/index.html)

This module is also the fourth in a series of modules about Git. We suggest continuing with the next module in the series on [working with others in Git](link/goes/here) and the entire collection is available on the [module catalog](link/goes/here)

<div class = "options">
If you have a repository with at least a few commits in it, such as the one created in the previous module in this series, you can use this module as a framework for exploring the history of that project.

You can also clone any repository you find on [GitHub](https://github.com) using

```
git clone https://www.github.com/RepositoryOwner/RepositoryName
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

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Using+Git+to+Revert%22)!

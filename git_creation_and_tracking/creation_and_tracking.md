<!--

author:   Elizabeth Drellich
email:    drelliche@chop.edu
version:  0.0.1
language: en
narrator: UK English Female
title: Creating your Git Repository
comment:  Create a new Git repository and get started with version control.
long_description: You have heard that version control is important for reproducible research and are ready to start tracking your files. This module will teach you how to create a Git repository, add files to it, update files in it, and keep track of those changes in a clear and organized manner.

@learning_objectives

After completion of this module, learners will be able to:

- Create a Git repository
- Add and make changes to files in the repository
- Write short helpful descriptions to track the changes

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Creating your Git Repository

<div class = "overview">

## Overview
@comment

**Is this module right for me?**

@long_description

**Estimated time to completion:**

**Pre-requisites**

Before you start this module, make sure you have

* Configured Git *on your computer*. See [this module](https://education.arcus.chop.edu) to learn how.
* The ability to edit .txt documents. Click [here](https://swcarpentry.github.io/shell-novice/03-create/#create-a-text-file) for an introduction to editing text files using `nano`.

If you would prefer to work through this module on your own computer, you can find a module on Bash 101 [here](link to bash 101 module).

**Learning Objectives**

@learning_objectives
</div>

## Lesson Preparation

Here we include information about a virtual box/command line emulator learners can use to do exercises.

If you prefer to run these examples on your own machine, open a command line interface (CLI).

## Creating a Repository

Once Git is configured,
we can start using it.

We will continue with the story of Wolfman and Dracula who are investigating if it
is possible to send a planetary lander to Mars.

![motivatingexample](./fig/motivatingexample.png)
[Werewolf vs dracula](https://www.deviantart.com/b-maze/art/Werewolf-vs-Dracula-124893530)
by [b-maze](https://www.deviantart.com/b-maze) / [Deviant Art](https://www.deviantart.com/).
[Mars](https://en.wikipedia.org/wiki/File:OSIRIS_Mars_true_color.jpg) by European Space Agency /
[CC-BY-SA 3.0 IGO](https://creativecommons.org/licenses/by/3.0/deed.en).
[Pluto](https://commons.wikimedia.org/wiki/File:PIA19873-Pluto-NewHorizons-FlyingPastImage-20150714-transparent.png) /
Courtesy NASA/JPL-Caltech.
[Mummy](https://commons.wikimedia.org/wiki/File:Mummy_icon_-_Noun_Project_4070.svg)
&copy; Gilad Fried / [The Noun Project](https://thenounproject.com/) /
[CC BY 3.0](https://creativecommons.org/licenses/by/3.0/deed.en).
[Moon](https://commons.wikimedia.org/wiki/File:Lune_ico.png)
&copy; Luc Viatour / [https://lucnix.be](https://lucnix.be/) /
[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en).


### Initializing the repository

First, let's create a directory in `Desktop` folder for our work and then move into that directory:


```console
$ cd ~/Desktop
$ mkdir planets
$ cd planets
```

Then we tell Git to make `planets` a [repository]({{ page.root }}{% link reference.md %}#repository)
-- a place where Git can store versions of our files:


```console
$ git init
```


It is important to note that `git init` will create a repository that
includes subdirectories and their files---there is no need to create
separate repositories nested within the `planets` repository, whether
subdirectories are present from the beginning or added later. Also, note
that the creation of the `planets` directory and its initialization as a
repository are completely separate processes.

If we use `ls` to show the directory's contents,
it appears that nothing has changed:

```console
$ ls
```


But if we add the `-a` flag to show everything,
we can see that Git has created a hidden directory within `planets` called `.git`:

```console
$ ls -a

.	..	.git
```

Git uses this special subdirectory to store all the information about the project,
including all files and sub-directories located within the project's directory.
If we ever delete the `.git` subdirectory,
we will lose the project's history.

### Creating the  `main` branch

Next, we will change the default branch to be called `main`.
This might be the default branch depending on your settings and version
of git.
See the [setup episode](02-setup.md) for more information on this change.

```console
git checkout -b main

Switched to a new branch 'main'
```


We can check that everything is set up correctly
by asking Git to tell us the status of our project:

```console
$ git status

On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

If you are using a different version of `git`, the exact
wording of the output might be slightly different.

### Knowledge Check 1

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
By initializing the Git repository inside the planets directory, Git will track every file inside planets.
</div>
***


Along with tracking information about planets (the project we have already created),
Dracula would also like to track information about moons.
Despite Wolfman's concerns, Dracula creates a `moons` project inside his `planets`
project with the following sequence of commands:

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
repository in the directory, check the output of `git status`. If it looks
like the following, you are good to go to create a new repository as shown
above:

```console
$ git status

fatal:
Not a git repository (or any of the parent directories):
.git
```
 </div>
 ***

### Fixing a nested `init`

<div class = "help">
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
Dracula can do this by running `pwd` and getting the output:

```console
/Users/Dracula/Desktop/planets
```
before running:

```console
$ rm -rf moons/.git
```
</div>

## Tracking changes

 It might seem like *making* changes and *documenting* them are two different things, but the entire point of version control is to document every change you make!

### Tell Git to track a file
Let's follow along with Dracula to add a file to the planets directory with notes about Mars.

First let's make sure we're still in the right directory.
You should be in the `planets` directory.

```console
$ cd ~/Desktop/planets
```

Let's create a file called `mars.txt` that contains some notes
about the Red Planet's suitability as a base.
We'll use `nano` to edit the file;
you can use whatever editor you like.
In particular, this does not have to be the `core.editor` you set globally earlier. But remember, the bash command to create or edit a new file will depend on the editor you choose (it might not be `nano`). For a refresher on text editors, check out ["Which Editor?"](https://swcarpentry.github.io/shell-novice/03-create/) in [The Unix Shell](https://swcarpentry.github.io/shell-novice/) lesson.

```console
$ nano mars.txt
```

Type the text below into the `mars.txt` file:


```console
Cold and dry, but everything is my favorite color
```


Let's first verify that the file was properly created by running the list command (`ls`):


```console
$ ls

mars.txt
```



`mars.txt` contains a single line, which we can see by running `cat`:


```console
$ cat mars.txt

Cold and dry, but everything is my favorite color
```


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

	new file:   mars.txt
```

Git now knows that it's supposed to keep track of `mars.txt`,
but it hasn't recorded these changes as a commit yet.
To get it to do that, we need to run one more command. Enter this into the console:

```console
$ git commit -m "Start notes on Mars as a base"
```
The console output will look like this, though your unique identifiers (f22b25e and 100644) will be different.

```console
[main (root-commit) f22b25e] Start notes on Mars as a base
 1 file changed, 1 insertion(+)
 create mode 100644 mars.txt
```

When we run `git commit`,
Git takes everything we have told it to save by using `git add`
and stores a copy permanently inside the special `.git` directory.
This permanent copy is called a [commit]({{ page.root }}{% link reference.md %}#commit)
(or [revision]({{ page.root }}{% link reference.md %}#revision)) and its short identifier is `f22b25e`. Your commit may have another identifier.

We use the `-m` flag (for "message")
to record a short, descriptive, and specific comment that will help us remember later on what we did and why.
If we just run `git commit` without the `-m` option,
Git will launch `nano` (or whatever other editor we configured as `core.editor`)
so that we can write a longer message.

[Good commit messages][commit-messages] start with a brief (<50 characters) statement about the
changes made in the commit. Generally, the message should complete the sentence "If applied, this commit will" <commit message here>.
If you want to go into more detail, add a blank line between the summary line and your additional notes. Use this additional space to explain why you made changes and/or what their impact will be.

If we run `git status` now:

```
$ git status

On branch main

nothing to commit, working directory clean
```
it tells us everything is up to date.

### Keeping track of your changes

Now that Git is keeping track of the file `mars.txt` we can keep a record of the changes we make to the file.

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
Where Are My Changes?

If we run `ls` at this point, we will still see just one file called `mars.txt`.
That's because Git saves information about files' history
in the special `.git` directory mentioned earlier
so that our filesystem doesn't become cluttered
(and so that we can't accidentally edit or delete an old version).
<\div>

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
but we haven't told Git we will want to save those changes
(which we do with `git add`)
nor have we saved them (which we do with `git commit`).
So let's do that now. It is good practice to always review
our changes before saving them. We do this using `git diff`.
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

  1. The first line tells us that Git is producing output similar to the Unix `diff` command comparing the old and new versions of the file.
  2. The second line tells exactly which versions of the file Git is comparing; `df0654a` and `315bf3a` are unique computer-generated labels for those versions.
  3. The third and fourth lines once again show the name of the file being changed.
  4. The remaining lines are the most interesting, they show us the actual differences and the lines on which they occur. In particular, the `+` marker in the first column shows where we added a line.
</div>

<div class = 'warning'>
If we immediately commit this change using `git commit` what will happen?

```
$ git commit -m "Add concerns about effects of Mars' moons on Wolfman"

On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   mars.txt

no changes added to commit (use "git add" and/or "git commit -a")
```
Git won't commit because we didn't use `git add` first!
</div>


To make sure our changes are tracked we must use `git add` first:

```
$ git add mars.txt
$ git commit -m "Add concerns about effects of Mars' moons on Wolfman"

[main 34961b1] Add concerns about effects of Mars' moons on Wolfman
 1 file changed, 1 insertion(+)
```
To double check that everything worked, you can run `git status` see:

```
$ git status

On branch main

nothing to commit, working directory clean
```

### Knowledge Check 2
A quiz! One question on add/commit order, one question on good commit messages.

Which sequence of commands would track the changes you made to `myFile.txt`?
*figure out how to have options be

[( )] `$ git commit -m "my short, descriptive message"`
[(X)] `$ git add myFile.txt` then `$ git commit -m "my short, descriptive message"`
[( )] `$ git commit -m "my short, descriptive message"` then `$ git add myFile.txt`
[( )] `$ git add -m "my short, descriptive message"` then `$ git commit myFile.txt`

***
<div class = 'answer'>
You must run the `git add` command before you can commit. We will discuss what the difference is between these steps in the [next section](#understanding_the_git_workflow).
</div>
***

With each commit, we want to leave a short, descriptive, message describing the changes we make. Which of these would be the *best* commit message?

[( )] "updates"
[( )] "The Martian atmosphere is only 1% oxygen."
[( )] "add a line that the Martian atmosphere is only 1% oxygen"
[(X)] "add comments on Martian atmosphere"



***
<div class = "answer">
The commit message should describe what this commit does. If you want to know the line by line changes you should use the `diff` command. The purpose of the message is so that you know what you changed without having to read all the individual changes, which is especially helpful if you edited many lines or files.
</div>
***

### Understanding the Git workflow
 There were a lot of steps to getting our changes saved in Git! You could memorize that sequence of steps, but you will remember them better if you understand what each is doing.

#### Put stuff from swcarpentries here.
images, and words, and metaphors

### Knowledge Check 3
Another quiz! This one about figuring out why something wasn't staged or didn't change things.

### Telling Git not to track some files
Extra how-to without a quiz.

## Module Content

Note that liascript will create a new page at each level 1, 2, or 3 header, so to avoid a page with only a header and no content, include text after each header before the next.

Text after level 2 headers provides a good opportunity to give a sentence or two of overview, explain the structure of the coming content, and/or get preliminaries out of the way.

## Including Media


![A valuable image, and this is its alt text.](https://upload.wikimedia.org/wikipedia/commons/0/0f/Grosser_Panda.JPG "Here is a subtitle that will display beneath the image.")


You can link to images online with their url, or locally with the file path, e.g. `![image caption](media/my_image.png)`

If you want to provide several images in a gallery, just make a "paragraph" of image links and LiaScript will render it as a gallery:

![img1 alt text.](https://upload.wikimedia.org/wikipedia/commons/6/68/Ailuropoda_melanoleuca_%28Panda_g%C3%A9ant%29_-_445.jpg) ![img2 alt text.](https://upload.wikimedia.org/wikipedia/commons/2/2d/Panda_giganti_al_Giant_Panda_Breeding_Research_Base_Chengdu.jpg) ![img3 alt text.](https://upload.wikimedia.org/wikipedia/commons/1/12/BabyPandaAtSDZ.jpg)


!?[This video is hosted on youtube.](https://www.youtube.com/watch?v=iIAO4Htzn8M)

You can also embed local videos, just as with images: `!?[An embedded video.](vid/intro.mp4 "This is its subtitle")`

In theory, you should be able to embed just about anything. Read more [here](https://liascript.github.io/course/?https://raw.githubusercontent.com/LiaScript/docs/master/README.md#24).

You can also include movies, audio, and any other embedded content in galleries just by putting the links for them all in a paragraph.

## Including highlight boxes

Include special notes with different formatting. The style "important" is for important points and key ideas. For example:

<div class = "important">
Tip: It's generally much easier to make any necessary changes to the dataframe, such as mutating variables, before sending it to the plotting command.
</div>

The style "care" is for content related to compassion, self-care, and motivation. For example:

<div class = "care">
This is a topic with a tremendous amount of jargon, which can make resources you may find online hard to understand for folks new to the field. When that happens it's easy to feel like there's something wrong with you if you don't get it, but that's not the case! Those kinds of gatekeeping explanations are a failure on the part of the writer, not the learner.
</div>


The style "help" is for educational first aid --- "help I'm lost!" suggestions. For example:

<div class = "help">
Feeling overwhelmed? It takes a long time to learn git, so don't be disheartened if it doesn't click initially. Just focus on stage, commit, and push. Ignore the rest for now, until you've had a chance to practice just the stage-commit-push process several times.
</div>

The style "warning" alerts users to potential pitfalls. For example:

<div class = "warning">
A common mistake when using `filter` is to write = when you mean ==. Remember that = is for argument assignment, and == is for testing equality in conditions. If you get them mixed up, your code won't run!
</div>

The style "learnmore" alerts users resources for further learning, especially links to a more in-depth discussion of an issue that might be touched on only briefly in the module.

<div class = "learnmore">
To learn more about the theory behind ggplot2, read [Hadley Wickham's article, "A Layered Grammar of Graphics"](http://vita.had.co.nz/papers/layered-grammar.pdf)
</div>

The style "options" is for an aside to let learners know there's another possible approach. For example:

<div class = "options">
You could also skip setting up an OSF account completely and just use github to publish and share your research products, but many people prefer to have OSF links available.
</div>
or
<div class = "options">
To do this in R instead of python, see this other module.
</div>

There's an additional style of highlight, "answer", that is used in [quizzes](#quiz).

## Including math

I want to include a math statement here: $ 1 + \beta = 2 $

## Including code

Next comes some code. This code won't do anything (it's not interactive).

```r
# You only need to install it once
install.packages("ggplot2")

# You'll need to load the library anew for each R session
library("ggplot2")
```
You don't have to specify the programming language, but you can, and it should help you get appropriate syntax highlighting.

```python
print("This is python code")
```

It is possible to include interactive code, too! See [the Rextester template for LiaScript](https://github.com/LiaTemplates/Rextester).

## Quiz

Quizzes are just more markdown text, so if you want it to show up on its own page, put a new header before it. Otherwise you can include quiz questions at the end of a section, or even interspersed with the rest of your content.

Quizzes should connect directly to your learning objectives. Each quiz question should connect to one learning objective, and every learning objective should have at least one quiz question associated with it somewhere in the module.

Here is the first question. It's multiple choice.

[(X)] This answer is right
[( )] This is wrong
[( )] Also wrong
[[?]] Hint: Provide a hint here if you like. Hints are marked with the ?
[[?]] Hint: You can include as many hints as you want.

You can have questions with multiple correct answers. Select all of the following correct choices:

[[ ]] Not this one
[[X]] This is one of the correct ones
[[X]] Here's another correct one
[[ ]] This one is wrong, though
[[?]] Hint: Remember to select ALL of the correct choices.

True or False: This statement is NOT true. ;)

[( )] TRUE
[(X)] FALSE

Short answer/text response. Note that, without any additional script, to get it marked "correct" the learner has to enter it exactly as you do.

[[right answer]]
[[?]] Hint: The answer is "right answer"
***
<div class = "answer">
This is extra text that will show up after the learner clicks to have the correct answer revealed. It can be as long as you like, and allows any markdown formatting (you can embed pictures or videos, links, etc.).

Use `<div class = "answer">` to mark these sections with special styling, so that they're visually distinct from the rest of the quiz. The style for `"answer"` is defined in the css file.

For this context to show up automatically when the learner answers the question correctly or clicks to have the right answer revealed, it needs to be surrounded by `***` (at least three, but you can use more if you want a more visually distinct horizontal marker in your md file).
</div>
***

We can allow some flexibility in what we accept as correct answers for text by adding a little script after the answer, though. For the following, either "right answer" or "correct answer" (not case sensitive) will be accepted:

[[right answer]]
<script>
  let input = "@input".trim().toLowerCase();
  input == "right answer" || input == "correct answer";
</script>
***
<div class = "answer">
For this question, either "right answer" or "correct answer" (not case sensitive) counts as correct.
</div>
***

This question accepts any of several items from a list of possible correct answers. It is not case sensitive (that's the little `i` at the end of the regex).

[[this text will never show up if they type a right answer and click "Check", only if they click the checkmark button to reveal the answer]]
[[?]] Hint: The answers are like "item1", "item2", etc.
<script>
  let input = "@input".trim();
  /item1|item2|item3|item4/i.test(input);
</script>
***
<div class = "answer">
With flexible answers like this, it's definitely a good idea to include a follow-up to help the learner put their answer in context.

For example, if the question was "Name one or more colors" with acceptable answers including red, orange, yellow, green, blue, and purple, and they wrote "red, green, and the center of a black hole" that would be marked as correct because it contains at least one string from the acceptable list. Similarly, "hammered metal" would be marked as correct because it contains the string "red" ([you can prevent this if you want](https://www.w3schools.com/jsref/jsref_regexp_begin.asp)). On the other hand "teal, scarlet, indigo" would be marked wrong.

Reiterate what the correct answer or answers should be, and try to anticipate likely wrong answers so you can explain why they're not correct.
</div>
***

There are also questions that allow you to select from a drop down, but I don't know why that would be preferable over regular multiple choice. [Read more about quiz syntax here.](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md#quizzes)

Note that you can use any markdown formatting you want in quizzes, including bold, links, math, etc.

Surveys (ungraded questions)
---

You can ask questions with no graded answer as well. LiaScript calls these [surveys](https://liascript.github.io/course/?https://raw.githubusercontent.com/LiaScript/docs/master/README.md#111).

Here's an ungraded question with a text box three lines long:

[[___ ___ ___]]

Here's one that's just one line long:

[[___]]

Here's a multiple choice with no correct answer. What is your favorite Beatles album?

[(rev)] Revolver
[(wa)] The While Album
[(ar)] Abbey Road
[(sgtp)] Sgt. Pepper's Lonely Hearts Club Band

Here's a survey multiple choice that lets you select more than one response. Which Beatles albums do you love super hard?

[[rev]] Revolver
[[wa]] The While Album
[[ar]] Abbey Road
[[sgtp]] Sgt. Pepper's Lonely Hearts Club Band

Hints and follow-up explanations don't work for survey questions.


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

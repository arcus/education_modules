<!--

author:   Your Name
email:    email@chop.edu
version:  0.0.0
module_type: standard
module_template_version: 3.0.0
language: en
narrator: UK English Female

title: Module Title

comment:  This is a short, focused description of the module.

long_description: This is a longer description, which should be understandable for a lay audience. It will print under "Is this module right for me?" in the overview.

estimated_time_in_minutes: This is rough guess of how long it might take a learner to work through the module. It will print under "Estimated time to completion" in the overview. Valid values are any integer 1-60. 

r_file: If this module uses binder to host an interactive rmd file, include the bare name of that file here, for example: this\_r\_module. Note that rmds in the education_r_environment repo should be saved in a directory that matches the file name, like "this_r_module/this_r_module.rmd". When you use the r_lesson_prep macro, it will fill in the text from r_file to use as both the directory name and file name for this lesson's notebook. Use backslashes to escape underscores (e.g. this\_r\_module rather than this_r_module). 

@prerequisites
List any skills and knowledge needed to do this module here. When available, include links to resources, especially other modules we've made (to show learners where this falls within our catalog).

* one skill we have [another module for, linked here](https://education.arcus.chop.edu)
* some familiarity with [a topic](https://education.arcus.chop.edu)
* understanding of [one thing](https://education.arcus.chop.edu) and [another](https://education.arcus.chop.edu)

If relevant, you can include recommendations for somewhere else to start if the learner doesn't have these prereqs. For example: If you are brand new to R or python (or want a refresher) consider starting with [Intro to R](link) or [Intro to python](link) first and then coming back here.
@end

@learning_objectives  
After completion of this module, learners will be able to:

- identify key elements
- create a product
- do a task
- articulate the rationale for something
@end

import: https://raw.githubusercontent.com/arcus/education_modules/templates_update/_module_templates/module_macros.md
-->

# Module Title

@overview

## Instructions for authors

This is the template for **standard modules**. 
Use this template if at least 50% of the module content will be written in this file (even if adapted from other open source content) rather than embedded or linked to. 
If more than half of the content is embedded or linked to, then use the wrapper module template instead.

To see how to use this **standard module** template, you'll need to look at this file in its [raw format](https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/standard_module_template.md).
To see what it looks like rendered via LiaScript, [click here](https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/standard_module_template.md) or go to [https://liascript.github.io/](https://liascript.github.io/) and paste the link to the **raw** file into the box on that page and click "load course".
This template is **not** a great example of what a real module should look like, though. 

To see what real modules look like, see [our list of completed modules](https://arcus.github.io/education_modules/list_of_modules).
If this is your first time writing a module, be sure to check out our [contributors guide](https://github.com/arcus/education_modules/blob/main/CONTRIBUTING) before you get started.

Some important things to keep in mind:

- We use "macros" for a lot of our standardized text. For exmaple, the overview and feedback sections of each module are created by the `@overview` and `@feedback` macros, respectively. 

  * General use macros are in the [module macros file](https://github.com/arcus/education_modules/blob/main/_module_templates/module_macros.md). This includes macros to generate the overview and feedback sections, as well as general-purpose javascript such as the gifPreload macro. It also loads our icon kit and style sheet. This macro file should be imported in every module. 
  * Macros for hands-on code in R, Python, and SQL modules are available in `module_macros_r.md`, `module_macros_python.md`, and `module_macros_sql.md`, respectively. SQL tables are loaded with additional files. For more details, see the sections on including interactive code in this template.
  * For more information about our macros and instructions for writing new ones, see the [macros instructions](https://github.com/arcus/education_modules/blob/main/macros_instructions.md).

- The title is the only level-1 header in the document.
- We use the module title to collate feedback in our REDCap survey, so if the title is edited after learners have begun sending in feedback we'll lose the ability to quickly group feedback for this module. Avoid making changes to the title after publication.
- LiaScript will create a new page at each level 1, 2, or 3 header, so to avoid a page with only a header and no content, include text after each header before the next.
- We have a standardized naming convention and directory structure:
  * Folder and file names use lowercase and underscores (no dashes)
  * Main module directory folder name is identical to the name of the module content markdown file.
  * Images, videos, and other audio-visual assets are saved within a `media` folder within the module directory
- Learning objectives are a very important element of the module. 
  * Learning objectives should be clearly defined using strong, descriptive verbs. (See [Bloom's taxonomy](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/) for ideas.)
  * Every learning objective should be covered in the module content.
  * All major topics covered should be represented by a learning objective -- there should be no significant knowledge imparted that isn't specified in the learning objectives
- Headers should be informative and follow a sensible hierarchical structure (the TOC in the left margin should give a good overview of the content covered)
- Avoid unclear language: unexplained idioms or references, unexplained acronyms, unnecessary technical language.
- Unusual words, or words taking on a very specific meaning in context, should always be defined for the learner, either on the page (e.g. using footnotes) or with links to a definition/glossary.
- Provide pronunciation guides for any especially unusual words of particular importance (a common example is package names, such as dplyr)
- Avoid unnecessarily gendered language (e.g. uses "they" singular rather than "he or she" for an unknown person).
- Use informative link text (e.g. instead of "To learn more about python, click [here](www.example.com)", say "Read this article to [learn more about python](www.example.com)."
- Try to write in short, digestible pieces --- avoid long paragraphs and break long sections up with sub-headers

### How to use the YAML header

We store a lot of important information in the YAML header section at the top of each module. Part of the module Quality Assurance (QA) process is checking that everything is correctly encoded in the YAML. 

The YAML for a **standard module** should include the following elements:
  * author name
  * email
  * module version number of at least 1.0.0 if first public version or if this is an update then an [appropriately incremented version number](https://github.com/arcus/education_modules/blob/main/versioning_guidelines.md)
  * module_type should be standard
  * module_template_version number is up to date with the current standard module template (this document) -- if not, the module should be brought in line with any changes that have occurred to the module template before continuing with QA
  * language
  * narrator
  * comment appropriately filled out (see instructions in YAML)
  * long_description appropriately filled out (see instructions in YAML)
  * estimated_time_in_minutes appropriately filled out (see instructions in YAML)
  * r_file appropriately filled out, if this module uses binder for an interactive rmd file (see instructions in YAML)
  * prerequisites appropriately filled out (see instructions in YAML)
  * learning_objectives appropriately filled out (see instructions in YAML)
  * import link provided to the macros module (`import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/module_macros.md`). Note that this imports all the macros needed for our modules, as well as the style sheet and javascript kit for our icons. 

### Tips for writing

When you're ready to start writing a new module:

1. Clone the education_modules repo if you don't already have it. Start a new git branch for your module. 
2. Open this template in a text editor like VSCode, and then use "save as" to save it in a new directory and with a filename that conveys the point of the module (e.g. "r_logistic_regression/r_logistic_regression.md"). You may find it helpful to have the examples of highlight boxes and quiz questions in this template that you can quickly copy-paste as you write.
3. Create a new empty subfolder in your module directory called "media". If you include images in your module, store them here.
4. Open up the **standard module** QA template (in the .github/ISSUE_TEMPLATE directory) as a reference, maybe keep it open side-by-side with your module draft.
5. You can use the LiaScript preview extension in VSCode to see what your rendered module will look like, or generate it from https://liascript.github.io/ after pushing your changes to GitHub (while your still drafting, remember that you'll need to link to your raw md file on your branch, since it won't be available yet on main).


## Lesson Preparation: RStudio

If your lesson includes R code examples hosted in binder from the repo https://github.com/arcus/education_r_environment, then you'll need to load the R macros by adding the following `import` statement to the YAML header of your module:

```
import: https://raw.githubusercontent.com/arcus/education_modules/templates_update/_module_templates/module_macros_r.md
```

You can then insert the following macro, which includes instructions for opening up the relevant rmd document, in your Lesson Preparation section:

@lesson_prep_r

Note that you should have `r_file` filled out in the YAML header. 

## Lesson Preparation: Interactive Python

If your lesson includes interactive python code in sagemath cells, then you'll need to load the Python macros by adding the following `import` statement to the YAML header of your module: 

```
import: https://raw.githubusercontent.com/arcus/education_modules/templates_update/_module_templates/module_macros_python.md
```

You can then insert the following macro, which includes instructions and an example interactive code block, in your Lesson Preparation section:

@lesson_prep_python

## Lesson Preparation: SQL

If your lesson includes interactive SQL code, you'll need to load the SQL macros. Each table is generated, row by row, in the macros for that lesson, so to avoid loading large macros unnecessarily, there are several different SQL macro modules available:

 - `module_macros_sql` is required for any module with interactive SQL
 - `module_macros_sql_table_allergies` loads the allergies table
 - `module_macros_sql_table_patients` loads the patients table
 - `module_macros_sql_table_observations` loads the observations table

Note that very small tables (just a few rows) can be constructed right in the YAML header for the module that uses them. Any larger tables, or tables that need to be re-used across different modules, should be created in separate table macro modules, though.

To use SQL macros (including tables), add the relevant `import` statements to your module's YAML header. For example: 

```
import: https://raw.githubusercontent.com/arcus/education_modules/templates_update/_module_templates/module_macros_sql.md
import: https://raw.githubusercontent.com/arcus/education_modules/templates_update/_module_templates/module_macros_sql_table_patients.md
```

To insert text providing a brief refresher on SQL, including our style guide and an example interactive code block, use the following macro in your Lesson Preparation section:

@lesson_prep_sql

## Including Media

This section includes examples of embedded media. 

Please note, we have guidelines in place to help keep our modules as accessible as possible, including **requirements for alt text for images and transcripts for audio**. Review our requirements for media in the relevant QA template saved in the .github/ISSUE_TEMPLATE directory. 

Important visuals (in video, image, or gif) should always be described in the audio or in accompanying text.

  - For example, in a screencast, instead of just, "And then click here," provide description that could help scaffold someone without visual access like, "And then click on the button that says 'Run' in the top-right corner of the screen". Be sure to make use of text cues when available (e.g. button labels), not just visual signals like color or location.
  - When important content is conveyed in a visual, describe the key elements. For example, "Running this query produces the table below. It displays the first 5 rows by default, and columns for ID, encounter ID, diagnosis, and outcome."
  - When including a data visualization, describe important features, such as both axis labels and visible trends in the data. For example, "Here's a scatterplot showing number of encounters on the y-axis and age on the x-axis. All 183 patients from our sample are represented here, and it looks like a weak positive trend, with older patients being more likely to have had more encounters. There are a few important outliers, though, such as this patient at about 6 months old with more than 20 encounters already."
  - When visual information is repeated with minimal changes, it's fine to indicate that without providing a full description again. For example, "And here's the updated table, filtered to only show patients who have been seen in the last 2 years."
  - When important visual information in a video is too complex to include sufficient audio description (i.e. it would slow the content down so much as to impair its utility), an alternative video file should be provided with audio descriptions included.

Here are several examples of embedded media:  

![A valuable image, and this is its alt text.](https://upload.wikimedia.org/wikipedia/commons/0/0f/Grosser_Panda.JPG "Here is a subtitle that will display beneath the image.")

You can change things like the size of the image two ways. 

You can add a comment with additional html after the markdown:

![RStudio as shown in the cloud platform Binder.](media/binder_rstudio.png)<!--
style = "border: 1px solid rgb(var(--color-highlight)); max-width: 800px;"-->

Or you can use html to specify the whole embedded image:

<img src="https://github.com/arcus/education_r_environment/blob/main/media/binder_rstudio.png?raw=true" alt="RStudio as shown in the cloud platform Binder." style = "border: 1px solid rgb(var(--color-highlight)); max-width: 800px;">

You can link to images online with their url, or locally with the file path, e.g. `![This is the alt text.](media/my_image.png)`

If you want to provide several images in a gallery, just make a "paragraph" of image links and LiaScript will render it as a gallery:

![img1 alt text.](https://upload.wikimedia.org/wikipedia/commons/6/68/Ailuropoda_melanoleuca_%28Panda_g%C3%A9ant%29_-_445.jpg) ![img2 alt text.](https://upload.wikimedia.org/wikipedia/commons/2/2d/Panda_giganti_al_Giant_Panda_Breeding_Research_Base_Chengdu.jpg) ![img3 alt text.](https://upload.wikimedia.org/wikipedia/commons/1/12/BabyPandaAtSDZ.jpg)

!?[This video is hosted on youtube.](https://www.youtube.com/watch?v=iIAO4Htzn8M)

You can also embed local videos, just as with images: `!?[An embedded video.](media/intro.mp4 "This is its subtitle")`

## Including highlight boxes

Include special notes with different formatting.

Note: There's an additional style of highlight not listed here, "answer", that is used in quizzes.

### behind-the-scenes

The style "behind-the-scenes" is for giving a little more technical detail about how something does what it does.
It has a gears icon and always begins with the text "Behind the scenes".
For example:

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

The commit number is a hash and associated details

</div>

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

In R the `<-` and `=` can both be used for assignment because...

</div>

### care

The style "care" is for content related to compassion, self-care, and motivation. For more technical help or troubleshooting, use "help" instead.
It has a hand-holding-heart icon and always begins with the text "A little encouragement..."
For example:

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

This is a topic with a tremendous amount of jargon, which can make resources you may find online hard to understand for folks new to the field. When that happens it's easy to feel like there's something wrong with you if you don't get it, but that's not the case! Those kinds of gatekeeping explanations are a failure on the part of the writer, not the learner.

</div>

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Feeling overwhelmed? It takes a long time to learn git, so don't be disheartened if it doesn't click initially. Just focus on stage, commit, and push. Ignore the rest for now, until you've had a chance to practice just the stage-commit-push process several times.

</div>

### cool-fact

The style "cool-fact" is for any cool fact that really doesn't fit into any of our other categories.
It has a brain icon and always begins with the text "Did you know?"
For example:

<div class = "cool-fact">
<b style="color: rgb(var(--color-highlight));">Did you know?</b><br>

Functions like this are sometimes called "syntactic sugar" because they don't change anything about how the code runs, they just make it easier for humans to read, the way that sugar makes food sweeter without adding any nutrition.

</div>


<div class = "cool-fact">
<b style="color: rgb(var(--color-highlight));">Did you know?</b><br>

This is a box showing how images work in a highlight box.

![Carebear team.](https://media.giphy.com/media/W256ghnG9iV8I/giphy.gif)


</div>

### external-resource

The style "external-resource" is specifically for wrapper modules, for linking to the external resource, as a way to draw attention to the fact that we're sending them out of the module and then they should come back. This is different from learn-more boxes we use in standard modules. 
It has a arrow-pointing-out-of-a-box icon and always begins with the text "External Content".
For example:

<div class = "external-resource">
<b style="color: rgb(var(--color-highlight));">External Content</b><br>

Next, complete the [Docker 101 tutorial](https://www.docker.com/101-tutorial/), which can be done either on your computer or in the cloud. 

Work through the whole tutorial, then return here to finish this module.

</div>

### gratitude

The style "gratitude" is for thanking authors of original sources we're using or adapting for our modules. There should always be a gratitude box for each external source linked in a wrapper module, but it's also something we will use in some standard modules when we adapt material (e.g. from carpentries lessons).
It has a heart icon and always begins with the text "Thank you!".
For example:

<div class = "gratitude">
<b style="color: rgb(var(--color-highlight));">Thank you!</b><br>

Material for this module was adapted, with permission, from [Stephan Kadauke's R for Clinical Data](https://skadauke.github.io/intro-to-r-for-clinicians-chop/) workshop materials. We owe special thanks to Dr. Kadauke as well as the R User Group at Children's Hospital of Philadelphia for their generosity in sharing these materials.

</div>

### help

The style "help" is for troubleshooting help, common errors, and specific technical problems. If you want to emphasize a very serious potential problem, use "warning" instead. For support that is more psycho/emotional or meta-learning in nature, use "care" instead.
It has a circle-question icon and always begins with the text "Troubleshooting help".
For example:

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

A common mistake when using `filter` is to write = when you mean ==. Remember that = is for argument assignment, and == is for testing equality in conditions. If you get them mixed up, your code won't run!

</div>

### history

The style "history" is for more historical context about how/when/why something came to be the way it currently is.
It has a clock-rotate-left icon and always begins with the text "Historical context".
For example:

<div class = "history">
<b style="color: rgb(var(--color-highlight));">Historical context</b><br>

The reason this command is named grep is...

</div>

<div class = "history">
<b style="color: rgb(var(--color-highlight));">Historical context</b><br>

The first README file was from 1971, etc.

</div>


### important

The style "important" is for important points and key ideas.
It has a star icon and always begins with the text "Important note".
For example:

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

It's generally much easier to make any necessary changes to the dataframe, such as mutating variables, before sending it to the plotting command.

</div>

### learn-more

The style "learn-more" alerts users resources for further learning, especially links to a more in-depth discussion of an issue that might be touched on only briefly in the module. It can link to outside sources, or other modules by us.
It has a book icon and always begins with the text "Learning connection".
For example:

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To learn more about the theory behind ggplot2, read [Hadley Wickham's article, "A Layered Grammar of Graphics"](http://vita.had.co.nz/papers/layered-grammar.pdf).

</div>


<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To do this in R instead of python, see [this other module](example.com).

</div>


### options

The style "options" is for an aside to let learners know there's another possible approach. This is for short explanations rather than linked resources; to link to another approach (e.g. here's a tutorial for another way to do this), use "learn-more" instead.
It has a left-right arrow icon and always begins with the text "Another option".
For example:

<div class = "options">
<b style="color: rgb(var(--color-highlight));">Another option</b><br>

You could also skip setting up an OSF account completely and just use github to publish and share your research products, but many people prefer to have OSF links available.

</div>

<div class = "options">
<b style="color: rgb(var(--color-highlight));">Another option</b><br>

You can run this in the cloud or download all of the files locally and run it on your computer. If you run it on your computer, be sure to make note of which directory you save the files in and update your working directory accordingly.

</div>

### version-update

The style "version-update" is for alerting learners to changes to a module.
It has a pencil icon and always begins with the text "Changes to this module".
For example:

<div class = "version-update">
<b style="color: rgb(var(--color-highlight));">Changes to this module</b><br>

We're constantly improving our materials, and this module has had recent changes. Specifically, we added a new section at the end explaining how to protect your API token when using git and GitHub for your code.

If you like, you can still access the [previous version of this module](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/a4ea7a7f1f9264dabe952b68941fc9f0f656c9fc/using_redcap_api/using_redcap_api.md). 

</div>

### warning

The style "warning" alerts users to potential pitfalls, and should be reserved for serious problems only. For less serious problems, use "help" instead.
It has a ! triangle icon and always begins with the text "Warning!".
For example:

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

Double check your working directory before running this code. If you're in the wrong directory, you risk overwriting your files and losing all of your work with no way to recover it.

</div>

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

Files uploaded to this account will be **publicly visible**. Be very careful not to upload anything with sensitive information like passwords or private data.

</div>

## Including math

Surround inline math statements with `$`: $ 1 + \beta = 2 $

## Including tables

If you wish to print a table, you can use markdown table formatting. 

Note that LiaScript has defaults that will allow users to toggle tables of data between table format and a plot of the data --- if you don't want to allow that functionality, you need to set the data-type to none. For example:

<!-- data-type="none" class="tight-table" style="font-size:80%"-->
| subj_id  | street_address  | city  | state   | zip  | date_start  | date_end   |
| :--------- | :--------- | :--------- | :--------- | :--------- | :--------- | :--------- |
| 11234   | 123 Main Street   | Smithtown    | PA  | 19000    | 2022-01-01   | `NULL`    |
| 11234   | 123 Oak Lane   | Old Towne    | PA  | 18000   | 2000-01-01    | 2021-12-31    |
| 93452   | 123 Green Blvd  | Kirby    | TN  | 37000    | 2020-05-01    | `NULL`   |


For more information about using tables in LiaScript, see the [tables section of the LiaScript documentation](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md#tables).

## Including non-interactive code

Include inline code with single backticks: `library(ggplot2)`. 

Make code blocks with at least three backticks:

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

## Including interactive coding exercises

We use three main approaches for interactive coding exercises: 

- We can link to interactive notebooks hosted on binder (see example notebooks in https://github.com/arcus/education_r_environment). This is our approach for most R modules, for example: https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_introduction/r_basics_introduction.md 
- We can have interactive coding cells in modules themselves using sagemath. This is our approach for most python modules, for example: https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_writing_python_code/python_basics_writing_python_code.md 
- We can also have interactive coding cells in modules using AlaSQL, which is our approach for SQL modules, for example: https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/sql_basics/sql_basics.md

We don't have a way to include interactive code for git or bash. For those modules, we just instruct learners to work on their own machines.

## Quizzes (automatically graded questions)

We use quizzes for [formative assessment](https://carpentries.github.io/instructor-training/aio.html#using-formative-assessment-to-support-memory-consolidation). There is no point value or grading, and students are allowed to retry quizzes as many times as they like until they get the right answer. The goal is to provide learners an opportunity to check their own understanding. 

Quizzes should connect directly to your learning objectives. Each quiz question should connect to one learning objective, and every learning objective should have at least one quiz question associated with it somewhere in the module. Learners should be able to answer all the questions based on the content within the module alone; they should not need to have read or consulted any of the linked learn-more resources. 

Quizzes should always be navigable from the sidebar, meaning they should be labeled with a level 2 or 3 header. If there is only one quiz in the module, it should be labelled as "Quiz". If there is more than one each header should be structured as "Quiz: label" where "label" is a short (ideally 1-2 words) description of the content covered in the question(s). E.g., "Quiz: Scatterplots"

Here is the first question. It's multiple choice.

[(X)] This answer is right
[( )] This is wrong
[( )] Also wrong
[[?]] Hint: Provide a hint here if you like. Hints are marked with the ?
[[?]] Hint: You can include as many hints as you want.
***
<div class = "answer">

Nearly every quiz question should have an  `answer` box after it to explain why the correct answer is correct. 
This text will show up after the learner answers the question correctly or clicks to have the right answer revealed. It can be as long as you like, and allows any markdown formatting (you can embed pictures or videos, links, etc.).

Use `<div class = "answer">` to mark these sections with special styling, so that they're visually distinct from the rest of the quiz. The style for `"answer"` is defined in the css file.

For this context to show up automatically when the learner answers the question correctly or clicks to have the right answer revealed, it needs to be surrounded by `***` (at least three, but you can use more if you want a more visually distinct horizontal marker in your md file).

</div>
***

You can have questions with multiple correct answers. Select all of the following correct choices:

[[ ]] Not this one
[[X]] This is one of the correct ones
[[X]] Here's another correct one
[[ ]] This one is wrong, though
[[?]] Hint: Remember to select ALL of the correct choices.
***
<div class = "answer">

Here is the answer box for this question.

</div>
***

True or False: This statement is NOT true. ;)

[( )] TRUE
[(X)] FALSE
***
<div class = "answer">

Here is the answer box for this question.

</div>
***

Short answer/text response. Note that, without any additional script, to get it marked "correct" the learner has to enter it exactly as you do.
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

Note that you can use any markdown formatting you want in quizzes, including bold, links, math, lists, embedded media, code blocks, etc. For accessibility for learners using screenreaders, if your question is more than a single markdown paragraph, you must enclose it in `<div>` tags. For example:

<div>
In the following code block, what should fill in the blank?

```r
install.packages(____)
```
</div>

[(X)] "ggplot2"
[( )] ggplot2
[( )] package = ggplot2
***
<div class = "answer">

Note that the `<div>` tags surround the full content of the question being asked (in this case, a sentence in markdown followed by the code block), and then there is one blank line, then the multiple choice options. 

For more details, see [notes about quizzes in the LiaScript documentation](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/do.cs/master/README.md#notes-about-questions)

</div>
***

There are many more options and examples of quiz questions in the LiaScript documentation. [Read more about quiz syntax here.](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md#quizzes)


## Ungraded quiz questions

Useful formative assessment doesn't have to be an actual quiz question. 

You can ask questions with no graded answer as well. LiaScript calls these [surveys](https://liascript.github.io/course/?https://raw.githubusercontent.com/LiaScript/docs/master/README.md#111).

Here's an ungraded question with a text box three lines long:

[[___ ___ ___]]

Here's one that's just one line long:

[[___]]

Hints and follow-up explanations don't work for survey questions, but you can use [html detail tags](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) to create a solution that won't be visible to the learner until they choose to open it. For example:

Think about your own research, and write out three ways you could make your work more reproducible this year.

[[___ ___ ___]]

<details>

<summary>Click here to see our answer</summary>

<div class = "answer">

The best approach for you depends on your research, of course! 

Here are some concrete, actionable changes to improve the reproducibility of your work:

- Switch from point-and-click to scripted analysis
- Share your data in a public repository
- Share your code on GitHub
- Write a pre-registration for your next study

</div>
</details>

You can also set a code block to be closed until the learner chooses to open it by giving it a title beginning with `-` (e.g. `-Solution`). For example:

Modify the code from the final example, the [lowess curve trend line](#lowess-curve-trend-lines), to separate out respondents by smoking status (`is_smoker`) with a separate facet for each.

```python  -Solution
sns.lmplot(data = covid_data,
            x="val_age", y="val_height_cm",
           scatter_kws={"alpha": .1},
           lowess=True,
           col = "is_smoker")

# Note that row = "is_smoker" would also work.
# If you used col, try switching to row now to see how the plot changes!
```

You can even use this to provide multiple possible correct options. Each solution will be closed until the learner clicks to open it. For example:

Write code to draw a linear trend line showing the relationship between Age and Glucose, but create a plot with just the line, no scatterplot underneath. Try it each of the three ways, using geom\_smooth, geom\_abline, and geom\_line.

```r  -Solution using geom_smooth
ggplot(breast_cancer_data, mapping = aes(y=Glucose, x=Age)) +
  geom_smooth(method = "lm") +
  theme_bw()
```
```r  -Solution using geom_abline
# note that this doesn't actually plot a line, since there are no observations to set the x and y scales
# you'll see a blank plot
ggplot(breast_cancer_data, mapping = aes(y=Glucose, x=Age)) +
  geom_abline(intercept = model$coefficients[1], slope = model$coefficients[2]) +
  theme_bw()

# you can set the x and y scales yourself manually by adding a layer for each
ggplot(breast_cancer_data, mapping = aes(y=Glucose, x=Age)) +
  geom_abline(intercept = model$coefficients[1], slope = model$coefficients[2]) +
  scale_y_continuous(limits = c(min(breast_cancer_data$Glucose), max(breast_cancer_data$Glucose))) +
  scale_x_continuous(limits = c(min(breast_cancer_data$Age), max(breast_cancer_data$Age))) +
  theme_bw()
```
```r  -Solution using geom_line
ggplot(breast_cancer_data, mapping = aes(y=Glucose, x=Age)) +
  geom_line(mapping = aes(y=model$fitted.values)) +
  theme_bw()
```
```r  -Another solution, using alpha
# you can also make any element of a plot invisible by setting its alpha to 0
# in this case, we can make the dots of the scatterplot disappear from any of the plots we made above
# for example:
ggplot(breast_cancer_data, mapping = aes(y=Glucose, x=Age)) +
  geom_point(alpha = 0) +
  geom_line(mapping = aes(y=model$fitted.values)) +
  theme_bw()

# this has the advantage of keeping the scales for the plot consistent
# and it means you don't have to set the scales manually when using geom_abline
```

## Additional Resources

The last section of the module content should be a list of additional resources to learn more about this topic.

Avoid linking to other modules we've written here.

## Feedback
@feedback

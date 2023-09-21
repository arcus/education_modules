<!--

author:   DART Team
email:    dart@chop.edu
version:  2.0.0
current_version_description: Made coding_required a mandatory front matter field for all modules
language: en
narrator: UK English Female
title: DART LiaScript docs

@add_item

<script modify="false">
try {
  let module_characteristics = @input(`module_characteristics`)

  if(module_characteristics[@0]) {
    send.liascript(`- @1 💫`)
  } else send.clear()
} catch(e) { }
</script>

@end

@version_history

Previous versions: 

- [1.3.1](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/b453a05b5ac756fb5c7b183deae9d4fc91b3a617/docs.md): Clarified that version_history cannot be blank but sets_you_up_for and depends_on_knowledge_available_in can
- [1.2.1](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/4347cd14c9f5a3fd110910ec09c0560a46e390bd/docs.md): Add genomics macros, add git_basics to the list of sequences.
- [1.1.0](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/8f41dd25216329b785335e15f1824b13d6240778/docs.md): Update SQL macros instructions (note that version number wasn't correctly incremented here)
- [1.0.0](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/ad25398d0eef884402cff0f0c4fb4ca360d3b8f4/docs.md): Added versioning info, initial version.

@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
-->

# DART LiaScript docs

This is the technical documentation for DART modules written with [LiaScript](https://liascript.github.io/). 
LiaScript is a [markdown](https://en.wikipedia.org/wiki/Markdown) dialect, so writing a DART module is a lot like writing any other plain text document, with a few exceptions for special formatting. 

**This is verison @version of this document.**

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

To see this document as an interactive LiaScript rendered version, click on the following link/badge:

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/docs.md)

</div>

## Important resources for writing DART modules

This documentation covers the technical part of writing only, i.e. how to use our custom DART templates and macros, and how to make sure a module you're writing will pass our Quality Assurance process. 

For more general guidance about how to contribute to the DART project, including how to propose a new module, see our [contributing guidelines](https://github.com/arcus/education_modules/blob/main/CONTRIBUTING.md). 
Also, before you begin writing a new module for the first time, be sure to look at some of our [existing modules](https://arcus.github.io/education_modules/list_of_modules) for examples of formatting, style, and tone.

If you're new to markdown, check out this general [guide to markdown syntax](https://daringfireball.net/projects/markdown/syntax). 

Most things that work in regular markdown will also work in LiaScript, but there are a few exceptions. 
To see how markdown works in LiaScript, look over the [LiaScript documentation on markdown syntax](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md#markdown-syntax).

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

This document is itself a LiaScript markdown file! 
To see what the text looks like, open the [raw version of this file](https://raw.githubusercontent.com/arcus/education_modules/main/docs.md).

</div>

## Module review process

When you write a new DART module, it will go through a formal review process before being published, called Quality Assurance (QA). 
The instructions in this documentation will help you make sure your module will pass QA with as few revisions as possible.

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

Our QA process is very transparent. 
You can view the [QA checklist](https://github.com/arcus/education_modules/blob/main/.github/ISSUE_TEMPLATE/qa-for-standard-modules.md) that will be used to check your module at any time. 
You can also see revisions and comments on [pull requests for other modules that have already been QAed](https://github.com/arcus/education_modules/pulls?q=is%3Apr+is%3Aclosed+label%3A%22Quality+Assurance%22) to see what kinds of adjustments were made. 

</div>

## Style and formatting requirements

- The title should be the only level-1 header in the module document.
- LiaScript will create a new page at each level 1, 2, or 3 header, so to avoid a page with only a header and no content, include text after each header before the next.
- We have a standardized naming convention and directory structure:

  * Folder and file names use lowercase and underscores (no dashes)
  * Main module directory folder name is identical to the name of the module content markdown file.
  * Images, videos, and other audio-visual assets are saved within a `media` folder within the module directory
  * Code files (including scripts, notebooks, etc.) are saved within a `src` folder within the module directory

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

In addition to the basic formatting requirements listed here, we have detailed [inclusivity guidelines](https://github.com/arcus/education_modules/blob/joy-contributors/_for_authors/inclusivity_guidelines.md) with requirements (and helpful examples!) for language choice, style, and accessibility.

**Please read the inclusivity guidelines carefully before you begin writing.** 
It's much easier to plan an inclusively designed module from the start than to attempt to fix a module you've already drafted.

</div>

## Which module template to use

There are three different module templates to choose from: 

- `template_standard.md`
- `template_wrapper.md`
- `template_exercise.md`

You should use the  **standard** template if at least 50% of the module content will be written in your LiaScript file (even if adapted from other open source content) rather than embedded or linked to. 
The overwhelming majority of our existing modules are standard modules. 

You should use the **wrapper** template if more than 50% of the content is embedded or linked to external resources (things not hosted in the DART repository). 

You should use the **exercise** template if the module is mostly practice, not instruction. This template is similar to the standard template but not exactly the same, and the module content will be very different. This type of module might present the learner with a problem to solve using the skills that could be acquired in our instructional modules, and might include a dataset to explore. 

## How to use template files

To see how to use a template, you'll need to look at it in its **raw** format.

If you open a template on GitHub, you'll see the rendered GitHub version, which will hide a lot of the important content. 
To see the raw version on GitHub, click the `Raw` button at the upper right corner of the file. 
If you open a markdown file in a text editor like VSCode, it will show you the raw file by default.

When you start writing a new module, you'll begin with the template file for the type of module you wish to write, and then fill it in with your content.

To see examples of DART modules, see [our list of completed modules](https://arcus.github.io/education_modules/list_of_modules).

## How to use the front matter

We store a lot of important information in the front matter section at the top of each module. Part of the [module QA process](#module-review-process) is checking that everything is correctly encoded in the front matter. 

Which front matter items are required? It depends on the content of the module you're writing:

|                                     | All Modules | R[^1] | Wrapper[^2] | Notes                                                                                     |
| :---------------------------------- | :---------: | :---: | :---------: | :---------------------------------------------------------------------------------------- |
| `author`                            |      X      |   X   |      X      |                                                                                           |
| `email`                             |      X      |   X   |      X      |                                                                                           |
| `version`                           |      X      |   X   |      X      |                                                                                           |
| `current_version_description`       |      X      |   X   |      X      |                                                                                           |
| `module_type`                       |      X      |   X   |      X      |                                                                                           |
| `docs_version`                      |      X      |   X   |      X      |                                                                                           |
| `langauge`                          |      X      |   X   |      X      |                                                                                           |
| `narrator`                          |      X      |   X   |      X      |                                                                                           |
| `mode`                              |      X      |   X   |      X      |                                                                                           |
| `title`                             |      X      |   X   |      X      |                                                                                           |
| `comment`                           |      X      |   X   |      X      |                                                                                           |
| `long_description`                  |      X      |   X   |      X      |                                                                                           |
| `estimated_time_in_minutes`         |      X      |   X   |      X      |                                                                                           |
| `r_file`                            |             |   X   |             |                                                                                           |
| `pre_reqs`                          |      X      |   X   |      X      |                                                                                           |
| `learning_objectives`               |      X      |   X   |      X      |                                                                                           |
| `module_structure`                  |             |       |      X      |                                                                                           |
| `resource1_name`[^3]                |             |       |      X      |                                                                                           |
| `resource1_description`[^3]         |             |       |      X      |                                                                                           |
| `resource1_wellvetted`[^3]          |             |       |      X      |                                                                                           |
| `resource1_wellvetted_text`[^3]     |             |       |      X      |                                                                                           |
| `resource1_maintained`[^3]          |             |       |      X      |                                                                                           |
| `resource1_maintained_text`[^3]     |             |       |      X      |                                                                                           |
| `resource1_stablesupport`[^3]       |             |       |      X      |                                                                                           |
| `resource1_stablesupport_text`[^3]  |             |       |      X      |                                                                                           |
| `resource1_a11y_issues`[^3]         |             |       |      X      |                                                                                           |
| `good_first_module`                 |      X      |   X   |      X      |                                                                                           |
| `data_domain`                       |             |       |             |                                                                                           |
| `data_task`                         |             |       |             |                                                                                           |
| `coding_required`                   |      X      |   X   |      X      |                                                                                           |
| `coding_level`                      |             |   X   |             |                                                                                           |
| `coding_language`                   |             |   X   |             |                                                                                           |
| `sequence_name`                     |             |       |             |                                                                                           |
| `previous_sequential_module`        |             |       |             |                                                                                           |
| `sets_you_up_for`                   |      X      |   X   |      X      |                                                                                           |
| `depends_on_knowledge_available_in` |      X      |   X   |      X      |                                                                                           |
| `is_parallel_to`                    |             |       |             |                                                                                           |
| `version_history`                   |      X      |   X   |      X      |                                                                                           |
| `import`                            |      X      |   X   |      X      | Importing `macros.md` is required for all modules. Additional import files may be needed. |


[^1]: Modules using [interactive R code](#interactive-r).
[^2]: Wrapper modules are built using the wrapper template (see [which module template to use](#which-module-template-to-use)).
[^3]: You can include up to three external resources in a wrapper module. 
  To add additional external resources, follow the same instructions for all the `resource1` front matter items for `resource2` items (e.g. `resource2_name`, `resource2_description`) and `resource3` items.

### Your front matter checklist

Use the checklist below to help make sure you're including all the front matter fields you need for your module.

**Which of the following describe your module?** 

- [ ] includes interactive R
- [ ] includes interactive Python
- [ ] includes interactive SQL
- [ ] learner will need to code to meet the learning objectives
- [ ] is about a particular kind of data (EHR, omics data, geospatial data, etc.)
- [ ] teaches a particular data skill or task (visualization, anlaysis, cleaning, etc.)
- [ ] is a [wrapper module](#which-module-template-to-use)
- [ ] is in a sequence (including the first module in the sequence)
- [ ] follows other modules in a sequence (i.e. it's not the first in the sequence)
- [ ] is parallel to one or more other modules (i.e. covers the same content but in a different coding langauge/operating system)
- [ ] uses the Data Carpentry genomics AMI on AWS
- [ ] uses the learning_bash repo
<script output="module_characteristics">"@input"</script>

You'll need the following fields in your front matter (new fields added by checking boxes above will be followed by 💫): 

- author
- email
- version
- current\_version\_description
- module\_type
- docs\_version
- language
- narrator
- mode
- title
- comment
- long\_description
- estimated\_time\_in\_minutes

@add_item(0,r\_file)

* pre\_reqs
* learning\_objectives

@add_item(6,resource1\_name)
@add_item(6,resource1\_description)
@add_item(6,resource1\_wellvetted)
@add_item(6,resource1\_wellvetted\_text)
@add_item(6,resource1\_maintained)
@add_item(6,resource1\_maintained\_text)
@add_item(6,resource1\_stablesupport)
@add_item(6,resource1\_stablesupport\_text)
@add_item(6,resource1\_a11y\_issues)

* good\_first\_module

@add_item(4,data\_domain)
@add_item(5,data\_task)

* coding\_required

<script modify="false">
try {
  let module_characteristics = @input(`module_characteristics`)

  if(module_characteristics[0] || module_characteristics[1] || module_characteristics[2] || module_characteristics[3]) {
    send.liascript(`- coding\_level 💫`)
  } else send.clear()
} catch(e) { }
</script>
<script modify="false">
try {
  let module_characteristics = @input(`module_characteristics`)

  if(module_characteristics[0] || module_characteristics[1] || module_characteristics[2] || module_characteristics[3]) {
    send.liascript(`- coding\_language 💫`)
  } else send.clear()
} catch(e) { }
</script>
<script modify="false">
try {
  let module_characteristics = @input(`module_characteristics`)

  if(module_characteristics[7] || module_characteristics[8]) {
    send.liascript(`- sequence\_name 💫`)
  } else send.clear()
} catch(e) { }
</script>

@add_item(8,previous\_sequential\_module)

* sets\_you\_up\_for
* depends\_on\_knowledge\_available\_in

@add_item(9,is\_parallel\_to)

* version\_history
* import macros.md

@add_item(6,import macros_wrapper.md)
@add_item(0,import macros_r.md)
@add_item(1,import macros_python.md)
@add_item(2,import macros_sql.md)
@add_item(10,import macros_genomics.md)
@add_item(10,import macros_bash.md)

### `author`

```
author:   Your Name
```

### `email`

```
email:    email@example.edu
```

### `version`

```
version:  0.0.0
```

When you're ready to submit your module for QA, it should have a module version number of at least 1.0.0 if first public version, or if this is an update then an [appropriately incremented version number](https://github.com/arcus/education_modules/blob/main/versioning_guidelines.md)

It's a good idea to keep your version set to `0.0.0` while you're still drafting as it will help prevent your browser from caching the module, making it easier for you to review changes as they render online. 
For more details, see the [LiaScript documentation about state](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md#state).

### `current_version_description`

```
current_version_description: Initial version
```

This is a 1-3 line description of the current version of the module. Start with `Initial version` for 1.0.0.
Then whenever the module gets a major (first number change) or minor update (second number change), this field should be updated to describe **from the learner's point of view** what meaningful changes have occured since the last version. If the most recent commit creates a revision (third number change), please keep the existing `current_version_description` and do not update it.  

The content of `current_version_description` should be simple text without bullet points. Use present tense for verbs, such as "add material on..." instead of "added material on...".  You can use fragments and no terminating punctuation is required.  

Focus on changes in module content rather than technical updates that might be invisible to learners (e.g. standardized text being replaced with a macro).

For example, for a module that has undergone at least one new version (major or minor), this field might look something like this:

```
current_version_description: add less command, update man section, improve quiz and appearance
```

### `module_type`

```
module_type: standard
```

Should be one of `standard`, `wrapper`, or `exercise` (see [which module template to use](#which-module-template-to-use)).

### `docs_version` 

```
docs_version: 1.0.0
```

This value refers to this document, docs.md, and it's how we keep track of what our module writing guidelines were when a module was last updated.

When you're ready to submit your module for QA, it should have a docs version number that is up to date with the **major** version of this document (@version, note that it's fine if there have been minor updates or revisions to docs.md, you only need to worry about the major version) -- if not, the module should be brought in line with any changes that have occurred to docs.md before continuing to submit it for QA.

If you wrote a module using a previous version of docs.md, look for a [checklist issue template](#updating-this-document) help you bring your module up to date. 

### `language`

```
language: en
```

This defines the language for the file (default is English, `en`). 
See the [LiaScript documentation on `language`](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md#language) for more details. 

### `narrator`

```
narrator: UK English Female
```

This defines the voice to be used for text to voice, if the learner chooses to use that.
See the [LiaScript documentation on `narrator`](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md#narrator) for more details. 

### `mode`

```
mode: Textbook
```

This sets the [default mode of display for LiaScript](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md#mode). 

It should be `Textbook`.

### `title` 

```
title: Module Title
```

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

We use the module title to collate feedback in our REDCap survey, so if the title is edited after learners have begun sending in feedback we'll lose the ability to quickly group feedback for this module. 
Avoid making changes to the title after publication.

</div>

### `comment` 

```
comment:  This is a short, focused description of the module.
```

### `long_description` 

```
long_description: This is a longer description, which should be understandable for a lay audience. It will print under "Is this module right for me?" in the overview.
```

### `estimated_time_in_minutes`

```
estimated_time_in_minutes: 45
```

This is rough guess of how long it might take a learner to work through the module. It will print under "Estimated time to completion" in the overview. Valid values are any integer 1-60. 

### `r_file`

```
r_file: r\_logistic\_regression
```

If this module uses refers to a specific directory and file within the `education_r_environment` directory structure, you can include that directory / file name, without file extension, here, for example: `this\_r\_module`.

Note that rmds in the `education_r_environment` repo should be saved in a directory that matches the file name, like `this_r_module/this_r_module.rmd`. When you use the [r\_lesson\_prep macro](#interactive-r), it will fill in the text from `r_file` to use as both the directory name and file name for this lesson's notebook. Use backslashes to escape underscores (e.g. `this\_r\_module` rather than `this_r_module`). 

### `pre_reqs` 

```
@pre_reqs
This module assumes some familiarity with X and Y, in particular:

* one skill we have [another module for](https://education.arcus.chop.edu)
* some familiarity with [a topic](https://education.arcus.chop.edu)
* understanding of [one thing](https://education.arcus.chop.edu) and [another](https://education.arcus.chop.edu)

If relevant, you can include recommendations for somewhere else to start if the learner doesn't have these prereqs. For example: If you are brand new to R or python (or want a refresher) consider starting with [Intro to R](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_introduction/r_basics_introduction.md) or [Intro to python](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_python/demystifying_python.md) first and then coming back here.
@end
```

List any skills and knowledge needed to do this module here. When available, include links to resources, especially other modules we've made (to show learners where this falls within our catalog).

Note that `@pre_reqs` is a [block macro](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md#blocks) in LiaScript, which means it has `@end` after the last line.

### `learning_objectives` 

```
@learning_objectives  
After completion of this module, learners will be able to:

- identify key elements
- create a product
- do a task
- articulate the rationale for something
@end
```

Learning objectives are a very important element of the module. 

- Learning objectives should be clearly defined using strong, descriptive verbs (see [Bloom's taxonomy](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/) for ideas).
- Every learning objective should be covered in the module content.
- All major topics covered should be represented by a learning objective -- there should be no significant knowledge imparted that isn't specified in the learning objectives.
- There should be at least one quiz question or exercise for each learning objective.

Note that `@learning_objectives` is a [block macro](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md#blocks) in LiaScript, which means it has `@end` after the last line.

The learning objectives will be automatically printed twice in each module: Once in the [Overview](#overview) and then again in the [Feedback](#feedback) section.

### `module_structure`

```
@module_structure
1. Part 1
2. Part 2
3. Part 3
@end
```

The point of `@module_structure` is to give learners a sense of the learning steps in a wrapper module --- in particular, it should emphasize what pieces they'll do in the LiaScript module itself and which they'll do elsewhere. It can include as many or as few steps as needed.

The following are just some examples of possible structures. The specific structure will depend greatly on the particular external module/educational resource(s) you are using in your wrapper module.

Example Structure 1:

```
@module_structure
1. Read about how this topic fits into some bigger picture here in this LiaScript course.
2. Do the activities embedded in this module (using iFrames).
3. Answer a few questions to make sure you understood the key parts.
@end
```

Example Structure 2:

```
@module_structure
1. Open the external resource in a new browser window.
2. Read Chapter 1 and do the activities at the end.
3. Return to this LiaScript course to answer a few questions to make sure you understood the key parts.
@end
```

Example Structure 3:

```
@module_structure
1. Open this external resource in a new browser window.
2. Read Section 2.1 and 2.2.
3. Return to this LiaScript course to do an activity.
4. Answer a few questions (again in the LiaScript course) to make sure you understood the key parts.
@end
```

Note that `@module_structure` is a [block macro](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md#blocks) in LiaScript, which means it has `@end` after the last line.
It will automcatically be printed in the Lesson Preparation section of wrapper modules. 

### `resource1_name`

```
resource1_name: Docker 101 Tutorial
```

This is the title of the external resource you'll be linking to. 
Don't make it a hyperlink (we want to wait to link to the resource until the right point in the module).

### `resource1_description`

```
resource1_description: In this self-paced, hands-on tutorial, you will learn how to build images, run containers, use volumes to persist data and mount in source code, and define your application using Docker Compose. You’ll even learn about a few advanced topics, such as networking and image building best practices.
```

A brief description of the external resource. 
This will print underneath the name of the resource and just above the criteria checklist.

### `resource1_wellvetted` 

```
resource1_wellvetted: true
```

**Do we have reason to believe in the accuracy of this content?**
Who are the expert authors? Or what institutional authority guarantees accuracy? 

Must be one of `true` or `false`.
If true, this item will show up with a green checkmark circle in the criteria list. 
If false, then it will show as a yellow circle with a horizontal line. 

### `resource1_wellvetted_text` 

```
resource1_wellvetted_text: The Docker 101 tutorial is an [open source project](https://github.com/docker/getting-started), so it has many authors, but it is sponsored and hosted by Docker Inc, the company that produces the docker software. The open source nature of the tutorial also helps ensure that any errors or problems can be caught and addressed quickly. 
```

This is a short explanation justifying the `true` or `false` decision recorded for `resource1_wellvetted`. If this is a resource by expert authors and/or well-vetted, then explain. If it is not, mention the shortcoming, and explain why you think it's worth linking to in a module anyway.
 
### `resource1_maintained` 

```
resource1_maintained: true
```

**Do we have reason to believe this material will stay up to date?**
Who is in charge of implementing regular updates to this material? This is important in fast-changing fields.

Must be one of `true` or `false`. 
If true, this item will show up with a green checkmark circle in the criteria list. 
If false, then it will show as a yellow circle with a horizontal line. 

### `resource1_maintained_text` 

```
resource1_maintained_text: This tutorial is maintained by Docker Inc, so we expect that it will remain up to date whenever changes are implemented in docker.
```

This is a short explanation justifying the `true` or `false` decision recorded for `resource1_maintained`. If this is a resource that is well maintained, then explain. If it is not, mention the shortcoming, and explain why you think it's worth linking to in a module anyway.

### `resource1_stablesupport`

```
resource1_stablesupport: true
```

**Do we have reason to believe this material won't disappear?**
Who hosts it?

Must be one of `true` or `false`. 
If true, this item will show up with a green checkmark circle in the criteria list. 
If false, then it will show as a yellow circle with a horizontal line. 

### `resource1_stablesupport_text`

```
resource1_stablesupport_text: This is hosted on the Docker website, and it is a popular and widely-shared tutorial. We expect it will continue to be available for the foreseeable future.
```

This is a short explanation justifying the `true` or `false` decision recorded for `resource1_stablesupport`. If this is a resource that we expect to have stable support, then explain. If it is not, mention the shortcoming, and explain why you think it's worth linking to in a module anyway.

### `resource1_a11y_issues`

```
resource1_a11y_issues: No known issues with accessibility, but we may have missed something. If you encounter an issue, please [let us know](#feedback)!
```

If you are aware of any issues with this resource related to inclusion or accessibility, list them here so learners can be forewarned. Anything that could create a barrier for a learner, or make it more difficult or frustrating to use the resource counts. Common problems are lack of transcript available for videos, lack of alt text (or sufficient written explanation in surrounding text) for images, sites that rely heavily on visual demonstration and/or point-and-click interaction for instruction, and anything that requires a credit card to sign up. 

Note that this text will print just beneath the criteria checklist, but it isn't part of the checklist and won't have a green or yellow check icon. 
We don't include accessibility and inclusion as a criterion intentionally because it isn't reasonable or helpful to assert that something is generally "accessible" or "inclusive" to all learners. 

### `good_first_module`

```
good_first_module: false
```

If this was a learner's very first experience with DART, would you be happy with this module being their first impression?

Required for all modules.

Must be one of `true` or `false`.

### `data_domain`

```
data_domain: ehr
```

This module is primarily useful for or focused on this type of data.

Must be one of the following:

- `ehr`
- `omics`
- `geospatial`
- `text`

As we write additional modules, we may add new data domains to this list!

### `data_task`

```
data_task: 
```

What type of task/action/skill does this module teach?

Must be one of the following:

- `data_visualization`: Creating representations of data such as plots, graphs, maps, etc.
- `data_management`: Organizing and storing data, including database structures, data sharing, cloud vs. local storage, and metadata.
- `data_wrangling`: Data processing steps in preparation for analysis and visualization, including cleaning, transforming, and reshaping data
- `data_analysis`: Identifying and quantifying patterns in the data, including exploratory analysis, descriptive statistics, and more formal modeling

As we write additional modules, we may add new data tasks to this list!

### `coding_required`

```
coding_required: true
```

Required for all modules.

True/False based on whether achieving the module's learning objectives requires coding. This includes a user running code locally or interacting with code in the module. 

Must be one of `true` or `false`.

### `coding_level`

```
coding_level: getting_started
```

The coding level required for the module as a whole.

Must be one of the following:

- `getting_started`: These modules are primarily about getting a platform set up
- `basic`: These modules require little or no previous exposure to coding
- `intermediate`: These modules require some previous coding exposure
- `advanced`: These modules focus on particularly difficult or specialized tasks.
- `practice_exercise`: These modules do not introduce new content.

### `coding_language`

```
coding_language: r, python
```

Must be one or more of the following:

- r
- python
- bash
- SQL
- git

### `sequence_name`

```
sequence_name: bash_basics
```

Must be one of the following: 

- `bash_basics`
- `r_basics`
- `sql`
- `python_basics`
- `genomics_tools_and_methods`
- `git_basics`
- (add more here)

### `previous_sequential_module`

```
previous_sequential_module: sql_basics
```

If it's in a sequence and there is another module before it (i.e. it's not the first module in its sequence), list the previous module here. 
Use the modules directory name (this should be the same as the name of its md file).

### `sets_you_up_for`

```
@sets_you_up_for

- sql_intermediate
- sql_joins

@end
```

Required for all modules. 

Notes how knowledge in this module will prepare the user for other concepts.

Note that `sets_you_up_for` and `depends_on_knowledge_available_in` do not need to be symmetric, i.e. it's fine for `module_a` to list that it sets you up for `module_b` without `module_b` also saying it depends on knowledge availabe in `module_a`.

If there are no modules to list here, leave it blank but do not omit it (modules may fail automatic checks if they don't have all required metadata). 
For example:

```
@sets_you_up_for

@end
```

### `depends_on_knowledge_available_in`

```
@depends_on_knowledge_available_in

- bash_command_line_101
- bash_command_line_102

@end
```

Required for all modules.

Notes where user can find useful knowledge in other modules.

Note that `sets_you_up_for` and `depends_on_knowledge_available_in` do not need to be symmetric, i.e. it's fine for `module_a` to list that it sets you up for `module_b` without `module_b` also saying it depends on knowledge availabe in `module_a`.

If there are no modules to list here, leave it blank but do not omit it (modules may fail automatic checks if they don't have all required metadata). 
For example:

```
@depends_on_knowledge_available_in

@end
```

### `is_parallel_to`

```
@is_parallel_to

- git_setup_windows

@end
```

The same instruction presented in a different coding language/environment/operating system. 

This field is not required, so if there are no modules parallel to this one, just omit this field completely.

### `version_history`

```
@version_history 

Previous versions: 

- [x.x.x](link): that version's current version description
- [x.x.x](link): that version's current version description
- [x.x.x](link): that version's current version description
@end
```

Required for all modules.

As modules are updated, every time we increment the version (major or minor only, ignore revisions) the description for the previous version (see [`current_version_description`](#current_version_description)) should be added to this `version_history` field up to a maximum of three most recent versions.

For the version number, use the highest one within that version (e.g. if there were 5 revisions during version 1.2.x, you would use 1.2.5 to record for the version history).

Include a link to the module rendered in LiaScript from that point in time.  Note that the links must be to **specific commits**, so that the module is frozen in time. 

For example:

```
[1.3.2](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/ba1dba7a4c1d4393ae8b42346fe5c69d587b8ee6/bash_command_line_101/bash_command_line_101.md#1): Remove Atom references
```

Note: `version_history` should have **max** 3 previous versions recorded. 
So when a module is on its 4+ version, every time you add a new entry to `version_history` you will also remove the oldest one.

Additionally, while we are backfilling the version_history field for modules which do not have `current_version_description` filled out for previous versions, there are [detailed instructions](https://chop365.sharepoint.com/:w:/r/teams/RSCH-Arcus/Shared%20Documents/Arcus%20Drive/Education/R25/Reconstructing%20Version%20Descriptions.docx?d=w400f6dc02dc745ad89fada5c0277ffdf&csf=1&web=1&e=75kLrP) available (for CHOP staff members only, as this is a temporary need that we don't anticipate needing to extend to outside contributors) on how to use the GitHub "blame" feature to read pertinent commit messages associated with new versions as well as constructing links for previous versions.

For a brand new module (version 1.0.0), `version_history` should say only "No previous versions" (but not omitted --- this is a required field).
It cannot be left empty because that will break the overview macro.

For example:

```
@version_history 
No previous versions.
@end
```
### `import`

```
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
```

Note that importing `macros.md` imports all the general-use macros needed for our modules (see [DART macros](#dart-macros) for details), as well as the style sheet and javascript kit for our icons. 
Every single module should import `macros.md`. 
For most modules, this is the only import file needed, but there are some notable exceptions.

Wrapper modules must import the wrapper macros as well: 

```
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_wrapper.md
```

Genomics modules that make use of the [Data Carpentry](https://datacarpentry.org/genomics-workshop/) AMI on AWS will need to import the genomics macros as well:

```
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_genomics.md
```

Bash modules that make use of the [learning_bash repo](https://github.com/arcus/learning_bash) will need to import the bash macros as well: 

```
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_bash.md
```

Modules using interactive R, Python, or SQL will need additional import files (see the sections on [interactive coding](#including-interactive-code) for details).

## DART macros

Macros are a way to include flexible text substitution with LiaScript. 

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To learn more about how macros work in general, including lots of examples, see the [LiaScript documentation on macros](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md#macros).

</div>

We use macros for a lot of our standardized text. 
For example, the Overview and Feedback sections of each module are created by the `@overview` and `@feedback` macros, respectively. 

- General use macros are in the [module macros file](https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md). This includes macros to generate the overview and feedback sections, as well as general-purpose javascript such as the gifPreload macro. It also loads our icon kit and style sheet. This macro file should be imported in **every module**. 
- Macros to create the descriptions of external resources for wrapper modules are in the [wrapper macros file](https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_wrapper.md).
- Macros for genomics modules that use AWS are in the [genomics macros file](https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_genomics.md). This includes a lesson prep macro reminding learners how to connect to their AWS instance and a reminder macro warning them that if they don't terminate their instance when they're done working they'll continue to be charged.
- A macro providing instructions on how to download the [learning_bash repo](https://github.com/arcus/learning_bash) contents (as well as links to instructions to set up the shell in Mac and Windows) is available in the [bash macros file](https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_bash.md).
- Macros for hands-on code in R, Python, and SQL modules are available in `macros_r.md`, `macros_python.md`, and `macros_sql.md`, respectively. SQL tables are loaded with additional files. For more details, see the sections on [including interactive code](#including-interactive-code) in this documentation.

For more information about our macros and instructions for writing new ones, see the [macros instructions](https://github.com/arcus/education_modules/blob/main/macros_instructions.md).

## Module sections

There are a few required sections to every module: Overview, Additional Resources, and Feedback. 
We use macros to create the overview and feedback text, so you don't need to write anything there at all other than the macro itself.

### Overview

The overview section comes immediately after the initial level-1 header, which will be the module title. For example:

```
# Logistic Regression in R
@overview

```

### Lesson Preparation

Many (but not all) modules include a Lesson Preparation section with any setup required to complete the module (see the section on [including interactive code](#including-interactive-code) for macros to create Lesson Preparation sections for R, Python, and SQL).

This section will appear in any module that requires the learner to prepare in some way. For example:

- the learner needs to download software (like git or bash)
- the learner needs an account with an external resource (like Google Colab or AWS)
- the learner will need to interact with an external resource (like a binderhub environment) 
- the function of the module requires explanation, such as how sagemath cells work 

Wrapper modules include a special section describing the external resource(s) linked to and outlining the structure of the module. 

### Content sections

Begin your module content with whatever level-2 headers make sense for your topic. 

Most modules include at least one quiz section (see [Quizzes](#quizzes-automatically-graded-questions)).

As you write, keep in mind that the headers should be clear and informative. 
The table of contents automatically generated from the headers should give learners a good overview of what to expect in the module content.

### Additional Resources

The final section of module content must be Additional Resources, and should be a list of additional resources to learn more about this topic.
Avoid linking to other modules we've written here.

### Feedback

The very last thing in the module should be the Feedback section. 
It is filled out automatically with the `@feedback` macro, so you don't need to write anything there other than the macro itself:

```
## Feedback
@feedback

```

## Including highlight boxes

Include special notes with different formatting.

Note: There's an additional style of highlight not listed here, "answer", that is used in quizzes.

### behind-the-scenes

The style "behind-the-scenes" is for giving a little more technical detail about how something does what it does.
It has a gears icon and always begins with the text "Behind the scenes".
For example:

```
<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

The commit number is a hash and associated details

</div>
```

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

The commit number is a hash and associated details

</div>

```
<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

In R the `<-` and `=` can both be used for assignment because...

</div>
```

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

In R the `<-` and `=` can both be used for assignment because...

</div>

### care

The style "care" is for content related to compassion, self-care, and motivation. For more technical help or troubleshooting, use "help" instead.
It has a hand-holding-heart icon and always begins with the text "A little encouragement..."
For example:

```
<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

This is a topic with a tremendous amount of jargon, which can make resources you may find online hard to understand for folks new to the field. When that happens it's easy to feel like there's something wrong with you if you don't get it, but that's not the case! Those kinds of gatekeeping explanations are a failure on the part of the writer, not the learner.

</div>
```

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

This is a topic with a tremendous amount of jargon, which can make resources you may find online hard to understand for folks new to the field. When that happens it's easy to feel like there's something wrong with you if you don't get it, but that's not the case! Those kinds of gatekeeping explanations are a failure on the part of the writer, not the learner.

</div>

```
<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Feeling overwhelmed? It takes a long time to learn git, so don't be disheartened if it doesn't click initially. Just focus on stage, commit, and push. Ignore the rest for now, until you've had a chance to practice just the stage-commit-push process several times.

</div>
```

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Feeling overwhelmed? It takes a long time to learn git, so don't be disheartened if it doesn't click initially. Just focus on stage, commit, and push. Ignore the rest for now, until you've had a chance to practice just the stage-commit-push process several times.

</div>

### cool-fact

The style "cool-fact" is for any cool fact that really doesn't fit into any of our other categories.
It has a brain icon and always begins with the text "Did you know?"
For example:

```
<div class = "cool-fact">
<b style="color: rgb(var(--color-highlight));">Did you know?</b><br>

Functions like this are sometimes called "syntactic sugar" because they don't change anything about how the code runs, they just make it easier for humans to read, the way that sugar makes food sweeter without adding any nutrition.

</div>
```

<div class = "cool-fact">
<b style="color: rgb(var(--color-highlight));">Did you know?</b><br>

Functions like this are sometimes called "syntactic sugar" because they don't change anything about how the code runs, they just make it easier for humans to read, the way that sugar makes food sweeter without adding any nutrition.

</div>

```
<div class = "cool-fact">
<b style="color: rgb(var(--color-highlight));">Did you know?</b><br>

This is a box showing how images work in a highlight box.

![Carebear team.](https://media.giphy.com/media/W256ghnG9iV8I/giphy.gif)

</div>
```

<div class = "cool-fact">
<b style="color: rgb(var(--color-highlight));">Did you know?</b><br>

This is a box showing how images work in a highlight box.

![Carebear team.](https://media.giphy.com/media/W256ghnG9iV8I/giphy.gif)

</div>

### external-resource

The style "external-resource" is specifically for wrapper modules, for linking to the external resource, as a way to draw attention to the fact that we're sending them out of the module and then they should come back. This is different from learn-more boxes we use in standard modules. 
It has a arrow-pointing-out-of-a-box icon and always begins with the text "External Content".
For example:

```
<div class = "external-resource">
<b style="color: rgb(var(--color-highlight));">External Content</b><br>

Next, complete the [Docker 101 tutorial](https://www.docker.com/101-tutorial/), which can be done either on your computer or in the cloud. 

Work through the whole tutorial, then return here to finish this module.

</div>
```

<div class = "external-resource">
<b style="color: rgb(var(--color-highlight));">External Content</b><br>

Next, complete the [Docker 101 tutorial](https://www.docker.com/101-tutorial/), which can be done either on your computer or in the cloud. 

Work through the whole tutorial, then return here to finish this module.

</div>

### gratitude

The style "gratitude" is for thanking authors of original sources we're using or adapting for our modules. There should always be a gratitude box for each external source linked in a wrapper module, but it's also something we will use in some standard modules when we adapt material (e.g. from carpentries lessons).
It has a heart icon and always begins with the text "Thank you!".
For example:

```
<div class = "gratitude">
<b style="color: rgb(var(--color-highlight));">Thank you!</b><br>

Material for this module was adapted, with permission, from [Stephan Kadauke's R for Clinical Data](https://skadauke.github.io/intro-to-r-for-clinicians-chop/) workshop materials. We owe special thanks to Dr. Kadauke as well as the R User Group at Children's Hospital of Philadelphia for their generosity in sharing these materials.

</div>
```

<div class = "gratitude">
<b style="color: rgb(var(--color-highlight));">Thank you!</b><br>

Material for this module was adapted, with permission, from [Stephan Kadauke's R for Clinical Data](https://skadauke.github.io/intro-to-r-for-clinicians-chop/) workshop materials. We owe special thanks to Dr. Kadauke as well as the R User Group at Children's Hospital of Philadelphia for their generosity in sharing these materials.

</div>

### help

The style "help" is for troubleshooting help, common errors, and specific technical problems. If you want to emphasize a very serious potential problem, use "warning" instead. For support that is more psycho/emotional or meta-learning in nature, use "care" instead.
It has a circle-question icon and always begins with the text "Troubleshooting help".
For example:

```
<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

A common mistake when using `filter` is to write = when you mean ==. Remember that = is for argument assignment, and == is for testing equality in conditions. If you get them mixed up, your code won't run!

</div>
```

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

A common mistake when using `filter` is to write = when you mean ==. Remember that = is for argument assignment, and == is for testing equality in conditions. If you get them mixed up, your code won't run!

</div>

### history

The style "history" is for more historical context about how/when/why something came to be the way it currently is.
It has a clock-rotate-left icon and always begins with the text "Historical context".
For example:

```
<div class = "history">
<b style="color: rgb(var(--color-highlight));">Historical context</b><br>

The reason this command is named grep is...

</div>
```

<div class = "history">
<b style="color: rgb(var(--color-highlight));">Historical context</b><br>

The reason this command is named grep is...

</div>

```
<div class = "history">
<b style="color: rgb(var(--color-highlight));">Historical context</b><br>

The first README file was from 1971, etc.

</div>
```

<div class = "history">
<b style="color: rgb(var(--color-highlight));">Historical context</b><br>

The first README file was from 1971, etc.

</div>

### important

The style "important" is for important points and key ideas.
It has a star icon and always begins with the text "Important note".
For example:

```
<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

It's generally much easier to make any necessary changes to the dataframe, such as mutating variables, before sending it to the plotting command.

</div>
```

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

It's generally much easier to make any necessary changes to the dataframe, such as mutating variables, before sending it to the plotting command.

</div>

### learn-more

The style "learn-more" alerts users resources for further learning, especially links to a more in-depth discussion of an issue that might be touched on only briefly in the module. It can link to outside sources, or other modules by us.
It has a book icon and always begins with the text "Learning connection".
For example:

```
<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To learn more about the theory behind ggplot2, read [Hadley Wickham's article, "A Layered Grammar of Graphics"](http://vita.had.co.nz/papers/layered-grammar.pdf).

</div>
```

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To learn more about the theory behind ggplot2, read [Hadley Wickham's article, "A Layered Grammar of Graphics"](http://vita.had.co.nz/papers/layered-grammar.pdf).

</div>

```
<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To do this in R instead of python, see [this other module](example.com).

</div>
```

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To do this in R instead of python, see [this other module](example.com).

</div>

### options

The style "options" is for an aside to let learners know there's another possible approach. This is for short explanations rather than linked resources; to link to another approach (e.g. here's a tutorial for another way to do this), use "learn-more" instead.
It has a left-right arrow icon and always begins with the text "Another option".
For example:

```
<div class = "options">
<b style="color: rgb(var(--color-highlight));">Another option</b><br>

You could also skip setting up an OSF account completely and just use github to publish and share your research products, but many people prefer to have OSF links available.

</div>
```

<div class = "options">
<b style="color: rgb(var(--color-highlight));">Another option</b><br>

You could also skip setting up an OSF account completely and just use github to publish and share your research products, but many people prefer to have OSF links available.

</div>

```
<div class = "options">
<b style="color: rgb(var(--color-highlight));">Another option</b><br>

You can run this in the cloud or download all of the files locally and run it on your computer. If you run it on your computer, be sure to make note of which directory you save the files in and update your working directory accordingly.

</div>
```

<div class = "options">
<b style="color: rgb(var(--color-highlight));">Another option</b><br>

You can run this in the cloud or download all of the files locally and run it on your computer. If you run it on your computer, be sure to make note of which directory you save the files in and update your working directory accordingly.

</div>

### version-update

The style "version-update" is for alerting learners to changes to a module.
It has a pencil icon and always begins with the text "Changes to this module".
For example:

```
<div class = "version-update">
<b style="color: rgb(var(--color-highlight));">Changes to this module</b><br>

We're constantly improving our materials, and this module has had recent changes. Specifically, we added a new section at the end explaining how to protect your API token when using git and GitHub for your code.

If you like, you can still access the [previous version of this module](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/a4ea7a7f1f9264dabe952b68941fc9f0f656c9fc/using_redcap_api/using_redcap_api.md). 

</div>
```

<div class = "version-update">
<b style="color: rgb(var(--color-highlight));">Changes to this module</b><br>

We're constantly improving our materials, and this module has had recent changes. Specifically, we added a new section at the end explaining how to protect your API token when using git and GitHub for your code.

If you like, you can still access the [previous version of this module](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/a4ea7a7f1f9264dabe952b68941fc9f0f656c9fc/using_redcap_api/using_redcap_api.md). 

</div>

### warning

The style "warning" alerts users to potential pitfalls, and should be reserved for serious problems only. For less serious problems, use "help" instead.
It has a ! triangle icon and always begins with the text "Warning!".
For example:

```
<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

Double check your working directory before running this code. If you're in the wrong directory, you risk overwriting your files and losing all of your work with no way to recover it.

</div>
```

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

Double check your working directory before running this code. If you're in the wrong directory, you risk overwriting your files and losing all of your work with no way to recover it.

</div>

```
<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

Files uploaded to this account will be **publicly visible**. Be very careful not to upload anything with sensitive information like passwords or private data.

</div>
```

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

Files uploaded to this account will be **publicly visible**. Be very careful not to upload anything with sensitive information like passwords or private data.

</div>

## Including non-interactive code

Include inline code with single backticks:

```
Here's some inline code: `library(ggplot2)`. 
```

Here's some inline code: `library(ggplot2)`. 

Make code blocks with at least three backticks:

````
```r
# You only need to install it once
install.packages("ggplot2")

# You'll need to load the library anew for each R session
library("ggplot2")
```
````

```r
# You only need to install it once
install.packages("ggplot2")

# You'll need to load the library anew for each R session
library("ggplot2")
```

You don't have to specify the programming language, but you can, and it should help you get appropriate syntax highlighting.

````
```python
print("This is python code")
```
````

```python
print("This is python code")
```

If you want to print code output, add a label to the code block to make that clear to learners: 

````
```bash
ls -l -h
```

``` +output
-rw-rw-r-- 1 dcuser dcuser 545M Jul  6 20:27 SRR2584863_1.fastq
-rw-rw-r-- 1 dcuser dcuser 183M Jul  6 20:29 SRR2584863_2.fastq.gz
-rw-rw-r-- 1 dcuser dcuser 309M Jul  6 20:34 SRR2584866_1.fastq.gz
-rw-rw-r-- 1 dcuser dcuser 296M Jul  6 20:37 SRR2584866_2.fastq.gz
-rw-rw-r-- 1 dcuser dcuser 124M Jul  6 20:22 SRR2589044_1.fastq.gz
-rw-rw-r-- 1 dcuser dcuser 128M Jul  6 20:24 SRR2589044_2.fastq.gz
```
````

```bash
ls -l -h
```

``` +output
-rw-rw-r-- 1 dcuser dcuser 545M Jul  6 20:27 SRR2584863_1.fastq
-rw-rw-r-- 1 dcuser dcuser 183M Jul  6 20:29 SRR2584863_2.fastq.gz
-rw-rw-r-- 1 dcuser dcuser 309M Jul  6 20:34 SRR2584866_1.fastq.gz
-rw-rw-r-- 1 dcuser dcuser 296M Jul  6 20:37 SRR2584866_2.fastq.gz
-rw-rw-r-- 1 dcuser dcuser 124M Jul  6 20:22 SRR2589044_1.fastq.gz
-rw-rw-r-- 1 dcuser dcuser 128M Jul  6 20:24 SRR2589044_2.fastq.gz
```


## Including interactive code

We use three main approaches for interactive coding exercises: 

- We can link to interactive notebooks hosted on Posit Cloud (see example notebooks in [our R notebook repository](https://github.com/arcus/education_r_environment)). This is our approach for most R modules, for example: [R Basics: Introduction](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_introduction/r_basics_introduction.md) 
- We can have interactive coding cells in modules themselves using sagemath. This is our approach for most python modules, for example: [Python Basics: Functions, Methods, and Variables](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md)
- We can also have interactive coding cells in modules using AlaSQL, which is our approach for SQL modules, for example: [SQL Basics](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/sql_basics/sql_basics.md)

We don't have a way to include interactive code for git or bash. For those modules, we just instruct learners to work on their own machines.

### Interactive R

If your lesson includes R code examples hosted in binder from [our R notebook repository](https://github.com/arcus/education_r_environment), then you'll need to load the R macros by adding the following `import` statement to the front matter of your module:

```
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_r.md
```

You can then insert the `@lesson_prep_r` macro, which includes instructions for opening up the relevant rmd document, in your Lesson Preparation section:

```
## Lesson Preparation: R Studio

@lesson_prep_r
```

Note that you must have `r_file` filled out in the front matter. 

### Interactive Python

If your lesson includes interactive python code in sagemath cells, then you'll need to load the Python macros by adding the following `import` statement to the front matter of your module: 

```
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_python.md
```

You can then insert the `@ lesson_prep_python_sage` macro, which includes instructions and an example interactive code block, in your Lesson Preparation section:

```
## Lesson Preparation: Interactive Python

@ lesson_prep_python_sage
```

### Interactive SQL

If your lesson includes interactive SQL code, you'll need to load the SQL macros. The SQL macros file includes the code to generate each of the tables, row by row. You'll need the following import statement in your front matter:

```
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_sql.md
```

Note that very small tables (just a few rows) can be constructed right in the front matter for the module that uses them. Any larger tables, or tables that need to be re-used across different modules, should be added to the `macros_sql.md` file though.

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To learn about creating a new macro, such as a new SQL table, see our [instructions for DART macros](https://github.com/arcus/education_modules/blob/main/macros_instructions.md).

</div>

To insert text providing a brief refresher on SQL, including our style guide and an example interactive code block, use the following macro in your Lesson Preparation section:

```
@lesson_prep_sql
```

## Including media

This section includes examples of embedded media. 

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Please note, we have guidelines in place to help keep our modules as accessible as possible, including **requirements about how to do alt text for images and transcripts for audio**. 
Review our [inclusivity guidelines](https://github.com/arcus/education_modules/blob/joy-contributors/_for_authors/inclusivity_guidelines.md) for details. 

</div>

Here are several examples of embedded media:  

```
![A valuable image, and this is its alt text.](https://upload.wikimedia.org/wikipedia/commons/0/0f/Grosser_Panda.JPG "Here is a subtitle that will display beneath the image.")
```

![A valuable image, and this is its alt text.](https://upload.wikimedia.org/wikipedia/commons/0/0f/Grosser_Panda.JPG "Here is a subtitle that will display beneath the image.")

You can change things like the size of the image two ways. 

You can add a comment with additional html after the markdown:

```
![RStudio as shown in the cloud platform Binder.](https://github.com/arcus/education_r_environment/blob/main/media/binder_rstudio.png?raw=true)<!--
style = "border: 1px solid rgb(var(--color-highlight)); max-width: 800px;"-->
```

![RStudio as shown in the cloud platform Binder.](https://github.com/arcus/education_r_environment/blob/main/media/binder_rstudio.png?raw=true)<!--
style = "border: 1px solid rgb(var(--color-highlight)); max-width: 800px;"-->

Or you can use html to specify the whole embedded image:

```
<img src="https://github.com/arcus/education_r_environment/blob/main/media/binder_rstudio.png?raw=true" alt="RStudio as shown in the cloud platform Binder." style = "border: 1px solid rgb(var(--color-highlight)); max-width: 800px;">
```

<img src="https://github.com/arcus/education_r_environment/blob/main/media/binder_rstudio.png?raw=true" alt="RStudio as shown in the cloud platform Binder." style = "border: 1px solid rgb(var(--color-highlight)); max-width: 800px;">

You can link to images online with their url, or locally with the file path, e.g. `![This is the alt text.](media/my_image.png)`

If you want to provide several images in a gallery, just make a "paragraph" of image links and LiaScript will render it as a gallery:

```
![img1 alt text.](https://upload.wikimedia.org/wikipedia/commons/6/68/Ailuropoda_melanoleuca_%28Panda_g%C3%A9ant%29_-_445.jpg) ![img2 alt text.](https://upload.wikimedia.org/wikipedia/commons/2/2d/Panda_giganti_al_Giant_Panda_Breeding_Research_Base_Chengdu.jpg) ![img3 alt text.](https://upload.wikimedia.org/wikipedia/commons/1/12/BabyPandaAtSDZ.jpg)
```

![img1 alt text.](https://upload.wikimedia.org/wikipedia/commons/6/68/Ailuropoda_melanoleuca_%28Panda_g%C3%A9ant%29_-_445.jpg) ![img2 alt text.](https://upload.wikimedia.org/wikipedia/commons/2/2d/Panda_giganti_al_Giant_Panda_Breeding_Research_Base_Chengdu.jpg) ![img3 alt text.](https://upload.wikimedia.org/wikipedia/commons/1/12/BabyPandaAtSDZ.jpg)

```
!?[This video is hosted on youtube.](https://www.youtube.com/watch?v=iIAO4Htzn8M)
```

!?[This video is hosted on youtube.](https://www.youtube.com/watch?v=iIAO4Htzn8M)

You can also embed local videos, just as with images: `!?[An embedded video.](media/intro.mp4 "This is its subtitle")`

## Including math

Surround inline math statements with `$`: 

```
Here's a sentence with some math in it $ 1 + \beta = 2 $.
```

Here's a sentence with some math in it $ 1 + \beta = 2 $.

You can also put in blocks of math:

```
$$
   \sum_{i=1}^\infty\frac{1}{n^2}
        =\frac{\pi^2}{6}
$$
```

$$
   \sum_{i=1}^\infty\frac{1}{n^2}
        =\frac{\pi^2}{6}
$$

## Including tables

If you wish to print a table, you can use markdown table formatting. 

Note that LiaScript has defaults that will allow users to toggle tables of data between table format and a plot of the data --- if you don't want to allow that functionality, you need to set the data-type to none. For example:

```
<!-- data-type="none" class="tight-table" style="font-size:80%"-->
| subj_id  | street_address  | city  | state   | zip  | date_start  | date_end   |
| :--------- | :--------- | :--------- | :--------- | :--------- | :--------- | :--------- |
| 11234   | 123 Main Street   | Smithtown    | PA  | 19000    | 2022-01-01   | `NULL`    |
| 11234   | 123 Oak Lane   | Old Towne    | PA  | 18000   | 2000-01-01    | 2021-12-31    |
| 93452   | 123 Green Blvd  | Kirby    | TN  | 37000    | 2020-05-01    | `NULL`   |
```

<!-- data-type="none" class="tight-table" style="font-size:80%"-->
| subj_id  | street_address  | city  | state   | zip  | date_start  | date_end   |
| :--------- | :--------- | :--------- | :--------- | :--------- | :--------- | :--------- |
| 11234   | 123 Main Street   | Smithtown    | PA  | 19000    | 2022-01-01   | `NULL`    |
| 11234   | 123 Oak Lane   | Old Towne    | PA  | 18000   | 2000-01-01    | 2021-12-31    |
| 93452   | 123 Green Blvd  | Kirby    | TN  | 37000    | 2020-05-01    | `NULL`   |


For more information about using tables in LiaScript, see the [tables section of the LiaScript documentation](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md#tables).

## Quizzes (automatically graded questions)

We use quizzes for [formative assessment](https://carpentries.github.io/instructor-training/aio.html#using-formative-assessment-to-support-memory-consolidation). There is no point value or grading, and students are allowed to retry quizzes as many times as they like until they get the right answer. The goal is to provide learners an opportunity to check their own understanding. 

Quizzes should connect directly to your learning objectives. Each quiz question should connect to one learning objective, and every learning objective should have at least one quiz question associated with it somewhere in the module. Learners should be able to answer all the questions based on the content within the module alone; they should not need to have read or consulted any of the linked learn-more resources. 

Note that sometimes it won't make sense to include quiz questions in a module. Exercise modules, for example, generally won't contain quizzes (though you are welcome to include them if you feel they add value to your module).

Quizzes should always be navigable from the sidebar, meaning they should be labeled with a level 2 or 3 header. If there is only one quiz in the module, it should be labelled as "Quiz". If there is more than one each header should be structured as "Quiz: label" where "label" is a short (ideally 1-2 words) description of the content covered in the question(s). E.g., "Quiz: Scatterplots"

```
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
```

### Multiple choice

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

You can have questions with multiple correct answers. 

```
Select all of the following correct choices:

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
```

Select all of the following correct choices:

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

```
True or False: This statement is NOT true. ;)

[( )] TRUE
[(X)] FALSE
***
<div class = "answer">

Here is the answer box for this question.

</div>
***
```

True or False: This statement is NOT true. ;)

[( )] TRUE
[(X)] FALSE
***
<div class = "answer">

Here is the answer box for this question.

</div>
***

### Short answer/text response 

Note that, without any additional script, to get it marked "correct" the learner has to enter it exactly as you do.
We can allow some flexibility in what we accept as correct answers for text by adding a little script after the answer, though. For the following, either "right answer" or "correct answer" (not case sensitive) will be accepted:

```
What is the right answer?

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
```

What is the right answer?

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

With flexible answers like this, it's definitely a good idea to include a follow-up to help the learner put their answer in context.

For example, if the question was "Name one or more colors" with acceptable answers including red, orange, yellow, green, blue, and purple, and they wrote "red, green, and the center of a black hole" that would be marked as correct because it contains at least one string from the acceptable list. Similarly, "hammered metal" would be marked as correct because it contains the string "red" ([you can prevent this if you want](https://www.w3schools.com/jsref/jsref_regexp_begin.asp)). On the other hand "teal, scarlet, indigo" would be marked wrong.

```
What are some items?

[[this text will never show up if they type a right answer and click "Check", only if they click the checkmark button to reveal the answer]]
[[?]] Hint: The answers are like "item1", "item2", etc.
<script>
  let input = "@input".trim();
  /item1|item2|item3|item4/i.test(input);
</script>
***
<div class = "answer">

Reiterate what the correct answer or answers should be, and try to anticipate likely wrong answers so you can explain why they're not correct.

</div>
***
```

What are some items?

[[this text will never show up if they type a right answer and click "Check", only if they click the checkmark button to reveal the answer]]
[[?]] Hint: The answers are like "item1", "item2", etc.
<script>
  let input = "@input".trim();
  /item1|item2|item3|item4/i.test(input);
</script>
***
<div class = "answer">

Reiterate what the correct answer or answers should be, and try to anticipate likely wrong answers so you can explain why they're not correct.

</div>
***

Note that you can use any markdown formatting you want in quizzes, including bold, links, math, lists, embedded media, code blocks, etc. 
For accessibility for learners using screenreaders, if your question is more than a single markdown paragraph, you must enclose it in `<div>` tags. For example:

````
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
````

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

Sometimes you may wish to include a quiz question that would be impossible to automatically grade (i.e. one with an open-ended repsonse). 
To mark all possible answers as correct, use a brief script to match everything with regex:

```
Take a look at your samples. Which sample(s) looks the best in terms of per base sequence quality? Which sample(s) look the worst?

[[describe sample quality]]
<script>
  let input = "@input".trim();
  /.*/i.test(input);
</script>
***
<div class = "answer">

(Note that we can't automatically grade an open-ended question like this, so it will be marked "correct" no matter what you write.)

All of the reads contain usable data, but the quality decreases toward the end of the reads.

</div>
***
```

Take a look at your samples. Which sample(s) looks the best in terms of per base sequence quality? Which sample(s) look the worst?

[[describe sample quality]]
<script>
  let input = "@input".trim();
  /.*/i.test(input);
</script>
***
<div class = "answer">

(Note that we can't automatically grade an open-ended question like this, so it will be marked "correct" no matter what you write.)

All of the reads contain usable data, but the quality decreases toward the end of the reads.

</div>
***


There are many more options and examples of quiz questions in the LiaScript documentation. [Read more about quiz syntax here.](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md#quizzes)


## Ungraded quiz questions

Useful formative assessment doesn't have to be an actual quiz question. 

You can ask questions with no graded answer as well. LiaScript calls these [surveys](https://liascript.github.io/course/?https://raw.githubusercontent.com/LiaScript/docs/master/README.md#111).

Here's an ungraded question with a text box three lines long:

```
[[___ ___ ___]]
```

[[___ ___ ___]]

Here's one that's just one line long:

```
[[___]]
```

[[___]]

Hints and follow-up explanations don't work for survey questions, but you can use [html detail tags](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) to create a solution that won't be visible to the learner until they choose to open it. For example:

```
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
```

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

````
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
````

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

````
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
````

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

## Updating this document

**This is verison @version of this document.**

When you update docs.md, be sure to [increment its version](https://github.com/arcus/education_modules/blob/main/versioning_guidelines.md) in the front matter.

For any **major** updates to docs.md, you should also provide an issue template checklist for bringing modules up to date with the new version of docs. 
For example, see the [checklist for docs v1](https://github.com/arcus/education_modules/blob/main/.github/ISSUE_TEMPLATE/docs_update_checklist_v1.md).
This will create a new option in our list of available issues (see [create a new issue](https://github.com/arcus/education_modules/issues/new/choose)), which we can then use to bring all of the current modules up to date with the new guidelines. 

If a module misses a round of updates (e.g. it never gets updated for docs 1.0.0 but there's already a docs 2.0.0 out), then it will need to go through all of the checklists to bring it up to date. 

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

If you're planning major updates to docs.md, it's a good idea to start your checklist issue template right at the beginning of your editing process and add to it gradually as you make changes in docs.md so you don't forget anything.

</div>

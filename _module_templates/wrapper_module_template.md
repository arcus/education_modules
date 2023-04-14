<!--

author:   Your Name
email:    email@chop.edu
version:  0.0.0
module_type: wrapper
module_template_version: 1.0.0
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


import: https://raw.githubusercontent.com/arcus/education_modules/template_test/a_sample_module_template/module_macros.md
-->

# Module Title

@overview

## Instructions for authors

This is the template for **wrapper modules**. 
This template should be used when a module is more than 50% content that is embedded or linked to.
If more than half of the module content is in the LiaScript markdown itself, then the other template should be used, even if that content is primarily adapted from other open source content.

To see how to use this **wrapper module** template, you'll need to look at this file in its [raw format](https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/wrapper_module_template.md).
To see what it looks like rendered via LiaScript, [click here](https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/wrapper_module_template.md) or go to [https://liascript.github.io/](https://liascript.github.io/) and paste the link to the **raw** file into the box on that page and click "load course".
This template is **not** a great example of what a real module should look like, though. 

To see what real modules look like, see [our list of completed modules](https://arcus.github.io/education_modules/list_of_modules).
If this is your first time writing a module, be sure to check out our [contributors guide](https://github.com/arcus/education_modules/blob/main/CONTRIBUTING) before you get started.

Some important things to keep in mind:

- We use "macros" for a lot of our standardized text. For exmaple, the overview and feedback sections of each module are created by the `@overview` and `@feedback` macros, respectively. All available macros are in the [module macros file](https://github.com/arcus/education_modules/blob/main/_module_templates/module_macros.md). For more information about our macros and instructions for writing new ones, see the [macros instructions](https://github.com/arcus/education_modules/blob/main/macros_instructions.md).
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

## Lesson Preparation

This module will direct you to external educational content.
---

Many topics have great content written by others! We chose this content for you based on how well it meets our criteria.

Not all selected materials will meet all of these criteria, but selected materials should meet as many as possible.
Write a short sentence about how this material meets, or does not meet, each criterion.

**Resource 1 Name**

Short optional summary sentence about resource 1.

<ul style="list-style-type: none">
   <li><i class="fa-solid fa-circle-check" style="color: #158d0c;" title="Checked"></i> Expert Authors / Well-Vetted: _who are the expert authors? or what institutional authority guarantees accuracy?_</li>
   <li><i class="fa-solid fa-circle-minus" style="color: #f0bc00;" title="Unchecked"></i> Maintained: _who is in charge of implementing regular updates to this material, important in fast-changing fields._</li>
   <li><i class="fa-solid fa-circle-check" style="color: #158d0c;" title="Checked"></i> Stable Support: _who hosts this material so it won't disappear? If it does, please let us know in a feedback form ASAP!_</li>
</ul>

**Known issues with accessibility and inclusive design:** Explain any known problems related to accessibility and inclusive design here. If there are none, you can write "No known issues, but we may have missed something. If you encounter an issue, please [let us know in our feedback form](#feedback)!"

**Resource 2 Name**

Short optional summary sentence about resource 2.

<ul style="list-style-type: none">
   <li><i class="fa-solid fa-circle-check" style="color: #158d0c;" title="Checked"></i> Expert Authors / Well-Vetted: _who are the expert authors? or what institutional authority guarantees accuracy?_</li>
   <li><i class="fa-solid fa-circle-minus" style="color: #f0bc00;" title="Unchecked"></i> Maintained: _who is in charge of implementing regular updates to this material, important in fast-changing fields._</li>
   <li><i class="fa-solid fa-circle-check" style="color: #158d0c;" title="Checked"></i> Stable Support: _who hosts this material so it won't disappear? If it does, please let us know in a feedback form ASAP!_</li>
</ul>

**Known issues with accessibility and inclusive design:** Explain any known problems related to accessibility and inclusive design here. If there are none, you can write "No known issues, but we may have missed something. If you encounter an issue, please [let us know in our feedback form](#feedback)!"

The structure of this module:
---
Give learners a short, concrete, description of what they will do. This might look like:

Example Structure 1:

1. Read about how this topic fits into some bigger picture here in this LiaScript course.
2. Do the activities embedded in this module (using iFrames).
3. Answer a few questions to make sure you understood the key parts.

Example Structure 2:

1. Open this external resource in a new browser window.
2. Read Chapter 1 and do the activities at the end.
3. Return to this LiaScript course to answer a few questions to make sure you understood the key parts.

Example Structure 3:

1. Open this external resource in a new browser window.
2. Read Section 2.1 and 2.2.
3. Return to this LiaScript course to do an activity.
4. Answer a few questions (again in the LiaScript course) to make sure you understood the key parts.
These are just some examples of possible structures. The specific structure will depend greatly on the particular external module/educational resource you are using.

Wrapper modules may or may not include much text in the LiaScript file itself. 
For instructions and examples about including embedded media, highlight boxes, math, code, and quiz questions, see the [standard module template](https://github.com/arcus/education_modules/blob/main/_module_templates/standard_module_template.md).

## Additional Resources

The last section of the module content should be a list of additional resources to learn more about this topic.

Avoid linking to other modules we've written here.

## Feedback
@feedback

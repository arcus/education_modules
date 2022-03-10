```
# Module Quality Assurance Report for PR #[PR number here]
----
Date: {yyyy-mm-dd}
Reviewer: {your name}
qa_template_version: 2.0.0
Name of Module: {take from the title of the main markdown in the PR}
Current Liascript URL: {makes it easy for reviewers and authors to look at content as learners will}
Current Version of Module (use the latest commit value):  {click on the PR and get the clickable short link to the latest commit -- see [quality_assurance_guide.md](quality_assurance_guide.md)}

# Checklist Reports:

## [Directory structure](how_to.md/#Begin-Writing)
* [ ] Folder and file names use lowercase and underscores (no dashes)
* [ ] Main module directory folder name is identical to the name of the module content markdown file.
* [ ] Images, videos, and other audio-visual assets are saved within a `media` folder within the module directory

## Module Organization
* [ ] YAML is at the very top of the file
  * [ ] author name
  * [ ] email
  * [ ] module version number of at least 1.0.0 if first public version or if this is an update then an [appropriately incremented version number](versioning_guidelines.md)
  * [ ] module_template_version number is up to date with the [current sample module](https://raw.githubusercontent.com/arcus/education_modules/main/a_sample_module_template/a_sample_module_template.md) -- if not, the module should be brought in line with any changes that have occurred to the module template before continuing with QA
  * [ ] language
  * [ ] narrator
  * [ ] comment appropriately filled out
  * [ ] long_description appropriately filled out
  * [ ] learning_objectives appropriately filled out
  * [ ] link to CSS (currently https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css)
  * [ ] script to Font Awesome kit (currently https://kit.fontawesome.com/83b2343bd4.js)
* [ ] Title is the first line after the end of the YAML
  * [ ] only level-1 header in the entire document.
* [ ] Overview section immediately following Title
  * [ ] surrounded in div with class overview
  * [ ] Comment is at the top of the Overview, linked from YAML rather than rewritten
  * [ ] "Is this module right for me?" contents linked from long_description YAML rather than rewritten
  * [ ] "Estimated time to completion" contents linked from estimated_time YAML rather than rewritten
  * [ ] Prerequisites listed and do not require learner to have specifically attained those skills through any of our other modules.
  * [ ] Learning objectives linked from learning_objectives YAML rather than rewritten
* [ ] All sections following Overview have content (no pages with just header and no additional text / media material).
* [ ] All quizzes start with a level 2 or 3 header. If there is only one quiz in the module, it is labelled "Quiz", or if there are multiple, each header is structured as "Quiz: label" where "label" is a short (~ 1-2 words) description of the content covered in the question(s). E.g., "Quiz: Scatterplots"
* [ ] Educational content ends with a section of additional resources, both ours and outside sources
* [ ] Final section is Feedback.
  * [ ] Learning objectives linked from YAML rather than rewritten
  * [ ] Feedback link is updated appropriately to automatically fill in the module name when clicked by learner.

## Module Content

* [ ] Complexity of the material covered seems appropriate given prerequisites.
* [ ] Time estimate appears accurate for a learner of the targeted level.
* [ ] Clearly defined learning objectives using strong, descriptive verbs. (See [Bloom's taxonomy](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/) for ideas.)
* [ ] Every learning objective is covered in the module content.
* [ ] All major topics covered are represented by a learning objective -- there's no significant knowledge imparted that isn't specified in the learning objectives
* [ ] The module title, blurb/comment, and long description accurately reflect the content of the module.
* [ ] Headers are informative and follow a sensible hierarchical structure (the TOC in the left margin should give a good overview of the content covered)
* [ ] Avoids unclear language: unexplained idioms or references, unexplained acronyms, unnecessary technical language.
* [ ] Unusual words, or words taking on a very specific meaning in context, are always defined for the learner, either on the page (e.g. using footnotes) or with links to a definition/glossary.
* [ ] Provides pronunciation guides for any especially unusual words of particular importance (a common example is package names, such as dplyr)
* [ ] Avoids unnecessarily gendered language (e.g. uses "they" singular rather than "he or she" for an unknown person).
* [ ] Informative link text (e.g. instead of "To learn more about python, click [here](www.example.com)", say "Read this article to [learn more about python](www.example.com).")
* [ ] Uses specially formatted highlight boxes consistently and appropriately
* [ ] Short, digestible pieces --- avoids long paragraphs and breaks long sections up with sub-headers
* [ ] All links work (See [Branch References to Change prior to PR Approval](#Branch-References-to-Change-prior-to-PR-Approval) for a place to keep track of internal references that will need to be updated.)
* [ ] Spelling and grammar are correct.


## Code availability
If the module includes code that learners may want to run:
* [ ] A link is provided to run the code in binder
* [ ] A link to the raw code and any other necessary materials (e.g., data) is provided for learners who prefer to work on their own machine

## Formative assessment

* [ ] Sufficient [formative assessment](https://carpentries.github.io/instructor-training/02-practice-learning/#identifying-and-correcting-misconceptions) in the form of quizzes and/or hands-on exercises
* [ ] Clear explanations available after questions unless the nature of the question itself or answer options makes it unnecessary (e.g. a T/F question may not always require follow-up explanation)
* [ ] Quiz questions and hands-on exercises relate directly to learning objectives
* [ ] Every learning objective has at least one associated question
* [ ] Questions can be answered based on the content within the module alone; learners should not need to have read or consulted any of the linked external resources

## Videos and images

* [ ] Screencasts cover a single coherent task so the recording is a short as is feasible. To demonstrate more than one related task, include several short screencasts in succession rather than recording one long screencast.
* [ ] Subtitles available for every recording with audio.
* [ ] Alt text is specified for each image. For help writing and assessing descriptive alt text, see this [alt text image concepts guide](https://www.w3.org/WAI/tutorials/images/) and this [alt text decision tree](https://www.w3.org/WAI/tutorials/images/decision-tree/).
  * [ ] Alt text never starts with "photo of", "screenshot of", "image of", or any other information describing the medium of the image (the only exception to this is when describing data visualization -- it is appropriate to start alt text with "a scatterplot...", for example)
  * [ ] Alt text is written to provide the same relevant information to someone using a screen-reader as provided to someone who accesses the information visually
    - E.g., rather than "Screenshot of PR with multiple commits", alt text says 'On a pull request, the PR comment appears at the top. Below, commits appear as their commit summary followed by commit hash.'
  * [ ] For any images that provide a function when clicked, the alt text describes the function of the button rather than describes the visual aspects of the button.
    - E.g., if an image of the GitHub logo is intended to be clicked on to access the education_modules repository, it is labelled "arcus education_modules GitHub repository" rather than "GitHub logo". If this information is also accompanied by a descriptive link in the text, however, then a blank alt tag is appropriate.
  * [ ] Alt text is ideally a maximum of 125 characters, or as close to this as possible.
  * [ ] Purely [decorative visuals](https://www.w3.org/WAI/tutorials/images/decorative/) ([other examples](https://www.portent.com/blog/design-dev/decorative-images-how-to-identify-and-tag-them-for-accessibility.htm)) have a blank alt text label: `![""](image_path)` Note that this is *not* the same as not specifying alt text at all: `![](image_path)`
* [ ] Important visuals (in video, image, or gif) are always described in the audio or in accompanying text.
  - For example, in a screencast, instead of just, "And then click here," provide description that could help scaffold someone without visual access like, "And then click on the button that says 'Run' in the top-right corner of the screen". Be sure to make use of text cues when available (e.g. button labels), not just visual signals like color or location.
  - When important content is conveyed in a visual, describe the key elements. For example, "Running this query produces the table below. It displays the first 5 rows by default, and columns for ID, encounter ID, diagnosis, and outcome."
  - When including a data visualization, describe important features, such as both axis labels and visible trends in the data. For example, "Here's a scatterplot showing number of encounters on the y-axis and age on the x-axis. All 183 patients from our sample are represented here, and it looks like a weak positive trend, with older patients being more likely to have had more encounters. There are a few important outliers, though, such as this patient at about 6 months old with more than 20 encounters already."
  - When visual information is repeated with minimal changes, it's fine to indicate that without providing a full description again. For example, "And here's the updated table, filtered to only show patients who have been seen in the last 2 years."
  - When important visual information in a video is too complex to include sufficient audio description (i.e. it would slow the content down so much as to impair its utility), an alternative video file should be provided with audio descriptions included.
* [ ] Color is never the sole method for distinguishing visual content (including in data visualizations).

## Branch References to Change prior to PR Approval

List here any internal references (stated or hyperlinked) that work now because they refer to the named branch, but will not work once this is on the main branch and the named branch is deleted. Prior to approving the PR and merging to main, all references should be updated in a new commit.

(If there are none, the reviewer can either check off the boxes below without making any edits, or can remove the items below and replace with the text "None".)

* [ ] {description or quote, line ___ in file ____}
* [ ] {description or quote, line ___ in file ____}
* [ ] {description or quote, line ___ in file ____}

## Just Before Approval
* [ ] Once there are no more commits to be made, get the newest commit value for the PR and update the commit value ("Current Version of Module:") at the top of this document.

Congratulations! You can now approve the PR, merge to main, and close (not delete) this issue.
```

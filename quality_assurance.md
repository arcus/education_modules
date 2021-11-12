# Quality Assurance for modules

When a module creator is ready to request that their module be included, they will create a Pull Request (PR).  This begins the work of quality assurance.

# Create an Issue

Go to https://github.com/arcus/education_modules/issues

New Issue (green button) - screenshot Here

Give title: QA [proposed directory name] (example QA reproducibility)

In body, put the title "Module Quality Assurance Report" plus number of the PR (preceded by hash #) and GH will auto link it on the first line

# Module Quality Assurance Report for PR #[pr#]  
----
Date: yyyy-mm-dd
Reviewer: your name
Name of Module: take from the title of the main markdown in the PR
Current Liascript URL: [makes it easy for reviewers to look at content as learners will]
Current Version of Module (use the latest commit value):  [click on the PR and get the clickable short link to the latest commit -- add screenshot here]
Checklist Reports:

## Content

* [ ] Good amount of content, both in terms of the complexity/usefulness of the material covered and the time estimate
* [ ] Clearly defined learning objectives using strong, descriptive verbs. (See [Bloom's taxonomy](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/) for ideas.)
* [ ] Every learning objective is covered in the module content.
* [ ] There are no tangents or mission creep in the module content, straying from the learning objectives.
* [ ] No betrayal of expectations: The module title, description, learning objectives, time estimate, and overview all accurately reflect the content of the module. A learner should be able to make an informed decision about whether or not to complete the module.
* [ ] Avoids unclear language: unexplained idioms or references, unexplained acronyms, unnecessary technical language.
* [ ] Unusual words, or words taking on a very specific meaning in context, are always defined for the user, either on the page (e.g. using footnotes) or with links to a definition/glossary. Provides pronunciation guides for especially unusual words of particular importance.
* [ ] Provides content in a variety of forms and styles: screencasts, text, webinars/lectures, practical exercises, etc. Whenever possible, multiple forms/styles should be incorporated in each module so learners have multiple avenues to the content.
* [ ] Avoids unnecessarily gendered language (e.g. uses "they" singular rather than "he or she" for an unknown person).
* [ ] Informative link text (e.g. instead of "To learn more about python, click [here](www.example.com)", say "Read this article to [learn more about python](www.example.com).")
* [ ] Includes accurately formatted and functional link to feedback form.

## Organization

* [ ] Clear, informative headers and sensible hierarchical structure (the TOC in the left margin should give a good overview of the content convered)
* [ ] Adheres to the module template structure
* [ ] Uses specially formatted highlight boxes consistently and appropriately
* [ ] Short, digestible pieces --- avoids long paragraphs and breaks long sections up with sub-headers

## Formative assessment

* [ ] Frequent [formative assessment](https://carpentries.github.io/instructor-training/02-practice-learning/#identifying-and-correcting-misconceptions) in the form of knowledge checks and/or hands-on exercises
* [ ] Clear explanations available after questions unless the nature of the question itself or answer options makes it unnecessary (e.g. a T/F question may not always require follow-up explanation)
* [ ] Knowledge check questions and hands-on exercises relate directly to learning objectives

## Videos and images

* [ ] Screencasts cover a single coherent task so the recording is a short as is feasible. To demonstrate more than one related task, include several short screencasts in succession rather than recording one long screencast.
* [ ] Subtitles available for every recording with audio.
* [ ] Alt text available for every image.
* [ ] Important visuals (in video, image, or gif) are always described in the audio or in accompanying text.
  - For example, in a screencast, instead of just, "And then click here," provide description that could help scaffold someone without visual access like, "And then click on the button that says 'Run' in the top-right corner of the screen". Be sure to make use of text cues when available (e.g. button labels), not just visual signals like color or location.
  - When important content is conveyed in a visual, describe the key elements. For example, "Running this query produces the table below. It displays the first 5 rows by default, and columns for ID, encounter ID, diagnosis, and outcome."
  - When including a data visualization, describe important features, such as both axis labels and visible trends in the data. For example, "Here's a scatterplot showing number of encounters on the y-axis and age on the x-axis. All 183 patients from our sample are represented here, and it looks like a weak positive trend, with older patients being more likely to have had more encounters. There are a few important outliers, though, such as this patient at about 6 months old with more than 20 encounters already."
  - When visual information is repeated with minimal changes, it's fine to indicate that without providing a full description again. For example, "And here's the updated table, filtered to only show patients who have been seen in the last 2 years."
  - When important visual information in a video is too complex to include sufficient audio description (i.e. it would slow the content down so much as to impair its utility), an alternative video file should be provided with audio descriptions included.
* [ ] Color is never the sole method for distinguishing visual content (including in data visualizations).

## Branch References to Change prior to PR

List here any internal references (stated or hyperlinked) that work now because they refer to the named branch, but will not work once this is on the main branch and the named branch is deleted.

* [ ] description or quote, line ___ in file ____
* [ ] description or quote, line ___ in file ____
* [ ] description or quote, line ___ in file ____


Click "Submit new issue" (don't worry about doing the checkboxes ahead of time, the issue creator and maybe PR reviewers? check on this can do them at any point after creating the issue)

Once you create the issue, then go through and actually evaluate the checklists and communicate with the author using comments on the issue (put in screenshot) and @ the author.  Be as precise as possible (e.g. what file, what line, what problem are you referring to?)

The author may make fixes to their code and commit to the branch.  This will simply update their PR.  This means that you will want to change the version in the top part of the issue (show screenshot of how to edit the main issue) with the commit hash for the now current version.

Once you are satisfied with the quality of the module (don't worry, it can always be improved, this is a best effort only, no perfection expected or implied), the last thing to do before the PR is to make sure that any changes to references within the material relating to the branch name are resolved (see the last bit of the copy-paste issue code).  Issue a final comment reminding the author to handle this in a new commit.  Check that commit and if all is well, approve the PR.

In general we should not delete issues or comments on issues, because they provide a useful history of the project.


Technical Issues (ie. links work, media plays work…etc.):
General Suggestions for Improvement:



Technical Issues (ie. links work, media plays work…etc.):

General Suggestions for Improvement:

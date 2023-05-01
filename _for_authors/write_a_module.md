# How to Create an Educational Module

This document describes how to create and submit an educational module for inclusion in the Children's Hospital of Philadelphia / Drexel University "Educational Pathways in Biomedical Data Science" program, financed by NIH and institutional funding by recipient organizations.

Contents of this document include:

* [Choose a Topic](#choose-a-atopic)
* [Begin Writing](#begin-writing)
* [Use GitHub](#use-github)
* [Checklists and Reports](#checklists-and-reports)

## Choose a Topic

It's tempting to jump in and start creating, but a few preliminary plans about how you'd like to proceed may save you a lot of time.  Please read this entire document and view some of the existing modules to understand how module materials are organized and what topics are appropriate.  To start, here are some priorities we keep in mind when we make a judgement on approving the inclusion of a module:

<details>
<summary>FAIR Principles</summary><br/>

The educational modules in this project both promote [FAIR principles](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4792175/) as described by NIH and attempt to embody these principles.  Our materials should be Findable, Accessible, Interoperable, and Reusable, and advocate these overarching priorities in the application of data science to research.  

As part of our FAIR methodology, we give our materials away free of charge and free of limits on their use, as long as proper citation is given.  You may not include proprietary data or intellectual property in your module, limit your module's use to only your institution, or promote commercial tools or resources that you have financial interest in.  In our use of the FAIR principles we prioritize whenever possible the use of and instruction in free, open-source software (FOSS) rather than commercial products.  If you would like to create a module teaching the use of a commercial resource, consider whether FOSS products can provide as good or better a research experience, with as good or greater FAIR data outcomes.  For example, Microsoft Excel is paid software (perhaps less accessible in lower resourced settings) in which data analytics is not particularly reusable (a script in R or Python can capture all of the steps of an analysis while an Excel spreadsheet cannot).  Instead of describing how to do a task in Excel, describe how to do it in a FOSS alternative instead, such as R within the RStudio IDE.
</details>

<details>
<summary>Inclusive Design</summary><br/>

We expect authors to design with a variety of ["edge" users](https://guide.inclusivedesign.ca/activities/inclusive-design-mapping/) in mind: those with limited access to visual content or auditory content, those with barriers related to attention, cognition, sensory processing, or language, and those with limited technology access and/or financial resources.  Wherever possible we encourage a multi-modal approach to education, such that no instruction relies solely on a single type of communication (text, video, audio, images, code) but provides several ways to engage with materials.  Our [inclusivity guidelines can be found below](#Inclusivity_Guidelines).

</details>

<details>
<summary>Topic, Audience, and Scope </summary><br/>

We aim to provide data analytics and closely related skills to researchers at all levels.  We hew closely to the [NIH Strategic Plan for Data Science](https://datascience.nih.gov/sites/default/files/NIH_Strategic_Plan_for_Data_Science_Final_508.pdf), and the modules we write should be linked to a particular objective and/or tactic of this Strategic Plan.  The topic should be relevant to the conduct of research and should clearly state both what pre-requisite knowledge or skills are necessary prior to engaging with the material, and some contextualization of why the topic matters for researchers.  

A module in this project will be brief (one hour or less) and therefore of limited, well-described scope.  Consider not only what you teach about, but what you intentionally exclude.  It may be useful to map a plan of 2, 3, or more modules that teach related skills and together provide broad coverage, but remember that modules are freestanding.  Modules can describe pre-requisite skills, but cannot ask learners to have acquired the necessary skills from other modules.  For example, a module covering the use of n-grams in NLP should not include a pre-requisite such as "previous completion of the module Introduction to NLTK in Python", but could include "previous experience with NLTK and the ability to ingest text data in Python", perhaps with a link to a related module for learners who would like to acquire such experience there.

</details>

## Begin Writing

### Name Files and Folders

Make a folder with an expressive name, using lower case and underscores, like `lasso_and_ridge_ml_in_R` or `bayesian_stats_in_python`.  This will hold all of the files that are unique to your module.

To start writing the main file that will make up your module, use [a sample module template](a_sample_module_template/a_sample_module_template.md) as your basis.  Make a copy of this and save it within your new folder with an almost identical title to the folder, one that ends in `.md`, like `lasso_and_ridge_ml_in_R.md` or `bayesian_stats_in_python.md`.  This template includes some boilerplate text to show you how to write in Liascript flavored markdown (it's pretty similar to other markdown flavors, but with a few things added in). It also includes information about important elements needed to meet our requirements for a module, such as including formative assessment.

Importantly, starting with your overview text will help you scope your topic.  Three to five learning objectives are plenty for a module of about one hour's duration.

### Save Assets Well

Images, videos, and other audio-visual assets that you want to include should be saved in a folder within your main folder, called `media`.  Code samples that you want to include should go in a folder named `code`.
Consider the following directory tree as a sample showing you how your lesson might look:

```
└── lesson_name
    ├── lesson_name.md
    ├── media
    │  ├── some_video.mp4
    │  └── some_image.png
    └── code
        ├── some_markdown.Rmd
        ├── python_sample.ipynb
        └── to_be_completed.R
```

## Use GitHub

New module submissions belong on their own branch while they are still in progress.  Only once a module has been approved and passed all quality checks may a PR (pull request) be merged to the main branch.  Create a new branch that is descriptive, and commit your changes to that branch and publish it to the repository (either the canonical repository, if you are a collaborator, or to your fork of the canonical repository, if you are an offsite potential collaborator).  Use descriptive commit messages and leave all changes on your new branch until you are ready to ask for module approval.

When you're ready to request approval, create a Pull Request in GitHub, asking to merge your branch into main.  Include a comment describing the module.  An administrator of the repository will create a new Issue in the repository, citing your PR.  The administrator will apply the [module quality assurance checklist](quality_assurance_template.md) and may reply with requests for updates within issue comments.  Feel free to conduct a conversation through the comments on the issue, which will endure in time, while your PR will not.  Comments on the issue are a better practice for historical records.

Once any outstanding improvements are addressed, the administrator checking your module will approve the PR with a squash and merge and delete your branch.  Congratulations, your module is now part of the portfolio of educational modules for the project!

### Inclusivity Guidelines

This is a working document articulating our goals and standards for creating content that will be valuable and accessible to as wide a range of users as possible. Specifically, we are designing with a variety of ["edge" users](https://guide.inclusivedesign.ca/activities/inclusive-design-mapping/) in mind: those with limited access to visual content or auditory content, those with barriers related to attention, cognition, sensory processing, or language, and those with limited technology access and/or financial resources. A core principle is to allow users as much flexibility as possible to configure their learning experiences to meet their own needs and preferences.

The guidelines presented here are inspired by several other guides including the [Web Content Accessibility Guidelines WCAG21](https://www.w3.org/WAI/WCAG21/quickref) and [The Inclusive Learning Design Handbook](https://handbook.floeproject.org/approachesoverview). Recommendations specific to educational videos can be found [here](https://ctl.wiley.com/how-to-ensure-accessibility-for-educational-videos/).

#### Guidelines

* Maximize opportunities for users to customize their own learning experience
  - Relevant information should be provided for each module upfront to help users decide which ones to do and which to skip: time estimate, expected learning outcomes, etc.
  - Provide content in a variety of forms and styles: screencasts, text, webinars/lectures, practical exercises, etc. Whenever possible, multiple forms/styles should be incorporated in each module so learners have multiple avenues to the content.
* Make text alternatives available by default for all visual and audio content
  - Subtitles available for every video with audio.
  - Alt text available for every image.
* Provide audio description for visuals presented in video
  - For example, in a screencast, instead of just, "And then click here," provide description that could help scaffold someone without visual access like, "And then click on the button that says 'Run' in the top-right corner of the screen". Be sure to make use of text cues when available (e.g. button labels), not just visual signals like color or location.
  - When important content is conveyed in a visual, describe the key elements. For example, "Running this query produces the table below. It displays the first 5 rows by default, and columns for ID, encounter ID, diagnosis, and outcome."
  - When including a data visualization, verbally describe important features, such as both axis labels and visible trends in the data. For example, "Here's a scatterplot showing number of encounters on the y-axis and age on the x-axis. All 183 patients from our sample are represented here, and it looks like a weak positive trend, with older patients being more likely to have had more encounters. There are a few important outliers, though, such as this patient at about 6 months old with more than 20 encounters already."
  - When visual information is repeated with minimal changes, it's fine to indicate that without providing a full description again. For example, "And here's the updated table, filtered to only show patients who have been seen in the last 2 years."
  - When important visual information is too complex to include sufficient audio description (i.e. it would slow the content down so much as to impair its utility), an alternative video file should be provided with audio descriptions included.
* Use color choices that maximize accessibility
  - Color should never be the sole method for distinguishing visual content
* Provide clear, consistent organization and content structure to reduce cognitive load for users
  - Use clear, informative headers for each subsection. The resulting table of contents should give a good sense of the flow and structure of the module. Avoid titles and headers that sacrifice clarity for playfulness.
  - Use parallel structure across modules covering similar content.
  - Use consistent formatting (e.g. consistent page headers and footers, consistent style controlled by css file)
* Reduce language barriers
  - The language of each page is identified in the HTML (e.g. `<html lang="en-US">`)
  - Unusual words, or words taking on a very specific meaning in context, should be defined for the user, either on the page (e.g. using footnotes) or with links to a definition/glossary
  - Provide pronunciation guides for especially unusual words of particular importance
* Take proactive steps to be welcoming to a diverse group of potential users
  - Avoid unnecessarily gendered language (e.g. use "they" singular rather than "he or she" for an unknown person)
  - Intentionally represent diversity in our examples and images
  - Strive for diverse voices in the people presenting our content (e.g. webinars), and in the sources we direct users to  

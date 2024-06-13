# How to Create an Educational Module

This document describes how to create and submit an educational module for inclusion in the Children's Hospital of Philadelphia / Drexel University "Educational Pathways in Biomedical Data Science" program, financed by NIH and institutional funding by recipient organizations.  Creating an educational module is considerably different than creating a manuscript, so please read this entire document to get an idea of how to work with us to add your expertise!

Contents of this document include:

* [Module Audience](#module-audience): We are writing for biomedical researchers.
* [Topics](#topics): What topics do we write about?  What are we actively soliciting?
* [Our Approach](#our-approach): We explore the values we abide by in our writing.
* [Use GitHub](#use-github): Our files are stored and version controlled using GitHub.
* [Composition](#composition): How to practically write a module, including naming conventions.

## Module Audience

We aim to provide data analytics and closely related skills to **biomedical researchers** at all levels (from undergraduate students to senior faculty) and regardless of geographical location.  We believe that biomedical researchers have specific needs that can be addressed in terms of topics we cover as well as in terms of our pedagogical approach.  This is one of the characteristics that makes our approach useful -- there is certainly no dearth of tutorials or articles or blog posts about data science techniques, but there *is* a lack of material that is aimed specifically at biomedical researchers, aimed at improving their research and their careers. Biomedical researchers are often problem-oriented and practical and enjoy narrowly scoped modules that clearly state what practical, research-related tasks they teach.  

## Topics

In terms of topics, we hew closely to the [NIH Strategic Plan for Data Science](https://datascience.nih.gov/sites/default/files/NIH_Strategic_Plan_for_Data_Science_Final_508.pdf), and the modules we write should be linked to a particular objective and/or tactic of this Strategic Plan.  The topic should be relevant to the conduct of research and should clearly state both what pre-requisite knowledge or skills are necessary prior to engaging with the material, and some contextualization of why the topic matters for researchers.  

For example, a module that describes how to create publication-quality cohort characteristics tables for research papers in the R language may be more attractive to learners than a module that focuses on how to write functions in the R language, even if the modules end up teaching similar skills.  It's easy for a researcher to understand how table creation helps their research, but they may have no idea why writing a function is interesting or helpful to them.  When thinking about topics to write about, consider the research data life cycle and the process of conducting research.  If you're not familiar with biomedical research, but have expertise to offer, we're happy to talk to you about what the research process looks like and some of the data science pain points our learners experience. 

We maintain a [list of the specific topics](module_development_plans.md) that are our highest priority for new module development, as well as what modules are currently planned or in development. 
If you are interested in writing a module on any of the topics in that list, that would be tremendously helpful!

Are you considering a topic and want to know what we think about your idea?  Please email us at [dart@chop.edu](mailto:dart@chop.edu).  We'd love to hear from you and we are enthusiastic about working with authors to hone their topic!

## Our Approach

While each educator's voice is unique, this program has some core values that shape our approach.  Our values and the particular approach we take in this project affects how we write, what we write about, how we share our materials, and how we improve our materials.

### Pedagogy

In terms of pedagogical approach, we acknowledge that biomedical researchers are busy and have a number of competing demands on their time.  For this reason we want our modules to be narrowly scoped and require one hour or less for completion.  Researchers also face a competitive funding and publishing environment and are often expected to demonstrate expertise and confidence not only in their area of previous training but in novel domains as well.  This can create, in some learners, a reticence to appear unknowledgable and a decreased tolerance for failure.  These learners need to develop metacognitive skills that build confidence and robustness to failure (a necessary stage of computer programming skill acquisition).  Because of the communal nature of science, biomedical researchers also need to develop the practical skills and attitudes necessary for a community approach to data science problem solving.  This includes learning how to ask questions effectively, learning terminology for useful online searches, and developing skills in collaboration tools such as version control software.  We have created a template which includes detailed scaffolding to help you develop a module that reflects our pedagogical values.

### FAIR Principles

The educational modules in this project both promote [FAIR principles](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4792175/) as described by NIH and attempt to embody these principles.  Our materials should be Findable, Accessible, Interoperable, and Reusable, and advocate these overarching priorities in the application of data science to research.  We give priority to materials that have the greatest possibility of wide-ranging use across various biomedical domains, geographic areas, and other contexts.  

### Free, Open Source Software (FOSS)

In our use of the FAIR principles we prioritize whenever possible the use of and instruction in free, open-source software (FOSS) rather than paid proprietary software.  If you would like to create a module teaching the use of a paid resource, consider whether FOSS products can provide as good or better a research experience, with as good or greater FAIR data outcomes.  For example, Microsoft Excel is paid software (perhaps less accessible in lower resourced settings) in which data analytics is not particularly reusable (a script in R or Python can capture all of the steps of an analysis while an Excel spreadsheet cannot).  Instead of describing how to do a task in Excel, describe how to do it in a FOSS alternative instead, such as using R or Python within a notebook or markdown document.

### Licensing

As part of our FAIR methodology, we give our materials away free of charge and free of limits on their use, as long as proper citation is given.  We do this via our use of the [Creative Commons Attribution-ShareAlike 4.0 International license](https://github.com/arcus/education_modules/blob/main/LICENSE). You may not include proprietary data or intellectual property in a  module you submit for inclusion in this project, nor may you limit your module's use to only your institution or promote commercial tools or resources that you have financial interest in.  By submitting materials for inclusion among these modules, you agree to donate your materials free of charge and agree to their use in accordance with our license.

### Transparency

We believe that greater transparency leads to better science, and we aim to not only promote transparency to our learners, but apply the same transparency demands to our own work.  We make problem reports ([GitHub "issues"](https://github.com/arcus/education_modules/issues)) and their resolutions public, and we intend to share any evidence of the effectiveness (or ineffectiveness) of our modules as soon as practicable.

### Inclusive Design

We expect authors to design with a variety of ["edge" users](https://guide.inclusivedesign.ca/activities/inclusive-design-mapping/) in mind: those with limited access to visual content or auditory content, those with barriers related to attention, cognition, sensory processing, or language, and those with limited technology access and/or financial resources.  Wherever possible we encourage a multi-modal approach to education, such that no instruction relies solely on a single type of communication (text, video, audio, images, code) but provides several ways to engage with materials.  Please review our [inclusivity guidelines](inclusivity_guidelines.md).  We encourage you to avoid the mistake of writing a module and then attempting to remediate any accessibility issues after the module is written.  It is generally much more effective for module authors and for all learners if a widely inclusive design is considered at the outset, with pedagogical decisions always keeping a variety of learners in mind.

## Use GitHub

Our files reside on GitHub and we use GitHub for git version control as well as for issue management, change management (pull requests), public communication, and more.  You will need to have a GitHub account (free) and develop some GitHub skills to be able to contribute successfully.  We hope to have some custom step-by-step instructions with screenshots added here soon, but for now, please consider reading over [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow) and [Contributing to Projects](https://docs.github.com/en/get-started/quickstart/contributing-to-projects).  

One thing to keep in mind is that you will **not** be able to mess up our files -- you can clone and fork our repository and completely obliterate your copy and this will not affect our repository.  In fact, it will be hard, if not impossible, for you to do anything that will negatively affect our repository.  We have protections in place to make it easier for novice users of GitHub to feel reassured that they aren't going to break anything.

You may wish to begin by forking our GitHub repository, so that you can have your own copy of our materials and can publish branches on your own, without working with our team directly at first.  Be aware, however, of the risk of your fork becoming out of date.  When you fork our project in order to propose a new module, you can configure Git to pull changes from our repository into the local clone of your fork.  Please read more in GitHub's [Fork a Repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo) how-to documentation.

Alternatively, you can clone our GitHub repository, which is public, and stay current with our progress.  However, without prior discussion, you will not be able to publish new branches.  If you intend to be an ongoing contributor who works with multiple modules, adding you as a contributor to our repository may be suitable.  Reach out to us at dart@chop.edu to discuss how to become a contributor to our canonical (official) repository.

Regardless of whether you are working in a clone or a fork, new module submissions belong on their own branch while they are still in progress.  Only once a module has been approved and passed all quality checks may a PR (pull request) be merged to the main branch.  Create a new branch that is descriptive, and commit your changes to that branch and publish it to the repository (either the canonical repository, if you are a collaborator, or to your fork of the canonical repository, if you are an offsite potential collaborator).  Use descriptive commit messages and leave all changes on your new branch until you are ready to ask for module approval.

When you're ready to request approval, create a Pull Request (PR) in GitHub, asking to merge your branch into main.  Include a comment describing the module.  An administrator of the repository will create a new Issue in the repository, citing your PR.  The administrator will apply the module Quality Assurance checklist (see our [QA templates](https://github.com/arcus/education_modules/tree/main/.github/ISSUE_TEMPLATE)) and may reply with requests for updates within issue comments.  Feel free to conduct a conversation through the comments on the issue, which will endure in time, while your PR will not.  Comments on the issue are a better practice for historical records.

Authoring a module is an iterative process, and we don't expect you to be approved on the first try.  It's absolutely a process of communication, editing, suggestions, tweaks, questions, and comments between the reviewer and author.  Try not to feel intimidated or that you need to be "perfect" to make a pull request (a request to bring your material into our repository main branch).  We try to be transparent so that our Quality Assurance (QA) process isn't a surprise.  You can view the [QA checklist](https://github.com/arcus/education_modules/blob/main/.github/ISSUE_TEMPLATE/qa-for-standard-modules.md) that will be used to check your module at any time. You can also see revisions and comments on [pull requests for other modules that have already been QAed](https://github.com/arcus/education_modules/pulls?q=is%3Apr+is%3Aclosed+label%3A%22Quality+Assurance%22) to see what kinds of adjustments were made.  For example, you can look at the changes and conversation that took place for our [Demystifying Machine Learning](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_machine_learning/demystifying_machine_learning.md#1) module by looking at [its pull request](https://github.com/arcus/education_modules/pulls?q=is%3Apr+is%3Aclosed+label%3A%22Quality+Assurance%22).

Once any outstanding improvements are addressed and the author and reviewer are in agreement that the module is ready to go, the reviewer checking your module will approve the PR with a squash and merge and delete your branch.  Congratulations, your module is now part of the portfolio of educational modules for the project!

## Composition

It's tempting to jump in and start creating, but a few preliminary plans about how you'd like to proceed may save you a lot of time.  Please read this entire document and view some of the existing modules to understand how module materials are organized and what topics are appropriate.  When choosing a topic and writing about it, consider whether your materials meet the specific needs of biomedical researchers and reflect the values of our project. 

### Scope

A module in this project will be brief (one hour or less) and therefore of limited, well-described scope.  Consider not only what you teach about, but what you intentionally exclude.  It may be useful to map a plan of 2, 3, or more modules that teach related skills and together provide broad coverage.  Still, keep in mind that for our project, modules are freestanding.  Modules can describe pre-requisite skills, but cannot ask learners to have acquired the necessary skills from other modules.  For example, a module covering the use of n-grams in NLP should not include a pre-requisite such as "previous completion of the module Introduction to NLTK in Python", but could include "previous experience with NLTK and the ability to ingest text data in Python", perhaps with a link to a related module for learners who would like to acquire such experience there.

### Structure

Begin your file structure by creating a folder with an expressive name, using lower case and underscores, like `lasso_and_ridge_ml_in_r` or `bayesian_stats_in_python`.  This will hold all of the files that are unique to your module.

To start writing the main file that will make up your module, use one of our [templates](https://github.com/arcus/education_modules/blob/main/_module_templates).  We have three templates:

* Our [standard template](../_module_templates/template_standard.md) is for modules that teach a skill using mostly original material.
* Our [wrapper template](../_module_templates/template_wrapper.md) is for modules that teach a skill using mostly existing material that we point learners to.  For example, a module teaching learners how to install RStudio will likely depend on Posit materials.
* Our [exercise template](../_module_templates/template_exercise.md) is for modules that do not teach additional skills but offer a practical exercise / sample project.

Make a copy of the appropriate template and save it within your new folder with an almost identical title to the folder, one that ends in `.md`, like `lasso_and_ridge_ml_in_r.md` or `bayesian_stats_in_python.md`.  

Technical instructions for how to write a module in LiaScript are available in the [DART module docs](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/docs.md#1). The docs includes some boilerplate text to show you how to write in LiaScript flavored markdown (it's pretty similar to other markdown flavors, but with a few things added in), including lots of examples you can copy and paste. It also includes information about important elements needed to meet our requirements for a module, such as including formative assessments.

Importantly, consider starting to write your module by beginning with the description and learning objectives.  This will help you scope your topic.  Three to five learning objectives are plenty for a module of about one hour's duration.

We know that this is a complex process, and you may have questions about how to use our [templates](https://github.com/arcus/education_modules/blob/main/_module_templates) or have other questions about any part of this process.  Please don't hesitate to reach out to ask questions or let us know if we haven't explained something fully.  This is how we improve!  If you send us an email at [dart@chop.edu](mailto:dart@chop.edu), we'll try to respond.  If we realize we need to improve the documentation, we may use your paraphrased email (stripped of all identifying information) to create an [issue](https://github.com/arcus/education_modules/issues) so that everyone using the repository knows we're working on a fix.  In fact, if you feel comfortable, you, too, can [create an issue](https://github.com/arcus/education_modules/issues/new/choose)!

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

## Get Credit

You've worked hard to write a module!  You can cite your module using the following format (APA style):

Lastname, F. (2023). *How to Make a Neural Net from Uncooked Macaroni.* https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/macaroni_neural_nets/macaroni_neural_nets.md#1

We encourage you to brag about your work and claim it.  Anyone using your module can see information about the author by clicking on the (i) icon (the letter 'i' enclosed in a small circle) in the upper right of the module.
# Module Development Plans

This document is a public list of the topics we intend to prioritize for new module development. 
We decide which topics to prioritize based on a combination of learner feedback and feasibility (what expertise we have available on which topics). 

## About this list

### Quarterly review meeting

Quarterly, we meet to review the list of topics here and compare it to the following:

- our current catalog of available modules
- feedback we've received on modules learners have completed 
- responses to the Needs Assessment instrument administered at the beginning of each wave 

During the meeting, we discuss as a group where we should allocate our efforts for new module development. 

This process requires the following jira tickets:

- Create and circulate a report on module feedback in advance of review meeting
- Create and circulate a report on learner needs from Needs Assessment in advance of review meeting
- Take notes during module development review meeting
- Update [topics to prioritize](#topics-to-prioritize) to reflect current priorities post review meeting, and update the [modules planned for development project board](https://github.com/orgs/arcus/projects/25) if needed

### Ongoing updates

As new modules are planned, update the [modules planned for development project board](https://github.com/orgs/arcus/projects/25). 
This list should always be a **complete** list of upcoming modules; modules not already listed there are "up for grabs" for authors to work on. 

Together, the list of topics to prioritize and the list of modules under development should provide a clear idea of the topics where we have the most need. 

## Topics to prioritize

This list was last updated 2024-01-17.
Note that all of these are high priority; the ordering here is not meaningful.

- **Applied statistics for biomedical research.** Specific modules might focus on a particular test or technique (e.g. logistic regression), a particular kind of data (e.g. longitudinal), or common statistical remedies (e.g. missing data).
_ **Machine learning.** We need lots of content here, both filling in basic concepts (how do you assess a model? What is accuracy vs specificity etc.?) and teaching specific techniques (prediction, clustering, dimension reduction, etc.). Everything needs to be tied to applications in biomedical research -- there's lots of great tutorials online already, but many use examples from e.g. advertising so our focus needs to be on providing material that's immediately relevant to our audience of learners. 
- **Data visualization for biomedical research applications.** We have overview modules on both `ggplot2` and `seaborn` for R and Python respectively, but we need more specific modules on popular visualizations. Heatmaps have been requested specifically. We should focus on applications for biomedical research specifically to avoid reinventing the wheel -- there are many, many good data viz tutorials and examples online already so we should focus closely on data viz needs that come up specifically in research applications rather than more general instructions on how to create certain kinds of plots. Specific modules might be something like "data viz for public health", "data viz clinical trials", "data viz for genomics", etc. We may also want to write a basic level "what kind of data viz should I use for these data" module, and something like "how to google effectively for data viz problems" (although check first for redundancy with content in our existing data viz modules on both of those topics).
- **Git and GitHub.** We've had strong learner interest in version control, but our modules only cover the most basic use of Git so far. In particular, we need content on collaboration (branches, conflicts, etc.). 
- **Reproducibility.** We need more actionable content / hands-on exercises for reproducibility. Ideas include a how-to module on pre-registration, and modules on best practices for writing reproducible code in R and Python. We could also use modules on library science topics like data dictionaries / code books, demystifying data sharing/reuse, etc.
- **Python.** Our learners report strong interest in Python. We need modules on machine learning in Python, specifically. [Wrapper modules](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/docs.md#which-module-template-to-use) for scipy might be a good choice. 
- **Omics.** We need lots more content here, but hands-on exercises are tricky because of the computational requirements. RNASeq would definitely be a good one to prioritize, there seems to be a lot of interest there. 

**NOTE:** Because the [Arcus Education](https://education.arcus.chop.edu/) team is in the process of reviewing/moving its website as of January 2024, our main focus will be on reworking material from the website archives rather than drafting brand new content. 

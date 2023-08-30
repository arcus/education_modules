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
- Update [topics to prioritize](#topics-to-prioritize) to reflect current priorities post review meeting, and delete any completed modules from the [modules planned for development](#modules-planned-for-development) list

### Ongoing updates

As new modules are planned, update the [modules planned for development](#modules-planned-for-development) list here. 
This list should always be a **complete** list of upcoming modules; modules not already listed here are "up for grabs" for authors to work on. 

Because listing a module as "planned for development" effectively prevents other would-be authors from working on that material, please only add a module there when you are ready to start working on it. 

Together, the list of topics to prioritize and the list of modules under development should provide a clear idea of what topics where we have the most need. 
When a new module from the "planned for development" list is completed (or, at least, under review), leave it in the list but link to the pull request. 
Only delete modules from this list if you wish to take yourself off a topic and put it back "up for grabs", or as part of the quarterly review and update.

## Topics to prioritize

This list was last updated 2023-08-22.
Note that all of these are high priority; the ordering here is not meaningful.

- **Applied statistics for biomedical research.** Specific modules might focus on a particular test or technique (e.g. logistic regresison), a particular kind of data (e.g. longitudinal), or common statistical remedies (e.g. missing data).
- **Data visualization for biomedical research applications.** We have overview modules on both `ggplot2` and `seaborn` for R and Python respectively, but we need more specific modules on popular visualizations. Heatmaps have been requested specifically. We should focus on applications for biomedical research specifically to avoid reinventing the wheel -- there are many, many good data viz tutorials and examples online already so we should focus closely on data viz needs that come up specifically in research applications rather than more general instructions on how to create certain kinds of plots. Specific modules might be something like "data viz for public health", "data viz clinical trials", "data viz for genomics", etc. We may also want to write a basic level "what kind of data viz should I use for these data" module, and something like "how to google effectively for data viz problems" (although check first for redundancy with content in our existing data viz modules on both of those topics).
- **Git and GitHub.** We've had strong learner interest in version control, but our modules only cover the most basic use of Git so far. In particular, we need content on collaboration (branches, conflicts, etc.). 
- **Reproducibility.** We need more actionable content / hands-on exercises for reproducibility. Ideas include a how-to module on pre-registration, and modules on best practices for writing reproducible code in R and Python. Other ideas might include a module on meta-analysis (with an emphasis on assessing literature for its reproducibility), or publication bias (e.g. [p-curves](https://www.bitss.org/education/mooc-parent-page/week-2-publication-bias/detecting-and-reducing-publication-bias/p-curve-a-tool-for-detecting-publication-bias/), [replications](https://journals.plos.org/plosone/browse/replication_studies), [null results](https://asm.org/Articles/2021/July/Null-Results,-Replication-Studies-and-Other-Import)). 
- **Python.** Our learners report strong interest in Python. We need modules on machine learning in Python, specifically. [Wrapper modules](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/docs.md#which-module-template-to-use) for scipy might be a good choice. We should also write a short module on Jupyter notebooks specifically since we expect learners to use them but we don't currently offer a good introduction.
- **Command Line / Bash.** Especially since we have a lot of learners interested in starting genomics analysis, we teach a lot of bash. We need more, though, including something to go before Bash 101 to ease new learners into that content better (demystifying bash?) and new content on automation and text manipulation (e.g. `find`, `awk`). 
- **Omics.** We need lots more content here, but hands-on exercises are tricky because of the computational requirements. RNASeq would definitely be a good one to prioritize, there seems to be a lot of interest there. 

## Modules planned for development

- **Applied statistics for biomedical research**
    * logistic regression (Rose Hartman)
- **Data visualization for biomedical research applications**
    * How to make Data Visualizations Accessible (Rose Franzen)
- **Reproducibility**
    * Demystifying pre-registration (Rose Hartman)
    * Pre-registration exercise module (Rose Hartman)
- **Omics**
    * RNA Seq wrapper module (Meredith Lee)
- **Command Line / Bash**
    * Demystifying the command line (Elizabeth Drellich)

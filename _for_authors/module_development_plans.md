# Module Development Plans

This document is a public list of the topics we intend to prioritize for new module development. 
We decide which topics to prioritize based on a combination of learner feedback and feasibility (what expertise we have available on which topics). 

## Topics to prioritize

Note that all of these are high priority; the ordering here is not meaningful.

- **Applied statistics for biomedical research.** Specific modules might focus on a particular test or technique (e.g. logistic regresison), a particular kind of data (e.g. longitudinal), or common statistical remedies (e.g. missing data).
- **Data visualization for biomedical research applications.** We have overview modules on both `ggplot2` and `seaborn` for R and Python respectively, but we need more specific modules on popular visualizations. Heatmaps have been requested specifically. We should focus on applications for biomedical research specifically to avoid reinventing the wheel -- there are many, many good data viz tutorials and examples online already so we should focus closely on data viz needs that come up specifically in research applications rather than more general instructions on how to create certain kinds of plots. Specific modules might be something like "data viz for public health", "data viz clinical trials", "data viz for genomics", etc. We may also want to write a basic level "what kind of data viz should I use for these data" module (although check first for redundancy with content in our existing data viz modules).
- **Git and GitHub.** We've had strong learner interest in version control, but our modules only cover the most basic use of Git so far. In particular, we need content on collaboration (branches, conflicts, etc.). 
- **Reproducibility.** We need more actionable content / hands-on exercises for reproducibility. Ideas include a how-to module on pre-registration, and modules on best practices for writing reproducible code in R and Python. Other ideas might include a module on meta-analysis (with an emphasis on assessing literature for its reproducibility), or publication bias (e.g. [p-curves](https://www.bitss.org/education/mooc-parent-page/week-2-publication-bias/detecting-and-reducing-publication-bias/p-curve-a-tool-for-detecting-publication-bias/), [replications](https://journals.plos.org/plosone/browse/replication_studies), [null results](https://asm.org/Articles/2021/July/Null-Results,-Replication-Studies-and-Other-Import)). 
- **Python.** Our learners report strong interest in Python. We need modules on machine learning in Python, specifically. [Wrapper modules](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/docs.md#which-module-template-to-use) for scipy might be a good choice. We should also write a short module on Jupyter notebooks specifically since we expect learners to use them but we don't currently offer a good introduction.
- **Command Line / Bash.** Especially since we have a lot of learners interested in starting genomics analysis, we teach a lot of bash. We need more, though, including something to go before Bash 101 to ease new learners into that content better (demystifying bash?) and new content on automation and text manipulation. 

## Modules planned for development

- **Applied statistics for biomedical research.**
    * logistic regression (Rose Hartman)
- **Git and GitHub.**
    * specific modules TBD, Joy Payton and Rose Franzen to meet to discuss and then update here.
- **Data visualization for biomedical research applications.**
    * How to make Data Visualizations Accessible (Rose Franzen)
- **Reproducibility**
    * Demystifying pre-registration (Rose Hartman)
    * Pre-registration exercise module (Rose Hartman)

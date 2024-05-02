<!--
module_id: genomics_setup
author:   Rose Hartman
email:    hartmanr1@chop.edu
version:  1.2.2
current_version_description: Updated link to the Data Carpentries instructions, which changed after an update to their website. 
module_type: wrapper
docs_version: 2.0.0
language: en
narrator: UK English Female
mode: Textbook

title: Genomics Tools and Methods: Computing Setup

comment:  This module walks you through setting up your own copy of a genomics analysis AMI (Amazon Machine Image) to run genomics analyses in the cloud. 

long_description: One challenge to getting started with genomics is that it's often not feasible to run even basic analyses on a personal computer; to work with genomics data, you need to first set up a cloud computing environment that will support it. This module walks you through how to set up the AMI (Amazon Machine Image) published by Data Carpentry as part of their Genomics Workshop. 

estimated_time_in_minutes: 30

@pre_reqs
This lesson assumes a working understanding of the bash shell.
If you aren’t familiar with the bash shell, please review our [Demystifying the Command Line Interface](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_command_line/demystifying_command_line.md#1) and [Command Line 101](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_command_line_101/bash_command_line_101.md#1) modules and/or the [Shell Genomics lesson by Data Carpentry](http://www.datacarpentry.org/shell-genomics/) before starting this lesson.

@end

@learning_objectives  
After completion of this module, learners will be able to:

- Launch and terminate instances on AWS
- Use the Data Carpentry Community AMI to set up an AMI set up for genomics analysis

@end

resource1_name: Data Carpentry AMI Setup Instructions
resource1_description: Instructions published along with the Data Carpentry Genomics Workshop to launch the AMI for genomics analysis.
resource1_wellvetted: true
resource1_wellvetted_text: Data Carpentries is a well-established organization with a great reputation and high standards for accuracy. The open source nature of the tutorial also helps ensure that any errors or problems can be caught and addressed quickly.
resource1_maintained: true
resource1_maintained_text: Data Carpentries assigns <a href="https://carpentries.org/maintainers/">lesson maintainers</a> to make sure tutorials, like this one, stay up to date.
resource1_stablesupport: true
resource1_stablesupport_text: This is hosted on the Carpentries website, and it is a popular and widely-shared tutorial. We expect it will continue to be available for the foreseeable future.
resource1_a11y_issues: No known issues with accessibility, but we may have missed something. If you encounter a problem, you can let us know in the [feedback form](#feedback) at the end of this module, or post [an issue directly on the Data Carpentry repository for these instructions](https://github.com/datacarpentry/genomics-workshop/issues). 


@module_structure
1. Read through an overview about genomics analysis, adapted from the Data Carpentry Genomics Workshop Overview.
2. Complete the AMI instructions from the Data Carpentry Genomics Workshop Setup page.
3. Return for the final sections of the module. 
@end

good_first_module: false
data_domain: omics
collection: infrastructure_and_technology
coding_required: true
coding_level: intermediate
coding_language: bash

@sets_you_up_for
- genomics_quality_control
@end

@depends_on_knowledge_available_in

- directories_and_file_paths
- demystifying_command_line
- bash_command_line_101

@end

@version_history 
Previous versions: 

- [1.1.1](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/768ecbb4a71dd338c90d78dab1ee5a6cc7b39581/genomics_setup/genomics_setup.md#1): Add explanation for why we use AWS for genomics modules.
- [1.0.0](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/e5ee3852f80245798baa280f195b806a39122849/genomics_setup/genomics_setup.md#1): Initial version.
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_wrapper.md
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_genomics.md
-->

# Genomics Tools and Methods: Computing Setup

@overview

<div class = "gratitude">
<b style="color: rgb(var(--color-highlight));">Thank you!</b><br>

We are grateful to the team of authors and maintainers at [Data Carpentry](https://datacarpentry.org/) for creating their Genomics Workshop and generously sharing it under a [CC-BY license](https://github.com/datacarpentry/genomics-workshop/blob/gh-pages/LICENSE.md): 

Erin Alison Becker, Tracy Teal, François Michonneau, Maneesha Sane, Taylor Reiter, Jason Williams, et al. (2019, June). datacarpentry/genomics-workshop: Data Carpentry: Genomics Workshop Overview, June 2019 (Version v2019.06.1). Zenodo. http://doi.org/10.5281/zenodo.3260309

</div>

@aws_explanation

## Lesson Preparation

@lesson_prep_wrapper

@print_resource1

## Getting started with genomics

Analysis of genomic sequencing data is different from many other kinds of analysis in several important ways:

- the data files are often so large that normal computing tools won't work to analyze them
- there are special issues of data quality to consider that are specific to sequencing data
- because of the unique challenges of genomics data, a number of specialized tools have been developed for each stage of the workflow, many of which have to be accessed via the command line

This module focuses specifically on how to set yourself up for genomics analysis; we won't actually start the analysis process here (there are related modules on that).

As you progress through the material in this and related lessons, keep in mind that, even if you aren’t going to be doing this exact same workflow in your research, you will be learning some very important lessons about using command-line bioinformatic tools.
What you learn here will enable you to use a variety of bioinformatic tools with confidence and greatly enhance your research efficiency and productivity.

## Using the command line

A lot of genomics analysis is done using command-line tools for three reasons:

1. you will often be working with a large number of files, and working through the command-line rather than through a graphical user interface (GUI) allows you to **automate** repetitive tasks
2. you will often need more compute power than is available on your personal computer, and connecting to and interacting with **remote** computers requires a command-line interface
3. you will often need to **customize** your analyses, and command-line tools often enable more customization than the corresponding GUI tools (if in fact a GUI tool even exists)

In this module, you will set up a computing environment you can use to run genomics analyses using the command line. 

## Setting up your computing environment in AWS

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Genomics analyses use large data files.
Even for the example data used here, which is from a relatively simple genome, many of the files will be too big to work with on a standard personal computer.
Therefore, **we strongly recommend that you perform the analyses in the cloud (AWS) rather than on your own machine**.

</div>

For these lessons, we will take advantage of the AMI instances generously built and freely shared by Data Carpentry.
You will need to create your own copy of the AMI instance using the instructions below from Data Carpentry.

The cost of using this AMI for a few days, with the t2.medium instance type is very low (about USD $1.50 per day).
Data Carpentry has no control over AWS pricing structure and provides this cost estimate with no guarantees.
Please read [AWS documentation on pricing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-getting-started.html) for up-to-date information.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

If you like, you can use a Visa prepaid debit card (instead of a credit card) for your payment method on AWS to ensure you won't go over your budget.

</div>


<div class = "external-resource">
<b style="color: rgb(var(--color-highlight));">External Content</b><br>

Now it's time to complete the AMI Setup instructions! 
Go to the [Data Carpentry AMI Setup instructions](https://datacarpentry.org/genomics-workshop/AMI-setup) and complete all the steps listed. 

When you're done, return to this page to finish the module.

</div>


## Additional Resources

AWS is one option for cloud computing, but you may prefer another platform, especially if your institution provides something they specifically support. 
Reach out to research tech support and/or information services at your institution for details.

Another popular platform is [Terra](https://terra.bio/resources/new-to-cloud/). 

## Feedback

@feedback

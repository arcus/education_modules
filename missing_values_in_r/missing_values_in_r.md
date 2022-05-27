<!--

author:   Rose Hartman
email:    hartmanr1@chop.edu
version:  0.0.1
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Missing Values in R
comment:  A practical demonstration of how missing values show up in R and how to deal with them. Note that this module does **not** cover statistical approaches for handling missing data like imputation, but instead focuses on the code you need to work with and replace missing values in R.
long_description: Beginning introduction of how missing data is handled in R, what is NA, how to work with missing data values (in a very basic sense), typical default behavior, etc. For example, `remove_na()`, `replace_na()`, `fill()`, are missing values causing your error?, `na.rm=TRUE/FALSE`, other similar v concrete applicable stuff. Not covered: Imputation, assessing the impact of missing data on your analyses (in terms of validity, stats, etc), considering possible relatedness of missing data, etc.
estimated_time: 45 min

@learning_objectives  

After completion of this module, learners will be able to:

- identify key elements
- create a product
- do a task
- articulate the rationale for something

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js
script: https://sagecell.sagemath.org/static/embedded_sagecell.js

@sage
<script input="hidden">
// Make *any* div with class 'r' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.r',
                      evalButtonText: 'Run R',
                      languages: ["r"],
                      hide: ['fullScreen', 'permalink'],
                      });
// Make *any* div with class 'r_run' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.r_run',
                      evalButtonText: 'Run R',
                      languages: ["r"],
                      hide: ['fullScreen', 'permalink'],
                      autoeval: 'true'
                      });
// Make *any* div with class 'r_data_init' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.r_data_init',
                      evalButtonText: 'Run R',
                      languages: ["r"],
                      editor: 'codemirror-readonly',
                      hide: ['fullScreen', 'permalink','output','evalButton'],
                      autoeval: 'true',
                      linked: 'true',
                      linkKey: "data"
                      });       
// Make *any* div with class 'r_data' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.r_data',
                      evalButtonText: 'Run R',
                      languages: ["r"],
                      hide: ['fullScreen', 'permalink'],
                      autoeval: 'false',
                      linked: 'true',
                      linkKey: "data"
                      });
</script>
@end
-->

# @title

<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

List any skills and knowledge needed to do this module here. When available, include links to resources, especially other modules we've made (to show learners where this falls within our catalog).

* one skill we have [another module for, linked here](https://education.arcus.chop.edu)
* some familiarity with [a topic](https://education.arcus.chop.edu)
* understanding of [one thing](https://education.arcus.chop.edu) and [another](https://education.arcus.chop.edu)

If relevant, you can include recommendations for somewhere else to start if the learner doesn't have these prereqs. For example: If you are brand new to R or python (or want a refresher) consider starting with [Intro to R](link) or [Intro to python](link) first and then coming back here.

**Learning Objectives**

@learning_objectives

For help articulating learning objectives, see [this guide to learning objectives, including lots of example verbs](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/).

</div>

## The data
@sage

And then read in the data set (note that we have to repeat our commands to load the libraries here, since this is a new cell):

<div class="r">
<lia-keep>
<script type="text/x-sage">
install.packages("readr")
library(readr)

covid_data <- read_csv("https://raw.githubusercontent.com/kendavidn/yaounde_serocovpop_shared/v1.0.0/data/yaounde_covid_seroprev_dataset.csv")
summary(covid_data)
</script>
</lia-keep>
</div>

These data are from a COVID-19 serological survey conducted in Yaounde, Cameroon (Nwosu, K., Fokam, J., Wanda, F. et al., 2021[^1](Kene David Nwosu, Joseph Fokam, Franck Wanda, Lucien Mama, Erol Orel, Nicolas Ray, Jeanine Meke, Armel Tassegning, Desire Takou, Eric Mimbe, Beat Stoll, Josselin Guillebert, Eric Comte, Olivia Keiser, & Laura Ciaffi. 2021. kendavidn/yaounde\_serocovpop\_shared: Initial release v1.0.0. Zenodo. https://doi.org/10.5281/zenodo.5218965)). The authors have made all of the code and data publicly available under a [creative commons 4.0 license](https://creativecommons.org/licenses/by/4.0/legalcode) to facilitate re-use.


<div class="learnmore">
To learn more about the study, see the [zenodo page for this dataset](https://zenodo.org/record/5218965#.YeBq2RPMITW). You can also read the published article online: [SARS-CoV-2 antibody seroprevalence and associated risk factors in an urban district in Cameroon](https://www.nature.com/articles/s41467-021-25946-0).
</div>

<div class="important">
The code from this section will be at the top of each code block in this module.

If you want to practice this code on your own computer, make sure to include the code to import the necessary modules and read in the data as the first lines, but you'll only have to do it once at the top of your script, not before each new command.
</div>

## What does "missing" look like in R?


<div class = "learnmore">
Technically, there are actually four different kinds of `NA`, one for each of the different data types in R. To learn more, read about [missing values in the free online book R for Data Science](https://r4ds.had.co.nz/vectors.html?q=missing#missing-values-4)

For most practical purposes, you don't need to know anything about these different kinds of `NA`, though; they all just mean "missing", and you can usually use `NA` to refer to all of them.
</div>

## How to check for missing values

## Reading in data with missing values

## Working around missing values

## Filtering out missing values

## Additional Resources

The last section of the module content should be a list of additional resources, both ours and outside sources, including links to other modules that build on this content or are otherwise related.

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Missing+Values+in+R%22)!

Remember to change the redcap link so that the module name is correct for this module!

<!--

author:   Rose Hartman
email:    hartmanr1@chop.edu
version:  0.0.1
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Module Title
comment:  This is a short, focused description of the module.
long_description: This is a longer description, which should be understandable for a lay audience. It will print under "Is this module right for me?" in the overview.
estimated_time: This is rough guess of how long it might take a learner to work through the module. It will print under "Estimated time to completion" in the overview

@learning_objectives  

After completion of this module, learners will be able to:

- describe data structures typical of EHR data, especially a 'normalized' database
- list three common sources of quality problems in EHR data
- explain the difference between structured and unstructured data as it applies to EHR
- identify statistical methods that are especially effective in analyzing EHR data

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# EHR Data

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

## Why use EHR for research?

Electronic health records (EHR) are a large and growing source of data for medical researchers.
There are several advantages to EHR research over other data sources:

- no need to collect data or recruit participants
- large, representative sample
- potential for detailed longitudinal analyses
- potential for multi-site studies, replications, and generalizations

## Data structures

https://education.arcus.chop.edu/getting-to-one-row/

A practical example of how combining data from multiple tables can be complicated
https://education.arcus.chop.edu/cartesian-results/

## Data quality

One source of bias in EHR is **informative presence bias** (also called "informed presence bias") --- the fact that there are systematic differences in the health information recorded as a result of the reason for the appointment.
Data collected at routine, scheduled appointments ("non-informative" visits) will be systematically different in a number of ways from data collected at appointments that occur in response to a health problem ("informative" visits).
This is compounded by the fact that the amount and type of appointments available in a patient's EHR will depend in part on their overall health.
Sicker patients are more likely to have more information recorded in their EHR than healthier patients.

The severity of informative presence bias will be different for different variables, depending on how stable each variable is over time.
For example, something like height (which is relatively stable over time) won't show much bias based on whether it's measured at a routine checkup versus when a patient seeks care because of health problems.
Something like temperature would be much more variable, though, and may be highly biased based on the type of appointment ---
people who seek care because they're feeling unwell may have higher temperatures on average than people receiving routine care at a checkup.

These systematic differences in measurements depending on the nature of the appointment can have far-reaching and sometimes subtle effects on the results of any analysis of EHR, especially longitudinal analyses where some patients may have more measurements recorded than others based on their overall health.
One way to protect against this type of bias in your analyses is to check the degree of informative presence bias in your variables of interest by checking how much measurements differ when recorded at routine versus patient-initiated appointments.

<div class="learnmore">

Learn more about informative presence bias in electronic health records, including how to measure and correct for it, by reading [this recent article](https://academic.oup.com/jamia/article/29/7/1191/6570639).

</div>

Note that some times you will see the recommendation to enter a patient's total number of visits as a proxy for their overall health in an attempt to correct for informative presence bias.
This may be effective in some situations, but there are a number of serious drawbacks to that approach as well.
See discussion of this technique [in this article](https://pubmed.ncbi.nlm.nih.gov/27852603/), as well as in the article linked in the box above.

## Text data

One common data type in EHR is text data, such as clinical notes.

When considering text data, there is an important distinction between **structured** and **unstructured** text:
Structured text data is restricted or validated in some way, such as selecting an option from a dropdown, whereas unstructured text data is filled in freely.

## Quiz: Text data

<div>
Consider the following three versions of a question on a hypothetical patient survey:

> 1. Please select your gender:
>
>  [[male|female|non-binary|prefer not to say]]
>
> 2. Please indicate your gender (select all that apply):
>
> [[male]] male
> [[female]] female
> [[nonbinary]] non-binary
> [[prefer not to say]] prefer not to say

> 3. Please write in your gender:
>
> [[___]]

Which of those questions would result in **unstructured** text data?
</div>

[( )] Only question 1
[( )] Only question 2
[(X)] Only question 3
[( )] Either question 2 or 3 could result in unstructured data, depending on how the patient responds

True or False: If we added another option to question 1 above that said "Other (please specify)" and triggered a small text box for the respondent to fill in if it was selected, all of the data for that question would then be considered unstructured.

[( )] True
[(X)] False

True or False: Techniques for the analysis of structured and unstructured text data are similar.

[( )] True
[(X)] False

## Statistical considerations

## Sources

key resource: https://www.med.upenn.edu/ehr-stats/assets/user-content/documents/COC_EHR_Traveling_Course.pdf

(worth contacting as a potential collaborator/contributor? https://www.dbei.med.upenn.edu/bio/rebecca-hubbard-phd)

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3555312/

https://pubmed.ncbi.nlm.nih.gov/23300414/

https://pubmed.ncbi.nlm.nih.gov/27668265/

https://pubmed.ncbi.nlm.nih.gov/28865143/

missing outcome data: https://pubmed.ncbi.nlm.nih.gov/30873729/

https://pubmed.ncbi.nlm.nih.gov/27852603/

https://pubmed.ncbi.nlm.nih.gov/29135770/

https://pubmed.ncbi.nlm.nih.gov/25062868/

need pennkey:
https://www.nature.com/articles/nrg3208

Recent example using ML and EHR, from DBHi: https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000073

Check out this recent talk by Dr. Ian Campbell on [Harnessing the EHR for Timely Diagnosis and Personalized Management for Children with Rare Genetic Diseases](https://www.youtube.com/watch?v=xZqQL1lCX_A). It includes examples of several EHR analyses such as machine learning, natural language processing, and other techniques. 

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

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22EHR+Data%22)!

Remember to change the redcap link so that the module name is correct for this module!

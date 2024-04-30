<!--
module_id: r_basics_practice
author:   Rose Hartman
email:    hartmanr1@chop.edu
version: 1.0.1
current_version_description: Initial version
module_type: exercise
docs_version: 3.0.0
language: en
narrator: UK English Female
mode: Textbook
title: R Basics Practice
comment: Use the basics of R coding, data transformation, and data visualization to work with real data.
long_description: The best way to learn R is by using it! This module provides an opportunity to practice basic R skills on real data. 
estimated_time_in_minutes: 60

r_file: r\_basics\_practice

@pre_reqs
This is a practice module, which means you'll be expected to use commands without them being explained first. You should be familiar with the following before starting: 

- the RStudio IDE, including how to look at data in the Data Viewer
- the following `dplyr` commands: `filter`, `select`, `mutate`
- logical tests for equality in R (`==`)
- the following `ggplot2` commands: `geom_histogram`, `geom_boxplot`, `ggtitle`, `xlab`, and `facet_wrap`

If you aren't familiar with the above, going through the first three modules in our R Basics sequence should give you the background you need: [Intro](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_introduction/r_basics_introduction.md#1), [Data Visualization](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_visualize_data/r_basics_visualize_data.md#1), and [Data Transformation](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_transform_data/r_basics_transform_data.md#1). 

Learners should also have access to R, either on their own computer or in the cloud.
@end

@learning_objectives

- Import a csv dataset into R
- Examine data in the Data Viewer
- Use `dplyr` to filter data and select columns, as well as to create new columns
- Use `ggplot2` to create data visualizations exploring the data

@end

good_first_module: false
data_task: data_visualization, data_wrangling
coding_required: true
coding_level: intermediate
coding_language: r
sequence_name: r_basics
previous_sequential_module: r_basics_transform_data

@sets_you_up_for

@end

@depends_on_knowledge_available_in
-r_basics_introduction
-r_basics_visualize_data
-r_basics_transform_data
@end

@version_history
No previous versions.
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_r.md
-->

# R Basics Practice

@overview

## Topics to Review

- Using RStudio: How to add code chunks, how to use the Data Viewer, running code
- Loading libraries
- Reading a CSV and creating a data frame
- Using `dplyr` pipelines to modify a data frame
- Exploratory data visualization with `ggplot2`
- Logical statements in R, like tests for equality using `==`

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

If you've been working through our R Basics sequence, then this might be your first time analyzing **real data** in R. 
Real data are generally a lot harder to work with than the sanitized fake datasets we use in teaching examples!

If you find yourself feeling overwhelmed or frustrated, take a step back. 
Sometimes ten minutes away from the keyboard is all you need to come at a problem with a fresh mindset.
You can also try going back to review earlier examples in previous modules you've completed to refresh yourself on how those commands work in a more scaffolded context.

And remember that [learning to ask for help with code](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/learning_to_learn/learning_to_learn.md#8) is also a important skill, and one you should be practicing! 
If you get stuck, ask for help!

</div>

## The Data

These data are from a COVID-19 serological survey conducted in Yaounde, Cameroon (Nwosu, K., Fokam, J., Wanda, F. et al., 2021[^1](Kene David Nwosu, Joseph Fokam, Franck Wanda, Lucien Mama, Erol Orel, Nicolas Ray, Jeanine Meke, Armel Tassegning, Desire Takou, Eric Mimbe, Beat Stoll, Josselin Guillebert, Eric Comte, Olivia Keiser, & Laura Ciaffi. 2021. kendavidn/yaounde\_serocovpop\_shared: Initial release v1.0.0. Zenodo. https://doi.org/10.5281/zenodo.5218965)). The authors have made all of the code and data publicly available under a [creative commons 4.0 license](https://creativecommons.org/licenses/by/4.0/legalcode) to facilitate re-use.


<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To learn more about the study, see the [zenodo page for this dataset](https://zenodo.org/record/5218965#.YeBq2RPMITW). You can also read the published article online: [SARS-CoV-2 antibody seroprevalence and associated risk factors in an urban district in Cameroon](https://www.nature.com/articles/s41467-021-25946-0).

</div>

## Lesson Preparation

@lesson_prep_r

## Practice Problem

Time to jump in! 
Open the `basics_practice_exercises.Rmd` file in RStudio. 

This file includes a list of instructions and questions for you to answer.
You'll need to add code chunks to the .Rmd file, and write R code to complete the tasks. 
Good luck, and have fun!

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

If you're having trouble, remember that the skills you'll need in this practice module are (almost!) all covered in previous modules in the R Basics sequence. 

You can go back to review those modules, or even just look over the exercise and solution files for them, which are also available in the same `education_r_environment` directory you're already working in. 
In particular, the files for `r_basics_introduction`, `r_basics_visualize_data`, and `r_basics_transform_data` will be helpful.

</div>

### Stuck?

If this practice problem was challenging, open up the `r_basics_practice_solutions.Rmd` file in the directory you're already working in (if you'd like a direct link, here is [the solutions file online](https://github.com/arcus/education_r_environment/blob/main/r_basics_practice/basics_practice_solutions.Rmd)). 
In that solutions file, we go through example code for the practice problems.

We encourage you to spend some time playing around with the data before you look at the solutions file! 
And remember, just because your solution doesn't look exactly like the example doesn't mean it's wrong-- there are a variety of ways you might have approached the tasks we gave you.  

## Additional Resources

A great way to keep resources close at hand is to use cheat sheets:

- [Posit.co](https://posit.co/about/) has many cheat sheets available to download, including one for [data transformation with dplyr](https://posit.co/wp-content/uploads/2022/10/data-transformation-1.pdf), [data visualization with ggplot2](https://posit.co/wp-content/uploads/2022/10/data-visualization-1.pdf).

And as always, [R for Data Science](https://r4ds.had.co.nz/) is a great resource!

## Feedback

@feedback

<!--
module_id: r_logistic_regression
author:   Rose Hartman
email:    hartmanr1@chop.edu
version:  1.0.0
current_version_description: Initial version
module_type: standard
docs_version: 4.0.0
language: en
narrator: UK English Female
mode: Textbook

title: Logistic Regression in R

comment:  

long_description: 

estimated_time_in_minutes: 60

r_file: r\_logistic\_regression

@pre_reqs
Learners should already be familiar with the following concepts in statistics and math:

- [linear regression](https://education.arcus.chop.edu/ordinary_linear_regression/) (also called "ordinary least squares (OLS) linear regression"), including how to interpret tests of model coefficients
- [null hypothesis significance testing (NHST)](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/intro_to_nhst/intro_to_nhst.md#1), also called "frequentist statistics" (this is the most commonly taught branch of statistics and includes techniques that use $p$ values to interpret results, like t-tests)

This module also assumes some basic familiarity with R, including the following:

- [installing and loading packages](https://r4ds.had.co.nz/data-visualisation.html#prerequisites-1)
- manipulating data frames, including [selecting columns and calculating new columns](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_transform_data/r_basics_transform_data.md)
- the difference between [numeric (continuous) and factor (categorical) variables](https://swcarpentry.github.io/r-novice-inflammation/13-supp-data-structures) in a dataframe

If you are brand new to R (or want a refresher) consider starting with [Intro to R](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_introduction/r_basics_introduction.md) first.

@end

@learning_objectives  
After completion of this module, learners will be able to:

- use the `glm` function in R to run a logistic regression model
- interpret significance tests for individual predictors or sets of predictors in a logistic regression model
- create a classification table (also called a confusion matrix) to assess model performance 
@end

good_first_module: false
data_task: data_analysis
collection: statistics
coding_required: true
coding_level: intermediate
coding_language: r

@sets_you_up_for

@end

@depends_on_knowledge_available_in
- intro_to_nhst
- generalized_linear_regression
- r_basics_transform_data
@end

@version_history 
No previous versions.
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
-->

# Logistic Regression in R

@overview

## 

### The data

https://www.nejm.org/doi/full/10.1056/NEJMoa1111103

From the help documentation:

> ERCP, or endoscopic retrograde cholangio-pancreatogram, is a procedure performed by threading an endoscope through the mouth to the opening in the duodenum where bile and pancreatic digestive juices are released into the intestine. ERCP is helpful for treating blockages of flow of bile (gallstones, cancer), or diagnosing cancers of the pancreas, but has a high rate of complications (15-25%).
> The occurrence of post-ERCP pancreatitis is a common and feared complication, as pancreatitis can result in multisystem organ failure and death, and can occur in ~ 16% of ERCP procedures.
> The inflammatory cytokine storm that can result from this procedural complication can be quite severe. Several small randomized trials suggested that anti-inflammatory NSAID therapies at the time of ERCP could reduce the rate of this complication, but all were rather small single-center studies, and were not sufficiently convincing to change practice.


alternate data: 


article: https://peerj.com/articles/175/

available on GH: https://github.com/hpiwowar/citation11k/tree/master/analysis/data

Learn more about how open science practices impact researchers' careers: https://elifesciences.org/articles/16800#bib105

### Writing the formula

### Link functions

### Summarize the results

Note that R prints the results such that the first level of the outcome variable is a failure, so these results articulate the probability of the second level of statement.included happening. 
To see the order of the levels in the data frame, use levels()

```r
model.sum <- summary(logit.model1)
pander(model.sum)
```

\seealso{the stargazer package, which makes lovely model tables and works for knitting to pdf but not Word}
\seealso{knitr has a function for making tables, kable(), but it doesn't work for model summaries}

### Testing a series of models

It's typical to test a series of glms, beginning with a null model (no predictors).

```r
logit.model0 <- glm(statement.included ~ 1, data=osf.lgt,
                    family=binomial(link="logit"),
                    na.action=na.exclude)
```

Use anova() to test for a significant improvement in model fit from the null model to our test model:

```r
anova(logit.model0, logit.model1, test="Chisq") 
```

Since we want to test for a significant change in model fit (deviance), we'll used a chi-squared test.

### Classification tables

For logistic regression, it's nice to have a classification table showing your model's predicted outcomes compared to the actual outcome.

```r
osf.lgt$pred1 <- predict(logit.model1, 
                                osf.lgt, 
                                type="response") 

osf.lgt$pred0 <- predict(logit.model0, 
                                 osf.lgt, 
                                 type="response") 
```

Note that if you leave out the `type="response"` argument, or enter `type="link"` instead, it will give you predicted logits instead of predicted probabilities.


Set a probability cutoff (let's use .5). Probabilities above this will be classified as "yes", and below will be classified as "no".

```r
osf.lgt$clas0 <- ifelse(osf.lgt$pred0 >= .5, 1,
                                ifelse(osf.lgt$pred0 < .5, 0, 
                                       NA))
osf.lgt$clas1 <- ifelse(osf.lgt$pred1 >= .5, 1,
                                ifelse(osf.lgt$pred1 < .5, 0, 
                                       NA))
```

Convert the new classification variables to factors, for cleaner output in the crosstabs.

```r
osf.lgt$clas0 <- factor(osf.lgt$clas0,
                                levels=c(1,0),
                                labels=c("yes", "no"))
osf.lgt$clas1 <- factor(osf.lgt$clas1,
                                levels=c(1,0),
                                labels=c("yes", "no"))
```

```r
xtabs(~ statement.included + clas0, data=osf.lgt)

xtabs(~ statement.included + clas1, data=osf.lgt)
```

\seealso{gmodels::CrossTable(), which makes fancier crosstabs}

### Plotting your logistic regression

The relationship between publication date and whether there was a data statement available

```r
ggplot(osf.lgt, aes(x=date, y=statement.included)) + 
  geom_point(alpha=.3)
```

Note that R counts factor levels starting at 1, so "no" and "yes" are plotted at 1 and 2 respectively. To line them up with the predicted values from the model, we need to subtract 1.


```r
ggplot(osf.lgt, aes(x=date, y=as.numeric(statement.included)-1)) + 
  geom_point( alpha=.3 ) + 
  geom_line( aes(y=pred, x=date) ) +
  labs(y="Probability of providing a data statement")
```

learnmore ggplot2

- Read Jenny Bryan's ggplot tutorials --- tons of great examples and code! Click on the files that have the file extension .md (those will be the easiest to read) \\ \url{https://github.com/jennybc/ggplot2-tutorial}
- All of the geoms, with pictures \\ \url{http://docs.ggplot2.org/current/}
- For more in-depth material on ggplot2, see the resources at \\ \url{http://ggplot2.org/}

### Adding more predictors

What question would this model test?

```r
logit.model2 <- glm(statement.included ~ date*Journal, data=osf.lgt,
                   family=binomial(link="logit"),
                   na.action=na.exclude)
```

Test against simpler models

```r
anova(logit.model0, logit.model1, logit.model2, test="Chisq") 
```

Getting predicted values

```r
osf.lgt$pred2 <- predict(logit.model2, 
                                osf.lgt, 
                                type="response") 
osf.lgt$clas2 <- ifelse(osf.lgt$pred2 >= .5, 1,
                                ifelse(osf.lgt$pred2 < .5, 0, 
                                       NA))
osf.lgt$clas2 <- factor(osf.lgt$clas2,
                                levels=c(1,0),
                                labels=c("yes", "no"))

xtabs(~ statement.included + clas2, data=osf.lgt)
```

```r
ggplot(osf.lgt, aes(x=date, y=as.numeric(statement.included)-1, 
                    color=Journal)) + 
  geom_point( alpha=.3 ) + 
  geom_line( aes(y=pred2, x=date) ) +
  labs(y="Probability of providing a data statement")
```
## Other kinds of GLMs

Let's say you wanted to see if the number of experiments reported in each article varies by journal. 

```r
summary(osf$Number.of.experiments)

hist(osf$Number.of.experiments)
```

There are a couple reasonable options for a link function here. Let's go with Poisson.

```r
osf.pois <- osf %>% 
  select(Number.of.experiments, Journal) %>% 
  filter(Journal != "Infant behavior & development") %>% 
  na.omit()
```

\hwydt{Write the glm call to model number of experiments by journal, using a Poisson link.}

```r
pois.model <- glm(Number.of.experiments ~ Journal, data=osf.pois,
                   family=poisson(link = "log"),
                   na.action=na.exclude)  
```

```r
ggplot(osf.pois, aes(x=Number.of.experiments)) + 
  geom_histogram() 
```

Show Journal info as well

```r
ggplot(osf.pois, aes(x=Number.of.experiments, fill=Journal)) + 
  geom_histogram()

ggplot(osf.pois, aes(x=Number.of.experiments, fill=Journal)) + 
  geom_density(alpha=.3, adjust=2) 
```

Try adding facet wrap by Journal as well, to put each density plot in its own facet.

## Additional Resources

There's an excellent [chapter on Logistic Regression](https://online.stat.psu.edu/stat504/lesson/6) published by Penn State.

If you'd like to compare output from different kinds of statistical software, [UCLA's IDRE](https://stats.oarc.ucla.edu/other/dae/) has published data analysis examples for logistic regression in a variety of softwares: 
* [Logistic Regression in R](https://stats.oarc.ucla.edu/r/dae/logit-regression/) 
* [Logistic Regression in Stata](https://stats.oarc.ucla.edu/stata/dae/logistic-regression/) 
* [Logistic Regression in SPSS](https://stats.oarc.ucla.edu/spss/dae/logit-regression/)
* [Logistic Regression in SAS](https://stats.oarc.ucla.edu/sas/dae/logit-regression/)
* [Logistic Regression in MPlus](https://stats.oarc.ucla.edu/mplus/dae/logit-regression/). 

## Feedback

@feedback
<!--

author:   Your Name
email:    email@chop.edu
version:  0.0.0
current_version_description: Brief description of why this version exists
module_type: standard
docs_version: 1.1.0
language: en
narrator: UK English Female
mode: Textbook

title: Module Title

comment:  This is a short, focused description of the module.

long_description: This is a longer description, which should be understandable for a lay audience.

estimated_time_in_minutes: 

@pre_reqs
List any skills or knowledge needed to complete this module here.
@end

@learning_objectives  
After completion of this module, learners will be able to:

- identify key elements
- create a product
- do a task
- articulate the rationale for something
@end

@version_history 

Previous versions: 

- [x.x.x](link): that version's current version description
- [x.x.x](link): that version's current version description
- [x.x.x](link): that version's current version description
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
-->

# Module Title

@overview

## Why do we need generalized linear models?

Linear models are only appropriate when your outcome variable(s) are **continuous** and **unbounded**. 
If you want to model a categorical outcome, or one that's bounded (like a proportion or percent), then usually can't rely on regular linear modeling to get the job done. 

<h3>What counts and continuous and unbounded?</h3>

A variable is **continuous** if it can take any value on a scale, not just discrete options. For example, age is generally continuous because you can be 11 years old, or 11.5, or 11.476 years old, etc.
In contrast, experimental group (treatment vs. control) is not continuous; there's no way to be halfway between treatment and control, you're in one or the other. 
Something like medication dose could be continuous or categorical depending on how it's used. 
If patients are restricted to categorical levels of dose (e.g. high, med, or low dose groups) then it would be categorical. But if it's something where their dose might theoretically be anywhere on the scale, then it's continuous.

A variable is **unbounded** if it can theoretically extend from negative infinity at the low end to positive infinity at the high end. 
We often have variables that aren't truly unbounded, but they're close enough for all practical purposes -- for example, IQ can't technically be negative, but in practice no measured IQs are close to 0 so the data stop naturally before they hit a the scale boundary at 0. 
IQ is generally treated as unbounded statistically.

Something like a probability or proportion is bounded at 0 and 1; it's not possible to have a negative probability, or one over 1. 

A variable like age might be unbounded or bounded depending on what ages you're studying. 
In a young pediatric population, age is bounded at 0 because you can't have any negative ages and a distribution of infant ages will get cutoff at that lower bound. 
But if you're studying adults, then age might be functionally unbounded in your dataset.

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

For an excellent review of continuous vs. categorical variables, see the [Khan Academy video on discrete and continuous random variables](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/random-variables-discrete/v/discrete-and-continuous-random-variables).

</div>

We can coerce problematic outcome variables into nice, continuous ones so that we can still model them with a line.
The strategy for transforming your outcome depends on what its distribution is like to begin with --- if it's binary (or bounded at 0 and 1), then a logit works well. 
If it's count data, then a log is the right transformation, etc.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Generalized linear models are just linear models on data that's been transformed with a link function.

</div>

## Special considerations for generalized linear models

- Unlike linear models, there is not a single analytic solution to glms
- The computer uses brute force to find a solution, iterating over tons of combinations of parameter estimates and seeing which gives the best model fit
- This means the results are not exact --- they depend on the sampling algorithm being used --- so you might see very small changes if you run the model again, or if you run it on other software
- There's a risk that your model won't converge if it's too complicated and you don't have enough data

## Example: Logistic regression

One of the most common kinds of generalized linear model is logistic regression. 
That's a linear model using a [logit](https://en.wikipedia.org/wiki/Logit) transformation to convert the outcome that's binary (or continuous but bounded at 0 to 1, like a proportion).

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

It's not necessary to really understand the logit transformation to be able to use logistic regression, so feel free to skip this bit if you don't find it helpful. 
But if you'd like to get a better idea of how the math works, here goes!

Data bounded at 0 and 1, like probabilities or binary outcomes, can be converted to unbounded data as follows:

1. Probabilities can be converted to odds by dividing the probability by 1-(the probability). So a probability of .5 becomes $0.5/(1-0.5) = 1$.
2. Odds are unbounded at the upper end (they can theoretically go to positive infinity), but they're still bounded at the lower end, at 0. We can fix that by taking the natural log of the odds. The natural log of the odds is called a logit. For a probability of .5, the logit would be $Ln(0.5/1-0.5) = 0$.

To build your intution of probability, odds, and log-odds, it may be helpful to consider what counts as "likely" or "unlikely" for each. 
If an event is unlikely to happen, it would have a probability less than .5. 
That corresponds to an odds of less than 1, and a log-odds of less than 0. 
If an event is likely to happen, then the probability would be greater than .5, the odds would be greater than 1, and the log-odds would be greater than 0. 

</div>

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

Note that if you leave out the type="response" argument, or enter type="link" instead, it will give you predicted logits instead of predicted probabilities.


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

## Quiz

True or False: Generalized linear models actually still use a line for the model (like ordinary linear regression), they just transform the outcome variable first.

[(X)] TRUE
[( )] FALSE
***
<div class = "answer">

True! 
We can only use ordinary linear regression when the outcome variable is continuous and unbounded, so if you have, for example, a binary outcome, then a regression model won't work unless you first transform the outcome to be continuous and unbounded -- that's what generalized linear models do! 

</div>
***

True or False: The logit transformation is an appropriate way to convert a variable that is binary or bounded at 0 and 1 (like a probability or proportion) to a continuous variable that isn't bounded.

[(X)] TRUE
[( )] FALSE
***
<div class = "answer">

True! 
We can only use linear regression when the outcome variable is continuous and unbounded, so if you have, for example, a binary outcome, then a regression model won't work unless you first transform the outcome to be continuous and unbounded -- that's what generalized linear models do! 

</div>
***

The transformation that will work (also called a "link" function) depends on the shape of the outcome variable to start with. 
For binary outcomes, a logit transformation works well. 
A generalized linear model with a logit link function is often called "logistic regression" for short.

## Additional Resources

There's an excellent chapter on [Logistic Regression](https://online.stat.psu.edu/stat504/lesson/6) published by Penn State.

If you'd like to compare output from different kinds of statistical software, [UCLA's IDRE](https://stats.oarc.ucla.edu/other/dae/) has published data analysis examples for logistic regression in [R](https://stats.oarc.ucla.edu/r/dae/logit-regression/), [Stata](https://stats.oarc.ucla.edu/stata/dae/logistic-regression/), [SPSS](https://stats.oarc.ucla.edu/spss/dae/logit-regression/), [SAS](https://stats.oarc.ucla.edu/sas/dae/logit-regression/), and [MPlus](https://stats.oarc.ucla.edu/mplus/dae/logit-regression/). 

## Feedback

@feedback

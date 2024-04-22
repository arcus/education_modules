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
Learners should already be familiar with the following concepts in statistics and math (but not necessarily how to do them in R):

- [linear regression](https://education.arcus.chop.edu/ordinary_linear_regression/) (also called "ordinary least squares (OLS) linear regression"), including how to interpret tests of model coefficients
- [null hypothesis significance testing (NHST)](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/intro_to_nhst/intro_to_nhst.md#1), also called "frequentist statistics" (this is the most commonly taught branch of statistics and includes techniques that use $p$ values to interpret results, like t-tests)
- [generalized linear models and link functions](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/generalized_linear_regression/generalized_linear_regression.m)

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

## Lesson Preparation

@lesson_prep_r

## When to use Logistic Regression

Logistic regression is an extension of linear regression. 
It's an example of what's known as a [generalized linear model](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/generalized_linear_regression/generalized_linear_regression.md#1).
Regular linear regression only works when your outcome variable (the variable you want to predict) is [continuous and unbounded](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/generalized_linear_regression/generalized_linear_regression.md#when-ordinary-linear-models-fail); if you want to run a model predicting a variable that is **not** continuous an unbounded, then you need a generalized linear model instead, and the specific kind of model depends on the type of outcome variable you want to predict.

**Logistic regression is used to model [binary](https://en.wiktionary.org/wiki/binary) (BI-na-ree) outcomes -- in other words, outcomes with two possible values.**

Binary outcomes are extremely common in medical and health data!
Any time you want to predict whether something happened or not (a particular diagnosis, hospitalization, complications after surgery, etc.), that is likely a binary outcome and logistic regression is probably the tool you need to analyze your data.

Here are some examples of binary outcomes in biomedicine:

- []()

## Overview of Models in R

Linear models (including generalized linear models like logistic regression) express the relationship between the predictor(s) and the outcome using the equation for a line, for example: 

$$
Y = \beta_0 + \beta_1 * X_1 + \beta_2 * X_2 + e 
$$

In this equation, $Y$ is the outcome variable, and $X_1$ and $X_2$ are the predictors.  

R is built for statistics, and regression models is one area where it really shines!
There's a consistent way to express equations like the above in R across many different modeling functions: a model formula. 

A model formula for the equation above would look like this: `Y ~ X1 + X2`

A few things to note about how to write a model formula in R: 

- The `~` separates the outcome side of the equation (on the left) from the predictor side (on the right)
- Use `+` between each predictor (if you want to include interactions or polynomial terms, things get a little more complicated, but we'll skip that for now)
- You don't need to explicitly include the intercept in your model, R assumes you want one by default

To run an ordinary least squares linear regression model, use the function `lm` (short for "linear model"). 
In our example, the code would look like this (assuming the variables `Y`, `X1` and `X2` are all columns in a dataframe called `my_data`):

```
lm(Y ~ X1 + X2, data = my_data)
```

**What if `Y` is a binary variable, and I need to run a logistic regression instead of a regular linear model?**

To run a logistic regression in R, the code looks very similar! 
Here's how we would adapt the code above if `Y` were binary:

```
glm(Y ~ X1 + X2, family = binomial(link="logit"), data = my_data)
```

What's changed?

- We're using the function `glm` (short for "generalized linear model") instead of `lm`.
- We added the argument `family = binomial(link="logit")`. This tells R what kind of GLM we want to run (what [link function](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/generalized_linear_regression/generalized_linear_regression.md#link-functions) to use). In this case, we want to use a [logit](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/generalized_linear_regression/generalized_linear_regression.md#logit-link-function) (LOW-jit) link function, which is what defines logistic regression. 
- That's it! Everything else about our code, including the model formula, is just like what we would use for a regular linear regression model.

## Logistic Regression Example

Let's try a real data analysis example!

Start by loading these helpful R packages:

```r
library(medicaldata) 
library(tidyverse)
library(pander)
```

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

If you're working on your own computer, you may need to install these packages first if you've never used them before. 
Try running `install.packages(c("medicaldata", "tidyverse", "pander"))`, then run the library commands again. 

The `pander` package is sometimes a little tricky to install, depending on your computer's setup, because it requires another program called [pandoc](https://rapporter.github.io/pander/#pandoc) (not an R package, a separate program) for some of its functionality.
If you have [RStudio](https://posit.co/products/open-source/rstudio/) installed, then pandoc will already be set up. 
If not, and if you're having trouble with the `pander` installation, just skip it -- there are [other ways to print nice tables in R](https://bookdown.org/yihui/rmarkdown/r-code.html#tables). 

</div>

We'll work with the `indo_rct` data, which comes in the `medicaldata` R package. 

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

There are lots of great datasets available in the `medicaldata` package! 
To learn more, checkout the [`medicaldata` website](https://higgi13425.github.io/medicaldata/). 

Also, if you have medical data that can be anonymized and shared publicly, [please consider donating it](https://higgi13425.github.io/medicaldata/#please-donate-datasets)!
It's a [great way to increase the visibility of any projects you have related to those data](https://elifesciences.org/articles/16800), and you can also take pride in contributing to a growing culture of data sharing and reuse. 

</div>

We'll also need to load two other packages for our analysis today: `tidyverse` and `pander`. 
The [`tidyverse`](https://www.tidyverse.org/) is actually a whole set of related packages for doing data science in R. 
We'll mostly use its data cleaning and transformation functions today, such as [`select` and `mutate`](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_transform_data/r_basics_transform_data.md). 

We'll use [`pander` package](https://rapporter.github.io/pander/) to convert R objects, especially our model output, into nicely formatted tables we can use in Word, HTML, PDF, etc. 

### The Data

We'll be analyzing the `ind_rct` data from the `medicaldata` package, data from a randomized control trial on the effectiveness of indomethacin in the prevention of post-ERCP pancreatitis ([Elmunzer, Higgins, et al., 2012](https://www.nejm.org/doi/full/10.1056/NEJMoa1111103)).
From the `indo_rct` help documentation (you can pull this up by running `?indo_rct` in the console):

> ERCP, or endoscopic retrograde cholangio-pancreatogram, is a procedure performed by threading an endoscope through the mouth to the opening in the duodenum where bile and pancreatic digestive juices are released into the intestine. ERCP is helpful for treating blockages of flow of bile (gallstones, cancer), or diagnosing cancers of the pancreas, but has a high rate of complications (15-25%).
> The occurrence of post-ERCP pancreatitis is a common and feared complication, as pancreatitis can result in multisystem organ failure and death, and can occur in ~ 16% of ERCP procedures.
> The inflammatory cytokine storm that can result from this procedural complication can be quite severe. Several small randomized trials suggested that anti-inflammatory NSAID therapies at the time of ERCP could reduce the rate of this complication, but all were rather small single-center studies, and were not sufficiently convincing to change practice.

For our model, we'll be using the data from this randomized control trial (RTC) to predict whether or not patients got post-ERCP pancreatitis (yes or no, a binary variable) from their underlying risk score (a score from 1-5.5) and whether they received the treatment (indomethacin) or a placebo. 

The results of the original trial were published in [Elmunzer, Higgins, et al. in 2012 in the New England Journal of Medicine](https://www.nejm.org/doi/full/10.1056/NEJMoa1111103). 


### Data Preparation

There are a few important data preparation steps before running a logistic regression. 

#### Check the structure of your data, especially your binary outcome variable

This dataset contains quite a few variables we won't actually need for our analysis, so let's save a version of the dataset that just includes the variables we want, to simplify output.

```r
indo_rct <- select(indo_rct, risk, rx, outcome)
```

Now we can use the `str()` command to get an overview of the variables in this dataframe, and whether each is continuous (numeric) or categorical (factor). 

```r
str(indo_rct)
```

```+output
tibble [602 × 3] (S3: tbl_df/tbl/data.frame)
 $ risk   : num [1:602] 2 1 1 2 3.5 3 1.5 1 2 2 ...
  ..- attr(*, "label")= chr "risk score"
  ..- attr(*, "format.stata")= chr "%8.0g"
 $ rx     : Factor w/ 2 levels "0_placebo","1_indomethacin": 2 1 1 1 2 1 2 2 2 2 ...
 $ outcome: Factor w/ 2 levels "0_no","1_yes": 2 1 1 2 1 1 1 1 1 1 ...
```

We can see that `outcome` is indeed a binary variable: It's a factor with two levels, "0_no" and "1_yes", indicating that the patient didn't or did have post-ERCP pancreatitis, respectively.
We can also see that `risk` is numeric, and `rx` is another factor, with two levels ("0_placebo" and "1_indomethacin") indicating whether the patient was assigned to receive the placebo or treatment.

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

It's very important to double check that R is using the correct variable types (numeric or factor) for each variable you'll include in your model.
If you have a categorical variable in your data that R mistakenly listed as numeric or vice versa, that can completely change your model results and ruin your analysis.

Categorical variables should always be encoded as factors, and continuous variables should always be encoded as numeric.

</div>

It's also a good idea to look at some basic summary statistics, and especially keep an eye out for any [missing values](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_missing_values/r_missing_values.md#1). 
We can do that with the `summary()` function:

```r
summary(indo_rct)
```

```+output
      risk                    rx       outcome   
 Min.   :1.000   0_placebo     :307   0_no :523  
 1st Qu.:1.500   1_indomethacin:295   1_yes: 79  
 Median :2.500                                   
 Mean   :2.381                                   
 3rd Qu.:3.000                                   
 Max.   :5.500                
```

There aren't any missing data on the variables we'll be looking at today. Yay!

#### Center any continuous predictors

Centering a continuous variable means subtracting the column mean from every observation.
For example, if you had the following observations `2,1,2,4` (the mean of these numbers is 2.25), centering it would make it into `-0.25,-1.25,-0.25,1.75`.

We have one continuous predictor in our model: `risk`. 
Let's center it now:

```r
indo_rct <- mutate(indo_rct, 
                   risk = risk - mean(risk, na.rm = TRUE))
```

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

Want a review of the `mutate()` function? 
Check out [R Basics: Transforming Data with dplyr](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_transform_data/r_basics_transform_data.md).

</div>

**Why is centering important?** 
Centering continuous predictors can make your coefficients a little easier to interpret, which is handy, but the real reason it's important is because if you end up including interaction terms in your model failing to center continuous predictors can introduce multicolinearity (if you've never heard of multicolinearity before, no worries! Just know that we'd like to avoid it, and centering predictors is an easy preventative measure to take).

If you know you won't have any interaction terms in your model, then you can decide to center continuous predictors or not, based on your preference. 
But it does no harm to center continuous predictors "unnecessarily," so we recommend it as a general practice, especially for folks new to modeling.

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To learn more about when centering predictors is (and isn't) useful, see  
["When not to center a predictor" on the Analysis Factor blog](https://www.theanalysisfactor.com/when-not-to-center-a-predictor-variable-in-regression/).

</div>

### Running the model


To run a logistic regression (or any generalized linear model) in R, we'll use the `glm()` (short for "generalized linear model") function. 
In the arguments for `glm()`, we need to specify the model formula, provide the dataframe, and give the link function that should be used. 
For our first model, predicting whether or not patients had post-ERCP pancreatitis (`outcome`) from their underlying risk score (`risk`), the command to run the model would look like this: 

```{r}
model_risk <- glm(outcome ~ risk, 
                  data = indo_rct,
                  family = binomial(link="logit"),
                  na.action = na.exclude)
```

Let's break that down. 

#### Model formula and data

The first argument in the `glm` function is the model formula.

Recall from the [overview of models in R](#overview-of-models-in-r) that many statistical functions in R start with a formula, with the variable(s) you want to predict (the outcome) on the left side of the `~`, and the predictors on the right side.
We want to predict whether or not patients had post-ERCP pancreatitis (`outcome`) from their underlying risk score (`risk`), so the formula looks like this: `outcome ~ risk`

The second argument in `glm` is the dataframe to use. 
Each of the variables in the forumla needs to be a column name in the dataframe you provide. 
In this case, our dataframe is `indo_rct`.

#### The link function

The next argument for `glm` is the link function, specified by the `family` argument.

A link function is the main thing that makes generalized linear models (like logistic regression) different from ordinary linear models.
When your outcome variable is binary, as ours is here, a regular linear model doesn't make sense. 
In order to run a regression model with a binary outcome, you need a function to transform the binary outcome into a continuous, unbounded variable -- that transformation is the link function. 
There are many different kinds of link functions available, and the particular link function you need for a given model depends on the shape of your outcome variable. 

For a binary variable (like `outcome`), the most typical link function is a [logit](https://en.wikipedia.org/wiki/Logit) (LOW-jit) transformation -- the term "logistic regression" means regression done with a logit link transformation. 

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

From a practical standpoint, it's not important for you to have a clear understanding of what a logit is or why it works as a link function for binary data. 
If you're content to just make note of the fact that logistic regression works for binary outcomes and move on, great!

If you're curious to learn more about why this works, though, check out [our explanation of the logit transformation](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/generalized_linear_regression/generalized_linear_regression.md#logit-link-function).

</div>

In R, you specify a logit link function with the argument `family = binomial(link="logit")`.

#### Tell R how to handle missing data

In this particular example, we actually don't have any missing data for the variables we're analyzing. 
But that's unusual!
It's good to be in the habit of specifically stating what action you want R to take with missing values when you run a model. 

In general, `na.action = na.exclude` is a reasonable choice -- this will have R drop any cases (rows) in the dataframe you provide it that have missing data on any of the variables included in the model formula.

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To learn more about options for `na.action`, including examples with R code, check out our module on [Missing Values in R](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_missing_values/r_missing_values.md#1).

</div>

Note that `na.action = na.exclude` will **not** drop cases that are missing on variables not in your model -- that means that, if you use different sets of predictors in different models, you can end up testing a slightly different dataset for each model. 
To avoid that, you can [save a version of your data that filters out cases with missing values on all of the variables you use across all your models](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_missing_values/r_missing_values.md#filtering-out-missing-values).

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
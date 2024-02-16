<!--

module_id: generalized_linear_regression
author:   Rose Hartman
email:    hartmanr1@chop.edu
version:  0.0.0
current_version_description: Initial version
module_type: standard
docs_version: 4.0.0
language: en
narrator: UK English Female
mode: Textbook

title: Generalized Linear Regression

comment:  What is generalized linear regression (including logistic regression) and when might you need it? 

long_description: This lesson walks you through what generalized linear models are, and how they are similar to and different from ordinary linear regression. It uses logistic regression as a specific example, but touches on other generalized linear models as well. This is a theoretical overview, not hands-on coding practice, so no experience with any particular software is expected. If you want to understand generalized linear models better, regardless of what statistical software you use, this is for you!

estimated_time_in_minutes: 60

@pre_reqs
Learners should already be familiar with the following concepts in statistics and math:

- linear regression (also called "ordinary least squares (OLS) linear regression")
- the equation of a line (intercept and slope)
@end

@learning_objectives  
After completion of this module, learners will be able to:

- describe how generalized linear models are similar to and different from linear models
- define a "link function"
- identify when a logistic regression model is appropriate
@end

good_first_module: false
data_task: data_analysis
collection: statistics
coding_required: false

@sets_you_up_for

@end

@depends_on_knowledge_available_in
- intro_to_nhst
@end

@version_history 
No previous versions.
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
-->

# Generalized Linear Regression

@overview

## Linear models: A quick review

Many of the most common statistical tests are applications of one big overarching statistical approach, called the **General Linear Model**. 
Correlation, t-tests, ANOVAs, and linear regression are all examples of linear models. 

A linear model is anything that can be expressed as an equation for a line: 

$$
Y = \beta_0 + \beta_1 * X_1 + \beta_2 * X_2 ... \beta_n * X_n + e 
$$

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Even if you're used to running regression models in your own analyses, you may feel like your grasp of the math behind linear models is not strong. 
You're not alone!

For an approachable review of linear regression models, including a review of the equation behind them, check out this [article explaining linear regression](https://education.arcus.chop.edu/ordinary_linear_regression/).

</div>

For example, we could express a model [predicting fetal weight from sonographic measurements of femur length](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6077071/) as the equation:

$$
fetal\_weight = \beta_0 + \beta_{femoral_length} * femoral_length + e
$$ 

If we wanted to look at differences in fetal weigh by sex (a categorical predictor) instead, the equation would actually look quite similar (assuming that the sex variable was coded 0 and 1 in the data): 

$$
fetal\_weight = \beta_0 + \beta_{sex} * sex + e
$$ 

What if you want to model sex and femur length together at the same time? No problem, you can add as many predictors to a linear model as you like: 

$$
fetal\_weight = \beta_0 + \beta_{femoral_length} * femoral_length + \beta_{sex} * sex + e
$$ 

And you can allow quite a lot of complexity and nuance in a linear model as well, by including things like interaction terms or polynomial terms. 

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To learn more about interaction terms in linear models, checkout this [article about how to interpret interactions in a regression model](https://education.arcus.chop.edu/understanding-interactions/).

</div>

Linear models are so popular in statistics because equations for lines are computationally simple (even if they're not simple to understand!) but still allow us to model pretty complex relationships.

It would be handy if linear models covered all possible research questions, but unfortunately they don't!
**Generalized linear models are a way to extend the functionality of linear models to cover situations when they normally wouldn't work.**

## Why do we need generalized linear models?

Linear models are only appropriate when your outcome variable(s) are **continuous** and **unbounded**. 
If you want to model a categorical outcome, or one that's bounded (like a proportion or percent), then usually can't rely on regular linear modeling to get the job done. 

<h3>What counts and continuous and unbounded?</h3>

A variable is **continuous** if it can take any value on a scale, not just discrete options. 
For example, age is generally continuous because you can be 11 years old, or 11.5, or 11.476 years old, etc.
In contrast, experimental group (treatment vs. control) is not continuous; there's no way to be halfway between treatment and control, you're in one or the other. 
Something like medication dose could be continuous or categorical depending on how it's used. 
If patients are restricted to categorical levels of dose (e.g. high, med, or low dose groups) then it would be categorical. 
But if it's something where their dose might theoretically be anywhere on the scale, then it's continuous.

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

When you run generalized linear models, it feels very similar in many ways to running a regular linear model. 
Your output will look largely similar (coefficient tests, measurement of overall model fit, etc.). 
Under the hood, though, your statistical software is doing something very different.

Unlike linear models, there is not a single analytic solution to generalized linear models -- that means you couldn't (even if you wanted to) figure out the solution by solving the equation by hand. 
Instead, the computer uses brute force to find a solution, iterating over tons of combinations of parameter estimates and seeing which gives the best model fit.

This means the results are not exact --- they depend on the sampling algorithm being used --- so you might see very small changes if you run the model again, or if you run it on other software. There's also a risk that your model won't converge if it's too complicated and you don't have enough data.

## Logistic regression

One of the most common kinds of generalized linear model is logistic regression. 
That's a linear model using a [logit](https://en.wikipedia.org/wiki/Logit) transformation to convert the outcome that's binary (or continuous but bounded at 0 to 1, like a proportion).

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

It's not necessary to really understand the logit transformation to be able to use logistic regression, so feel free to skip this bit if you don't find it helpful. 
But if you'd like to get a better idea of how the math works, here goes!

Data bounded at 0 and 1, like probabilities or binary outcomes, can be converted to unbounded data as follows:

1. Probabilities can be converted to odds by dividing the probability by 1-(the probability). So a probability of .5 becomes $0.5/(1-0.5) = 1$.
2. Odds are unbounded at the upper end (they can theoretically go to positive infinity), but they're still bounded at the lower end, at 0. We can fix that by taking the natural log of the odds. The natural log of the odds is called a logit. For a probability of .5, the logit would be $Ln(0.5/1-0.5) = 0$.

| Logit|    Odds| Probability|
|-----:|-------:|-----------:|
|  -Inf|   0.000|       0.000|
|    -5|   0.007|       0.007|
|    -4|   0.018|       0.018|
|    -3|   0.050|       0.047|
|    -2|   0.135|       0.119|
|    -1|   0.368|       0.269|
|     0|   1.000|       0.500|
|     1|   2.718|       0.731|
|     2|   7.389|       0.881|
|     3|  20.086|       0.953|
|     4|  54.598|       0.982|
|     5| 148.413|       0.993|
|   Inf|     Inf|       1.000|

To build your intuition of probability, odds, and log-odds, it may be helpful to consider what counts as "likely" or "unlikely" for each. 
If an event is unlikely to happen, it would have a probability less than .5. 
That corresponds to an odds of less than 1, and a log-odds of less than 0. 
If an event is likely to happen, then the probability would be greater than .5, the odds would be greater than 1, and the log-odds would be greater than 0. 

</div>

### Example

Let's return to the linear model example we were considering, predicting fetal weight from femoral length measured during an ultrasound. 
As a reminder, here's the linear equation for that model: 

$$
fetal\_weight = \beta_0 + \beta_{femoral_length} * femoral_length + e
$$ 

But what if you're interested in predicting not weight, but whether or not the fetus has trisomy 21, a binary outcome?
In this case the predictor would be something like femur length (FL) relative to head size (biparietal diameter, BPD), so the variable captures whether the femur is relatively long or short for the fetus's overall size.
(Note that [although relative femur length has historically been used as a way to try to identify pregnancies affected by trisomy 21, its value as a predictor has been called into question]((https://pubmed.ncbi.nlm.nih.gov/11117083/)), especially for early in pregnancy. 
It's still a useful example of a model with a binary outcome, though!) 

$$
trisomy\_21\_dx = \beta_0 + \beta_{BPD/FL} * BPD/FL + e
$$ 

<div class = "cool-fact">
<b style="color: rgb(var(--color-highlight));">Did you know?</b><br>

Trisomy 21 is the most common chromosomal condition!
Learn more about trisomy 21 at the [National Down Syndrome Society website](https://ndss.org/about). 

</div>

Assume that `trisomy_21_dx` is coded as 0 (no) or 1 (yes) in the data.
**What would happen if you just tried to estimate this as a regular linear model?**

#### Trying a linear model 

``` -See the R code to generate some fake data
library(tidyverse)
# set the random seed so results replicate exactly with the random number generators
set.seed(24601)

# sample size
n <- 100

# random sampling of 0 and 1 for trisomy_21_dx
# sample from a normal distribution for BPD/FL, but use a higher mean if trisomy_21_dx == 1
data <- data.frame(trisomy_21_dx = sample(x = c(0,0,0,1), 
                                          size = n, 
                                          replace = TRUE)) |> 
  mutate(`BPD/FL` = ifelse(trisomy_21_dx == 1, 
                           rnorm(n, mean = 1.6, sd = .2),
                           rnorm(n, mean = 1.5, sd = .2)))
```

![Scatterplot showing BPD/FL on the x-axis (ranging from roughly 1 to 2) and `trisomy_21_dx` (0 or 1) on the y-axis. There are a range of BPD/FL values for both `trisomy_21_dx` = 1 and `trisomy_21_dx` = 0, but there appear to be more lower values of BPD/FL for `trisomy_21_dx` = 0. A straight line of best fit is overlaid on the data. It has a positive slope, starting at approximately `trisomy_21_dx` = -0.01 for BPD/FL values close to 1, and reaching `trisomy_21_dx` = 0.5 at a BPD/FL of approximately 1.9.](media/linear_prediction.png)

``` -R code for the above plot
ggplot(data, aes(y=trisomy_21_dx, x=`BPD/FL`)) + 
  geom_point() + 
  theme_bw() + 
  labs(y = "Trisomy 21 Dx") + 
  stat_smooth(method = "lm")
```

This model shows the probability of trisomy 21 diagnosis on the y-axis (0 = no, 1 = yes), and ratio of BPD to femur length on the x-axis. 
As we might expect, the probability of trisomy 21 diagnosis goes up as BPD/FL increases.

But there's one very serious problem with the above plot: 
At very low values of BPD/FL, the predicted value for trisomy 21 diagnosis actually goes below 0. 
What does it mean to have a negative probability of trisomy 21? 
That value doesn't make any sense.

#### Transform with a link function

In order for our model to generate sensible predictions, we need to transform it with a link function. 

If we take the logit of the binary outcome variable, that will give us a variable that is **unbounded**.
It runs from negative infinity to positive infinity --
negative values indicate that the outcome is unlikely, and positive values indicate that the outcome is likely. 

$$
logit(trisomy\_21\_dx) = \beta_0 + \beta_{BPD/FL} * BPD/FL + e
$$ 

Now we can estimate a linear model on the transformed outcome.
Then, after we get the estimates for the coefficients $\beta_0$ and $\beta_{BPD/FL}$, we can covert the equation back to the original scale to get predictions that will be probabilities (0-1).

If we were to actually try to calculate this for our fake data by hand, though, we would quickly run into a problem. 
The data are observed cases where the pregnancy either was or wasn't affected by trisomy 21, so they're all 0 or 1 exactly in the data. 
The log odds of 0 and 1 will be negative infinity and positive infinity, respectively. 
We can't actually work with those numbers. 
But the computer can!

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

You certainly don't need to understand how your statistical software arrives at its solution in order to run and interpret generalized linear models.
But if you're curious, one of the most common methods is called [maximum likelihood estimation](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation).

</div>

If we estimate the model with the logit link function, and then convert the predictions back to a 0-1 scale, we get something like this:

![The same scatterplot showing `BPD/FL` on the x-axis and `trisomy_21_dx` (0 or 1) on the y-axis, but the line of best fit is now a sigmoidal curve, approaching but never reaching 0 for low values of `BPD/FL`, and then curving up gently as `BPD/FL` increases.](media/linear_prediction.png)

``` -R code for the above plot
ggplot(data, aes(y=trisomy_21_dx, x=`BPD/FL`)) + 
  geom_point() + 
  theme_bw() + 
  labs(y = "Trisomy 21 Dx") + 
  stat_smooth(method = "glm", method.args = list(family = "binomial"))
```

That looks much better!
The predicted values now respect the boundaries on our outcome variable -- they can never go below 0 or above 1. 

## Other kinds of GLMs

Logistic regression (regression using a logit link function) works well for binary outcomes.
But what about other kinds of outcome variables?

If your outcome is counts of something, you can use a **Poisson** or **Negative Binomial** link function. 
For example, perhaps your outcome is the number of [Adverse Childhood Experiences (ACEs)](https://www.cdc.gov/violenceprevention/aces/fastfact.html) per patient. 
It's not possible for someone to have fewer than 0 ACEs, so that variable is bound at 0. 
It's also measured as a count (how many total ACEs experienced), so no one will have 1.2 ACEs, for example. 

For outcomes bounded at 0 and 1 (like a probability or proportion), you can use logistic regression, but a **beta** link function may be more appropriate.

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

For more details on beta regression and when to use it, see [Analysing continuous proportions in ecology and evolution: A practical introduction to beta and Dirichlet regression](https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.13234) by Douma and Weedon (2019).

</div>

If your outcome is positively skewed, especially something bound at 0, then you can use a **Gamma** or **Inverse-Gaussian** link function. 
These are especially useful for outcomes like cost, income, or length of stay -- continuous variables bound at 0 and usually positively skewed.

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To learn more about how to talk about the shape of a variable, such as identifying positive and negative skew, see the [Khan Academy lesson on shapes of distributions](https://www.khanacademy.org/kmap/measurement-and-data-j/md231-data-distributions/md231-displays-of-distributions/v/shapes-of-distributions).

</div>

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

Which of the following best describes what a "link function" is?

[( )] A link function expresses the relationship between predictors and an outcome, such as $b_0 + b_x * x$
[(X)] A link function is a transformation to convert an outcome variable to a form that is appropriate for linear regression
***
<div class = "answer">

A link function is a transformation to convert an outcome variable to a form that is appropriate for linear regression.
($b_0 + b_x * x$ is an example of a linear model, not a link function.)

The transformation that will work depends on the shape of the outcome variable to start with. 
For binary outcomes, a logit transformation works well. 
A generalized linear model with a logit link function is often called "logistic regression" for short.

</div>
***

What is an appropriate link function to transform a binary outcome variable?

[(X)] Logit
[( )] Poisson
[( )] Gamma
[( )] Gaussian
[( )] Inverse-Gaussian
***
<div class = "answer">

A **logit** (log odds) link function is usually the best choice for a binary outcome variable. 

Poisson regression works well for outcomes that are count data. 
Gamma regression and inverse-Gaussian regression work well for outcomes that are positively skewed and bounded at 0. 

Gaussian regression is actually just regular linear regression! 
A Gaussian distribution, also called a [normal distribution](https://www.khanacademy.org/math/statistics-probability/modeling-distributions-of-data/normal-distributions-library/a/normal-distributions-review), is the [default assumption for linear regression models](https://www.theanalysisfactor.com/assumptions-of-linear-models/). 
So it's actually no transformation at all!

</div>
***

## Additional Resources

There's an excellent chapter on [Logistic Regression](https://online.stat.psu.edu/stat504/lesson/6) published by Penn State.

If you'd like to compare output from different kinds of statistical software, [UCLA's IDRE](https://stats.oarc.ucla.edu/other/dae/) has published data analysis examples for logistic regression in [R](https://stats.oarc.ucla.edu/r/dae/logit-regression/), [Stata](https://stats.oarc.ucla.edu/stata/dae/logistic-regression/), [SPSS](https://stats.oarc.ucla.edu/spss/dae/logit-regression/), [SAS](https://stats.oarc.ucla.edu/sas/dae/logit-regression/), and [MPlus](https://stats.oarc.ucla.edu/mplus/dae/logit-regression/). 

## Feedback

@feedback

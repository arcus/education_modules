<!--

module_id: generalized_linear_regression
author:   Rose Hartman
email:    hartmanr1@chop.edu
version:  1.0.1
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

- $Y$ is the outcome variable (also sometimes called the response variable or the dependent variable). It's the thing you're trying to predict.
- $\beta_0$ is the y-intercept (also sometimes called the "bias term" or "bias parameter" in machine learning). It is what value, on average, you would expect $Y$ to be when all the predictors are at 0.
- $X_1$, $X_2$, etc. are predictor variables, and $\beta_1$, $\beta_2$, etc. are the coefficients (also called "slopes") for each predictor. 
- $e$ is the error term. It articulates the fact that, even after accounting for all the predictors, there will be a certain amount of random variability in $Y$, so we never expect our predictions to be completely perfect.

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Even if you're used to running regression models in your own analyses, you may feel like your grasp of the math behind linear models is not strong. 
You're not alone!

For an approachable review of linear regression models, including a review of the equation behind them, check out this [article explaining linear regression](https://education.arcus.chop.edu/ordinary_linear_regression/).

</div>

For example, we could express a model [predicting heart rate from temperature in febrile children](https://www.frontiersin.org/articles/10.3389/fped.2020.548154/full) as the equation:

$$
\text{heart} \_ \text{rate} = \beta_0 + \beta_{\text{temp}} * \text{temp} + e
$$ 

If we wanted to look at differences in heart rate by sex (a categorical predictor) instead, the equation would actually look quite similar (assuming that the sex variable was coded 0 and 1 in the data): 

$$
\text{heart} \_ \text{rate} = \beta_0 + \beta_{\text{sex}} * \text{sex} + e
$$ 

What if you want to model sex and temperature together at the same time? No problem, you can add as many predictors to a linear model as you like: 

$$
\text{heart} \_ \text{rate} = \beta_0 + \beta_{\text{temp}} * \text{temp} + \beta_{\text{sex}} * \text{sex} + e
$$ 

And you can allow quite a lot of complexity and nuance in a linear model as well, by including things like interaction terms or polynomial terms. 

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To learn more about interaction terms in linear models, checkout this [article about how to interpret interactions in a regression model](https://education.arcus.chop.edu/understanding-interactions/).

</div>

Linear models are so popular in statistics because equations for lines are computationally simple (even if they're not simple to understand!) but still allow us to model pretty complex relationships.

It would be handy if linear models covered all possible research questions, but unfortunately they don't!
This is where Generalized Linear Models come in. **Generalized linear models** are a way to extend the functionality of linear models to cover situations when they normally wouldn't work.**

## When Ordinary Linear Models Fail

Linear models are only appropriate when your outcome variable(s) are **continuous** and **unbounded** (we'll cover the definitions of continuity and boundedness more thoroughly after the following example). 
If you want to model a categorical outcome, or one that's bounded (like a proportion or percent), then you can't rely on regular linear models to get the job done. 

For example, let's return to the linear model example we were considering, predicting heart rate from temperature in febrile children. 
As a reminder, here's the linear equation for that model: 

$$
\text{heart} \_ \text{rate} = \beta_0 + \beta_{\text{temp}} * \text{temp} + e
$$ 

But what if you're interested in predicting not heart rate, but whether or not the patient is at risk for sepsis, a [binary](https://en.wiktionary.org/wiki/binary) (BI-na-ree) outcome?

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

[Sepsis](https://www.chop.edu/conditions-diseases/sepsis) is a very complex condition and predicting it is much more difficult than just using a linear model based on a patient's temperature. 
We're using a simplified model here so we can just focus on the mechanics of logistic regression, and we're using fake data to make the relationship easier to see. 
In reality, predicting and diagnosing sepsis is enormously challenging and generally requires a range of predictors including vital signs, blood work, and additional scans and tests.

For more context on the relationship between temperature and pediatric sepsis, read [Yehya et al. 2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9117394/).

</div>

$$
\text{sepsis} = \beta_0 + \beta_{\text{temp}} * \text{temp} + e
$$ 

The question of whether a patient has sepsis is, statistically, a different type of question than the question of what a patient's heart rate is. 
The patient either does or does not have sepsis -- the outcome is **binary**.

Assume that `sepsis` is coded as 0 (no) or 1 (yes) in the data.
**What would happen if you just tried to estimate this as a regular linear model?**

### Example: Predicting Sepsis with a Linear Model

Below is a plot showing (fake) temperature and sepsis data, corresponding to the model we want to run.
The line overlaid on the plot shows the results of an ordinary linear regression model predicting sepsis from temperature. 
You can read the plot by picking a temperature value along the x-axis, and then going straight up until you hit the regression line and looking across at the y-axis to see what the predicted value for sepsis is at that temperature.

**What do you notice in the plot?**

- For example, what are the values of temperature for which the predicted sepsis value is over .5? 
- As a rough guess, what do you think the approximate predicted value of sepsis would be at a normal body temperature (98.6)?

``` -See the R code to generate some fake data
library(tidyverse)
# set the random seed so results replicate exactly with the random number generators
set.seed(24601)

# sample size
n <- 100

# random sampling of 0 and 1 for sepsis
# sample from a normal distribution for heart_rate and temp, but use a higher mean if sepsis == 1
data <- data.frame(sepsis = sample(x = c(0,0,0,1), 
                                          size = n, 
                                          replace = TRUE)) |> 
  mutate(heart_rate = ifelse(sepsis == 1, 
                           rnorm(n, mean = 100, sd = 10),
                           rnorm(n, mean = 95, sd = 10)),
         temp = ifelse(sepsis == 1, 
                           rnorm(n, mean = 102, sd = 1),
                           rnorm(n, mean = 101, sd = 1)))    
```

![Scatterplot showing temperature on the x-axis (ranging from roughly 99 to 104) and sepsis (0 or 1) on the y-axis. There are a range of temperature values for both sepsis = 1 and sepsis = 0, but there appear to be more lower values of temperature for sepsis = 0. A straight line of best fit is overlaid on the data. It has a positive slope, starting at approximately sepsis = -0.01 for temperature values close to 1, and reaching sepsis = 0.6 at a temperature of approximately 104.](media/linear_prediction.png)

``` -R code for the above plot
ggplot(data, aes(y=sepsis, x=temp)) + 
  geom_point() + 
  theme_bw() + 
  labs(y = "Sepsis", x = "Temperature") + 
  scale_y_continuous(breaks = c(0,1)) + 
  stat_smooth(method = "lm")
```

This model shows the probability of sepsis on the y-axis (0 = no, 1 = yes), and temperature on the x-axis. 
As we might expect (in this made-up example), the probability of sepsis goes up as temperature increases.

But there's one very serious problem with the above plot: 
At the lowest values of temperature, the predicted value for sepsis actually goes below 0. 
What does it mean to have a negative probability of sepsis? 
That value doesn't make any sense.

**A linear model can give you nonsense predictions if your outcome variable is not continuous and unbounded.**

We'll take a closer look at what it means for a variable to be continuous and unbounded in the next sections.

### Continuity

A variable is **continuous** if it can take any value on a scale, not just discrete options. 
For example, age is generally continuous because you can be 11 years old, or 11.5, or 11.476 years old, etc.
In contrast, experimental group (treatment vs. control) is not continuous; there's no way to be halfway between treatment and control, you're in one or the other. 

Something like medication dose could be continuous or categorical depending on how it's used. 
If patients are restricted to categorical levels of dose (e.g. high, med, or low dose groups) then it would be categorical. 
But if it's something where their dose might theoretically be anywhere on the scale, then it's continuous.

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

For an excellent review of continuous vs. categorical variables, see the [Khan Academy video on discrete and continuous random variables](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/random-variables-discrete/v/discrete-and-continuous-random-variables).

</div>

### Boundedness

A variable is **unbounded** if it can theoretically extend from negative infinity at the low end to positive infinity at the high end. 
We often have variables that aren't truly unbounded, but they're close enough for all practical purposes -- for example, IQ can't technically be negative, but in practice no measured IQs are close to 0 so the data stop naturally before they hit the scale boundary at 0. 
IQ is generally treated as unbounded statistically.

Something like a probability or proportion is bounded at 0 and 1; it's not possible to have a negative probability, or one over 1. 

A variable like age might be unbounded or bounded depending on what ages you're studying. 
In a young pediatric population, age is bounded at 0 because you can't have any negative ages and a distribution of infant ages will get cutoff at that lower bound. 
But if you're studying adults, then age might be functionally unbounded in your dataset.

### Quiz: Types of Outcome Variables

Dr. Jemison wants to run a model predicting length of stay (calculated from timestamps in the electronic health record) for patients at her hospital. How would you describe her outcome variable?

[( )] continuous and unbounded
[(X)] continuous, but not unbounded
[( )] unbounded, but not continuous
[( )] neither continuous nor unbounded
***
<div class = "answer">

Length of stay is continuous because it can be any value in its range -- a patient might have a measured length of stay of 2 days, or 2.5 days, or 2 days 3 hours and 12 minutes, etc. 
It's not discrete categories of time, it's a continuous scale.

But it's not unbounded! 
Although there's no theoretical upper limit on length of stay, it would be impossible to have a length of stay less than 0 days, so the variable is bound at zero.
And unless Dr. Jemison is studying a particular population that all have unusually long hospital stays, it's likely that the data will actually run right up to the boundary at 0 -- there will plenty of patients with a length of stay of 3 days, and 2 days, and 1 day, and then of course nothing below zero.
That's why length of stay would have to be treated as bounded in this example.

If Dr. Jemison was in fact studying a population with very long hospital stays (perhaps patients with a condition that nearly always requires hospital stays of weeks or months) and none of the lengths of stay in the data were close to 0, then it could be treated as unbounded -- even though there would still technically be a lower bound at 0, that doesn't matter statistically if the data don't approach it (just like in the IQ example earlier). 

</div>
***

Eli is running an analysis to assess the effectiveness of new antipyretic (a drug to reduce fever). His main outcome variable is body temperature measured 1 hour after administration of the drug. How would you describe his outcome variable?

[(X)] continuous and unbounded
[( )] continuous, but not unbounded
[( )] unbounded, but not continuous
[( )] neither continuous nor unbounded
***
<div class = "answer">

Body temperature is continuous because it can theoretically be any value in its range.
It's also unbounded.
Although [technically there is a lower limit to the physics of temperature](https://en.wikipedia.org/wiki/Absolute_zero), none of the measurements in this study will approach that limit. 
The data in this case will taper off naturally before they get close to any hard upper or lower limit, making them functionally unbounded.  

</div>
***

Dr. Carter is building a model to predict which patients will have complications within a year of surgery. How would you describe their outcome variable?

[( )] continuous and unbounded
[( )] continuous, but not unbounded
[( )] unbounded, but not continuous
[(X)] neither continuous nor unbounded
***
<div class = "answer">

This one is a little trickier, and there are definitely multiple ways to analyze data like this. 
But the most likely scenario given the above description is that Dr. Carter has a binary variable as their main outcome (did the patient have complications within a year, yes or no).

A variable like this is not continuous -- a patient either did have complications or they didn't, they can't be halfway between "yes" and "no". 
This is also bounded. 
It's not possible for a patient to have more than "yes" complications, or less than "no" complications. 
The variable only allows those two options.

Side note: You may be wondering, "is it possible to actually have a variable that is unbounded but not continuous?" 
The answer is no, variables like that don't exist in practice. 
For a variable to be unbounded but not continuous it would have to be a categorical variable with an infinite set of possible categories, and that's just not how categorical variables generally work.
We've never come across a variable like that, but if you have definitely write in to correct us! 

</div>
***

## Link Functions

So if linear regression only works for outcome variables that are continuous and unbounded, how do you model other kinds of variables?

We can coerce problematic outcome variables into nice, continuous ones so that we can still model them with a line.
The strategy for transforming your outcome depends on what its distribution is like to begin with --- if it's binary, then you'll need a different transformation than if it's count data, for example. 

**The transformation you use to convert a problematic outcome variable (i.e. a variable that is not continuous and unbounded) into something you can use linear regression on is called a link function.**

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Generalized linear models are just linear models on data that's been transformed with a link function.

</div>

## Logistic Regression

One of the most common kinds of generalized linear model is logistic regression. 
That's a linear model using a [logit](https://en.wikipedia.org/wiki/Logit) (LOH-jit) transformation to convert an outcome that's binary.

If you want to build a model predicting a binary outcome (e.g. yes or no, true or false, has or doesn't have a diagnosis, survives or dies, relapses or doesn't), then logistic regression is a great tool!

### Talking About Chance

Logistic regression is for binary outcomes (e.g. has sepsis or doesn't have sepsis). 
But statistical models are always imperfect; each prediction will be a guess, with some expected error around that guess. 
So we express the predictions from a model of a binary outcome in terms of the _chance_ of that outcome. 
In our example, given a particular temperature, what is the predicted chance that patient has sepsis?

There are a few different ways to talk about chance. 
Two of the most commonly used are "probability" and "odds". 
They are sometimes used interchangeably in casual speech, but in statistics each has a very specific meaning:

- **Probability** is a number between 0 and 1, indicating how likely it is that a statement like "this patient has sepsis" is true. 0 means "impossible" and 1 means "definitely true". Some people prefer to multiple probability by 100 and talk in terms of percents (e.g. at this temperature, we predict a 60% chance of sepsis).
- **Odds** is a proportion --- it is the probability of an outcome (e.g. probability of sepsis) divided by the probability of the other outcome (e.g. probability of not having sepsis). Odds of 0 means "impossible", odds of 1 means an even chance, and odds greater than 1 means the outcome is increasingly likely. You can express odds in statement like "for every one patient with this temperature who does not have sepsis, we expect n patients who do have sepsis." 

### Logit Link Function

To build a regression model predicting the chance of sepsis based on temperature, we'll transform the binary sepsis variable using a **logit** link function.

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

It's not necessary to really understand the logit transformation to be able to use logistic regression, so feel free to skip this bit if you don't find it helpful. 
But if you'd like to get a better idea of how the math works, here goes!

Data bounded at 0 and 1, like probabilities or binary outcomes, can be converted to unbounded data as follows:

1. Probabilities can be converted to odds by dividing the probability by 1-(the probability). So a probability of .5 becomes $0.5/(1-0.5) = 1$.
2. Odds are unbounded at the upper end (they can theoretically go to positive infinity), but they're still bounded at the lower end at 0. We can fix that by taking the natural log of the odds. The natural log of the odds is called a logit. For a probability of .5, the logit would be $Ln(0.5/1-0.5) = 0$.

<!-- data-type="none"-->
| Logit (log-odds)|    Odds| Probability|
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

### Predicting Sepsis with a Generalized Linear Model

Let's return to our example model, predicting whether or not patients have sepsis from their temperature. 
We [tried running that with an ordinary linear model](#example-predicting-sepsis-with-a-linear-model), but because our outcome variable is **not** continuous and unbounded, the model didn't make a lot of sense.

In order for our model to generate sensible predictions, we need to transform the outcome variable first with a link function. 

If we take the logit of the binary outcome variable, that will give us a variable that is **unbounded** and **continuous**.
It runs from negative infinity to positive infinity --
negative values indicate that the outcome is unlikely, and positive values indicate that the outcome is likely. 

$$
logit(\text{sepsis}) = \beta_0 + \beta_{\text{temp}} * \text{temp} + e
$$ 

Now we can estimate a linear model on the transformed outcome.
Then, after we get the estimates for the coefficients $\beta_0$ and $\beta_{\text{temp}}$, we can covert the equation back to the original scale to get predictions that will be probabilities (0-1).

If we were to actually try to calculate this for our fake data by hand, though, we would quickly run into a problem. 
The data are observed cases where the patient either did or did not have sepsis, so they're all 0 or 1 exactly in the data. 
The log odds of 0 and 1 will be negative infinity and positive infinity, respectively. 
We can't actually work with those numbers. 
But the computer can!

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

You certainly don't need to understand how your statistical software arrives at its solution in order to run and interpret generalized linear models.
But if you're curious, one of the most common methods is called [maximum likelihood estimation](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation).

</div>

If we estimate the model with the logit link function, and then convert the predictions back to a 0-1 scale, we get something like this:

![The same scatterplot showing temperature on the x-axis and sepsis (0 or 1) on the y-axis, but the line of best fit is now a sigmoidal curve, approaching but never reaching 0 for low values of temperature, and then curving up gently as temperature increases.](media/logit_prediction.png)

``` -R code for the above plot
ggplot(data, aes(y=sepsis, x=temp)) + 
  geom_point() + 
  theme_bw() + 
  labs(y = "Sepsis", x = "Temperature") + 
  scale_y_continuous(breaks = c(0,1))  + 
  stat_smooth(method = "glm", method.args = list(family = "binomial"))
```

That looks much better!
The predicted values now respect the boundaries on our outcome variable -- they can never go below 0 or above 1. 

## Other Link Functions

Logistic regression (regression using a logit link function) works well for binary outcomes.
But what about other kinds of outcome variables?

If your outcome is counts of something, you can use a **Poisson** or **Negative Binomial** link function. 
For example, perhaps your outcome is the number of [Adverse Childhood Experiences (ACEs)](https://www.cdc.gov/violenceprevention/aces/fastfact.html) per patient. 
It's not possible for someone to have fewer than 0 ACEs, so that variable is bound at 0. 
It's also measured as a count (how many total ACEs experienced), so no one will have 1.2 ACEs, for example. 

For continuous outcomes bounded at 0 and 1 (like a probability or proportion), you can use logistic regression, but a **beta** link function may be more appropriate.

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

## Special Considerations for Generalized Linear Models

When you run generalized linear models, it feels very similar in many ways to running a regular linear model. 
Your output will look largely similar (coefficient tests, measurement of overall model fit, etc.). 
Under the hood, though, your statistical software is doing something very different.

Unlike linear models, there is not a single analytic solution to generalized linear models -- that means you couldn't figure out the solution by solving the equation by hand, even if you wanted to. 
Instead, the computer uses brute force to find a solution, iterating over tons of combinations of parameter estimates and seeing which gives the best model fit.

This means the results are not exact --- they depend on the sampling algorithm being used --- so you might see very small changes if you run the model again, or if you run it on other software. 
There's also a risk that your model won't converge (meaning you won't get any results at all) if it's too complicated and you don't have enough data. 

## Quiz: Generalized Linear Models

True or False: Generalized linear models actually still use a line for the model (like ordinary linear regression), they just transform the outcome variable first.

[(X)] TRUE
[( )] FALSE
***
<div class = "answer">

True! 
We can only use ordinary linear regression when the outcome variable is continuous and unbounded. So if you have, for example, a binary outcome then a regression model won't work unless you first transform the outcome to be continuous and unbounded -- that's what generalized linear models do! 

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

There's an excellent [chapter on Logistic Regression](https://online.stat.psu.edu/stat504/lesson/6) published by Penn State.

If you'd like to compare output from different kinds of statistical software, [UCLA's IDRE](https://stats.oarc.ucla.edu/other/dae/) has published data analysis examples for logistic regression in a variety of softwares: 
* [Logistic Regression in R](https://stats.oarc.ucla.edu/r/dae/logit-regression/) 
* [Logistic Regression in Stata](https://stats.oarc.ucla.edu/stata/dae/logistic-regression/) 
* [Logistic Regression in SPSS](https://stats.oarc.ucla.edu/spss/dae/logit-regression/)
* [Logistic Regression in SAS](https://stats.oarc.ucla.edu/sas/dae/logit-regression/)
* [Logistic Regression in MPlus](https://stats.oarc.ucla.edu/mplus/dae/logit-regression/). 

## Feedback

@feedback

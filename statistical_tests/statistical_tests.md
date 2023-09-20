<!--
author: Rose Hartman
email: hartmanr1@chop.edu
version: 1.3.2
current_version_description: 
module_type: standard
docs_version: 2.0.0
language: en
narrator: UK English Female
mode: Textbook
title: Statistical Tests in Open Source Software
comment:  This module provides an overview of the most commonly used kinds of statistical tests and links to code for running many of them in both R and python.
long_description: This module contains a curated list of links to tutorials and examples of many common statistical tests in both R and python. If you want to use R or python for data analysis but aren't sure how to write code for the statistical tests you want to run, this is a great place to start. This will be an especially valuable resource for people who have experience conducting analysis in other software (e.g. SAS, SPSS, MPlus, Matlab) and are looking to move to R and/or python. If you are new to data analysis, this module provides some structure to help you think about which statistical tests to run, and examples of code to execute them. It doesn't cover the statistical theory itself, though, so you'll need to do some additional reading before applying the code for any tests you don't already understand (there are recommended resources for learning statistical techniques at the end of the module).
estimated_time_in_minutes: 20

@pre_reqs

* Learners should already be familiar with the purpose and assumptions of any test they intend to run --- this module covers the "how" only, not the "why".
* This module also assumes some basic familiarity with either R or python. If you are brand new to one or both (or want a refresher) consider starting with our [R Basics](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_introduction/r_basics_introduction.md) or [Python Basics](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md) series first and then coming back here.

@end

@learning_objectives  
After completion of this module, learners will be able to:

- Use four key questions to help determine which statistical tests will be most appropriate in a given situation
- Discuss general differences between running statistical tests in R vs. python
- Quickly find the code they need to be able to run most common statistical tests in R or python
@end

good_first_module: false
data_task: analysis
coding_required: false
coding_level: advanced
coding_language: r, python

@sets_you_up_for

@end

@depends_on_knowledge_available_in
- r_basics_introduction
- python_basics_variables_functions_methods
- intro_to_nhst
@end

@version_history

@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
-->

# Statistical Tests in Open Source Software
@overview

## R vs python

R and python are both excellent open-source programming languages with broad support and strong data science tools. In general, you can use either one for most data analysis tasks, although one may be better suited than the other for certain situations (see [this post on strengths and weakness of R and python](https://www.ibm.com/cloud/blog/python-vs-r) to learn more). While python is a general-use programming language, though, R was built specifically for statistical analyses --- that means R has a lot of ready-made tools for data analysis that might not exist (or might not be as user-friendly) in python.

In the examples in this module, you'll notice there isn't always python code available for each test. That doesn't mean it's not possible in python (anything is possible in python if you're willing to write the code!), it's just that we don't have a good tutorial for it yet. Also, keep in mind that you have the option to [run little bits of R code in your python scripts](https://rpy2.github.io/doc/v2.9.x/html/overview.html), which might be a good workaround if you prefer python in general but want to take advantage of some of the ready-to-go stats tools in R.

## Thinking About Statistical Tests

When deciding what statistical test to run, there are a couple key considerations:

1. Do you have distinct outcome variables vs. predictor variables, or are you just measuring relationships?
2. Are your variables continuous or categorical? (For more on this distinction, see [this Khan Academy video](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/random-variables-discrete/v/discrete-and-continuous-random-variables))
3. If you have outcome variables, is it just one variable or do you have multiple outcomes?
4. Can you make [the assumptions of the General Linear Model (GLM)](https://www.theanalysisfactor.com/assumptions-of-linear-models/)?  

The answers to the above questions will impact which statistical tests will work for your analysis. Common tests below are grouped according to responses to these questions in order to help you quickly find tests that will best meet your needs.

## Example Code for Statistical Tests

In the following sections, you will find tables of links to example code for a range of statistical tests, broken into groups based on possible answers to the four questions from [the previous section](#thinking-about-statistical-tests).

Whenever possible, we've linked to tutorials that include explanation of what the code does line by line and at least some background on the rationale for the statistical test in question. There are many cases where full tutorials are not yet available, though, in which case bare example code may be all there is.

Even when a rich tutorial is available, the information linked here will generally **not** be enough for you to effectively use a statistical technique you're not already familiar with. Before applying a test you don't fully understand, seek out advice from someone experienced in the technique you want to use. We also have [recommendations for further statistical education](#additional-resources) at the end of this module.

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

This module provides links to code for running statistical tests, but it doesn't explain the statistical theory or assumptions behind the tests themselves (and neither do the linked tutorials and code examples, in many cases).

You'll need to do some additional reading before applying the code for any tests you don't already understand (there are [recommended resources for learning statistical techniques](#additional-resources) at the end of the module).

</div>

### No Distinct Outcome

If you're interested only in measuring the strength of a relationship without conceptualizing variables as predictors vs. outcomes, then you can often use a test that's a bit simpler than more formal models (and simpler is always a win!). Note that even if you don't have a specific outcome in mind, it's also generally fine to use outcome-oriented tests and just pick a variable to act as your outcome so you can assess the strength of the relationship. The results will often be interchangeable (for example, the t-test and p-value for a correlation will be the same as the t-test and p-value you would get from putting those two variables in a simple linear regression model, regardless of which one you specified as the outcome).

Principal Components Analysis (PCA) isn't an assessment of the strength of relationships per se, but rather a summary of a large number of variables revealing which variables in a data set tend to cluster together.

| Test  |  R |  python |
|---|---|---|
| Correlation | [R code](https://www.statmethods.net/stats/correlations.html), also [here](https://education.arcus.chop.edu/understanding-pearsons-r/) | [python code](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html) |
| Chi-squared test | [R code](https://stats.idre.ucla.edu/r/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-r/#chisq) | [python code](https://www.pythonfordatascience.org/chi-square-test-of-independence-python/) |
| Principal Components Analysis (PCA) | [R code](http://www.sthda.com/english/articles/31-principal-component-methods-in-r-practical-guide/118-principal-component-analysis-in-r-prcomp-vs-princomp/) | [python code](https://scipy-lectures.org/packages/scikit-learn/auto_examples/plot_pca.html#sphx-glr-packages-scikit-learn-auto-examples-plot-pca-py) |

### Continuous Outcomes

Models with continuous outcomes are the most commonly used statistical tests, and those which are most likely to be taught in an introductory stats text book. Many of them are actually not truly distinct tests but just different manifestations of one very powerful underlying model, the General Linear Model (GLM).

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

For a deeper understanding of the GLM, it helps to use matrix algebra notation, as in this [matrix algebra explanation of regression models](https://online.stat.psu.edu/stat462/node/132/). It is definitely not necessary to understand the underlying math to effectively use GLM tests, though, so only go into that if it interests you.

</div>

#### One Continuous Outcome

| Test  |  R |  python |
|---|---|---|
| Ordinary Least Squares (OLS) Linear Regression | [R code](https://education.arcus.chop.edu/ordinary_linear_regression/) | [python code](https://scipy-lectures.org/packages/statistics/index.html#formulas-to-specify-statistical-models-in-python) |
| One Sample t-tests | [R code](https://stats.idre.ucla.edu/r/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-r/#1sampt) | [python code](https://scipy-lectures.org/packages/statistics/index.html#student-s-t-test-the-simplest-statistical-test) |
| Independent Sample t-tests | [R code](https://stats.idre.ucla.edu/r/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-r/#2ittest) | [python code](https://www.pythonfordatascience.org/independent-samples-t-test-python/) |
| Dependent Sample (a.k.a. Paired) t-tests | [R code](https://stats.idre.ucla.edu/r/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-r/#pairt) | [python code](https://pythonfordatascienceorg.wordpress.com/paired-samples-t-test-python/) |
| ANOVA (one-way) | [R code](https://stats.idre.ucla.edu/r/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-r/#1anova) | [python code](https://www.pythonfordatascience.org/anova-python/) |
| ANOVA (factorial) | [R code](https://stats.idre.ucla.edu/r/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-r/#factanov) | [python code](https://www.pythonfordatascience.org/factorial-anova-python/) |

For more applications of linear regression in R, [see this summary](https://www.statmethods.net/stats/regression.html).

#### More Than One Continuous Outcome

General Linear Models with multiple outcomes are usually called "multivariate" models --- for example, multivariate multiple regression is an OLS regression model with more than one outcome (multivariate) and more than one predictor (multiple regression).

| Test  |  R |  python |
|---|---|---|
| Multivariate Multiple Regression | [R code](https://data.library.virginia.edu/getting-started-with-multivariate-multiple-regression/) | [python code](https://www.statsmodels.org/stable/generated/statsmodels.multivariate.manova.MANOVA.html) |
| Canonical Correlation Analysis | [R code](https://stats.idre.ucla.edu/r/dae/canonical-correlation-analysis/) | [python code](https://www.statsmodels.org/stable/generated/statsmodels.multivariate.cancorr.CanCorr.html#statsmodels.multivariate.cancorr.CanCorr) |
| MANOVA (one-way) | [R code](http://www.sthda.com/english/wiki/manova-test-in-r-multivariate-analysis-of-variance) | [python code](https://www.statsmodels.org/stable/generated/statsmodels.multivariate.manova.MANOVA.html) |
| MANOVA (factorial)| [R code](https://www.statmethods.net/stats/anova.html) | [python code](https://www.statsmodels.org/stable/generated/statsmodels.multivariate.manova.MANOVA.html) |

There are many more multivariate tests available, these are just a few of the most common. To learn more, see our [recommendations for learning statistics](#additional-resources) at the end of this module.

### Nonparametric Tests

Many of the [continuous outcome](#continuous-outcomes) models rely on the assumption of normally distributed errors, one of the assumptions of the General Linear Model.

That means that, after accounting for the effect of any predictors, the error of your outcome variable should be in a roughly normal distribution. This is important
for the calculation of p-values --- in order to get a probability estimate for how likely your estimate or more extreme would be under the null hypothesis (the p value), you need to have a hypothetical distribution of possible estimates. With most tests, we assume this hypothetical distribution is normal, and then we can define it easily with just two parameters: its mean, and its standard deviation. If the random error in your data does look at least roughly normal (and it really can be quite rough, thanks to the [Central Limit Theorem](http://mfviz.com/central-limit/)), then this assumption holds and your p-values will make sense.

For cases where your data are strikingly non-normal, in particular if you have very [skewed data](https://www.mathsisfun.com/data/skewness.html), you may be better off with non-parametric tests: tests that don't rely on an assumed distribution that can be described in a small number of parameters (like the normal distribution).

In many cases, there is a non-parametric version of existing parametric tests ([see this table for comparisons](https://www.scribbr.com/statistics/statistical-tests/#nonparametric)). So if, for example, you wish to perform a paired samples t-test but are concerned about skew in your data, you can conduct a Wilcoxon signed rank test instead.

| Test  |  R |  python |
|---|---|---|
| Mann-Whitney test | [R code](https://www.statmethods.net/stats/nonparametric.html) | [python code](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html) |
| Wilcoxon signed rank test | [R code](https://www.statmethods.net/stats/nonparametric.html) | [python code](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html) |
| Kruskal Wallis Test | [R code](https://www.statmethods.net/stats/nonparametric.html) | [python code](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kruskal.html#scipy.stats.kruskal) |
| Friedman Test | [R code](https://www.statmethods.net/stats/nonparametric.html) | [python code](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.friedmanchisquare.html#scipy.stats.friedmanchisquare) |
| Spearman’s r | [R code](https://www.statmethods.net/stats/correlations.html) | [python code](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html#scipy.stats.spearmanr) |

Note: If you want to run an ordinary least squares regression but have problematic outliers, consider robust regression ([R code](https://stats.idre.ucla.edu/r/dae/robust-regression/), [python code](https://www.statsmodels.org/stable/rlm.html)) instead.

### Categorical Outcomes

Although you can often use the same test whether or not your **predictors** are continuous, categorical, or a mixture of both, you generally shouldn't use the same test for both continuous and categorical **outcome** variables. Instead, you'll need a model specifically built for categorical outcomes. Here are a few common examples.

| Test  |  R |  python |
|---|---|---|
| Logistic Regression | [R code](https://stats.idre.ucla.edu/r/dae/logit-regression/) | [python code](https://www.pythonfordatascience.org/logistic-regression-python/) |
| Repeated Measures Logistic Regression | [R code](https://stats.idre.ucla.edu/r/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-r/#1replog) | |
| Multinomial Logistic Regression | [R code](https://stats.idre.ucla.edu/r/dae/multinomial-logistic-regression/) | [python code](https://www.datasklr.com/logistic-regression/multinomial-logistic-regression) |
| Binomial Test | [R code](https://stats.idre.ucla.edu/r/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-r/#bitest) | [python code](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html#scipy.stats.binomtest) |
| Chi-square goodness of fit | [R code](https://stats.idre.ucla.edu/r/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-r/#chifit) | [python code](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html)|
| Fisher's exact test | [R code](https://stats.idre.ucla.edu/r/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-r/#exact) | [python code](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.fisher_exact.html) |
| Discriminant analysis | [R code](https://stats.idre.ucla.edu/r/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-r/#discrim) | [python code](https://scikit-learn.org/stable/modules/lda_qda.html#lda-qda) |

### Other Tests

There are many, many analysis situations that do not fit neatly into any of the above categories. Below is a short list of a few popular approaches for atypical (although not uncommon!) data structures.

| Test  |  R |  python |
|---|---|---|
| Repeated Measures | [R code](https://stats.idre.ucla.edu/r/seminars/repeated-measures-analysis-with-r/) | [python code](https://www.statology.org/repeated-measures-anova-python/) |
| Structural Equation Modeling | [R code](https://lavaan.ugent.be/tutorial/index.html) | [python code](https://semopy.com/tutorial.html) |
| Survival Analysis | [R code](https://rviews.rstudio.com/2017/09/25/survival-analysis-with-r/) | [python code](https://towardsdatascience.com/survival-analysis-intuition-implementation-in-python-504fde4fcf8e)  |
| Mixed Effects Modeling | [R code](https://rpubs.com/mlmcternan/BC-lme) | [python code](https://www.statsmodels.org/stable/mixed_linear.html) |

Note: When the outcome of your mixed effects model is not continuous, you may need a generalized linear mixed model ([R code](https://stats.idre.ucla.edu/other/mult-pkg/introduction-to-generalized-linear-mixed-models/), [python code](https://www.statsmodels.org/stable/mixed_glm.html)).

## Quiz

True or False: R and python are equally user-friendly for running most statistical tests.

[( )] TRUE
[(X)] FALSE
****
<div class = "answer">

While both R and python are excellent languages for data science, R was built specifically with statistical analysis in mind, whereas python is a general purpose programming language. That often means the code to run a test in R may be shorter and easier to read than it would be in python, and the resulting output may be more informative.

That said, excellent statistical analysis tools do exist in python (see the many links in this module), and if you want additional tests or more detailed output, you can always write the code yourself.

</div>
****

True or False: The best way to find out if a new statistical test is appropriate for your data is to try to run it --- if you get no errors or warnings, then you can assume it's an appropriate test for your data and research question.

[( )] TRUE
[(X)] FALSE
****
<div class = "answer">

For many programming tasks, if your code runs without errors then you can consider it a success --- that is **not** the case with statistical programming. Any statistical software, including both R and python, will allow you to run tests that actually make no sense at all for your data or research question.

It is important that you understand the statistical theory and assumptions underlying a test before you try to apply it to your data. That usually means seeking out guidance (a consultation with a colleague, reading a stats textbook, taking a course, etc.) that goes beyond what you'll find in example code or accompanying documentation. Many statistical techniques --- even very common ones like correlations or t-tests --- take a fair amount of study to be able to understand, so make sure to allow yourself time for additional learning if you're thinking of applying a test that's new to you.

</div>
****

Which of the following are key points to consider when deciding which statistical tests to run? Select all that apply.

[[X]] The type of outcome variable(s) (continuous or categorical)
[[X]] Whether you have distinct outcomes at all
[[X]] The distribution of the residuals of your model
[[ ]] The type of predictor variable(s) (continuous or categorical)
[[?]] Hint: Remember to select all of the correct answers. For review, see [Thinking about statistical tests](#thinking-about-statistical-tests).
****
<div class = "answer">

The number (one or more than one) and type (continuous or categorical) of **outcome** variables will definitely influence the kind of statistical test that will be appropriate.  

Although there are a couple exceptions, generally the type of **predictor** variables (continuous or categorical) will not impact which test you choose; most tests work the same whether you use continuous predictors, categorical predictors, or a combination of both (although note that depending on how you run your models, categorical predictors may need to be [dummy coded](https://en.wikiversity.org/wiki/Dummy_variable_(statistics)).

The assumptions of the General Linear Model include the assumption of normally distributed residuals. If that assumption is violated, you may need to run a [nonparametric test](#nonparametric-tests).

</div>
****

**For each of the following examples, try to think through what kind of statistical test would be most appropriate and type your answer in the space provided.**

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Note that due to the open-ended nature of the questions, the quiz won't be able to automatically grade your response; it will accept any answer as correct for these questions. But when you submit your answer, explanation text will appear to help you assess your own understanding.

</div>

Dr. Rosado wants to test the relationship between patients' age and BMI. Both are continuous variables. What kind of test would you recommend?

[[correlation]]
<script>
  let input = "@input".trim();
  /.*/i.test(input);
</script>
****
<div class = "answer">

This sounds like a case with [no clear outcome variables](#no-distinct-outcome). Dr. Rosado just wants to test the strength of the relationship between the variables. If they wanted to consider age as a predictor and BMI as an outcome, then they could run this as a [linear regression](#one-continuous-outcome).

</div>
****


Di has run an experiment where patients were randomly assigned to one of two treatment conditions or a control. Now she wants to examine how three different biomarkers (continuous variables) differ based on experimental group. What kind of test would you recommend?

[[MANOVA]]
<script>
  let input = "@input".trim();
  /.*/i.test(input);
</script>
****
<div class = "answer">

Because Di has multiple outcome variables to consider, [multivariate tests](#more-than-one-continuous-outcome) would likely be appropriate. The predictor in this case will be experimental group (treatment 1, treatment 2, or control), so a one-way MANOVA would be a reasonable choice.

</div>
****

Prof. Chatti was planning to run a regression model, but they're working with data that have pronounced skew and a lot of outliers. What kind of test should they consider?

[[nonparametric]]
<script>
  let input = "@input".trim();
  /.*/i.test(input);
</script>
****
<div class = "answer">

[Nonparametric tests](#nonparametric-tests) are probably the best choice here, since they do not rely on the assumption that the model residuals conform to any particular distribution, unlike models based on the GLM.

</div>
****

## Additional Resources

For another excellent resource on the same topic, see [Choosing a Statistical Test, from the Biostatistics Handbook](http://www.biostathandbook.com/testchoice.html).

<h3>Learning statistics</h3>

There are a number of high quality resources available for learning more about statistical theory and applied data analysis techniques. Here are a few:

* There are many excellent [videos on statistics from Khan Academy](https://www.khanacademy.org/math/statistics-probability), great for building better understanding of statistical theory and probability.
* [Stanford's free statistical learning course](https://online.stanford.edu/courses/sohs-ystatslearning-statistical-learning) starts with a great introduction to the basics of linear regression models and builds to more complicated machine learning techniques. Depending on your needs, you may want to do the whole course or just use the first few weeks of it.
* [Applied Multiple Regression](https://books.google.co.in/books?id=gkalyqTMXNEC) by Cohen, Cohen, West and Aiken is very thorough without getting too mathematical (and in case you're wondering, yes, the first author is [Jacob Cohen](https://en.wikipedia.org/wiki/Jacob_Cohen_(statistician), of Cohen's d fame).
* If you expect to use tests for categorical outcomes often, [Categorical Data Analysis](https://www.google.com/books/edition/Categorical_Data_Analysis/6PHHE1Cr44AC) by Alan Agresti is an excellent guide.
* If you will be using [multivariate models](#more-than-one-continuous-outcome), check out Penn State's [STAT 505: Applied Multivariate Statistical Analysis](https://online.stat.psu.edu/stat505/) available for free online.  

Note that the recommendations above all focus on statistics specifically rather than on data science more broadly. There are also many excellent courses and textbooks available about data science, most of which include a brief and superficial introduction to statistics. If you have already worked through some data science education materials but find you want to understand the statistical tests more deeply, then these recommendations may help you find what you need.

<h3>Resources for Other Software</h3>

We recommend sticking to open source software whenever possible (to read about why check out [this Nature article on the importance of open source software for science](https://www.nature.com/articles/nature10836)).

That said, if you're used to working in non-open source statistical software, like SPSS or Stata, you may find it helpful to see the commands and output from those environments to compare to approaches in R and/or python. UCLA's Institute for Digital Research and Education has an excellent set of posts of [annotated output for most common statistical tests in Stata, SAS, SPSS, and Mplus](https://stats.idre.ucla.edu/other/annotatedoutput/) as well as several [data analysis examples](https://stats.idre.ucla.edu/other/dae/), which include a little more background on the techniques used.

## Feedback
@feedback

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

Linear models are only appropriate when your outcome variable(s) are continuous and unbounded. 
If you want to model a categorical outcome, or one that's bounded (like a proportion or percent), then usually can't rely on regular linear modeling to get the job done. 

We can coerce problematic outcome variables into nice, continuous ones so that we can still model them with a line.
The strategy for transforming your outcome depends on what its distribution is like to begin with --- if it's binary (or bounded at 0 and 1), then a logit works well. If it's count data, then a log is the right transformation, etc.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Generalized linear models are just linear models on data that's been transformed with a link function.

</div>

## Special considerations for generalized linear models

- Unlike linear models, there is not a single analytic solution to glms
- The computer uses brute force to find a solution, iterating over tons of combinations of parameter estimates and seeing which gives the bets model fit
- This means the results are not exact --- they depend on the sampling algorithm being used --- so you might see very small changes if you run the model again, or if you run it on other software
- There's a risk that your model won't converge if it's too complicated and you don't have enough data

## Example: Logistic regression

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


## Additional Resources

## Feedback

@feedback

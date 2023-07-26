<!--

author:   Rose Hartman
email:    hartmanr1@chop.edu
version:  0.0.0
current_version_description: Initial version
module_type: standard
docs_version: 1.0.0
language: en
narrator: UK English Female
mode: Textbook

title: Module title

comment:   

long_description: 

estimated_time_in_minutes: 

@pre_reqs
None.
@end

@learning_objectives  
After completion of this module, learners will be able to:

- use best practices to report a statistical test, including effect size and confidence interval

@end

good_first_module: false
data_task: data_analysis

@sets_you_up_for

- statistical_tests

@end

@depends_on_knowledge_available_in

@end

@version_history
No previous versions.
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
-->

# Module title


## What is the standard deviation?

Standard deviation (SD) is a measure of your data's variability, or dispersion.
In other words, how spread out are your data?
If all of your observations are quite close together, then you would have a small SD. 
If your observations are more spread out, then SD will be higher.

![](media/sd.png)

How can we capture that variability mathematically? 

One approach would be to measure how far each observation is from the center of the distribution, and then take the average of all of those distances to get an overall idea of how spread out the data are. 

If you start computing this for an actual dataset, though, you'll soon run into trouble because some of the observations will be above the mean (positive differences) and some will be below (negative differences), so they'll cancel each other out.
In fact, if you were to try to calculate the average distance from the mean for all the points in your data, it will always be exactly zero. Fun fact about the mean.

So to fix that you could take the absolute value of all of the differences instead, and then average those. 
That will work (and in fact it is a statistic you might sometimes see, the [mean absolute deviation](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/other-measures-of-spread/v/mean-absolute-deviation)), but absolutely values are a little cumbersome to work with mathematically. 
So instead we square all of the differences --- since a negative times itself will always be positive, we'll end up with all positive values for the squared differences.  

Of course, we have a new problem now: Since we squared everything, we're now dealing in squared units. 
The solution is to take the square root of that value. 
This is the standard deviation, with one small adjustment --- instead of dividing by n (the number of observations), as you normally would to get an average, it turns out we need to divide by n-1 or the [estimate of SD would systematically underestimate the population SD](https://en.wikipedia.org/wiki/Bessel%27s_correction#Source_of_bias). 
If we divide by n-1 instead, that corrects for the bias and then the formula works. 

Using n-1 instead of n as the denominator for variance and standard deviation is known as [Bessel's correcton](https://en.wikipedia.org/wiki/Bessel%27s_correction).

**So standard deviation measures, roughly, the average distance from the mean for all the observations in the data.**

## Z-test

Standard deviations give us a universal way to talk about how extreme observations are, indpenedent of the scale the orginal variable was on. 

If I tell you my patient scored 23 on a measure of risk factors for pancreatitis, that means nothing to you without me giving you more information about the scale --- is 23 low, normal, or high? 
If I were to tell you that he scored 2 standard deviations above the mean on the risk factor scale, though, that tells you right away that his score was quite high. 

**Expressing a value as the number of standard deviations from the mean is called a Z-score.**

A Z-test adds a cutoff for what counts as a meaningful deviation from the mean, so we have an agreed-upon way to determine when a Z-score is **statistically significant**. 
That cutoff is -1.96 below the mean and 1.96 above the mean. 

So in our example above, where the patient scores 2 standard deviations above the mean on a risk scale for pancreatitis, that would be a Z-score of 2, and it would be considered significant. 
In other words, that score is high enough that it's implausible he might truly have only average risk but just happened to score higher because of some random variability in the measurements. 

## t-test
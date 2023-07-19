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

title: Introduction to Null Hypothesis Significance Testing

comment:  This is a short, focused description of the module.

long_description: This is a longer description, which should be understandable for a lay audience.

estimated_time_in_minutes: 

@pre_reqs
List any skills or knowledge needed to complete this module here.
@end

@learning_objectives  
After completion of this module, learners will be able to:

- identify the null hypothesis and alternate hypothesis given a research question
- define a p-value
- use best practices to report a statistical test, including effect size and confidence interval

@end

@version_history 
No previous versions.
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
-->

# Module Title

@overview

## Statistical hypothesis vs. scientific hypothesis

https://education.arcus.chop.edu/null-hypothesis-testing/

## The null hypothesis


## The Bayesian approach

NHST is not the only way to test for statistical significance!

Another popular approach is Bayesian inference, named for [Thomas Bayes](https://en.wikipedia.org/wiki/Thomas_Bayes), who forumulated the [theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem) on which it is based. 
Briefly, Bayes' theorem tells us how to update the probability of something given new evidence. 

For example, without any more specific information, you would assume a given patient's probability of having beast cancer is about the same as the population probability of that cancer. 
If you find out that she's had a mamogram that detected cancer (new evidence), how does that change your estimation of her probability of having breast cancer? 
It still wouldn't be 100% (mamograms have false positives), but it would be higher than before you knew about the mamogram. 
Bayes' theorem expresses precisely, in math, what the updated probability would be, given the prior probability and the strength of the evidence (how good of a test is a mamogram?). 

In a research context, you would specify a prior probability for your hypothesis (if you want to be conservative, you might set it to zero, like a null hypothesis). 
Then you collect your data and estimate the strength of the evidence, for example as an effect size, and you can use Bayes' theorem to calculate what the probability of your hypothesis is now, given the evidence. 

**In other words, Bayesian inference allows to you directly test the questions you're actually curious about in a way that is much more intutive than NHST.**

So why aren't we all just using Bayesian inference instead of NHST?

Well, some people are! 
Bayesian methods are becoming more common, especially as more statistical software supports them.

But there are a few reasons we're opting to teach mostly NHST here instead of Bayesian inference:

- There's a huge body of existing literature using NHST, so it's important you understand those methods even if you prefer Bayesian inference for your own analysis.
- The available tools are still much more user friendly for NHST. 
- In a practical sense, using NHST vs. Bayesian inference usually won't change your conclusions. If you analyze your data with Bayesian methods and then re-analyze it with NHST, you'll almost always see comprable results. And that makes sense --- it's the same data, after all! 

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

For a much more thorough (but still approachable!) explanation of Bayes' theorem, see [the StatQuest video, "Bayes' Theorem, Clearly Explained"](https://statquest.org/bayes-theorem-clearly-explained/).

</div>

## The dangers of p-hacking

https://youtu.be/HDCOUXE3HMM

## Additional Resources

http://www.biostathandbook.com/hypothesistesting.html

https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample/more-significance-testing-videos/v/hypothesis-testing-and-p-values

## Feedback

@feedback

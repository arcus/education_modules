<!--

author:   Rose Hartman
email:    hartmanr1@chop.edu
version:  1.0.0
current_version_description: Initial version
module_type: standard
docs_version: 1.2.1
language: en
narrator: UK English Female
mode: Textbook

title: Introduction to Null Hypothesis Significance Testing

comment:  This is an introduction to NHST for biomedical researchers. 

long_description: Null Hypothesis Significance Testing (NHST) is by far the most commonly used method of statistical inference in research --- regression, ANOVAs, and t-tests are all tests from the NHST framework. This module introduces the important concepts that underlie NHST and prepares you to learn how to use NHST responsibly in your research. It does not assume any prior knowledge of statstics. 

estimated_time_in_minutes: 40

@pre_reqs
None.
@end

@learning_objectives  
After completion of this module, learners will be able to:

- identify the null hypothesis given a research question
- define a p-value
- define Type 1 error, Type 2 error, and statistical power
- describe common pitfalls of NHST in research and how to avoid them

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

# Introduction to Null Hypothesis Significance Testing

@overview

## What is NHST?

Null hypothesis significance testing (NHST) is a system for infering information about a larger population by measuring a sample. 
It is also called **frequentist** statistics. 

Although it's not the only way to do statsitical inference, it's very widely used across many different research fields. 
When you think of statistical tests, chances are you're thinking of the NHST framework. 

Unfortunately, NHST is also notoriously difficult to understand! 
In this module we'll step through the important concepts that underlie NHST and how to think about frequentist statistics in your research.

## Populations vs samples

The goal of statistical testing is generally to infer something about a **population** by looking at a **sample** from that population. 

For example, let's say you want to know how tall adult humans are on average. 
The ideal approach would be to find literally every adult person in the world and measure their height and then compute the average; this would be the true population mean. 
That strategy is impractical, though, and it's not really necessary --- if you just took a random sample of maybe 1000 adults and measured their heights, you would probably get a mean that's reasonably close to the true population mean (and the data would be much easier to collect!). 

<h3>What counts as a sample?</h3>

Crucially, in the example above, we talked about getting a **random sample from the population**.
If our population of interest is all adult humans in the world, then that means every person in the world should have an equal probability of being included in the sample. 

That's actually almost as tricky as trying to measure every person! 

We don't have a complete list of all people in the world to randomly sample from, and even if we did it might not be feasible to measure all of the people we randomly selected from it (some might be hard locate, some might not consent to being measured, etc.). 
Getting a true random sample is often very hard to do.

Typically, researchers make do with a non-random sample, or with a random sample that's not quite from their population of interest. 

In the height example, a researcher might decide to pick a city with a globally diverse population, like [Toronto, Ontario](https://en.wikipedia.org/wiki/Demographics_of_Toronto) and attempt to analyze a random sample from the city's population. 
In that case, although their population of interest is all adults in the world, the population their test actually refers to is just all Toronto adults. 
The researcher would then be making a logical leap to assume that the heights of people in Toronto are a good approximation of adult heights in general.
In the discussion section of this hypothetical paper, the researcher would need to discuss the limitations of the sample they tested and make a case for why their results are informative about the population of interest even though their sample was not ideal. 

<h3>What counts as the population?</h3>

We've been using "all adult humans" as our example population, but that's actually not as clear cut as it may first appear. 
Do we mean only all adult humans who are alive right now, or are we actually thinking about adult humans more generally, including in the past and future?

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

The definition of your population of interest depends on how you intend to generalize your results.

</div>

If you expect that your estimate of height will apply to past and future adults as well, then the population you want to test actually includes all of those theoretical people as well (making it even more impossible to collect the population data!).

Let's consider a smaller example. 
Let's say you work at a pediatric hospital, and you want to use your hospital's data to examine the outcomes of patients that were diagnosed with Covid-19 in the first year of the pandemic. 

What counts as your population of interest depends on how you want to generalize your results: 

- If you want to learn something about how pediatric patients in general (not only in your hospital) fared, then the data you have from your hospital is a (non-random) sample from a larger population (all kids who got Covid-19 in the first year of the pandemic). 
- Alternatively, maybe you're only interested in patients at your hospital specifically, but your questions are about how patients at your hospital might fare in pandemic events in general, not just specifically the Covid-19 pandemic --- in that case, your data are again a (non-random) sample. 
- It's possible, though, that your question is truly just about how patients at your hospital fared during this specific event, and you're not trying to extrapolate. In that case, your data represent the whole population of interest, not a sample. 

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

For most research questions, it's impossible to test the full population, and it's also impossible to get a true random sample from it. 
It's still an important intellectual exercise to identify what your theoretical population of interest is, so that you can think clearly about the limitations of your sample to inform you about that population (and maybe even identify ways to collect a more useful sample!). 

</div>

## The null hypothesis

Often, researchers are curious about an effect, but they usually have only a general scientific hypothesis rather than a precise statistical hypothesis. 

For example, let's say a reseacher is interested in predictors of asthma attacks and has identified an environmental toxin that may be associated with more attacks. 
The researcher's scientific hypothesis would be something like "patients with exposure to X will have more asthma attacks than patients without exposure to X." 
Although that's a perfectly good scientific hypothesis, it's not precise enough to test statistically because "more" could mean any of a range of effects (a slight increase, a huge increase, or anything in between).

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

For a great discussion of the difference between scientific and statistical hypotheses, see this [post on null hypothesis significance testing](https://education.arcus.chop.edu/null-hypothesis-testing/). 

</div>

A statistically precise hypothesis would be something like "patients with exposure to X will have an average of 2.6 more asthma attacks per year than patients without exposure to X," but that's not really useful scientifically-- if you end up finding that they have an average of 3.5 more attacks per year instead of 2.6, does that mean your hypothesis was wrong?

One way to get around this issue is to **not test your hypothesis of interest itself, but rather its opposite**. 
This is called the **null hypothesis**.

So you can test the hypothesis that "patients with exposure to X have exactly the same number of asthma attacks as patients without exposure to X"-- that is statistically precise (we're testing that the difference is equal to 0), but it's also still scientifically informative. 
If you find evidence that that hypothesis is wrong, you can conclude that there *is* a difference in number of asthma attacks per year for patients who are exposed to toxin X compared to those who aren't.

The general process for NHST is to articulate a scientific hypothesis, then identify a null hypothesis version of it and test that, and then apply the results to conclusions about your original scientific hypothesis. 
If you want to test for a relationship between two variables, then your null hypothesis would be that there is no relationship.
If you want to test whether something predicts an outcome, then your null hypothesis would be that it does not predict the outcome at all. 
If you want to test whether two or more groups differ on some measure, then your null hypothesis would be that they don't differ on that measure at all. 

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

If you're finding the logic of NHST baffling or frustrating, you're not alone! 
NHST works well in a lot of applications, but it's notoriously unintuitive and difficult to learn. 

!['Two stick figures talking in a classroom. The first says "I can't believe schools are still teaching kids about the null hypothesis. I remember reading a big study that conclusively disproved it *years* ago."'](https://imgs.xkcd.com/comics/null_hypothesis.png "[The null hypothesis](https://xkcd.com/892/) by xkcd, shared under a [CC license](https://xkcd.com/license.html).")

If it doesn't feel like this material clicks for you on the first time through (or second, or third!), give yourself a break and come back to it again later. 
You may find that the theory makes more sense after you've a had a chance to practice running tests and interpreting statistical results. 

</div>

## Interpreting results

So let's say you've thought through what your population of interest is, and you have a sample to analyze that you feel can inform you about that population.
You've articulated your scientific hypothesis, and then identified a null hypothesis to test. 
You ran the test.
**What do you do with the results?**

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

In NHST, your results can go one of two ways: you can **reject** the null hypothesis, or you can **fail to reject** the null hypothesis. 
If your results are statistically significant, that means you can reject the null hypothesis.

</div>

If your test comes back **statistically significant**, that means the data you observed would be very unlikely if the null hypothesis were true, and therefore you reject the null hypothesis.
In particular, NHST relies on the $p$-value, which gives the probability of observing an effect as big or bigger than the one in your data if the null hypothesis were true. 

By convention, we set a threshold for how small a $p$-value needs to be to reject the null hypothesis. 
This threshold is called **the criterion** or **alpha**, and most fields set it to .05. 
So if your $p$-value is below .05, meaning the chance of observing an effect as extreme (or more) as is in your data would be less than 5% (1 in 20), then the results are statistically significant and you would reject the null hypothesis. 

If your $p$-value is larger than the alpha cutoff, that means it wouldn't be that surprising to observe this size effect if the null hypothesis were true. 
Since the data don't disconfirm the null hypothesis, we don't reject it. 

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

**If you have non-significant results, does that mean the null hypothesis is true?**

No, NHST will never be able to tell you that the null is true.
That's why we talk about "failing to reject the null hypothesis" rather than saying something like "accepting" the null hypothesis, which might feel like a more natural opposite for "rejecting" it. 

This is a persistent point of confusion, even for experienced researchers and analysts.

It's not possible to accept the null hypothesis because NHST *starts* from the assumption that the null is true. 
You can reject that assumption or you can retain it, but you can't logically prove something you're already assuming.

</div>

Let's return to the example of the asthma researcher studying the difference in number of asthma attacks for patients with and without exposure to toxin X.
Their null hypothesis is that there is no difference in the number of asthma attacks for patients with exposure to X vs. those without exposure to X. 
Let's say they see an average of 5 attacks in the exposure group and 3 in the non-exposure group. 
When they run their statistical test, they'll see one of two things: 

- They get a $p$-value < .05, meaning the observed difference in number of asthma attacks would be very unlikely to occur if there was really no underlying difference between groups based on exposure. In other words, the difference between groups is statistically significant. 
- Or, they get a $p$-value ≥ .05, meaning that if there really is no underlying difference between the groups the observed difference in number of asthma attacks is something that might reasonably have occured just by chance. In other words, the difference between groups is not statistically significant, and we cannot reject the null hypothesis. 

### Type 1 and Type 2 errors

In NHST, there are two different kinds of errors you can have:

- The first is that you might get a significant result even though actually in reality the null hypothesis is correct-- when we get a $p$-value < .05, the chance of those data happening when the null is true is small (less than 5%), but it's not zero! This is called a **Type 1 error**. You can also think of this as a false positive.
- The second kind of error is that you may get non-significant results when actually the null hypothesis really was wrong. In other words, you might fail to detect a true effect. This is called a **Type 2 error**. You can also think of this as a false negative.

We can think about these possibilities in terms of a 2x2 matrix, where your results are either significant (reject) or not (fail to reject), and the real underlying truth is that the null hypothesis is either true or false. 

|               | Reject           | Fail to reject   |
| ------------- | ---------------- | ---------------- |
| Null is true  | Type 1 error     | Correct decision |
| Null is false | Correct decision | Type 2 error     |

In the case of the asthma researcher, a significant difference ($p < .05$) in number of asthma attacks for the two exposure groups might be a correct decision (there really is a difference between groups) or it might be a Type 1 error. 
If they found a non-significant difference between groups ($p ≥ .05$), then they would not reject the null hypothesis and that might be a correct decision or it might be a Type 2 error.

### Confidence and power

The probability of a Type 1 error (getting a significant result when the null hypothesis is in fact true) is called **confidence**, and it's actually the alpha critierion we set. 

As a reminder, a $p$-value is the probability of the effect observed in the data (or larger effect) if the null hypothesis were indeed true. 
And Type 1 error is when the null is true but you reject the null hypothesis, which we do whenever $p$ is less than alpha (typically .05). 
So by definition, we're saying we'll reject true null hypotheses 5% of the time. 

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

**Why .05?**

There's no good reason alpha should be .05, it's just a convention we've settled on. 
It could just as easily be .01 or .1, or even .5 (although that would mean we'd be accepting 50% chance of Type 1 errors, which would add a lot of noise to the published literature!). 

</div>

The probability of a Type 2 error (failing to reject the null hypothesis when it's really false) is represented by the letter **beta**. 
Because there are only two possible outcomes when the null is false (either correctly rejecting it or having a Type 2 error), the probability of correctly rejecting the null hypothesis (getting a significant result when the null is truly false) is 1-beta, and it is called **power**.

So if your test has statistical power of 80%, that means you have a 20% chance of incorrectly failing to reject the null hypothesis (a Type 2 error). 
If you want to decrease your chance of a Type 2 error, you need to increase your power. 

**How can you increase power?**

Power is a function of three things: alpha (which we generally don't change), your sample size, and your effect size. 
Increasing your sample size increases power, and increasing your effect size increases power. 

You may be asked to run a **power analysis**, either before beginning a study (as part of a grant application or pre-registration, for example) or when reporting your result after the fact. 
Generally, the goal of a power analysis is to assess whether or not the study as it's designed has a decent chance of detecting an effect if the null is indeed false. 

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To read more about power analyses, check out the article [Power and sample size](https://pubmed.ncbi.nlm.nih.gov/18450060) (Case & Ambrosius, 2007).

</div>

Especially in fields where data collection is expensive or difficult, researchers may be working with small sample sizes; if you're trying to test for a subtle effect with a small sample, then even if the effect is there your power might be too low for you to expect to get a significant result.
A power analysis can make it clear to you that, with the sample size you're planning, it may not be worth your time to test for the effect you're interested in. 
If a study doesn't have "enough" power (often 80% is used as a cutoff), it is said to be **underpowered**.

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

For a discussion of the prevalence and ramifications of underpowered studies in a particular field, see [Power failure: why small sample size undermines the reliability of neuroscience](https://www.nature.com/articles/nrn3475) (Button et al., 2013).

Spoilers: They estimate the median power of studies in the neurosciences to be between 8% and 31%! 
In other words, assuming that the effects they're testing for are real (the null hypotheses are false) most of these studies had less than a 50% chance of getting a significant result.

</div>

## The Bayesian approach

NHST is not the only way to infer information about a population from a sample!

Another popular approach is Bayesian inference, named for [Thomas Bayes](https://en.wikipedia.org/wiki/Thomas_Bayes), who forumulated the [theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem) on which it is based. 
Briefly, Bayes' theorem tells us how to update the probability of something given new evidence. 

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

For a much more thorough (but approachable!) explanation of Bayes' theorem, see [the StatQuest video, "Bayes' Theorem, Clearly Explained"](https://statquest.org/bayes-theorem-clearly-explained/).

</div>

For example, without any more specific information, you would assume a given patient's probability of having beast cancer is about the same as the population probability of that cancer. 
If you find out that she's had a mammogram that detected cancer (new evidence), how does that change your estimation of her probability of having breast cancer? 
It still wouldn't be 100% (mammograms have false positives), but it would be higher than before you knew about the mammogram. 
Bayes' theorem expresses precisely, in math, what the updated probability would be, given the prior probability and the strength of the evidence (how good of a test is a mammogram?). 

In a research context, you would specify a prior probability for your hypothesis (if you want to be conservative, you might set it to zero, like a null hypothesis). 
Then you collect your data and estimate the strength of the evidence, for example as an effect size, and you can use Bayes' theorem to calculate what the probability of your hypothesis is now, given the evidence. 

**In other words, Bayesian inference allows to you directly test the questions you're actually curious about in a way that is much more intutive than NHST.**

Bayesian inference also provides a natural way to incoporate additional knowledge into your hypothesis test-- if you're testing a hypothesis that seems very unlikely, the evidence should need to be much stronger than if you're testing for something that's pretty common sense. 

For example, there is a real, published study in a mainstream journal purporting to show evidence that research participants have some abililty to sense the future before it happens ([Bem, 2011](https://pubmed.ncbi.nlm.nih.gov/21280961/)). 
That article triggered several responses from other scientists arguing about a number of details in the statistical methods employed in the original study, including the fact that a Bayesian analysis would have allowed the analyst to specify a prior probability for being able to correctly anticipate random images, and that prior probability should have been quite low given the very reasonable skepticsm around extrasensory perception, or ESP (for example, see [Rouder & Morey, 2011](https://link.springer.com/article/10.3758/s13423-011-0088-7)). 
NHST considers all hypotheses to be equally likely, whether you're replicating a well-established effect or testing something controversial. 

!['Above the first panel: "Did the sun just explode? (It's night so we're not sure)". Panel 1: Two stick figures with a machine in between them. The first says, "This neutrino detector measures whether the sun has gone nova." The second says, "Then, it rolls two dice. If they both come up six, it lies to us. Otherwise, it tells the truth." And the first says, "Let's try. Detector! Has the sun gone nova?" The machine makes a "roll" noise and then repsonds, "YES." Panel 2, titled "Frequestist Statistician": The first stick figure says, "The probability of this result happening by chance is 1/36 = 0.027. Since p < 0.05, I conclude that the sun has exploded." Panel 3, titled "Bayesian Statistician": The second stick figure says, "Bet you $50 it hasn't."'](https://imgs.xkcd.com/comics/frequentists_vs_bayesians.png "[Frequentists vs. Bayesians](https://xkcd.com/1132/) by xkcd, shared under a [CC license](https://xkcd.com/license.html).")

<h3>So why aren't we all just using Bayesian inference instead of NHST?</h3>

Well, some people are! 
Bayesian methods are becoming more common, especially as more statistical software supports them.

But there are a few reasons we're opting to teach mostly NHST here instead of Bayesian inference:

- There's a huge body of existing literature using NHST, so it's important you understand those methods even if you prefer Bayesian inference for your own analysis.
- The available tools are still much more user friendly for NHST. 
- In a practical sense, using NHST vs. Bayesian inference usually won't change your conclusions. If you analyze your data with Bayesian methods and then re-analyze it with NHST, you'll almost always see comparable results. And that makes sense-- it's the same data, after all! 

## The dangers of p-hacking

As we mentioned earlier, the Type 1 error rate (the probability of incorrectly rejecting the null hypothesis when it is in fact true) is set by convention at 5%. 
That suggests that, if your scientific hypothesis is wrong and you're testing for an effect that isn't really there (i.e. the null hypothesis is true), the chance of you getting a significant result is pretty small: 1 in 20. 
In fact, though, the way many people routinely analyze data results in an actual Type 1 error rate that is much, much higher. 

Here are a few common practices that are actually **p-hacking**: 

- Using NHST to run a test that didn't occur to you until you started looking at the data
- Running several different statistical tests and then only reporting the significant ones
- Making adjustments in the data cleaning steps (transforming variables, removing outliers, etc.) after checking the results of the hypothesis test
- Running a statistical test on preliminary data and then deciding whether or not to collect more data based on whether the results are significant or not
- Looking at exploratory data analysis (plots, group means, etc.) and then picking which hypothesis tests to run based on what looks promising

All of those practices (and others) dramatically increase the probability of a Type 1 error and have contributed to large bodies of published findings that can't be replicated. 

Here's a great [StatQuest](https://statquest.org/) video explaining more about what p-hacking looks like in practice:

!?[StatQuest video "p-hacking: What it is and how to avoid it!"](https://youtu.be/HDCOUXE3HMM)

An incredibly influential paper, [False-positive psychology: Undisclosed flexibility in data collection and analysis allows presenting anything as significant](https://pubmed.ncbi.nlm.nih.gov/22006061/) (Simmons, Nelson & Simonsohn, 2011), shows what p-hacking can look like in a real data analysis, and how it dramatically changes the results you get from your statistical testing. 
Although the authors focus on psychology as an example, the article is broadly applicable to research in many domains. 

One of the things the authors emphasize is that in practice p-hacking is very easy to do accidentally, even when you have the best intentions. 
As [statistician Andrew Gelman puts it](https://statmodeling.stat.columbia.edu/2012/02/16/false-positive-psychology/):

> A key part of the story is that, although such manipulations could be performed by a cheater, they could also seem like reasonable steps to a sincere researcher who thinks there’s an effect and wants to analyze the data a bit to understand it further.

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

There are many excellent articles about the problems associated with p-hacking and how to avoid them. 
Here are three of our favorites: 

- [The garden of forking paths: Why multiple comparisons can be a problem, even when there is no “fishing expedition” or “p-hacking” and the research hypothesis was posited ahead of time](http://www.stat.columbia.edu/~gelman/research/unpublished/p_hacking.pdf) (Gelman & Loken, 2013)
- [Practices: Definition, Detection, and Recommendations for Better Practices](https://replicationindex.com/2015/01/24/qrps/) (Replication Index, 2015)
- [HARKing: hypothesizing after the results are known](https://pubmed.ncbi.nlm.nih.gov/15647155) (Kerr, 1998)

</div>

<h3>How to not p-hack</h3>

There are some corrections you can apply, such as the [False Discovery Rate](https://www.publichealth.columbia.edu/research/population-health-methods/false-discovery-rate) correction mentioned in the StatQuest video, to fix $p$-values that are artificially low because of p-hacking. 
However, by far the easiest way to not p-hack is to specify what hypotheses you intend to test and exactly how you'll test them (including the sample size you'll use) *before* you look at the data.
This is called **preregistration**.
You can do this privately, just for your own benefit, or you can publish your pregistration publicly on a repository like the [Open Science Foundation](https://help.osf.io/article/330-welcome-to-registrations).

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To read more about the benefits of preregistration, read the *PLOS Computational Biology* Methods paper [Ten simple rules for socially responsible science](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010954#sec004) (Zivony, Kardosh, Timmins & Reggev, 2023). 

</div>

## Quiz

True or False: NHST is based on the assumption that your sample is drawn **randomly** from your population of interest.

[(X)] True
[( )] False
***
<div class = "answer">

Yes, NHST assumes you have a random sample from your population of interest. 
It's often not feasible to obtain a true random sample from your population of interest, though, so part of interpreting your results is considering how your sample may differ from the population you want to generalize your results to.
This is often an important part of the discussion section in a published paper.

</div>
***

Consider a researcher who has been developing a checklist to improve care for postpartum people. The researcher has the opportunity to conduct a randomized trial at their hospital, so they randomly assign one group of birthing patients to be treated with the checklist protocol and another to get care as usual. They hypothesize that outcomes will be better in the group that gets the checklist. What null hypothesis should they test? 

[[ that there is no difference in outcomes for the group that gets the checklist vs. the group that gets care as usual]]
<script>
  let input = "@input".trim();
  /.*/i.test(input);
</script>
***
<div class = "answer">

(Note that we can't automatically grade an open-ended question like this, so it will be marked "correct" no matter what you write.)

The null hypothesis would be that there is no difference in outcomes for the group that gets the checklist vs. the group that gets care as usual.

</div>
***

Which of the following are true statements about the null hypothesis? Select all that apply.

[[ ]] If your results are not significant ($p ≥ .05$), you conclude that the null hypothesis is true.
[[X]] If your results are significant ($p < .05$), you conclude that the null hypothesis is false.
[[X]] The null hypothesis is usually the opposite of your scientific hypothesis. 
[[X]] All $p$ values are calculated based on the assumption that the null hypothesis is true. 
***
<div class = "answer">

These statements are all true, except the first one. 
When your results are not significant ($p ≥ .05$), you **cannot** conclude that the null hypothesis is true; rather, you can only fail to reject it. 

</div>
***

Which of the following is the best definition of a $p$ value?

[( )] The probability that your scientific hypothesis is true, given your observed effect
[( )] The probability that the null hypothesis is true, given your observed effect
[(X)] The probability of your observed effect being that big or bigger, given that the null hypothesis is true
[( )] The probability of your observed effect being that big or bigger, given that the null hypothesis is false
***
<div class = "answer">

For a review of this tricky topic, see [the section on Interpreting results](#interpreting-results).

</div>
***

True or False: P-hacking is a form of scientific misconduct, and although it's a serious problem, it rarely occurs.

[( )] True
[(X)] False
***
<div class = "answer">

This is not true. 
In many cases, p-hacking is done accidentally by researchers who are sincerely trying to analyze their data responsibly.
And it is unfortunately very common! 

The upside of that, though, is that there are a lot of researchers all working together to try to figure out better practices for more reproducible science. 
Some have even [publicly shared their progress as they work on finding better ways to conduct research](https://sometimesimwrong.typepad.com/wrong/2015/02/this-is-what-p-hacking-looks-like.html). 

</div>
***

Think about a study you ran in the past, or one you might run in the future. What is one thing you can do to avoid p-hacking in your own research? 

[[preregistration]]
<script>
  let input = "@input".trim();
  /.*/i.test(input);
</script>
***
<div class = "answer">

(Note that we can't automatically grade an open-ended question like this, so it will be marked "correct" no matter what you write.)

There are a lot of potential steps you can take to reduce your own p-hacking! 
You'll find lots of ideas and suggestions in the resources linked throughout this module. 
One strategy we particularly like, though is [preregistration](https://help.osf.io/article/330-welcome-to-registrations).

</div>
***

## Additional Resources

The chapter on hypothesis testing from the [Handbook of Biological Statistics](http://www.biostathandbook.com/hypothesistesting.html). 

A great Khan Academy video on [Hypothesis testing and p-values](https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample/more-significance-testing-videos/v/hypothesis-testing-and-p-values).

## Feedback

@feedback

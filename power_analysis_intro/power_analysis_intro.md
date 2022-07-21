<!--

author:   Rose Hartman
email:    hartmanr1@chop.edu
version:  0.0.1
module_template_version: 2.0.1
language: en
narrator: UK English Female
title: Introduction to Power Analysis
comment:  This is a short, focused description of the module.
long_description: This is a longer description, which should be understandable for a lay audience. It will print under "Is this module right for me?" in the overview.
estimated_time: This is rough guess of how long it might take a learner to work through the module. It will print under "Estimated time to completion" in the overview

@learning_objectives  

After completion of this module, learners will be able to:

- identify when power analyses are and are not appropriate
- explain the relationship between sample size, effect size, and statistical power
- describe the three main kinds of power analyses and what each is for

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Introduction to Power Analysis

<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

None.

**Learning Objectives**

@learning_objectives

</div>


## What is a power analysis?

## Why would you run a power analysis?

## Sample size, effect size, and power

### What is sample size?



### What is effect size?

Effect size is how dramatic the effect you're testing is.
It can be measured in many different ways, depending on your research question.
If you're interested in whether two continuous variables are related to each other, then your effect size would be measured as a [correlation](link).
If you're interested in whether two populations differ from each other on some measured variable, then your effect size would be measured as the difference between the sample means divided by their standard deviation (this statistic is called [Cohen's d](link)).

In other words, the effect size captures whether you're testing something very dramatic (a big effect size), quite subtle (a small effect size), or something in between.
What actual values typically count as "big" vs. "small" effects vary by discipline.  

One important characteristic of measures of effect size is that they **do not depend on the size of your sample**.
This is in contrast to something like a $p$ value --- $p$ can also (sort of) give you a sense of how dramatic your effect is.
A smaller $p$ value results from a bigger effect than a larger $p$ value does at the same sample size.
But, crucially, that "at the same sample size" is important; $p$ values are related to sample size, so $p$ can't be considered a pure measure of effect size.

For example, let's say you measure the strength of the relationship between two variables X and Y with a sample of 50 observations, and you calculate a correlation of $r = .319$, $p = .024$.
If you ran a replication study measuring exactly the same relationship but collected ten times the number of samples (N=500),
what would you expect to happen to your estimates?
**Take a guess:**

- [( )] $p$ value goes down, $r$ goes up
- [(X)] $p$ value goes down, $r$ stays roughly the same
- [( )] $p$ value and $r$ both stay roughly the same
- [( )] $p$ value stays roughly the same, $r$ goes up
<script output="prediction:p_vs_r">
// Correct answer is 1 (second option)

  if ("@input" == 1) {
    true
  } else {
    "@input"
  }
</script>

<script style="display: block">

if (@input(`prediction:p_vs_r`) == 0 || @input(`prediction:p_vs_r`) == 3) {

    // Explain why r shouldn't change.

    send.liascript(`Remember, we're testing the exact same question ("What is the relationship between X and Y?"), just with a larger sample.
      Correlation is an estimate of the strength and direction of a relationship in the population, regardless of the size of a given sample. We wouldn't expect the correlation to change (beyond some random variation) as a result of collecting a larger sample.
  `)
} else ""

</script>

<script style="display: block">

if (@input(`prediction:p_vs_r`) == 2 || @input(`prediction:p_vs_r`) == 3) {

  // Explain why p should decrease

  send.liascript(`Unlike measures of effect size, $p$ values are sensitive to how big your sample is.
    That's because even though the underlying effect isn't changing, the precision with which you're estimating it improves as you increase your sample size.
    In other words, you'll get less random variation sample to sample if you're taking big samples than you would with small samples.
    That makes your estimate of the $p$ value smaller as sample size gets bigger.

    For a good video on the intuition behind $p$ values:
    !?[Estimating p values from a simulation.](https://www.khanacademy.org/math/ap-statistics/xfb5d8e68:inference-categorical-proportions/idea-significance-tests/v/estimating-p-value-from-simulation)
`)
} else ""

</script>

<script style="display: block">

if (@input(`prediction:p_vs_r`) != -1) {

  // After any section is made (right or wrong), show explanation:

  send.liascript(`The value of $r$ will probably change a bit because of random error, but we wouldn't expect it to systematically go up (or down) just because we have a larger sample.

  The $p$ value, on the other hand, will almost certainly go down.`)
} else ""

</script>


#### Examples of effect size measures

Here is a table of some common statistical tests and the typical corresponding measures of effect size for each:

### What is power?

Within the null hypothesis significance testing (NHST) framework, there are theoretically four possibilities for any given test:
You can reject the null hypothesis (get a significant result) correctly or incorrectly, and you can also retain the null hypothesis (get a non-significant result) correctly or incorrectly.

Power is the probability of rejecting the null hypothesis when the null hypothesis is indeed wrong ---
in other words, power is the probability of correctly identifying a real effect.

<div class="learnmore">

If you've taken some statistics classes before, this may be reminding you of the concepts of Type 1 and Type 2 errors.
Indeed, power is closely related to Type 2 errors especially!
Although it's not necessary to understand this level of detail in order to do a power analysis, some learners may find the extra background helpful.

If you're interested in watching a good explanation of the idea of power, and how it relates to Type 1 and Type 2 errors, check out this video by KhanAcademy (if not, feel free to skip!):

!?[](https://youtu.be/6_Cuz0QqRWc)

</div>

#### High power is good!

If you're going to the trouble to collect data and analyze it in order to test a hypothesis, you want to feel like there's a decent chance that your results will come out significant if your idea is solid (i.e. you want the probability of correctly rejecting the null --- power --- to be high).

It may help to think about it from the other side:
If someone told you that even if you're correct that the null hypothesis is untrue there's still only a 20% chance of you rejecting it with your statistical test, that would be very discouraging.
You'd be facing a situation where whether the null is true or false, the most likely outcome is that you'll get non-significant results either way.
That's a low-power design.

One potential reason to conduct a power analysis is to check that you're not setting yourself up for that kind of disappointment, i.e. to check that your experiment has high enough power to make it worth your time.  

### Quiz: Sample size, effect size, and power

Which of the following are examples of measures of effect size? Select all that apply.

[[X]] correlation ($r$)
[[ ]] $p$-values
[[X]] Cohen's *d*
[[ ]] regression coefficients
[[ ]] *F*-statistics
[[ ]] 95% confidence intervals
****
<div class="answer">

Measures of effect size must be independent of sample size --- that is, they can't change just because of an increase or decrease in N.
Regression coefficients, $F$-statistics, 95% confidence intervals, and $p$-values are all sensitive to sample size.

For a review, see the list of [some common measures of effect size](#examples-of-effect-size-measures).

</div>
****

## Three different kinds of power analysis

### one



## Including highlight boxes

Include special notes with different formatting. The style "important" is for important points and key ideas. For example:

<div class = "important">
Tip: It's generally much easier to make any necessary changes to the dataframe, such as mutating variables, before sending it to the plotting command.
</div>

The style "care" is for content related to compassion, self-care, and motivation. For example:

<div class = "care">
This is a topic with a tremendous amount of jargon, which can make resources you may find online hard to understand for folks new to the field. When that happens it's easy to feel like there's something wrong with you if you don't get it, but that's not the case! Those kinds of gatekeeping explanations are a failure on the part of the writer, not the learner.
</div>


The style "help" is for educational first aid --- "help I'm lost!" suggestions. For example:

<div class = "help">
Feeling overwhelmed? It takes a long time to learn git, so don't be disheartened if it doesn't click initially. Just focus on stage, commit, and push. Ignore the rest for now, until you've had a chance to practice just the stage-commit-push process several times.
</div>

The style "warning" alerts users to potential pitfalls. For example:

<div class = "warning">
A common mistake when using `filter` is to write = when you mean ==. Remember that = is for argument assignment, and == is for testing equality in conditions. If you get them mixed up, your code won't run!
</div>

The style "learnmore" alerts users resources for further learning, especially links to a more in-depth discussion of an issue that might be touched on only briefly in the module.

<div class = "learnmore">
To learn more about the theory behind ggplot2, read [Hadley Wickham's article, "A Layered Grammar of Graphics"](http://vita.had.co.nz/papers/layered-grammar.pdf)
</div>

The style "options" is for an aside to let learners know there's another possible approach. For example:

<div class = "options">
You could also skip setting up an OSF account completely and just use github to publish and share your research products, but many people prefer to have OSF links available.
</div>
or
<div class = "options">
To do this in R instead of python, see this other module.
</div>
There's an additional style of highlight, "answer", that is used in [quizzes](#quiz).

## Additional Resources

Power, and especially the prevalence of under-powered studies, is an important part of the conversation on questionable research practices (QRPs) like p-hacking.
Here are a few resources that draw the connection between power and general issues of quality in the scientific literature:

- [Blog post on what range of p-values you might expect at different power levels](https://sometimesimwrong.typepad.com/wrong/2015/06/why-p-048-should-be-rare-and-why-this-feels-counterintuitive.html)
- [The flawed logic of chasing large effects with small samples](https://thehardestscience.com/2013/09/09/the-flawed-logic-of-chasing-large-effects-with-small-samples/)

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Introduction+to+Power+Analysis%22)!

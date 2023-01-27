<!--

author:   Joselinne Piedras-Sarabia
email:    piedrassaj@chop.edu
version:  1.0.0
module_template_version: 3.0.0
language: EN
narrator: UK English Female
title: Demystifying Algorithmic Fairness

comment:  An introduction to world of Algorithmic Fairness and the overarching problem it is attempting to fix.

long_description: This module aims to give brief overview on what the issue of bias in machine learning entails and its impact in real life scenarios. Algorithmic fairness is tackling biases with the intent of correcting and understanding the problem. Basic Data Science terminology will be helpful but it is not required for this module. 

estimated_time: 30 mins

@learning_objectives  

After completion of this module, learners will be able to:

- Articulate the meaning of bias and recall examples of bias in real-life scenarios
- List some of the biases listed in the module
- Understand what algorithmic fairness is and its goals
- Understand the future of algorithmic fairness

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Demystifying Algorithmic Fairness 

<div class = "overview">

## Overview
@comment

**Is this module right for me?** 
@long_description

**Estimated time to completion:** 
@estimated_time

**Pre-requisites**

None. This lesson is appropriate for beginners looking to learn more about the ethical problems arising in Data Science. Experience with basic Data Science terminology is helpful but it is not required.

**Learning Objectives**

@learning_objectives

</div>

## Bias in Machine Learning

Although scientists before believed machine learning was an ethical, nonbiased mechanism to approach different problems, the truth is that bias still exists in algorithms. After all, humans create algorithms. Whether biases are enforced intentionally or without knowing, biases continue to exist.

Below is a short video created by RSA with Cathy O'Neil narrating the dangers hidden with algorithms and machine learning.

https://www.youtube.com/watch?v=heQzqX35c9A 

True or False: There are over more than 100 human biases recorded that can potentially impact algorithms.

[(X)] TRUE
[( )] FALSE


## Types of Bias in Machine Learning

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

There are more than 100 human biases. These biases listed are only the tip of the iceberg.
</div>

* Reporting Bias: Algorithms that relied on data sets can have an issue in the amount of times a particular instance is reported. This is an issue within frequency. As people often document events that are unusual or rare, the data set may lack how frequent "ordinary" events go.
* Implicit Bias: These are assumptions based on a programmer's own perspective and personal experiences that may not necessarily be true for everyone. A programmer can falsely attribute assumptions to their algorithm, therefore causing a chain reaction. 
* Confirmation Bias: Developers can classify data in ways that will provoke an algorithm to prove their existing belief.
* Hidden Bias: These are underlying stereotypes that are attributed to a group of people unconciously. 

## Examples of Bias 

There are several examples of machine learning impacting real people. Below are examples briefly outlined;

* In 2019, a [Science](https://www.scientificamerican.com/article/racial-bias-found-in-a-major-health-care-risk-algorithm/) article found evidence of racial bias in commercial algorithms used by the U.S. health care system. This algorithm falsely determined Black patients were healthier than equally sick White patients. The effects of this was in both the care they recieved and their financia aid.
* COMPAS, known as the Correctional Offender Management Profiling for Alternative Sanctions, was an algorithm used to determine the likelihood of a criminal reoffending. An article published by [ProPublica](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm) led to further analysis of the algorithm, which argued Black defendants were "twice as likely" as white defendants to be classified as being of higher risk of reoffending. This led to a dispute between the publication and Equivant- the company responsible for the software. 
* A much different example shows an action that can cause previous held biases to disrupt the status quote. According to a [SFGATE](https://www.sfgate.com/news/article/sanas-startup-creates-american-voice-17382771.php) article, Sanas is a startup aiming to make call center workers sound "American" by hiding their accent. This idea as a based on Sanas assumption that callers will be nicer to hearing a "White" voice.  While Sanas brags about how their startup will "bring millions of jobs to the Philippines, millions of jobs to India", many criticize the band-aid approach Sanas took to covering actual issues in call centers- such as low pay, little to no support, and long hours. Others argued the approach dehumanized the workers, though Sanas is still continoung with their business plan. 
* And these are just some of the overwhelming amount of biases found in algorithms.

Below is a video that further provides examples visually. It contains a list of examples regarding data and bias, while also addressing the issue and what algorithmic fairness hopes to achieve. 

(https://www.youtube.com/watch?v=gV0_raKR2UQ)


## What is Algorithmic Fairness?

Algorithmic Fairness is  described as a field of research dedicated to understanding biases such as those outlined in the previous section. Described as being an ethical way of approaching biases within machine learning, researchers aim to find ways to correct these biases. Of course, there is a high amount of complexity within this issue as a whole, and one universal clear policy seems unlikely to be attained any time soon. Although the field of Algorithmic Fairness is fairly new and is everchanging, learning about its core goals and its attempts is vital to better analyze how intertwined ethics can be in Data Science. 


<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

There are differing views in how Algorithmic Fairness can impact research and more- whether for percieved good or bad. Reading these materials can help jumpstart uncomfortable conversations and acknowledge truths. While this module aims to explain the field, its relevancy, and its potential future, the actions you take are ultimately up to you. However, this can help you understand the impact your actions can take and see the impacts it will continue to take. 

</div>


## The Goals of Algorithmic Fairness

Accoridng to an article published on [towardsdatascience](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f), some of the goals of algorithmic fairness are as below;

* Finding a definition of fairness
* Finding a way to appropriately measure fairness
* Finding ways to properly inform programmers/developers, companies, researchers, and more.
* Developing ethical ways to collect data that will be interpreted as fair.

## The Future of Algorithmic Fairness

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Becoming overwhelmed or feelings of impotence can arise from looking into issues within algorithms. This is a topic that can be uncomfortable to many and even new to some. However, there is a lot of work that can be done to correct biases in algorithms, and education is one of the first steps to understanding the complexity of this issue. Ethics as a whole can be scary, but the future of Data Science is still bright. There is so much that can be done and so much that is being done as you finish this module. 
</div>

The future of Algorithmic Fairness relies on the willingness for those in and out of the field to adapt and learn. This is easier said than done, as evident by articles that have risen in popularity to list the cons of believing algorithms can ever be fair and the articles condemning them in response. However, there is a lot of work being done that can help the future of algorithms and machine learning. Below are just a few examples of people and projects advancing alogorithmic fairness:

* Canada CIFAR AI Chair [Dhanya Sridhar](https://cifar.ca/cifarnews/2022/09/12/believe-the-impossible-the-future-of-fairness-in-ai/) hopes to develop methods where machine learning can draw from "stable" and "casual" information. She plans on finding ethical ways to incorporate AI into decision making by forcing AI to focus on the fairer and newer conclusions, rather than producing outcomes based on past assumptions.
* Individuals like Matthew Finney, a data scientist researching the advancement of algorithmic bias at Harvard, look to define and measure algorithmic bias while advocating for more data scientists of color. 
* Groups like the Algorithmic Fairness Opacity Group, or the AFOG, became established to bring together different perspectives into fixing the issues of bias in algorithms. 
* There are attempts at raising awareness of the harm biases can cause. This is evident in professional seminars, online lessons, and various scientific articles.
* There are different ways being brainstormed to tackle this issue. One solution is to retrain algorithms every so often with fresh data. Of course, these possible solutions need to be tested.


## Additional Resources

The last section of the module content should be a list of additional resources, both ours and outside sources, including links to other modules that build on this content or are otherwise related.

For more information on biases, [Google](https://developers.google.com/machine-learning/crash-course/fairness/types-of-bias) has provided a crash course lesson with examples. 

For more information on algorithmic fairness and possible solutions, this article published on [TowardsDataScience](https://towardsdatascience.com/what-is-algorithm-fairness-3182e161cf9f) covers some of it. 

This [video](https://youtu.be/WNvQG2WqJG0) posted on YouTube comes hand in hand with the previous article's content. 


## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Module+Template%22)!

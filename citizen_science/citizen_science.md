<!--
module_id: citizen_science
author:   Rose Hartman
email:    hartmanr1@chop.edu
version: 1.0.5
current_version_description: Initial version.
module_type: standard
docs_version: 1.0.0
language: en
narrator: UK English Female
mode: Textbook

title: Citizen Science

comment:  This is an overview of citizen science for biomedical researchers.

long_description: This module covers the what, who, why, and how of citizen science research: what citizen science is, who volunteers, why citizen science might be a good choice for your research, and options for how to get started. Throughout, it highlights several examples of real citizen science projects being used in biomedical research and related fields. No prior knowledge is assumed.

estimated_time_in_minutes: 45

@pre_reqs
None.
@end

@learning_objectives  



- list several ways members of the public can contribute to scientific projects
- recognize several different factors that motivate people to volunteer in citizen science
- identify research questions that may be a particularly good fit for citizen science
- examine published materials from citizen science projects for things like policies on collaboration and strategies for implementation

@end

good_first_module: false
collection: intro_to_data_science
coding_required: false

@sets_you_up_for

@end

@depends_on_knowledge_available_in

@end

@version_history
No previous versions.
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md

-->

# Citizen Science

@overview

## What is citizen science?

Citizen science is a broad term that is used to describe scientific projects that invite participation from the public in any of a number of ways.
Often, volunteer citizen scientists take on work that would otherwise be done by research staff.
Some of the ways citizen scientists can participate in a project include the following:

- collect data ([Alabama Water Watch](https://aaes.auburn.edu/alabamawaterwatch/); [eBird](https://science.ebird.org/en))
- text coding, such as in the creation of training data for machine learning algorithms ([Injury Coding](https://github.com/NASA-Tournament-Lab/CDC-NLP-Occ-Injury-Coding))
- image analysis ([Placenta Profiles](https://www.zooniverse.org/projects/msbrhonclif/science-scribbler-placenta-profiles/about/research))
- problem solving ([Hewman game](https://citizensciencegames.com/games/hewmen/))
- writing and debugging code, including complex data science projects ([EvidentlyAI's Hacktoberfest](https://www.evidentlyai.com/hacktoberfest-2022))
- donate spare CPU time for computationally intense analyses ([FoldingatHome](https://foldingathome.org/))
- and more!


Citizen science is attractive to many researchers not only because of the possibility of outsourcing work on large complex data, but because it provides the potential to democratize science and allow the public more influence over and involvement in the scientific process.

<div class = "cool-fact">
<b style="color: rgb(var(--color-highlight));">Did you know?</b><br>

Some projects focus especially on how public involvement in science can put power back in the hands of communities.
For example, Public Lab works to pursue environmental justice through community science and open technology. From the [Public Lab About page](https://publiclab.org/about):

> When people can easily and reliably track local effects associated with environmental injustices — increased flooding, poor air quality, pollution and destruction of wetlands — they can make better-informed decisions and take action.

</div>


The prevalence of citizen science has increased dramatically in recent years, especially as more digital platforms emerge to support it (for example [Zooniverse](https://www.zooniverse.org/), [Globe at Night](https://www.globeatnight.org/), [Foldit](https://fold.it/), and [The Many Brains Project](https://www.testmybrain.org/)).


<div class = "history">
<b style="color: rgb(var(--color-highlight));">Historical context</b><br>

[What Is Citizen Science? – A Scientometric Meta-Analysis](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0147152) explores the history of citizen science projects, including which fields make the most use of citizen science and what scientific output they have produced.
It includes a meta-analysis of more than 2000 published papers.

</div>

What's the difference between a study participant and a citizen scientist?
---

Study participants provide only data to a project, whereas citizen scientists can be involved in a much wider range of tasks, often taking over work that would otherwise be done by research staff.
Some of the most well-known citizen science projects use volunteers to help classify images or other raw data, or collect measurements and samples to be sent in for analysis.

In some cases, though, the line between "participant" and "citizen scientist" can be blurry.
For a project like [TestMyBrain](https://www.testmybrain.org/), the only contribution most volunteers make is completing the tests --- exactly what traditional study participants would do.
What distinguishes it from a more traditional study is mostly the framing.
The project organizers provide a lot of educational content about their study designs, process, and preliminary results, inviting participants to learn about the science from a different perspective than they normally would.
Encouraging volunteers to think about how their contribution fits into the larger scientific process is characteristic of citizen science.

### Quiz: Defining citizen science

Which of the following are ways citizen scientists can help a project? Check all that apply.

[[X]] data/sample collection
[[X]] data coding
[[X]] scientific programming
[[X]] donating computing power
[[X]] influencing study design or the identification of research goals
***
<div class = "answer">

These are all examples of how citizens can support scientific discovery!

</div>
***

## What motivates citizen scientists?

Citizen scientists vary a tremendous amount in terms of the level of dedication they bring to a project, their expertise, and their motivation for participating.
In some cases, participants are attracted just by the prospect of contributing to a scientific project, especially if it's an issue they care about.
They also may be motivated by helping their community or themselves with the output of the research.


Other times, the project includes more traditional incentives like money to attract participants, or is designed as a game.

Using free smartphone games to collect research data can be quite effective, as this [article in PLOS](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0100662) shows.

Some platforms encourage engagement by letting users track their contributions, earn points, and even [form teams to compete against other volunteers](https://stats.foldingathome.org/).


There are many possible reasons to donate time and effort to a project, and different reasons may apply for different kinds of projects as well as different citizen scientists.

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

Check out this recent article exploring the reasons people participated in a citizen science project:

[Why (not) participate in citizen science? Motivational factors and barriers to participate in a citizen science program for malaria control in Rwanda](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0237396)

</div>

### Consider an existing project: Motivating volunteers

As you learn about new citizen science projects, read their recruitment materials and think about what kinds of motivation they're attempting to tap into to attract citizen scientists.

For example, here is part of the text from the [call for coding contributions for the EvidentlyAI project](https://www.evidentlyai.com/hacktoberfest-2022):

>Evidently is an open-source project, and is always open for contributions. For Hacktoberfest, we added a special set of issues labeled “hacktoberfest” to the Evidently GitHub repository. We invite data scientists to dip their toes into open-source contribution and help us add new statistical metrics and tests to detect data drift for production ML models.
>
> Don’t forget to register for Hacktoberfest by October 31! If you register and have 4 pull requests accepted among the first 40000 participants, you can get a prize.

And here is part of the homepage text from [TestMyBrain](https://testmybrain.org/):

>TestMyBrain aims to engage and collaborate with citizen scientists like you, by providing tools to help you learn about yourself. When you test yourself, you contribute to brain research.

**What strategies do you notice each project using to try to recruit citizen scientists to help?**

Keep in mind that they're recruiting two very different auidences --- EvidentlyAI needs volunteers with a specialized skill set (data scientists), but TestMyBrain can recruit from the general population.
In both cases, though, you can see they use multiple strategies to motivate potential participants.
For EvidentlyAI, they emphasize the opportunity to learn something new and join a productive community of peers, but they also mention prizes.
TestMyBrain motivates participants with the opportunity to get personlized information from the tests and also the opportunity to contribute to brain science.

### Quiz: Motivation

Which of the following might motivate someone to participate as a citizen scientist? Check all that apply.

[[X]] learning something interesting
[[X]] wanting to be involved in science
[[X]] payment or gift incentives
[[X]] fun
[[X]] competitiveness
[[X]] wanting to give back to their community
[[X]] wanting support an important cause
***
<div class = "answer">

All of these are reasons people put their time and effort towards citizen science projects!

As you learn about new citizen science projects, notice the language they use on their recruitment materials and think about what kinds of motivation they're attempting to tap into.
If you start your own citizen science project, carefully consider what might best motivate your participants.

</div>
***

## Getting started in citizen science for researchers

Although citizen science projects have been around for quite a long time, the recent increase in popularity means that for many researchers this is the first time they're considering using citizen science in their work.

So what kinds of research questions might be a good fit for citizen science, and how can you get started?

<div class = "cool-fact">
<b style="color: rgb(var(--color-highlight));">Did you know?</b><br>

One of the earliest citizen science projects is arguably the [Longitude Act of 1714](https://en.wikipedia.org/wiki/Longitude_Act), which offered a prize for anyone that could come up with an efficient way to determine a ship's longitude.

</div>

### Why choose citizen science?

Not every research question is a good fit for citizen science.
The health and medical sciences in particular often require very high levels of both data privacy and data quality, which can make crowdsourcing tricky.
However, there is a large and growing body of published research in the biomedicine using citizen science (for several examples, see [this review article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3889976/)).
In many cases, the researchers are able to succesfully bring the public in to help with their work by presenting only a very narrow slice of the data to citizen scientists (e.g. images of tissue samples with no other linked information) so as to avoid potential risks to patient privacy.

So why do biomedical researchers turn to citizen science?
Here are a few common reasons:

- to solve problems that are still too complex for computers to tackle effectively, especially [image analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3285221/) and [problem solving](https://journals.plos.org/plosone/article/comment?id=10.1371/annotation/2271ef78-f7ef-4a0d-aa34-568e7054a32b)
- to [replace expensive expert analysis](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0037245)
- to do work that would traditionally be done by research staff but doesn't necessarily require any special knowledge or training, especially [collecting measurements or observations](https://malariajournal.biomedcentral.com/articles/10.1186/1475-2875-11-43) or [processing data](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0039808)
- to access [larger and more diverse participant populations](http://cognitivehealth.tech/wp-content/uploads/2019/02/DodellFeder2019-SCZRes.pdf) than would otherwise be available through more traditional recruitment methods

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

Read [an interview with biologist Caren Cooper](https://e360.yale.edu/features/interview_caren_cooper_how_rise_of_citizen_science_is_democratizing_research) about her experience with several citizen science projects.
She discusses how using citizen science has changed the kinds of research questions she's able to ask, and also the impact participating in science has had on the individuals and communities she works with.

> In the beginning I didn’t really see the full benefits of citizen science. At first I did have this narrow, selfish view of it, like, “Oh, there are more people to help with the work and that will be great.” It didn’t take long though to learn two things. One was that I can ask these amazing questions that transcend single study sites. And the other was that I learned that these field experiences and this collaborative relationship between members of the public and scientists actually provide meaningful and really transformative experiences for individuals and for communities. 

</div>

One thing to keep in mind is that nearly all projects that rely on crowdsourcing employ some kind of validity and quality checks for the work done by volunteers (in this [review article about crowdsourcing in medical and health science](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3889976/), they note that 100% of the studies they analyzed did some kind of validity checks and/or data quality improvement).

#### Consider an existing project: Why use citizen science?

Read the abstract of this [journal article about the development of a tool for malaria diagnosis using citizen science](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0037245).

**Why did the authors want to try using crowdsourcing to analyze the blood smears?**

They tried both machine learning and classification by non-expert humans as alternatives to analysis by trained experts with the goal of making diagnosis faster, cheaper, and more widely available.
Traditional evaluation of blood smears takes a lot of time and requires trained experts who may not be readily available, especially in some of the areas of the world that have the highest malaria burden.
They wanted to see if it was feasible to get highly accurate malaria diagnoses without needing trained experts.

If you read further in the article, you'll find they also compare the human coders to a machine learning algorithm to see which did a better job classifying blood smears, and they found that their non-expert human participants classified the images with more success than the machine learning algorithm they tested.
In this case, machine learning solutions for automatic detection of infected red blood cells have struggled because of the variability in images.
The human visual system is much better adapted to see past the irrelevant variation and identify the key characteristics of infected vs. healthy cells, so this is a situation where untrained humans out perform machine learning tools.

One neat thing about their approach, though, is that it suggests the possibility for using the human and machine systems productively together --- as the humans generate a larger and larger database of classified images, the machine learning algorithm can learn on a larger and larger training dataset, which will likely improve its performance.

This is one of several studies showing how citizen science and machine learning can be used together.

### How to start a citizen science project

Large citizen science projects take a substantial effort to get off the ground but are worthwhile because they pay dividends for a long time once they reach a certain momentum.
It may take years before a project produces valuable scientific output.
Successful projects often rely on grant funding to pay for dedicated staff.

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

For an idea of what might be involved in setting up a larger project, see the [Federal Crowdsourcing and Citizen Science Toolkit](https://www.citizenscience.gov/toolkit/#) published by the U.S. government.

</div>

For a quicker start, see if there's an existing project you can join rather than starting your own.
If you can contribute time and expertise to an existing project, it may be possible for you to add tests or experiments to their ongoing work.

Another option for researchers looking to get started with citizen science without all the investment of launching a full project is to post a project on an existing platform, like [Zooniverse](https://www.zooniverse.org/lab).

#### Consider an existing project: Platforms for citizen science

Read the abstract and then scroll down to the Methodology section of this [journal article on an analysis of Google image results related to the Covid-19 pandemic](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9759662/).
The authors used citizen scientists to build the sample of images they analyzed.

**How did they set up the project? In other words, how did they recruit volunteers, provide instructions, and collect the images?**

Information about how projects are set up (such as what platforms were used, if any) is often available in the methods section of publications, but not always.
In this case, the authors provide plenty of detail about the platform they used (clickwork) and how they used it.

### Quiz: Getting started

True or False: There are platforms available online to help you launch new citizen science projects without having to do all of the setup work yourself.

[(X)] TRUE
[( )] FALSE
***
<div class = "answer">

True!
The largest online platform is [the Zooniverse](https://www.zooniverse.org/about), but there are many others.
As you learn about new citizen science projects, notice where they're hosted, or, if you can't tell, reach out to the organizers to ask them about how they set up their project.

</div>
***

Go to [TestMyBrain.org](https://testmybrain.org/about.html).  Can you, as a researcher, get access to the tests and quizzes used on the site to run your own studies?

[(X)] Yes
[( )] No
***
<div class = "answer">

Yes, they provide a special version of their website for use by researchers wanting to use their tests and quizzes.
For more information, see their [research page](https://testmybrain.org/research.html). They also have more information about collaboration at [The Many Brains Project](https://www.manybrains.net/work-with-us).

Many large citizen science projects invite collaboration.
If you're curious about whether you could contribute, or if you're interested in obtaining the data, code, or materials for an existing citizen science project, it's worth reaching out to the organizers!

</div>
***

Read the abstract of this [journal article about using citizen science to identify novel drug targets for tuberculosis](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0039808) to get an overview of the study. Why might the authors have opted to make this a citizen science project rather than using more traditional methods?

[[the research question required a tremendous amount of work that could be done without special training]]
<script>
  let input = "@input".trim();
  /./i.test(input);
</script>
***
<div class = "answer">
(Note that we can't automatically grade open ended answers to quiz questions, so the page will say your answer was correct no matter what you typed.)

There are many potential reasons to start a citizen science project, but for the authors of this article, the primary reason was the scope of the work required to answer their research question.

They needed many, many hours of annotation of the *Mycobacterium tuberculosis* genome in order to identify potential drug targets.
Because this work could be done by people without special training, it was a good candidate for crowd sourcing.

</div>
***

## Additional Resources

To learn more about citizen science and its applications in biomedical research, check out the NIH's [Guide to Biomedical Citizen Science](https://www.cancer.gov/research/resources/citizen-science).

Read the following editorial in PLOS Computational Biology: [Ten Simple Rules for Cultivating Open Science and Collaborative R&D](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003244).

To read about more examples of citizen science in action, check out this [review article covering 21 published studies in the health sciences that used crowdsourcing](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3889976/).

## Feedback

@feedback

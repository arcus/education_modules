<!--
author:   Joy Payton
email:    paytonk@chop.edu
version:  1.2
language: en
narrator: US English Female
comment:  This module provides learners with an approachable introduction to the concepts and impact of **research reproducibility**, **generalizability**, and **data reuse**, and how technical approaches can help make these goals more attainable.
long_description: **If you currently conduct research or expect to in the future**, the concepts we talk about here are important to grasp.  This material will help you understand much of the current literature and debate around how research should be conducted, and will provide you with a starting point for understanding why some practices (like writing code, even for researchers who have never programmed a computer) are gaining traction in the research field.  **If research doesn't form part of your future plans, but you want to *use* research** (for example, as a clinician or public health official), this material will help you form criteria for what research to consider the most rigorous and useful and help you understand why science can seem to vacillate or be self-contradictory.

@learning_objectives  

After completion of this module, learners will be able to:

* Explain the importance of conducting research that is **reproducible** (can be re-done by a different, unaffiliated scientist)
* Argue in support of a data analysis method that helps research be more reproducible
* Argue in support of a method in the organization and description of documents, datasets, and other files that helps research be more reproducible

@end
script:  https://code.jquery.com/jquery-3.6.0.slim.min.js

@gifPreload
<script>
(function($) {

  // Get the .gif images from the "data-alt".
	var getGif = function() {
		var gif = [];
		$('img').each(function() {
			var data = $(this).data('alt');
			gif.push(data);
		});
		return gif;
	}

	var gif = getGif();

	// Preload all the gif images.
	var image = [];

	$.each(gif, function(index) {
		image[index]     = new Image();
		image[index].src = gif[index];
	});

	// Change the image to .gif when clicked and vice versa.
	$('figure').on('click', function() {

		var $this   = $(this),
				$index  = $this.index(),

				$img    = $this.children('img'),
				$imgSrc = $img.attr('src'),
				$imgAlt = $img.attr('data-alt'),
				$imgExt = $imgAlt.split('.');

		if($imgExt[1] === 'gif') {
			$img.attr('src', $img.data('alt')).attr('data-alt', $imgSrc);
		} else {
			$img.attr('src', $imgAlt).attr('data-alt', $img.data('alt'));
		}

		// Add play class to help with the styling.
		$this.toggleClass('play');

	});

})(jQuery);
</script>
@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css
script: https://kit.fontawesome.com/83b2343bd4.js
-->

# Reproducibility, Generalizability, and Reuse: How Technology Can Help

<div class = "overview">

## Overview

@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** 1 hour

**Pre-requisites**: It is helpful if learners have conducted research, are familiar with -- by reading or writing -- peer-reviewed literature, and have experience using data and methods developed by other people.  There is no need to have any specific scientific or medical domain knowledge or technical background.    

**Learning Objectives**

@learning_objectives

</div>

## Before We Get Started

Non-technical tools that you'll need along the way, in this module and elsewhere, include a tolerance for ambiguity, the willingness to be a beginner, and practiced rebuttals to the self-critic / impostor syndrome.

The tools we're describing in this material are often complex and are used differently by different constituencies.  It can be intimidating to learn how to use **git**, for example, from people who work in large software development teams.  Users like these have years of experience with established **agile** project management practices.  They may refer to **milestones**, each related to one or more **sprints**.  They may use short acronyms (**LGTM!**) within **issues**, including linking to **commits**, and have specific naming conventions for each **branch**, along with demands to "always **squash and merge**!".  Teams with established norms may make inside jokes or references that make it seem like any mistake or deviation from procedure is a huge problem.

Do ***you*** have to learn all of this?  What's centrally important, and what's optional or ancillary?  It can be daunting even to simply get started when you run into scenarios like this one.

Jargon abounds in the tech field, and unfortunately, so does **gatekeeping.**

By gatekeeping, we mean that with or without intent, some people with greater technical experience can suggest that people with less experience don't belong or shouldn't participate.  This can take a lot of forms, such as:

* Using lots of TLAs (Three Letter Acronyms) without context or explanation.
* Snarky, unhelpful comments on Stack Overflow when a new user poses a question that doesn't meet the standards of a well-crafted, reproducible example.
* Condescension which can mask insecurity, with words like "well, clearly you should..." or "oh, just...", which add nothing to the conversation except a display of dominance.

We propose an approach that is more gate **opening** than gate **keeping** and includes positive regard such as delight at sharing knowledge.  We're not alone:

<div style = "margin: 2rem auto; max-width: 50%; font-size:0.8em; align: center;">

![XKCD Cartoon, the text of which begins "I try not to make fun of people for admitting they don't know things."  The cartoon depicts sharing knowledge as something fun.](media/ten_thousand_2x.png)

(Image used under a Creative Commons Attribution-NonCommercial 2.5 License.  Original post at https://xkcd.com/1053.)

</div>

As learners, we ask that you build your core competencies and non-technical skills by:

* Asking instructors to repeat ourselves, spell terms and explicitate acronyms.
* Asking for help with self-education.  Ask your peers and instructors for additional resources as well as criteria for evaluating whether a page you found is useful or not.
* Calling out your instructors if we act as gatekeepers.  We were beginners once, too!
* Pushing back on your inner critic.  You belong here.
* Having a sense of humor around failing code.  Your instructors have to Google syntax, too!  
* Becoming aware of the physical and psychological markers of fatigue, frustration, and the need for a break.
* Recalling your own ability to master difficult material.  The fact that something feels staggeringly difficult today doesn't mean it will always be so challenging.


<div class = "question">
True or False: If you're a driven, intelligent researcher, you're unlikely to experience failure as you learn skills like writing code.

[( )] TRUE
[(X)] FALSE

<div class = "answer">
<details><summary>Click to see an explanation of the answer.</summary>

FALSE!  Failure is something that people who work a lot with technology have to become comfortable with.  You can even think of the process of writing code as failing a lot until you get things right, then moving on to failing on the next project.  Error codes, mistakes, and confusion with new methods can be frustrating, especially if you have a lot of confidence and competence in your current way of working.  It's easier said than done, but you might find it helpful to recall that failure is a critically important tool in science, even if it's a tool we don't love to talk about.
</details>
</div>
</div>

## Concepts

The concepts of **reproducibility**, **generalizability**, and **reuse** will frame the problem space that we'll describe in this module.  We'll define these terms and give some examples.  

These concepts will be illustrated in a (charming if rage-inducing) YouTube video, *A Data Management and Sharing Snafu*.

After exploring these concepts, we'll go over some methods to address these challenges, using technology.

### Reproducibility

You may hear the terms **"reproducibility"** and/or **"replicability"**, depending on context.  Jargon varies by field and you may see either or both terms used to refer to similar goals: the ability to (1) precisely redo analyses on original data to check the original findings or (2) to carefully apply the original methods to new data to test findings in a different dataset.  Here, we usually follow what is becoming more customary and use the term "reproducible" to refer to both efforts.

The **"reproducibility crisis"** refers to the problem in peer-reviewed research in which studies *cannot* be reproduced or replicated because of insufficient information, or in which studies *fail* to be reproduced or replicated because of preventable problems in the initial research.  This is problematic because it means wasted time and money, reduced public trust in science, unverifiable claims, and lost chances for scientific consensus.

<div class = "hint" style = "align-items: center; display: flex;">

<div style = "margin: 2rem; max-width: 50%"> If you've ever tried to reproduce an analysis or study procedure from just the methods section of a paper, you probably experienced it as something like "drawing a horse" as shown here.

Providing vague methods that can't be easily reproduced can be a product of many factors influencing manuscript authors, such as:

* Preserving word count for other sections
* Assuming that implicit steps will be understood by others
* Feeling vulnerable about close scrutiny
* Not having methods well documented to begin with
* Obscuring practices that might prompt manuscript rejection or unfavorable review

When describing a multi-step task that should be able to be carried out by others, explicit step by step instructions are key.
 </div>

<div style = "margin: 2rem; max-width: 50%; float:left;">
![Humorous illustration of "how to draw a horse" which shows trivial complexity until the final step, "add small details".  This last step is not explained but provides most of the drawing of the horse.](media/horse.png)

Courtesy of artist. [Original work](https://oktop.tumblr.com/post/15352780846)

</div>

</div>

Examples of reproducibility problems exist at small and large scale.  Importantly, reproducibility affects not just interaction between scientific collaborators (or rivals), but also between "current you" and "you six months ago".  Perhaps you have felt the impact of non-reproducible research:

* Experiencing dread at trying to reproduce your own findings a few months after doing it the first time
* Being stymied by a collaborator's cryptic notes that don't explain how to do a particular analysis step
* Being unable to perform required computation because of reliance on expensive, deprecated, or proprietary software or hardware
* Results that don't replicate due to poor statistical practices, such as "p-hacking", "HARKing", convenient outlier selection, or multiple tests without correction

<div class = "question">

Think about it: when have you been frustrated by a process or study that had poor reproducibility?  Have you ever put **yourself** in a bad situation because you didn't think ahead to how you'd need to replicate your actions?

</div>

<div class = "question">
Who benefits from reproducible research practices?  Choose all that apply.

[[X]] The original authors of novel research
[[X]] Patient populations
[[X]] Journal editors and peer reviewers
[[X]] Taxpayers
[[X]] Authors of meta-analyses
[[?]] There are multiple correct answers!

<div class = "answer">
<details><summary>Click to see an explanation of the answer.</summary>

All of these groups benefit!  

Researchers who publish novel studies that can be reproduced will benefit from having more of their peers use their methods, data, and statistical approaches, which means more citations and greater influence.  Researchers may also be able to get their manuscripts into higher reputation journals than if their research was not reproducible.

Patient populations benefit from evidence based research that is robust and demonstrated in multiple settings by various teams.  Reproducible research is a key part of translating findings to clinical care.

Journal editors and peer reviewers benefit when submitters use reproducible methods because they can more quickly assess the quality of the research, test the statistical assumptions, and ensure that work can be tested by future investigation.  

Taxpayers benefit when government funded research has the greatest generalizability and highest quality.  Reproducible methods allow a single funded study to have a ripple effect that will continue to influence scientific knowledge well into the future.

Authors of meta-analyses benefit from reproducible practices like data and script sharing, because it allows them to check the findings asserted within a manuscript, compare its findings to those of other manuscripts, and discover differences between analyses that may point to the best methods to use in the practice of science in a given area.
</details>
</div>
</div>

### Generalizability

Research is **generalizable** if findings can be applied to a broad population.  

Historically, biomedical and social science research projects have struggled with generalizability due to unrepresentative data.  For example, the acronym **"WEIRD"** refers to the tendency of psychological studies to rely on subjects (often undergraduate students) who are disproportionately from **W**estern, **E**ducated, **I**ndustrialized, **R**ich, and **D**eveloped cultures -- cultures which, compared with the global population as a whole, are indeed weird.  

<div class = "hint">

Read more: in 2010 Joseph Henrich and others published a brief in *Nature* coining "WEIRD" to describe skewed participation in psychological studies.  The citation below includes a link to this piece in Penn libraries.

<div style = "margin-left: 40px; text-indent: -40px; font-size:0.8em;">

Henrich, Joseph, et al. "Most people are not WEIRD: to understand human psychology, behavioural scientists must stop doing most of their experiments on Westerners." *Nature*, vol. 466, no. 7302, 2010, p. 29. *Gale In Context: Science*, https://link.gale.com/apps/doc/A230766048/SCIC?u=upenn_main&sid=summon&xid=b438bdf6.

</div>

</div>

Until recently, many biomedical studies were conducted on disproportionately male populations and ignored disease presentation, physiology, and pharmacodynamics in women and girls (or even female lab animals).  In 1993, the [NIH Revitalization Act](https://www.ncbi.nlm.nih.gov/books/NBK236531/) began requiring NIH-funded clinical research to include women as subjects.  

This mandate did not require the same inclusivity in bench research, but NIH encouraged adoption of sex-balanced research outside of human subjects.  Two decades after the 1993 legislation, Janine Clayton and Francis Collins wrote a [pointed call to action in *Nature*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5101948/), indicating that bench researchers had not willingly followed best practices and that NIH apparently needed to require the use of female animals and cells:

> There has not been a corresponding revolution in experimental design and analyses in cell and animal research — despite multiple calls to action. Publications often continue to neglect sex-based considerations and analyses in preclinical studies. Reviewers, for the most part, are not attuned to this failure. The over-reliance on male animals and cells in preclinical research obscures key sex differences that could guide clinical studies. And it might be harmful: women experience higher rates of adverse drug reactions than men do. Furthermore, inadequate inclusion of female cells and animals in experiments and inadequate analysis of data by sex may well contribute to the troubling rise of irreproducibility in preclinical biomedical research, which the NIH is now actively working to address.

In early 2016, a policy requiring the consideration of sex as a biological variable (SABV) went into effect, and applications for NIH funding were required to comply with best practices related to sex-inclusive experimental design.  Progress in NIH's SABV efforts were [recently reported in a 2020 article](https://pubmed.ncbi.nlm.nih.gov/31971851/).

<div class = "hint">

[Listen to Janine Clayton speak about scientific rigor and female animal inclusion (5 minute listen).](https://www.wbur.org/hereandnow/2014/05/20/nih-female-animals).  A partial transcript accompanies the audio.

</div>

Human bias doesn't just lead to potentially misleading studies, but to potentially misleading research tools as well.  For example, in wearable sensor and computer vision development, engineers using skewed samples failed to realize that the optical sensors and computer vision algorithms they created may perform less well on dark skin. See, for example, [a STAT piece about Fitbits](https://www.statnews.com/2019/07/24/fitbit-accuracy-dark-skin/) and [a New York Times opinion piece about bias in facial analysis](https://www.nytimes.com/2018/06/21/opinion/facial-analysis-technology-bias.html).

The challenge of generalizability is closely linked to reproducibility.  For example, a study that demonstrates the effectiveness of exercise to improve functioning in depressed suburban teenagers may not generalize to city-dwelling adults.  In order to gain broader generalizability, this promising experiment on a limited population should be reproduced in a broader or different population.  If the original study is difficult to reproduce, however, such broader application may prove impossible.

Technological solutions alone cannot correct human problems such as recruitment bias or white overrepresentation in research personnel.  Careful use of technology can, however, add to research transparency and reproducibility and promote honest disclosure of challenges to generalizability.

<div class = "question">

Can research bias be quantified and disclosed using technology?  How can bias be reduced and generalizability improved in your research area?

</div>


### Reuse

In addition to reproducibility, another important element of research is the ability to **reuse** assets such as data and methods to related research that may not be a direct replication.  Researchers may hypothesize that a computer vision approach used to analyze moles might be useful as well in other areas of medicine that need edge detection, such as tumor classification.  Longitudinal data that provides rich phenotyping of a cohort of patients with hypermobility syndromes may be useful not just to the original orthopedic researcher community but also to cardiologists interested in comorbid vascular and ANS conditions.  The reuse of research data and methods allows researchers to collaborate in ways that advance cross-domain knowledge and professional interaction, as well as honoring the time and energy of human subjects whose data can be leveraged to get as much scientific value as possible.

The reuse of data and other research assets has numerous challenges.  You may have experienced problems in this area such as:

* Encountering resistance to sharing data, methods, scripts, or other artifacts
* Data that is not well described or labeled, or is stored in a "supplemental materials" page without context
* Overly strict informed consent documents that prevent researchers from reusing their own data or sharing it with colleagues

Survey results from a recent poll conducted by Arcus librarians and archivists (experts in data reusability) appear to indicate that CHOP researchers generally want to make their data reusable, but report (possibly incorrectly) that regulatory, ethical, or technical constraints prevent them from doing so.  Planning ahead for data reuse is an important part of grant writing, experimental design, IRB interaction, subject consent, and documentation of data and methods.

<div class = "hint">

Read more: Want to get a quick overview of some of the privacy practices that regulate responsible data sharing?  Check out [a brief article with an overview of privacy practices related to data sharing in research](https://education.arcus.chop.edu/privacy-overview/).

</div>

### A Data Management and Sharing Snafu

This is an approachable and humorous introduction to the practical impact of poor research practices leading to downstream impact.  

<div class = "question">

As you listen to the video, try to identify problematic research practices which could have been prevented by more careful use of technology.  Which of these mistakes have you encountered personally?  Which have you committed?

</div>

!?[A Data Management and Sharing Snafu, which depicts an interaction between two scientists, drawn as cartoon animals](https://www.youtube.com/watch?v=66oNv_DJuPc?cc_load_policy=1)

## Tools for Better Practices

Here we aim to provide a broad overview of how some tools and practices (scripts, data management and metdata, version control, and dependency management) can ameliorate some of the challenges we've outlined earlier.  Technology alone cannot solve the reproducibility crisis, but tools can support researchers who are trying to apply rigor and clarity to their research efforts.

Areas we won't cover here, but are critical to the consistent production of reproducible science, include researcher bias, research incentivization, publication bias, research culture, mentorship, and more.  While we assert that proper use of technology is a **necessary** part of reproducible science, technology alone is not **sufficient**.

<div class = "question">

In the "Data Management and Sharing Snafu" on the previous page, we hear some common researcher errors that are hard to prevent with technology, such as a tendency to gloss over questions with a bit of arrogance: "Everything you need to know is in the article...".  However, technology would have helped solve some of the problems that Dr. Judy Benign had to deal with.  Which of these problems are examples of the kinds of problems that may have a potential technological fix?

[[ ]] Unwillingness to share data
[[X]] Lack of clarity about what variable names mean
[[X]] Not remembering where data is located
[[X]] Software becoming unavailable
[[ ]] Mentors relying on postdocs to do most of the work
[[?]] Hint: We consider three of these to be problems with potential technological fixes!

<div class = "answer">
<details><summary>Click to see an explanation of the answer.</summary>

While technology alone can't motivate researchers to change some behavior, like being skeptical about data sharing in general or turfing much of the hard work of analysis to junior researchers, technology can help save us from ourselves in other ways.

For example, it's understandable that short variable names may be hard to connect to their full meaning, and the creation of a **data dictionary** might have helped avoid the problem of trying to decode the meaning of "SAM1" and "SAM2".  

Researchers are busy, lab churn is a fact of life, and staff like research assistants and postdocs can move on in the middle of a project.  That's why consistently applying **data management** best practices such as shared drives, version controlled repositories, or automated backup can be helpful in preventing misplaced files.  

The careful listing of **dependencies** like software can help quantify the risk of data becoming unusable, and data management practices can include saving plain text versions of encoded data, so that if a proprietary data format is no longer easily usable, a version of the data exists that can still have some utility.
</details>
</div>
</div>

### Scripts

**Scripts**, in this context, are a series of computer code instructions that handle elements of research such as:

* Ingesting data (for example, accessing a .csv file or downloading the latest data from REDCap)
* Reshaping and cleaning data (such as removing rows that don't meet given conditions for completeness or correctness, combining data from two or more sources, or creating a new field using two or more existing fields)
* Reporting statistical characteristics (for example, finding quartiles, median values, or standard deviations)
* Conducting statistical tests (e.g. ANOVA, two-sample t-tests, Cohen's effect size)
* Creating models (such as a linear or logistic model or a more complex machine learning algorithm like clustering or random forest classification)
* Saving interim datasets (e.g. storing a "cleaned" version of data for use in later steps, or creating a deidentified version of data)
* Creating data visualizations (such as boxplots, Q-Q plots, ROCs, and many more)
* Communicating methods and findings in a step-by-step way (e.g. writing a methods section from within the steps of analysis)
* And more....

Scripts may be written in free, open source tools like R, Python, Julia, and Octave, or, with care, can be extracted from commercial tools (for instance, by using a syntax file).  It's important to realize that good scripts are complete and don't rely on human memory of steps that aren't recorded in the script.  For example, using a point-and-click solution like Excel to clean data prior to analyzing it using code relies on human memory of what was done in Excel.

We can contrast scripts with tools that don't record every step explicitly.  Excel is one example we've already touched on.  You may also have been exposed to SAS, SPSS, and Stata, all of which have a point-and-click element as well as the possibility of scripted analysis.  However, many users of these tools depend on un-scripted actions such as cleaning data beforehand in a separate program and the use of point-and-click, menu driven selections.  For this reason, we suggest the use of R and Python for most research purposes.  These are widely used, well-documented and tested, and have a scientific and medical user base that is friendly for beginners.  Additionally, these tools are free and open-source, which allows for greater reproducibility, including in lower-resourced settings.  However, learning these tools requires an investment of time and energy that can be difficult for a busy clinician or scientist to justify, especially when one has already developed considerable experience in point-and-click analysis.

It's worth considering the words of an archaeological team that wrote an article about reproducible research for a lay audience in a [2017 *Slate* article](https://slate.com/technology/2017/07/how-to-make-a-study-reproducible.html):

>However, while many researchers do this work by pointing and clicking using off-the-shelf software, we tried as much as possible to write scripts in the R programming language.<br/><br/>Pointing and clicking generally leaves no traces of important decisions made during data analysis. Mouse-driven analyses leave the researcher with a final result, but none of the steps to get that result is saved. This makes it difficult to retrace the steps of an analysis, and check the assumptions made by the researcher. <br/><br/> ... <br/><br/>It's easy to understand why many researchers prefer point-and-click over writing scripts for their data analysis. Often that's what they were taught as students. It's hard work and time-consuming to learn new analysis tools among the pressures of teaching, applying for grants, doing fieldwork and writing publications. Despite these challenges, there is an accelerating shift away from point-and-click toward scripted analyses in many areas of science.


### Data management and metadata

**Data management** includes the organization, annotation, and preservation of data and metadata related to your research or clinical project.

Data management is a critical pain point for many data users.  What's the best way to wrangle the data files needed to carry out a project?  Should documents be stored in a common drive?  Using what kinds of subfolders?  How should researchers deal with emails that are sent back and forth between researchers to define a specific cohort?  What is the long-term storage strategy for this data?  Are there ways to save the data in multiple formats to accomodate unknown future needs?  Even a small project organized by a single researcher can be complex, and when a team of several researchers and supporting staff are involved, individual data management practices can collide.  A few topics that fall under the category of data management include:

* File naming standards for project files
* The format in which data is collected, and where it is stored
* How data is backed up and kept private
* Where regulatory files such as protocols are kept
* How processes and procedures are stored and kept up to date
* Who has access to what assets and when that access expires

Importantly, NIH will require data sharing & management plan for all grants starting January 2023, and it's worth practicing the skills for developing a robust plan.

**Metadata** is, in its simplest definition, data about data. Some examples of metadata might include:

* Who collected the data?
* When was the data collected?
* What units does the data use?
* What kind of thing is the data measuring?
* What are the expected values?
* Are there any codes for specific cases (e.g. missing vs. unwilling to answer vs. does not apply)?

Metadata can be found in many places. Sometimes it's implicit, as when it appears in variable names.  The variable "weight_kg", for example, discloses both the measure and the units. Often metadata is found more fully explained in **data dictionaries** or **codebooks**, where variables in a dataset are described more completely. Sometimes metadata can be found almost in passing, mentioned in an abstract or in the methods section of a paper, or in some descriptive text that accompanies a data download or a figure.

Creating useful metadata is a crucial step in reproducible science.  It's essential in helping run an efficient project involving multiple people, since helpful metadata can help reduce incorrect data collection, recording, and storage.  Metadata can help explain or contextualize some findings (e.g. when the time of day of a blood draw affects lab results).  It can also support the use, discovery, and access of data over time.

Metadata can exist at various levels of a project. For example, some metadata is overarching and describes an entire project (e.g. the institution that oversaw the data collection), while other metadata adheres to a specific data field (e.g. the make and model of a medical device that gave a certain measurement).  

REDCap is one example of software that explicitly creates a data dictionary that includes information such as the name and description of a variable, the kind of input that can appear there (alphanumeric, numeric, email format, etc.), and whether a field could identify a subject or not.  

<div class = "hint">

Discover:  The Arcus program at Children's Hospital of Philadelphia has a team of librarians and archivists who have created materials to help CHOP scientists with data management.  Their [Research Data Management Resources](https://www.research.chop.edu/arcus/resources) tend to be very practical and can be used right away to improve data management!

</div>

### Version Control

Version control is the discipline of tracking changes to files in a way that captures important information such as who made the change and why.  It also allows for reversion to previous versions of a file.

Many of us use "home grown" version control systems, such as using file names to capture who most recently added comments to a grant proposal or the date of a particular data download.  The difficulty with this is that each member of a team or lab may use different file naming protocols, and within a few months, the number of files can proliferate wildly.  Collaborators may feel unsure about deleting old versions of files, and data and file hoarding leads to delays and confusion.

Technological solutions for version control have been around for decades, and one system in particular has won the bulk of the market share in version control -- **git**.  Git is free, open source version control software.  

We won't go into details at this point, but one of the helpful aspects of git is that it allows you to see what changed, when, and by whom, in your files, along with a helpful (we hope) comment describing the change.  See below for a humorous interpretation (which isn't that far off the mark).

<div style = "margin: 2rem auto; max-width: 50%; font-size:0.8em; align: center;">

![XKCD Cartoon showing a git commit history that devolves into messages like "my hands are just typing words".  Captioned "As a project drags on, my git commit messages get less and less informative."](media/git_commit_2x.png)

(Image used under a Creative Commons Attribution-NonCommercial 2.5 License.  Original post at https://xkcd.com/1296 .)

</div>

Git and GitHub are distinct organizations with different products.  Git is a free, open-source version control system, and GitHub is a company that provides services to make it easier to use git for software development and related uses.  GitHub has free tier use as well as paid services.  

Some institutions, [including Children's Hospital of Philadelphia](https://github.research.chop.edu), pay for an enterprise version of GitHub that may be accessible only to institutional users on a secure network, and not available to the general public.  For science that can be more broadly shared, many researchers use the publicly available [GitHub.com](https://github.com), which is a website run by GitHub.  As an example of another GitHub resource, many git users find that the [GitHub Desktop](https://desktop.github.com/) software is useful for working with git on their local computers.

### Dependency Management

If you've ever created a slide show in one computer only to have it look terrible in another, you know the problem that **dependencies** can cause.  Dependencies are requirements such as (in our slide show example) having the same fonts installed, having a default group of settings turned on, having the same version of PowerPoint or other software running, and having access to particular image or sound files.  Dependencies that are well-documented and understood will help make research more reproducible.  Dependencies that are undocumented or not known about will inevitably cause problems.  Sometimes it isn't clear whether something is a hard dependency (this value or program *must* be the same as what you used) or just a circumstance (you used a particular version of Python but there's no reason to think that previous or subsequent versions wouldn't work just as well).  For this reason, recording both known and possible dependencies is a helpful practice. Common dependencies in research and data analytics include:

* Operating system: does your use of particular software require the use of Microsoft Windows 10 or later?
* Regional data formatting: does your analysis assume that decimal values use a period, not a comma, to set off the decimal value?
* Program versions: did you conduct your analysis in R 3.6?  Have you tried it in 3.7?
* Technical data formatting: does your analysis expect a .csv of data with specified columns holding certain measures?
* Access to reference files: are you aligning to hg38 or to a previous reference genome?
* Hardware requirements: does your research paradigm require a particular kind of hardware for generating stimuli or recording response?

Dependency management is an approach that makes it easier to determine the precise set of tools and inputs required by your data collection and analysis.  Every research effort should document which tools were used and which version of each was employed.  This can be as simple as a text file, or could include installation instructions or even a file that includes the exact versions of software used in the original research, in order to create a computer environment that can perform the analysis under the original conditions.

## Additional Materials

Enjoy some supplemental materials that you might find useful, and feel free to suggest additions!  


### Center for Open Science

The Center for Open Science is one of the foremost thought leaders in reproducible science.  Their materials provide rich reading material and practical support for researchers and explore topics that are beyond the scope of this training, including how incentivization is contributing to ineffective science.  

>The mission of the Center for Open Science (COS) is to increase openness, integrity, and reproducibility of research. We envision a future scholarly community in which the process, content, and outcomes of research are openly accessible by default. All scholarly content is preserved and connected and transparency is an aspirational good for scholarly services. All stakeholders are included and respected in the research lifecycle and share pursuit of truth as the primary incentive and motivation for scholarship. Achieving the mission requires culture change in the incentives that drive researchers’ behavior, the infrastructure that supports research, and the business models that dominate scholarly communication. This Strategic Plan is the result of collective effort by the COS team, board, and community stakeholders.

<a href = "https://www.cos.io/" target="blank">COS Website</a>

### John Oliver

A 20-minute long clip from John Oliver's infotainment show "Last Week Tonight" includes off-color language and adult references but is a great introduction to topics including:

* p-hacking
* non-publication of null findings (the "file drawer" problem)
* replication studies
* incentivization problems in research
* scientific communication in mass media
* generalizability
* public support of science
* industry funding

Among many other quotable moments, Oliver drives home the point of how research methods have important public funding and public policy implications.  

>"In science, you don't just get to cherry-pick the parts that justify what what you were going to do anyway! ... And look, this is dangerous... that is what leads people to think that manmade climate change isn't real or that vaccines cause autism...."

To watch this (intermittently NSFW) segment, [watch it directly in YouTube](https://www.youtube.com/watch?v=0Rnq1NpHdmw).

### For Excel Users

* An educator for the Arcus program at Children's Hospital of Philadelphia [shares some harm reduction techniques for Excel users](https://education.arcus.chop.edu/excel-caveats/)
* A former user of Excel [shares why he's moved on to using scripted code and gives helpful hints to those still using Excel](https://education.arcus.chop.edu/the-spreadsheet-betrayal/)

### Mentioned in This Module

* [How to Draw a Horse](https://oktop.tumblr.com/post/15352780846)
* [Henrich, Joseph, et al. "Most people are not WEIRD: to understand human psychology, behavioural scientists must stop doing most of their experiments on Westerners."](https://link.gale.com/apps/doc/A230766048/SCIC?u=upenn_main&sid=summon&xid=b438bdf6)
* [NIH Revitalization Act](https://www.ncbi.nlm.nih.gov/books/NBK236531/)
* [NIH to balance sex in cell and animal studies](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5101948/)
* [Sex as a Biological Variable: A 5-Year Progress Report and Call to Action](https://pubmed.ncbi.nlm.nih.gov/31971851/)
* [NIH: Scientists Must Include Female Animals In Testing](https://www.wbur.org/hereandnow/2014/05/20/nih-female-animals)
* [Fitbits and other wearables may not accurately track heart rates in people of color](https://www.statnews.com/2019/07/24/fitbit-accuracy-dark-skin/)
* [When the Robot Doesn’t See Dark Skin](https://www.nytimes.com/2018/06/21/opinion/facial-analysis-technology-bias.html)
* [Data Sharing and Privacy: A Very Cursory Overview](https://education.arcus.chop.edu/privacy-overview/)
* [A Data Management and Sharing Snafu](https://www.youtube.com/watch?v=66oNv_DJuPc?cc_load_policy=1)
* [Here’s How We Made Our Study Reproducible](https://slate.com/technology/2017/07/how-to-make-a-study-reproducible.html)
* [Arcus Resources](https://www.research.chop.edu/arcus/resources)
* [Git Commit](https://xkcd.com/1296)
* [Enterprise GitHub](https://github.research.chop.edu)
* [GitHub.com](https://github.com)
* [GitHub Desktop](https://desktop.github.com/)

## Feedback

In the beginning, we stated some learning objectives:

@learning_objectives

Now that you've completed this module, we ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Reproducibility,+Generalizability,+and+Reuse:+How+Technology+Can+Help%22)!

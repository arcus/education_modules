<!--
author:   Joy Payton
email:    paytonk@chop.edu
version:  1.0.0
module_template_version: 2.0.0
language: en
narrator: US English Female
title: How to Troubleshoot
comment:  Learning to use technical methods like coding and version control in your research inevitably means running into problems.  Learn practical methods for troubleshooting and moving past error codes and other difficulties.
long_description: When technical methods, such as writing code, using version control, and creating data visualizations are used, there will moments when a cryptic error message appears or the code simply doesn't do what it was intended to do.  This module will help people at various levels of technical expertise learn how to troubleshoot in tech more effectively.
estimated_time: 30 minutes

@learning_objectives  

After completion of this module, learners will be able to:

- Describe technical problems more effectively
- Explain why a "reproducible example" is critical to asking for help
- Find potentially helpful answers in Stack Overflow


@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# How to Troubleshoot

<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

This module assumes that learners have started using technical methods such as writing code.  However, this module is useful for learners at any stage of their technical journey, and is not specific to any particular methods or programming languages. 

**Learning Objectives**

@learning_objectives

</div>


## First, Don't Panic

Some technical types (including the author of this module) are also fans of *The Hitchhiker's Guide to the Galaxy*, so we begin with a quote from that illustrious text.

> Ford handed the book to Arthur.<br/><br/> "What is it?" asked Arthur. <br/><br/> "The Hitchhiker's Guide to the Galaxy. It's a sort of electronic book. It tells you everything you need to know about anything. That's its job." <br/><br/>Arthur turned it over nervously in his hands. "I like the cover," he said. "Don't Panic. It's the first helpful or intelligible thing anybody's said to me all day."

While not even the entirety of the Internet can promise to tell you **everything** you need to know about technology, we do believe that the slogan "Don't Panic" is a useful one.  Technology can be baffling, inconsistent, and frustrating, and lead its users to experience rage or fear or feel incompetent.  If you feel this way, you're not alone, and there are practical steps to troubleshooting we'll share with you in this module to help you feel more empowered.  Try not to panic!

The "steps" we're describing in this module don't necessarily take place in the order we describe -- often there's a flow from one method to another and back again as you get closer and closer to understanding, describing, and solving your problem.  This module also is not exhaustive -- you may have tips, ideas, and methods we don't describe here. Everyone's debugging process looks a little bit different, and that's perfectly okay! 

<div class = "important">
One thing that tends to intimidate people is the dreaded **error message**.  Error messages can seem cryptic, but we encourage you to read them aloud if possible.  Reading aloud makes it less likely that you'll skim over important, useful, and recognizably helpful information.  Yes, you can certainly search for error message text in your favorite web browser, but you might surprise yourself with your debugging prowess if you slow down and read your error messages aloud.  At the very least, reading it out loud might help you identify _which parts of the error code_ to search, as the messages can contain some generic text mixed with elements that are very specific to your code or data.
</div>


### Describing the Problem

Consider the way you would describe a car problem to a professional.  You'd include details like:

* What sounds the car is making
* If any lights on the dashboard are lit
* Whether the problem is made better or worse by weather or driving conditions
* When the problem started and if anything noteworthy happened at that time (like an oil change or a flooded street)

If you're a clinician, you may have guided patients into more detailed descriptions of abdominal pain, asking questions like:

* Is it made better, worse, or no change when you eat?  When you lie down?
* Is the pain dull, sharp, constant, throbbing, severe, mild?
* Does it happen at a certain time of day?  Week?  Month?
* When did you notice it begin?  How long has it been going on?
* Is it accompanied by tenderness? Rash? Vomiting? Change in bowel habits?

In both of these examples, describing a problem more thoroughly is the key to narrowing down the possible source of the issue. The same idea holds true when encountering a technical snag. When something isn't working as expected, a good place to start is by documenting (yes, do actually type it out) details like:

* What did you try to do?  
* What code did you use?
* What did you think / hope would happen?  
* Do you have an example of when it **did** work the way you expected?
* What happened instead?
* Were there any error messages?  What do they say?  
* What did you try already to fix the problem?  

When you're in a hurry, in a panic, or annoyed (at yourself, at your computer, or at the world), it can be very tempting to throw your hands up and give a very vague description like "data import is broken!".  However, that description won't help you pinpoint the cause of your problems, and it will make it very unlikely that people you're asking for help (say in a user group Slack or on a website like Stack Overflow) will go out of their way to help you, either.  While your problem feels very familiar to you, and rehashing it might seem like too much effort, other people reading your request for help aren't familiar with your data, your computer, your customary use of software, or your experience level.

<div class = "important">

Which of these problem descriptions would you rather tackle?  

Option 1:  "I'm so frustrated. No matter what I try to import my data, I can't get it to work! I just keep getting error messages. "

Option 2:  "I'm so frustrated.  I have been trying to load a .csv from my local drive using the `read_csv` function, which I've read is the best way to import .csv data, but I keep getting the error `Error in read_csv("intervention_case_control.csv") : could not find function "read_csv"`.  I know the file is there, and I'm 99% sure it's not a file path issue."

</div>

### Rubber Duck Debugging

Once you've described the problem, even if just to yourself, try explaining it to... a rubber duck!  Yes, you read that correctly.  "Rubber duck debugging" is an old trick used by software developers, and while the traditional object used for this exercise is a rubber duck, you can also use your newborn, a pet, or a sock puppet.  

![""](media/rubber_duck.png)<!-- style = "max-width: 400px;" -->

<figcaption style = "font-size: 0.8em; margin-bottom:1rem;">Image courtesy Steve Webel, https://www.flickr.com/photos/webel/306290032 </figcaption>

The idea is that by describing your problem carefully to something or someone who doesn't know much about coding, you'll unwittingly stumble upon the answer.  We've also experienced this when we've asked a supervisor to "please come look at this code".  As soon as we start explaining the problem, the answer becomes clear (or sometimes, inexplicably, the problem simply disappears, presumably due to the magical qualities of boss proximity, but that's beyond the scope of this module).

Remember that your rubber duck (or sock puppet, etc.) isn't the expert you are, so you'll have to explain **why** you want to do certain things and how various procedures work.  With luck, this cognitive trick of getting back to basics and fully mapping out the logic of each step will be enough to help you realize what made things go wrong.  If not, you can consider additional techniques, like searching for clues online and asking others for help.  Plus, you've described your problem simply, which will help other people understand what you're trying to do and what's going wrong.

## Searching for Clues Online

One thing you might not realize if you're new to coding or version control or other technical fields is that even experts who write software all day often use the Internet for help. Sometimes, people find this surprising! In fact, depending upon your field it may well be that reaching for a search engine to answer a "simple" question would be considered bad form. If you feel as though searching for help is a sign of weakness or inability, we invite you to ask your friendly local neighborhood web developer or data scientist or genomics researcher how well they could do their jobs without a search engine.  Our guess is that they'll explain that while experience has given them a lot of best practices and instincts that make life easier, many of the small implementation details simply aren't something worth memorizing when Google or Bing can handle that instead.

In fact, much of what distinguishes experts from novices is knowing how to search for answers more effectively.  Experts know tech lingo enough to use search terms like "R ternary operator" or "git squash and merge or rebase", and they know which websites and even which authors are trustworthy.  



### The Right Question

Let's start with the right question!

There's a delightful [Twitter thread](https://twitter.com/xkcd/status/1333529967079120896) about asking the wrong question by the inimitable Randall Munroe, of [xkcd](https://xkcd.com) fame, of which we'll share just one small screenshot:

![Learning new things from Google: a search box with the text "what year did tom hanks land on the moon" is followed by a suggested answer of "1970".](media/tom_hanks.png)<!-- style = "border: 1px solid rgb(var(--color-highlight)); max-width: 400px" -->

Luckily, learning to ask the right question using trial and error is a skill you can learn.  

<h3>A Silly (but True) Example </h3>

The author of this module did grad school for the first time in Spain, and had been in Spain for around a year when they went looking for a tool necessary to prepare that evening's meal.  They didn't know the name of the thing and at the time, it was really hard to explain what the thing was to friends and roommates.  But then they remembered that it was often used for shredding carrots for salads.  Since the word "shred" wasn't part of their Spanish vocabulary, they did the best they could and asked, "¿cómo se llama el enemigo de zanahorias?" and used pantomime and sound effects to mimic using a grater to shred carrots finely.  "What do you call the enemy of carrots?"  It was a silly way to describe the use of a grater, but it was effective, and memorable!  (By the way, "grater" in Spanish is "rallador".)

Does this feel familiar? This feeling of awkward inarticulacy can be very typical in learning new technology skills. Does one "github" a file?  Or "git" a file?  Is "markdown" a thing, or an action?  Is it right to say "I will markdown this file."?  Or "I will make a markdown."?  Even once you have a few of the most common words figured out, you might not be sure how they interact with each other. The nice thing is that modern search engines (we'll use Google for our examples, but other search engines are similar) are very good at helping you use the few words you know to provide you with more precise terms.  For example, Googling phrases like "I need to make tiny carrot pieces" or "what thing is sharp and has holes and you can cut carrots with it" can provide surprisingly great suggestions in "Related searches".  By scanning the first page of search results, you can hone your vocabulary and learn, in context, what a "grater" is.

The next time you are trying to solve a coding problem, try using your first two or three searches **just to hone and refine your question and your vocabulary**.  Don't be tempted to click on the first link that might be an answer, but instead, use the titles of the search results, the "Related searches" that are suggested, and other context clues to get a more precise handle on what your use case is called.

<h3>A More Technical Example</h3>

For example, let's say you are new to using SQL and you have to get data out of two tables and combine them.  One table has the patient MRN and some demographic data, and the other table has patient MRN and some diagnosis information.  You want to combine the demographic data and diagnosis data into one set of results, such that you have all the information for a given patient MRN all in one row.  You might try searching for "combine information from two tables", "in SQL how can I get data out of two tables on the same individual", or "unite data from two tables in SQL".  

Go ahead and search on those phrases or your own problem description.  

Before too long, you should have figured out that the special word for that kind of work in SQL is "join".  That means that your next search question might be "how to join in SQL".  By tapping into novel jargon, your results will be much more useful and precise... which hopefully helps us not ask a question like "What year did Tom Hanks land on the moon".

### The Right Source

Learning what sources are trustworthy and useful takes time and experience, and it's often very context specific.  However, there are clues evident in search results that can help you make educated guesses about what might have better quality or utility.  These include things like:

* The number of comments on videos
* Likes / dislikes on blog posts or videos
* Whether a snippet shared on the page of search results seems well written
* If the URL or text seems like an aggregator or keyword miner (https://best-handbags-and-python-queries-and-airfare.biz)
* If it seems that the website will try to sell you something
* The date / recency of the result
* Result ranking (how high up on the page of search results it appears)
* Similarity to your problem

While online privacy is a thorny issue, searching for answers online is one place where **cookies** and  other personalization (such as being logged in with a Google identity) can be very helpful.  Once you've run a few searches, your web search tool of choice (unless you choose strict privacy controls) will realize that you're more interested in "Python" the language than "Python", part of the name of a comedy troupe or "Python", a type of constrictor.

One common place that many people find extremely useful for solving technical problems is a website called [Stack Overflow](https://stackoverflow.com/). Stack Overflow is a crowdsourced Q&A site, where you can either browse questions and answers that others have posted, or create an account and start contributing.

We'll talk about how to contribute good questions to Stack Overflow later in this module, but for now let's consider the anatomy of a Stack Overflow question.  Below, we've searched for the phrase "ggplot black and white", because we need to create a black and white data visualization and we like using the `ggplot2` package in R.  You'll notice that in the list of search results, each one has a descriptive title and a short snippet.  To the left of each search item, there's a bit of information about votes, answers, and views.


![The search provides hundreds of results. On the right of the screen the default sort by option is "Relevance". Next to that is newest, and then a dropdown for additional options labelled "More".](media/stack_overflow.png)<!-- style = "border: 1px solid rgb(var(--color-highlight));"-->

When sourcing an answer from Stack Overflow, look for:

* Votes (people with accounts can "upvote" a useful question and "downvote" a low quality question)
* A title and snippet that seem to describe a problem similar to your own
* A recent date (unless this is a "classic" / basic question)
* At least one "answer", particularly if there's a check mark, indicating that the person who originated the question selected the answer that worked for them
* Tags (which appear below the snippet, in our case including "r", "ggplot2", "colors", and "graphics") that might prove useful


## Crowdsourcing: Asking for Help

One of the nice things about working with code is that there are many people who are willing to take time out of their day to help you, expecting nothing in exchange (except, perhaps, another few reputation points on Stack Overflow).  However, there are also grouchy people online who aren't friendly to people who ask what they consider "bad" questions.  Let's consider how you can get the most out of asking others for help.

First, whom should you ask for help?  The answer is "anyone likely to help you", as long as your question doesn't disclose private data or proprietary information that should be kept secret.  You may have a user group or data literacy or training group in your institution.  You might belong to some affinity groups in your city who use Slack or other apps to communicate about code questions and other topics.  There's always Stack Overflow, too.  Don't be hesitant to ask for help.  Most people enjoy feeling important and respected, and being asked for help often feels good, especially if the question is asked in a way that makes it easy to respond.  

The crafting of a question or problem description is very important, and that's why we addressed it early in this module.  Understanding precisely what step of a multi-step process didn't work as intended, the steps you took to try to resolve the problem, and what you wanted to happen instead are all necessary ingredients for a good problem description.  You will get better at describing problems once you have a bit more experience in understanding what's relevant (e.g. if you have diffuse abdominal pain, it probably doesn't matter that you're left handed, but it might be relevant that you tried a new ceviche and seafood restaurant last night).  Still, try to describe things succinctly but with enough detail to help your potential allies have a head start in solving your problem.

If you decide to create a Stack Overflow (or other similar site) account and start asking your own questions, be aware that a poorly crafted, vague, hostile, or "please do my homework for me" question will quickly receive downvotes and negative comments.  This can be very discouraging.  What is the single most helpful way to avoid receiving negative attention on a crowdsourced Q&A site?  A **reproducible example**.

### Making a Minimal Reproducible Example

A **(minimal) reproducible example** (not everyone includes the word "minimal" and some abbreviate it to **reprex** (pronounced ree-precks)) is a way for another person to re-create the problem you're experiencing in just a few lines they can run on their own computer.  Usually, your data or computing details are something you want to keep secret -- you just want answers about how to do one specific thing to your data.  If you're doing data analysis, you might have hundreds of rows, dozens of columns, and get an error halfway through an eighty-line script.  So, how can you create a reproducible example?

You can start by creating separate data that shares relevant details with your situation.  For example, if you're trying to separate first names and last names by using the space between them, you might want to create a sample data frame or table with three rows and just one column, writing the R, Python, or SQL code needed to create a simple data structure like this:

<!-- data-type = "none" -->

| name |
| --- |
| John Doe |
| Giovanni Ferraro |
| María López-Ayllón|

Then, try breaking the code down into more atomic elements -- this has the added benefit of often increasing your understanding of how different pieces of code work together. Does the first bite sized chunk you run produce the error?  No, not yet?  OK, well, run the next small chunk of code. Figure out which step of the code is causing the problem, and what the data looks like just before you do that step.   

Then you might want to state your desired outcome:

<blockquote class = "lia-quote">

I'd like to separate the `name` column into two, like this:

| first | last|
| --- | --- |
| John | Doe |
| Giovanni  | Ferraro |
| María | López-Ayllón |

</blockquote>

You'll also want to include important details like what language you're working in, what you've already tried and why it wasn't good enough, and if there are any constraints that are important to mention.  It's important that you share an example that's succinct, clear, will demonstrate the problem, and doesn't require a lot of work to recreate.  

To go back to our car analogy, would you rather help a friend figure out what's wrong with their car if they said "OK, let it get warm for about five minutes, then put it in reverse and you'll hear it squeal" or "Well, I think I have seen this on long trips, so maybe drive it for an hour or two, and then try a few things like parallel parking or backing into a garage and I think you might hear the sound"?

Creating a minimal reproducible example means that you might have to do a significant amount of work to figure out how exactly to reproduce the problem, but that effort is incredibly useful -- to you, and to your online helpers. In fact, the process of creating a reprex may end up leading you to your own solution, all without ever getting to the stage of posting it. And if it doesn't (because that won't always happen) you're perfectly set up to get help from others! 

Stack Overflow itself offers a great post called [How to create a Minimal, Reproducible Example](https://stackoverflow.com/help/minimal-reproducible-example) and we strongly urge you to read this post before asking your first question.  If you're not sure how in your circumstance to create such an example, say so!  You might, for example, post using text like this:

> I'm not sure how to create a minimal, reproducible example for this because it only happens on my Windows computer, and I can't get it to reproduce on my work Macbook.  But what I'm seeing is....

This kind of demonstration that you're trying to abide by the culture of online Q&A will make it more likely that someone will reach out to ask clarifying questions or offer suggestions.  

## Quiz

Which of the below is a motive for using a minimal reproducible example?

[[X]] People will be less mean to you on the Internet
[[X]] The added effort of creating the problem in a simple context might help you solve it
[[X]] It shows respect for other people's time
[[X]] It can help other people with similar problems find your question and any helpful answers
[[?]] There are several correct answers!
***********

<div class = "answer">

You guessed it, **all** of these are great reasons to use a minimal reproducible example when you're describing a code or other technical problem!

</div>

*******

In Stack Overflow, what does a check mark next to an answer indicate?

[[ ]] The answer was provided by a known expert in the field
[[ ]] The answer was judged correct by the majority of voters
[[X]] The answer was judged correct by the original question asker
[[ ]] The question itself is considered high quality
***********

<div class = "answer">

A check mark next to an answer in Stack Overflow indicates that the original question asker judged the answer provided to be what best solved their problem.  Sometimes there are several answers that might be useful to look through, and even several correct answers, but there's only one answer that the original question asker indicates is the "winner".

</div>

*******

Which of these is **not** a strategy for describing a problem more precisely?

[[ ]] Talking to an inanimate object to explain the problem
[[ ]] Using a search engine like Google to learn the correct jargon to use in a problem description
[[ ]] Creating a minimal, reproducible example
[[X]] Panicking
***********

<div class = "answer">

Don't panic!  Yes, talk to your rubber duck about your frustrations and why you think your code should work.  Yes, use a search engine to learn what that pattern of data or use case is called in the coding community.  Yes, by all means create a minimal, reproducible example.  But don't let your frustration, impostor syndrome, or fear get in the way of systematically breaking down your problem into smaller, more easily digestible and describable parts.  You can do this!

</div>

*******

## Additional Resources

Twitter can be very reassuring, and [this post by Ryan Cavanaugh](https://twitter.com/searyanc/status/1512549675835944962) is one example.  Just check out the number of retweets!

Another example, which is superficially related to the R language but will elicit a chuckle from anyone who's written code, is a [bingo card](https://twitter.com/cogscimom/status/1354508785365078016) from Dr. Ji Y. Son.

Matthew Rocklin has some great Python examples (but they're understandable even if you don't know Python) in his [Craft Minimal Bug Reports](https://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports).


## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22How+to+Troubleshoot%22)!

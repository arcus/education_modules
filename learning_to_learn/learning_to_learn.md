<!--

author:   Rose Franzen
email:    franzenr@chop.edu
version: 1.0.3
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Learning to Learn Data Science
comment:  Discover how learning data science is different than learning other subjects.
long_description: The process of learning data science can be different from that of learning other subjects. This module goes over some of those differences and provides advice for navigating this potentially unfamiliar territory.
estimated_time: 20 minutes

@learning_objectives  

After completion of this module, learners will be able to:

- recognize ways in which learning data science and coding may be different than other educational experiences
- identify ways to extend their learning beyond module content
- recognize how to understand when to ask for help

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css
script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Learning How to Learn Data Science
<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

This module is appropriate for anyone who is interested in continuing to learn data science, regardless of their level of expertise. While some of the content may be written in a way that assumes the learner is totally unfamiliar with the field, it is written with the goal of being useful for all, whether it's as a first exposure to these ideas or a nice refresher.

**Learning Objectives**

@learning_objectives

</div>
## What's so special about data science?
You might be wondering why we've even bothered to make content on how to learn data science. After all, by the very virtue of you being here, you are clearly motivated to learn and have a history of successful acquisition of knowledge.

Data science has its own quirks related to the best ways to process and learn new knowledge. This module addresses setting expectations and makes explicit some of the "hidden" curriculum for learning a new technical topic. Depending on the other subjects you've studied and your own level of knowledge in data science, it could be that you already know everything we're about to say. Regardless, it seems important to us to be upfront about knowledge acquisition in data science.  Perhaps another way to frame this module is "Things We Wish We Knew When We Started Learning Data Science".

It is our hope that this content will allow you to plan your approach to learning in a way that maximizes the value you get out of however much time you are able to dedicate to learning.

## To Memorize or Not to Memorize

While some subjects rely on a large foundation of memorization, that's not the case with data science. Unlike the average grade school math teacher, we don't think it's important for you to memorize every possible function and formula. The real-life equivalence of an infinite formula sheet (also known as the internet) is at your disposal at all times. So long as you know how to efficiently search for the right function (something we'll cover in another module, and a skill you will no doubt gain the more code you write), there's no need to be concerned with trying to keep all of this information in your mind.
While you will eventually build a large internal knowledge base of various functions, features, and elements, it will build up naturally as a result of writing many lines of code, rather than by flipping through flashcards.

## No Right Answers
While within the context of the educational modules you complete there will be questions to check your understanding, outside of the educational context, there are no "right" answers in coding.

As you go through our content, you'll be learning functions and features within the context of certain example data or circumstances that we're providing. Outside of that, however, there will be many ways those functions can be utilized that we won't describe (or in some instances, may not have ever even considered!)

This also works in the opposite direction -- our content will often show a specific way to solve a problem as a means of demonstration of a new technique. It is almost a guarantee that there will be many other ways to solve that problem, perhaps even some you already know! That's part of the beauty of coding -- continue to hold on to that sense of flexibility, infinite possibility, and wonder.


That being said, within the field, there can be strongly held opinions on which approach is the "best". This can also lend itself rather unfortunately to a sense of [gatekeeping](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/reproducibility/reproducibility.md#2).

For example, [Stack Overflow](https://stackoverflow.com/) (an online forum that is useful for finding answers to coding problems) is notorious for having some bordering-on-hostile answers to questions, particularly on much older questions.
This can be discouraging to encounter.  Try to shift your focus on what you can learn from their suggestion, and make the decision for yourself which approach makes the most sense for you.
Above all else, remember that you're no less of a programmer for approaching things in a different way.

## Asking Questions and Finding Answers
Ask a lot of questions, especially "Why?", "How?", and "How else?"
Ask these questions not just of your instructors or peers, but of yourself, and especially of your code!

- "**Why** does this function only work if I give it a number as input, but not a string of characters?"
- "**How** does this line of code know whether my data is in [long or wide format](https://www.statology.org/long-vs-wide-data/)?"
- "**How else** could this function be useful?"

Asking questions is an important step even when things are already working as expected.

One of the best ways to answer your own questions is to experiment with your code. Take a single line of code that you already understand, and try manipulating it, one element at a time. What happens if you change the data type of one of the variables you're using? Does it still work? Does it give an error? What happens when you add an extra comma to the end of the line? Iterative manipulation of code like this can really contribute to your growing mental models of how your code is accomplishing what it is.

## Practice, Practice, Practice
Because coding is such a hands-on subject, one of the biggest keys to success is simply practice. The more opportunities you can find to play around with some code, the better situated you'll be. While we will give you exercises and activities throughout your modules, it is likely that those alone will not be sufficient to solidify your practice. We encourage you to integrate what you've learned into your workflows wherever possible, rather than waiting until you feel like you've mastered everything you need to transform your entire data analysis process.
E.g., even if you're not ready to do your entire analysis in code, practice the data transformation steps you've learned by doing your work in R instead of Excel -- even if there's more work you'll need to do in Excel after the fact.


As much as possible, as you become comfortable it's especially valuable to stretch the limits of your understanding by attempting to apply the methods you've learned to a variety of situations, especially those the modules may not have explicitly covered. This is because at its core, coding is problem solving. The more opportunities you have to grapple with code, the stronger your understanding of essential elements will become.

By attempting to apply new knowledge to solve problems you may not have explicitly seen that knowledge applied to, you will learn about the edge cases of the capabilities you're testing, and through that will gain a deeper understanding of how exactly the pieces of code are working together. You're also much less likely to forget those lessons, since you have something concrete to attach them to.


Don't worry if this sounds like a tall order right now -- this can look like a lot of different things, and it may take time to build up to.



## Be prepared to fail ... and fail again!
Coding and data science are all about failure. In fact, it could be said that coding is just a process of failing, working really hard to figure out what's causing the error or failure, finally figuring it out, and then proceeding for a bit until you fail again.


Recognizing the inevitability of failure can be stressful. For many of us, failure is something to be avoided at all costs, and it's not hard to understand why when you consider our achievement-prioritizing society. Within academia specifically, due to the incentives and structures within our academic and publishing institutions, failure can weigh heavily.  A failed experiment may spell trouble for getting a grant renewal or another peer-reviewed publication. Depending on your background, failure can be especially terrifying -- if you do or have ever done any sort of clinical work, failure can often be related quite directly with some sort of harm to a patient. In those circumstances, where the consequences of failure are so severe, it makes a lot of sense to be highly failure averse. Within the realm of writing code, however, failure is **embraced**, or at the very least accepted as an integral part of the process.



It's not unusual to find this process particularly frustrating at first. Despite the fact that failure will continue to be a part of every data scientist's workflow, be reassured that it doesn't always feel as hard as it might at first.
Over time, you will get better at understanding error messages, troubleshooting, and debugging.

You may still Google things just as frequently as you do now, but you'll have better grasp of the best keywords to bring the right information to the top, and you'll have improved models for sifting through the results to find what will work.

## Balancing Problem Solving and Asking for Help
As mentioned above, a lot of your learning is likely to be derived from hands-on code writing, troubleshooting, and problem solving.

However, although self-teaching is a useful skill, it’s equally crucial to be prepared to recognize when you’ve spent too much time trying to trouble shoot an error on your own.

Unfortunately, because everyone has a different tolerance for ambiguity and frustration, there are no good hard and fast rules on when to ask for help rather than continuing to power through on your own.

However, there are a few things that can be useful to keep in mind as heuristics:

- Are you at the end of your rope? If the choice is between giving up entirely and reaching out for help -- **always** reach out for help!
- Are you out of ideas? If you've exhausted everything you can think of, and you aren't sure what else you could try -- you likely should reach out for help!
- How much value are you getting from troubleshooting on your own? If you still haven't solved the problem but feel as though you're learning new things along the way, it might be a good idea to keep trying. On the other hand, finding yourself getting increasingly confused is a good sign it's time to call for backup!
- When in doubt, reach out!

## Quiz:

True or False: "Real" data scientists and coders rarely look things up on Google.

[( )] True
[(X)] False
***
<div class = "answer">

This is false! While the type of things that experts look up are likely quite different from the Google search history of novices, even experienced programmers use Google on a daily basis to help them.

</div>
***

What are some ways in which learning data science and coding may be different than other subjects? (Select all that apply)


[[X]] There's rarely just one right answer
[[ ]] Rote memorization is one of the keys to success
[[X]] Failure is encouraged and necessary
[[ ]] Most progress comes from reading the lessons.
[[?]] Hint: Remember to select ALL of the correct choices.
***
<div class = "answer">

It is almost never going to be the case that there is just one right answer when it comes to how to solve a problem in code. Additionally, failure is an essential part of the process.

However, rote memorization of functions is not a primary focus of data science education, and most progress is likely to come from repeated practice and application of the skills taught in lessons.

</div>
***


True or False: If you hope to change your current data analytics pipeline, it's best to iteratively integrate what you've learned, rather than to wait until you have all the skills necessary to update the entire process.

[(X)] True
[( )] False
***
<div class = "answer">

This is true! Instead of letting perfect be the enemy of good, taking small steps to change your process is not only going to make the task much more manageable, it will also allow you to engage in the crucial practice needed to further hone your skills.

</div>
***

Finish the line:
In terms of deciding when to seek out assistance to help you figure something out, when in doubt...

[[reach out]]
[[?]] Hint: use all lower case letters and no punctuation. If you're still stuck, see the last point in [Balancing Problem Solving and Asking for Help](#Balancing-Problem-Solving-and-Asking-for-Help)

## Additional Resources

Check out this wonderful (and entertaining) [cartoon guide to bioinformatics](https://www.nature.com/articles/d41586-021-01485-y) by a biologist who later learned to code

For more inspiration on embracing failure, check out [Fail Fest](https://failfest.us/) and this great [blog post from a 2014 Fail Fest attendee](https://www.codeguru.com/blog/learning-from-failure/).


## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Learning+How+to+Learn+Data+Science%22&version=1.0.3)!

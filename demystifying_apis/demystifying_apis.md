<!--
author:   Joy Payton
email:    paytonk@chop.edu
version:  1.0.0
current_version_description: Initial version
module_type: standard
docs_version: 3.0.0
language: en
narrator: US English Female
mode: Textbook
title: Demystifying Application Programming Interfaces (APIs) 
comment:  Understand what an application programming interface (API) is and why APIs are useful!
long_description: An application programming interface (API) can allow you to work more easily with data sources and technical tools.  Learn more about what an API is, how to find out more about your API, and use cases for when using an API makes sense.  It's appropriate for brand new beginners.
estimated_time_in_minutes: 30

@pre_reqs
No particular skills or experience are required for this module.  
@end

@learning_objectives  
After completion of this module, learners will be able to:

- Define the term *application programming interface* (API)
- Explain why APIs can be useful to biomedical researchers
- Explain how to interact with an API

@end

good_first_module: true
coding_required: false

@sets_you_up_for

@end

@depends_on_knowledge_available_in


@end

@version_history 

Previous versions: 

No previous versions.

@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
-->

# Demystifying Application Programming Interfaces (APIs)

@overview

## What is an API?

**API** (you can pronounce it by saying each letter: A - P - I) stands for **Application Programming Interface**.  Let's take each of those words in turn.

An **application** is a computer system -- such as the system that holds the list of New York Times bestsellers, or the REDCap system of electronic research data capture, or the PubMed system of searchable academic articles related to medicine.

**Programming** is the use of special methods -- usually written compute code -- to control what an application does.  When you write Python or R, you're programming.  Some people like to distinguish between "scripting" and "programming", but we think this is a false dichotomy.  

Finally, an **interface** is a way to interact with a system.  The dashboard of your car is an interface, and the menu in your word processing software is an interface.  Interfaces allow you to give instruction to a system, get information from a system, or both.

If we put these together, we can describe an API as a way for people or machines to:
* interact with (that's the **interface** part)
* software (that's the **application** part)
* in a very specific and prescribed way (often, but not always, by **programming**). 

That feels very vague -- what about some examples?  We'll consider some on the next page.

## API Examples 

What kinds of APIs might you, a biomedical researcher, encounter?  Well, let's consider some practical use cases.

* Instead of manually doing a literature review where you copy/paste the results from a hand-typed search result page into a Word document, you might want to use the PubMed API to give you a count or list of results instead, and try plugging different values of year, search terms, or other data elements to quickly measure the effectiveness of your search terms.
* You might use the REDCap API to download today's latest recruitment numbers into a pre-made dashboard to share with your lab and encourage them to step up recruitment efforts in your weekly meeting.
* Perhaps you'd like to study newspaper coverage of a public health topic, and use the New York Times API to give the the counts and references to articles written about your topic of interest, so you can visualize the change over time of public awareness and interest.
* As someone interested in the social determinants of health, you want to use the U.S. Census API to obtain economic data from the American Community Survey about the census tracts in Philadelphia.
* Because you educate the public about infectious disease, you want to get the latest data about the popularity of posts and pages on your website, and analyze that data to see what kinds of articles get the most traction.
* The sensor data you use to study air quality across the Commonwealth require you to use an API to download data and give you historical information you need to understand the risk factors that might explain increased asthma acuity among your patients.
* Because you're building an automated system that your animal models will interact with, you want to use these systems to trigger data being written to REDCap or another data capture system.  That means interacting with an API!

Many systems may have manual ways to interact with them.  For example, in our use cases above, you could just go to PubMed and search, then copy-paste your results, or go to the Census.gov website and find the ACS data to download.  Why, then, create an automated way to work with systems?

## Why Use APIs?

We've written about the "whys" behind API usage as well in our module Using the REDCap API, so we're going to borrow some language from that module.

Two important advantages to using an API are **data freshness** and **reproducibility**.

**Data Freshness**

Let's say you have to run some analysis on data you're collecting in REDCap, and you want to re-run this analysis every couple of weeks to see the latest figures. One way to do that is to manually export data from REDCap to a .csv and save it to a file that you analyze.  REDCap likes to download files with a date stamp as part of the file name, so you have to keep track of various file names and make sure you are analyzing the right data. You may, after all, end up collecting multiple .csvs, each of which has a particular version of the data in REDCap. This can easily become overwhelming and cause confusion or mistakes.

What's a better approach? Reach into the REDCap database directly each time you run your analysis script, so that you know you're using the most up-to-date data.

**Reproducibility**

Another problem with using manually methods to obtain your data (whether that's from REDCap, or the search results page from the New York Times) is that this method requires unscripted, point-and-click manual work. If you were to document this carefully, you'd have to give several steps, like what system to go to or web page to go to, what log in to use (if applicable), which menu item to click or tab to select, any special download settings, how to name a file, and where to put the file. Most of us don't go into this level of detail in our manual workflows, for good reason! It's tiresome, and we know that sometimes things change in the look and feel of a website, so including screenshots and detailed instructions about where to look for a link or how to type into a search bar is a lot of work for something that might have slightly different steps next week or next month.

A better approach is to use a script that uses an API call. First of all, it's scripted, which means no manual steps to write up in a Word document or add to a GitHub repo or jot down on a sticky note. Also, the typical API has a standard interface that will change very little. API access may improve over time, adding new features, but it's very infrequent that an API will radically change and remove options, rendering your script unusable. The same half-dozen lines of code you use to access your data will almost always be stable for months or years, and if you do need to change it, you're only changing that small chunk of code, instead of a step-by-step document with words and images that describe a manual effort.

## But How Do You Use It?

APIs that you'll be likely to work with -- APIs that are available through the Internet -- are "listening" for requests in the same way the application is "listening" for requests for web pages.  


## What Do You Supply?

Different APIs require different things.

Generally, most well-crafted APIs will accept query parameters that include things like:

What kind of data is being requested (e.g. what fields from a database)
Which data items are being requested (e.g. by an identifier or resource name)
The format requested (e.g. CSV or JSON)
Any key and/or password required (e.g. IBM Watson or other for-pay or freemium APIs need to track how much of their services you’ve used)
A data payload, if data is being uploaded
Search terms, if applicable
Ranges (like date ranges), if applicable
The API will either return the desired data in the desired format to the requesting (client) program, send a return code that means success (in the case, say, of adding data), or provide a descriptive and helpful error message. For an example of how an API works, a good resource is the “API playground” in REDCap. If you own a REDCap database, you can give yourself (or others) API access to both request or alter data, and play with the API by using menus in the browser to see the various options.

png

You’ll get output that shows the payload of the data you’d get back from that request. There’s a helpful section below the menus that shows how various API calls would be rendered in different kinds of code (like R, Python, or PHP).

png

This is how many APIs (like IBM Watson, ProPublica, Twitter) train users in how to use them – they provide a user friendly interface that doesn’t require much or any code up front while you learn them.

Why use APIs? They provide a structured, consistent way to carry out a process so that it can be automated and standardized. An API provides consistency around a process. Imagine two different people doing the exact same data download task using a manual approach. They will most definitely have a different process for doing the task and likely a different result as well. An API defines and requires a specific structure for input and provides a specific structure for the output.



## Additional Resources

## Feedback

@feedback
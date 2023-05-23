<!--

author:   Rose Hartman
email:    hartmanr1@chop.edu
version:  0.0.0
module_type: wrapper
module_template_version: 1.0.0
language: en
narrator: UK English Female

title: Docker 101 Tutorial

comment:  This module introduces the popular Docker 101 tutorial, a hands-on way to get started using containers.

long_description: This is a longer description, which should be understandable for a lay audience.

estimated_time_in_minutes: 

@prerequisites
You will need some familiarity with the command line, such as being able to change directories and run bash commands that will be supplied for you to copy and paste. You will need to create and edit text files in a text editor like VSCode. 

You'll also need to create an account on [Docker Hub](https://hub.docker.com/) (it's free), if you don't have one already. 
@end

@learning_objectives  
After completion of this module, learners will be able to:

- identify key elements
- create a product
- do a task
- articulate the rationale for something
@end

resource1_name: Docker 101 Tutorial
resource1_description: From the Docker website: "In this self-paced, hands-on tutorial, you will learn how to build images, run containers, use volumes to persist data and mount in source code, and define your application using Docker Compose. You’ll even learn about a few advanced topics, such as networking and image building best practices."
resource1_wellvetted: true
resource1_wellvetted_text:  The Docker 101 tutorial is an [open source project](https://github.com/docker/getting-started), so it has many authors, but it is sponsored and hosted by Docker Inc, the company that produces the docker software. The open source nature of the tutorial also helps ensure that any errors or problems can be caught and addressed quickly.
resource1_maintained: true
resource1_maintained_text: This tutorial is maintained by Docker Inc, so we expect that it will remain up to date whenever changes are implemented in docker.
resource1_stablesupport: true
resource1_stablesupport_text: This is hosted on the Docker website, and it is a popular and widely-shared tutorial. We expect it will continue to be available for the foreseeable future.
resource1_a11y_issues: No known issues with accessibility, but we may have missed something. If you encounter an issue, please [let us know](#feedback)!


@module_structure
1. Read [Docker for Scientists](#docker-for-scientists) to help contextualize the tutorial for research applications.
2. Do the Docker 101 tutorial.
3. Return to this module to complete the [Quiz](#quiz) to check your understanding and consolidate your knowledge.
@end

import: https://raw.githubusercontent.com/arcus/education_modules/templates_update/_module_templates/macros.md
import: https://raw.githubusercontent.com/arcus/education_modules/templates_update/_module_templates/macros_wrapper.md
-->

# Module Title

@overview

## Lesson Preparation

@lesson_prep_wrapper

@print_resource1

## Docker for Scientists

The tutorial we link to in the next section is an excellent practical introduction to using containers, but it's written with a software developer audience in mind, rather than people who might want to use containers for their research. 

As you work through the tutorial, you'll open and edit javascript files for a simple app (Don't worry! You don't need to know any javascript at all to be able to to the tutorial.).
The use cases you'll work through include sharing the app with other developers

## Docker 101 Tutorial

Now it's time to open the Docker 101 tutorial in a new tab!
We recommend you keep this module open in another window so it's easy for you to return. 

<div class = "external-resource">
<b style="color: rgb(var(--color-highlight));">External Content</b><br>

Complete the [Docker 101 tutorial](https://www.docker.com/101-tutorial/), which can be done either on your computer or in the cloud. 

**Work through the whole tutorial, then return here to finish this module.**

</div>

Note that you'll need to 

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

**Does your first container fail in the `Our Application` section?**

If you get an error message like `ERROR [2/5] RUN apk add --no-cache python g++ make` when you try to run the `docker build` command to create the container, you may be experiencing a known issue with that line. 
If so, try deleting that line from your Dockerfile (it should be the second line in the file), save the file, and then run the `docker build` command again.

See [this post on stackoverflow](https://stackoverflow.com/questions/71200635/can-i-remove-run-apk-add-no-cache-python2-g-make-from-my-dockerfile) for some additional context.

</div>

Other tips:

- To see all the docker images you've built on your computer use `docker image ls`.
- To see all docker containers currently running use `docker ps`.

## Quiz

Which of the following are part of the container image? Select all that apply.

[[X]] The system of files and directories
[[X]] Environment variables
[[X]] Dependencies
[[X]] Configuration
[[X]] Scripts
***
<div class = "answer">

Everything needed to run your code is part of the container image! That includes the directory system itself, all the files (scripts, data, etc.) needed, any dependencies, things like environment variables, configuration files, and metadata. 

</div>
***

What is the correct file extension for a Dockerfile?

[( )] .txt
[( )] .sh
[( )] .dkr
[(X)] It should not have a file extension
***
<div class = "answer">

`Dockerfile` should have no extension. Some text editors will automatically add an extension like `.txt`, so it's important to check that the file has no extension or it won't work to create the container image. 

</div>
***

True or False: A Dockerfile is a text description of the purpose and structure of a container.

[( )] True
[(X)] False
***
<div class = "answer">

The Dockerfile is a set of instructions for generating a container image. You can think of it like a recipe: It tells the computer what ingredients to use and how to combine them to create the container.

A text description about the project sounds more like a [README file](https://www.makeareadme.com/) --- a great thing to include in your project, just not in your Dockerfile. 

Note that you can (and should!) include comments in your Dockerfile describing what it does and why. This makes your Dockerfile much more useful to anyone trying to replicate your work, including future you looking back at your old code. 

</div>
***

True or False: The command to create a container image is `docker run`.

[( )] True
[(X)] False
***
<div class = "answer">

The command `docker run` starts a container that you've already built. 
Use `docker build` to create a container image.

</div>
***

Once you've built a docker image, what is the easiest way to share it?

[( )] Send the Dockerfile via email
[(X)] Share the image via an online repository
[( )] Either of the above will work
***
<div class = "answer">

The best way to share a container image is with the [Docker Hub](https://hub.docker.com/) repository. For a review, see the "Sharing our App" section of the tutorial.

Note that sending just the Dockerfile to someone isn't enough for them to be able to build the container image, so that won't work. 

</div>
***



If you update your code in a container you're already running, which of the following do you have to do to for the changes to be implemented? Select all that apply.

[[X]] Stop and remove the current container
[[X]] Re-run the `docker build` command
[[X]] Re-run the `docker run` command
***
<div class = "answer">

In the section `Updating Our App`, the tutorial uses all three of the above steps to implement a change in the code. 

</div>
***

## Adding Containers to your Research Workflow

So now that you have an idea of how to use docker, how should you apply that in your research? 


>The differences between a helpful, stable Dockerfile and one that is misleading, prone to failure, and full of potential obstacles are not obvious, especially for researchers who do not have extensive software development experience or formal training. By committing to this article’s rules, one can ensure that their workflows are reproducible and reusable, that computing environments are understandable by others, and that researchers have the opportunity to collaborate effectively.

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

**Thinking about security**

Anyone can write and publish docker containers, so it is possible that someone could intentionally use a container to spread malware or for other malicious purposes (although we don't know of any documented cases of that actually happening within research communities).
A more common problem is that docker containers may not be updated after they're published, which means some use old versions of software and operating systems and may be missing important security patches. 

Either way, it's important to carefully evaluate any docker container you're thinking of using. 
In particular, look for [Docker Official Images](https://docs.docker.com/docker-hub/official_images/), which are kept up to date and are very unlikely to have vulnerabilities. 

</div>


## Additional Resources

[An Introduction to Rocker: Docker Containers for R](https://journal.r-project.org/archive/2017/RJ-2017-065/RJ-2017-065.pdf) by Carl Boettiger and Dirk Eddelbuettel


## Feedback

@feedback

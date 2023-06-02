<!--

author:   Rose Hartman
email:    hartmanr1@chop.edu
version:  1.0.0
current_version_description: Initial version
module_type: wrapper
docs_version: 1.0.0
language: en
narrator: UK English Female
mode: Textbook

title: Getting Started with Docker for Research

comment: This tutorial combines a hands-on interactive Docker tutorial published by Docker Inc with an academic article outlining best practices for using Docker for research. 

long_description: If you've been curious about how to use Docker for your research, this module is a great place to start. The Docker 101 tutorial is a popular, hands-on approach to learning Docker that will get you using containers right away, so you can learn by doing. To help you bridge the gap between basic Docker use and best practices for using Docker in research, we also link to an article outlining 10 rules to help you create great containers for research, and lists of ready-to-use Docker images for a variety of analysis workflows. This module includes running and editing commands in the terminal, so you'll need some basic familiarity with bash, but it is otherwise appropriate for beginners. No prior experience with Docker or containers is assumed. 

estimated_time_in_minutes: 60

@pre_reqs
This module assumes no prior experience with containers, and no particular coding other than some familiarity with the command line, such as being able to change directories and run bash commands that will be supplied for you to copy and paste. You will need to create and edit text files in a text editor like VSCode. 

You'll also need to create an account on [Docker Hub](https://hub.docker.com/) (it's free), if you don't have one already, and you'll need to be able to install the Docker Desktop software on your machine (also free). 
@end

@learning_objectives  
After completion of this module, learners will be able to:

- Use the command line to create and run a container from a Dockerfile
- Share containers 
- Understand both technical requirements and best practices for writing Dockerfiles for use in research
@end

resource1_name: Docker 101 Tutorial
resource1_description: From the Docker website: "In this self-paced, hands-on tutorial, you will learn how to build images, run containers, use volumes to persist data and mount in source code, and define your application using Docker Compose. You’ll even learn about a few advanced topics, such as networking and image building best practices."
resource1_wellvetted: true
resource1_wellvetted_text:  The Docker 101 tutorial is an <a href="https://github.com/docker/getting-started">open source project</a>, so it has many authors, but it is sponsored and hosted by Docker Inc, the company that produces the Docker software. The open source nature of the tutorial also helps ensure that any errors or problems can be caught and addressed quickly.

resource1_maintained: true
resource1_maintained_text: This tutorial is maintained by Docker Inc, so we expect that it will remain up to date whenever changes are implemented in Docker.
resource1_stablesupport: true
resource1_stablesupport_text: This is hosted on the Docker website, and it is a popular and widely-shared tutorial. We expect it will continue to be available for the foreseeable future.
resource1_a11y_issues: No known issues with accessibility, but we may have missed something. If you encounter an issue, please [let us know](#feedback)!

resource2_name: Ten simple rules for writing Dockerfiles for reproducible data science
resource2_description: From the article: "The differences between a helpful, stable Dockerfile and one that is misleading, prone to failure, and full of potential obstacles are not obvious, especially for researchers who do not have extensive software development experience or formal training. By committing to this article’s rules, one can ensure that their workflows are reproducible and reusable, that computing environments are understandable by others, and that researchers have the opportunity to collaborate effectively."
resource2_wellvetted: true
resource2_wellvetted_text: This article was written by expert authors and published in PLOS Computational Biology, a peer reviewed scientific journal (you can read about their <a href="https://journals.plos.org/ploscompbiol/s/editorial-and-peer-review-process">editorial and peer review process</a> on their website). 
resource2_maintained: true
resource2_maintained_text: PLOS Computational Biology links any corrections, expressions of concern, or retractions to the affected article's PLOS web page, so any important updates should be available there (for more details read <a href="https://journals.plos.org/ploscompbiol/s/corrections-expressions-of-concern-and-retractions">PLOS's policy on posting corrections</a>).
resource2_stablesupport: true
resource2_stablesupport_text: This article has an assigned DOI (digital identifier of an object), which helps to ensure it will continue to be available (read more <a href="https://www.doi.org/the-identifier/what-is-a-doi/">about DOIs at doi.org</a>). 
resource2_a11y_issues: No known issues with accessibility, but we may have missed something. If you encounter an issue, please [let us know](#feedback)!

@module_structure
1. Do the first half of the "Docker 101" tutorial (on the Docker website).
2. Return to this module to complete the "Docker 101 Quiz" to check your understanding and consolidate your knowledge.
3. Read the article "Ten simple rules for writing Dockerfiles for reproducible data science" by Nüst et al. 2020 (on plos.org).
4. Return to this module for the "Docker for Research Quiz", and for the final sections of the module.
@end

good_first_module: false
coding_required: true
coding_level: intermediate
coding_language: bash

@sets_you_up_for

@end

@depends_on_knowledge_available_in
- demystifying_containers
@end

@version_history
No previous versions.
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_wrapper.md
-->

# Getting Started with Docker for Research

@overview

## Lesson Preparation

@lesson_prep_wrapper

@print_resource1

@print_resource2

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

This is a hands-on module, and it jumps right into how to use Docker without much preamble. 

If you'd prefer a more high-level overview of what containers are and when they're useful, check out our module on [Demystifying Containers](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_containers/demystifying_containers.md).

</div>

## Docker 101 Tutorial

The tutorial we link to in this section is an excellent practical introduction to using containers, but it's written with a software developer audience in mind, rather than people who might want to use containers for their research. 

As you work through the tutorial, you'll open and edit javascript files for a simple app. (Don't worry! You don't need to know any javascript at all to be able to to the tutorial.)
The tutorial sets you up to build a container that, when run, starts the app. 

A more common application in research might be a container that loads required libraries in Python and does the first stage of data preprocessing on startup. 
Or a container that takes a set of RMarkdown files and images and compiles them into a pdf version of the article you're drafting. 
Or a container that trains a machine learning model on a provided dataset. 

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

As you consider the tutorial, imagine the kinds of coding projects you typically work on --- whatever those are --- rather than the example code they provide. 

</div>

### Before you Start

To do the Docker 101 tutorial, you'll need a couple things set up: 

- Create an account (it's free) at Docker Hub ([Docker Hub signup page](https://hub.docker.com/signup/)).
- Install [Docker Desktop](https://docs.docker.com/desktop/) on your computer ([installation instructions for Windows](https://docs.docker.com/desktop/install/windows-install/), [installation instructions for Mac](https://docs.docker.com/desktop/install/mac-install/), and [installation instructions for Linux](https://docs.docker.com/desktop/install/linux-install/)).

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

To check that you have successfully installed Docker on your computer, open the command line and run the following: 

```
docker run hello-world
```

You should see a message that starts with "Hello from Docker!"

</div>

### Work through the first half of the Docker 101

Now it's time to open the Docker 101 tutorial!
We recommend you keep this module open in another window or tab so it's easy for you to return. 

<div class = "external-resource">
<b style="color: rgb(var(--color-highlight));">External Content</b><br>

Complete the **first half** of the [Docker 101 tutorial](https://www.docker.com/101-tutorial/), through the section called "Sharing our App". 
You are welcome to continue past that point if you wish, but it focuses on topics that are more relevant for software development and less likely to be of use in a research context.

<br>
<b style="color: rgb(var(--color-highlight));">Work through the first half of the tutorial, then return here to finish this module.</b>
</div>

Some tips you can apply at any time:

- To see all the Docker images you've built on your computer use `docker image ls`.
- To see all Docker containers currently running use `docker ps`.

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

**Does your first container fail in the "Our Application" section?**

If you get an error message like `ERROR [2/5] RUN apk add --no-cache python g++ make` when you try to run the `docker build` command to create the container, you may be experiencing a known issue with that line. 
If so, try deleting that line from your Dockerfile (it should be the second line in the file), save the file, and then run the `docker build` command again.

See [this post on stackoverflow](https://stackoverflow.com/questions/71200635/can-i-remove-run-apk-add-no-cache-python2-g-make-from-my-dockerfile) for some additional context.

</div>

### Quiz: Docker 101

Which of the following are part of the container image? Select all that apply.

[[X]] The system of files and directories
[[X]] Environment variables
[[X]] Dependencies
[[X]] Configuration
[[X]] Scripts
***
<div class = "answer">

Everything needed to run your code is part of the container image! That includes the directory system itself, all the files (scripts, etc.) needed, any dependencies, things like environment variables, configuration files, and metadata. 

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

In the command `docker build -t getting-started .` what does the `-t` flag stand for?

[[tag]]
<script>
  let input = "@input".trim().toLowerCase();
  input == "tag";
</script>
***
<div class = "answer">

It refers to a tag, a custom identifier you can use to refer to this image (instead of relying on the long, random IDs Docker assigns by default). 
The tag in this example is `getting-started`, so if we want to run this container we just built we can use a command like `docker run getting-started` and Docker will know we're talking about the image we built and tagged above.

To learn more, see the [Docker handbook section on tags](https://docker-handbook.farhan.dev/image-manipulation-basics#tagging-images).

</div>
***

True or False: The command to create a container image is `docker build`.

[(X)] True
[( )] False
***
<div class = "answer">

Yes, you use `docker build` to create a container image.
The command `docker run` starts a container that you've already built. 

</div>
***

Once you've built a Docker image, what is the easiest way to share it?

[( )] Send the Dockerfile via email
[(X)] Share the image via an online repository
[( )] Either of the above will work
***
<div class = "answer">

The best way to share a container image is with the [Docker Hub](https://hub.docker.com/) repository. For a review, see the "Sharing our App" section of the tutorial.

Note that sending just the Dockerfile to someone isn't enough for them to be able to build the container image (just as sending a recipe to someone won't let them cook the dish unless you also send the ingredients), so that won't work. 

</div>
***

## Using Docker in Research

Most of the tutorials and explanations you'll find online about Docker (including the Docker 101 tutorial you just worked on) focus on its use in software development. 
Importantly, most of the example Dockerfiles you'll find online are also written by and for developers. 
As someone new to Docker (and even for experienced users!), being able to copy existing Dockerfiles is an important time saver.
Although you might be able to get these images to work for your research needs, there are a lot of special considerations that come up when you're using containers for reproducible research rather than software development. 

**So what do you need to keep in mind as you think about how to use Docker in your research?** 

One big difference is the value placed on **transparency** and **interpretability** in the research community. 
A good, reproducible container for a research project should be not only functional, but easy for others to understand. 
Because of that, you should think of your Dockerfile as not just a set of instructions but an important form of communication.

This article provides concrete guidance on how to set up your containers for use in research. 

<div class = "external-resource">
<b style="color: rgb(var(--color-highlight));">External Content</b><br>

Next, read [Ten simple rules for writing Dockerfiles for reproducible data science](https://doi.org/10.1371/journal.pcbi.1008316) by Nüst et al. (2020). 

<br>
<b style="color: rgb(var(--color-highlight));">Read the whole article, then return here to finish this module.</b>
</div>

### Quiz: Docker for Research

True or False: The authors recommend including your dataset in the container, to make your analysis fully reproducible.

[( )] True
[(X)] False
***
<div class = "answer">

They recommend storing datafiles outside of the container and using bind mounts to attach the data just when you run the container, rather than building it into the image. 
See [Rule 7: Mount datasets at run time](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008316#sec020). 

For more guidance on using bind mounts, see the [Docker documentation on bind mounts](https://docs.docker.com/storage/bind-mounts/).

</div>
***

Which of the following would the authors say is more important?

[(X)] Making your Dockerfile as explicit as possible, so the layers in the image are easier to see
[( )] Making your Dockerfile as efficient as posisble, so the image is smaller and more portable
***
<div class = "answer">

See [Rule 3: Format for clarity](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008316#sec009). 
In particular:

> In general, if your container is mostly software dependencies, you should not need to worry about image size because (a) your data is likely to have much larger storage requirements; and (b) transparency and inspectability outweigh storage concerns in data science. 

</div>
***

What character is used to start a comment line in a Dockerfile?

[[#]]
<script>
  let input = "@input".trim().toLowerCase();
  input == "#";
</script>
***
<div class = "answer">

See [Rule 4: Document within the Dockerfile](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008316#sec010) for examples.

</div>
***

True or False: For a container with complex anlaysis code, the authors recommend writing your Dockerfile so that the whole analysis workflow runs automatically when you start the container.

[( )] True
[(X)] False
***
<div class = "answer">

While they do recommend you set the container up to run the "entrypoint" of the workflow, running the whole workflow automatically might be surprising (and unwelcome) for someone who just wanted to run the container to inspect it. 
See [Rule 8: Make the image one-click runable](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008316#sec021).

For a concrete example, checkout the [demo Dockerfile](https://github.com/nuest/ten-simple-rules-dockerfiles/blob/master/examples/full-demo/Dockerfile) the authors posted on their GitHub repository for this paper. 
As written, the Dockerfile will set up a container with all the software and scripts needed to run the analysis, but it won't execute the analysis yet. 
At the end of the Dockerfile, they provide additional commented-out lines that can be used to optionally also run the preprocessing tasks as part of the `docker build` command. 
And they provide detailed usage instructions for how to run the whole workflow with `docker run`, and then how to extract the data and figures using `docker cp` commands (to learn more about `docker cp` see the [Docker Command Line documentation](https://docs.docker.com/engine/reference/commandline/cp/)). 

</div>
***

True or False: When you run `docker build`, it will execute each line in the Dockerfile in order, starting at the top and working its way down.

[(X)] True
[( )] False
***
<div class = "answer">

Yes, Docker executes instructions in the Dockerfile in the order in which they appear. 

This is valuable to know because Docker also uses [caching](https://en.wikipedia.org/wiki/Cache_%28computing%29) to store the results of executed instructions. 
Then the next time you build the image, it will check each line of the Dockerfile to see if it's changed since the last build, and if there have been no changes it will just use the cached results until it reaches a line that's been edited. 
At that point, it will switch back to executing instead of using the cache and will run all remaining lines in the Dockerfile. 
That means re-running a build when you've only made edits to the end of a Dockerfile will be potentially much faster than if you had made the same edits at the beginning. 

So when you're actively working on developing a container, it's a good idea to arrange the Dockerfile with the lines least likely to change at the top and lines more likely to change at the bottom. 
When you're ready to finalize and share your container, though, it's a good idea to re-order the lines so that the order of the instructions makes sense logically to a human reader.
They provide a suggested order of sections under [Rule 9: Order the instructions](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008316#sec022). 

</div>
***

## Additional Resources

**Curious about the second half of that Docker 101 tutorial?**

We prioritized the first half of the [Docker 101 tutorial](docker-101-tutorial) for this lesson because those are the sections that will be most directly relevant to a typical research workflow. 

There's great content in the remaining sections, though, and you may wish to work through them as well, especially now that you have additional context about how Docker gets used in research after reading Nüst et al. (2020).
The tutorial section on bind mounts ("Using Bind Mounts") may be particularly useful, as it gives you a chance to practice the approach Nüst et al. advocate for in [Rule 7: Mount datasets at runtime](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008316#sec020).

**Here are some other sources you may find helpful:**

[An Introduction to Rocker: Docker Containers for R](https://journal.r-project.org/archive/2017/RJ-2017-065/RJ-2017-065.pdf) by Boettiger and Eddelbuettel (2017).

For an overview using containers with high performance computing (HPC) centers, see [Singularity: Scientific containers for mobility of compute](https://doi.org/10.1371/journal.pone.0177459) by Kurtzer, Sochat, and Bauer (2017).

[Docker 101 for Reproducible Science](https://kordinglab.com/2022/10/28/LabTeaching-Docker-for-Science.html) by the Kording Lab

[Docker for Reproducible Research](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/reproducible-work/docker/) by Tilburg Science Hub

### Example Docker Images

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

Anyone can write and publish Docker containers, so it is possible that someone could intentionally [use a container to spread malware](https://www.cyber.nj.gov/alerts-advisories/malicious-cryptojacking-images-in-docker-hub) (although we don't know of any documented cases of that actually happening within research communities).
A more common problem is that Docker containers may not be updated after they're published, which means some use old versions of software and operating systems and may be missing important security patches. 

When possible, use [Docker Official Images](https://docs.docker.com/docker-hub/official_images/), which are kept up to date and are very unlikely to have vulnerabilities. 
Note that the official images are built for very general-purpose containers, though, and are often not setup properly for research needs.

A good second-best option is to use images published and maintained by recognized communities --- see our list below.
There's a good chance you'll find an existing image already built with all of the software and dependencies you need for your analysis workflow.

Either way, it's important to carefully evaluate any Docker container you're thinking of using, and never use a container if you don't have access to its Dockerfile. 

</div>

It's a great idea to use already-existing container images when possible. 
It saves you time, and it also makes your work even more reproducible since you're using a container that's already available in your research community rather than writing one from scratch. 

- For R and RStudio, see images maintained by [rocker](https://rocker-project.org/)
- For Jupyter notebook images, see [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html)
- For bioinformatics, see [Bioconductor Docker images](https://bioconductor.org/help/docker/)
- For neuroscience, see [NeuroDebian images](https://hub.docker.com/_/neurodebian)

Do you know of other sets of Docker images we should list here? Please [let us know](#feedback)!

## Feedback

@feedback

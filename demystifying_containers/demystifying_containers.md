<!--

author:   Meredith Lee
email:    leemc@chop.edu
version:  1.0.0
current_version_description: Initial version
module_type: standard
docs_version: 1.0.0
language: en
narrator: UK English Female

title: Demystifying Containers

comment: Containers can be a useful tool for reproducible workflows and collaboration. This module describes what containers are, why a researcher might want to use them, and what your options are for implementation. 

long_description: Writing code in multiple environments can be tricky. Collaboration can be hindered by different language versions, packages, and even operating systems. Developing code in containers can be a solution to this problem. In this module, we'll describe what containers are at a high level and discuss how they might be useful to researchers. 

estimated_time_in_minutes: 20

@pre_reqs
- some familiarity with programming is helpful, but not required
@end

@learning_objectives  
After completion of this module, learners will be able to:

- understand when it might be useful to use containers for development
- describe the basic concept of containerization
- identify several containerization implementations
@end

good_first_module: false

sets_you_up_for: docker_101

depends_on_knowledge_available_in:


import: https://raw.githubusercontent.com/arcus/education_modules/templates_update/_module_templates/macros.md
-->

# Demystifying Containers

@overview

## The purpose of containerization

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

This module is a high-level discussion of what containers are and why you might want to use them. For information on how to get started with containers using Docker, see our module [Getting Started with Docker for Research](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/docker_101/docker_101.md#1).

</div>

If you have spent some time learning programming, you might have come across some terms like "container", "containerization", or "Docker". But what exactly do these terms mean, and why would you want to learn about them?

Essentially, a **container** is a lightweight, portable bundle that contains some code along with the necessary packages, files, and other dependencies that are required to run the code. It can seem like most of the information out there suggests that containers are exclusively used by software developers, but that's not true-- anyone working with code may run into situations in which containerizing that code would be beneficial. 

So why should you consider "containerizing" your code? The real power of developing code in a container is that you can control the environment in which that code will run. Have you ever had the problem where a script or application runs on your own computer, but when a coworker tries to run it, it doesn't work? This could be due to different language or package versions, or even completely different operating systems! This problem can largely be avoided by working in a container. 

Here are a few possible scenarios: 

- You're working on an application that will eventually need to run in an environment that isn't your personal computer (on a server, for example). 

- You and your coworkers regularly collaborate on some code, but you all have different language versions and different packages or libraries installed, making it difficult to send the code files from person to person without making a lot of changes either to the code itself or to your personal system (which could break other code that you're working on).

- You don't collaborate with others, but need to be able to develop and run your code on multiple computers (like a work and a personal computer, for example).

Working in a container can make all of these scenarios much easier to deal with-- it just requires a bit more work up-front. 

### Quiz: Why Containers?

Which of the following are situations that might be improved with containerization? Select all that apply. 

[[ ]] You are collecting some data in an Excel spreadsheet and creating scatter plots of those data.
[[X]] You and your colleagues are working together on an R script to help automate some of your analyses.  
[[X]] You are creating a web application to find the latest journal articles about a topic and display the title and abstract.
***
<div class = "answer">

Collaborating on code and creating web applications are great uses of containers. While collecting and plotting data might be helped by collaboration tools, perhaps in the cloud, it is not a process that would be helped by containerization (no code needs to be run that would be dependent on the computing environment).

</div>
***

## How containers work

![Schematic of a Docker container with six applications labeled A through F. They sit on top of a Docker layer, which sits on top of a a host operating system layer, which in turn sits on top of an Infrastructure layer.](media/docker-containerized-application.png)

Before you build a container, you need a container **image**. An image is essentially the instructions for how to build the container: the code or application that you want in the container, what dependencies should be installed, and what should happen when the container launches. Often, you don't need to start completely from scratch when creating a container image. Many container platforms have **base images** that already have some basic building blocks in place (for example, you might select a Python base image, which will already have the instructions for installing Python and its dependencies); all you need to do then is to add anything special that your container needs. 

Generally, to get started making your container image, you'll need a couple of things:

- A set of instructions for building your container: This is usually the most difficult part of containerization. Usually you will start with a base image, then add anything else required. 
- A list of required packages: This lets the container platform you are using know what libraries to install. This is generally in a separate file from the other instructions, so that it is easy to update. 

After you have created your image, then the container platform you are using can take your instructions and build the container itself, a small computing environment that runs on your computer, but isolated from it, with only the components that it needs and nothing more. It only has access to what you have put inside it via your instructions, and once you're done, you can turn it off and it no longer exists until the next time you need it. You can even attach folders from your computer to the container, if you need to save data before the container stops running. 

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Feeling overwhelmed? Containerization is a topic that can be difficult to wrap your head around at first! Don't worry about the implementation details right now-- this module is just here to give you a little sense of why containers might be useful and what's involved. 

</div>

### Containers vs. virtual machines

![On left side is a schematic of a Docker container with six applications labeled A through F. They sit on top of a Docker layer, which sits on top of a a host operating system layer, which in turn sits on top of an infrastructure layer. On the right side is a schematic of three virtual machines, each with its own guest operating system and application. These three virtual machines sit on top of a hypervisor layer, which sits on top of an infrastructure layer.](media/docker-containerized-and-vm.png)

Some of you might be thinking that containers sound a bit like virtual machines. While virtual machines (or VMs) and containers can serve similar purposes, they aren't exactly the same. 

Virtual machines are divisions of a server into multiple, smaller units. Each machine has its own operating system, and you can divide up hardware elements like CPU and disk space. Virtual machines behave like computers in most respects-- but they're a "virtual" copy.

Containers are much smaller than virtual machines. The element that is "virtualized" is the software, not the hardware underneath (that all comes from your computer). Because of this, it is easier to share and modify container images. 

### Quiz: How containers work

Which of the following describes what a container image is?

[(X)] A set of instructions that describes how a container will be built.
[( )] A small package of software that has everything it needs to run in any environment.
[( )] A digital copy of a computer that runs on a server. 
***
<div class = "answer">

Unlike a container, which is a lightweight bundle of software with all of the code and dependencies required to run in any environment, a container image is the set of instructions that describes how that container will be built. A digital copy of a computer that runs on a server is a virtual machine.  

</div>
***

## Container technology

There are a variety of choices when it comes to containerization technology, but the most popular is **Docker**. [Docker's website](https://www.docker.com/) has many resources and articles to help you get started, as well as a [registry for container images, called DockerHub](https://hub.docker.com/), where you can store your own container images and make use of images already out there. 

However there are other providers that you might come across, that are very similar to Docker but might have subtle differences that may make them better for specific workflows (don't worry about those differences right now though). Here are just a few:

- [Podman](https://podman.io/) is a container service developed by [RedHat](https://www.redhat.com/en). It is often used in conjunction with [Buildah](https://buildah.io/).
- [Linux Daemon, or LXD](https://linuxcontainers.org/)
- [rkt](https://github.com/rkt/rkt), pronounced like "rocket", is a free container engine that is available on GitHub (although the project has ended and is no longer in active development, you can still use it).

You can also run containers on cloud platforms like [Amazon Web Services, or AWS](https://aws.amazon.com/) and [Google Cloud Platform, or GCP](https://cloud.google.com/) using various orchestration (or automation of the operational tasks that are involved in deploying and managing containers) and computing tools. You can check out [containers in AWS](https://aws.amazon.com/containers/services/) and [containers in GCP](https://cloud.google.com/containers) for more information. 

### Quiz: Container technology

True or false: A Docker container is the only kind of container.

[( )] True
[(X)] False 

***
<div class = "answer">

While Docker is the most popular container platform, and has many helpful resources to help you get started, it is not the only option. 

</div>
***

## Additional Resources

- [Another brief description of what a container is from the Docker website](https://www.docker.com/resources/what-container/)
- [Article with more information about containers vs. virtual machines](https://www.atlassian.com/microservices/cloud-computing/containers-vs-vms) 

## Feedback

@feedback


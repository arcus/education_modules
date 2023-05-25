<!--

author:   DART Team
email:    dart@chop.edu
version:  1.1.0
current_version_description: Add current_version_description and version_history metadata
language: en
narrator: UK English Female
title: R Module Macros
comment:  This is placeholder module to save macros used in other modules.

@version_history 

Previous versions: 

- [1.0.0](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/e983922162e6fbf971c03dc96052f68713cc72af/_module_templates/macros_r.md#1): Initial version
@end

@lesson_prep_r

Please do this step now, because we're going to ask you to follow along throughout and try out code as you go.  

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Please read over all the options before you start performing any actions, to make sure you pick the right option for you.

</div>

### Option 1: Work Anonymously in the Cloud

This might work well for you if you either can't or don't want to install R and RStudio on your computer.  The benefit is that you don't have to install anything or have any account set up with an online cloud provider.  This solution is completely anonymous.  However, there are some drawbacks.  One negative is that this option requires a bit of waiting for your environment to come online.  Another is that your changes aren't saved anywhere, and your environment will time out and disappear forever.  

**First**, we need to create a small container in the cloud for you to work in just using your web browser.  **Click "Launch binder" below.**  It might take a while (5 minutes) to create, depending on how recently it was created (when it's being used more, it's quicker!).  We're looking for a faster way to get you off and running in RStudio without downloads and without creating accounts, but for now this is a great, free way for us to get you working with no extra work on your part.

  <a href = "https://mybinder.org/v2/gh/arcus/education_r_environment/main?urlpath=rstudio" target = "_blank"><img src="https://mybinder.org/static/images/badge_logo.svg"></a> **← Click the "launch binder" button!**

<div class = "important" style = "align-items: center; display: flex;">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

<div style = "margin: 1rem; max-width: 45%; float:left;"> If you're the first person to fire up this environment in a while, you might see this loading screen for up to five minutes.  Be patient!</div>
<div style = "margin: 1rem auto; max-width: 45%; float:left;"> ![Binder loading screen.](https://github.com/arcus/education_r_environment/blob/main/media/binder_loading.gif?raw=true)
</div>
</div>

**Then**, once you have access to RStudio and you see something like the image below, you'll need to open the sample data for this course.  In the file area to the lower right, you'll see, among multiple choices, the folder called "@r_file".  That's the code for this module!

<img src="https://github.com/arcus/education_r_environment/blob/main/media/binder_rstudio.png?raw=true" alt="RStudio as shown in the cloud platform Binder." style = "border: 1px solid rgb(var(--color-highlight)); max-width: 800px;">

### Option 2: Use Posit Cloud

Posit (the company formerly known as RStudio) provides a multi-tiered cloud environment for using RStudio.  Unlike option 1 above, this option does require you to have an account with Posit Cloud, their online RStudio server.  The good news is that the base level of Posit Cloud is free!

First, you'll need to [create a (free!) Posit cloud account](https://posit.cloud/plans).  

Then, once you're logged in at [https://posit.cloud](https://posit.cloud), open the "education\_r\_environment" project at [https://posit.cloud/content/5273350](https://posit.cloud/content/5273350).  That will give you a temporary copy so you can run our code, but not make any changes to it.

In the file area to the lower right, you'll see, among multiple choices, the folder called "@r_file".  That's the code for this module!

Click on "Save a Permanent Copy" if you want to save any changes to your version of this code.

<img src="https://github.com/arcus/education_r_environment/blob/main/media/make_copy.png?raw=true" alt="Posit menu bar with 'Make Permanent Copy'." style = "border: 1px solid rgb(var(--color-highlight)); clear:both;">

Now you can not only work in the cloud, but also save your work.

### Option 3: Work on Your Computer

If you have [R](https://www.r-project.org/) and [RStudio](https://www.rstudio.com/products/rstudio/download/#download) installed already on your local computer, you might be interested in simply downloading our sample code to your computer. Here's how.  Note: If you've already done this step in another module, you might have the material for this module already!

* In RStudio, open a new project (File, New Project)
* Select Version Control, then Git
* Drop this link into the "Repository URL": https://github.com/arcus/education_r_environment
* Change the "Project directory name" and "Create project as a subdirectory of" boxes to suit your needs (where will this code be stored on your computer?).
* Click to select the "Open in new session" checkbox
* Click "Create Project"
* In the file area to the lower right, you'll see, among multiple choices, the folder called "@r_file".  That's the code for this module!

**Want to watch this process?  Click on the image below to play an animated gif.  It will continue to loop and you can re-start it by clicking again.**

<div style="display:none">

@gifPreload

</div>

<figure>

  <img src="https://github.com/arcus/education_r_environment/blob/main/media/rstudio_new_project.png?raw=true" height="384" width="512" alt="RStudio can create a new project that gets its contents from a git repository." data-alt="https://github.com/arcus/education_r_environment/blob/main/media/rstudio_new_project.gif?raw=true" style = "border: 1px solid rgb(var(--color-highlight));">

<figcaption style = "font-size: 1em;">

Click on the image to play the demo of the above steps!

</figcaption>

</figure>

If you already completed this work for a previous module, and it's been a while since you downloaded this project to your computer, you may want to get any new and improved files that have been placed there in the meantime:

* Open your project.
* In the Version Control menu, choose "pull branches".  There are two places to do this, as shown below:

<img src="https://github.com/arcus/education_r_environment/blob/main/media/pull_branches.png?raw=true" alt="Git button menu with choices to pull and push branches." style = "border: 1px solid rgb(var(--color-highlight)); max-width:400px;">

<img src="https://github.com/arcus/education_r_environment/blob/main/media/pull_branches_2.png?raw=true" alt="Tools menu with choices to pull and push branches." style = "border: 1px solid rgb(var(--color-highlight)); max-width:400px;">

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

If you're pulling branches after having worked in other R modules, you might have made local changes (for example, when you filled in exercise code) that will be overwritten by pulling the latest version.  If you want to save your changes, consider making a copy of any exercise files and naming them something new.  For example, if you have already worked in the `r_basics_example` exercise files, you might want to save your version of `example_exercises.Rmd` to `my_example_exercises.Rmd`.  That way, you can pull down the latest version of code, overwriting `example_exercises.Rmd` while holding on to your changes in the new file.

</div>

@end
-->

# R Module Macros

@lesson_prep_r

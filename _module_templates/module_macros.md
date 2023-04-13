<!--

author:   DART Team
email:    dart@chop.edu
version:  1.0.0
language: en
narrator: UK English Female
title: Module Macros
comment:  This is placeholder module to save macros used in other modules.

@overview
<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

@prerequisites

**Learning Objectives**

@learning_objectives

</div>
@end

@make_survey_url
<script>
function makeURL(title, version_number, module_type) {
  let url = new URL('https://redcap.chop.edu/surveys');
  url.searchParams.set('s', 'KHTXCXJJ93');
  url.searchParams.set('module_name', title);
  url.searchParams.set('version_number', version_number);
  url.searchParams.set('module_type', module_type);
  return url;
}
var surveyURL = makeURL(@0, @1, @2);

send.html(`<a href="${surveyURL}")">our brief survey</a>`)
</script>
@end

@feedback
In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out @make_survey_url('@title', '@version', '@module_type')!
@end

@lesson_prep_python
@sage

You will have opportunities for hands-on coding as you work your way through this module using interactive python cells.
The interactive python cells are powered by [SageMathCell](https://sagecell.sagemath.org/). For the most part, these will appear with some code already in them, and you can run that code by clicking the **Run python** button. You can also edit the code in these cells and run your own code.


**Give it a try:**
<div class="python">
<lia-keep>
<script type="text/x-sage">
print(7+2)
</script>
</lia-keep>
</div>

Code will not persist from one page to the next, and you can always refresh the page to return the code (and the stored memory of the cell) to its initial state.

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

These cells will compute everything you ask them to, but will only display what you explicitly request using the `print()` command.

</div>

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

**Navigating with arrow keys**

You can navigate the pages of this course using left and right arrow keys. This means that you **cannot** use left and right arrow keys to navigate **within** a code cell.

</div>


@end

@lesson_prep_r

Please do this step now, because we're going to ask you to follow along throughout and try out code as you go.  

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Please read over all the options before you start performing any actions, to make sure you pick the right option for you.

</div>

<h3>Option 1: Work Anonymously in the Cloud</h3>

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

<h3>Option 2: Use Posit Cloud</h3>

Posit (the company formerly known as RStudio) provides a multi-tiered cloud environment for using RStudio.  Unlike option 1 above, this option does require you to have an account with Posit Cloud, their online RStudio server.  The good news is that the base level of Posit Cloud is free!

First, you'll need to [create a (free!) Posit cloud account](https://posit.cloud/plans).  

Then, once you're logged in at [https://posit.cloud](https://posit.cloud), open the "education\_r\_environment" project at [https://posit.cloud/content/5273350](https://posit.cloud/content/5273350).  That will give you a temporary copy so you can run our code, but not make any changes to it.

In the file area to the lower right, you'll see, among multiple choices, the folder called "@r_file".  That's the code for this module!

Click on "Save a Permanent Copy" if you want to save any changes to your version of this code.

<img src="https://github.com/arcus/education_r_environment/blob/main/media/make_copy.png?raw=true" alt="Posit menu bar with 'Make Permanent Copy'." style = "border: 1px solid rgb(var(--color-highlight)); clear:both;">

Now you can not only work in the cloud, but also save your work.

<h3>Option 3: Work on Your Computer</h3>

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

@sage
<script input="hidden">
// Make *any* div with class 'python' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python',
                       evalButtonText: 'Run python',
                       languages: ["python"],
                       hide: ['fullScreen', 'permalink'],
                       });
// Make *any* div with class 'python_run' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python_run',
                      evalButtonText: 'Run python',
                      languages: ["python"],
                      hide: ['fullScreen', 'permalink'],
                      autoeval: 'true'
                      });
// Make *any* div with class 'python_link' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python_link',
                      evalButtonText: 'Run python',
                      languages: ["python"],
                      hide: ['fullScreen', 'permalink'],
                      autoeval: 'false',
                      linked: 'true'
                      });
// Make *any* div with class 'python_data_init' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python_data_init',
                      evalButtonText: 'Run python',
                      languages: ["python"],
                      editor: 'codemirror-readonly',
                      hide: ['fullScreen', 'permalink','output','evalButton'],
                      autoeval: 'true',
                      linked: 'true',
                      linkKey: "data"
                      });       
// Make *any* div with class 'python_data' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python_data',
                      evalButtonText: 'Run python',
                      languages: ["python"],
                      hide: ['fullScreen', 'permalink'],
                      autoeval: 'false',
                      linked: 'true',
                      linkKey: "data"
                      });                

// Make *any* div with class 'r' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.r',
                      evalButtonText: 'Run R',
                      languages: ["r"],
                      hide: ['fullScreen', 'permalink'],
                      });
// Make *any* div with class 'r_run' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.r_run',
                      evalButtonText: 'Run R',
                      languages: ["r"],
                      hide: ['fullScreen', 'permalink'],
                      autoeval: 'true'
                      });
</script>
@end

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
script:  https://code.jquery.com/jquery-3.6.0.slim.min.js
script: https://sagecell.sagemath.org/static/embedded_sagecell.js

-->

# Module Macros

@overview

## Lesson Preparation: R

@lesson_prep_r

## Lesson Preparation: Python

@lesson_prep_python

## Feedback
@feedback

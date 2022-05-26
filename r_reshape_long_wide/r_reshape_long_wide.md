<!--
author:   Joy Payton
email:    paytonk@chop.edu
version:  1.0.0
module_template_version: 2.0.0
language: en
narrator: US English Female
title: Reshaping Data in R: Long and Wide Data
comment:  A module that teaches how to reshape tabular data in R, concentrating on some typical shapes known as "long" and "wide" data.
long_description: Reshaping data is one of the essential skills in getting your data in a tidy format, ready to visualize, analyze, and model.  This module is appropriate for learners who feel comfortable with R basics and are ready to take on the challenges of real life data, which is often messy and requires considerable effort to tidy.

estimated_time: 1 hour

@learning_objectives  

After completion of this module, learners will be able to:

- Define and differentiate "long data" and "wide data"
- Use dplyr tools to reshape data effecdtively


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
# Reshaping Data in R: Long and Wide Data

<div class = "overview">

## Overview

@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

This module assumes familiarity with R basics, including ingesting .csv data and using dplyr tools to do basic transformation including choosing only certain columns or rows of a data frame.  If you need to learn these basics, we suggest our [R Basics: Introduction](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_introduction/r_basics_introduction.md) module and our [R Basics: Transform Data](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/r_basics_transform_data/r_basics_transform_data.md) module

**Learning Objectives**

@learning_objectives

</div>

## Data Shapes

Importantly, we're only dealing with "rectangular" data here. Rectangular data (or **"tabular"** data, from the word "table") has rows and columns.  Rectangular data (such as rows and columns of demographic or biosample data) is by no means the only data that matters to biomedical researchers.  For example, wave form data, genomics files, and audio recordings can all be important data for research.  That kind of data is out of scope for this module, however.

A rectangular data set can take on a lot of different rectangular shapes with different styles of organizing data. Some disciplines have specific types of summary tables, for example, that customarily appear in published manuscripts.  The one method or shape that is best suited for data analysis is known as "tidy".

Two rectangular data shapes are the "long" and "wide" formats.

### Wide Data

We'll start with wide data, which may be more familiar to you.  Wide data stores variables in columns, with (ideally) each variable assigned its own column.  Consider, for example, some fabricated biosample data.  In this study, research subjects have come in for one or two biosample data collections.  Either blood or saliva was taken.  This is the way data might be stored in REDCap, for example, if you use events with suffixes to indicate which event.

subject_id | biosample_id_1 | collection_date_1 | collection_time_1 | sample_type_1 | collection_method_1 | collected_by_id_1 | sample_size_1 | biosample_id_2 | collection_date_2 | collection_time_2 | sample_type_2 | collection_method_2 | collected_by_id_2 | sample_size_2
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
876123 | 3380629109 | 2019-05-14 | 9:15 | blood | venipuncture | 4511 | 10 ml | 3380629887 | 2019-05-14 | 18:34 | blood | venipuncture | 4511 | 10 ml
612351 | 3531370968 | 2019-06-04 |  | blood | venipuncture | 7124 | 10 ml | 4182110569 | 2020-02-14 | 13:55 | blood | venipuncture | 3201 | 10 ml
716978 | 3860881351 | 2019-10-20 | 10:45 | saliva | swab | 4511 | 4 g |  |  |  |  |  |  |
321900 | 4190070221 | 2020-02-25 |  | saliva | swab | 7124 | NA |  |  |  |  |  |  |
342855 | 4348365204 | 2020-06-19 | 15:20 | blood | venipuncture | NA | 10 ml |  |  |  |  |  |  |
901284 | 4377143652 | 2020-08-10 |  | blood | venipuncture | 3201 | 10 ml |  |  |  |  |  |  |

### Long Data

Compare that with long data, which might seem less familiar.  Long data has one or more columns that uniquely identify an observation, then just one column that discloses the name of a measured variable, and one column that gives the value of that variable.

The long data below, which focuses on the `biosample_id` (which is unique for each biosample) instead of the `subject_id`, has the same information as the wide data above.  However, the data is organized in a format that features **keys** (variable names) and **values** appearing in **key-value pairs**.  You'll also notice that we've changed the variable names to remove the `_1` and `_2` suffixes used to indicate a first or second collection and instead added a "sequence" variable to state that information.

| biosample_id | key |	value |
| --------- | --- | --- |
| 3380629109 | subject_id | 876123 |
| 3380629109 | collection_date | 2019-05-14 |
| 3380629109 | collection_time | 09:15:00 |
| 3380629109 | sample_type | blood |
| 3380629109 | collection_method | venipuncture |
| 3380629109 | collected_by_id | 4511 |
| 3380629109 | sample_size | 10 ml |
| 3380629109 | sequence | 1 |
| 3531370968 | subject_id | 612351 |
| 3531370968 | collection_date | 2019-06-04 |
| 3531370968 | sample_type | blood |
| 3531370968 | collection_method | venipuncture |
| 3531370968 | collected_by_id | 7124 |
| 3531370968 | sample_size | 10 ml |
| 3531370968 | sequence | 1 |
| 3860881351 | subject_id | 716978 |
| 3860881351 | collection_date | 2019-10-20 |
| 3860881351 | collection_time | 10:45:00 |
| 3860881351 | sample_type | saliva |
| 3860881351 | collection_method | swab |
| 3860881351 | collected_by_id | 4511 |
| 3860881351 | sample_size | 4 g |
| 3860881351 | sequence | 1 |
| 4190070221 | subject_id | 612351 |
| 4190070221 | collection_date | 2020-02-25 |
| 4190070221 | sample_type | saliva |
| 4190070221 | collection_method | swab |
| 4190070221 | collected_by_id | 7124 |
| 4190070221 | sequence | 1 |
| 4348365204 | subject_id | 342855 |
| 4348365204 | collection_date | 2020-06-19 |
| 4348365204 | collection_time | 15:20:00 |
| 4348365204 | sample_type | blood |
| 4348365204 | collection_method | venipuncture |
| 4348365204 | sample_size | 10 ml |
| 4348365204 | sequence | 1 |
| 4377143652 | subject_id | 901284 |
| 4377143652 | collection_date | 2020-08-10 |
| 4377143652 | sample_type | blood |
| 4377143652 | collection_method | venipuncture |
| 4377143652 | collected_by_id | 3201 |
| 4377143652 | sample_size | 10 ml |
| 4377143652 | sequence | 1 |
| 3380629887 | subject_id | 876123 |
| 3380629887 | collection_date | 2019-05-14 |
| 3380629887 | collection_time | 18:34 |
| 3380629887 | sample_type | blood |
| 3380629887 | collection_method | venipuncture |
| 3380629887 | collected_by_id | 4511 |
| 3380629887 | sample_size | 10 ml |
| 3380629887 | sequence | 2 |
| 4182110569 | subject_id | 612351 |
| 4182110569 | collection_date | 2020-02-14 |
| 4182110569 | collection_time | 13:55 |
| 4182110569 | sample_type | blood |
| 4182110569 | collection_method | venipuncture |
| 4182110569 | collected_by_id | 3201 |
| 4182110569 | sample_size | 10 ml |
| 4182110569 | sequence | 2 |

Why would you ever want data in long format?  Your eyes have to do a lot of work to keep track of all the variables for a given biosample.  Long data might seem awkward and not particularly useful.  However, getting data into a long format allows you to reshape the data effectively.  

In fact, you may also hear long data called "molten" data, and hear phrases like "melting" the data.  When something is molten or melted, it's easier to then "pour" that data into a new shape (you might hear "cast" or "mold" to describe this process).  It's easier to melt something down to reshape it, rather than take a shape you don't want, cut off bits and reattach them in the new shape.

## Reshaping into a Tidy Format

A data set is tidy, [according to Hadley Wickham and Garrett Grolemund](https://r4ds.had.co.nz/tidy-data.html#tidy-data-1), if:

* Each variable is in its own column
* Each observation is in its own row, and
* Each value is in its own cell

If you want to understand more about tidy data, we encourage you to try our brief [Tidy Data](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/tidy_data/tidy_data.md#1) module.

"Tidy" data is wide, but not all wide data is tidy! For example, we'd argue that the wide biosample data isn't particularly tidy.

For example, we're repeating columns (`collection_date_1`, `collection_date_2`, etc.) in a way that makes it tricky to do things like count the number of blood draws or do a time-series graph on number of samples taken per day.  We're also treating the "observation" for each row as a subject, but really, a unique observation is a single biosample collection.  Our data is split into two column sets, and we'd like to tidy it.  

We'll work with this dataset in R, to give you the practice you need!

## Lesson Preparation: Our RStudio Environment

Please do this step now, because we're going to ask you to follow along throughout and try out code as you go.  

Please read over both options before you start performing any actions, to make sure you pick the right option for you.

<h3>Option 1: Work in the Cloud</h3>

This might work well for you if you either can't or don't want to install R and RStudio on your computer.  The benefit is that you don't have to install anything, but one negative is that this option requires a bit of waiting for your environment to come online.

**First**, we need to create a small container in the cloud for you to work in just using your web browser.  **Click "Launch binder" below.**  It might take a while (5 minutes) to create, depending on how recently it was created (when it's being used more, it's quicker!).  We're looking for a faster way to get you off and running in RStudio without downloads and without creating accounts, but for now this is a great, free way for us to get you working with no extra work on your part.

  <a href = "https://mybinder.org/v2/gh/arcus/education_r_environment/main?urlpath=rstudio" target = "_blank"><img src="https://mybinder.org/static/images/badge_logo.svg"></a> **← Click the "launch binder" button!**

<div class = "hint" style = "align-items: center; display: flex;">

<div style = "margin: 1rem; max-width: 45%; float:left;"> If you're the first person to fire up this environment in a while, you might see this loading screen for up to five minutes.  Be patient!</div>
<div style = "margin: 1rem auto; max-width: 45%; float:left;"> ![Binder loading screen](media/binder_loading.gif)<!--
style = "border: 1px solid rgb(var(--color-highlight));"-->
</div>
</div>

**Then**, once you have access to RStudio and you see something like the image below, you'll need to open the sample data for this course.  In the file area to the lower right, you'll see, among multiple choices, the folder called "r\_reshape\_long\_wide".  That's the code for this module!

![RStudio as shown in the cloud platform Binder](media/binder_rstudio.png)<!--
style = "border: 1px solid rgb(var(--color-highlight)); max-width: 800px;"-->

<h3>Option 2: Work on Your Computer</h3>

If you have [R](https://www.r-project.org/) and [RStudio](https://www.rstudio.com/products/rstudio/download/#download) installed already on your local computer, you might be interested in simply downloading our sample code to your computer. Here's how.  Note -- if you've already done this step in another module, you might have the material for this module already!

* In RStudio, open a new project (File, New Project)
* Select Version Control, then Git
* Drop this link into the "Repository URL": https://github.com/arcus/education_r_environment
* Change the "Project directory name" and "Create project as a subdirectory of" boxes to suit your needs (where will this code be stored on your computer?).
* Click to select the "Open in new session" checkbox
* Click "Create Project"
* In the file area to the lower right, you'll see, among multiple choices, the folder called "r\_reshape\_long\_wide".  That's the code for this module!

**Want to watch this process?  Click on the image below to play an animated gif.  It will continue to loop and you can re-start it by clicking again.**

<div style="display:none">@gifPreload</div>

<figure>
  <img src="https://github.com/arcus/education_modules/blob/main/r_basics_introduction/media/rstudio_new_project.png?raw=true" height="384" width="512" alt="RStudio can create a new project that gets its contents from a git repository." data-alt="https://github.com/arcus/education_modules/blob/main/r_basics_introduction/media/rstudio_new_project.gif?raw=true" style = "border: 1px solid rgb(var(--color-highlight));">

<figcaption style = "font-size: 1em;">Click on the image to play the demo of the above steps!</figcaption>
</figure>

If you already completed this work for a previous module, and it's been a while since you downloaded this project to your computer, you may want to get any new and improved files that have been placed there in the meantime:

* Open your project.
* In the Version Control menu, choose "pull branches".  There are two places to do this, as shown below:

![Git button menu with choices to pull and push branches](media/pull_branches.png)<!-- style = "border: 1px solid rgb(var(--color-highlight)); max-width:400px;" -->  
![Tools menu with choices to pull and push branches](media/pull_branches_2.png)<!-- style = "border: 1px solid rgb(var(--color-highlight)); max-width:400px;" -->

<div class = "warning">
If you're pulling branches after having worked in other R modules, you might have made local changes (for example, when you filled in exercise code) that will be overwritten by pulling the latest version.  If you want to save your changes, consider making a copy of any exercise files and naming them something new.  For example, if you have already worked in the `r_basics_transform_data` exercise files, you might want to save your version of `transform_exercises.Rmd` to `my_transform_exercises.Rmd`.  That way, you can pull down the latest version of code, overwriting `transform_exercises.Rmd` while holding on to your changes in the new file.
</div>


## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22R+Basics+Introduction%22)!

Material for this module was adapted, with permission, from [Stephan Kadauke's R for Clinical Data workshop materials](https://skadauke.github.io/intro-to-r-for-clinicians-chop/).  We owe special thanks to Dr. Kadauke as well as the R User Group at Children's Hospital of Philadelphia for their generosity in sharing these materials.

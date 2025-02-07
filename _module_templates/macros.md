<!--

author:   DART Team
email:    dart@chop.edu
version:  1.4.3
current_version_description: Add text after Overview and Feedback that invites learners to the rest of the modules
language: en
narrator: UK English Female
title: Module Macros
comment:  This is placeholder module to save macros used in other modules.

@version_history 

Previous versions: 

- [1.4.3](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/5d38321396c995da5c48ea80352fae31d5d8b806/_module_templates/macros.md#1): Add text after Overview and Feedback that invites learners to the rest of the modules
- [1.3.0](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/bbd9189b6c598c77059da184995c83b4037cbd73/_module_templates/macros.md#1) :Add module\_id to macros for creating the REDCap survey link
- [1.2.1](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/a9aa1b38fc51db4252c9547654d9e36dba7864e5/_module_templates/macros.md#1): make CSS come from GCS


@end

@overview
<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time_in_minutes minutes

**Pre-requisites**

@pre_reqs

**Learning Objectives**

After completion of this module, learners will be able to:

@learning_objectives

**Version History**

This version (@version): @current_version_description

@version_history

</div>

Looking for other modules on this topic or other topics related to data analytics and data science in biomedicine?  Please see [our complete list of educational modules](https://arcus.github.io/education_modules/list_of_modules) or consider trying our [prototype curriculum builder](https://learn.arcus.chop.edu).

@end

@make_survey_button
<script modify="false">
function makeURL(title, version, module_type, module_id) {
  let url = new URL('https://redcap.chop.edu/surveys');
  url.searchParams.set('s', 'KHTXCXJJ93');
  url.searchParams.set('module_name', title);
  url.searchParams.set('version', version);
  url.searchParams.set('module_type', module_type);
  url.searchParams.set('module_id', module_id);
  return url;
}
var surveyURL = makeURL(@0, @1, @2, @3);

send.html(`<a href="${surveyURL}" target="_blank">
  <button class="survey-button">Provide Your Feedback</button>
</a>`)
</script>
@end

@feedback
@make_survey_button('@title', '@version', '@module_type', '@module_id') 

Our brief survey takes just a few minutes. We use this information to fix and improve our content. Crucially, since our modules do not track user behavior, this is also the only way we can estimate how many learners are using our materials. 

One of the questions will ask if we achieved the learning objectives for the module. As a reminder, here's what those were: 


**Learning Objectives:**

After completion of this module, learners will be able to:

@learning_objectives

Looking for other modules on this topic or other topics related to data analytics and data science in biomedicine?  Please see [our complete list of educational modules](https://arcus.github.io/education_modules/list_of_modules) or consider trying our [prototype curriculum builder](https://learn.arcus.chop.edu).

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

link:  https://cdn.jsdelivr.net/gh/arcus/education_modules@main/assets/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js
script:  https://code.jquery.com/jquery-3.6.0.slim.min.js

-->

# Module Macros

@overview

## Feedback

@feedback

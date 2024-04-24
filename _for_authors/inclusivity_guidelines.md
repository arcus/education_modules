# Inclusivity Guidelines

This is a working document articulating our goals and standards for creating content that will be valuable and accessible to as wide a range of users as possible. Specifically, we are designing with a variety of ["edge" users](https://guide.inclusivedesign.ca/activities/inclusive-design-mapping/) in mind: those with limited access to visual content or auditory content, those with barriers related to attention, cognition, sensory processing, or language, and those with limited technology access and/or financial resources. A core principle is to allow users as much flexibility as possible to configure their learning experiences to meet their own needs and preferences.

The guidelines presented here are inspired by several other guides including the [Web Content Accessibility Guidelines WCAG21](https://www.w3.org/WAI/WCAG21/quickref) and [The Inclusive Learning Design Handbook](https://handbook.floeproject.org/approachesoverview). Recommendations specific to educational videos can be found [here](https://ctl.wiley.com/how-to-ensure-accessibility-for-educational-videos/).

## Guidelines

* Maximize opportunities for users to customize their own learning experience
  - Relevant information should be provided for each module upfront to help users decide which ones to do and which to skip: time estimate, expected learning outcomes, etc.
  - Provide content in a variety of forms and styles: screencasts, text, webinars/lectures, practical exercises, etc. Whenever possible, multiple forms/styles should be incorporated in each module so learners have multiple avenues to the content.
* Make text alternatives available by default for all visual and audio content
  - Subtitles available for every video with audio.
  - Alt text available for every image.
* Provide audio description for visuals presented in video
  - For example, in a screencast, instead of just, "And then click here," provide description that could help scaffold someone without visual access like, "And then click on the button that says 'Run' in the top-right corner of the screen". Be sure to make use of text cues when available (e.g. button labels), not just visual signals like color or location.
  - When important content is conveyed in a visual, describe the key elements. For example, "Running this query produces the table below. It displays the first 5 rows by default, and columns for ID, encounter ID, diagnosis, and outcome."
  - When including a data visualization, verbally describe important features, such as both axis labels and visible trends in the data. For example, "Here's a scatterplot showing number of encounters on the y-axis and age on the x-axis. All 183 patients from our sample are represented here, and it looks like a weak positive trend, with older patients being more likely to have had more encounters. There are a few important outliers, though, such as this patient at about 6 months old with more than 20 encounters already."
  - When visual information is repeated with minimal changes, it's fine to indicate that without providing a full description again. For example, "And here's the updated table, filtered to only show patients who have been seen in the last 2 years."
  - When important visual information is too complex to include sufficient audio description (i.e. it would slow the content down so much as to impair its utility), an alternative video file should be provided with audio descriptions included.
* Use color choices that maximize accessibility
  - Color should never be the sole method for distinguishing visual content
* Provide clear, consistent organization and content structure to reduce cognitive load for users
  - Use clear, informative headers for each subsection. The resulting table of contents should give a good sense of the flow and structure of the module. Avoid titles and headers that sacrifice clarity for playfulness.
  - Use informative link text (e.g. instead of "To learn more about python, click [here](https://www.example.com)", say "Read this article to [learn more about python](https://www.example.com).")
  - Use parallel structure across modules covering similar content.
  - Use consistent formatting (e.g. consistent page headers and footers, consistent style controlled by css file)
* Reduce language barriers
  - The language of each page is identified in the HTML (e.g. `<html lang="en-US">`)
  - Avoid unclear language: unexplained idioms or references, unexplained acronyms, unnecessary technical language. 
  - Try to write in short, digestible pieces --- avoid long paragraphs and break long sections up with sub-headers
  - Unusual words, or words taking on a very specific meaning in context, should be defined for the user, either on the page (e.g. using footnotes) or with links to a definition/glossary
  - Provide pronunciation guides for especially unusual words of particular importance (a common example is package names, such as dplyr)
* Take proactive steps to be welcoming to a diverse group of potential users
  - Avoid unnecessarily gendered language (e.g. use "they" singular rather than "he or she" for an unknown person)
  - Intentionally represent diversity in our examples and images
  - Strive for diverse voices in the people presenting our content (e.g. webinars), and in the sources we direct users to  

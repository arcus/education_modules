<!--

author:   DART Team
email:    dart@chop.edu
version:  1.0.0
current_version_description: Initial version
language: en
narrator: UK English Female
title: Using macros in LiaScript

@version_history
No previous versions: 
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
-->
# Using macros in LiaScript

## Intro

For an excellent overview, see the [liascript help documentation on macros](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md).

Basically, macros can be defined in the header of a liascript document and then you can use them throughout the document itself as a basic text substitution. So if you define `author: Octavia Butler` in the header, then every time you put `@author` in the document, it will be replaced by the text `Octavia Butler`.

There are a few handy features that make this much more powerful than it first appears, though:

- you can call macros from other macros
- you can include markdown, html, css, and javascript in the text you're subbing in, and it will execute
- you can pass arguments to macros (especially helpful when your macro includes javascript)
- you can automatically load all of the macros for another module by just linking to that module as an `import` in your new module's header. This means we can have a separate macro module where we save all of the macros, and then load them all with a single line in each new module.

## Example: Overview section

We have a very formulaic start to every module. Previously, we copy-pasted most of the boiler plate and used small macros to sub in module-specific text, estimated_time. Because we can call macros from other macros, though, we can define a macro for the overview that calls each of the module-specific macros within it.

## Example: Lesson Prep sections

We also use a lot of repeated text in our lesson prep sections for R and Python modules. We can apply the same approach as for the overview, but (especially for R lessons) the subbed in text is much more complicated --- it includes images, highlight boxes, gifs, etc. --- but it all works great!

The only exception is markdown comments. We had some markdown comments to add html to images e.g. `![""](media/rstudio_panes.png)<!-- style = "max-width:900px;" -->` and that doesn't work because the end of the comment looks like the end of the liascript header comment. Easy fix, though. We can just use all html to insert the image, instead of blending html and markdown.

I love being able to move a lot of the html-heavy content to a macro because it makes the module md document a lot easier to read.

## Example: Feedback section

The most complicated example currently is the feedback section because we need a little javascript to generate the survey URL. So we have a macro called `make_survey_url` that is javascript and takes a few arguments (title, version_number, module_type) and uses them to generate an html link of the format `<a href="${surveyURL}")">our brief survey</a>`, where each of the arguments are appended to the redcap survey link as search parameters.

Then there's a `feedback` macro that is mostly just text substitution, like the overview, but includes a line that uses the `make_survey_url` macro and plugs in macros from this template as the arguments: `Thank you in advance for filling out @make_survey_url('@title', '@version', '@module_type')!`

## Our macro files

To avoid loading lots of macros unnecessarily, and to make the macro files themselves easier to read and edit, we have more than one md file for storing macros. 

- `macros.md` includes the general-purpose macros such as those to generate the overview and feedback sections. 
- `macros_wrapper.md` includes macros for use in wrapper modules, in particular, the macros to generate the Lesson Preparation section with the list of external resources. 
- `macros_r.md` includes the macro `lesson_prep_r` that inserts instructions for opening and using interactive rmd files 
- `macros_python.md` includes the macros ` lesson_prep_python_sage`, which inserts instructions for using interactive python cells in the lesson, and `sage`, which is necessary to make those cells work. It also loads associated scripts for sagemath. 
- `macros_sql.md` includes the macros `lesson_prep_sql`, which inserts instructions for using interactive SQL cells and a brief refresher on SQL including our style guide, and also `AlaSQL.eval`, which builds the functions to make the interactive SQL cells work. 

Additionally, there is a separate file for each SQL table to load.  This is because the tables are generated, row by row, in the macros, which takes up a lot of space --- storing tables separately keeps our general SQL macros file easier to read, and avoids generating tables we may not need in a given module. 

## Steps for adding a macro

1. Add the text you want to sub in to the appropriate macros module, in the header, specified as either a [single line or block macro](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md#single-line)
2. Make sure that macros module is listed as an import in the header of your new macro
3. Insert your macro wherever you want it to appear with `@macro_name` (note that macro names are case-sensitive, so `@author` is different from `@Author`)
4. Check that all of the substituted text is rendering as expected in your final module. 

Note: If you want to change an existing macro in one of the module macros files, **you must check how the changes render in all modules referencing that macro**. To get a list of all modules using the macro, try `grep -r "macro_name"` in the terminal for the education_modules directory.   

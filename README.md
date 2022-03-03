# Education Modules

## Intention

This repository holds publicly available instructional modules aimed at teaching data science and related skills to researchers, as part of an NIH emphasis on improving research reproducibility, transparency, and rigor.

These materials have been created for the purpose of sharing them widely with the research community.  Support for this effort includes NIH funding via an R25 grant mechanism.

## About These Materials

The training materials here are built in [markdown](https://www.markdownguide.org/), and you can use the Liascript markdown renderer to make them into attractive, configurable training modules.  To use Liascript, go to https://liascript.io and enter the url of the (raw) markdown.

For example, to use the training included in [data_visualization_in_ggplot2](data_visualization_in_ggplot2/data_visualization_ggplot2.md), navigate to https://liascript.io add the url for the "raw" version of [data_visualization_in_ggplot2](data_visualization_in_ggplot2/data_visualization_ggplot2.md), which is https://raw.githubusercontent.com/arcus/education_modules/main/data_visualization_in_ggplot2/data_visualization_ggplot2.md.  Together, that gives you this combined url: https://liascript.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/data_visualization_in_ggplot2/data_visualization_ggplot2.md

## Links to Repository Contents

||||
|--|--|--|
|Command Line 101|[Training Course](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_scripting_101/bash_scripting_101.md)|[Markdown](bash_scripting_101/bash_scripting_101.md)|
|Data Visualization in ggplot2|[Training Course](https://liascript.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/data_visualization_in_ggplot2/data_visualization_ggplot2.md)| [Markdown](data_visualization_in_ggplot2/data_visualization_ggplot2.md)|
|Data Visualization in Open Source Software|[Training Course](https://liascript.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/data_visualization_in_open_source_software/data_visualization.md) | [Markdown](data_visualization_in_open_source_software/data_visualization.md) |
|Data Visualization in Seaborn|[Training Course](https://liascript.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/data_visualization_in_seaborn/data_visualization_seaborn.md) | [Markdown](data_visualization_in_seaborn/data_visualization_seaborn.md)|
|Intro to R and RStudio|[Training Course](https://liascript.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/intro_to_r_rstudio/intro_to_r_rstudio.md) | [Markdown](intro_to_r_rstudio/intro_to_r_rstudio.md)|
|Intro to Python|[Training Course](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/intro_to_python/intro_to_python.md)| [Markdown](intro_to_python/intro_to_python.md)|
|Reproducibility|[Training Course](https://liascript.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/reproducibility/reproducibility.md)| [Markdown](reproducibility/reproducibility.md)|
|Statistical Tests|[Training Course](https://liascript.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/statistical_tests/statistical_tests.md)| [Markdown](statistical_tests/statistical_tests.md)|


## For Contributors

If you would like to create a module for inclusion here, please review the methods for doing so within our [How To Guide](how_to.md).

Root level folders in this repository include instructional modules as well as some shared assets that will be used by instructional modules.  Want to submit a pull request to add materials?  Please abide by the file structure and naming conventions described here and captured in existing materials.

File and directory names, except for when established convention (e.g. README.md) differs, should be in lower case with underscores separating words.  

```
./
├── README.md
├── assets
│   ├── media
│   ├── css
│   │   ├── styles.css
│   │   └── maybe_one_more.css
│   └── js
│       ├── some_script.js.min
│       └── Other_Commonly_Written_This_Way_Script.js
├── lesson_name
│   ├── lesson_name.md
│   ├── media
│   │   ├── some_video.mp4
│   │   └── some_image.png
│   └── code
│       ├── some_markdown.Rmd
│       ├── python_sample.ipynb
│       └── to_be_completed.R
└── different_lesson_name
    ├── different_lesson_name.md
    ├── media
    │   ├── best_video.mp4
    │   └── an_image.png
    └── code
       └── sample.R

```

## A Few Notes and Caveats

If you use .css or .js scripts, it's important to know that you can't supply these scripts directly from GitHub.  GitHub does not provide the appropriate metadata to indicate that the content of the files is of the correct type, which means that browsers won't include them.

One solution is to use a CDN that re-packages GitHub contents for use in a web page.  For example, [Liascript itself suggests using a CDN](https://github.com/liaScript/custom-style/) to provide a CSS script from GitHub.

Since CDNs generally have a refresh rate that doesn't meet the "let's try this really quickly" pace of development in GitHub, another option is to host your script in another publicly accessible location.  In our case, we've made use of the AWS S3 service to host a custom css file.  This means updating the S3 version of the file as well as the version hosted here, in this GitHub, but the extra headache is worth it.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

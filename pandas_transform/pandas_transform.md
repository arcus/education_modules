<!--

author:   Elizabeth Drellich
email:    drelliche@chop.edu
version:  0.0.1
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Module Title
comment:  This is a short, focused description of the module.
long_description: This is a longer description, which should be understandable for a lay audience. It will print under "Is this module right for me?" in the overview.
estimated_time: This is rough guess of how long it might take a learner to work through the module. It will print under "Estimated time to completion" in the overview

@learning_objectives  

After completion of this module, learners will be able to:

- Navigate the row and column structure of a `pandas` DataFrame
- Locate data using the `.loc` method
- Filter data using conditional statements
- Create new DataFrames from existing DataFrames
- Edit data in a `pandas` DataFrame.

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

script: https://sagecell.sagemath.org/static/embedded_sagecell.js

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
</script>
@end
-->

# Transforming Data in Python using Pandas

## Embedded Code Testing:
@sage

Python cell:
<div class="python">
<lia-keep>
<script type="text/x-sage">
1+2
</script>
</lia-keep>
</div>


<div class="python">
<lia-keep>
<script type="text/x-sage">
import pandas as pd
d = {'col1': [1, 2], 'col2': [3, 4]};
df = pd.DataFrame(data=d);
print(df)
</script>
</lia-keep>
</div>


Jupyterlite lab environment:
??[notebook](https://arcus.github.io/jupyterlite/lab/index.html)

Jupyterlite classic notebook:
??[notebook](https://arcus.github.io/jupyterlite/retro/notebooks/?path=p5.ipynb)
## Overview

@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

Before starting this module it is useful for you to have:

* some familiarity with [tabular data](tabular/data/module)
* an introductory level exposure to coding in [python](intro/to/python/module)


If relevant, you can include recommendations for somewhere else to start if the learner doesn't have these prereqs. For example: If you are brand new to R or python (or want a refresher) consider starting with [Intro to R](link) or [Intro to python](link) first and then coming back here.

**Learning Objectives**

@learning_objectives

For help articulating learning objectives, see [this guide to learning objectives, including lots of example verbs](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/).

</div>

## Lesson Preparation

If you want to do all of the exercises in your browser window, there is no preparation required for this lesson. Your code will run, but will not be saved.

If you would prefer to save your work, particularly the hands on exercises, you have a few options:

1. If you have python on your computer, you can download he notebook and run it yourself.

2. Make and account somewhere?



## The `pandas` Package

The `pandas` [package](https://pandas.pydata.org/) lets you store, examine, and manipulate tabular data using python.

When and why would `pandas` and programming in python be preferable to doing similar things in `R`?

What is this `import`, `as pd` and `import numpy as np`?

## `DataFrame`s

Tabular data! Tidy tabular data! Use `.head()` to see it!

Always indexed by `[row,column]`

## Filter specific rows and columns

Identify an entry with `loc` and `iloc`

## Creating new columns

### Logical and mathematical functions in Python

## Chaining Methods

## Additional Resources

The last section of the module content should be a list of additional resources, both ours and outside sources, including links to other modules that build on this content or are otherwise related.

The creators of the pandas package have [great tutorials](https://pandas.pydata.org/docs/getting_started/index.html) with very thorough examples.

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Transform+Data+with+Pandas%22)!

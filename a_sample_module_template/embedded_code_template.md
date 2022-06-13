<!--

author:   Elizabeth Drellich, Meredith Lee, and Rose Hartman
email:    drelliche@chop.edu
version:  0.0.1
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Embedding code into Liascript
comment:  This is a place to figure out how to embed code into a Liascript module.
long_description: Do you want to include python code in your module?

@learning_objectives  

After completion of this module, learners will be able to:

- Embed individual cells
- Link individual embedded cells
- Embed Jupyter notebooks
- Embed Jupyterlite labs.

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


@SAGE.cell
<lia-keep>
<div class="@0">
<script type="text/x-sage">
@1
</script>
</div>
</lia-keep>
@end

-->
# Embedding Code into Liascript
<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

**Learning Objectives**

@learning_objectives

</div>

## Embedding sagemath cells

One cool spin-off of the [SageMath Project](https://www.sagemath.org) is the [SageMathCell](https://sagecell.sagemath.org) which allows you to run a single cell, not just in Sage, but in a number of languages including both python and R.

Full documentation is available on the [sagecell GitHub](https://github.com/sagemath/sagecell).

<div class= "important">
The sagemath cell is licensed under [GPLv2+](https://www.gnu.org/licenses/gpl-3.0.html) since there are some packages included in it with that license. For full details see the [licensing statement](https://github.com/sagemath/sagecell/blob/master/LICENSE.txt).
</div>

### Basic setup

In order to run cells in Liascript, we need to have a script in the header yaml to call out and run our code on the sagecell server.

```
script: https://sagecell.sagemath.org/static/embedded_sagecell.js
```

If we later decided that we need our own server, there are instructions on how to do that on [GitHub](https://github.com/sagemath/sagecell) but that would certainly need to go through some significant security vetting. For the moment, SageMathCell is certainly adequate for our needs.

In addition, we need to call a script defining the type of cells we want. To make this easier, several types of cells are ready to go. We will see examples of all of them on the next few pages, and show you how to make your own environments.

By including `@sage` on any page you want to have a cell on, all of these environments will be available on that page.


### Python cells

The `python` class will now give you a cell that runs python, and can be evaluated by clicking a button. The individual cell must be set up like this:

````
``` python @SAGE.cell(python)

Your python code goes here.

```
````

Under the hood the `@SAGE.cell` script is creating the sage cell and of the particular type, in this case `python`.

Let's see a first example:
@sage

``` python @SAGE.cell(python)

1+2  # this line will compute but not return output

print(3+4) #but this line will return output

```

<div class = "warning">
One twitchy thing about SageMathCells is that they won't return output unless you specifically ask them to print. The next cell imports `pandas` and then creates a Data Frame. If we make the last line `df` instead of `print(df)` it might not give us output even though a Jupyter notebook cell or using python in the command line would give output.
</div>


``` python @SAGE.cell(python)
import pandas as pd
d = {'col1': [1, 2], 'col2': [3, 4]};
df = pd.DataFrame(data=d);
print(df)
```

You can also have a python cell run automatically using the class `python_run`. This cell can still be edited and re-run by the user, but it will load with both the input and the output.

``` python @SAGE.cell(python_run)
import numpy as np
a = np.arange(15).reshape(3, 5)
print(a.transpose())
```

Even fancier, you can link cells using the class `python_link`, so that what is run in one cell impacts other cells run afterwards.

``` python @SAGE.cell(python_link)
import numpy as np
B = np.arange(16).reshape(4, 4) +  np.identity((4))
print(B.transpose())
```

In the cell above we imported `numpy` and defined a numpy array. Since the next cell is linked, if you run it after, it will use the same kernel as the cell above it.

``` python @SAGE.cell(python_link)
C = np.linalg.inv(B)
print("B * C =")
print(B,"*",C,"=")
print(np.rint(np.dot(B,C)))
```

<div class = "warning">
These linked cells won't communicate from one page to the next, but you can have what you want in the kernel load in a linked cell at the start of each page.
</div>

### R cells
@sage

Similarly you can include R code in a cell with the class `r`:

``` r @SAGE.cell(r)
# R Program to find the multiplicationtable (from 1 to 10)
# take input from the user
num = 7
# use for loop to iterate 10 times
for(i in 1:10) {
print(paste(num,'x', i, '=', num*i))
}
```

And if you want something to run automatically in R, the class `r_run` is currently set up to do that.

``` r @SAGE.cell(r_run)
# Program to check if the input number is prime or not
# take input from the user
for(num in 1:20){
flag = 0
# prime numbers are greater than 1
if(num > 1) {
# check for factors
flag = 1
for(i in 2:(num-1)) {
if ((num %% i) == 0) {
flag = 0
break
}
}
}
if(num == 2)    flag = 1
if(flag == 1) {
print(paste(num,"is a prime number"))
} else {
print(paste(num,"is not a prime number"))
}
}
```

### Loading data into a sagemathcell

If your data is stored as a file in the GitHub repository, you can ask the sagecell to download it directly from GitHub. The `python_data_init` class will run automatically when the page loads. The assumption is that this is not code that you want the user to be able to change, so they can't. This is the set-up, with no output whatsoever.
@sage

``` python @SAGE.cell(python_data_init)

import pandas as pd
covid_testing = pd.read_csv('https://raw.githubusercontent.com/arcus/education_modules/embedded_code/a_sample_module_template/covid_testing.csv')

```

If you use a linked cell to import the data, it will hang around for subsequent cells on the same page. You will have to reload everything for the next page, but this also helps keep tasks/topics organized. The `python_data` class is linked to `python_data_init` but will won't run until the user clicks a button.

**Click the "Run python" button** to see that the data did in fact load:

``` python @SAGE.cell(python_data)
print(covid_testing.loc[[0,1,2,3,4],["first_name","last_name"]])
```

All of the `python_data` cells are linked to the first cell, and completely editable by the user.

``` python @SAGE.cell(python_data)
print(covid_testing.loc[4,:])
```

The cells are also linked to each other and to the `python_data_init` cell which ran automatically. Because they are linked to a cell that ran automatically, all of them ran as soon as you loaded the page. Try running the second of these cells **before** the first to confirm that the object `day` is already defined:

``` python @SAGE.cell(python_data)
day = covid_testing.loc[4,"pan_day"]
print(day)
```

``` python @SAGE.cell(python_data)
print(day >= 5)
```

### Define your own sagemath cells type

We have defined a few types of cells so far in the yaml. That doesn't mean those are the only types of cells that you can embed. Check out the documentation on [customizing sagemath cells](https://github.com/sagemath/sagecell/blob/master/doc/embedding.rst) to learn how to link cells, pre-load cells with code, use other open source languages.

## Embedding Jupyterlite

We can also use Jupyterlite to embed full notebooks, or even full Jupyter labs directly into a page.

Right now we are hosting a [Jupyterlite webpage](https://arcus.github.io/jupyterlite/) using GitHub pages. Notebooks you want to be available there need to be added to the [arcus/jupyterlite](https://github.com/arcus/jupyterlite) repository.

<div class = "warning">
For the moment, the embedded Jupyterlite webpage does not load in Chrome. We are working with the developers of Liascript to fix this.
</div>

### Jupyterlite classic notebook
You can embed a single notebook using the retro version of notebooks. Go to **Help -> Launch Jupyter Classic Notebook** to launch a version in which each notebook has it's own url.

Then you can embed the url for your notebook directly in an iFrame using

```
??[notebook name](https://arcus.github.io/jupyterlite/retro/notebooks/?path=YourNotebookHere.ipynb)
```

??[notebook](https://arcus.github.io/jupyterlite/retro/notebooks/?path=p5.ipynb)

### Jupyterlite lab environment

If you want to have users explore a bigger project, you can also embed the entire Jupyter lab into the browser. This is clunky since your users will then have to navigate the file directory themselves.

??[notebook](https://arcus.github.io/jupyterlite/lab/index.html)

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Transform+Data+with+Pandas%22)!

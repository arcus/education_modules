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
// Make *any* div with class 'compute' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.compute',
                       evalButtonText: 'Evaluate'});
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
// Make *any* div with class 'r_cell' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.r_cell',
                      evalButtonText: 'Run R',
                      languages: ["r"],
                      hide: ['fullScreen', 'permalink'],
                      });
// Make *any* div with class 'r_run' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.r_run',
                      evalButtonText: 'Run python',
                      languages: ["r"],
                      hide: ['fullScreen', 'permalink'],
                      autoeval: 'true'
                      });
</script>
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

### Python cells

You can include a regular python cell that will evaluate for you. One twitchy thing about sagemathcells is that they won't return output unless you specifically ask them to print.

@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

1+2  # this line will not return output

print(3+4) #but this line will return output

</script>
</lia-keep>
</div>

The next cell imports `pandas` and then creates a dataframe. If we make the last line `df` instead of `print(df)` it might not give us output even though a Jupyter notebook cell or using python in the command line would give output.

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

You can also have a cell run automatically. This cell can still be edited and re-run by the user, but it will load with both the input and the output.

<div class="python_run">
<lia-keep>
<script type="text/x-sage">
import numpy as np
a = np.arange(15).reshape(3, 5)
print(a.transpose())
</script>
</lia-keep>
</div>


### R cells
@sage

Similarly you can include R code in a cell with the class `"r_cell"`:

<div class="r_cell">
<lia-keep>
<script type="text/x-sage">
# R Program to find the multiplicationtable (from 1 to 10)
# take input from the user
num = 7
# use for loop to iterate 10 times
for(i in 1:10) {
print(paste(num,'x', i, '=', num*i))
}
</script>
</lia-keep>
</div>

And if you want something to run automatically in R, the class `"r_run"` is currently set up to do that.

<div class="r_run">
<lia-keep>
<script type="text/x-sage">
# Program to check if the input number is prime or not
# take input from the user
for(num in 1:20){
flag = 0
# prime numbers are greater than 1
if(num > 1) {
# check for factors
flag = 1
for(i in 2:20) {
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
</script>
</lia-keep>
</div>

### Define your own sagemath cells type


## Embedding Jupyterlite


### Jupyterlite classic notebook
??[notebook](https://arcus.github.io/jupyterlite/retro/notebooks/?path=p5.ipynb)

### Jupyterlite lab environment
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

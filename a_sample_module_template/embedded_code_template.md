<!--

author:   Elizabeth Drellich, Meredith Lee, and Rose Hartman
email:    drelliche@chop.edu
version:  0.0.1
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Embedded code
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
<script>
// Make *any* div with class 'compute' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.compute',
                       evalButtonText: 'Evaluate'});
// Make *any* div with class 'python' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python',
                       evalButtonText: 'Run python',
                       languages: ["python"],
                       });
sagecell.makeSagecell({inputLocation: 'div.Rcell',
                      evalButtonText: 'Run R',
                      languages: ["r"]});
</script>
@end

-->
# Embedded Code Testing
<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

**Learning Objectives**

@learning_objectives

</div>

## Python cell
@sage
<div class="python">
<lia-keep>
<script type="text/x-sage">

print(1+2)

</script>
</lia-keep>
</div>

And here is some text describing that the next cell tries to import `pandas` and doesn't seem able to?

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


## R cell
@sage
<div class="Rcell">
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

## Jupyterlite lab environment
??[notebook](https://arcus.github.io/jupyterlite/lab/index.html)


## Jupyterlite classic notebook
??[notebook](https://arcus.github.io/jupyterlite/retro/notebooks/?path=p5.ipynb)

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Transform+Data+with+Pandas%22)!

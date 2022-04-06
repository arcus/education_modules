<!--

author:   Rose Hartman
email:    hartmanr1@chop.edu
version:  1.0.0
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Data Visualization in seaborn

comment:  This module includes code and explanations for several popular data visualizations using python's seaborn library. It also includes examples of how to modify seaborn plots to customize them for different uses.  

long_description: You can use the seaborn module in python to make many different kinds of data visualizations (also called plots or charts), including scatterplots, histograms, line plots, and trend lines. This module provides an example of each of these kinds of plots, including python code to make them using the seaborn module. It may be hard to follow if you are brand new to python, but it is appropriate for beginners with at least a small amount of python experience.

@learning_objectives  

After completion of this module, learners will be able to:

- use seaborn to create several common data visualizations
- customize some elements of a plot, and know where to look to learn how to customize others

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css
script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Data Visualization in seaborn

<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

This module assumes some familiarity with principles of data visualizations. If you've done some data visualization programming before, especially using seaborn or R's ggplot2, this module should be right for you. If you are brand new to both ggplot2 and seaborn, start with the overview of [data visualizations in open source software](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/data_visualization_in_open_source_software/data_visualization_in_open_source_software.md#1) first, and then come back here.

This module also assumes some basic familiarity with python, including

* installing and importing libraries
* reading in data
* manipulating data frames, including calculating new columns

If you are brand new to python (or want a refresher) consider starting with [Intro to python](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/intro_to_python/intro_to_python.md#1) first.

**Learning Objectives**

@learning_objectives

</div>

## Lesson Preparation


For the hands-on activities in this module, we will be using an online environment containing a Jupyter notebook. You don't need to install anything or set up an account, but you need a modern web browser like Chrome and a moderately good wifi connection.

Because it can take a few minutes for the environment to be created, we suggest you click the link below to start up the activity. We recommend using right-click to open it in a new tab or window, and then returning here to continue learning while the environment finishes loading. Here is the link:

<a href = "https://mybinder.org/v2/gh/arcus/education_modules/data_viz_seaborn?labpath=data_visualization_in_seaborn%2Fnotebooks%2Fdata_visualization_seaborn.ipynb" target = "_blank"> <img src = "https://mybinder.org/badge_logo.svg"></a> **← Click the "launch binder" button!**

If you have python already installed on your computer and you prefer to work through code examples there, you can <a href="https://raw.githubusercontent.com/arcus/education_modules/main/data_visualization_in_seaborn/notebooks/data_visualization_seaborn.ipynb" download>download the code for this module to run offline</a>.

### Importing seaborn

To use the seaborn library to make visualizations, you need to import it.

By convention, you import it with the shorthand `sns`. This is optional, but we recommend you do that because when you look at seaborn code online, you'll nearly always see it with that same abbreviation. Following that convention will make your code more comparable to examples you see online.

```Python
import seaborn as sns
```

### Working through interactive coding examples


Hopefully your [binder instance](#lesson-preparation) is done loading now! If not, be patient --- it can take as long as 20 or 30 minutes sometimes if the files haven't been used recently.

When it is ready, you should see a jupyter notebook in your browser with the code for this module. While you read through this module, we recommend you keep returning back to the binder instance to try running the code for yourself. Even better, try changing the code and see what happens.

<div class = "important">
Note that binder instances aren't stable. When you close the window or if it idles too long, it may erase all of your work. If you want to save any code or output you come up with while working in binder, you need to copy-paste the code to a new file to save it on your computer.
</div>


### The data

First, we need to load the modules we'll be using:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

```

<div class = "learnmore">
The [`pandas` module](https://pandas.pydata.org/docs/getting_started/index.html)) is for working with data in python. It is conventional to import `pandas` as `pd`.

The [`numpy` module](https://numpy.org/) has several useful functions for statistical calculations and other mathematical operations useful in scientific computing. It is conventional to import `numpy` as `np`.

The `seaborn` module is the plotting module that is the focus of this lesson, and it requires some pieces of `matplotlib`, since it is built as an extension to it.
</div>

And then read in the data set:

```python
covid_data = pd.read_csv("https://raw.githubusercontent.com/kendavidn/yaounde_serocovpop_shared/v1.0.0/data/yaounde_covid_seroprev_dataset.csv")

```

These data are from a COVID-19 serological survey conducted in Yaounde, Cameroon (Nwosu, K., Fokam, J., Wanda, F. et al., 2021[^1](Kene David Nwosu, Joseph Fokam, Franck Wanda, Lucien Mama, Erol Orel, Nicolas Ray, Jeanine Meke, Armel Tassegning, Desire Takou, Eric Mimbe, Beat Stoll, Josselin Guillebert, Eric Comte, Olivia Keiser, & Laura Ciaffi. (2021). kendavidn/yaounde_serocovpop_shared: Initial release (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.5218965)). The authors have made all of the code and data publicly available under a [creative commons 4.0 license](https://creativecommons.org/licenses/by/4.0/legalcode) to facilitate re-use.


<div class="learnmore">
To learn more about the study, see the [zenodo page for this dataset](https://zenodo.org/record/5218965#.YeBq2RPMITW). You can read the published article online: [SARS-CoV-2 antibody seroprevalence and associated risk factors in an urban district in Cameroon](https://www.nature.com/articles/s41467-021-25946-0).
</div>

<div class="important">
Run the above code yourself in binder (see [lesson preparation](#lesson-preparation) for links to start the binder instance) or on your own computer.

In the data\_visualization\_seaborn.ipynb file, the code in the **Setup** section includes these import commands and the command to read the csv file for the data. Before you will be able to generate the plots in the rest of the module, you should run those lines of code.
</div>

## Scatterplots

Scatterplots show the relationship between two continuous variables, one on the x-axis and one on the y-axis. Because they show each individual data point as a marker, they also provide a handy way to check visually for outliers.

For more background on scatterplots, watch [this Kahn Academy series](https://www.khanacademy.org/math/cc-eighth-grade-math/cc-8th-data/cc-8th-scatter-plots/v/constructing-scatter-plot).



### Basic scatterplot

The seaborn library includes a powerful function called `relplot`, short for "relationships plot" because it's designed to highlight relationships among variables in the data.

If you provide `relplot` with two continuous variables, it will default to making a scatterplot. Here we'll plot age and height.

```Python
sns.relplot(data = covid_data,
            x="val_age", y="val_height_cm")
```
![Basic scatterplot, with age on the x-axis and height on the y-axis. Age runs from approximately 5 to 80. Height increases sharply from 100-120 cm at 5 years old to an average of approximately 160 cm at about 20 years old, and then holds to 80 years old. There are 1011 observations plotted, with most observations between 5 and roughly 50 years old. There are three notable outliers with much lower height values than the rest, at roughly 60-80 cm. ](media/seaborn_scatter_1.png)

<div class = "options">
You can also create scatterplots with a similar function: `regplot` (short for "regression plot"), which we'll take a closer look at in the [trend lines section](#trend-lines).
</div>

### Using color for continuous variables

Let's try adding information about a third variable, weight, by using color.

```Python
sns.relplot(data = covid_data,
            x="val_age", y="val_height_cm", hue="val_weight_kg")
```
![Age and height scatterplot from the previous figure, but with weight represented by a color scale ranging from a very light pink (25 kg) to a dark purple (150 kg). Weight appears to correlate with both age and height, such that taller and older participants are also heavier. The three outliers with very small heights also have very high weights, suggesting they may represent typos during data entry.](media/seaborn_scatter_2.png)

Note that adding hue to the command automatically adds a legend to your plot as well.

### Using color to show groups

Now let's look at using color for a categorical variable(`is_smoker`, with options `ex_fumeur`, `fumeur`, and `non_fumeur`, referring to former smokers, current smokers, and non-smokers, respectively).

The values entered for `is_smoker` in the data are actually much longer than we need them to be --- they include the text of the option after the shorthand for it (e.g. former smokers are indicated by `ex_fumeur__j_ai_fum__mais_ne_fume_plus`). We don't want that additional text in the plot, so we'll recode that variable now.

```Python
# recode is_smoker to make the variable labels shorter
orig_codes = ["ex_fumeur__j_ai_fum__mais_ne_fume_plus", "fumeur__je_fume_actuellement", "non_fumeur__je_n_ai_jamais_fum"]
new_codes = ["ex-smoker", "smoker", "non-smoker"]

covid_data['is_smoker'] = covid_data['is_smoker'].replace(orig_codes, new_codes)

```

<div class = "learnmore">
For a refresher, see this tutorial on [recoding variables in a pandas dataframe](https://www.sfu.ca/~mjbrydon/tutorials/BAinPy/05_recode.html#replacing-values-from-a-list).
</div>

Then we can update our scatterplot to use `is_smoker` for color.

```Python
sns.relplot(data = covid_data,
            x="val_age", y="val_height_cm",
            hue="is_smoker")
```
![Age and height scatterplot again, but with "is smoker" represented by color, with non-smoker as blue, smoker as orange, and ex-smoker as green. Most of the observations are non-smokers, and smokers and ex-smokers don't start appearing until approximately age 15. There is no visually clear relationship between smoking status and height.](media/seaborn_scatter_3.png)


<div class = "important">
Tip: It's generally much easier to make any necessary changes to the dataframe, such as modifying variables, before sending it to the plotting command.
</div>

### Distinguish groups more clearly with color and shape

We'll improve this plot by using shape and color together to mark the Classification groups.

<div class = "important">
Tip: Don't use color alone to convey important information in your plots because if your end users are unable to distinguish the colors, the plot loses its value. Instead, double-up color information with another element, such as marker shape, to make the different groups easier to distinguish.
</div>

```Python
sns.relplot(data = covid_data,
            x="val_age", y="val_height_cm",
            hue="is_smoker", style = "is_smoker")
```
![Age and height scatterplot from the previous figure, with Classification represented using both color and shape: blue circles for non-smokers, orange exes for smokers, and green squares for ex-smokers.](media/seaborn_scatter_4.png)

### Custom colors

The seaborn library includes many color palettes to choose from, or you can specify colors manually.

Here we'll try switching from the default color palette to a version that is easier to distinguish for people with some types of colorblindness (although remember that even when using a palette that is supposedly colorblind friendly, you should still avoid using color on its own to display important information).

```Python
sns.relplot(data = covid_data,
            x="val_age", y="val_height_cm",
            hue="is_smoker", style = "is_smoker",
           palette = "colorblind")
```
![Age and height scatterplot from previous figure, now with slightly different shades of blue, orange, and green.](media/seaborn_scatter_5.png)

Rather than changing the palette for each individual plot, you may want to change the default color palatte for all of the plots you're generating. To do that, use `set_theme` to change the default settings for seaborn plots.

```Python
# to set the colorblind palette as default
sns.set_theme(palette="colorblind")
```

Now all of our plots will use the `colorblind` palette, unless we specify otherwise.

<div class = "learnmore">
The seaborn library has many different built-in color palettes to choose from. To learn more about setting custom colors in seaborn visualizations, see the [seaborn tutorial on color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html).
</div>

### Controlling figure aesthetics

The seaborn library handles the appearance of plots with two kinds of functions: style, and context.

- `style` refers to things like background color, gridlines, and axis ticks
- `context` refers to the visual scale of the plot, such as the size of the font used for axis labels

Seaborn controls style and context separately so that you can get a plot that has all the style elements you want, and then you can present that same plot scaled appropriately in different contexts --- for example, if you want to include it in a slide deck presentation, you probably want the fonts much larger and the lines heavier than you would if you wanted to include it as a figure in a paper. In this case, you would leave all of the style settings the same, but change context to "talk" to scale it for the slide deck and "paper" to scale it for use in the paper.

<div class = "learnmore">
We'll show a quick example of changing style and context here, but there are many more options available. To learn more about tweaking style and context, see the [seaborn tutorial on controlling figure aesthetics](https://seaborn.pydata.org/tutorial/aesthetics.html).
</div>

#### Setting plot style

```Python
# there are 5 preset seaborn themes: darkgrid, whitegrid, dark, white, and ticks
sns.set_style("white")

sns.relplot(data = covid_data,
            x="Age", y="Glucose",
            hue="Classification", style = "Classification")
```
![Age and height scatterplot from the previous figure, now with a blank white background and no gridlines.](media/seaborn_scatter_6.png)


#### Setting plot context

```Python
# there are 4 different contexts available: notebook (default), paper, talk, and poster
sns.set_context("poster")

sns.relplot(data = covid_data,
            x="Age", y="Glucose",
            hue="Classification", style = "Classification")
```
![Age and height scatterplot from the previous figure, with much larger font for axis scales and labels, and larger markers for the points in the plot.](media/seaborn_scatter_7.png)

```Python
# set context back to notebook (the default)
sns.set_context("notebook")
```

### Quiz: Scatterplots

What is the command to create a scatterplot in seaborn?

[[sns.relplot()]]
<script>
  let input = "@input".trim();
  /relplot/.test(input) || /regplot/.test(input);
</script>
***
<div class = "answer">
By default, the `relplot` command creates a scatterplot (although it can also be used to create [line plots](#line-plots)). You can also use `regplot` to create scatterplots, as we'll see in the [trend lines section](#trend-lines).

Note the `sns` before the function name. That's because we imported the seaborn library with an alias, as is conventional. See [making plots in seaborn](#making-plots-in-seaborn).
</div>
***

True or False: The only two crucial arguments to supply (in addition to providing the data) for a scatterplot are x and y.

[(X)] TRUE
[( )] FALSE
***
<div class = "answer">
While x and y are the only two **crucial** arguments for you to supply the plotting function, you may want to include others, such as hue and style, to communicate information about additional variables in the data.
</div>
***

## Histograms

Histograms show the distribution of a continuous variable. The values of the variable are shown along the x-axis, and data are grouped into bins, with the height of each bin corresponding to the number of data points in that bin. In other words, it communicates where your data for a given variable fall within its range. It is a great way to quickly assess for symmetry vs skew, outliers, and less common issues like multimodality.

We'll continue using the same data we explored to make scatter plots.

### Basic histogram

Because histograms show just one variable, the only aesthetic they require is x. The y-axis of the plot will just show the counts of observations in each bin on the x-axis. (Note that it is possible to provide `sns.displot` with y instead of x, in which case it will generate a sideways histogram.)

```python
sns.displot(covid_data, x="val_age")
```

![Histogram showing the distribution of age values.](media/seaborn_hist_1.png)


### Change the number of bins

The appearance of a histogram can change a lot depending on the number of bins you use along the x-axis. It's a good idea to try a few different sets of bins to see what works well for communicating this distribution.

```python
sns.displot(covid_data, x="val_age", binwidth=1)

```

![Histogram showing the distribution of ages with many narrow bins, each representing a single year.](media/seaborn_hist_2.png)

```python
sns.displot(covid_data, x="val_age", binwidth=10)
```

![Histogram showing the distribution of ages with eight wide bins, each representing a decade.](media/seaborn_hist_3.png)

### Using color to show groups

As with scatterplots, we can add information about an additional variable by using color. Let's put in the variable `is_smoker` for hue so we can see how the distribution of ages differs by smoking status.

Note that seaborn is continuing to use the color palette we set when we were making scatter plots (see [custom colors](#custom-colors)). If you want to change the color palette, you can do so at any time.

```python
sns.displot(covid_data, x="val_age", hue="is_smoker")

```

![Histogram showing the distribution of ages, with non-smokers in blue, smokers in orange, and ex-smokers in green, overlaid.](media/seaborn_hist_4.png)

You may be noticing that the distribution of non-smokers, which makes up the majority of the data, appears to be covering the other smaller groups. By default, seaborn plots each group as if they were each their own histogram, making each slightly translucent so you can see where distributions overlap. The height of each colored bar shows the count for that bin within that group.

That's often the most useful way to plot multiple histograms, but in this case, it makes it hard to see the smoker and ex-smoker distributions clearly because they fall completely within the non-smoker distribution.

You can control how `seaborn` plots the distributions with the `multiple` argument. To show stacked groups instead, use `multiple = "stack"`. This will put the three distributions one on top of the other, so the height of all three colors together in each bin corresponds to the total count across groups; the silhouette of this histogram will be identical to the original histogram without coloring by group.


```python
sns.displot(covid_data, x="val_age", hue="is_smoker", multiple="stack")
```

![Histogram showing the distribution of ages, with non-smokers in blue, smokers in orange, and ex-smokers in green, stacked.](media/seaborn_hist_5.png)

<div class = "options">
You can also use this same `displot` function to create [density plots](https://seaborn.pydata.org/tutorial/distributions.html#kernel-density-estimation) instead of histograms.
</div>

### Adding marginal histograms to other plots

Some times you may wish to show a distribution as context for another plot, such as a scatter plot. You can add marginal histograms to a bivariate plot with the `jointplot` function.

```python
sns.jointplot(data=covid_data, x="val_age", y="val_height_cm")
```

![Age and height scatterplot from the previous section on scatter plots, but with two small histograms added, one along the top showing the distribution of ages and another along the right edge showing the distribution of heights.](media/seaborn_hist_6.png)

By default, it plots x and y as a scatterplot, adding a marginal histogram for each.

<div class = "learnmore">
Learn more about a variety of ways to add marginal distribution information to plots in the [seaborn distributions tutorial](https://seaborn.pydata.org/tutorial/distributions.html#distribution-visualization-in-other-settings).
</div>

### Quiz: Histograms

Which of the following aesthetics can be used to plot a histogram using `displot`?

[( )] x only
[(X)] either x or y
[( )] y only
[( )] both x and y
****
<div class = "answer">
Histograms can only make use of one dimension of data (x or y, but never both) because the other dimension will always be the count of observations in each bin. If you try to provide variables for both x and y, `seaborn` will plot a [bivariate distribution heatmap](https://seaborn.pydata.org/tutorial/distributions.html#visualizing-bivariate-distributions) instead of a histogram.

In all of our examples, we used the x argument for our histograms, but it is possible to provide y instead. As an experiment, try generating one of the plots above, but substitute y for x and see what happens!
</div>
****

True or False: To show multiple histograms for different subgroups on a single plot (e.g. age distributions for smokers, non-smokers, and ex-smokers), use the `jointplot` function.

[( )] True
[(X)] False
****
<div class = "answer">
The `jointplot` function is for showing a bivariate plot with supplemental univariate distributions in the margins (for a review, see [adding marginal histograms to other plots](#adding-marginal-histograms-to-other-plots)).

To show histograms for two or more subgroups in a single plot, use the `hue` argument to color each subgroup separately (for a review, see [using color to show groups](#using-color-to-show-groups)).
</div>
****

True or False: When making histograms, the default binwidth in `seaborn` is probably the best choice for most data sets.

[( )] True
[(X)] False
****
<div class = "answer">
Not necessarily! The `seaborn` defaults are sensible, so that's often a good starting place, but it can be dangerous to accept the default bins without examining other options.  Changing the binwidth on a histogram can dramatically change the patterns highlighted in the data, so it's always a good idea to try multiple binwidths when you're making a histogram.

You can read more about this issue in the [seaborn distributions tutorial](https://seaborn.pydata.org/tutorial/distributions.html#choosing-the-bin-size).
</div>
****

## Line Plots

Line plots are especially useful when you want to show data points that are connected in a meaningful way. The most common application is repeated measures over time (also called time series data), such as when patients are measured on a given variable (plotted on the y-axis) at several times (plotted along the x-axis). Each line would represent one patient or a summary across a group of patients.

<div class = "important">
A word of caution: You may see line plots where the data points don't actually share a meaningful theoretical connection (e.g. all being from the same patient, or the same group). Although it's not uncommon, this is generally not considered good practice and you may receive pushback from reviewers or readers.
</div>

### Data for line plots

The data we've been using for the other examples so far doesn't lend itself well to line plots. Instead, for this example we'll use [one of the datasets included with the seaborn module](http://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset), called `fmri`. It contains the hemodynamic response (`signal`) at several timepoints for a number of subjects in response to two different events (`stim` and `cue`) in two brain regions (`parietal` and `frontal`).

This dataset is a special example dataset for `seaborn`, so you don't need to download it separately. You can call it with the `load_dataset` function (although you will need an internet connection for that to work).

```Python
fmri = sns.load_dataset("fmri")
```

### Basic line plot

```python
sns.relplot(x="timepoint", y="signal", kind="line", data=fmri)
```
![Basic line plot showing the strength of the FMRI signal over time, with timepoint on the x-axis and signal on the y-axis.](media/seaborn_line_1.png)

Note that by default `seaborn` aggregates across multiple observations at each time point, with a line at the mean and a 95% confidence interval shaded around it.

In this case, we have several different subjects, and from each we have readings from two brain regions and in response to two events, so there are many observations at each timepoint. If there were only a single observation for each timepoint (more typical of standard time series data), then `relplot` would show a line connecting those observations and no confidence interval.

### Using color and line type to show groups

If you want to show multiple lines on a single plot, you can achieve that by adding arguments for `hue` (controls color) and `style` (controls line type, like solid or dashed), as we did for scatter plots and histograms.

```python
sns.relplot(x="timepoint", y="signal", hue="event", style="event", kind="line", data=fmri)
```

![Line plot with timepoint on the x-axis and signal on the y-axis, and two lines: a solid blue line for event = stim and a dashed yellow line for event = cue.](media/seaborn_line_2.png)

### Using facets to compare plots

If you want to make more than one version of a similar plot, consider using facets.

In the current example, let's say we wanted to create two versions of the signal line plots for the two types of events: one showing the response in the parietal region, and one showing the response in the frontal region.

You can add facets to a `seaborn` plot by adding an argument for either `col` (for columns) or `row` (for rows) --- or both, if you want to show several different facets.

```python
sns.relplot(x="timepoint", y="signal", hue="event", style="event", col = "region", kind="line", data=fmri)
```

![Two side by side line plots with timepoint on the x-axis and signal on the y-axis. Each plot shows two lines: a solid blue line for the stim event and a dashed yellow line for the cue event. The plot on the left displays data collected from the parietal region of the brain, and the right plot is of data from the frontal region.](media/seaborn_line_3.png)

<div class = "learnmore">
For many more examples of line plots, see the [seaborn relplot tutorial section on line plots](https://seaborn.pydata.org/tutorial/relational.html#emphasizing-continuity-with-line-plots).
</div>

### Quiz: Line Plots

True or False: You can create both scatter plots and line plots with the same function in `seaborn`.

[(X)] TRUE
[( )] FALSE
****
<div class = "answer">
We used just one function, `relplot`, to make both scatter plots and line plots. Under the hood, there are actually two separate functions being used --- `scatterplot()` and `lineplot()`, which are equivalent to `relplot()` with `kind = "scatter"` (the default) and `kind = "line"`, respectively --- but it's nice to be able to stick to the higher-level `relplot` function for simplicity.

Because they're both called by the `relplot` function, you can use the same additional variables (e.g. `hue`, `style`, `col`) applied to either scatter or line plots, and they work in much the same way.
</div>
****

True or False: Line plots are appropriate in most situations in which a scatter plot would work, so you can general pick whichever one you prefer.

[( )] TRUE
[(X)] FALSE
****
<div class = "answer">
There are very few situations in which a scatter plot and line plot are equally appropriate.

Line plots emphasize continuity and because of that are rarely used except for with data that have some kind of time component. Scatter plots are much more flexible and can work to show the relationship between almost any two continuous variables.  
</div>
****

What argument do you add to include facets in a `seaborn` plot?

[[col, row]]
<script>
  let input = "@input".trim();
  /col|row/i.test(input);
</script>
****
<div class = "answer">
You can add facets to a plot by including the arguments for `col`, `row`, or both.
</div>
****

## Trend Lines

Trend lines look like line plots, but they are different in one key way: They show a **summary** of other data (usually a linear model), rather than plotting data directly.

Trend lines are used to show the overall trend in a scatterplot. Sometimes, the scatterplot points themselves are omitted and just the trend lines are shown to keep the visualization as clean as possible, but they're still implied.

### Linear regression trend lines

Because trend lines are such a useful visual summary, `seaborn` provides several options to add trend lines to your plots quickly and easily.

<div class = "options">
There are two very similar functions available for drawing trend lines: `regplot` and `lmplot`. For many use cases, they are close to identical. For simplicity, we'll stick to `lmplot` in this lesson. Try subbing in `regplot` instead and make note of how the plots differ.

For more background on `regplot` vs. `lmplot`, see [the seaborn regression tutorial](https://seaborn.pydata.org/tutorial/regression.html#controlling-the-size-and-shape-of-the-plot).
</div>

```python
sns.lmplot(data = covid_data,
            x="val_age", y="val_height_cm")
```

![Scatterplot with age on the x-axis and height on the y-axis, and a straight trend line running through the points, with a lighter shaded band around it.](media/seaborn_trend_1.png)

A couple things about this plot are not ideal:

1. Overplotting. The density of the scatter plot makes it hard to see the trend line as it runs through the bulk of the data.
2. The linear trend doesn't appear to be a very good description of the relationship between age and height. It systematically over-estimates height at the very young ages, then under-estimates through early adulthood and over-estimates again late in life.

We can address the first issue by adjusting alpha for the scatterplot to make the markers more transparent. Alpha ranges between 0 (totally transparent) and 1 (totally opaque).

<div class = "important">
Tip: When your data overlap too much on a plot, use alpha to make them more transparent.
</div>

We face a problem here, though: Since we're using a single function to draw both the scatter plot and the trend line, how do we adjust alpha for the scatter plot without affecting the line?

The solution is to pass additional arguments to the `matplotlib` functions on which `seaborn` is built.

Although `seaborn` is great at making many complex data visualizations smoothly and with very few lines of code, it sometimes lacks control of little details within those plots. It is built on top of the extremely powerful and flexible `matplotlib` library, however, so if you ever find yourself wanting more control of your `seaborn` visualizations, the answer is often to leverage the underlying `matplotlib` functions.

<div class = "care">
There is a much steeper learning curve for `matplotlib` compared to `seaborn`, however, and you may find you're happy with most `seaborn` plots without needing additional control --- don't bother with it if it feels too overwhelming. When you're ready to read more about `matplotlib`, start with their [introductory tutorials](https://matplotlib.org/stable/tutorials/index).
</div>

In this case, we can add an argument `scatter_kws` that passes additional "keyword arguments" to the `matplotlib` function drawing the scatter plot via a [python dictionary](https://www.w3schools.com/python/python_dictionaries.asp). There are [many possible keyword arguments](https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D) you can use, but we'll just set `alpha` here.

```Python
sns.lmplot(data = covid_data,
            x="val_age", y="val_height_cm",
           scatter_kws={"alpha": .1})
```

![The same scatter plot with trend line as above, but now the points of the scatterplot are much lighter, making the darker trend line easier to see on top of them.](media/seaborn_trend_2.png)

This solves the overplotting issue, but we still have the problem of the linear trend line not being a good fit for the data.

### Polynomial regression trend lines

One way to add more flexibility to a linear trend line is by adding [polynomial terms](https://www.theanalysisfactor.com/regression-modelshow-do-you-know-you-need-a-polynomial/) to the model. A second order polynomial model includes linear and quadratic terms, a third order polynomial model includes linear, quadratic, and cubic terms, and so on.

We'll try adding a quadratic term here, to see if it looks like a second order polynomial linear regression is a better description of the data.

```python
sns.lmplot(data = covid_data,
            x="val_age", y="val_height_cm",
           scatter_kws={"alpha": .1},
           order = 2)
```

![The scatter plot with age on the x-axis and height on the y-axis, but now the trend line drawn is a upside-down U shape, suggesting that the general trend is for height to increase with age until it reaches some maximum, at which point height begins decreasing.](media/seaborn_trend_3.png)

This appears to be a slight improvement on the linear regression model, especially at the youngest ages, but it is still systematically over-estimating height for young children and, because the quadratic trend follows a smooth arc shape, it predicts a drop in height at the older ages which is neither supported by the data nor sensible from a theoretical standpoint. A model that suggests height peaks around 40 years of age and then drops off dramatically does not make practical sense.

<div class = "warning">
As you add higher order polynomials, your regression line is allowed to follow more subtle patterns in the data, but interpretation gets much messier. It can be tempting to add higher and higher order polynomials until you achieve excellent model fit, but it's generally not advisable.

In general, polynomial models are a good choice when the polynomial relationship is **theoretically motivated**, which almost always means sticking to second or third order polynomials only.
</div>

### Lowess curve trend lines

If you want a high level of flexibility in your trend line, you can achieve that with much less complexity by switching to a non-parametric approach like [local regression](https://en.wikipedia.org/wiki/Local_regression), one example of which is lowess ("locally weighted scatterplot smoothing") curves.

<div class = "learnmore">
For a deeper understanding of what is meant by parametric vs. non-parametric models, see section 2.1.2 of the book [Statistical Learning](https://hastie.su.domains/ISLR2/ISLRv2_website.pdf).
</div>

```python
sns.lmplot(data = covid_data,
            x="val_age", y="val_height_cm",
           scatter_kws={"alpha": .1},
           lowess=True)
```

![The same scatter plot with age on the x-axis and height on the y-axis, but now the trend line drawn rises sharply from age 0 to 20 then levels off and is close to horizontal through the oldest ages.](media/seaborn_trend_4.png)

<div class = "learnmore">
There are several more options for kinds of trend lines to draw in `seaborn`, including [logistic regression trend lines and robust regression trend lines](https://seaborn.pydata.org/tutorial/regression.html#fitting-different-kinds-of-models).
</div>

### Quiz: Trend Lines

What function can you use to draw a scatterplot with trend line?

[[regplot, lmplot]]
<script>
  let input = "@input".trim();
  /regplot|lmplot/i.test(input);
</script>
****
Either `regplot` or `lmplot` can be used to draw scatter plots with trend lines.
****

Modify the code from the final example, the [lowess curve trend line](#lowess-curve-trend-lines), to separate out respondents by smoking status (`is_smoker`) with a separate facet for each.

```r  -Solution
sns.lmplot(data = covid_data,
            x="val_age", y="val_height_cm",
           scatter_kws={"alpha": .1},
           lowess=True,
           col = 'is_smoker')
```

Modify the code from the final example, the [lowess curve trend line](#lowess-curve-trend-lines), to get separate trend lines for each smoking status (`is_smoker`), but all shown together on single plot. (Hint: Use color to distinguish the groups.)

```r  -Solution
sns.lmplot(data = covid_data,
            x="val_age", y="val_height_cm",
           scatter_kws={"alpha": .1},
           lowess=True,
           hue = 'is_smoker')
```

## Additional Resources

The creator of `seaborn` [Michael Waskom](https://mwaskom.github.io/) maintains an [excellent website](https://seaborn.pydata.org/) with examples, explanations, tutorials, and more.

There are also many questions and answers about `seaborn` available on [stackoverflow](https://stackoverflow.com/questions/tagged/seaborn/) and [discourse](https://discourse.matplotlib.org/c/3rdparty/seaborn/21), so if you run into trouble that can be a good place to look for answers.

We have several interactive python data science notebooks available on google colab, some of which use `seaborn`. They all provide excellent opportunities to pratice data science skill in python:

- [Introduction to tabular .csv data with pandas](https://colab.research.google.com/github/arcus/education-materials/blob/master/tidy-csv-pandas/tidy-csv-pandas-full.ipynb)
- [Exploring diagnostic data with python](https://colab.research.google.com/github/arcus/education-materials/blob/master/data-analysis-with-pandas/01-exploring-diagnostic-data-with-pandas.ipynb)
- [Exploring data using pandas and seaborn](https://colab.research.google.com/github/arcus/education-materials/blob/master/explore-pandas-seaborn/explore-pandas-seaborn-full.ipynb)
- [Intro to machine learning, Part 1: Classification with Scikit-learn](https://colab.research.google.com/github/arcus/education-materials/blob/master/intro-to-ml/ml_workbook_00_intro.ipynb) (note, this pairs with an article on the Arcus Education team website: [What type of machine learning should I use?](https://education.arcus.chop.edu/types-of-ml/))
- [Intro to machine learning, Part 2: Validation, tuning, and model selection](https://colab.research.google.com/github/arcus/education-materials/blob/master/intro-to-ml/ml_workbook_01_validation_tuning.ipynb)
- [Intermediate machine learning](https://github.com/arcus/education-materials/tree/master/ml-intermediate) (scroll down to the README description for links to several interactive notebooks)
- [Network analysis and visualization with NetworkX](https://colab.research.google.com/github/arcus/education-materials/blob/master/network-viz/introduction.ipynb)

You may find the [pandas cheatsheet (pdf)](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) helpful.

To learn how to make plots in R using ggplot2, see [data visualization in ggplot2](https://liascript.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/data_visualization_in_ggplot2/data_visualization_ggplot2.md).

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Data+Visualizations+in+seaborn%22)!

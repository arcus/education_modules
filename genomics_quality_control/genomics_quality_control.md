<!--

author:   Rose Hartman
email:    hartmanr1@chop.edu
version:  1.0.0
current_version_description: Initial version.
module_type: standard
docs_version: 1.1.0
language: en
narrator: UK English Female
mode: Textbook

title: Genomics Tools and Methods: Quality Control

comment:  Get started with genomics! This module walks you through how to analyze FASTQ files to assess read quality, the first step in a common genomics workflow - identifying variants among sequencing samples taken from multiple individuals within a population (variant calling). 

long_description: This module uses command line tools to complete the first steps of genomics analysis using cloud computing. We'll look at real sequencing data from an *E. coli* experiment and walk through how to assess the quality of sequenced reads using FastQC. You'll learn about FASTQ files and how to analyze them. This module assumes some familiarity with bash; if you've worked through some bash training already, this is a great opportunity to practice those skills while getting hands-on experience with genomics.  

estimated_time_in_minutes: 40

@pre_reqs
This lesson assumes a working understanding of the bash shell, including the following commands: `ls`, `cd`, `mkdir`, `grep`, `less`, `cat`, `ssh`, `scp`, and `for` loops.
If you aren’t familiar with the bash shell, please review our [Command Line 101](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/bash_scripting_101/bash_scripting_101.md) module and/or the [Shell Genomics lesson by Data Carpentry](http://www.datacarpentry.org/shell-genomics/) before starting this lesson.

This lesson also assumes some familiarity with biological concepts (including the structure of DNA, nucleotide abbreviations, and the concept of genomic variation within a population) and genomics (concepts like sequencing). 
It does not assume any experience with genomics analysis. 
@end

@learning_objectives  
After completion of this module, learners will be able to:

- Explain how a FASTQ file encodes per-base quality scores.
- Interpret a FastQC plot summarizing per-base quality across all reads.
- Use `for` loops to automate operations on multiple files.
@end

good_first_module: false
data_domain: omics
coding_required: true
coding_level: intermediate
coding_language: bash

sequence_name: genomics_tools_and_methods

@sets_you_up_for

@end

@depends_on_knowledge_available_in

- bash_103_combining_commands
- bash_command_line_101
- bash_command_line_102
- bash_conditionals_loops
- data_storage_models
- directories_and_file_paths
- genomics_setup
- omics_orientation

@end

@version_history 

Previous versions: 
No previous versions.
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
import: https://raw.githubusercontent.com/arcus/education_modules/omics_tools_and_methods/_module_templates/macros_genomics.md
-->

# Genomics Tools and Methods: Quality Control

@overview

<div class = "gratitude">
<b style="color: rgb(var(--color-highlight));">Thank you!</b><br>

We are grateful to the team of authors and maintainers at [Data Carpentry](https://datacarpentry.org/) for creating their Genomics Workshop, from which this module content is lightly adapted, and generously sharing it under a [CC-BY license](https://github.com/datacarpentry/wrangling-genomics/blob/main/LICENSE.md): 

Josh Herr, Ming Tang, Lex Nederbragt, Fotis Psomopoulos (eds): "Data Carpentry: Wrangling Genomics Lesson."
Version 2017.11.0, November 2017,
[http://www.datacarpentry.org/wrangling-genomics/](http://www.datacarpentry.org/wrangling-genomics/),
doi: 10.5281/zenodo.1064254

</div>

## Lesson preparation

@lesson_prep_ami

## The data

We are going to use a long-term sequencing dataset from a population of *Escherichia coli*.

**What is *E. coli*?**

*E. coli* are rod-shaped bacteria that can survive under a wide variety of conditions including variable temperatures, nutrient availability, and oxygen levels. Most strains are harmless, but some are associated with food-poisoning.

![Escherichia coli: Scanning electron micrograph of Escherichia coli, grown in culture and adhered to a cover slip.](media/EscherichiaColi_NIAID.jpg "Credit: Rocky Mountain Laboratories, NIAID, NIH. [Public domain](https://commons.wikimedia.org/wiki/File:EscherichiaColi_NIAID.jpg?uselang=en#Licensing).")<!-- style = "max-width:200px; display: block; margin-left: auto;margin-right: auto;" -->

**Why is *E. coli* important?**

*E. coli* are one of the most well-studied model organisms in science. As a single-celled organism, *E. coli* reproduces rapidly, typically doubling its population every 20 minutes, which means it can be manipulated easily in experiments. In addition, most naturally occurring strains of *E. coli* are harmless. Most importantly, the genetics of *E. coli* are fairly well understood and can be manipulated to study adaptation and evolution.

### This dataset

The data we are going to use is part of a long-term evolution experiment led by [Richard Lenski](https://en.wikipedia.org/wiki/E._coli_long-term_evolution_experiment).

The experiment was designed to assess adaptation in *E. coli*. A population was propagated for more than 40,000 generations in a glucose-limited minimal medium (in most conditions glucose is the best carbon source for *E. coli*, providing faster growth than other sugars). This medium was supplemented with citrate, which *E. coli* cannot metabolize in the aerobic conditions of the experiment. 

Sequencing of the populations at regular time points revealed that spontaneous citrate-using variant (**Cit+**) appeared between 31,000 and 31,500 generations, causing an increase in population size and diversity. In addition, this experiment showed hypermutability in certain regions. Hypermutability is important and can help accelerate adaptation to novel environments, but also can be selected against in well-adapted populations.

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

To read more about the history of the experiment, see this paper [Blount et al. 2008: Historical contingency and the evolution of a key innovation in an experimental population of *Escherichia coli*](http://www.pnas.org/content/105/23/7899).

A timeline of the experiment from Wikipedia shows a history of major events (the timeline only shows to 2016, but note that the experiment is on-going): 

![*E. coli* long-term evolution experiment timeline from 1988 to 2016, with *E. coli* generations from 0 to 65,000. The **Cit+** variant does not appear until approximately 31,000 generations, more than a decade into the experiment.](media/LTEE_Timeline.png "Credit: [Zachary Blount](https://commons.wikimedia.org/wiki/User:Uncle_Zooey), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0).")<!-- style = "max-width:300px; display: block; margin-left: auto;margin-right: auto;" -->

</div>

### The metadata

We will be working with three sample events from the **Ara-3** strain of this experiment, one from 5,000 generations, one from 15,000 generations, and one from 50,000 generations.
The population changed substantially during the course of the experiment, and we will be exploring how (the evolution of a **Cit+** mutant and **hypermutability**) with our variant calling workflow.

The metadata file associated with this lesson can be [downloaded directly here](data/Ecoli_metadata_composite.csv) or [viewed in Github](https://github.com/datacarpentry/wrangling-genomics/blob/main/episodes/files/Ecoli_metadata_composite.csv). 

Open the metadata file and examine it now.

The metadata describes information on the *Ara-3* clones, and the columns represent:

| Column           | Description                                |
|------------------|--------------------------------------------|
| strain           | strain name					|
| generation       | generation when sample frozen		|
| clade            | based on parsimony-based tree		|
| reference        | study the samples were originally sequenced for				|
| population       | ancestral population group |
| mutator          | hypermutability mutant status |
| facility         | facility samples were sequenced at |
| run              | Sequence read archive sample ID		|
| read_type        | library type of reads |
| read_length      | length of reads in sample |
| sequencing_depth | depth of sequencing |
| cit              | citrate-using mutant status		|

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

If you would like to know details of how the file was created, you can look at [some notes and sources here](https://github.com/datacarpentry/wrangling-genomics/blob/main/episodes/files/Ecoli_metadata_composite_README.md).

</div>

### Quiz: The data

**Based on the metadata, answer the following questions:**

How many different generations exist in the data?

[[25]]
****
<div class = "answer">

If you look in the `generations` column of the metadata file, you'll see there are 25 unique values there. 

If you want to try doing this in bash for fun, check out [the `cut` command](https://stackoverflow.com/questions/4921879/getting-the-count-of-unique-values-in-a-column-in-bash) to get just the second column, and then [use `sort` and `uniq` to print just the unique values](https://stackoverflow.com/questions/618378/select-unique-or-distinct-values-from-a-list-in-unix-shell-script): 

```bash
cut -d "," -f 2 Ecoli_metadata_composite.csv | sort | uniq
```

Note that if you would rather just look at the metadata in spreadsheet software, like Excel, or using a tool like R or Python, that's perfectly fine! 
We're just providing a little extra bash practice here for those that want to try it.

</div>
****

How many citrate+ mutants have been recorded in **Ara-3**?

[[10]]
****
<div class = "answer">

Note that all of the samples here are from the **Ara-3** population, so we just need to look at the `cit` column. 
Look at the values in that column and you'll see there are 10 that say "plus", indicating that they have the **Cit+** mutation.

If you want to try this in bash, add the `-c` flag to the `uniq` command to get counts of each value. We want the 12th column (`cit`), so use `-f 12` instead of `-f 2` from before.

```bash
cut -d "," -f 12 Ecoli_metadata_composite.csv | sort | uniq -c
```

(You'll notice `cut` doesn't do well with the empty fields that are in some columns, which is why we end up with some extraneous numbers showing up.)

</div>
****

How many hypermutable mutants have been recorded in **Ara-3**?

[[6]]
****
<div class = "answer">

Note that all of the samples here are from the **Ara-3** population, so we just need to look at the `mutator` column (the 6th column). 
If you count down the values in that column, you'll see there are 6 "plus" values, meaning they are hypermutable.

```bash
cut -d "," -f 6 Ecoli_metadata_composite.csv | sort | uniq -c
```

</div>
****

## Bioinformatics workflows

When working with high-throughput sequencing data, the raw reads you get off of the sequencer will need to pass through a number of different tools in order to generate your final desired output.
The execution of this set of tools in a specified order is commonly referred to as a workflow or a pipeline.

An example of the workflow we will be using for our variant calling analysis is provided below with a brief description of each step.

![Typical variant calling workflow, description in text.](media/variant_calling_workflow.png)

1. Quality control - Assessing quality using FastQC
2. Quality control - Trimming and/or filtering reads (if necessary)
3. Align reads to reference genome
4. Perform post-alignment clean-up
5. Variant calling

These workflows in bioinformatics adopt a plug-and-play approach in that the output of one tool can be easily used as input to another tool without any extensive configuration.

**Having standards for data formats is what makes this feasible.**

Standards ensure that data is stored in a way that is generally accepted and agreed upon within the community.
The tools that are used to analyze data at different stages of the workflow are therefore built under the assumption that the data will be provided in a specific format.

## Starting with data

Often times, the first step in a bioinformatic workflow is getting the data you want to work with onto a computer where you can work with it.
If you have outsourced sequencing of your data, the sequencing center will usually provide you with a link that you can use to download your data.
For this lesson, we will be working with publicly available sequencing data.

We are studying a population of Escherichia coli (designated Ara-3), which were propagated for more than 50,000 generations in a glucose-limited minimal medium.
We will be working with three samples from this experiment, one from 5,000 generations, one from 15,000 generations, and one from 50,000 generations.
The population changed substantially during the course of the experiment, and we will be exploring how with our variant calling workflow.

The data are paired-end, so we will download two files for each sample.
We will use the [European Nucleotide Archive](https://www.ebi.ac.uk/ena) to get our data.
The ENA “provides a comprehensive record of the world’s nucleotide sequencing information, covering raw sequencing data, sequence assembly information and functional annotation.”
The ENA also provides sequencing data in the fastq format, an important format for sequencing reads that we will be learning about today.

To download the data, run the commands below.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Here we are using the `-p` option for `mkdir`. This option allows `mkdir` to create the new directory, even if one of the parent directories does not already exist.
It also suppresses errors if the directory already exists, without overwriting that directory.

</div>

It will take about 15 minutes to download the files.

```bash
mkdir -p ~/genomics_tools_and_methods/data/untrimmed_fastq/
cd ~/genomics_tools_and_methods/data/untrimmed_fastq

curl -O ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR258/004/SRR2589044/SRR2589044_1.fastq.gz
curl -O ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR258/004/SRR2589044/SRR2589044_2.fastq.gz
curl -O ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR258/003/SRR2584863/SRR2584863_1.fastq.gz
curl -O ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR258/003/SRR2584863/SRR2584863_2.fastq.gz
curl -O ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR258/006/SRR2584866/SRR2584866_1.fastq.gz
curl -O ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR258/006/SRR2584866/SRR2584866_2.fastq.gz
```

The data comes in a compressed format, which is why there is a `.gz` at the end of the file names. 
This makes it faster to transfer, and allows it to take up less space on our computer. 
Let’s unzip one of the files so that we can look at the fastq format.

```bash
gunzip SRR2584863_1.fastq.gz
```

## Quality control

We will now assess the quality of the sequence reads contained in our fastq files.

![Variant calling workflow from above, showing just the first two steps, which are quality control.](media/var_calling_workflow_qc.png)

## Details on the FASTQ format

Although it looks complicated (and it is), we can understand the [fastq](https://en.wikipedia.org/wiki/FASTQ_format) format with a little decoding. Some rules about the format include...

|Line|Description|
|----|-----------|
|1|Always begins with '@' and then information about the read|
|2|The actual DNA sequence|
|3|Always begins with a '+' and sometimes the same info in line 1|
|4|Has a string of characters which represent the quality scores; must have same number of characters as line 2|

## Quality scores

We can view the first complete read in one of the files our dataset by using `head` to look at
the first four lines.

```bash
head -n 4 SRR2584863_1.fastq
```

``` +output
@SRR2584863.1 HWI-ST957:244:H73TDADXX:1:1101:4712:2181/1
TTCACATCCTGACCATTCAGTTGAGCAAAATAGTTCTTCAGTGCCTGTTTAACCGAGTCACGCAGGGGTTTTTGGGTTACCTGATCCTGAGAGTTAACGGTAGAAACGGTCAGTACGTCAGAATTTACGCGTTGTTCGAACATAGTTCTG
+
CCCFFFFFGHHHHJIJJJJIJJJIIJJJJIIIJJGFIIIJEDDFEGGJIFHHJIJJDECCGGEGIIJFHFFFACD:BBBDDACCCCAA@@CA@C>C3>@5(8&>C:9?8+89<4(:83825C(:A#########################
```

Line 4 shows the quality for each nucleotide in the read.
Quality is interpreted as the
probability of an incorrect base call (e.g. 1 in 10) or, equivalently, the base call
accuracy (e.g. 90%).
To make it possible to line up each individual nucleotide with its quality
score, the numerical score is converted into a code where each individual character
represents the numerical quality score for an individual nucleotide.

For example, in the output above, the quality score line is:

``` +output
CCCFFFFFGHHHHJIJJJJIJJJIIJJJJIIIJJGFIIIJEDDFEGGJIFHHJIJJDECCGGEGIIJFHFFFACD:BBBDDACCCCAA@@CA@C>C3>@5(8&>C:9?8+89<4(:83825C(:A#########################
```

The numerical value assigned to each of these characters depends on the
sequencing platform that generated the reads.

The sequencing machine used to generate our data
uses the standard Sanger quality PHRED score encoding, using by Illumina version 1.8 onwards.
Each character is assigned a quality score between 0 and 40 as shown in the chart below.

```
Quality encoding: !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHI
                  |         |         |         |         |
Quality score:    0........10........20........30........40
```

Each quality score represents the probability that the corresponding nucleotide call is
incorrect.
This quality score is logarithmically based, so a quality score of 10 reflects a base call accuracy of 90%, but a quality score of 20 reflects a base call accuracy of 99%.
These probability values are the results from the base calling algorithm and dependent on how much signal was captured for the base incorporation.

Looking back at our read:

``` +output
@SRR2584863.1 HWI-ST957:244:H73TDADXX:1:1101:4712:2181/1
TTCACATCCTGACCATTCAGTTGAGCAAAATAGTTCTTCAGTGCCTGTTTAACCGAGTCACGCAGGGGTTTTTGGGTTACCTGATCCTGAGAGTTAACGGTAGAAACGGTCAGTACGTCAGAATTTACGCGTTGTTCGAACATAGTTCTG
+
CCCFFFFFGHHHHJIJJJJIJJJIIJJJJIIIJJGFIIIJEDDFEGGJIFHHJIJJDECCGGEGIIJFHFFFACD:BBBDDACCCCAA@@CA@C>C3>@5(8&>C:9?8+89<4(:83825C(:A#########################
```

We can now see that there are a range of quality scores, but that the end of the sequence is
very poor (`#` = a quality score of 2).

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

Although we have used a particular quality encoding system to demonstrate interpretation of read quality, different sequencing machines use different encoding systems.
This means that, depending on which sequencer you use to generate your data, a `#` may not be an indicator of a poor quality base call.

This mainly relates to older Solexa/Illumina data, but it is essential that you know which sequencing platform was used to generate your data, so that you can tell your quality control program which encoding to use.
If you choose the wrong encoding, you run the risk of throwing away good reads or (even worse) not throwing away bad reads!

</div>

### Quiz: Quality scores

Use `tail -n 4 SRR2584863_1.fastq` to view the last read in the `SRR2584863_1.fastq` file.
How does the quality of this read compare to the quality of the first read, examined above?

[( )] The first read seems to be higher quality
[( )] The first and last reads appear to be similar in quality
[(X)] The last read seems to be higher quality
****
<div class = "answer">

Here is the output you should see when running the above command:

``` +output
@SRR2584863.1553259 HWI-ST957:245:H73R4ADXX:2:2216:21048:100894/1
CTGCAATACCACGCTGATCTTTCACATGATGTAAGAAAAGTGGGATCAGCAAACCGGGTGCTGCTGTGGCTAGTTGCAGCAAACCATGCAGTGAACCCGCCTGTGCTTCGCTATAGCCGTGACTGATGAGGATCGCCGGAAGCCAGCCAA
+
CCCFFFFFHHHHGJJJJJJJJJHGIJJJIJJJJIJJJJIIIIJJJJJJJJJJJJJIIJJJHHHHHFFFFFEEEEEDDDDDDDDDDDDDDDDDCDEDDBDBDDBDDDDDDDDDBDEEDDDD7@BDDDDDD>AA>?B?<@BDD@BDC?BDA?
```

This read has more consistent quality at its end than the first read that we looked at, but still has a range of quality scores, most of them high.
We will look at variations in position-based quality in the next section.

</div>
****

## Check FastQC installation

Before proceeding, lets validate that all the relevant tools are installed by running `fastqc -h`.
If it is correctly installed, you should see the help file:

``` +output
FastQC - A high throughput sequence QC analysis tool

SYNOPSIS

fastqc seqfile1 seqfile2 .. seqfileN

fastqc [-o output dir] [--(no)extract] [-f fastq|bam|sam]
[-c contaminant file] seqfile1 .. seqfileN

DESCRIPTION

FastQC reads a set of sequence files and produces from each one a quality

(truncated)
```

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

If `fastqc` is not installed, then you would expect to see an error like

``` +output
The program 'fastqc' is currently not installed. You can install it by typing:
sudo apt-get install fastqc
```

If `fastqc` is not installed, see the [installation instructions for your operating system](https://raw.githubusercontent.com/s-andrews/FastQC/master/INSTALL.txt).
Note that if you're using the Data Carpentry AMI, then everything should already be installed for you.

</div>

## Assessing quality using FastQC

In real life, you won't be assessing the quality of your reads by visually inspecting your FASTQ files.
Rather, you'll be using a software program to assess read quality and filter out poor quality reads.
We'll first use a program called [FastQC](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/) to visualize the quality of our reads.
Later in our workflow, we'll use another program to filter out poor quality reads.

FastQC has a number of features which can give you a quick impression of any problems your data may have, so you can take these issues into consideration before moving forward with your analyses.
Rather than looking at quality scores for each individual read, FastQC looks at quality collectively across all reads within a sample.
The image below shows one FastQC-generated plot that indicates a very high quality sample:

![Boxplots of quality scores (y-axis) by position in read (x-axis), with all read positions clustered at the high end of the quality scale.](media/good_quality1.8.png)

The x-axis displays the base position in the read, and the y-axis shows quality scores.
In this example, the sample contains reads that are 40 bp long.
This is much shorter than the reads we are working with in our workflow.
For each position, there is a box-and-whisker plot showing the distribution of quality scores for all reads at that position.
The horizontal red line indicates the median quality score and the yellow box shows the 2nd to 3rd quartile range.
This means that 50% of reads have a quality score that falls within the range of the yellow box at that position.
The whiskers show the range to the 1st and 4th  quartile.

For each position in this sample, the quality values do not drop much lower than 32.
This is a high quality score.
The plot background is also color-coded to identify good (green),
acceptable (yellow), and bad (red) quality scores.

Now let's take a look at a quality plot on the other end of the spectrum.

![Boxplot of quality scores (y-axis) by position in read (x-axis), but for this read only about the first half of the read shows quality scores in the good range, with later positions showing much larger ranges in quality and lower scores overall.](media/bad_quality1.8.png)

Here, we see positions within the read in which the boxes span a much wider range.
Also, quality scores drop quite low into the "bad" range, particularly on the tail end of the reads.
The FastQC tool produces several other diagnostic plots to assess sample quality, in addition to the one plotted above.

### Running FastQC  

We will now assess the quality of the reads that we downloaded. First, make sure you're still in the `untrimmed_fastq` directory:

```bash
cd ~/genomics_tools_and_methods/data/untrimmed_fastq/
```

How big are the files?

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

Hint: Look at the options for the `ls` command to see how to show file sizes.

</div>

```bash
ls -l -h
```

``` +output
-rw-rw-r-- 1 dcuser dcuser 545M Jul  6 20:27 SRR2584863_1.fastq
-rw-rw-r-- 1 dcuser dcuser 183M Jul  6 20:29 SRR2584863_2.fastq.gz
-rw-rw-r-- 1 dcuser dcuser 309M Jul  6 20:34 SRR2584866_1.fastq.gz
-rw-rw-r-- 1 dcuser dcuser 296M Jul  6 20:37 SRR2584866_2.fastq.gz
-rw-rw-r-- 1 dcuser dcuser 124M Jul  6 20:22 SRR2589044_1.fastq.gz
-rw-rw-r-- 1 dcuser dcuser 128M Jul  6 20:24 SRR2589044_2.fastq.gz
```

There are six FASTQ files ranging from 124M (124MB) to 545M.

FastQC can accept multiple file names as input, and on both zipped and unzipped files,
so we can use the `*.fastq*` wildcard to run FastQC on all of the FASTQ files in this directory.

```bash
fastqc *.fastq*
```

You will see an automatically updating output message telling you the progress of the analysis. It will start like this:

``` +output
Started analysis of SRR2584863_1.fastq
Approx 5% complete for SRR2584863_1.fastq
Approx 10% complete for SRR2584863_1.fastq
Approx 15% complete for SRR2584863_1.fastq
Approx 20% complete for SRR2584863_1.fastq
Approx 25% complete for SRR2584863_1.fastq
```

In total, it should take about five minutes for FastQC to run on all six of our FASTQ files.
When the analysis completes, your prompt (`$`) will return.
So your screen will look something like this:

``` +output
Approx 80% complete for SRR2589044_2.fastq.gz
Approx 85% complete for SRR2589044_2.fastq.gz
Approx 90% complete for SRR2589044_2.fastq.gz
Approx 95% complete for SRR2589044_2.fastq.gz
Analysis complete for SRR2589044_2.fastq.gz
$
```

The FastQC program has created several new files within our `data/untrimmed_fastq/` directory.

```bash
ls
```

``` +output
SRR2584863_1.fastq        SRR2584866_1_fastqc.html  SRR2589044_1_fastqc.html
SRR2584863_1_fastqc.html  SRR2584866_1_fastqc.zip   SRR2589044_1_fastqc.zip
SRR2584863_1_fastqc.zip   SRR2584866_1.fastq.gz     SRR2589044_1.fastq.gz
SRR2584863_2_fastqc.html  SRR2584866_2_fastqc.html  SRR2589044_2_fastqc.html
SRR2584863_2_fastqc.zip   SRR2584866_2_fastqc.zip   SRR2589044_2_fastqc.zip
SRR2584863_2.fastq.gz     SRR2584866_2.fastq.gz     SRR2589044_2.fastq.gz
```
For each input FASTQ file, FastQC has created a `.zip` file and a
`.html` file.
The `.zip` file extension indicates that this is actually a compressed set of multiple output files.
We'll be working with these output files soon.
The `.html` file is a stable webpage displaying the summary report for each of our samples.

We want to keep our data files and our results files separate,
so we will move these output files into a new directory within our `results/` directory.

```bash
mkdir -p ~/genomics_tools_and_methods/results/fastqc_untrimmed_reads
mv *.zip ~/genomics_tools_and_methods/results/fastqc_untrimmed_reads/
mv *.html ~/genomics_tools_and_methods/results/fastqc_untrimmed_reads/
```

Now we can navigate into this results directory and do some closer inspection of our output files.

```bash
cd ~/genomics_tools_and_methods/results/fastqc_untrimmed_reads/
```

### Viewing the FastQC results

If we were working on our local computers, we would be able to look at each of these HTML files by opening them in a web browser.

However, these files are currently sitting on our remote AWS instance, where our local computer can not see them. And, since we are only logging into the AWS instance via the command line - it does not have any web browser setup to display these files either.

So the easiest way to look at these webpage summary reports will be to transfer them to our local computers (i.e. your laptop).

To transfer a file from a remote server to our own machines, we will use `scp`.

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

For a review of `scp`, see the section on [transferring data between your local machine and the cloud](https://datacarpentry.org/shell-genomics/05-writing-scripts.html#transferring-data-between-your-local-machine-and-the-cloud) from the Data Carpentry Shell Genomics lesson.

</div>

First we will make a new directory on our computer to store the HTML files we are transferring.
Let’s put it on our desktop for now.
Open a new tab in your terminal program (you can use the pull down menu at the top of your screen or the Cmd+t keyboard shortcut) and type:

```bash
scp dcuser@ec2-34-238-162-94.compute-1.amazonaws.com:~/genomics_tools_and_methods/results/fastqc_untrimmed_reads/*.html ~/Desktop/fastqc_html
```

As a reminder, the first part
of the command `dcuser@ec2-34-238-162-94.compute-1.amazonaws.com` is
the address for your remote computer. Make sure you replace everything
after `dcuser@` with your instance number (the one you used to log in).

The second part starts with a `:` and then gives the absolute path
of the files you want to transfer from your remote computer. Don't
forget the `:`. We used a wildcard (`*.html`) to indicate that we want all of
the HTML files.

The third part of the command gives the absolute path of the location
you want to put the files. This is on your local computer and is the
directory we just created `~/Desktop/fastqc_html`.

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

**Note on using zsh**:
If you are using zsh instead of bash (macOS for example changed the default recently to zsh), it is likely that a no matches found error will be displayed.
The reason for this is that the wildcard ("*") is not correctly interpreted. To fix this problem the wildcard needs to be escaped with a "\":

```bash
scp dcuser@ec2-34-238-162-94.compute-1.amazonaws.com:~/genomics_tools_and_methods/results/fastqc_untrimmed_reads/\*.html ~/Desktop/fastqc_html
```

Alternatively, you can put the whole path into quotation marks:

```bash
scp "dcuser@ec2-34-238-162-94.compute-1.amazonaws.com:~/genomics_tools_and_methods/results/fastqc_untrimmed_reads/*.html" ~/Desktop/fastqc_html
```

</div>

You should see a status output like this:

``` +output
SRR2584863_1_fastqc.html                      100%  249KB 152.3KB/s   00:01    
SRR2584863_2_fastqc.html                      100%  254KB 219.8KB/s   00:01    
SRR2584866_1_fastqc.html                      100%  254KB 271.8KB/s   00:00    
SRR2584866_2_fastqc.html                      100%  251KB 252.8KB/s   00:00    
SRR2589044_1_fastqc.html                      100%  249KB 370.1KB/s   00:00    
SRR2589044_2_fastqc.html                      100%  251KB 592.2KB/s   00:00
```

Now we can go to our new directory and open the 6 HTML files.

Depending on your system, you should be able to select and open them all at once via a right click menu in your file browser.

### Quiz: FastQC

Take a look at your samples. Which sample(s) looks the best in terms of per base sequence quality? Which sample(s) look the worst?

[[describe sample quality]]
<script>
  let input = "@input".trim();
  /.*/i.test(input);
</script>
***
<div class = "answer">

(Note that we can't automatically grade an open-ended question like this, so it will be marked "correct" no matter what you write.)

All of the reads contain usable data, but the quality decreases toward the end of the reads.

</div>
***

## Decoding the other FastQC outputs

We have now looked at quite a few "Per base sequence quality" FastQC graphs, but there are nine other graphs that we have not talked about!
Below we have provided a brief overview of interpretations for each of these plots.
For more information, please see the FastQC documentation [here](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/)

- [**Per tile sequence quality**](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/3%20Analysis%20Modules/12%20Per%20Tile%20Sequence%20Quality.html): the machines that perform sequencing are divided into tiles. This plot displays patterns in base quality along these tiles. Consistently low scores are often found around the edges, but hot spots can also occur in the middle if an air bubble was introduced at some point during the run.
- [**Per sequence quality scores**](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/3%20Analysis%20Modules/3%20Per%20Sequence%20Quality%20Scores.html): a density plot of quality for all reads at all positions. This plot shows what quality scores are most common.
- [**Per base sequence content**](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/3%20Analysis%20Modules/4%20Per%20Base%20Sequence%20Content.html): plots the proportion of each base position over all of the reads. Typically, we expect to see each base roughly 25% of the time at each position, but this often fails at the beginning or end of the read due to quality or adapter content.
- [**Per sequence GC content**](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/3%20Analysis%20Modules/5%20Per%20Sequence%20GC%20Content.html): a density plot of average GC content in each of the reads.
- [**Per base N content**](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/3%20Analysis%20Modules/6%20Per%20Base%20N%20Content.html): the percent of times that 'N' occurs at a position in all reads. If there is an increase at a particular position, this might indicate that something went wrong during sequencing.
- [**Sequence Length Distribution**](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/3%20Analysis%20Modules/7%20Sequence%20Length%20Distribution.html): the distribution of sequence lengths of all reads in the file. If the data is raw, there is often on sharp peak, however if the reads have been trimmed, there may be a distribution of shorter lengths.
- [**Sequence Duplication Levels**](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/3%20Analysis%20Modules/8%20Duplicate%20Sequences.html): A distribution of duplicated sequences. In sequencing, we expect most reads to only occur once. If some sequences are occurring more than once, it might indicate enrichment bias (e.g. from PCR). If the samples are high coverage (or RNA-seq or amplicon), this might not be true.
- [**Overrepresented sequences**](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/3%20Analysis%20Modules/9%20Overrepresented%20Sequences.html): A list of sequences that occur more frequently than would be expected by chance.
- [**Adapter Content**](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/3%20Analysis%20Modules/10%20Adapter%20Content.html): a graph indicating where adapater sequences occur in the reads.
- [**K-mer Content**](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/3%20Analysis%20Modules/11%20Kmer%20Content.html): a graph showing any sequences which may show a positional bias within the reads.

### Working with the FastQC text output

Now that we have looked at our HTML reports to get a feel for the data, let's look more closely at the other output files.
Go back to the tab in your terminal program that is connected to your AWS instance (the tab label will start with `dcuser@ip`) and make sure you are in our results subdirectory.   

```bash
cd ~/genomics_tools_and_methods/results/fastqc_untrimmed_reads/
ls
```

``` +output
SRR2584863_1_fastqc.html  SRR2584866_1_fastqc.html  SRR2589044_1_fastqc.html
SRR2584863_1_fastqc.zip   SRR2584866_1_fastqc.zip   SRR2589044_1_fastqc.zip
SRR2584863_2_fastqc.html  SRR2584866_2_fastqc.html  SRR2589044_2_fastqc.html
SRR2584863_2_fastqc.zip   SRR2584866_2_fastqc.zip   SRR2589044_2_fastqc.zip
```

Our `.zip` files are compressed files.
They each contain multiple different types of output files for a single input FASTQ file.
To view the contents of a `.zip` file, we can use the program `unzip` to decompress these files.
Let's try doing them all at once using a
wildcard.

```bash
unzip *.zip
```

``` +output
Archive:  SRR2584863_1_fastqc.zip
caution: filename not matched:  SRR2584863_2_fastqc.zip
caution: filename not matched:  SRR2584866_1_fastqc.zip
caution: filename not matched:  SRR2584866_2_fastqc.zip
caution: filename not matched:  SRR2589044_1_fastqc.zip
caution: filename not matched:  SRR2589044_2_fastqc.zip
```

This did not work.
We unzipped the first file and then got a warning message for each of the other `.zip` files.
This is because `unzip` expects to get only one zip file as input.
We could go through and unzip each file one at a time, but this is very time consuming and error-prone.
Someday you may have 500 files to unzip!

A more efficient way is to use a `for` loop lesson to iterate through all of our `.zip` files.

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

For a refresher on how to write `for` loops, see the section on [writing for loops in the Data Carpentry Shell Genomics lesson](https://datacarpentry.org/shell-genomics/04-redirection.html#writing-for-loops).

</div>

Let's see what that looks like and then we will  discuss what we are doing with each line of our loop.

```bash
for filename in *.zip
do
unzip $filename
done
```

In this example, the input is six filenames (one filename for each of our `.zip` files).
Each time the loop iterates, it will assign a file name to the variable `filename` and run the `unzip` command.
The first time through the loop,
`$filename` is `SRR2584863_1_fastqc.zip`.
The interpreter runs the command `unzip` on `SRR2584863_1_fastqc.zip`.
For the second iteration, `$filename` becomes
`SRR2584863_2_fastqc.zip`. This time, the shell runs `unzip` on `SRR2584863_2_fastqc.zip`.
It then repeats this process for the four other `.zip` files in our directory.

When we run our `for` loop, you will see output that starts like this:

``` +output
Archive:  SRR2589044_2_fastqc.zip
   creating: SRR2589044_2_fastqc/
   creating: SRR2589044_2_fastqc/Icons/
   creating: SRR2589044_2_fastqc/Images/
  inflating: SRR2589044_2_fastqc/Icons/fastqc_icon.png
  inflating: SRR2589044_2_fastqc/Icons/warning.png
  inflating: SRR2589044_2_fastqc/Icons/error.png
  inflating: SRR2589044_2_fastqc/Icons/tick.png
  inflating: SRR2589044_2_fastqc/summary.txt
  inflating: SRR2589044_2_fastqc/Images/per_base_quality.png
  inflating: SRR2589044_2_fastqc/Images/per_tile_quality.png
  inflating: SRR2589044_2_fastqc/Images/per_sequence_quality.png
  inflating: SRR2589044_2_fastqc/Images/per_base_sequence_content.png
  inflating: SRR2589044_2_fastqc/Images/per_sequence_gc_content.png
  inflating: SRR2589044_2_fastqc/Images/per_base_n_content.png
  inflating: SRR2589044_2_fastqc/Images/sequence_length_distribution.png
  inflating: SRR2589044_2_fastqc/Images/duplication_levels.png
  inflating: SRR2589044_2_fastqc/Images/adapter_content.png
  inflating: SRR2589044_2_fastqc/fastqc_report.html
  inflating: SRR2589044_2_fastqc/fastqc_data.txt
  inflating: SRR2589044_2_fastqc/fastqc.fo
```

The `unzip` program is decompressing the `.zip` files and creating a new directory (with subdirectories) for each of our samples,
to store all of the different output that is produced by FastQC.
There are a lot of files here.
The one we are going to focus on is the `summary.txt` file.

If you list the files in our directory now you will see:

``` +output
SRR2584863_1_fastqc       SRR2584866_1_fastqc       SRR2589044_1_fastqc
SRR2584863_1_fastqc.html  SRR2584866_1_fastqc.html  SRR2589044_1_fastqc.html
SRR2584863_1_fastqc.zip   SRR2584866_1_fastqc.zip   SRR2589044_1_fastqc.zip
SRR2584863_2_fastqc       SRR2584866_2_fastqc       SRR2589044_2_fastqc
SRR2584863_2_fastqc.html  SRR2584866_2_fastqc.html  SRR2589044_2_fastqc.html
SRR2584863_2_fastqc.zip   SRR2584866_2_fastqc.zip   SRR2589044_2_fastqc.zip
```

The `.html` files and the uncompressed `.zip` files are still present,
but now we also have a new directory for each of our samples.
We can see for sure that it is a directory if we use the `-F` flag for `ls`.

```bash
ls -F
```

``` +output
SRR2584863_1_fastqc/      SRR2584866_1_fastqc/      SRR2589044_1_fastqc/
SRR2584863_1_fastqc.html  SRR2584866_1_fastqc.html  SRR2589044_1_fastqc.html
SRR2584863_1_fastqc.zip   SRR2584866_1_fastqc.zip   SRR2589044_1_fastqc.zip
SRR2584863_2_fastqc/      SRR2584866_2_fastqc/      SRR2589044_2_fastqc/
SRR2584863_2_fastqc.html  SRR2584866_2_fastqc.html  SRR2589044_2_fastqc.html
SRR2584863_2_fastqc.zip   SRR2584866_2_fastqc.zip   SRR2589044_2_fastqc.zip
```

Let's see what files are present within one of these output directories.

```bash
ls -F SRR2584863_1_fastqc/
```

``` +output
fastqc_data.txt  fastqc.fo  fastqc_report.html	Icons/	Images/  summary.txt
```

Use `less` to preview the `summary.txt` file for this sample.

```bash
less SRR2584863_1_fastqc/summary.txt
```

``` +output
PASS    Basic Statistics        SRR2584863_1.fastq
PASS    Per base sequence quality       SRR2584863_1.fastq
PASS    Per tile sequence quality       SRR2584863_1.fastq
PASS    Per sequence quality scores     SRR2584863_1.fastq
WARN    Per base sequence content       SRR2584863_1.fastq
WARN    Per sequence GC content SRR2584863_1.fastq
PASS    Per base N content      SRR2584863_1.fastq
PASS    Sequence Length Distribution    SRR2584863_1.fastq
PASS    Sequence Duplication Levels     SRR2584863_1.fastq
PASS    Overrepresented sequences       SRR2584863_1.fastq
WARN    Adapter Content SRR2584863_1.fastq
```

The summary file gives us a list of tests that FastQC ran, and tells
us whether this sample passed, failed, or is borderline (`WARN`). 

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

Remember, to quit from `less` you must type `q`.

</div>

### Documenting our work

We can make a record of the results we obtained for all our samples by concatenating all of our `summary.txt` files into a single file using the `cat` command.
We will call this `fastqc_summaries.txt` and move it to `~/genomics_tools_and_methods/docs`.

```bash
cat */summary.txt > ~/genomics_tools_and_methods/docs/fastqc_summaries.txt
```

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

**Same symbols, different meanings**

As you work through this code, you will see `>` being used as a shell prompt, but `>` is also used to redirect output. Similarly, `$` is used as a shell prompt, but, as we saw earlier, it is also used to ask the shell to get the value of a variable.

If the shell prints `>` or `$` then it expects you to type something, and the symbol is a prompt.

If you type `>` or `$` yourself, it is an instruction from you that the shell should redirect output or get the value of a variable.

</div>

### Quiz: Additional FastQC tests

What command would you use to see which samples failed at least one of FastQC's quality tests, and what test(s) those samples failed?

[[grep FAIL fastqc_summaries.txt]]
[[?]] Hint: Try using `grep`.
***
<div class = "answer">

We can get the list of all failed tests using `grep`.
For a review of `grep` and how to use it, see the section on [searching files in the Shell Genomics lesson by Data Carpentries](https://datacarpentry.org/shell-genomics/04-redirection/index.html#searching-files).

First, make sure you're in the correct directory:

```bash
cd ~/genomics_tools_and_methods/docs
```

Then use `grep` to return every line that includes the phrase "FAIL" within the file `fastqc_summaries.txt`.
This will be all the failing tests.

```bash
grep FAIL fastqc_summaries.txt
```

``` +output
FAIL    Per base sequence quality       SRR2584863_2.fastq.gz
FAIL    Per tile sequence quality       SRR2584863_2.fastq.gz
FAIL    Per base sequence content       SRR2584863_2.fastq.gz
FAIL    Per base sequence quality       SRR2584866_1.fastq.gz
FAIL    Per base sequence content       SRR2584866_1.fastq.gz
FAIL    Adapter Content SRR2584866_1.fastq.gz
FAIL    Adapter Content SRR2584866_2.fastq.gz
FAIL    Adapter Content SRR2589044_1.fastq.gz
FAIL    Per base sequence quality       SRR2589044_2.fastq.gz
FAIL    Per tile sequence quality       SRR2589044_2.fastq.gz
FAIL    Per base sequence content       SRR2589044_2.fastq.gz
FAIL    Adapter Content SRR2589044_2.fastq.gz
```

</div>
***

## Terminate your instance

@aws_billing_reminder

## Additional Resources

## Feedback

@feedback

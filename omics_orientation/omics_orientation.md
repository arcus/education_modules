<!--

author:   Meredith Lee
email:    leemc@chop.edu
version:  1.0.1
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Omics Orientation
comment: This module provides a brief introduction to omics and its associated fields.
long_description: Omics is a wide-reaching field, with many different subfields. This module aims to disambiguate several omics-related terms and topics, discuss some of the most popular omics research fields, and examine the challenges of and caveats for omics research.
estimated_time: 15m

@learning_objectives

After completion of this module, learners will be able to:

- Define what omics is and explain why a researcher might choose an omics approach
- Identify several popular omics domains
- Describe some challenges and caveats of omics research


@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Omics Orientation


<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites:** None

**Learning Objectives**

@learning_objectives


</div>


## What is Omics?

"**Omics**" (pronounced OH-micks) is a suffix added to a large number of biological disciplines which denotes a "comprehensive, or global, assessment of a set of molecules" (Hasin et al., 2017) related to that domain.  Genomics is possibly the most well-known member of this family of disciplines, but is certainly not the only one! Omics has become something of a buzzword in recent years with the improvement of high-throughput technologies and increased ability to analyze large amounts of data.

<div class = "learnmore">
Much of the content of this module, particularly the definitions of specific omics domains, was derived from an article by Hasin *et al.* published in the journal *Genome Biology*. The citation is below and the article is open source if you are interesting in reading more about this topic.

<div style = "margin-left: 40px; text-indent: -40px; font-size:0.8em;">

Hasin, Y., Seldin, M. & Lusis, A. Multi-omics approaches to disease. Genome Biol 18, 83 (2017). https://doi.org/10.1186/s13059-017-1215-1

</div>

</div>

### Why study omics?

While studying single molecules or genetic loci is often valuable, biological processes and diseases are generally complicated and are rarely explained by variation in just one component of a system. For example, some genetic diseases and disorders are polygenic (due at least in part to contributions from multiple genes), and many are believed to result from changes in gene regulation rather than changes in the genes themselves. Furthermore, these variations contribute to individual phenotypes in various ways; genetic background and environment play their own roles! In short, there are a lot of moving parts, and studying omics can give researchers a "global" view of biology. This can help explain such things as why some variants cause disease in some individuals and not others, or how the components of a biological system work together to form a whole.

### Quiz: What is omics?

True or False: Omics focuses on a narrow, simplified view of biological systems.

[( )] TRUE
[(X)] FALSE
***
<div class = "answer">

While there is often value in simplifying the study of biological phenomena to one or a few specific targets, omics fields don't take this approach; rather, omics fields leverage the power of big data to try to capture the complexity of biological systems and processes.  

</div>
***

## Omics topics

There are many "omics" topics that correspond to various biological domains. The following sections will discuss some of the most popular topics: genomics, transcriptomics, and proteomics.

### Genomics

As the name suggests, genomics is the study of **genomes**. A genome is the complete genetic information of an organism, and so the study of genomics is generally focused on identifying and studying the effects of variants within this genetic information. In medicine, this can lead to a better understanding of variation in response to pharmacological agents or disease prognoses. A commonly conducted type of genomics study is called a **genome-wide association study** (GWAS) which, [according to the National Human Genome Research Institute](https://www.genome.gov/genetics-glossary/Genome-Wide-Association-Studies#:~:text=A%20genome%2Dwide%20association%20study,disease%20or%20a%20particular%20trait), is "a research approach used to identify genomic variants that are statistically associated with a risk for a disease or a particular trait."  In these studies, "thousands of individuals are genotyped for more than a million genetic markers, and statistically significant differences in minor allele frequencies between cases and controls are considered evidence of association" (Hasin et al., 2017).

Genomics vs. genetics
=====

Though they are often mixed up or used interchangeably, genomics and genetics are distinct fields with different goals. Whereas genomics is the study of an organism's genome, or all of its genetic information, **genetics** is the study of specific genes (or parts of genes), their effects, and how they are inherited.

What about bioinformatics? Is that the same thing?
=====

Bioinformatics is another word that is often used interchangeably with genomics, but they are also not the same thing! The National Human Genome Research Institute [defines](https://www.genome.gov/genetics-glossary/Bioinformatics) Bioinformatics as "using computer technology to collect, store, analyze and disseminate biological data and information, such as DNA and amino acid sequences or annotations about those sequences."  Bioinformatics makes the study of genomics and other omics disciplines possible.

### Transciptomics

An organism's **transcriptome** is all of the RNA that is transcribed from that organism's DNA, and **transcriptomics** is the qualitative (which transcripts are present) and quantitative (how much of each transcript is present) study of these RNA transcripts. While some RNA transcripts are templates to be translated into proteins, it is becoming increasingly recognized that many RNA molecules have important biological roles beyond encoding proteins, including gene regulation and translation.

While every cell in an organism has the same genome, the transcriptome will vary between cell populations and can change in response to changes in the environment, such as disease or treatment. The primary technologies for studying transcriptomics are **microarray**, in which RNA fragments of known sequences are bound to a surface (or "chip") and the amount of each fragment is quantified, and **RNA-Seq**, in which RNA sequences (which can be known or unknown) are analyzed qualitatively and quantitatively using **next-generation sequencing** (in which millions of sequences can be run at one time).

### Proteomics

Proteomics is the study of a cell or organism's complete set of proteins. This involves quantifying how much of each protein is present, how they interact with each other and other molecules, and how the proteins are modified (a protein's function and regulation can often be affected by post-translation modifications). Like a cell's transcriptome, the **proteome** of a cell (or organism) is constantly shifting in response to changing conditions.

The most common high-throughput method of studying the proteome is **mass spectrometry** (often called mass spec), in which proteins or protein fragments are **ionized** (or charged) and then separated based on their mass-to-charge ratio. For more information about protein mass spectrometry, check out [this beginner's guide to protein mass spec](https://portlandpress.com/biochemist/article/42/5/64/226371/A-beginner-s-guide-to-mass-spectrometry-based).

### Other topics

A few other omics topics that you may encounter include:

* **Epigenomics:** The study of a cell or organism's **epigenome**, or the specific set of proteins and other molecules that bind to and regulate DNA.

* **Metabolomics:** The study of the set of small molecules in a cell known as **metabolites** that result from cellular metabolism.

* **Microbiomics:** The study of a system's microorganisms, such as those that live in the human digestive system.


### Multi-omics

In "Multi-omics approaches to disease", Hasin et al. write:

>Each type of omics data, on its own, typically provides a list of differences associated with the disease. These data can be useful both as markers of the disease process and to give insight as to which biological pathways or processes are different between the disease and control groups.

All of these biology domains that we have talked about so far are interconnected, and so it is perhaps not very surprising that there are circumstances in which it makes sense to take a **multi-omic** approach for a particular study. Biological processes are complex and can rarely be explained by just one set of molecules. Perhaps a disease-associated genomic variant might be due to contributions of differential regulation (the realm of transcriptomics) and/or changes in protein expression (which might be elucidated by proteomic analysis). A study into a specific disease might wish to examine all of the various biological processes that are altered, from cellular metabolism to gene expression. There are a variety of ways in which multiple omics domains might contribute to a more thorough understanding of biological processes!

### Quiz: Omics topics

Which of the following omics topics involves studying gene expression by quantifying or sequencing RNA?

[( )] Genomics
[(X)] Transcriptomics
[( )] Proteomics
[( )] Metabolomics
***
<div class = "answer">

Transcriptomics is the study of the RNA transcripts in a system, which is considered one measure of gene expression under certain conditions. Genomics is the study of the genome, which is DNA; proteomics deals with proteins, and metabolomics studies the small molecules resulting from cell metabolism.

</div>
***

## Caveats and Challenges

While omics approaches can be powerful, this doesn't mean that an omics approach is always the "best", nor that omics studies are guaranteed to provide every answer to every question! While omics studies can leverage large data sets to find patterns and correlations, they can't provide much insight about individuals, nor do they offer 100% certainty about any results or conclusions. There are several caveats to be aware of when planning or reading about an omics study:

* **Heterogeneity of populations:** According to Hasin et al., "[i]nsights gained from omics approaches are mostly comparative" (2017), meaning that omics studies involve comparing groups to each other (such as "disease vs. healthy" or "treatment vs control", for example). Inherent heterogeneity in any of these populations makes it difficult to distinguish important differences, or "signal", from unrelated variation, also called "noise." Because of the amount of data being analyzed in omics studies, this problem can be amplified compared to traditional approaches.

* **Confounding variables:** Omics allows researchers to ask complex questions with many variables, but that doesn't mean studies can include every possible variable. Variables that researchers don't know about or don't measure can still be contributing to the effect being studied. Any conclusions drawn from the results of an omics study (or any scientific study) should account for this possibility.

* **Reproducibility:** Due to the amount and complexity of the data in omics studies, the analysis process can require many steps, and there will be differences in workflows between studies. This means that results sometimes can't be reproduced from one study to another.

### Quiz: Caveats and Challenges

True or False: A well-designed omics study will allow a researcher to pinpoint the cause of a specific disease in an individual.

[( )] TRUE
[(X)] FALSE
***
<div class = "answer">

While a well-designed omics study might offer some insight into factors that could contribute to the disease in question (which in turn could reveal promising treatment targets or more information about disease prognosis), study populations are simply too heterogeneous and there are too many possible variables for a study to lead to a definite conclusion about a specific individual.

</div>
***


## Additional Resources

The website [genome.gov](https://www.genome.gov) has a variety of educational resources and infographics for reading more about various omics topics:

* The [About Genomics](https://www.genome.gov/about-genomics) has overviews on genomes, genomics, and even a useful glossery of genomics-related terms.

* They also have [a brief overview of transcriptomics](https://www.genome.gov/about-genomics/fact-sheets/Transcriptome-Fact-Sheet)


## References

Hasin, Y., Seldin, M. & Lusis, A. Multi-omics approaches to disease. Genome Biol 18, 83 (2017). https://doi.org/10.1186/s13059-017-1215-1

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Omics+Orientation%22)!

Remember to change the redcap link so that the module name is correct for this module!

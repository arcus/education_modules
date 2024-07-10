<!--

author:   DART Team
email:    dart@chop.edu
version:  2.0.1
current_version_description: Added macro aws_explanation to provide context for learners about why we're requiring them to set up an AWS account.
language: en
narrator: UK English Female
title: Genomics Module Macros
comment:  This is placeholder module to save macros used in other modules.

@version_history 
Previous versions: 

- [1.0.0](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/a588227c04699c46112b01bea136679f8d6f7dc0/_module_templates/macros_genomics.md#1): Initial version

@end

@aws_explanation

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

This module includes hands-on genomics analysis examples that are too demanding to run on most personal computers. 
In order to follow along, you'll need to use Amazon's cloud computing (AWS), which will require you to have an AWS account with a credit card.

</div>

We regret having to rely on a paid service for our learners to practice this code, but unfortunately we have been unable to find a free service that can support the computing power needed for genomics. 
If you have a suggestion for a free platform we could direct learners to instead of AWS, please [let us know](#feedback)!

We'll continue to look for a better solution, but in the meantime we wanted to make these training materials available in the best way we know how.

<div class = "options">
<b style="color: rgb(var(--color-highlight));">Another option</b><br>

**What other options do you have?**

You can try to download all of the relevant files and install the necessary software on your computer (there are instructions for doing so in the [Data Carpentry genomics setup instructions](https://datacarpentry.org/genomics-workshop/#setup)).
Please note that even for very small genomics analysis examples, the files required are large and it may take hours for you to download them. 
Even after downloading everything, your computer might not be powerful enough to run the necessary commands without hanging. 

You may have access to powerful cloud computing via your institution. 
If so, that can be a great option for practicing genomics analysis without having to set up an AWS account. 
Reach out to your IT team for help accessing and using computing resources at your institution. 
It may be helpful to share the [Data Carpentry genomics setup instructions](https://datacarpentry.org/genomics-workshop/#setup) with them to let them know what software you'll need.

</div>

@end

@lesson_prep_ami

For this lesson, we recommend you work in the cloud rather than on your personal computer. 
There is an Amazon Machine Image (AMI) published by [Data Carpentry](https://datacarpentry.org/) that will have everything you need set up. 

For step by step instructions on how to set up your own copy of the AMI, see [Genomics Tools and Methods: Computing Setup](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/genomics_setup/genomics_setup.md#setting-up-your-computing-environment-in-aws).
If you've set this AMI up already for a previous module, you don't need to do it again. 

<div class = "gratitude">
<b style="color: rgb(var(--color-highlight));">Thank you!</b><br>

We are grateful to the authors at maintainers at [Data Carpentry](https://datacarpentry.org/) for creating and sharing the Community AMI for genomics analysis!

</div>

Once you have set up your instance, you will need to connect to it from the command line on your computer. 

As a reminder, you will need the **Public IPv4 DNS** for your instance, which you can copy from your AWS EC2 Dashboard. 
You will also need to use the username `dcuser` with the password `data4Carp`. 

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

For full instructions on how to connect to your instance, see the Data Carpentry instructions for connecting from a [MacOS/Linux computer](https://datacarpentry.org/genomics-workshop/AMI-setup#headingSpoiler1) or from a [Windows computer](https://datacarpentry.org/genomics-workshop/AMI-setup#headingSpoiler2).

</div>

@end

@aws_billing_reminder

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

You will continue to be billed as long as your AWS instance is available, even if it is stopped. 
To stop accumulating charges, you must **terminate** your instance.

For more details, see the [Data Carpentry warning about AWS instances](https://datacarpentry.org/genomics-workshop/AMI-setup#very-important-warning---avoid-unwanted-charges).

Remember that when you terminate an AWS instance, any data on it is permenantly lost. 
If there are files on your instance that you don't want to lose, be sure to move them to your own computer with `scp` before terminating the instance.

</div>

@end

-->

# Genomics Module Macros

@aws_explanation

## Lesson Preparation

@lesson_prep_ami

## Terminate your instance

@aws_billing_reminder

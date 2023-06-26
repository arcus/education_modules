<!--

author:   DART Team
email:    dart@chop.edu
version:  1.0.0
current_version_description: Initial version.
language: en
narrator: UK English Female
title: Genomics Module Macros
comment:  This is placeholder module to save macros used in other modules.

@version_history 
No previous versions.
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

For full instructions on how to connect to your instance, see the Data Carpentry instructions for connecting from a [MacOS/Linux computer](https://datacarpentry.org/genomics-workshop/AMI-setup/#connect-to-your-amazon-instance-macoslinux) or from a [Windows computer](https://datacarpentry.org/genomics-workshop/AMI-setup/#connect-to-your-amazon-instance-windows).

</div>

@end

@aws_billing_reminder

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

You will continue to be billed as long as your AWS instance is available, even if it is stopped. 
To stop accumulating charges, you must **terminate** your instance.

For more details, see the [Data Carpentry warning about AWS instances](https://datacarpentry.org/genomics-workshop/AMI-setup/#very-important-warning---avoid-unwanted-charges).

Remember that when you terminate an AWS instance, any data on it is permenantly lost. 
If there are files on your instance that you don't want to lose, be sure to move them to your own computer with `scp` before terminating the instance.

</div>

@end

-->

# Python Module Macros

@sage

@lesson_prep_python_sage

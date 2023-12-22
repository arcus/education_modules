<!--
module_id: data_management_basics
author:   Ene Belleh
email:    bellehe@chop.edu
version: 1.1.4
current_version_description: Fixed mermaidchart error that was causing diagram to not render; updated metadata
module_type: standard
docs_version: 3.0.0
language: en
narrator: US English Female
mode: Textbook
title: Research Data Management Basics
comment: Learn the basics about research data management.
long_description:  If you conduct research or work with research data or researchers, it's likely that research data management topics affect you.  Learn what research data management is, how to think about it in a structured way, and understand its scientific importance.
estimated_time_in_minutes: 40
@pre_reqs
The only pre-requisite suggested for this module is experience working in research in any capacity.
@end

@learning_objectives  

After completion of this module, learners will be able to:

- Define research data management
- Explain why data management forms an important part of the responsible conduct of research
- Explain how various research stakeholders share responsibility for research data management
- Give examples of research data management tasks within various stages of the research lifecycle

@end
good_first_module: true
collection: intro_to_data_science
data_task: data_management
coding_required: false
@sets_you_up_for

@end
@depends_on_knowledge_available_in

@end

@version_history

Previous versions: 

- [1.0.1](https://liascript.github.io/course/?https://raw.githubusercontent/arcus/education_modules/3cdfc807be26db43d837de9e325b66c9213a3d5c/data_management_basics/data_management_basics.md):  First version with improved feedback survey
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
script: https://cdn.jsdelivr.net/npm/mermaid@9.4.3/dist/mermaid.min.js

-->

# Research Data Management Basics

@overview

## Research Data Management

Let's start with a quick definition.  **Research data management** (sometimes you'll also see **RDM** as an abbreviation) consists of activities that enable long term use and reuse of data and includes two principal sets of tasks, each associated with a goal.

* **Tasks:** the routine processing and workflow of research data throughout the active stage of a project.  **Goal:** Permit investigation of a hypothesis or scientific exploration, over a limited span of time.
* **Tasks:** the procedures that support long-term preservation, access, and usage of the data after the project is finished. **Goal:** Permit ongoing future scientific inquiry and dialog.

**You Already Do Data Management!**
------

If you conduct research, you already perform some level of research data management.  Whether your workflow involves scattered sticky notes or carefully organized lab notebooks, you are organizing what is recorded about your methods and data, where that information is kept, and who can access and work with that information.  That's one of the central tasks of data management!

Research data management is a critical pain point for many data users.  There are so many decisions that have to take place along the way:

* What's the best way to arrange the data files needed to carry out a project?  
* How are ongoing decisions about the study being recorded?  What kinds of notes need to be preserved?  For how long?
* Should documents be stored in a common drive?  Using what kinds of subfolders? 
* Which members of the team need access to which research data?
* Do digital copies of physical forms suffice, or will physical copies be kept?  Where? For how long? 
* How should researchers deal with emails that are sent back and forth between researchers to define a specific cohort? 
* What is the long-term storage strategy for this data?
* Are there ways to save the data in multiple formats to accommodate unknown future needs?
* Should data be de-identified?  At what stage?  
* Should identifying data be discarded? When? By whom?

Even a small project organized by a single researcher can be complex, and when a team of several researchers and supporting staff are involved, individual data management practices can collide.  This is complicated by the fact that many seemingly ordinary tasks (like saving a file with a name) are actually research data management decisions that we may not think of in those terms.  Even if you don't think of yourself as making research data management decisions, you almost certainly are!

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Sometimes in our work we encounter what we call "data shame".  That's the unpleasant experience of feeling that one's research project is so disorganized that it's embarrassing and needs to be kept hidden.  

If this ever happens to you, or you feel overwhelmed at the prospect of creating a research data management plan, take a breath and realize that most people struggle with the level of organization that a research project entails.  There are lots of reasons why data management is difficult, and you're not alone in wanting to improve.

</div>

### Quiz: Research Data Management

Which of the following is the most comprehensive definition of data management?

[( )] Activities and practices that support long-term storage of data in a secure location.
[(X)] Activities and practices that support the long-term preservation, access, and use of data.
[( )] Activities and practices that support making data available on the web.
[( )] Activities and practices that support cleaning of data after they are collected.
*****
<div class = "answer">
While long term storage of data in a secure location is often a crucial part of research data management (RDM), it's really only one small aspect of the full scope of RDM.  Similarly, cleaning data is almost always a stage in research data management, but it only constitutes part of RDM.  While some research data may need to be made available online, that's not always the case, and so we're once again left with only an incomplete definition of research data management.  The most complete answer is that research data management consists of activities and practices that support the long-term preservation, access, and use of data.

</div>
*****

## Research Data Lifecycle

At the start of this module, we gave a description of research data management that had two major aspects: work done to keep a research project going, and work done to make research data usable after a project ends.  

We're going to offer a more complex taxonomy of research data management here, based on RDM tasks that belong to each of the five stages in the **research data lifecycle**.  Before we share our visualization of the research data lifecycle, we'd like to offer a caveat.  

> All models are wrong, but some are useful." - George E. P. Box

You've perhaps seen visualizations of the research data lifecycle that show a circular diagram.  We'll add our own circular diagram to the mix, but keep in mind that you may see these stages called slightly different things in different places!  You may also see similar diagrams with more or fewer steps.  We'll go into each phase of research data management in greater detail.

<div style = "background-color:white;">

<script style="display: block" run-once="true" modify="false">
mermaid.initialize({});

var svg = mermaid.render(
'data_lifecycle',
`flowchart LR
  A[Discovery\\nand Planning] --> B[Data Collection]
  B --> C[Preparation and\\nData Analysis]
  C --> D[Publication\\nand Sharing]
  D --> E[Long-Term\\nManagement]
  E --> A
`,
function(g) {
    return true;
})

"HTML: " + svg
</script>

</div>

The diagram shows a circular diagram of the five phases of the research data lifecycle appear in a circle, including

* Discovery and Planning
* Data Collection
* Preparation and Data Analysis
* Publication and Sharing, and 
* Long term Management

The last phase reconnects to the first phase, discovery and planning, to start the cycle again in an iterative way.

### Discovery & Planning

This stage of the research data lifecycle involves creating formal and informal plans for how research will be conducted.  Much of this planning will result in official documentation (such as a data management and sharing plan, a research protocol, or study pre-registration).  This documentation itself will also form part of the research data that is managed.  

Researchers and research staff have to make a number of important decisions at this stage. Important research data management tasks for this stage of research include, but are not limited to:

* deciding whether a project will create new datasets, combine existing datasets, or analyze existing datasets
* identifying privacy, confidentiality, and other ethical concerns
* thinking about the format and content of documentation as well as the metadata standards to use when describing the data
* identifying potential project users
* choosing an appropriate data repository to store the project's data
* figuring out the costs associated with data management


### Data Collection

At this point, researchers carry out the workflows and methods they planned for their data organization.  This includes both physical assets as well as digital data.  For digital data, it is important to ensure that there are file backup plans and that appropriate storage is planned (including aspects such as the size, cost, and security of storage). At this point, investigators should be implementing their plans for quality control, security, and access controls, whether for physical samples, digital files, or both.

As an example, you may use the REDCap research data capture software, and your institution may handle backing up those servers on your behalf.  You'll still have to exercise some governance on how data is entered (will double entry be used, for example?), who on your team has access to that data, and whether data downloading is permitted during data collection.  

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Sometimes the data collection phase of the research data lifecycle is the moment when researchers realize that they didn't plan for all the eventualities of research data.   This is also a very busy phase of research and it can be very tempting to settle for a quick solution to a data issue, rather than to gather the team and make a well-thought plan for how to address the situation.  

We encourage you to think back to previous research efforts.  What unplanned decisions did you have to make with regard to storing or discarding data, naming or renaming files, tracking new fields you hadn't planned on recording, making reports to stakeholders you had forgotten to account for, recording decision points, retracting access when someone left the lab, and so on?  Recalling these pain points that occurred during data collection last time can help you move the planning for these eventualities into the earlier planning stage for your next research effort.

</div>

### Preparation & Data Analysis

Researchers almost always have to perform cleaning, manipulation, or processing of raw research data. Documenting the changes to the raw data during this phase is crucial, as is producing a "master" version that can then be examined and eventually archived. Research rigor and reproducibility depends on the ability of reviewers and other researchers to understand exactly what was done to data during preparation and data analysis, in order to ensure that no mishaps occur that could cause errors in data interpretation.

Additionally, it is crucial that researchers record the analysis processes, including any changes made to the data, any model that was used, the code that was used to carry out the analysis, and any hardware and software dependencies.

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

If you haven't already had a chance to read our module on [Reproducibility, Generalizability, and Reuse](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/reproducibility/reproducibility.md), or it's been a while since you've read it, consider skimming some of the topics in that module to refresh your understanding of research reproducibility.  If your collaborators (including future **you**) know exactly each step you made in the journey from raw data to findings, you have a highly reproducible research effort.  

</div>

It can be tempting for researchers at this point in the research data life cycle to interpret data in ways that are favorable to their hypotheses.  This is another moment in which early, careful, detailed planning can help researchers maintain the statistical rigor that will strengthen their case.  For example, consider the relative trustworthiness of study with a pre-registration that details precisely what statistical tests will be performed before any data is collected or analyzed.  Beyond research rigor, having an analysis plan formulated ahead of time means that researchers won't find themselves in the situation of not having asked the right questions to be able to perform an analysis they decided to try after data was already collected.

### Publication and Sharing

Most publishers have their own requirements related to data formats, documentation of scripts used to clean and analyze data, and other materials that must be submitted along with a manuscript.  During the publication stage, researchers should consider their documentation carefully.  Are the submitted materials sufficient to permit the data to be used effectively again by a third party?  To allow reviewers to examine their methods and statistical rigor?  If primary data cannot be shared for ethical reasons, sample fabricated data can be used to demonstrate the expected data format used by scripts and models used in the study.

### Long-term Management

During this phase, researchers publish their data and findings, turn in reports, and deposit data and supporting materials into an archive or repository.  This is a highly contextual part of the research data management lifecycle, which will change according to the norms of various disciplines.


<div class = "history">
<b style="color: rgb(var(--color-highlight));">Historical context</b><br>

The United States government, which funds many research efforts, has been at the forefront of data repository creation.  Government agencies have also developed several policies and glossaries to help researchers be better stewards of federal funds and organize their data in ways that are better for the conduct of science.  The 2010 [Administrative Order 212-15 of the National Oceanic and Atmospheric Association](https://nosc.noaa.gov/EDMC/nao_212-15.php), for example, gave definitions of **Data Stewards**, **Data Management**, **Data Management Services**, and **Data Stewardship**.

Later efforts by the US National Institutes of Health (NIH) have been instrumental in helping define best practices in data management and sharing.  Importantly, NIH now requires data management and sharing (DMS) plans for NIH funded studies.  Their [resources on the topic](https://sharing.nih.gov/data-management-and-sharing-policy/data-management) are understandable and very high quality.

</div>

### Quiz: Research Data Lifecycle

During which phase of the Research Data Lifecycle should researchers determine what type and format of data they are going to collect?

[( )] Initial Data Collection
[( )] Publication and Sharing
[(X)] Discovery and Planning
[( )] Final Preparation and Data Analysis
*****

<div class="answer">
Data collection decisions should be made in the "Discovery and Planning" stage, **not** in the subsequent phase of initial data collection.  

That being said, it sometimes happens that once data starts being collected, it becomes clear that new questions make sense to ask in a questionnaire, or that additional measurements should be made of a biosample. This requires time-consuming amendments of protocols and can slow the progress of a project. A good practice to avoid this is to have some practice runs of data collection with simulated subjects or samples in order to discover these potential enhancements before data collection begins!

Final preparation and data analysis is far too late to consider data type and format, and the same can be said for publication and sharing.

</div>
****

## Stakeholder Responsibilities

Regardless of your role within a research project, you can contribute to successful research data management.  From the undergraduate intern who is processing paper forms to the institutional data governance officers who are responsible for regulatory compliance, everyone has a role to play.  Here are some specific roles and responsibilities that are worth highlighting:

* Primary Researcher or Principal Investigator: Creates and uses data, is responsible for protocol creation and adherence, is the ultimate stakeholder responsible for research rigor and the responsible use of data according to best practices and regulatory requirements.
* Research Institution: Sets internal data management policy and normally provides assistance and some level of monitoring of higher-level regulatory requirements (such as the Federal Common Rule).
* Data Repository: Curates and provides access to data.  A data respository typically ensures that data is organized according to repository standards, is submitted according to any required funder timelines, and is disclosed to parties with legitimate reasons to access or reuse the data.
* User: Uses 3rd party data, and may be responsible for adherence to policies like a Data Use Agreement (DUA) and properly citing data stewards for their data if data is used in a subsequent manuscript or other publication.
* Funder: Provides the resources to support a research project and sets standards for funds recipients.  In the case of many biomedical researchers, the funder may be a governmental agency which has the moral obligation to ensure that taxpayer funds are spent wisely, in support of science that uses best practices.
* Publisher: Disseminates discoveries and maintains the scientific record.  Increasingly, publishers require data sharing if ethically feasible, as well as other details such as data dictionaries, model and analysis details, and other artifacts of research data management.

### Quiz: Stakeholder Responsibilities

Which of the following is not a responsibility of the principal investigator of a research project?

[( )] Planning for the responsible and ethical use of data
[(X)] Handling disclosures of scientific data generated from the study, once that data is submitted to a central database
[( )] Ensuring adherence to research protocols and to applicable laws and regulations
[( )] Being the ultimate responsible party for statistical and procedural rigor in the scientific work
****
<div class = "answer">

All of these are the responsibility of the principal investigator, except for handling disclosures of scientific data generated from the study, once that data is submitted to a central database.  Once data is submitted to a repository, it is generally the repository who handles data disclosures. Sometimes this is accomplished through a scientific committee, sometimes through a simple application or attestation, and occasionally by way of an unregulated download, in the case of non-sensitive data of general public interest.

</div>
****

## Quiz: Why RDM?

Why is it important to practice proper research data management? Select all that apply.

[[X]] Research data management helps researchers create higher quality research output.
[[X]] Research data management supports the long-term preservation of data for future use.
[[ ]] Few publishers have standards for data associated with manuscripts, so researchers have to apply their own rigor.
[[X]] Funding agencies supporting the research require research data management.
[[ ]] Research data management has recently appeared as a new practice, and performing this work shows that researchers are up-to-date.
[[?]] There are three correct answers!
****
<div class = "answer">

Research data management is important for multiple reasons, among which we highlighted three in this question:

* Research data management helps researchers create higher quality research output.
* Research data management supports the long-term preservation of data for future use.
* Funding agencies supporting the research require research data management.

It's false that publishers don't apply their own standards. While some publishers were earlier adopters of the most up-to-date data management policies, all publishers have an important role to play in setting high standards for researchers who submit manuscripts for consideration. It's also false that research data management is a new practice. While it's true that RDM has gotten much more attention lately, research data management has been taking place since the first researchers developed the scientific method, and it's changed over time to adapt to new circumstances and requirements.

</div>
***

## Additional Resources

The [data sharing policies and helpful information](https://sharing.nih.gov/data-management-and-sharing-policy) published online by the National Institutes of Health (NIH) are some of the best materials you can consult for help. 

We also recommend the NIH's [guidance around writing a Data Management and Sharing Plan](https://sharing.nih.gov/data-management-and-sharing-policy/planning-and-budgeting-for-data-management-and-sharing/writing-a-data-management-and-sharing-plan), which they now require for all grants planning to generate scientific data.

## Feedback
@feedback
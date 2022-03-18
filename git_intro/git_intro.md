<!--

author:   Rose Hartman
email:    hartmanr1@chop.edu
version:  1.0.1
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Intro to Version Control

comment:  An introduction to what version control systems do and why you might want to use one.

long_description: Version control systems allow you to keep track of the history of changes to a text document (e.g. writing, code, and more). Version control is an increasingly important tool for scientists and scientific writers of all disciplines; it has the potential to make your work more transparent, more reproducible, and more efficient. This module is appropriate for beginners with no previous exposure to version control.

estimated_time: 10 min

@learning_objectives

After completion of this module, learners will be able to:

- Understand the benefits of an automated version control system
- Understand the basics of how automated version control systems work

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css
script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Intro to Version Control

<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

None. This lesson is appropriate for beginners with no experience using version control. Experience using word processing software like Microsoft Word, Google Docs, or LibreOffice may be helpful but is not required.


**Learning Objectives**

@learning_objectives

</div>

## How we keep track of changing documents

We'll start by exploring how version control can be used
to keep track of what one person did and when.
Even if you aren't collaborating with other people,
automated version control is much better than this situation:

![Comic showing a student revising a paper called Final.doc on their computer. The student gives it to their advisor, who provides feedback for a new version, which is then called FINAL\_rev.2.doc. They go back and forth several times, adding more comments and renaming the file each time with increasingly more complex names: FINAL\_rev.6.COMMENTS.doc, FINAL\_rev.8.comments5.CORRECTIONS.doc, FINAL\_rev.18.comments7.corrections9.MORE.30.doc, FINAL\_rev22.comments49.corrections.10 why did i come to grad school????.doc.](media/phd101212s.png "'notFinal.doc' by Jorge Cham [www.phdcomics.com](https://phdcomics.com/comics/archive.php?comicid=1531)")

We've all been in this situation before: it seems unnecessary to have multiple nearly-identical versions of the same document. Some word processors let us deal with this a little better, such as
Microsoft Word's [Track Changes](https://support.office.com/en-us/article/Track-changes-in-Word-197ba630-0f5f-4a8e-9a77-3712475e806a),
Google Docs' [version history](https://support.google.com/docs/answer/190843?hl=en), or
LibreOffice's [Recording and Displaying Changes](https://help.libreoffice.org/Common/Recording_and_Displaying_Changes).

<div class = "help">
**Do you use ‘undo’ in your editor? ‘Undo’ is the simplest form of version control.**

Most people already use aspects of a version control system already even if they don't realize it. Switching to a more formal version control system lets you take advantage of tools you already rely on (like undo, track changes, and the ability to work on documents collaboratively) but in a way that gives you much more power and control.
</div>

### Changes are saved sequentially

Version control systems start with a base version of the document and then record changes you make each step of the way. You can think of it as a recording of your progress: you can rewind to start at the base document and play back each change you made, eventually arriving at your more recent version.

![Cartoon of a document as it changes. In the first stage, it has one full paragraph and a single line of the second paragraph. An arrow indicates the final line of the document is being edited, and in the next image that line is shown as orange instead of black to indicate that a change has been made. A second arrow shows that now a new paragraph is being added, and in the final image the document is shown with the edited line and the new paragraph in orange to indicate that they are marked as changes from the original version.](media/play-changes.svg)

### Different versions can be saved

Once you think of changes as separate from the document itself, you can then think about "playing back" different sets of changes on the base document, ultimately resulting in different versions of that document. For example, two users can make independent sets of changes on the same document.

![A cartoon of a document being edited by two different people. In the first stage, the document is shown as one full paragraph and a single line of the second paragraph. There are then two arrows, one pointing up to a version edited by one person and the other pointing down to a version edited by someone else. The first editor adds a new line to the first paragraph, shown in orange to indicate a change. The second editor adds several lines to the second paragraph, shown in purple.](media/versions.svg)

### Multiple versions can be merged

Unless multiple users make changes to the same section of the document - a conflict - you can incorporate two sets of changes into the same base document.

![The two edited versions of the document from the previous example are shown merging into a single final document. The final document shows the original text in black, the first editor's addition in orange, and the second editor's addition in purple, all integrated seamlessly into one document.](media/merge.svg)

## Version control systems

A version control system is a tool that keeps track of these changes for us, effectively creating different versions of our files. It allows us to decide which changes will be made to the next version (each record of these changes is called a [commit](https://swcarpentry.github.io/git-novice/reference.html#commit), and keeps useful metadata about them.

The complete history of commits for a particular project and their metadata make up a [repository](https://swcarpentry.github.io/git-novice/reference.html#repository). Repositories can be kept in sync across different computers, facilitating
collaboration among different people.

<div class = "learnmore">
**The Long History of Version Control Systems**

Automated version control systems are nothing new.
Tools like [RCS](https://en.wikipedia.org/wiki/Revision_Control_System), [CVS](https://en.wikipedia.org/wiki/Concurrent_Versions_System), or [Subversion](https://en.wikipedia.org/wiki/Apache_Subversion) have been around since the early 1980s and are used by many large companies.
However, many of these are now considered legacy systems (i.e., outdated) due to various limitations in their capabilities.
More modern systems, such as [Git](https://git-scm.com/) and [Mercurial](https://swcarpentry.github.io/hg-novice/), are **distributed**, meaning that they do not need a centralized server to host the repository.
These modern systems also include powerful merging tools that make it possible for
multiple authors to work on the same files concurrently.
</div>

## Quiz: Version control

Imagine you drafted an excellent paragraph for a paper you are writing, but later ruin it. How would you retrieve the **excellent** version of your conclusion? Is it even possible? Take a moment to write your thoughts in the box below, then click the checkmark to see our solution.

[[answer]]
<script>
  let input = "@input".trim();
  /.*/i.test(input);
</script>
***
<div class = "answer">
Recovering the excellent version is only possible if you created a copy of the old version of the paper. The danger of losing good versions often leads to the problematic workflow illustrated in the PhD Comics cartoon at the beginning of this lesson.

(Note that because of the open-ended nature of this question, we can't automatically grade your response. It will show up as correct no matter what you write.)
</div>
***

Imagine you have 5 co-authors. How would you manage the changes and comments they make to your paper?  If you use LibreOffice Writer or Microsoft Word, what happens if you accept changes made using the `Track Changes` option? Do you have a history of those changes? Take a moment to write your thoughts in the box below, then click the checkmark to see our solution.

[[answer]]
<script>
  let input = "@input".trim();
  /.*/i.test(input);
</script>
***
<div class = "answer">
Collaborative writing with traditional word processors is cumbersome. Either every collaborator has to work on a document sequentially (slowing down the process of writing), or you have to send out a version to all collaborators and manually merge their comments into your document. The 'track changes' or 'record changes' option can highlight changes for you and simplifies merging, but as soon as you accept changes you will lose their history. You will then no longer know who suggested that change, why it was suggested, or when it was merged into the rest of the document. Even online word processors like Google Docs or Microsoft Office Online do not fully resolve these problems.

(Note that because of the open-ended nature of this question, we can't automatically grade your response. It will show up as correct no matter what you write.)
</div>
***

## Key points

* Version control is like an unlimited ‘undo’.

* Version control also allows many people to work in parallel.


## Additional Resources

The material for this lesson is based closely on the [Automated Version Control lesson](https://swcarpentry.github.io/git-novice/01-basics/index.html) published by [Software Carpentry](https://software-carpentry.org/) under a creative commons license. Many thanks to Carpentries for developing and sharing this material!

There is an article written for scientists about how and why to get started with version control: Blischak JD, Davenport ER, Wilson G. [A Quick Introduction to Version Control with Git and GitHub](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4718703/). PLoS Comput Biol. 2016;12(1):e1004668. Published 2016 Jan 19.

There is an excellent book available for free online, [Happy Git with R](https://happygitwithr.com/big-picture.html), targeting R users who want to get started with version control. The opening chapter provides relevant background on version control regardless of whether you have any R experience.

For discussion of how version control can improve your scientific writing process, see our article [Version Control for Writing](https://education.arcus.chop.edu/version-control-writing/).

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Intro+to+Version+Control%22)!

# Quality Assurance for modules

When a module creator is ready to request that their module be included, they will create a Pull Request (PR).  This begins the work of quality assurance.  As someone who is reviewing the modules created by others, it's important to have use a consistent method for evaluating content.  This work is exacting and can be tedious.  It's probably worthwhile to look at other QA issues that have successfully been closed to see a bit more information about the level of detail other reviewers provide. To see a completed review, check out https://github.com/arcus/education_modules/issues/53.

## Step 1: Create an Issue

* Click on "Issues" or go to https://github.com/arcus/education_modules/issues.
* Choose "New Issue" (or if your screen is small, just "New").  This is a green button on the right side:
![Arcus/education_modules repo issues page shows the green "New issue" button on the right side above the list of open issues](media/new_issue.png)
* Select the "Get Started" button for the type of module you're QAing: Standard, Wrapper, or Exercise. This will automatically populate the issue with the correct QA template for you, and will automtically assign the "Quality Assurance" label.
* Title the issue as "QA" plus the proposed directory name from the PR. (For example, if the PR includes a new module with the directory named "reproducibility", the title would be "QA reproducibility".)
* Where curly brackets appear in the template text, remove the curly brackets and their contents and replace with the appropriate values. To see a completed review, check out https://github.com/arcus/education_modules/issues/53.
* How do you find the liascript link? You have to generate this!  But it's easy!
  - First, go to the .md file that makes up the module (for example, the reproducibility module .md is reproducibility/reproducibility.md) in GitHub.
  - Then, copy the URL of this file.  It will look something like https://github.com/arcus/education_modules/blob/name_of_branch/name_of_module/name_of_module.md
  - Then, paste that URL into the box at https://liascript.github.io and click "load course".
  - Copy the resulting URL, and that's your liascript link!  It will look something like this: https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/name_of_branch/name_of_module/name_of_module.md#1
* Click on the "Preview" tab to see if everything is rendering nicely and link to the PR is clickable.
* Click "Submit new issue".

## Step 2: Go through checklists

Once you create the issue, then go through and actually evaluate the checklists.  

If you're convinced a checklist item is complete, you can click the checkbox without editing the text of the issue -- simply click in the checkbox as if it were a checkbox on any web page.  Helpfully, you will see the number of "tasks" at the top of the issue reflect what's been marked as complete.

![The issue title appears at the top of the page. The issue's "open" status appears below that, followed by a task counter reading "4 of 26 tasks".](media/task_counter.png)

If there are problems to resolve before a checklist item is complete, communicate with the author using comments on the issue and @ the author.  Be as precise as possible (e.g. what file, what line, what problem are you referring to?).  If it's clear that the module has many glaring issues, it's okay to stop work on review, close the PR, and simply ask the author to review the checklist and resubmit.  It's not worth a lot of effort to do QA on a module that needs a substantial rework.

![A comment written on the "write" tab. There are two buttons below to leave the comment: "close with comment" and "comment".](media/issue_comment.png)

The author may make fixes to their code and commit to the branch.  This will simply update their PR with newer commits. In GitHub, when you look at the PR, the most recent commit is the lowest one down on the page:

![On a pull request, the PR comment appears at the top. Below, commits appear as their commit summary followed by commit hash.](media/pr_with_multiple_commits.png)

Once you are satisfied with the quality of the module (don't worry, it can always be improved, this is a best effort only, no perfection expected or implied), the last thing to do before the PR is to make sure that any changes to references within the material relating to the branch name are resolved (see the last bit of the QA template text).  Issue a final comment reminding the author to handle this in a new commit.  Check that commit and if all is well, approve the PR and close the issue.

In general we should not delete issues or comments on issues, because they provide a useful history of the project.
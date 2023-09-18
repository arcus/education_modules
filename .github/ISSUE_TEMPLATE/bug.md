---
name: Bug Report
about: Report something broken or not working as expected
title: ''
labels: bug
assignees: ''

---
<!--
Note: If this bug was reported via the Quick Module Feedback form, remember to include `record number:` at the top so we can link it back to the original comment if needed, and add the `user-reported` label.
-->

Description of problem: 

---

**Some things to try first!** 

- If pyodide cells aren't working as expected in Python modules, we may need to update pyodide. 
- If LiaScript macros aren't rendering properly, especially `@overview`, check for blank macros defined in the front matter (e.g.`version_history` is a common culprit). You may need to add load bearing white space. 
- If the `feedback` macro isn't working, check that no front matter fields used in the generated REDCap link are missing (e.g. `module_type`).

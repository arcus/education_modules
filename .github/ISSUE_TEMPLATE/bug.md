---
name: Bug Report
about: Report something broken or not working as expected
title: ''
labels: bug
assignees: ''

---
<!--
Note: If this bug was reported via the Quick Module Feedback form, remember to fill in `record number:` at the top so we can link it back to the original comment if needed, and add the `user-reported` label.
If this was NOT reported via the Quick Module Feedback form, then feel free to delete the `record number:` line or leave it blank.
-->
record number:

Description of problem: 

---

**Some things to try first!** 

- If pyodide cells aren't working as expected in Python modules, we may need to update pyodide. 
- If LiaScript macros aren't rendering properly, especially `overview`, check for blank macros defined in the front matter (e.g.`version_history` is a common culprit). You may need to add load bearing white space. 
- If the `feedback` macro isn't working, check that no front matter fields used in the generated REDCap link are missing (e.g. `module_type`).
- Problems with `div`? You may need a newline after the `div` tag and before the `/div` tag. 
- Quiz answer boxes not displaying properly? There cannot be a newline between the last answer option and the beginning of the question followup section. Make sure the `****` surrounding the answer div starts immediately after the last line of the question. 

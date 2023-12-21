---
name: Checklist for updating modules to v4
about: Checklist for updating a module to comply with docs.md v4
title: Docs v4 Update Checklist
assignees: ''

---

# Module Update Checklist
----
Name of Module: {take from the title of the main markdown file for the module}
PR for module update: #[PR number here]

This is the checklist for bringing a module up to date with the latest major version of docs.md: v4

## Summary of changes

There is a new required front matter field: `module_id`

The module\_id for each module should exactly match the module's directory name and markdown file name.

## Front matter

* [ ] module\_id field matches the module's directory name / file name

## Final check

When you're ready to finalize the updated module, do the following in the module front matter:

* [ ] Increment `version` for the module. This is a revision. 
* [ ] Update `docs_version` to 4.0.0

---
name: Checklist for updating modules to v2
about: Checklist for updating a module to comply with docs.md v2
title: Docs v2 Update Checklist
assignees: ''

---

# Module Update Checklist
----
Name of Module: {take from the title of the main markdown file for the module}
PR for module update: #[PR number here]

This is the checklist for bringing a module up to date with the latest major version of docs.md: v2

## Summary of changes

The only change is that `coding_required` is now a mandatory front matter field. 
It must be either `true` or `false`. 
See [the `coding_required` page in docs](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/docs.md#38) for more details about this field. 

## Front matter

* [ ] `coding_required` is either `true` or `false`

## Final check

When you're ready to finalize the updated module, do the following in the module front matter:

* [ ] Increment `version` for the module. This is a revision. 
* [ ] Update `docs_version` to 2.0.0

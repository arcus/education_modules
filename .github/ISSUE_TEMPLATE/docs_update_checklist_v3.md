---
name: Checklist for updating modules to v3
about: Checklist for updating a module to comply with docs.md v3
title: Docs v3 Update Checklist
assignees: ''

---

# Module Update Checklist
----
Name of Module: {take from the title of the main markdown file for the module}
PR for module update: #[PR number here]

This is the checklist for bringing a module up to date with the latest major version of docs.md: v3

## Summary of changes

An optional front matter field, `collection`, is now available. Check if this module should belong in one or more collections. To learn more, read the [description in docs](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/docs.md#collection).

There is also a new option, `text`, for `data_domain`.

Every module should have at least one of `data_domain`, `data_task` or `collection` populated with something.

## Front matter

* [ ] If relevant, `collection` is listed, with one or more collections (separated by commas)
* [ ] If relevant, add `text` as the data domain

## Final check

When you're ready to finalize the updated module, do the following in the module front matter:

* [ ] Increment `version` for the module. This is a revision. 
* [ ] Update `docs_version` to 3.0.0

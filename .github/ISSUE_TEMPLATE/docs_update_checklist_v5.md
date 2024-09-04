---
name: Checklist for updating modules to v5
about: Checklist for updating a module to comply with docs.md v5
title: Docs v5 Update Checklist
assignees: ''

---

# Module Update Checklist
----
Name of Module: {take from the title of the main markdown file for the module}
PR for module update: #[PR number here]

This is the checklist for bringing a module up to date with the latest major version of docs.md: v5

*Note*: There is no checklist to update to v4 because all modules were updated with the v4 change, adding `module_id` to front matter, in the same PR that updated docs.md.
To bring a module at v2 up to date with v5, for example, you only need to use the checklists for v3 and v5. 

## Summary of changes

New requirements for directory structure. 
Many modules will already follow these conventions, but for those that don't change the subdirectory names and organization to match the new requirements.

## Module directory structure 

* [ ] The module content markdown file is the only file on the first level of the directory. All other files are contained within subdirectories.
* [ ] Images, videos, and other audio-visual assets are saved within a `media` folder within the module directory
* [ ] Code files (including scripts, notebooks, etc.) are saved within a `code` folder within the module directory
* [ ] Data files are saved within a `data` folder within the module directory. 
* [ ] The only subdirectories that exist are `media`, `code`, and `data`.

## Final check

When you're ready to finalize the updated module, do the following in the module front matter:

* [ ] Increment `version` for the module. This is a revision (although the module content isn't changing at all, the metadata is changing slightly as `docs_version` is updated). 
* [ ] Update `docs_version` to 5.0.0

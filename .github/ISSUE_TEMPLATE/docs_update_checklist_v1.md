---
name: Checklist for updating modules
about: Checklist for updating a module to comply with docs.md v1
title: Docs v1 Update Checklist
assignees: ''

---

# Module Update Checklist
----
Name of Module: {take from the title of the main markdown file for the module}
PR for module update: #[PR number here]

This is the checklist for bringing a module up to date with the latest major version of docs.md: v1

## Summary of changes

The biggest changes to docs for this version are extensive updates to the required front matter, including lots of new fields, and the introduction of shared macros to replace standardized sections.

The following sections provide a complete (hopefully!) list of potential changes to modules needed to bring them up to date with the new version of docs.md. 

## Front matter

* [ ] The front matter includes all required fields from the new templates. Some of these are new fields and some are not. Use the ["Your front matter checklist"](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/docs.md#your-front-matter-checklist) section of docs.md to get a customized list of the required front matter for a given module. 

Also watch specifically for the following:

* [ ] current_version_description is a short, present-tense text fragment without bullets, and gives a learner-centric quick overview of version changes from the learner perspective
* [ ] version_history contains 1-3 past versions with bulleted links to commit-specific documents, unless this is an initial version of a module, in which case version_history should say "No previous versions." For detailed instructions on how to fill out the version fields, see the [docs descriptions](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/docs.md#version_history).

The following should **NOT** be included in module front matter: 

- [ ] REMOVED: any macros defined in the shared macro files
- [ ] REMOVED: `link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css`
- [ ] REMOVED: `script: https://kit.fontawesome.com/83b2343bd4.js`
- [ ] REMOVED: `script:  https://code.jquery.com/jquery-3.6.0.slim.min.js`


## Macros

* For all modules:
    - [ ] Overview is created with the macro, not written
    - [ ] Feedback is created with the macro, not written

* For modules with interactive R, Python, or SQL:
    - [ ] Lesson Preparation is created with the relevant macro, not written

* For wrapper modules:
    - [ ] Lesson Preparation is created with the relevant macro, not written
    - [ ] There is a `print_resource` macro for each external resource just after the `lesson_prep_wrapper` macro

## Other changes

* [ ] Avoid linking to our own modules in the Additional Resources section at the end of each module
* [ ] Check that highlight boxes use the updated style

## Final check

These updates should not change the rendered module much, for the most part. 
To check, pull up the rendered version from before the update and your updated version and look for missing/changed/added content, or anything that's not rendering properly. 
For conveience, paste the liascript links here:

- Original: {paste liascript link for original module}
- Update: {paste liascript link for updated module}

When you're ready to finalize the updated module, do the following in the module front matter:

* [ ] Increment `version` for the module. If no meaningful changes were made to the content of the module as it renders for learners, this is a revision. If there were updates to the module content (e.g. in the Additional Resources section), then it's a minor update.
* [ ] Update `docs_version`

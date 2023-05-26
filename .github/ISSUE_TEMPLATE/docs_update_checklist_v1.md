---
name: Checklist for updating modules
about: Checklist for updating a module to comply with docs.md v1
title: Docs Update Checklist
assignees: ''

---

# Module Update Checklist
----
Name of Module: {take from the title of the main markdown file for the module}
PR for module update: #[PR number here]

This is the checklist for bringing a module up to date with the [latest major version of docs.md: v1](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/ddc7d4a1a8659723c3f0db0a87fcc3b26a0ae071/docs.md#1) 
Note that this link points to a specific commit and is therefore frozen in time. 
If you want to update this checklist after pushing new changes to docs.md, be sure to update this link as well.

## Summary of changes

The biggest changes to docs for this version are extensive updates to the required front matter, including lots of new fields, and the introduction of shared macros to replace standardized sections.

The following sections provide a complete (hopefully!) list of potential changes to modules needed to bring them up to date with the new version of docs.md. 

## Front matter

Make sure the front matter includes all required fields from the new templates. Some of these are new fields and some are not.

TIP: You can also use the "Your front matter checklist" section of docs.md to get a customized list of the required front matter for a given module. 

* [ ] For all modules
    - [ ] author
    - [ ] email
    - [ ] version
    - [ ] current_version_description
    - [ ] module_type
    - [ ] module\_template\_version (should this change to docs_version?)
    - [ ] language
    - [ ] narrator
    - [ ] mode: Textbook
    - [ ] title
    - [ ] comment
    - [ ] long_description
    - [ ] estimated\_time\_in\_minutes
    - [ ] pre_reqs 
    - [ ] learning_objectives
    - [ ] good\_first\_module
    - [ ] sets\_you\_up\_for
    - [ ] depends\_on\_knowledge\_available\_in
    - [ ] version_history
    - [ ] import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md

* [ ] If the learner will need to code to meet the learning objectives, the following are required:

    - [ ] coding_required: true
    - [ ] coding_level
    - [ ] coding_language

* [ ] For modules using interactive R code (binder), the following are required:

    - [ ] r_file
    - [ ] coding_level
    - [ ] coding_language
    - [ ] import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_r.md
    
* [ ] For modules using interactive Python code (sagemath), the following are required:

    - [ ] coding_level
    - [ ] coding_language
    - [ ] import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_python.md

* [ ] For modules using interactive SQL (AlaSQL), the following are required:

    - [ ] coding_level
    - [ ] coding_language
    - [ ] import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_sql.md
    - [ ] import statements for any SQL tables needed

* [ ] For modules about a particular kind of data, or teaching a particular data task/skill:

    - [ ] data_domain
    - [ ] data_task

* [ ] For modules that are part of a sequence:

    - [ ] sequence_name
    - [ ] previous\_sequential\_module (only for modules that are not first in their sequence)

* [ ] For modules that are parallel to another module:

    - [ ] is\_parallel\_to

* [ ] For wrapper modules:

    - [ ] resource1_name
    - [ ] resource1\_description
    - [ ] resource1\_wellvetted
    - [ ] resource1\_wellvetted\_text
    - [ ] resource1\_maintained
    - [ ] resource1\_maintained\_text
    - [ ] resource1\_stablesupport
    - [ ] resource1\_stablesupport\_text
    - [ ] resource1\_a11y\_issues
    - [ ] for wrapper modules with a second external resource, include all of the above for resource2 as well
    - [ ] for wrapper modules with a third external resource, include all of the above for resource3 as well
    - [ ] import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_wrapper.md

The following should **NOT** be included in module front matter: 

- [ ] REMOVED: any macros defined in the shared macro files
- [ ] REMOVED: `link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css`
- [ ] REMOVED: `script: https://kit.fontawesome.com/83b2343bd4.js`
- [ ] REMOVED: `script:  https://code.jquery.com/jquery-3.6.0.slim.min.js`


## Macros

* [ ] For all modules:
    - [ ] Overview is created with the macro, not written
    - [ ] Feedback is created with the macro, not written

* [ ] For modules with interactive R, Python, or SQL:
    - [ ] Lesson Preparation is created with the relevant macro, not written

* [ ] For wrapper modules:
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

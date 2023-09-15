# Module Metadata

Metadata is on each module is stored in that module's front matter. For a complete list of the required metadata, see the [DART LiaScript Documentation's section on front matter](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/docs.md#7).

## Metadata's uses

Metadata helps both learners and module authors to know what exists, and get a better sense of what a module contains without having to first read through the entire module.

## Processing metadata

The metadata from the modules is processed automatically through a series of GitHub actions.

Whenever something is pushed to the main branch of education_modules, an action pulls metadata from the front matter of every module into a python file. If that file is different from the existing version of the metadata records, the metadata is then updated in several places:

1. The [metadata records for this repository](https://github.com/arcus/education_modules/tree/metadata_workflow/assets/metadata), which live on the metadata_workflow branch, are **automatically updated**. These consist of the python file itself and a [generated csv](https://github.com/arcus/education_modules/blob/metadata_workflow/assets/metadata/module_data.csv) for readability.
2. The [module_discovery repository](https://github.com/arcus/module_discovery), which uses the metadata in an application to help learners discover what modules exist is [**automatically updated each Sunday**](https://github.com/arcus/module_discovery/actions/workflows/update_module_data.yml). This action can also be run manually.
3. The [list of modules on the public facing website for DART](https://github.com/arcus/education_modules/blob/gh-pages/docs/list_of_modules.md) also needs to be updated to reflect any new modules or major changes to modules reflected in the metadata. **This update needs to be done manually** for the moment.


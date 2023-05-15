# On-the-fly Validation for YAML in VSCode

To allow for on-the-fly validation in VSCode, you need to update the settings in your instance of VSCode or supply the correct relative path in a $schema key in the archival-request.yml file.

- Install the [Red Hat YAML extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) for VSCode.

- Follow [these instructions] (https://github.com/redhat-developer/vscode-yaml#associating-a-schema-to-a-glob-pattern-via-yamlschemas) to access and update yaml settings in your instance of VSCode. A specific example of updates to the settings.json file that associates module-name.md files to their schemas may look as follows:
`````    
{
    "window.zoomLevel": 1,
    "editor.renderWhitespace": "all",
    "editor.minimap.enabled": false,
    "yaml.schemas": {
        "/Users/pakstisj/Documents/GitHub/education_modules/assets/schemas/metadata_schema.json": ["stub-record.yml", "/Users/pakstisj/Documents/GitHub/education_modules/*/*.md"]
    },
    "yaml.customTags": [    
    ]
}
`````
- Alternatively, you could use the following relative link format in an archival-request.yml file in the `labs` repo. This assumes you have the `labs` repo and the `library` stored parallel to one another in the directory structure on your local machine. Because this method makes assumptions about the location of cloned repos, the editor yaml schema association method is preferred. 
  - `# yaml-language-server: $schema=../../../../../../../archival_request/schema.json`

## Process for incorporating metadata as LiaScript macros

Follow the documentation for how to include metadata in the [DART documentation for writing modules](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/roseh_docs/docs.md).
- The front matter of the `this_module.md` is the source of truth for the module's metadata.
- Each metadata item in the front matter of `this_module.md` is parsed as a macro by LiaScript
    - One line macros have the form `macro_name: data`
    - Block macros start with `@macro_name` and end with `@end` with the data contained on lines between those.
- All required metadata fields must be filled in.
- Optional metadata fields can be entirely omitted from the front matter if not in use.

### Validation

**Future plans:** When a pull request is created to merge a module into main, its front matter is checked against the schema (via GitHub actions) and the author is notified of what needs to be changed. Merging into `main` branch will not be possible until metadata issues are corrected.

### Database for exploration

A script will pull all of the metadata from all modules on main into a single pandas dataframe that can then be processed for other purposes like building the network graph of modules and the module discovery app. This could be automatically recreated every time something is merged into `main`.

### docs.md correspondance to metadata-schema.json 

Becuase docs.md is user facing, it may need to include additional information not necessary or approrpiate to be stroed in the metadata-schema.json. However, where the two (docs.ms and metadata-schema.json) do need to share values, they should be automatically source from the source of truth schema. Below is a list of correspondances for building out that automation.  

- The free-text description in docs.md should come from metadata-schema.json/key/description. 
- The list of possible controlled terms should come from the const key in the referenced section of vaocabulary.json from metadata-schema.json. 
- A description of each of these possible terms, glossing them in a list, should come from the const key in the referenced section of vocabulary.json from metadata-schema.json. 
- Required fields are listed in the metadata-schema.json required array for each field. Others are not required for validation purposes.
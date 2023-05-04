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

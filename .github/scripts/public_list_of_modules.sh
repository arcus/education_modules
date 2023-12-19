## This is a script to create the page with the list of modules.

page=automated_list_of_modules.md

# Create front matter for the page
echo "---
title: Educational Modules
---

This page includes a complete list of our published modules. 

We're also building a self-service tool to help you find the modules most relevant to you. 
Test out our [prototype module discovery application](https://learn.arcus.chop.edu/), and please leave feedback to help us improve!

" > $page

# Start the table
echo "| Training Course | Description | Estimated Time | Collection | Coding Language | Task | Domain |
| -- | -- | -- | -- | -- | -- | -- |" >> $page

for FOLDER in *
do
    if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" ]]      ## Only do this for folders that have a course .md file inside an identically named folder in education_modules
    then

        title="`grep -m 1 "title": $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"

        comment="`grep -m 1 comment: $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"
        comment=${comment//"\""/"\\\""} #add escape characters to quotes
        
        estimated_time_in_minutes="`grep -m 1 "estimated_time_in_minutes": $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"
        
        collection="`grep -m 1 "collection": $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"
        collection=${collection//"_"/" "} #replace _ with spaces

        coding_language="`grep -m 1 "coding_language": $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"
                
        task="`grep -m 1 "data_task": $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"
                
        domain="`grep -m 1 "data_domain": $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"

        
        echo "| [$title](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/$FOLDER/$FOLDER.md) | $comment | $estimated_time_in_minutes min| $collection | $coding_language | $task | $domain |" >> $page

    fi
done
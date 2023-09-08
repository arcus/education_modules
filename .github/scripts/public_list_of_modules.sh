## This is a script to create the page with the list of modules.

page=list_of_modules.md

# Create front matter for the page
echo "---
title: Educational Modules
---

We understand that waiting for a cohort and guided curriculum might be too long to wait, so you are welcome to explore these materials on your own. The benefits of waiting and participating in our research include receiving a customized curriculum of materials and the peership and support of a community of learners like you. To express interest in participating in research, please fill out the [DART interest form](https://redcap.chop.edu/surveys/?s=FPHWFNEA9KN3HERF) or go directly to our [research screening form](https://redcap.link/DART-survey).

If you do access any of these modules, please fill out the module feedback survey at the end to let us know what you think." > $page

# Start the table
echo "| Training Course | Description | Estimated Time | Coding Language |
| -- | -- | -- | -- |" >> $page

for FOLDER in *
do
    if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" ]]      ## Only do this for folders that have a course .md file inside an identically named folder in education_modules
    then
        ### pull the one-line macros, process "comment" and "long_description" separately due to possible double quotes
        # for CATEGORY in  "author" "email" "version" "current_version_description" "module_type" "docs_version" "language" "narrator" "mode" "title" "estimated_time_in_minutes" "module_type" "good_first_module" "data_domain" "data_task" "coding_required" "coding_level" "coding_language" "sequence_name" "previous_sequential_module" #"comment" "long_description"
        # do
        #     category_metadata="`grep -m 1 "$CATEGORY": $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"
        #     echo "df.loc[\"$FOLDER\", \"$CATEGORY\"] = \"$category_metadata\"" >> $metadata_df
        # done
        title="`grep -m 1 "title": $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"
        estimated_time_in_minutes="`grep -m 1 "estimated_time_in_minutes": $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"
        coding_language="`grep -m 1 "coding_language": $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"

        #### TODO Some comments and long descriptions contain double quotes... this is a problem. For the moment they have been replaced with the character +
      
        comment="`grep -m 1 comment: $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]' | tr '"' '+'`"
        
        echo "| [$title](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/$FOLDER/$FOLDER.md) | $comment | $estimated_time_in_minutes minutes| $coding_language |" >> $page

    fi
done
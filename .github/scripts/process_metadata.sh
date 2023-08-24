### This script will create the file module_data.py
### Run this script from the main education_modules directory

metadata_df=assets/metadata/module_data.py

### Set up the basics of creating a pandas dataframe
echo "import pandas as pd
df=pd.DataFrame()" > $metadata_df
echo >> $metadata_df


for FOLDER in *
do
    if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" ]]      ## Only do this for folders that have a course .md file inside an identically named folder in education_modules
    then
        ### pull the one-line macros, process "comment" and "long_description" separately due to possible double quotes
        for CATEGORY in  "author" "email" "version" "current_version_description" "module_type" "docs_version" "language" "narrator" "mode" "title" "estimated_time_in_minutes" "module_type" "good_first_module" "data_domain" "data_task" "coding_required" "coding_level" "coding_language" "sequence_name" "previous_sequential_module" #"comment" "long_description"
        do
            category_metadata="`grep -m 1 "$CATEGORY": $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"
            echo "df.loc[\"$FOLDER\", \"$CATEGORY\"] = \"$category_metadata\"" >> $metadata_df
        done

        #### TODO Some comments and long descriptions contain double quotes... this is a problem. For the moment they have been replaced with the character +
      
        comment="`grep -m 1 comment: $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]' | tr '"' '+'`"
        echo "df.loc[\"$FOLDER\", \"comment\"] = \"$comment\" " >> $metadata_df
        
        long_description="`grep -m 1 long_description: $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]' | tr '"' '+'`"
        echo "df.loc[\"$FOLDER\", \"long_description\"] = \"$long_description\" " >> $metadata_df


        #### pull the block macros. To speed up the process because not all of these are necessarily present, there is an IF statement.

        for BLOCK_MACRO in "pre_reqs" "learning_objectives" "sets_you_up_for" "depends_on_knowledge_in" "is_parallel_to" "version_history"
        do
            if grep $BLOCK_MACRO -q $FOLDER/$FOLDER.md
            then
                start=$(( $(grep -n -m 1 $BLOCK_MACRO $FOLDER/$FOLDER.md  | cut -f1 -d:) +1 ))

                end=$(( $(tail -n +$start $FOLDER/$FOLDER.md | grep -n -m 1 "@end" | cut -f1 -d:) - 1 ))
                #### TODO figure out a better solution to line breaks instead of just replacing them with & symbols!
                macro_contents=$(tail -n +$start $FOLDER/$FOLDER.md | head -n $end | tr '\n' '&' | tr '"' '+')
                echo "df.loc[\"$FOLDER\", \"$BLOCK_MACRO\"] = \"$macro_contents\" " >> $metadata_df
            fi
        done
    fi
done

### Find all links to other modules:

echo  "df[\"Linked Courses\"] = [list() for x in range(len(df.index))]" >> $metadata_df

for FOLDER in *
do
  if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" != "a_sample_module_template" ]] 
  then
    echo "a = df.loc[\"$FOLDER\", \"Linked Courses\"]" >> $metadata_df
    for LINKED_COURSE in *
    do
      if [[ -s $LINKED_COURSE/$LINKED_COURSE.md && "$LINKED_COURSE" != "a_sample_module_template" && "$LINKED_COURSE" != "$FOLDER" ]] 
      then
#          echo $FOLDER, $LINKED_COURSE
         if [ "$(grep -c $LINKED_COURSE $FOLDER/$FOLDER.md)" -ge 1 ]
           then
             echo "a.append(\"$LINKED_COURSE\")" >> $metadata_df
             
         fi

      fi 
    done
    echo "df.at[\"$FOLDER\", \"Linked Courses\"] = list(a)" >> $metadata_df
  fi
done

### add a line so running the file also writes the dataframe to a csv

echo "df.to_csv('assets/metadata/module_data.csv')" >> $metadata_df
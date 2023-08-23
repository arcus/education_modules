### This script will create the file knowledge_graph.py containing all of the possible data for visualizing connections between modules.
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

      ### Start pulling the data from block macros. So far there is only one of those. First find the line number where the "@learning_objectives" first appears
      start=$(( $(grep -n -m 1 "@learning_objectives" $FOLDER/$FOLDER.md  | cut -f1 -d:) +1 ))

      end=$(( $(tail -n +$start $FOLDER/$FOLDER.md | grep -n -m 1 "@end" | cut -f1 -d:) - 1 ))
      #### TODO figure out line breaks!
      learning_objectives=$(tail -n +$start $FOLDER/$FOLDER.md | head -n $end | tr '\n' '&' | tr '"' '+')
      echo "df.loc[\"$FOLDER\", \"learning_objectives\"] = \"$learning_objectives\" " >> $metadata_df

      #### pre_reqs (The "IF" is because not every module has the prereqs in this format yet...)
      if grep "@pre_reqs" -q $FOLDER/$FOLDER.md
      then
        start=$(( $(grep -n -m 1 "@pre_reqs" $FOLDER/$FOLDER.md  | cut -f1 -d:) +1 ))

        end=$(( $(tail -n +$start $FOLDER/$FOLDER.md | grep -n -m 1 "@end" | cut -f1 -d:) - 1 ))
        #### TODO figure out line breaks!
        pre_reqs=$(tail -n +$start $FOLDER/$FOLDER.md | head -n $end | tr '\n' '&' | tr '"' '+')
        echo "df.loc[\"$FOLDER\", \"Prerequisties\"] = \"$pre_reqs\" " >> $metadata_df
      fi

      #### sets_you_up_for (The "IF" is because not every module has this yet...)
      if grep "@sets_you_up_for" -q $FOLDER/$FOLDER.md
      then
        start=$(( $(grep -n -m 1 "@sets_you_up_for" $FOLDER/$FOLDER.md  | cut -f1 -d:) +1 ))

        end=$(( $(tail -n +$start $FOLDER/$FOLDER.md | grep -n -m 1 "@end" | cut -f1 -d:) - 1 ))
        
        sets_you_up_for=$(tail -n +$start $FOLDER/$FOLDER.md | head -n $end | tr '\n' ' ' | tr '-' ' ')
        echo "df.loc[\"$FOLDER\", \"Sets You Up For\"] = \"$sets_you_up_for\" " >> $metadata_df
      fi

      #### depends_on_knowledge_available_in (The "IF" is because not every module has this yet...)
      if grep "@depends_on_knowledge_available_in" -q $FOLDER/$FOLDER.md
      then
        start=$(( $(grep -n -m 1 "@depends_on_knowledge_available_in" $FOLDER/$FOLDER.md  | cut -f1 -d:) +1 ))

        end=$(( $(tail -n +$start $FOLDER/$FOLDER.md | grep -n -m 1 "@end" | cut -f1 -d:) - 1 ))
        
        depends_on_knowledge_available_in=$(tail -n +$start $FOLDER/$FOLDER.md | head -n $end | tr '\n' ' ' | tr '-' ' ')
        echo "df.loc[\"$FOLDER\", \"Depends On Knowledge In\"] = \"$depends_on_knowledge_available_in\" " >> $metadata_df
      fi
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

### Debugging code, modify as needed:

#echo "print(df.loc[:,[\"coding_required\", \"coding_language\", \"coding_level\", \"sequence_name\", \"next_sequential_module\"]])">>$metadata_df
#
#
#python assets/module_discovery_app/module_data.py
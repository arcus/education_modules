### This script will create the file module_data.csv
### Run this script from the main education_modules directory

metadata_df=module_data.csv

#Use ; as the separators for this csv since many metadata categories themselves contain commas.
echo "SEP=;" > $metadata_df

#Create the headers for the csv
headers="module_id"
for CATEGORY in  "author" "email" "version" "current_version_description" "module_type" "docs_version" "language" "narrator" "mode" "title" "estimated_time_in_minutes" "good_first_module" "data_domain" "data_task" "collection" "coding_required" "coding_level" "coding_language" "sequence_name" "previous_sequential_module" "comment" "long_description"
  do
    headers+="; $CATEGORY"
  done
for BLOCK_MACRO in "pre_reqs" "learning_objectives" "sets_you_up_for" "depends_on_knowledge_available_in" "is_parallel_to" "version_history"
  do 
    headers+="; $BLOCK_MACRO"
  done
echo $headers >> $metadata_df


for FOLDER in *
do
    if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" ]]      ## Only do this for folders that have a course .md file inside an identically named folder in education_modules
    then
      ### start building the line for that folder that will be written to the csv
      module_metadata="$FOLDER"
        ### pull the one-line macros
        for CATEGORY in  "author" "email" "version" "current_version_description" "module_type" "docs_version" "language" "narrator" "mode" "title" "estimated_time_in_minutes" "good_first_module" "data_domain" "data_task" "collection" "coding_required" "coding_level" "coding_language" "sequence_name" "previous_sequential_module" "comment" "long_description"
        do
            category_metadata="`grep -m 1 "$CATEGORY": $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"
            #Add the category metadata to the line, being sure to replace any semicolons with commas (apologies to the library scientists who used them in their grammatically correcly)
            module_metadata=$module_metadata"; "${category_metadata//;/,}
        done

        #### pull the block macros

        for BLOCK_MACRO in "pre_reqs" "learning_objectives" "sets_you_up_for" "depends_on_knowledge_available_in" "is_parallel_to" "version_history"
        do
            if grep $BLOCK_MACRO -q $FOLDER/$FOLDER.md
            then
                start=$(( $(grep -n -m 1 $BLOCK_MACRO $FOLDER/$FOLDER.md  | cut -f1 -d:) +1 ))

                end=$(( $(tail -n +$start $FOLDER/$FOLDER.md | grep -n -m 1 "@end" | cut -f1 -d:) - 1 ))
                #### TODO figure out a better solution to line breaks instead of just replacing them with & symbols! For the moment the cat -e command replaces line breaks with $
                macro_contents=$(tail -n +$start $FOLDER/$FOLDER.md | head -n $end | cat -e)
                macro_contents=${macro_contents//"$"/"\\n"}
            else 
              macro_contents=""
            fi
            module_metadata=$module_metadata"; ""${macro_contents//;/,}"

        done
    
    echo $module_metadata >> $metadata_df
    fi
done

### Find all links to other modules:

#echo  "df[\"Linked Courses\"] = [list() for x in range(len(df.index))]" >> $metadata_df

# for FOLDER in *
# do
#   if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" != "a_sample_module_template" ]] 
#   then
#     echo "a = df.loc[\"$FOLDER\", \"Linked Courses\"]" >> $metadata_df
#     for LINKED_COURSE in *
#     do
#       if [[ -s $LINKED_COURSE/$LINKED_COURSE.md && "$LINKED_COURSE" != "a_sample_module_template" && "$LINKED_COURSE" != "$FOLDER" ]] 
#       then
# #          echo $FOLDER, $LINKED_COURSE
#          if [ "$(grep -c $LINKED_COURSE $FOLDER/$FOLDER.md)" -ge 1 ]
#            then 
#             # echo "a.append(\"$LINKED_COURSE\")" >> $metadata_df
             
#          fi

#       fi 
#     done
#     echo "df.at[\"$FOLDER\", \"Linked Courses\"] = list(a)" >> $metadata_df
#   fi
# done
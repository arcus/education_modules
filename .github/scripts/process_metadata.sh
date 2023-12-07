### This script will create the file module_data.csv
### Run this script from the main education_modules directory

metadata_df=module_data.json

echo '[' > $metadata_df
# #Create the headers for the csv
# headers="module_id"
# for CATEGORY in  "author" "email" "version" "current_version_description" "module_type" "docs_version" "language" "narrator" "mode" "title" "estimated_time_in_minutes" "good_first_module" "data_domain" "data_task" "collection" "coding_required" "coding_level" "coding_language" "sequence_name" "previous_sequential_module" "comment" "long_description"
#   do
#     headers+=", $CATEGORY"
#   done
# for BLOCK_MACRO in "pre_reqs" "learning_objectives" "sets_you_up_for" "depends_on_knowledge_available_in" "is_parallel_to" "version_history"
#   do 
#     headers+=", $BLOCK_MACRO"
#   done
# headers+=", Linked Courses"
# #echo $headers > $metadata_df


for FOLDER in *
do
    if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" ]]      ## Only do this for folders that have a course .md file inside an identically named folder in education_modules
    then
      ### start building the line for that folder that will be written to the csv
      echo '{' >> $metadata_df
      echo "\"module_id\": \"$FOLDER\"," >>$metadata_df
        ### pull the one-line macros
        for CATEGORY in  "author" "email" "version" "current_version_description" "module_type" "docs_version" "language" "narrator" "mode" "title" "estimated_time_in_minutes" "good_first_module" "data_domain" "data_task" "collection" "coding_required" "coding_level" "coding_language" "sequence_name" "previous_sequential_module" "comment" "long_description"
        do
            category_metadata="`grep -m 1 "$CATEGORY": $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"
            category_metadata=${category_metadata//"\""/"\\\""} #add escape characters to quotes
            #category_metadata=${category_metadata//";"/"\[semicolon\]"} #replace semicolons with commas
            #Add the category metadata to the line
            echo "\"$CATEGORY\": \"$category_metadata\"," >> $metadata_df
        done

        #### pull the block macros

        for BLOCK_MACRO in "pre_reqs" "learning_objectives" "sets_you_up_for" "depends_on_knowledge_available_in" "is_parallel_to" "version_history"
        do
            if grep $BLOCK_MACRO -q $FOLDER/$FOLDER.md
            then
                start=$(( $(grep -n -m 1 $BLOCK_MACRO $FOLDER/$FOLDER.md  | cut -f1 -d:) +1 ))

                end=$(( $(tail -n +$start $FOLDER/$FOLDER.md | grep -n -m 1 "@end" | cut -f1 -d:) - 1 ))
                ### Process the contents of the block macro for the csv
                macro_contents=$(tail -n +$start $FOLDER/$FOLDER.md | head -n $end | cat -e | tr -d '\n' ) #print that section with $ for line breaks, removing actual line breaks so it is a single line
                macro_contents=${macro_contents//"$"/"\\n"} #replace $ for line breaks with \n for easier use later
                macro_contents=${macro_contents//"\""/"\\\""} #replace quotes with the unicode for quotes
                #macro_contents=${macro_contents//";"/"\[semicolon\]"} #replace semicolons with commas
                echo "\"$BLOCK_MACRO\": \"$macro_contents\"," >> $metadata_df
            #else 
              #macro_contents="" # maintain the tabular format when a module doesn't have a particular block macro
            fi
            #module_metadata=$module_metadata", \""$macro_contents"\"" ### QUESTION: does the additional quotes around macro_contents here create the problem if there is a * is the block macro? Or is it a different problem? 
        done
      
      ## add a final column with all of the linked courses
      links=""
      for LINKED_COURSE in *
        do
          if [[ -s $LINKED_COURSE/$LINKED_COURSE.md && "$LINKED_COURSE" != "a_sample_module_template" && "$LINKED_COURSE" != "$FOLDER" ]] 
          then
            if [ "$(grep -c $LINKED_COURSE $FOLDER/$FOLDER.md)" -ge 1 ]
              then 
                links=$links$LINKED_COURSE" "
            fi
          fi 
        done
      echo "\"Linked Course\":\"$links\"" >> $metadata_df   

    ## close the json entry
    echo "}," >> $metadata_df
    fi
done
echo "{}" >>$metadata_df
echo "]" >> $metadata_df

### Find all links to other modules:

# links=""
# #echo  "df[\"Linked Courses\"] = [list() for x in range(len(df.index))]" >> $metadata_df

# for FOLDER in *
# do
#   if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" != "a_sample_module_template" ]] 
#   then
#     #echo "a = df.loc[\"$FOLDER\", \"Linked Courses\"]" >> $metadata_df
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
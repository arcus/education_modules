### This script will create the file knowledge_graph.py containing all of the possible data for visualizing connections between modules.

graph_data=knowledge_graphing/module_data.py

echo "import pandas as pd
df=pd.DataFrame()" > $graph_data


### Make every module a graph node

echo >> $graph_data

for FOLDER in *
do
  if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" != "a_sample_module_template" ]]      ## Only do this for folders that have a course .md file inside an identically named folder in education_modules
    then
      ### pull the one-line macros
      title="`grep -m 1 title: $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"
      echo "df.loc[\"$FOLDER\", \"title\"] = \"$title\" " >> $graph_data
      author="`grep -m 1 author: $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"
      echo "df.loc[\"$FOLDER\", \"author\"] = \"$author\" " >> $graph_data
      estimated_time="`grep -m 1 estimated_time: $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"
      echo "df.loc[\"$FOLDER\", \"time\"] = \"$estimated_time\" " >> $graph_data
      
      #### TODO Some comments and long descriptions contain double quotes... this is a problem. For the moment they have been replaced with the character +
      comment="`grep -m 1 comment: $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]' | tr '"' '+'`"
      echo "df.loc[\"$FOLDER\", \"comment\"] = \"$comment\" " >> $graph_data
      long_description="`grep -m 1 long_description: $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]' | tr '"' '+'`"
      echo "df.loc[\"$FOLDER\", \"long_description\"] = \"$long_description\" " >> $graph_data

      ### Start pulling the data from block macros. So far there is only one of those. First find the line number where the "@learning_objectives" first appears
      start=$(( $(grep -n -m 1 "@learning_objectives" $FOLDER/$FOLDER.md  | cut -f1 -d:) +1 ))

      end=$(( $(tail -n +$start $FOLDER/$FOLDER.md | grep -n -m 1 "@end" | cut -f1 -d:) - 1 ))
      #### TODO
      learning_objectives=$(tail -n +$start $FOLDER/$FOLDER.md | head -n $end | tr '\n' '&' | tr '"' '+')
      echo "df.loc[\"$FOLDER\", \"Learning Objectives\"] = \"$learning_objectives\" " >> $graph_data
      
      ### pull derived data about what modules this module links to
      # echo "df.loc[\"$FOLDER\", \"Linked Courses\"] = [] " >> $graph_data
      # for LINKED_COURSE in *
      # do
      #   if [[ -s $LINKED_COURSE/$LINKED_COURSE.md && "$LINKED_COURSE" != "a_sample_module_template" && "$LINKED_COURSE" != "$FOLDER" ]] 
      #   then
      #     if [ "$(grep -c $LINKED_COURSE $FOLDER/$FOLDER.md)" -ge 1 ]
      #       then
      #         echo "df.loc[\"$FOLDER\", \"Linked Courses\"] = df.loc[\"$FOLDER\", \"Linked Courses\"].append($LINKED_COURSE)" >> $graph_data
      #     fi

      #   fi 
      # done

  fi
done

echo  "df[\"Linked Courses\"] = [list() for x in range(len(df.index))]" >> $graph_data

### Find all links to other modules:

for FOLDER in *
do
  if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" != "a_sample_module_template" ]] 
  then
    echo "a = df.loc[\"$FOLDER\", \"Linked Courses\"]" >> $graph_data
    for LINKED_COURSE in *
    do
      if [[ -s $LINKED_COURSE/$LINKED_COURSE.md && "$LINKED_COURSE" != "a_sample_module_template" && "$LINKED_COURSE" != "$FOLDER" ]] 
      then
#          echo $FOLDER, $LINKED_COURSE
         if [ "$(grep -c $LINKED_COURSE $FOLDER/$FOLDER.md)" -ge 1 ]
           then
             echo "a.append(\"$LINKED_COURSE\")" >> $graph_data
             
         fi

      fi 
    done
    echo "df.at[\"$FOLDER\", \"Linked Courses\"] = list(a)" >> $graph_data
  fi
done


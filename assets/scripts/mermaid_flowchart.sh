#############################
# try to generate a file that has mermaid flowchart of modules.
#############################

type=$1
classification=$2

echo $type
echo $classification
echo "graph LR" > flowcharts/$type$classification.md

###
for FOLDER in *
do
  if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" != "a_sample_module_template" ]]       ## Only do this for folders that have a real module inside them.
    then
      tag=`grep -m 1 "$type:" $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //"`  ## Pull out the tags from the yaml. This will also be able to be modified for a topic
      if [[ $tag == "$classification" ]]  ## Only do this for the modules that use the tag we want
        then
          module_title=`grep -m 1 "title:" $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]' | tr ',' ' '`
          echo "$FOLDER[$module_title];">>flowcharts/$type$classification.md ## This will make sure that nodes that show appear because they are the category show up even if they dont have any prereqs? maybe unneccessary...
          echo "click $FOLDER href \"https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/$FOLDER/$FOLDER.md\";">>flowcharts/$type$classification.md ##Make the mermaid box a clickable link to the liascript course.

      fi
  fi
done

for FOLDER in *
do
  if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" != "a_sample_module_template" ]]       ## Only do this for folders that have a real module inside them.
    then
      tag=`grep -m 1 "code_language:" $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //"`  ## Pull out the code_language from the yaml. This will also be able to be modified for a topic
      if [[ $tag == "$classification" ]]  ## Only do this for the modules that use the language we want
        then
          code_prereqs=`grep -m 1 "code_language_prereqs:" $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //"` ### what coding prereqs does this have (if any)
          topic_prereqs=`grep -m 1 "topic_prereqs:" $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //"` ### what topical prereqs does this have (if any)
          for prereq in $code_prereqs
          do
            if [[ "$prereq" != "none" ]] ##If a course has prereqs left blank... we can just make the QA force people to put "none" for their prereqs! What about prereqs that don't have to do with the same code language...? Maybe just have prereqs? Not differentiated based on code/topic
              then
                prereq_title=`grep -m 1 "title:" $prereq/$prereq.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]' | tr ',' ' '`
                module_title=`grep -m 1 "title:" $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]' | tr ',' ' '`
                echo "$prereq[$prereq_title] --> $FOLDER[$module_title];">>flowcharts/$type$classification.md  ##This creates the mermaid flow from the prereq course to the current course.
            fi
          done

          for prereq in $topic_prereqs
          do
            if [[ "$prereq" != "none" ]] ##If a course has prereqs left blank... we can just make the QA force people to put "none" for their prereqs!
              then
                prereq_title=`grep -m 1 "title:" $prereq/$prereq.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]' | tr ',' ' '`
                module_title=`grep -m 1 "title:" $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]' | tr ',' ' '`
                echo "$prereq[$prereq_title] -.-> $FOLDER[$module_title];">>flowcharts/$type$classification.md  ##This creates the mermaid flow from the prereq course to the current course.
                echo "click $prereq href \"https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/$prereq/$prereq.md\";">>flowcharts/$type$classification.md ##Make the mermaid box a clickable link to the liascript course.
            fi
          done
      fi
  fi
done

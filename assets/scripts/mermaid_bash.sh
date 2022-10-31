#############################
# try to generate a file that has mermaid flowchart of modules.
#############################

echo "graph BT" > mermaid_bash.md


for FOLDER in *
do
  if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" != "a_sample_module_template" ]]       ## Only do this for folders that have a real module inside them.
    then
      code_lang=`grep -m 1 "code_language:" $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //"`  ## Pull out the code_language from the yaml. This will also be able to be modified for a topic
      if [[ $code_lang == "Bash" ]]  ## Only do this for the modules that use the language we want
        then
          code_prereqs=`grep -m 1 "code_language_prereqs:" $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //"` ### make the code_language a variable
          for prereq in $code_prereqs
          do
            if [[ "$prereq" != "none" ]] ##If a course is not a prereq to anything and has no prereqs itself, it won't show up... hmmm.... that may be a problem
              then
                prereq_title=`grep -m 1 "title:" $prereq/$prereq.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]' | tr ',' ' '`
                module_title=`grep -m 1 "title:" $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]' | tr ',' ' '`
                echo "$prereq[$prereq_title] --> $FOLDER[$module_title];">>mermaid_bash.md  ##This creates the mermaid flow from the prereq course to the current course.
            fi
          done
      fi
  fi
done

### The click links need to be after the other stuff so we need to run through the modules of the type we care about again...
for FOLDER in *
do
  if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" != "a_sample_module_template" ]]       ## Only do this for folders that have a real module inside them.
    then
      code_lang=`grep -m 1 "code_language:" $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //"`  ## Pull out the code_language from the yaml. This will also be able to be modified for a topic
      if [[ $code_lang == "Bash" ]]  ## Only do this for the modules that use the language we want
        then
          echo "click $FOLDER href \"https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/$FOLDER/$FOLDER.md\";">>mermaid_bash.md ##Make the mermaid box a clickable link to the liascript course.

      fi
  fi
done

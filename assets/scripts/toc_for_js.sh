#############################
# This is a .csv file for use visualizing the modules in d3
#############################

# This file has a different columns than the .md table since it is for backend analysis rather than displaying to the public.

csvCOLUMNS="title code_language topic"

csvHEADINGS=" \"title\" ; \"code_language\"; \"topic\" "

#for COL in $csvCOLUMNS
#  do
#    csvHEADINGS+="\"$COL\" ; "
#done

echo $csvHEADINGS > TOC_for_js.csv

# Add a row for each module, this time the sample module is included

for FOLDER in *
do
  if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" != "a_sample_module_template" ]]       ## Only do this for folders that have a real module inside them.
    then
      ROW=''
      for COL in $csvCOLUMNS
        do
          ROW+=" \"`grep -m 1 $COL: $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]' | tr ',' ' '`\";"  # Pull the YAML entry but remove excess white space at the front, as well as any unprintable characters or commas
        done
      ROW=${ROW%;}
      echo $ROW >> TOC_for_js.csv
  fi
done

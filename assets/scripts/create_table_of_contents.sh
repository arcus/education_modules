#!/bin/bash

# This script should be run from the main education_modules directory
# With the command:
# bash assets/scripts/create_table_of_contents.sh
# It will create 3 files:
#   table_of_contents.md for our reference
#   table_of_contents.csv for analysis
#   site_table_of_contents.md for display on our public facing website

#############################
# First we create the .md file
#############################

COLUMNS="title author email version comment estimated_time"

# Create a .md file with the column headings specified above

HEADINGS='| Link to Training Course | Markdown |'
BREAK='| -- | -- |'
for COL in $COLUMNS
do
  HEADINGS+=" $COL |"
  BREAK+=" -- |"
done

echo $HEADINGS > table_of_contents.md
echo $BREAK >> table_of_contents.md

# Create entries, with links to the liascript course and the .md files

for FOLDER in *
do
  if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" != "a_sample_module_template" ]]      ## Only do this for folders that have a course .md file inside an identically named folder in education_modules
    then
      ROW='|'
      ROW+=" [Training Course](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/$FOLDER/$FOLDER.md) |"
      ROW+=" [Markdown File](https://github.com/arcus/education_modules/blob/main/$FOLDER/$FOLDER.md) |"
      for COL in $COLUMNS
        do
          ROW+=" `grep -m 1 $COL: $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'` |"  # Pull the YAML entry but remove excess white space at the front, as well as any unprintable characters
        done
      echo $ROW >> table_of_contents.md
  fi
done

#############################
# Next we create the .csv file
#############################

# This file has a different columns than the .md table since it is for backend analysis rather than displaying to the public.

csvCOLUMNS="title author email estimated_time  version module_template_version language narrator code_language topic"

csvHEADINGS=""

for COL in $csvCOLUMNS
  do
    csvHEADINGS+="$COL , "
done

echo $csvHEADINGS > table_of_contents.csv

# Add a row for each module, this time the sample module is included

for FOLDER in *
do
  if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" != "a_sample_module_template" ]]       ## Only do this for folders that have a real module inside them.
    then
      ROW=''
      for COL in $csvCOLUMNS
        do
          ROW+=" `grep -m 1 $COL: $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]' | tr ',' ' '` ,"  # Pull the YAML entry but remove excess white space at the front, as well as any unprintable characters or commas
        done
      echo $ROW >> table_of_contents.csv
  fi
done


#############################
# This is an additional table of contents for use on our public facing website for learners and educators, not potential developers.
#############################

COLUMNS="title comment estimated_time"

# Create a .md file with the column headings specified above

HEADINGS='| Training Course | Description | Estimated Time |'
BREAK='|'
for COL in $COLUMNS
do
  BREAK+=" -- |"
done

echo $HEADINGS > site_table_of_contents.md
echo $BREAK >> site_table_of_contents.md

# Create entries, with links to the liascript course and the .md files

for FOLDER in *
do
  if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" != "a_sample_module_template"
]]      ## Only do this for folders that have a course .md file inside an identically named folder in education_modules
    then
      ROW='|'
      #create title as link to LiaScript
          ROW+=" [`grep -m 1 "title:" $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/$FOLDER/$FOLDER.md) |"  # Pull the YAML entry but remove excess white space at the front, as well as any unprintable characters
      #Add description
          ROW+=" `grep -m 1 "comment:" $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'` |"  # Pull the YAML entry but remove excess white space at the front, as well as any unprintable characters
      #Add estimated time
          ROW+=" `grep -m 1 "estimated_time:" $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'` |"  # Pull the YAML entry but remove excess white space at the front, as well as any unprintable characters
      #  done
      echo $ROW >> site_table_of_contents.md
  fi
done

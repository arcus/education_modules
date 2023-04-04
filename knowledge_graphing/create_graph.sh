### This script will create the file knowledge_graph.py containing all of the possible data for visualizing connections between modules.

graph_data=knowledge_graphing/graph_data.py

echo "import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()" > $graph_data


### Make every module a graph node

for FOLDER in *
do
  if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" != "a_sample_module_template" ]]      ## Only do this for folders that have a course .md file inside an identically named folder in education_modules
    then
      title="`grep -m 1 title: $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"
      author="`grep -m 1 author: $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"
      estimated_time="`grep -m 1 estimated_time: $FOLDER/$FOLDER.md | sed "s/^[^ ]* //" | sed "s/^[ ]* //" | tr -dc '[:print:]'`"
      create_node="G.add_node(\"$FOLDER\", title=\"$title\", author=\"$author\", estimated_time=\"$estimated_time\")"
      echo $create_node >> $graph_data
      echo "('$FOLDER', '$title', '$author', '$estimated_time'),"
  fi
done

### Find all links to other modules:

for FOLDER in *
do
  if [[ -s $FOLDER/$FOLDER.md && "$FOLDER" != "a_sample_module_template" ]] 
  then
    for LINKED_COURSE in *
    do
      if [[ -s $LINKED_COURSE/$LINKED_COURSE.md && "$LINKED_COURSE" != "a_sample_module_template" && "$LINKED_COURSE" != "$FOLDER" ]] 
      then
#          echo $FOLDER, $LINKED_COURSE
         if [ "$(grep -c $LINKED_COURSE $FOLDER/$FOLDER.md)" -ge 1 ]
           then
             create_edge="G.add_edge(\"$FOLDER\", \"$LINKED_COURSE\", link_type=\"internal_link\")"
             echo $create_edge >> $graph_data
             #echo "('$FOLDER', '$LINKED_COURSE'),"
         fi

      fi 
    done
  fi
done


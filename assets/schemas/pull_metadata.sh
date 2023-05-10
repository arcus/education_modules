### This is a script to pull the metadata 

file=$1 

### Find the line number where the "@learning_objectives" first appears
start=$(( $(grep -n -m 1 "@learning_objectives" $file  | cut -f1 -d:) +1 ))

end=$(( $(tail -n +$start $file | grep -n -m 1 "@end" | cut -f1 -d:) - 1 ))

tail -n +$start $file | head -n $end 

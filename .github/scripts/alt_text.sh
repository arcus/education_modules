grep -rn --include=\*.md "\!\[\]"  | # search for lines with "![]" empty alt tag, only in markdown files
grep  -v "ISSUE_TEMPLATE" > issues #return only lines in files that are NOT in the issue template folder
 #bc QA issue templates include example code block showing empty tag for illustration

if [[ -s issues ]] # if file size > 0, ie there are issues with any of the markdown files
    then 
        echo "File paths + lines with missing alt text" 
        cat issues # for end user clarity on what needs to be fixed in each file -- when fails, they can go look at output to see what the issue is. 
        false
fi
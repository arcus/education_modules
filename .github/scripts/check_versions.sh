#!/bin/bash
awk 'BEGIN { RS = "diff --git" }   # splits diff file such that each file represented in the diff is treated as an individual record. each record is processed individually with the below statements
{
    if (system("bash .github/scripts/is_module.sh " $1 " || bash .github/scripts/is_docs_or_macros.sh " $1 )  == 0)
        { 
            if ( $0 ~ /\/dev\/null/ ) # is this a module file being uploaded for the first time? 
                { 
                    version_line_index=match ($0, /\+version:[^\n]+/) # gets the starting index of where the pattern is matched, sets RSTART to that value, and RLENGTH to the length of pattern match.
                    extracted_version_line=substr($0, RSTART, RLENGTH)  # pulls out the substring that matches.
                    system( "version_number=$(echo " extracted_version_line " | tr -d \"\\+version:\"); if [ $version_number != \"1.0.0\" ]; then echo \"New module "$1" version number needs to be 1.0.0\" >> version_issues ; fi  " )
                    # trims the extracted version line to now just contain the version number itself. Checks if it is equal to 1.0.0, and adds message to list of issues if not. 
                }
            else if ( $0 ~ /\+version:/) # is there a new version line? 
                { 
                    version_line_index=match ($0, /(-version:.*\+version:[^\n]+)/) # gets the starting index of where the pattern is matched, sets RSTART to that value
                    # regex used above accounts for the fact that there may be other lines displayed in the diff in between old and new version lines
                    extracted_version_lines=substr($0,RSTART,RLENGTH) # pulls out the substring that matches.
                    system("bash -c '\''issue=$(grep \"[+-]version:\" <<<  \""extracted_version_lines "\"| sed \"s/[+-]version://g\"| bash .github/scripts/version_values_comparison.sh); if [ -n \"$issue\" ]; then echo \""$1": $issue\" >> version_issues ; fi'\''")
                    # removes any extra lines from diff by grepping for only lines with +/- version, then trims the line to just contain version number itself. if issue string is not null (ie, value comparison script returns issue messages), adds messages to list of issues. 
                }
            else
                {
                    print $1 " does not have an updated version number" >> "version_issues"
                }
        }
    else 
        {  
            #do nothing, as only modules need to be checked for version number incrementation. 
        }
    
} ' "$1"

if [[ -s version_issues ]] # if file size > 0, ie there are issues with any of the modules
    then 
        echo "Issues with version numbers:" 
        cat version_issues # for end user clarity on what needs to be fixed in each module -- when fails, they can go look at output to see what the issue is. 
        false
fi

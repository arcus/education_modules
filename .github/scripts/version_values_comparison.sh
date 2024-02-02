awk -F "." 'BEGIN {FS="\\.|\n."; RS = "\n\n" } 
{
    if ( NF != 6 ) # if more or less than 6 fields are parsed, that means there is something wrong either with the formatting of the version numbers, or there is more than one version line being added to the module.
        {
            print "There is something unexpected happening with the version numbers. Ensure that the current version of the file only has one version field listed in the header, and that the appropriate number structure is followed."
        }  
    else 
        {
            if ( $1 == $4 ) #if old major = new major
                { 
                    if ($2==$5) # if old minor = new minor
                        {
                            if ( $3==$6)  # old revision = new revision
                                { 
                                    print "The version numbers are identical. Appropriately increment the number" # realistically, shouldnt ever actually happen unless the only edit is to add or remove whitespace. 
                                } 
                            else 
                                { 
                                    if ( $3+1==$6) # old revision plus one = new revision
                                        {
                                            # do nothing
                                        }
                                    
                                    else 
                                        { 
                                            print "Revision does not equal old revision plus one. Please review the versioning guidelines and update this module accordingly. " 
                                        }
                                } 
                        }
                    else 
                        {
                            if ( $2+1==$5 && $6 == 0 ) 
                                {
                                    #do nothing
                                }
                            else 
                                {
                                    print "Seems like minor was not incremented by just one, or revision was not set back to zero. Please review the versioning guidelines and update this module accordingly." 
                                }
                        }
                }
            else 
                { 
                    if ($1+1==$4  && $5 == 0 && $6 == 0)
                        {
                            #do nothing
                        }
                    else 
                        {
                            print "Major either changed by something other than one, or the other numbers did not reset to zero. Please review the versioning guidelines and update this module accordingly." 
                        }
                }
        } 
} ' 
'''
This file is a python script which reads from a log file
named "logs.txt" and steps through it line by line to take
the component name, directory, and error message using a regular
expression. It then sorts them by component, renames component
to the feature it corresponds to, sorts alphabetically, and 
takes out duplicates (using dictionaries). Then prints the 
sorted nested dictionary neatly.

'''


#import regular expression function
import re


#open log file
logfile=open("err_logs.txt")


#setup the regular expression
#
#                          group1 group2       group3      *the whole expression is group0
re = re.compile("halon-src/(.+?)/(.+?):\d+:\s+.*?\((.*)")


#define the outer-level dictionary named dict1
dict = {}


#loop to step through log file line by line
for line in logfile:
    #find matches
    matches = re.search(line)
    if matches:
        #add to a dictionary the key being component and value being
        #a nested dictionary with key being error message and value
        #being another nested dictionary with key being directory
        #and value being count of how many times that error has occured
        count=0
        if matches.group(1) in dict.keys():
            if matches.group(3) in dict[matches.group(1)].keys():
                if matches.group(2) in dict[matches.group(1)][matches.group(3)].keys():
                    dict[matches.group(1)][matches.group(3)][matches.group(2)]=dict[matches.group(1)][matches.group(3)][matches.group(2)]+1 
                else:
                    dict[matches.group(1)][matches.group(3)].update({matches.group(2):1})
            else:
                dict[matches.group(1)].update({matches.group(3):{matches.group(2):1}})
        else:
            dict.update({matches.group(1):{matches.group(3):{matches.group(2):1}}})
	

#close the file	
logfile.close()


#print the dictionary by feature, then errormessage, then directory
for component in sorted(dict.iterkeys()):
    #print the component
    print (component)
    errordict=dict[component]
    for errormsg in sorted(errordict.iterkeys()):
        #inside the component print the error message
        print '    {}'.format(errormsg)
        directorydict=errordict[errormsg]
        for directory in sorted(directorydict.iterkeys()):
            #inside the error message print the directory and count
            print '        {} : {}'.format(directory, dict[component][errormsg][directory])
            
            
#end of program

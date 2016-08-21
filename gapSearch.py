#! /usr/bin/python3
# gapSearch.py -  Looks for gaps in numbering scheme of file names

import os, sys, re

# Folder name. Change to dynamic later
foldername = '/home/tso/Documents/Python Files/gapSearch'
print('Performing check in: ' + foldername)

# Regex for numeric sequence at end
digitRegex = re.compile(r'\d+$')

## Manual file name input
## Retrieve sample prefix
##print('Please enter name of first file in sequence (with extension)')
##while True:
##    filename = input()
##    # Split the filename
##    nameSplit = filename.split('.')
##    # Validate file extension exists
##    if len(nameSplit) < 2:
##        print('Extension missing. Please try again: ')
##    # Validate number sequence exists
##    elif digitRegex.search(nameSplit[-2]) == None:
##        print('No digit sequence in name. Please try again: ')
##    # Validate file eactually exists in folder
##    elif not os.path.exists(os.path.join(foldername, filename)):
##        print('No such file exists in the folder. Please try again: ')    
##    else:
##        break

# Retrieve list of files in the folder
fileList = os.listdir(foldername)
# Reverse sort to retrieve name of last file
fileList.sort(reverse = True)
filename = fileList[0]
# Separate extension
nameSplit = filename.split('.')
# Retrieve the characters for the number sequence
mo = digitRegex.search(nameSplit[-2])
numSequence = mo.group()
# Retrieve rest of the file name
prefix = filename.split(numSequence)
# Expected count of files
count = int(numSequence)

# TODO: Add extra check for starting file count (if != 1)

# Check for gaps
for i in range(count):
    # Create filename based on same pattern
    checkFilename = prefix[0] + str(i+1).zfill(len(numSequence)) + \
                    '.' + nameSplit[-1]
    # Check for missing sequence
    if not os.path.exists(os.path.join(foldername, checkFilename)):
        print('Missing file: ' + checkFilename);
        # Create replacement file
        if not open(os.path.join(foldername, checkFilename), 'w') == None:
            print('Replacement file created!')
        else:
            print('Error creating new file.')

print ('Done!')

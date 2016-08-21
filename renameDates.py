#! /usr/bin/python3
# renameDates.py - Renames files with American format dates to European

import shutil, os

# Create a regex that matches the American date format MM-DD-YYYY
datePattern = re.compile(r'''^(.*?) # all text before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the date
    ((19|20)\d\d)                     # four digits for the year
    (.*?)$                          # all text after the date
    
''', re.VERBOSE)

# Loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date
    if mo == None:
        continue

    # Get the different parts of a filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European style file name
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart
                    + afterPart

    # Get the full, absolute paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files
    print ('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))

    print('Currently in test mode. Remove comment in script to affect files.')
    #shutil.move(amerFilename, euroFilename) # Remove comment to execute

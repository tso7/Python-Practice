#! /usr/bin/python3
# selectiveCopy.py - Walks through a folder and copies files based on
# specified extension


import os, shutil

# TODO: read from input arguments
sourceDir = '/home/tso/Downloads/automate_online-materials'
targetDir = '/home/tso/Documents/Python Files/selectiveCopy'
extension = 'txt'

# Walk through folder
for foldername, subfolders, filenames in os.walk(sourceDir):
    print('Searching files in %s...' % (foldername))
    for filename in filenames:
        # Check for valid extension
        if filename.endswith(extension):
            print ('Copying file ' + filename)
            # Copy file to destination folder
            shutil.copy(os.path.join(foldername, filename), targetDir)
print('Done')


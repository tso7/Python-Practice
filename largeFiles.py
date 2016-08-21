#! /usr/bin/python3
# largeFiles.py - Walks through a folder and returns files with large sizes
# Usage: largFiles.py <foldername>

import os, sys

# Define threshold size
sizeLimitMB = 10                     # Value in MB
sizeLimit = sizeLimitMB * 1024 * 1024 # Value in bytes

# Read cpmmand line argument
if len(sys.argv) != 2:
    print ('Invalid number of arguments. Usage: largeFiles.py <foldername>')
    sys.exit()

sourceDir = sys.argv[1]
sourceDir = os.path.abspath(sourceDir) # Ensure absolute path is retrieved

# Walk through folder
print('Current threshold limit is %s MB' % sizeLimitMB)
for foldername, subfolders, filenames in os.walk(sourceDir):
    print('Searching files in %s...' % (foldername))
    totalSize = 0
    for filename in filenames:
        # Check for large size
        fileSize = os.path.getsize(os.path.join(foldername, filename))
        totalSize += fileSize
        if fileSize > sizeLimit:
            print ('File: %s\nSize: %s MB' % (os.path.join(foldername, filename),
                                              round(fileSize/1024/1024,2)))
    # Check for large folders
    if totalSize > sizeLimit:
       print('Total folder size: %s MB' % round((totalSize/1024/1024), 2))
print('Done')


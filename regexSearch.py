#! /usr/bin/python3
# regexSearch.py - Program to looks up all text files in a folder for a string

import sys, re, os

# Check for valid parameters
if len(sys.argv) != 3:
    print('Incorrect number of arguments. Usage: regexSearch.py <folder> <regex>')
    sys.exit()

folder = sys.argv[1]
try:
    os.chdir(folder)
except FileNotFoundError:
    print('Invalid folder. Please try again.')
    sys.exit()

# Retrieve list of text files within folder

regex = re.compile(sys.argv[2])
fileList = os.listdir(folder)
for file in fileList:
    if '.txt' not in file:
        del fileList[fileList.index(file)]

for file in fileList:
    print ('Filename: ' + file)
    fileHandler = open(folder + file)
    content = fileHandler.read()
    print ('Matched regex: ')
    key = regex.search(content)
    for item in content.split('\n'):
        if key.group() in item:
            print (item.strip())
    fileHandler.close()
 
# Open each file one by one
print (fileList)
# Display matched expression

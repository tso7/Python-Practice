#! /usr/bin/python3
# madlibs.py - Program to read text file and prompt user for specific inputs.
#              Generated text is saved as a separate file.
# Usage: madlibs.py <filename> - Reads the input from the text file and exports
#        result to <filename_completed>

import sys, re

# Read the input text file

if len(sys.argv) != 2:
    print ('Invalid number of arguments. Usage: madlibs.py <filename>')
    sys.exit()

try:
    mlFile = open (sys.argv[1])
except FileNotFoundError:
    print('File not found. Please check the name and try again.')
    sys.exit()

content = mlFile.read()
mlFile.close()

# Fetch list of keywords to be changed
keywordRegex = re.compile ('ADJECTIVE|NOUN|ADVERB|VERB')
wordList = keywordRegex.findall(content)

# Fetch user input and replace
for word in wordList:
    if word.startswith('A'):
        print('Enter an ' + word.lower() + ':')
    else:
        print('Enter a ' + word.lower() + ':')
    content = re.sub(word, input(), content, 1)

# Display result and export text to new file
print(content)
extension = re.compile('(\.\w{2,4})?')
completedFile = extension.sub('', sys.argv[1])
completedFile += '_completed.txt'
mlFile = open(completedFile, 'w')
mlFile.write(content)
mlFile.close()

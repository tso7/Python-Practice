#! /usr/bin/python3
# regexStrip.py - Practice project to implement strip using regex

import re

message = "\t\n     The   quick brown fox   jumps over   the     lazy dog    \t"
print("Original string: ")
print (message)

def stripRegex(message, char = '\s'):
    if char != '\s':
        whitespaceRegex = re.compile('(' + char + ')+', re.I)
        print(whitespaceRegex.sub ('', message))
    else:
        whitespaceRegex = re.compile(r'^' + char + '*(.*)' + char + '*$')
        mo = whitespaceRegex.search(message)
        print(mo.group(1))

print("\nAfter processing: ")
stripRegex(message)
stripRegex(message, 'T')
stripRegex(message, ' ')
stripRegex(message, 'o')



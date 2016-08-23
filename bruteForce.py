#! /usr/bin/python3
# bruteForce.py - Brute forces a PDF decryption based on dictionary text
#
# Usage: bruteForce.py <filename>

import sys, PyPDF2

# Read command line arguments
if len(sys.argv) != 2:
    print('Invalid arguments. Please try again.')
    sys.exit()

filename = sys.argv[1]

# Read dictionary file into list (Currently static input and all UPPERCASE words)
dictionaryFile = open('dictionary.txt', 'r')
dictionaryInput = dictionaryFile.readlines()
dictionaryFile.close()
# Strip all the newlines and store in a new list
passwords = []
for i in range(len(dictionaryInput)):
    passwords.append(dictionaryInput[i].rstrip())

# Prepare PDF file
PdfReader = PyPDF2.PdfFileReader(open(filename, 'rb'))

# Check if actually encrypted
if PdfReader.isEncrypted:
    print('Hacking in progress...')
    count = 0
    for password in passwords:
        count += 1
        print(round(count/len(passwords)*100,2),end=' percent complete        \r')
        # Return password if successful
        if PdfReader.decrypt(password):
            print('Haha! The password is: ' + password)
            break
        # Lowercase
        if PdfReader.decrypt(password.lower()):
            print('Haha! The password is: ' + password.lower())
            break
    # If not found
    if password == passwords[-1]:
        print('\nUnsuccessful! :(')
else:
    print('File is already decrypted!')




            

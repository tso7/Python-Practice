#! /usr/bin/python3
# passwordStrength.py - Practice file to check password strength based on provided requirements

import re

print("Enter a password: ")
password = input()
while True:
    if re.search('\w{8,}', password) != None:
        if re.search('[a-z]+', password) != None:
            if re.search('[A-Z]+', password) != None:
                if re.search('[0-9]+', password) != None:
                    print ("Password OK")
                    break
                else:
                    print("Needs at least 1 digit")
            else:
                    print("Needs at least 1 upper case letter")
        else:
                    print("Needs at least 1 lower case letter")
    else:
                    print("Needs to be at least 8 characters")

    print("Weak password. Enter again: ")
    password = input()


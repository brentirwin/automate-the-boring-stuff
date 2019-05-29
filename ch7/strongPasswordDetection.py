#! python3
# strongPasswordDetection.py

'''
Write a function that uses regular expressions to make sure the password string
it is passed is strong. A strong password is defined as one that is at least
eight characters long, contains both uppercase and lowercase characters, and
has at least one digit. You may need to test the string against multiple regex
patterns to validate its strength.
'''

import re

def strongPassword(password):
    # patterns to match
    lengthRegex = re.compile(r'.{8}')
    upperRegex = re.compile(r'[A-Z]')
    lowerRegex = re.compile(r'[a-z]')
    digitRegex = re.compile(r'[0-9]')

    # compare against patterns
    lengthMo = lengthRegex.search(password)
    upperMo = upperRegex.search(password)
    lowerMo = lowerRegex.search(password)
    digitMo = digitRegex.search(password)

    # validate
    if (lengthMo == None or
        upperMo == None or
        lowerMo == None or
        digitMo == None):
            return False
    else:
        return True

password = input("Validate password: ")
if strongPassword(password):
    print("Valid")
else:
    print("Invalid")

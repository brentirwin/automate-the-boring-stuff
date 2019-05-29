#! python3
# regexStrip.py

'''
Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to strip,
then whitespace characters will be removed from the beginning and end of the
string. Otherwise, the characters specified in the second argument to the
function will be removed from the string.
'''

import re

def regexStrip(string, substring = None):
    # No substring
    if substring == None:
        # Find whitespace at beginning and/or end
        startSpaceRegex = re.compile(r'^\w+')
        endSpaceRegex = re.compile(r'\w+$')
        
        # Remove whitespace at beginning and/or end
        string = startSpaceRegex.sub('', string)
        string = endSpaceRegex.sub('', string)

        return string
    
    # Yes substring
    else:
        substringRegex = re.compile(substring)
        return substringRegex.sub('', string)

string = input("String: ")
substring = input("Substring: ")

if substring == '':
    print(regexStrip(string))
else:
    print(regexStrip(string, substring))

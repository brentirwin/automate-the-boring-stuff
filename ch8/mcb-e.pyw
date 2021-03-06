#! python3
'''
Extended version for exercise - Extend the multiclipboard program in this
chapter so that it has a delete <keyword> command line argument that will
delete a keyword from the shelf. Then add a delete command line argument that
will delete all keywords.
'''
# mcb-e.pyw - Saves and loads pieces of text to the clipboard.
# Usage:    py.exe mcb.pyw save <keyboard> - Saves clipboard to keyword.
#           py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#           py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    # Delete keyword
    if sys.argv[1].lower() == 'delete':
        keyword = sys.argv[2]
        if keyword in mcbShelf:
            del mcbShelf[keyword]
elif: len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(lsit(mcbShelf.keys())))
    # Delete all
    if sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    # Load content
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

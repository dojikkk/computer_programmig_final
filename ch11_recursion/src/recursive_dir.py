"""
Recursive directory traversals
"""

import os


def printAllFiles(directory):
    """Recursive directory traversal."""
    files = os.listdir(directory)
    for file in files:
        fullname = directory + '/' + file
        if os.path.isdir(fullname):
            printAllFiles(fullname)
        else:
            if os.path.isfile(fullname):
                print('File:', fullname)


def printAllFiles2(directory):
    """"Recursive directory traversal, guarded against OSError."""
    files = os.listdir(directory)
    for file in files:
        fullname = directory + '/' + file
        try:
            if os.path.isdir(fullname):
                printAllFiles2(fullname)
            else:
                print('File:', fullname)
        except OSError:
            print('Access denied to:' + fullname)


#
# Main program:
#
printAllFiles('C:/Users/')

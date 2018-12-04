import sys

from file_process_functions import isInputFilenameValid, processInputFile
from print_functions import printTopNEditors, printTopNEdits, printTopNArticles

#define the dictionaries to be used
editorsDictionary = {}
editsDictionary = {}
articlesDictionary = {}

while True:

    # Print the options for the user
    print(
        '''
        Please choose an option - for d, e and f, n is from 1 to 9
            a. QUIT
            b. HELP
            c. INPUT filename
            d. TOP n EDITORS
            e. TOP n EDITS
            f. TOP n ARTICLES
        '''
    )

    user_input = input(' ')
    user_input = user_input.lower()

    if (user_input == "quit"):
        sys.exit()
    elif (user_input == "help"):
        print("These are your options")
    elif (user_input[:6] == "input "):
        filename = user_input[6:]
        #check if the filename is valid and print error if not
        if isInputFilenameValid (filename) == True:
            processInputFile (filename, editorsDictionary, editsDictionary, articlesDictionary)
        else:
            print ("INVALID INPUT - try again")
    elif (user_input[:4] == "top "):
        if (user_input[6:] == "editors"):
            N = user_input[4]
            N = int(N)
            printTopNEditors (N, editorsDictionary)
        elif (user_input[6:] == "edits"):
            N = user_input[4]
            N = int(N)
            printTopNEdits (N, editsDictionary)
        elif (user_input[6:] == "articles"):
            N = user_input[4]
            N = int(N)
            printTopNArticles (N, articlesDictionary)
        else:
            print ("INVALID INPUT - try again")
    else:
        print ("INVALID input - try again")
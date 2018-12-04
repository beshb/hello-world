import pprint
import os
import re

def isInputFilenameValid(fileToCheckIfValid):
    dirContents = os.listdir()
    for filename in dirContents:
        if fileToCheckIfValid == filename:
            return True
    return False

def processInputFile (fileToOpen, editorsDictionaryToDatafill, editsDictionaryToDatafill, articlesDictionaryToDatafill):
    file = open(fileToOpen, "r")
    dataToProcess = file.readlines()

    for line in dataToProcess:
        wordsToProcess = line.split()
        if (line != '\n'):
            if (wordsToProcess[0] == 'REVISION') and re.match("[\w\d_-]", wordsToProcess[3]) and re.match("[\w\d_-]", wordsToProcess[5]):
                addToEditorsDictionary(wordsToProcess[5], wordsToProcess[3], editorsDictionaryToDatafill)
                addToEditsDictionary(wordsToProcess[3], wordsToProcess[5], editsDictionaryToDatafill)
                addToArticlesDictionary(wordsToProcess[3], wordsToProcess[5], articlesDictionaryToDatafill)
            else:
                continue
        else:
            continue
    file.close()
    return

#{editor: {set of articles revised by editor}}
def addToEditorsDictionary(editorToAdd, articleToAdd, realEditorsDictionary):
    if editorToAdd in realEditorsDictionary:
        for articlesAlreadyAdded in realEditorsDictionary[editorToAdd]:
            if articlesAlreadyAdded == articleToAdd:
                #pprint.pprint (realEditorsDictionary, width=1)
                return
            else:
                realEditorsDictionary[editorToAdd].append(articleToAdd)
                #pprint.pprint (realEditorsDictionary, width=1)
                return
    else:
        realEditorsDictionary[editorToAdd] = [articleToAdd]
    #print ("Editors Dictionary")
    #pprint.pprint (realEditorsDictionary, width=1)
    return


#{article: (total count of edits including duplicates, {set of editors who revised the article})}
def addToEditsDictionary(articleToAdd, editorToAdd, realEditsDictionary):
    if realEditsDictionary == {}:
        realEditsDictionary[articleToAdd] = [1, editorToAdd]
    else:
        if articleToAdd in realEditsDictionary:
            realEditsDictionary[articleToAdd][0] +=1
            if (editorToAdd in realEditsDictionary[articleToAdd]):
                return
            else:
                realEditsDictionary[articleToAdd].append(editorToAdd)
                return
        else:
            realEditsDictionary[articleToAdd] = [1, editorToAdd]
    #print ("Edits Dictionary")
    #print (realEditsDictionary)
    #pprint.pprint (realEditsDictionary, width=1)
    return


#{article: (count of edits, {set of editors who revised the article})}
def addToArticlesDictionary(articleToAdd, editorToAdd, realArticlesDictionary):
    if realArticlesDictionary == {}:
        realArticlesDictionary[articleToAdd] = [1, editorToAdd]
    else:
        if articleToAdd in realArticlesDictionary:
            if (editorToAdd in realArticlesDictionary[articleToAdd]):
                return
            else:
                realArticlesDictionary[articleToAdd][0] +=1
                realArticlesDictionary[articleToAdd].append(editorToAdd)
                return
        else:
            realArticlesDictionary[articleToAdd] = [1, editorToAdd]
    #print ("Articles Dictionary")
    #print (realArticlesDictionary)
    #pprint.pprint (realArticlesDictionary, width=1)
    return


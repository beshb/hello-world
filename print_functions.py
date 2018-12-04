import operator


# EDITORS – the editors who have revised the most articles (display the user name of the editor and the
# number of articles revised by that editor).
def printTopNEditors (n, editorsDictionary):
    print ("Top %d editors\r\r" % n)
    print ("Editors and Number of Articles")
    editorsDictionaryCounts = {}
    for i in sorted(editorsDictionary):
        editorsDictionaryCounts[i] = editorsDictionary[i]
    for key in editorsDictionaryCounts:
        editorsDictionaryCounts[key] = []
    for key, value in editorsDictionary.items():
        valueCount = len(list(filter(None, value)))
        editorsDictionaryCounts[key] = int(valueCount)
    for key in editorsDictionaryCounts:
        editorsMaxCount = 0
        for key in editorsDictionaryCounts:
            if editorsDictionaryCounts[key] > editorsMaxCount:
                editorsMaxCount = editorsDictionaryCounts[key]
    x=0
    while x < n:
        for entry in editorsDictionaryCounts:
            if (x < n) and (editorsDictionaryCounts[entry] == editorsMaxCount):
                print (entry, editorsDictionaryCounts[entry])
                x += 1
        editorsMaxCount -= 1
        if editorsMaxCount == 0:
            break
    return


# EDITS – the articles which have been revised the most often (display the
# title of the article and the number of times that article was revised).
def printTopNEdits (n, editsDictionary):
    print ("Top %d edits\r\r" % n)
    print ("Articles and Number of Revisions")
    editsDictionaryCounts = {}
    for k in sorted(editsDictionary):
        editsDictionaryCounts[k] = editsDictionary[k]
    for key in editsDictionaryCounts:
        valueCount = editsDictionaryCounts[key][0]
        editsDictionaryCounts[key][0] = int(valueCount)
    #print (editsDictionaryCounts)
    for key in editsDictionaryCounts:
        editsMaxCount = 0
        for key in editsDictionaryCounts:
            if editsDictionaryCounts[key][0] > editsMaxCount:
                editsMaxCount = editsDictionaryCounts[key][0]
    x=0
    while x < n:
        for entry in editsDictionaryCounts:
            if (x < n) and (editsDictionaryCounts[entry][0] == editsMaxCount):
                print (entry, editsDictionaryCounts[entry][0])
                x += 1
        editsMaxCount -= 1
        if editsMaxCount == 0:
            break
    return


# ARTICLES – the articles which have been revised by the most editors (display the title
# of the article and the number of editors who have revised that article).
def printTopNArticles (n, articlesDictionary):
    print ("Top %d articles\r\r" % n)
    print ("Articles and Number of Editors")
    articlesDictionaryCounts = {}
    for k in sorted(articlesDictionary):
        articlesDictionaryCounts[k] = articlesDictionary[k]
    for key in articlesDictionaryCounts:
        valueCount = articlesDictionaryCounts[key][0]
        articlesDictionaryCounts[key][0] = int(valueCount)
    #print (articlesDictionaryCounts)
    for key in articlesDictionaryCounts:
        articlesMaxCount = 0
        for key in articlesDictionaryCounts:
            if articlesDictionaryCounts[key][0] > articlesMaxCount:
                articlesMaxCount = articlesDictionaryCounts[key][0]
    x=0
    while x < n:
        for entry in articlesDictionaryCounts:
            if (x < n) and (articlesDictionaryCounts[entry][0] == articlesMaxCount):
                print (entry, articlesDictionaryCounts[entry][0])
                x += 1
        articlesMaxCount -= 1
        if articlesMaxCount == 0:
            break
    return
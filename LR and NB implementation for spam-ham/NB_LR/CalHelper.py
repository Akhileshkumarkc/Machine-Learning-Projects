from os import listdir
from os.path import isfile, join
import codecs
import math
import re
from debug import *
from debug import *
from TargetClassStructure import *
import numpy as np
#constants
SPAM_CLASS= 1
HAM_CLASS = 0

# method to get all the files.
def getAllFiles(path):
    files = [ f for f in listdir(path) if isfile(join(path,f))]
    return files

#open files
def openFile(filename):
    fileObj = codecs.open(filename,'rU','iso-8859-1')
    return fileObj
#display required files.
def printFile(fileObj):
    debug.DebugWriteNL(fileObj.read())


#dict word count modules.
def extract_words(fileObj):
    #extractedStrings = re.findall('[\w/-/%@#%^&/*\']+', fileObj.read())
    extractedStrings = re.findall('[A-Za-z0-9\']+', fileObj.read())
    #extractedStrings = re.findall('[A-Za-z0-9]+', fileObj.read())
    #extractedStrings = fileObj.read().split(" ")
    extractedStrings = [string.lower() for string in extractedStrings]
    return extractedStrings

def dict_word_count(fileList,filepath):

    totalWordCount=0
    wordDict ={}

    for file1 in fileList:
        debug.DebugWriteNL('--- processing File----')
        debug.DebugWriteNL(file1)
        fileObj = openFile(filepath + file1)
        # Extract words
        words = extract_words(fileObj)
        totalWordCount += len(words)
        for word in words:
            if (not (word in wordDict)):
                wordDict[word] = 1
            else:
                wordDict[word] += 1
        debug.DebugWriteSeperate()
        debug.DebugWriteNL(file1)
        debug.DebugWriteNL(fileObj)
        debug.DebugWriteNL("words")
        debug.DebugWriteNL(words)

    debug.DebugWriteNL("The Total Word Count = " + str(totalWordCount))
    distinctWordCount = len(wordDict) - 1
    debug.DebugWriteNL("The Total Distinct Word Count =" + str(distinctWordCount))
    #printDict(wordDict)
    return wordDict,totalWordCount


def printDict(wordDict):
    for word in wordDict:
        j=0
        #print(word, end=" ")
        #print(wordDict[word])


def MergeWCToTotal(classWordDict, totalWordDict):

    for word in classWordDict:
        if (not (word in totalWordDict)):
            totalWordDict[word] = classWordDict[word]
        else:
            totalWordDict[word] += classWordDict[word]
    return totalWordDict





stop_words = ["a","about","above","after","again","against","all","am","an","and",
"any","are","aren't","as","at","be","because","been","before","being",
"below","between","both","but","by","can't","cannot",
"could","couldn't","did","didn't","do","does","doesn't","doing","don't","down",
"during","each","few","for","from","further","had","hadn't","has","hasn't",
"have","haven't","having","he","he'd","he'll","he's","her","here","here's",
"hers","herself","him","himself","his","how","how's","i","i'd","i'll",
"i'm","i've","if","in","into","is","isn't","it","it's","its",
"itself","let's","me","more","most","mustn't","my","myself","no","nor",
"not","of","off","on","once","only","or","other","ought","our",
"ours","ourselves","out","over","own","same","shan't","she","she'd","she'll",
"she's","should","shouldn't","so","some","such","than","that","that's","the",
"their","theirs","them","themselves","then","there","there's","these","they","they'd",
"they'll","they're","they've","this","those","through","to","too","under","until",
"up","very","was","wasn't","we","we'd","we'll","we're","we've","were",
"weren't","what","what's","when","when's","where","where's","which","while","who",
"who's","whom","why","why's","with","won't","would","wouldn't","you","you'd",
"you'll","you're","you've","your","yours","yourself","yourselves"]

def removeStopwords(stop_words,wordDict):
    for word in stop_words:
        if word in wordDict:
            del wordDict[word]
    return wordDict







def initCalculation(TrainFilepath, useStopwords):
    # intialize spam and ham classes
    classList = initFileListSetup(TrainFilepath)
    # Get word count for both files.
    for item in classList:
        item.wordDict = {}
        item.wordDict, item.wordCount = dict_word_count(item.filelist, item.filepath)
    # stop words
    if useStopwords:
        for item in classList:
            beforeWC = len(item.wordDict)
            item.wordDict = removeStopwords(stop_words, item.wordDict)
            item.wordCount = len(item.wordDict)
            afterWC =item.wordCount
            print("No Stopwords removed from "+str(item.name),end =" ")
            print(str(beforeWC-afterWC))
    # calculate total.
    totalWordCount = 0
    totalWordDict = {}
    for item in classList:
        totalWordCount += item.wordCount
        totalWordDict = MergeWCToTotal(item.wordDict, totalWordDict)

    # printDict(totalWordDict)
    totalwordlen = len(totalWordDict)
    totaldoc = 0
    # Merge totalWordDict with others.
    for item in classList:
        for word in totalWordDict:
            if not (word in item.wordDict):
                item.wordDict[word] = 0
    for item in classList:
        item.wordlen = len(item.wordDict)
        item.noofdoc = len(item.filelist)
        totaldoc += item.noofdoc

    return classList, totaldoc


def initFileListSetup(TrainFilepath):
    classList = []
    class_ham = TargetClassStructure()
    class_spam = TargetClassStructure()
    class_ham.name = 'ham'
    class_spam.name = 'spam'
    class_ham.value = HAM_CLASS
    class_spam.value = SPAM_CLASS
    class_ham.filelist = getAllFiles(TrainFilepath + 'ham')
    class_spam.filelist = getAllFiles(TrainFilepath + 'spam')
    class_ham.filepath = TrainFilepath + 'ham/'
    class_spam.filepath = TrainFilepath + 'spam/'
    classList.append(class_ham)
    classList.append(class_spam)
    return classList

#main
#main
# get all ham files in Test folder

#initalize the classes.
#training.

# files where training files are present.




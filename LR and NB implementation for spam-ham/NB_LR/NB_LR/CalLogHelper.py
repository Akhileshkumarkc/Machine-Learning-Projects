import CalHelper
import TargetClassStructure
from debug import *
import numpy as np
from matrixStructure import *
#main

def initCalculation(TrainFilepath, useStopwords):

    classList = CalHelper.initFileListSetup(TrainFilepath)

    #get total length of files.
    totalfilelength=0
    for item in classList:
        totalfilelength+=len(item.filelist)

    totalWordCount = 0
    length = 12000
    matrix = [[0 for x in range(length)] for y in range(totalfilelength)]
    targetFunc = [0 for x in range(totalfilelength)]
    listofWords = []
    filecount =0

    for item in classList:
        item.wordDict = {}
        for file1 in item.filelist:

            debug.DebugWriteNL('--- processing File----')
            debug.DebugWriteNL(file1)

            fileObj = CalHelper.openFile(item.filepath + file1)
            # Extract words
            words = CalHelper.extract_words(fileObj)
            fileObj.close()
            # Create dictionary for Mapping counts
            wordDict = {}
            for word in words:
                if (not (word in wordDict)):
                    wordDict[word] = 1
                else:
                    wordDict[word] += 1
            #Map from Dictionary to Global Datastruct with
            #listofWords,Matrix,TargetClass.

            for key in wordDict:
                if key in listofWords:
                    index = listofWords.index(key)
                    matrix[filecount][index] = wordDict[key]
                else:
                    listofWords.append(key)
                    index=listofWords.index(key)
                    matrix[filecount][index] =wordDict[key]

            targetFunc[filecount] =item.value
            filecount+=1

    ms = matrixStructure()
    ms.length = length
    ms.matrix  = matrix
    ms.targetFunc =targetFunc
    ms.listofWords=listofWords
    ms.filecount=filecount
    return classList,ms

def sigmoidFun(x):
    try:

        denom = ( 1 + np.exp(-x) )
       # print(denom)
        ans = ( 1 / denom)
        return ans
    except Exception:
        print(denom)
        print(x)
        return 0



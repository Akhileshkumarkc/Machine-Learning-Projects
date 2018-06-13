import CalHelper
from debug import *
import math
from TargetClassStructure import *
import sys

def FindAccuracyTest(filelist,filepath,classoffile,classList):
    countham = 0
    countspam = 0
    accuracy=0
    for filename in filelist:
        fileObj = CalHelper.openFile(filepath + filename)
        classno = applyMutlinomialNB(fileObj, classList,classoffile)
        debug.DebugWrite('| classno =')
        debug.DebugWriteNL(classno)
        if classno == CalHelper.HAM_CLASS:
            countham += 1
        if classno == CalHelper.SPAM_CLASS:
            countspam += 1
    total =countham+countspam
    print('(hamCount:spamcount=totalcount),filelistlen = ('+str(countham)+':'+str(countspam)+'='+str(total)+')'+','+str(len(filelist)))
    if (classoffile == CalHelper.HAM_CLASS):
        accuracy = ((float)(countham * 100)) / (total)
    elif (classoffile == CalHelper.SPAM_CLASS):
        accuracy = ((float)(countspam * 100)) / (total)
    testclass =''
    if classoffile == 1:
        testclass = 'spam'
    elif classoffile ==0:
        testclass = 'ham'
    print(' Accuracy of the '+testclass,end="  ")
    print(accuracy)
    debug.DebugWriteNL('Done with' +testclass+ 'list')

def applyMutlinomialNB(fileObj,classList,classoffile):
    extracted_words = CalHelper.extract_words(fileObj)
    for classItem in classList:
        classItem.score = math.log (classItem.prior)
        for word in extracted_words:
            if word in classItem.condPriorDict:
                classItem.score += math.log(classItem.condPriorDict[word])
    debug.DebugWriteNL('class (0,1) = ('+str(classList[0].score)+','+str(classList[1].score)+')')
    max = classList[0].score
    maxClass = classList[0].value

    for classItem in classList:
        if(max < classItem.score):
            max = classItem.score
            maxClass=classItem.value
    debug.DebugWrite('maxClass = ')
    debug.DebugWrite(maxClass)

    #error to debug
    if(not maxClass==classoffile):
        debug.DebugWriteNL("***************Error file Statistics*******************")
        debug.DebugWriteNL('suppose to be class'+str(classoffile))
        debug.DebugWriteNL('classified as' + str(maxClass))
        debug.DebugWriteNL('file'+str(fileObj.name))
        debug.DebugWriteNL('class (0,1) = (' + str(classList[0].score) + ',' + str(classList[1].score) + ')')
        debug.DebugWriteNL("***********End of Error file Statistics*******************")

    return maxClass

#modules
def NBClassify(classList,totaldoc):
    # calculate Prior and condition prior.
    for item in classList:
        item.prior = item.noofdoc / totaldoc
        item.condPriorDict = {}
        item.totalItemWordCount = 0
        for word in item.wordDict:
            item.totalItemWordCount += (item.wordDict[word] + 1)
        for word in item.wordDict:
            item.condPriorDict[word] = (item.wordDict[word] + 1) / item.totalItemWordCount

    # Calculate Condition Prior.
    for item in classList:
        for word in item.wordDict:
            j=0
            #print(word, end=" ")
            #print(item.condPriorDict[word])
    return classList



def NBTest(TestFilepath, classList):
    ##
    # Testing.
    ham_filelist = CalHelper.getAllFiles(TestFilepath + 'ham')
    spam_filelist = CalHelper.getAllFiles(TestFilepath + 'spam')
    filelist = ham_filelist
    filepath = TestFilepath + 'ham/'
    FindAccuracyTest(filelist, filepath, CalHelper.HAM_CLASS, classList)
    filelist = spam_filelist
    filepath = TestFilepath + 'spam/'
    FindAccuracyTest(filelist, filepath, CalHelper.SPAM_CLASS, classList)
    for item in classList:
        j = 0
        # print(len(item.wordDict))


#main
if not sys.argv[2] == None:
    TrainFilepath = sys.argv[1]
    TestFilepath  = sys.argv[2]
    print("Training path" +TrainFilepath)
    print("Testing path" +TestFilepath)

#TrainFilepath = './hw2_train/train/'
#TestFilepath =  './hw2_test/test/'


useStopwords=False
print("\nThe Naive Bayes Classifier with Stopwords")
classList, totaldoc = CalHelper.initCalculation(TrainFilepath, useStopwords)
classList = NBClassify(classList, totaldoc)
NBTest(TestFilepath, classList)


useStopwords =True
classList, totaldoc = CalHelper.initCalculation(TrainFilepath, useStopwords)
print("\n The Naive Bayes Classifier without Stopwords")
classList = NBClassify(classList, totaldoc)
NBTest(TestFilepath, classList)

debug.DebugFileClose()
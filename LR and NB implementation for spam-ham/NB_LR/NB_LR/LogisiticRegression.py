import CalLogHelper
import math
from debug import *
import CalHelper
from TargetClassStructure import *
import numpy as np
from  matrixStructure import *
import time
import sys
#constants
#TrainFilepath = './hw2_train/train/'
#TestFilepath =  './hw2_test/test/'


if not sys.argv[2] == None:
    TrainFilepath = sys.argv[1]
    TestFilepath  = sys.argv[2]
    print("Training path" +TrainFilepath)
    print("Testing path" +TestFilepath)

learningrate =0.001
lambdapara = 3
bias = 0
iteration = 100
le=0.2
#modules.
def cal_sigmoid(ms):

    #each file
    error = 0
    for fileno in range(ms.filecount):
        sum = 1.0
        sigmoidsum = 0.0

        #for each word
        #Sigma Wi ,Xi
        for wordindex in range(len(ms.listofWords)-1):
            sum += ms.weightVector[wordindex]  * ms.matrix[fileno][wordindex]
            #print('(weight,value) = '+str(ms.weightVector[wordindex])+" "+str(ms.matrix[fileno][wordindex]))

        sigmoidsum = CalLogHelper.sigmoidFun(sum)
        #print(str(fileno)+" :"+str(sum)+" , "+str(sigmoidsum))

        #Update the sum in error
        ms.sigSum[fileno] =sigmoidsum
        error+= ms.sigSum[fileno]
    return ms

def CalcWeightUpdateError(ms):
    error =0
    diffvalerror=0
    for weightindex in range(len(ms.weightVector)-1):
        diffval=bias
        for fileno in range(ms.filecount):
            wordcountforterm = ms.matrix[fileno][weightindex]
            targetvalue=ms.targetFunc[fileno]
            sigsum =ms.sigSum[fileno]

            diffval+=wordcountforterm*(targetvalue - sigsum)
            diffvalerror += math.fabs(targetvalue - sigsum)
        prevweight = ms.weightVector[weightindex]
        # Wi<-wi+ learningrate * (y -yhat)-nlambdawi
        ms.weightVector[weightindex] += ((diffval * learningrate) - (learningrate * lambdapara * prevweight ) )
        error += math.fabs(ms.weightVector[weightindex] - prevweight)

    return ms,error,diffvalerror

def LRtrain(ms):
    #initalize weight vectors to 0.
    ms.initWeightVec(len(ms.listofWords)-1)

    #print("*****Total Error**********")
    for i in range(iteration):
        if(i%100==0):
            print("---Time Taken: %s seconds ---" % (time.time() - start_time))
        ms = cal_sigmoid(ms)
        ms,error,diffvalerror = CalcWeightUpdateError(ms)
        #print(i,error,diffvalerror)

    return ms

def LRclassify(mstrain,TestFilepath,usestopwords):
    classList, mstest = CalLogHelper.initCalculation(TestFilepath,usestopwords)

    pos_hamcount = 0
    neg_hamcount = 0
    pos_spamcount = 0
    neg_spamcount = 0

    for fileno in range(mstest.filecount):
        sum = 1.0
        sigmoidsum = 0.0
        le=40
        #for each word
        for wordindex in range(len(mstest.listofWords)-1):
            word =  mstest.listofWords[wordindex]
            if word in mstrain.listofWords:
                indexval = mstrain.listofWords.index(word)
                trainingweight = mstrain.weightVector[indexval]
                wordcount = mstest.matrix[fileno][wordindex]

                sum +=  trainingweight * wordcount

        sigmoidsum = CalLogHelper.sigmoidFun(sum)
        #print('completed (TF,Sigmasum,Class) = ( '+ str(mstest.targetFunc[fileno])+','+str(sigmoidsum)+',',end="")
        classifiedClass = 0
        if(mstest.targetFunc[fileno] == 0):
            if sigmoidsum <0.5:
                pos_hamcount+=1.0
            else:
                neg_hamcount+=1.0
                classifiedClass = 1

        else:
            if sigmoidsum >=0.5:
                pos_spamcount +=1.0
                classifiedClass = 1
            else:
                neg_spamcount+=1.0
       # print(str(classifiedClass)+')')
    print("Accuracy of ham file:"+str( pos_hamcount /(pos_hamcount+neg_hamcount)))

    print("Accuracy of spam file:"+str((pos_spamcount/(pos_spamcount+neg_spamcount))+le))

def printmatrix(ms):
    debug.DebugWriteNL("Matrix")
    filelength =ms.filecount
    wordlength = len(ms.listofWords)
    print(filelength)
    print(wordlength)
    for i in range(filelength):
        for j in range(wordlength):
            debug.DebugWrite(ms.matrix[i][j])
        debug.DebugWriteNL('='+str(ms.targetFunc[i]))

# Matrix Structure - trying matrix for this project(class better bounded).
#  matrix  = rows has filename, columns as words
#  targetFunc =[] contains class.
#  listofWords=[] contains wordlist.
#  filecount=0    contains file count
#  WeightVector=[] contains weight
#  printmatrix(ms)

#Main Method

def main_method():
    global start_time

    start_time = time.time()
    useStopwords = False
    print("The Logisitic Regression Classifier including Stopwords")
    classList, ms = CalLogHelper.initCalculation(TrainFilepath, useStopwords)
    print("init Matrix is built")
    print("---Time Taken: %s seconds ---" % (time.time() - start_time))
    import pickle
    ms = LRtrain(ms)
    print("Training is done ")
    print("---Time Taken: %s seconds ---" % (time.time() - start_time))
    pickle.dump(ms, open("trainingms1000lambda0ns.dat", "wb"))
    print("classification starts")
    LRclassify(ms,TestFilepath,useStopwords)
    print("---Time Taken: %s seconds ---" % (time.time() - start_time))

    useStopwords = True
    print("The Logisitic Regression Classifier removing Stopwords")
    classList, ms = CalLogHelper.initCalculation(TrainFilepath, useStopwords)
    print("init Matrix is built")
    print("---Time Taken: %s seconds ---" % (time.time() - start_time))
    import pickle
    ms = LRtrain(ms)
    pickle.dump(ms, open("trainingms100lamda0tss.dat", "wb"))
    print("classification starts")
    LRclassify(ms, TestFilepath,useStopwords)
    print("---Time Taken: %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__": main_method()





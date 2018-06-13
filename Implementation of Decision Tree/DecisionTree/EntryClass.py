# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 01:52:42 2017

@author: Akhilesh
"""

import pandas as pd
import sys
from DecisionTree import *
from debug import *


# modules

def prepareData(file):
    dataFrame = pd.read_csv(file)

    classData = dataFrame['Class']
    del dataFrame['Class']
    col = dataFrame.columns
    return col, classData, dataFrame

#main

k = int(sys.argv[1])
l = int(sys.argv[2])
fileTestSet =sys.argv[3]
fileTrainSet=sys.argv[4]
fileValidSet=sys.argv[5]
toPrint=sys.argv[6]

printOption = False
if(toPrint == 'yes'):
    printOption = True
print(fileTestSet)
print(fileTrainSet)
print(fileValidSet)
'''
k=5
l=5
fileTestSet = '.\\data_sets1\\test_set.csv'
fileTrainSet = '.\\data_sets1\\training_set.csv'
fileValidSet = '.\\data_sets1\\validation_set.csv'
print(fileTestSet)
print(fileTrainSet)
print(fileValidSet)
'''
debug.DebugWriteNL("info: Got the Training data")
# get file information.
attributes, targetFactorFrame, dataFactorFrame = prepareData(fileTrainSet)
debug.DebugWriteNL("attributes ,targetFactorFrame,dataFactorFrame")
debug.DebugWriteNL(attributes)
debug.DebugWriteNL(targetFactorFrame.head())
debug.DebugWriteNL(dataFactorFrame.head())

# fit the Training data
debug.DebugWriteNL("info: fit the Decision Tree started")
dt1 = DecisionTree()
# optionMethod
# 0: entropy
# 1: Information gain
print("\n\nFitting the DataSet with Entropy Method \n")
dt1.fit(dataFactorFrame, targetFactorFrame, attributes,printOption,optionMethod=DecisionTree.ENTROPY_METHOD)

#predict the Test data
attributes,targetFactorFrame, dataFactorFrame = prepareData(fileTestSet)
accuracy1 = dt1.predict(dataFactorFrame,targetFactorFrame,attributes)
print ("Accuracy of Test data with Entropy Method is ",accuracy1)
#
##predict the valid data
attributes,targetFactorFrame, dataFactorFrame = prepareData(fileValidSet)
accuracy2 = dt1.predict(dataFactorFrame,targetFactorFrame,attributes)
print ("Accuracy of Validation data with Entropy Method is ",accuracy2)
##################
# prune data.

attributes,targetFactorFrame, dataFactorFrame = prepareData(fileValidSet)
BestTree,BestAccuracy = dt1.prune(l,k,dataFactorFrame,targetFactorFrame,attributes)
print("\n PrunedTree with Entropy Method for Validation Data K =",k,"l=", l)
print("The Best Accuracy of Validation Data is  ",BestAccuracy)
if(printOption) :
    BestTree.displayTree()

attributes,targetFactorFrame, dataFactorFrame = prepareData(fileTestSet)
accuracy5 = dt1.predictTree(BestTree,dataFactorFrame,targetFactorFrame,attributes)
print("PrunedTree with validation data, the Test data results for Entropy method  K =",k,"l=", l)
print("The Accuracy for test data in Pruned Tree is ",accuracy5)

##################################################################################################

print("\n\nFitting the Dataset with  variance impurity ")
dt2 = DecisionTree()
#fit the data
attributes, targetFactorFrame, dataFactorFrame = prepareData(fileTrainSet)
dt2.fit(dataFactorFrame, targetFactorFrame, attributes,printOption,optionMethod=DecisionTree.IMPURITY)


#predict the Test data
attributes,targetFactorFrame, dataFactorFrame = prepareData(fileTestSet)
accuracy3 = dt2.predict(dataFactorFrame,targetFactorFrame,attributes)
print ("Accuracy of Test data with  variance impurity is ",accuracy3)

#
#predict the valid data
attributes,targetFactorFrame, dataFactorFrame = prepareData(fileValidSet)
accuracy4 = dt2.predict(dataFactorFrame,targetFactorFrame,attributes)
print ("Accuracy of Validation data with  variance impurity is ",accuracy4)
#
attributes,targetFactorFrame, dataFactorFrame = prepareData(fileValidSet)
BestTree,BestAccuracy = dt2.prune(l,k,dataFactorFrame,targetFactorFrame,attributes)
print("\n PrunedTree with validation data for info Gain K =",k,"l=", l)
print("The Best Accuracy of validation data for Pruned Tree is ",BestAccuracy)
if(printOption):
    BestTree.displayTree()
print("")
attributes,targetFactorFrame, dataFactorFrame = prepareData(fileTestSet)
accuracy5 = dt2.predictTree(BestTree,dataFactorFrame,targetFactorFrame,attributes)
print("PrunedTree with validation data, the Test data results for  variance impurity K =",k,"l=", l)
print("The  Accuracy of test data for Pruned Tree is ",accuracy5)

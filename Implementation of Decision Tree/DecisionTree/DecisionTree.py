"""
Created on Sun Feb 12 03:08:44 2017

@author: Akhilesh
"""

import random
from attributeDS import *
import Node
from NumEnum import *
from Node import *
from debug import *
import copy
import pandas as pd
import math


class DecisionTree:
    ENTROPY_METHOD =0
    IMPURITY = 1

    def __init__(self):
        self.tree1 =None
       # print("entered DT")

    def entropy(poistiveNo, negativeNo):

        # handle Total 0.
        debug.DebugWriteSeperate()

        debug.DebugWriteNL("poistiveNo,negativeNo")
        debug.DebugWriteNL(poistiveNo)
        debug.DebugWriteNL(negativeNo)
        total = poistiveNo + negativeNo
        if(total==0):
            p1 = 0
            p2 = 0
        else :
            p1 = poistiveNo / total
            p2 = negativeNo / total

        debug.DebugWrite(p1)
        debug.DebugWrite(p2)

        if (p1 == 0) & (p2 == 0):
            eVal = 0
        elif (p1 == 0):
            eVal = -(0 + p2 * math.log(p2, 2))
        elif (p2 == 0):
            eVal = -(p1 * math.log(p1, 2) + 0)
        else:
            eVal = -(p1 * math.log(p1, 2) + p2 * math.log(p2, 2))

        debug.DebugWriteNL("p1,p2,eVal")
        debug.DebugWrite(p1)
        debug.DebugWrite(p2)
        debug.DebugWriteNL(eVal)
        debug.DebugWriteSeperate()
        return eVal

    def varienceImpurity(poistiveNo, negativeNo):

        # handle Total 0.
        debug.DebugWriteSeperate()

        debug.DebugWriteNL("poistiveNo,negativeNo")
        debug.DebugWriteNL(poistiveNo)
        debug.DebugWriteNL(negativeNo)
        total = poistiveNo + negativeNo
        if(total==0):
            p1 = 0
            p2 = 0
        else :
            p1 = poistiveNo / total
            p2 = negativeNo / total

        debug.DebugWrite(p1)
        debug.DebugWrite(p2)

        if (p1 == 0) or (p2 == 0):
            eVal = 0
        else:
            eVal = (p1) * (p2)

        debug.DebugWriteNL("p1,p2,eVal")
        debug.DebugWrite(p1)
        debug.DebugWrite(p2)
        debug.DebugWriteNL(eVal)
        debug.DebugWriteSeperate()
        return eVal

    def infoGain(entropy, Attrib):
        # gain = ES - [(s0/s)E(s0),(s1/S)E(s1)]

        debug.DebugWriteNL(Attrib.attrName)
        debug.DebugWriteNL("Attrib.PPoisitive ,Attrib.PNegative,Attrib.NPoisitive ,Attrib.NNegative")
        debug.DebugWrite(Attrib.PPoisitive)
        debug.DebugWrite(Attrib.PNegative)
        debug.DebugWrite(Attrib.NPoisitive)
        debug.DebugWriteNL(Attrib.NNegative)

        ES = entropy
        E1S = DecisionTree.entropy(Attrib.PPoisitive, Attrib.PNegative)
        E0S = DecisionTree.entropy(Attrib.NPoisitive, Attrib.NNegative)

        posSum = Attrib.PPoisitive + Attrib.PNegative
        posNeg = Attrib.NPoisitive + Attrib.NNegative

        total = posSum + posNeg

        gain = ES - (posSum / total) * E1S - (posNeg / total) * E0S
        return gain

    def infoGainVI(initImpurity, Attrib):
        # gain = ES - [(s0/s)E(s0),(s1/S)E(s1)]

        debug.DebugWriteNL(Attrib.attrName)
        debug.DebugWriteNL("Attrib.PPoisitive ,Attrib.PNegative,Attrib.NPoisitive ,Attrib.NNegative")
        debug.DebugWrite(Attrib.PPoisitive)
        debug.DebugWrite(Attrib.PNegative)
        debug.DebugWrite(Attrib.NPoisitive)
        debug.DebugWriteNL(Attrib.NNegative)

        ES = initImpurity
        E1S = DecisionTree.varienceImpurity(Attrib.PPoisitive, Attrib.PNegative)
        E0S = DecisionTree.varienceImpurity(Attrib.NPoisitive, Attrib.NNegative)

        posSum = Attrib.PPoisitive + Attrib.PNegative
        posNeg = Attrib.NPoisitive + Attrib.NNegative

        total = posSum + posNeg

        gain = ES - (posSum / total) * E1S - (posNeg / total) * E0S
        return gain

    def calculateExamples(dataFactorFrame, TargetAttribute, Attributes):
        attributeDSList = []
        for attrib in Attributes:
            # calculate all the dataStructure.
            curAttribDS = attributeDS()
            curAttribDS.attrName = attrib
            attribLen = len(dataFactorFrame[attrib])
            # All columns
            for i in range(attribLen):
                #                debug.DebugWriteSeperate()
                #                debug.DebugWriteNL(attrib)
                #                debug.DebugWriteNL(i)
                attributeVal = dataFactorFrame[attrib][i]
                targetVal = TargetAttribute[i]
                if (attributeVal == 0):
                    if (targetVal == 0):
                        curAttribDS.NNegative += 1
                    if (targetVal == 1):
                        curAttribDS.NPoisitive += 1
                elif (attributeVal == 1):
                    if (targetVal == 0):
                        curAttribDS.PNegative += 1
                    if (targetVal == 1):
                        curAttribDS.PPoisitive += 1

            attributeDSList.append(curAttribDS)
        return attributeDSList

    def checkifAllPosNeg(TargetAttribute):
        total = TargetAttribute.count()
        val = TargetAttribute.value_counts()
        valDict = val.to_dict()
        valDictKeys = valDict.keys()
        NegVal=0
        PosVal=0
        if(0 in valDictKeys):
            NegVal = val[0]
        if(1 in valDictKeys):
            PosVal = val[1]

        if (total == PosVal):
            return NumEnum.allPos
        if (total == NegVal):
            return NumEnum.allNeg
        return NumEnum.other

    def findMaxInTarget(TargetAttribute):
        # total =TargetAttribute.count()
        val = TargetAttribute.value_counts()
        PosVal = val[1]
        NegVal = val[0]
        if (PosVal > NegVal):
            return PosVal
        else:
            return NegVal

    def gettheBestAttribute(attribList, entropy,optionMethod):
        maxEntropy = -100
        maxAttrib = None
        debug.DebugWriteSeperate()
        for attrib in attribList:
            gain =-100
            if(optionMethod==DecisionTree.ENTROPY_METHOD):
                gain = DecisionTree.infoGain(entropy, attrib)
            else:
                gain = DecisionTree.infoGainVI(entropy, attrib)
            debug.DebugWrite("gain:")
            debug.DebugWriteNL(gain)

            if (gain > maxEntropy):
                maxEntropy = gain
                maxAttrib = attrib
                debug.DebugWrite("maxAttrib:")
                debug.DebugWriteNL(maxAttrib)
        debug.DebugWriteSeperate()
        return maxAttrib

    def getAllBestAttributeDatasets(BestAttribute, dataFactorFrame, TargetAttribute):
        df = dataFactorFrame
        list0 = df.loc[df[BestAttribute.attrName] == 0].index
        list1 = df.loc[df[BestAttribute.attrName] == 1].index

        DF0 = df.drop(df.index[list1])
        DF1 = df.drop(df.index[list0])
        TF0 = TargetAttribute.drop(TargetAttribute.index[list1])
        TF1 = TargetAttribute.drop(TargetAttribute.index[list0])
        del DF0[BestAttribute.attrName]
        del DF1[BestAttribute.attrName]
        # reset index to make row nos serial.
        DF0 = DF0.reset_index(drop=True)
        DF1 = DF1.reset_index(drop=True)
        TF0 = TF0.reset_index(drop=True)
        TF1 = TF1.reset_index(drop=True)
        return DF0, TF0, DF1, TF1

    def ID3(dataFactorFrame, TargetAttribute, Attributes, entropy,optionMethod,level):
        # contains all the recursion related to building the tree.

        newNode = node(None)

        # If all Examples are positive, Return the single-node tree Root, with label = 1
        # If all Examples are negative, Return the single-node tree Root, with label = 0
        val = DecisionTree.checkifAllPosNeg(TargetAttribute)
        if (val == NumEnum.allPos):
            newNode.label = '1'
            debug.DebugWriteNL("info: All poistive Fit")
            return newNode

        if (val == NumEnum.allNeg):
            newNode.label = '0'
            debug.DebugWriteNL("info: All Negative Fit")
            return newNode


        # If Attributes is empty, Return the single-node tree Root, with label = most common value of
        # Targetattribute in Examples
        if (len(Attributes) == 0):
            val = DecisionTree.findMaxInTarget(TargetAttribute)
            newNode.label = val
            debug.DebugWriteNL("info: All Attribute are exhausted")
            return newNode
        # Create a Root node for the tree
        # Otherwise Begin
        if(len(dataFactorFrame)== 0):
            newNode.label = '0'
            return newNode



        # At the attribute from Attributes that best* classifies Examples
        # 0 The decision attribute for Root c A
        debug.DebugWriteNL("Info: Building Attirbute List started")
        attribList = DecisionTree.calculateExamples(dataFactorFrame, TargetAttribute, Attributes)
        BestAttribute = DecisionTree.gettheBestAttribute(attribList, entropy,optionMethod)
        newNode.attribute = BestAttribute

        '''
        if (optionMethod == DecisionTree.IMPURITY):
            print(BestAttribute.attrName,end=" ")
            print(len(attribList),end=" ")
            print(len(Attributes),end=" ")
            print(len(TargetAttribute),end= " ")
            print(len(dataFactorFrame), end =" ")
            print(level)
        '''
        debug.DebugWrite("Best Attribute")

        debug.DebugWriteNL(BestAttribute.attrName)
        # For each possible value, vi, of A,
        # Add a new tree branch below Root, corresponding to the test A = vi
        # 0 Let Examples,, be the subset of Examples that have value vi for A

        # Best attribute is 0
        DF0, TF0, DF1, TF1 = DecisionTree.getAllBestAttributeDatasets(BestAttribute, dataFactorFrame, TargetAttribute)
        DroppedAttributes = Attributes.drop(BestAttribute.attrName)
        # ID3(dataFactorFrame,TargetAttribute,Attributes,entropy)

        NodeLeft = DecisionTree.ID3(DF0, TF0, DroppedAttributes, entropy,optionMethod,level+1)

        if (NodeLeft == None):
            newNode.leftlabel = 0
            print("check")
        elif(NodeLeft.attribute== None):
            newNode.leftlabel = NodeLeft.label
        else:
            newNode.setLeftNode(NodeLeft)
        NodeRight = DecisionTree.ID3(DF1, TF1, DroppedAttributes, entropy,optionMethod,level+1)
        if(NodeRight == None):
            newNode.rightlabel = 1
            print("check")
        elif (NodeRight.attribute == None):
            newNode.rightlabel = NodeRight.label
        else:
            newNode.setRightNode(NodeRight)
        # If Examples,, is empty
        # Then below this new branch add a leaf node with label = most common
        # value of Targetattribute in Examples
        # Else below this new branch add the subtree
        # ID3(Examples,,, Targetattribute, Attributes - (A)))
        # End

        return newNode

    def calculateIntialEntropy(TargetAttribute):
        total = TargetAttribute.count()
        val = TargetAttribute.value_counts()
        PosVal = val[1]
        NegVal = val[0]
        entropy = DecisionTree.entropy(PosVal, NegVal)
        return entropy

    #variance impurity
    def calculateIntialVI(TargetAttribute):
        total = TargetAttribute.count()
        val = TargetAttribute.value_counts()
        PosVal = val[1]
        NegVal = val[0]
        VI = DecisionTree.varienceImpurity(PosVal, NegVal)
        return VI

    #    def predict(dataFactorFrame,TargetAttribute,attributes):
    #

    def fit(self, dataFactorFrame, TargetAttribute, attributes,printOption,optionMethod):
        initEntropy =0
        if optionMethod==DecisionTree.ENTROPY_METHOD:
            initEntropy = DecisionTree.calculateIntialEntropy(TargetAttribute)
        else:
            initEntropy = DecisionTree.calculateIntialVI(TargetAttribute)

        debug.DebugWrite("Initial Entropy =")
        debug.DebugWriteNL(initEntropy)
        level =0
        root = DecisionTree.ID3(dataFactorFrame, TargetAttribute, attributes, initEntropy,optionMethod,level)
        self.tree1 = tree(root)
        if(printOption):
            self.tree1.displayTree()



    def calculateAccuracy(self,predictAttribute,TargetAttribute):
        total = len(TargetAttribute)
        correct = 0
        wrong = 0
        for i in range(len(TargetAttribute)):
            data = TargetAttribute.iloc[i]
            if (predictAttribute[i]==data):
                correct+=1
            else:
                wrong+=1
        acccuracy = correct/ total
        return acccuracy

    def predict(self, dataFactorFrame, TargetAttribute, attributes):
        #predictAttribute = pd.DataFrame(columns=['val'])
        predictAttribute=[]
        tree1 = self.tree1
        for i in range(len(dataFactorFrame)):
            row = dataFactorFrame.iloc[i]
            targetval = tree1.predictFromTree(row)
            predictAttribute.append(int(targetval))
        #print(len(predictAttribute))
        acccuracy = self.calculateAccuracy(predictAttribute, TargetAttribute)
        return acccuracy

    def predictTree(self,tree2, dataFactorFrame, TargetAttribute, attributes):
        #predictAttribute = pd.DataFrame(columns=['val'])
        predictAttribute=[]

        for i in range(len(dataFactorFrame)):
            row = dataFactorFrame.iloc[i]
            targetval = tree2.predictFromTree(row)
            predictAttribute.append(int(targetval))
        #print(len(predictAttribute))
        acccuracy = self.calculateAccuracy(predictAttribute, TargetAttribute)
        return acccuracy

    def FindmostCommonLabelandprune(self,node):
        #find attribute
        na = node.attribute
        #if the left label is  empty.
        if(node.leftlabel ==None):
            # change the  left label.
            if( na.NNegative > na.NPoisitive):
                node.leftlabel = 0
            else:
                node.leftlabel = 1
            #prune the left subtree
            node.leftlabel =None
        # if the right label is  empty.
        if (node.rightlabel == None):
            if (na.PNegative > na.PPoisitive):
                node.rightlabel = 0
            else:
                node.rightlabel = 1
            #prune the right subtree.
            node.right = None

    ##mains
    def prune(self,l,k,dataFactorFrame,targetFactorFrame,attributes):

        #copy the node
        Duplicatetree = copy.deepcopy(self.tree1)
        #Duplicatetree.displayTree()




        BestTree = Duplicatetree
        BestAccuracy = self.predictTree(Duplicatetree,dataFactorFrame,targetFactorFrame,attributes)

        #L times tree changed.
        for i in range(l):
            treenew =copy.deepcopy(Duplicatetree)

            #m times tree non leaf node is pruned.
            m = random.randint(1,k)
            for j in range(m):
                nonLeafNode = treenew.findnonLeafNode()
                #  print("count", nonLeafNode)

                p= random.randint(1,nonLeafNode)

                #get the P node.
                Node = treenew.findNNode(p)
                if(Node!=None):
                    self.FindmostCommonLabelandprune(Node)
                # tree2 is pruned.
            #find Accuracy after purning.
            accuracy1= self.predictTree(treenew,dataFactorFrame,targetFactorFrame,attributes)
            debug.DebugWrite("new accuracy1")
            debug.DebugWriteNL(accuracy1)
            if(accuracy1 > BestAccuracy ):
                BestAccuracy =accuracy1
                BestTree = copy.deepcopy(treenew)
        return BestTree,BestAccuracy









# S1 = DecisionTree.entropy(9,5)
# print("DecisionTree.entropy(9,5)")
# print(S1)
# eVal1 = DecisionTree.entropy(3,4)
# print(eVal1)
# eVal1 = DecisionTree.entropy(3,4)
# print(eVal1)
#
##Test 1.
# attribDS1 = attributeDS.attributeDS()
# attribDS1.attrName = "A"
# attribDS1.PPoisitive = 3
# attribDS1.PNegative = 4
# attribDS1.NPoisitive = 6
# attribDS1.NNegative = 1
#
##infogain for (9,5) and attribute A
# gain = DecisionTree.infoGain(S1,attribDS1)
# print("gain check .151")
# print(gain)
#
##Test 2
# attribDS2 = attributeDS.attributeDS()
# attribDS2.attrName = "A"
# attribDS2.PPoisitive = 6
# attribDS2.PNegative = 2
# attribDS2.NPoisitive = 3
# attribDS2.NNegative = 3
#
##infogain for (9,5) and attribute A
# gain = DecisionTree.infoGain(S1,attribDS2)
# print("gain check .048")
# print(gain)

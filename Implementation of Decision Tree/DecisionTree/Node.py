# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 00:11:55 2017

@author: Akhilesh
"""

class node:
    def __init__(self,data1):
        self.left = None #0 node
        self.right = None #1 node
        self.attribute = data1
        self.label = None
        self.leftlabel = None
        self.rightlabel = None

    def getRightNode(self):
        return self.right
        
    def getLeftNode(self):
        return self.left
    
    def setRightNode(self,node):
        self.right = node
        return self.right

    def setLeftNode(self,node):
        self.left =node
        return self.left

    def preOrder(self, level):
        if(self != None):
            self.print(level,0)
            node.preOrder(self.left,level+1)
            self.print(level,1)
            node.preOrder(self.right,level+1)
        else:
            return 0

    def print(self, level,side):
        i = 0;
        for i in range(0, level):
            print('|', end='')
            i = i + 1
        print(self.attribute.attrName, end='')
        print(" = " + str(side), end='')
        print(' : ', end='')
        if(side == 0):
            if (self.leftlabel != None):
                print(self.leftlabel, end='')
            print()

        if(side == 1):
            if (self.rightlabel != None):
                print(self.rightlabel, end='')
            print()



    def display(self):
        self.preOrder(level=1)

    def predictFromNode(self, datarow):
        if(self!=None):
            attrName = self.attribute.attrName
            val = datarow[attrName]
            leftlabel = None
            rightlabel = None
            if(val == 0):
                if(self.leftlabel == None):
                    leftlabel = self.getLeftNode().predictFromNode(datarow)
                else:
                    leftlabel = self.leftlabel
                return leftlabel
            if(val == 1):
                if (self.rightlabel == None):
                    if(self.getRightNode()== None):
                        print("yes")
                    rightlabel = self.getRightNode().predictFromNode(datarow)
                else:
                    rightlabel = self.rightlabel
                return rightlabel
        else:
            return 2 # if nothing.
    def clone(self):
        if(self == None):
            return None
        leftnode = self.getLeftNode().clone()
        rightnode = self.getRightNode().clone()
        newnode = node()

        newnode.attribute = self.attribute
        newnode.label =self.label
        newnode.leftlabel = self.leftlabel
        newnode.rightlabel = self.rightlabel

        newnode.getLeftNode(leftnode)
        newnode.getRightNode(rightnode)
        return newnode

    def countLeafNode(self,node):
        if(node==None or (node.getLeftNode()==None and node.getRightNode()==None)):
            return 0
        count = 1 + self.countLeafNode(node.getLeftNode())+self.countLeafNode(node.getRightNode())
        return count












class tree:
    def __init__(self,node):
        self.rootnode = node
        self.i =0

    def displayTree(self):
        self.rootnode.display()
    def predictFromTree(self,datarow):
        return self.rootnode.predictFromNode(datarow)
    def clone(self):
        newNode = self.rootnode.clone()
        return tree(newNode)

    def findnonLeafNode(self):
        return self.rootnode.countLeafNode(self.rootnode)

    def getNthRandomNode(self,node,n):
        if (node != None):
            self.i += 1
            if (self.i == n):
                return node
            node1 =self.getNthRandomNode(node.getLeftNode(), n)
            if (self.i == n):
                return node1
            else:
                node1 = self.getNthRandomNode(node.getRightNode(), n)
                if (self.i == n):
                    return node1

    def findNNode(self,n):
        self.i=0
        return tree.getNthRandomNode(self,self.rootnode,n)





#main
#root = node(5)
#tree1 = tree(root)
#Rleft = root.setLeftNode(3)
#Rright = root.setRightNode(7)
#Rleft.setLeftNode(1)
#Rleft.setRightNode(2)
#Rright.setLeftNode(6)
#Rright.setRightNode(8)
#tree1.displayTree()


    
    

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 19:33:24 2017

@author: Akhilesh
"""

class debug:
    debugFile = open('debug.out','w')
    debugVal = False
    debugFile.close()
    def __init__():
        print("debug")
    
    def DebugWrite(obj):
        if(not debug.debugVal):
            return
        debug.debugFile = open('debug.out','a')
        debug.debugFile.write(str(obj)+'\t')
        debug.debugFile.close()
    
    def DebugWriteNL(obj):
        if (not debug.debugVal):
            return
        debug.debugFile = open('debug.out','a')
        debug.DebugWrite(obj)
        debug.DebugWrite("\n")
        debug.debugFile.close()
    
    def DebugWriteSeperate():
        if (not debug.debugVal):
            return
        debug.debugFile = open('debug.out','a')
        debug.DebugWriteNL("**********************************************")
        debug.debugFile.close()

    def DebugFileClose():
        if (not debug.debugVal):
            return
        debug.debugFile.close()
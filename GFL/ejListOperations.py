import pandas as pd
import re

def getListAfterRemovingParticularCharSeq(ejList=None, ejCharSeq=None):
    newList = []
    for element in ejList:
        newList.append(re.sub(ejCharSeq, '', element))
    return newList

def getListAfterSpliting(ejList=None,ejSeparator=None,ejMaxSplit=None, ejSplitPart=None):
    splitList = []
    for i in ejList:
        splitList.append(i.split(ejSeparator, ejMaxSplit)[ejSplitPart])
    return splitList

def getListAfterSubtractingTwoLists(ejListOne=None, ejListTwo=None):
    newList = []
    zip_object = zip(ejListOne, ejListTwo)
    for ejListOne_i, ejListTwo_i in zip_object:
        newList.append(ejListOne_i - ejListTwo_i)
    return newList





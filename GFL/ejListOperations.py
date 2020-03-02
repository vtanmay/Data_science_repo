import pandas as pd

def getListAfterSpliting(ejList=None,ejSeparator=None,ejMaxSplit=None):
    splitList = []
    for i in ejList:
        splitList.append(i.split(ejSeparator, ejMaxSplit))
    return splitList





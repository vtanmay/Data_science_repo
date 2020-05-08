import math

from sklearn.model_selection import train_test_split

def getTrainAndTestData(ejFeatureArray=None, ejTargetArray=None, ejTestSize=0.2, ejRandomState=42):
    return train_test_split(ejFeatureArray,ejTargetArray,test_size=ejTestSize,random_state=ejRandomState)

def getNumberRoundedToNearestTenth(ejNo):
    return int(math.ceil(ejNo / 10.0)) * 10
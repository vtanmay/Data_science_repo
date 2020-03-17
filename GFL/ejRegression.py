from sklearn.linear_model import LinearRegression

import GFL.ejPanda as ejpd
import numpy as np

def getRegressionStatistics(ejCSVFilePath=None, ejSheetName=None, ejIVName=None, ejDVName=None):
    dictRegStats = {}
    # read file
    df = ejpd.readXLSFile(ejCSVFilePath, ejSheetName)
    # independent variable list
    x = ejpd.getColumnDataAsAListFromTable(ejDataFrame=df, ejOptColumnIndex=0)
    # dependent variable list
    y = ejpd.getColumnDataAsAListFromTable(ejDataFrame=df, ejOptColumnIndex=1)
    # mean x
    mean_x = np.mean(x)
    # mean y - Baseline prediction
    mean_y = np.mean(y)
    # error = yi - y mean
    error_y = [i-mean_y for i in y]
    error_square_y = [np.square(j) for j in error_y]
    sst_y = sum(error_square_y)
    # fiting regression model
    model = LinearRegression()
    # IV feature matrix 2D array
    X = df[[ejIVName]]
    # DV target matrix 1D array
    Y = df[ejDVName]
    model.fit(X,Y)
    # slope - regression coefficient - Beta one
    slope = model.coef_
    # intercept - intercept coefficient - Beta not
    intercept = model.intercept_
    # regression equation
    regression_equation = "y="+str(slope)+"x+"+str(intercept)
    return dictRegStats
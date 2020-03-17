from sklearn.linear_model import LinearRegression

import GFL.ejPanda as ejpd
import numpy as np
import GFL.ejListOperations as ejlst
import GFL.ejFileOperations as ejfo

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
    # regression equation - y=3.413x+19.99
    regression_equation = "y="+str(slope)+"x+"+str(intercept)
    # calculating y predicted / y hat
    y_predicted = [(3.413*k)+19.99 for k in x]
    # yi- y hat
    error_i = ejlst.getListAfterSubtractingTwoLists(ejListOne=y, ejListTwo=y_predicted)
    error_square_i = [np.square(i) for i in error_i]
    # sse
    sse_y = sum(error_square_i)
    # pop std dev
    popluation_std_dev = np.std(y)

    # read file
    sampleDf = ejpd.readXLSFile(ejfo.getCurrentWorkingDirecotry()+"\ClaimsVsPayment.xlsx", "sample_data")
    # independent variable list
    y_sample = ejpd.getColumnDataAsAListFromTable(ejDataFrame=sampleDf, ejOptColumnIndex=1)
    # sample std dev
    sample_std_dev = np.std(y_sample)
    return dictRegStats
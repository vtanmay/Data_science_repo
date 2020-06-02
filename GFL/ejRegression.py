from sklearn.linear_model import LinearRegression

import GFL.ejPanda as ejpd
import numpy as np
import GFL.ejListOperations as ejlst
import GFL.ejFileOperations as ejfo
from scipy.stats import pearsonr
from sklearn.model_selection import GridSearchCV

def getLinearRegressionStatistics(ejCSVFilePath=None, ejSheetName=None, ejIVName=None, ejDVName=None):
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

    #  Covariance - All you can really tell from covariance is if there is a positive or negative relationship.
    covariance = np.cov(x, y)
    cov_y = round(covariance[1][0],2)
    # A problem with covariance as a statistical tool alone is that it is challenging to interpret. This leads us to
    # the Pearson’s correlation coefficient Correlation - will give you a value for the relationship. 1 is perfect
    # correlation and 0 is no correlation calculate covariance and Pearson correlation coefficient -
    # https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/
    # calculate Pearson's correlation - The pearsonr() SciPy function can be used to calculate the Pearson’s
    # correlation coefficient between two data samples with the same length
    corrCoef, _ = pearsonr(x, y)
    pearsons_r = round(corrCoef,2)
    # Model Performance : Compute R-Square(=1 best fit, R-Square = 1 - sse/sst) R square - it is a statistical
    # measure of how close the data are to the fitted regression line. It is also known as the coefficient of
    # determination
    model_score_R_square = round(model.score(X,Y), 2)
    # creating dictionary
    dictRegStats = {'x':x, 'y':y, 'mean_x':mean_x, 'mean_y':mean_y,
                    'sst_y':sst_y,'slope':slope,'intercept':intercept,
                    'sse_y':sse_y,'popluation_std_dev': popluation_std_dev,
                    'sample_std_dev':sample_std_dev,'cov_y':cov_y,
                    'pearsons_r':pearsons_r,'regression_equation':regression_equation,
                    'error_y':error_y,'error_square_y':error_square_y,
                    'model_score_R_square':model_score_R_square}
    return dictRegStats

def getRegressionStatistics(ejModel = None, ejFeatureArrayTrain=None, ejTargetArrayTrain=None, ejFeatureArrayTest=None, ejTargetArrayTest=None):
    # fitting regression model
    ejModel.fit(ejFeatureArrayTrain,ejTargetArrayTrain)
    # slope - regression coefficient - Beta one
    #slope = ejModel.coef_
    # intercept - intercept coefficient - Beta not
    #intercept = ejModel.intercept_
    # regression equation
    #regression_equation = "y=" + str(slope) + "x+" + str(intercept)
    model_score_R_square_train = round(ejModel.score(ejFeatureArrayTrain, ejTargetArrayTrain), 2)
    # predict for test data
    y_pred = ejModel.predict(ejFeatureArrayTest)
    # calculate sse sst and r square for test data
    sse = sum((ejTargetArrayTest-y_pred)**2)
    sst = sum((ejTargetArrayTest-np.mean(ejTargetArrayTrain))**2)
    r2 = round(1 - sse / sst,2)
    # creating dictionary
    dictRegStats = {'model_score_R_square_train': model_score_R_square_train,
                    'y predicted': y_pred,
                    'SSE':sse,
                    'SST':sst,
                    'model_score_R_square_test':r2}
    return dictRegStats

def getGridSearchCvStats(ejModel = None, ejFeatureArrayTrain=None, ejTargetArrayTrain=None,ejParameters=None,ejCv=5):
    grid = GridSearchCV(estimator=ejModel, param_grid=ejParameters, cv=ejCv)
    grid.fit(ejFeatureArrayTrain, ejTargetArrayTrain)
    bestParam = grid.best_params_
    bestGridScore = grid.best_score_
    gridSearchCvDict = { 'best_parameter': bestParam,
                         'best_grid_score': bestGridScore
    }
    return gridSearchCvDict

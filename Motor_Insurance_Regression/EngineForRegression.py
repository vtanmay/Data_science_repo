from sklearn.linear_model import LinearRegression

import GFL.ejFileOperations as ejfo
import Motor_Insurance_Regression.BusinessLogicReg as bl
import GFL.ejCharts as ejchs

# read data set from excel
loc = (ejfo.getCurrentWorkingDirecotry()+"\ClaimsVsPayment.xlsx")
claimsAndPaymentData = bl.getClaimsAndPaymentDataFromExcelSheet(ejFilePath=loc, ejSheetName="sample_data")
print("==== data from excel ====", claimsAndPaymentData)

# get column value as list.
x = bl.getClaimsDataAsList(ejFilePath=loc, ejSheetName="sample_data")
y = bl.getPaymentDataAsList(ejFilePath=loc, ejSheetName="sample_data")

linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(x, y)  # perform linear regression
Y_pred = linear_regressor.predict(x)  # make predictions

# draw scatter plot
ejchs.drawScatterPlot(ejXAxisValList=x,  ejYAxisValList=y, ejXAxisLabel="No of Claims", ejYAxisLabel="Total payment", ejYpred=Y_pred)
# draw line of regression
# find slope , intercept, SSE, RMSE, R^2
# use best fit line to make the predictions.
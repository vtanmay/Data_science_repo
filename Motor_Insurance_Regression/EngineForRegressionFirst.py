from sklearn.linear_model import LinearRegression

import GFL.ejFileOperations as ejfo
import Motor_Insurance_Regression.BusinessLogicReg as bl
import GFL.ejCharts as ejchs
import seaborn as sns
import matplotlib.pyplot as plt

# read data set from excel
loc = (ejfo.getCurrentWorkingDirecotry()+"\ClaimsVsPayment.xlsx")
claimsAndPaymentData = bl.getClaimsAndPaymentDataFromExcelSheet(ejFilePath=loc, ejSheetName="sample_data")
print("==== data from excel ====", claimsAndPaymentData)

# get column value as list.
x = bl.getClaimsDataAsList(ejFilePath=loc, ejSheetName="sample_data")
y = bl.getPaymentDataAsList(ejFilePath=loc, ejSheetName="sample_data")

# draw regression line
#Create a linear Regression Model
model=LinearRegression()
# print data frame column names
#print("==== df columns===", claimsAndPaymentData.columns)

#Independent Variable: Feature matrix/(2-D)
X=claimsAndPaymentData[['claims']]
#Dependent Variable: Target matrix/(1-D)
Y=claimsAndPaymentData['payment']
#Fit linear model
model.fit(X,Y)
#Beta-not
print("=====intercept coefficient=====", model.intercept_)
#Beta-One
print("=====regression coefficient=====", model.coef_)
# plot regression line
sns.lmplot("claims","payment",data=claimsAndPaymentData,truncate=True)
plt.show()
# draw scatter plot
#ejchs.drawScatterPlot(ejXAxisValList=x,  ejYAxisValList=y, ejXAxisLabel="No of Claims", ejYAxisLabel="Total payment")

# draw line of regression
# find slope , intercept, SSE, RMSE, R^2
# use best fit line to make the predictions.
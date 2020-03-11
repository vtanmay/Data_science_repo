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

# draw scatter plot
ejchs.drawScatterPlot(ejXAxisValList=x,  ejYAxisValList=y, ejXAxisLabel="No of Claims", ejYAxisLabel="Total payment")
# draw line of regression
# find slope , intercept.
# use best fit line to make the predictions.
import GFL.ejFileOperations as ejfo
from GFL.ejRegression import getRegressionStatistics

loc = (ejfo.getCurrentWorkingDirecotry()+"\ClaimsVsPayment.xlsx")
regressionStats = getRegressionStatistics(ejCSVFilePath=loc, ejSheetName="ClaimsVsPayment", ejIVName="X", ejDVName="Y")
print("==== Regression stats =====", regressionStats)
#claimsAndPaymentData = bl.getClaimsAndPaymentDataFromExcelSheet(ejFilePath=loc, ejSheetName="sample_data")
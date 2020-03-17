import GFL.ejFileOperations as ejfo
from GFL.ejRegression import getRegressionStatistics

loc = (ejfo.getCurrentWorkingDirecotry()+"\ClaimsVsPayment.xlsx")
getRegressionStatistics(ejCSVFilePath=loc, ejSheetName="ClaimsVsPayment", ejIVName="X", ejDVName="Y")
#claimsAndPaymentData = bl.getClaimsAndPaymentDataFromExcelSheet(ejFilePath=loc, ejSheetName="sample_data")
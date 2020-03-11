import GFL.ejPanda as ejpd

def getClaimsAndPaymentDataFromExcelSheet(ejFilePath=None,ejSheetName=None):
    df = ejpd.readXLSFile(ejFilePath, ejSheetName)
    return df

def getClaimsDataAsList(ejFilePath=None,ejSheetName=None):
    df = ejpd.readXLSFile(ejFilePath, ejSheetName)
    listData = ejpd.getColumnDataAsAListFromTable(ejDataFrame=df, ejOptColumnIndex=0)
    return listData

def getPaymentDataAsList(ejFilePath=None,ejSheetName=None):
    df = ejpd.readXLSFile(ejFilePath, ejSheetName)
    listData = ejpd.getColumnDataAsAListFromTable(ejDataFrame=df, ejOptColumnIndex=1)
    return listData
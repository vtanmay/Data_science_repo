import pandas as pd
#https://towardsdatascience.com/21-pandas-operations-for-absolute-beginners-5653e54f4cda
#in order to understand each method use this given below table as a reference
#Table Name: employee
#       date     name   exp     sal    city
#0   1012020   manish  19.5  100000    pune
#1   1022020  jagruti  10.9   50000  nagpur
#2  25012020    rucha   1.5   10000    Pune
#3  23032020   dhruva   0.9    5000  mumbai
#4   1022020  jagdish  12.0   20000  baroda

def getTableFromSQLQuery(ejDBConnectionOBJ=None,ejSQLQuery=None,ejColArray=None):
    SQL_Query =pd.read_sql_query(ejSQLQuery,ejDBConnectionOBJ)
    df = pd.DataFrame(SQL_Query, columns=ejColArray)
    return df
def readXLSFile(ejFilePath=None,ejEitherSheetName=None,ejOrSheetIndex=0):
    if ejEitherSheetName is not None:
       df=pd.read_excel(ejFilePath,sheet_name=ejEitherSheetName)
       return df
    else:
       df= pd.read_excel(ejFilePath,sheet_name=ejOrSheetIndex)
       return df
def createTableFromCSV(ejCSVFilePath=None):
     return pd.read_csv(ejCSVFilePath)
def selectFromTable(ejDataFrame=None,ejOptViewColList=None,ejOptOrderByColNameList=None,ejOptOrder="ASC",ejOptStartFromRecords=0,ejOptEndToRecords=None):
    if ejOptViewColList is None:
        ejOptViewColList=ejDataFrame.columns
    else:
        ejDataFrame=ejDataFrame[ejOptViewColList]

    if ejOptEndToRecords is None:ejOptEndToRecords=ejDataFrame.shape[1]
    if ejOptOrderByColNameList is not None and ejOptOrder=="ASC":
       ejDataFrame=ejDataFrame.sort_values(by=ejOptOrderByColNameList,ascending=True)[ejOptViewColList]
    elif ejOptOrderByColNameList is not None and ejOptOrder=="DESC":
       ejDataFrame=ejDataFrame.sort_values(by=ejOptOrderByColNameList,ascending=False)[ejOptViewColList]
    ejDataFrame.index=range(len(ejDataFrame))#as we have rearrange the rows it is mandatory
    ejDataFrame=ejDataFrame.loc[ejOptStartFromRecords:ejOptEndToRecords]
    return ejDataFrame
def selectTopNRecordsFromTable(ejDataFrame=None,ejTopNRecords=100):
    return ejDataFrame.loc[0:ejTopNRecords]
def selectBottomNRecordsFromTable(ejDataFrame=None,ejBottomNRecords=100):
    return ejDataFrame.tail(ejBottomNRecords)
def selectSpecificRecordsFromTable(ejDataFrame=None,ejStartFromRecords=0,ejEndToRecords=100000):
    return ejDataFrame.loc[ejStartFromRecords:ejEndToRecords]
# To Get Entire Column records From a Given Table
def getColumnDataAsAListFromTable(ejDataFrame=None,ejOptColumnName=None,ejOptColumnIndex=0):
    if ejOptColumnName is not None:
            return ejDataFrame[ejOptColumnName].values.tolist()
    elif ejOptColumnName is None:
            return ejDataFrame[ejDataFrame.columns[ejOptColumnIndex]].values.tolist()
#To Get Entire Row records From a Given Table
def getRowDataAsAListFromTable(ejDataFrame=None,ejOptRowIndex=0,ejRowOptHeader=None):
    if ejOptRowIndex is not None and ejRowOptHeader is None:
        return ejDataFrame.iloc[ejOptRowIndex].values.tolist()
    elif ejOptRowIndex==0 and ejRowOptHeader is not None:
        val= ejDataFrame.loc[ejRowOptHeader].values.tolist()
        return val
def getDataTypeOfAColForTheTable(ejDataframe=None,ejColumnName=None):
    return ejDataframe[ejColumnName].dtype
def setDateAsADataTypeForTheGivenColumn(ejDataFrame=None,ejColumnName=None,ejOptDateTimeFormat="%d%b%Y"):
    ejDataFrame[ejColumnName]=pd.to_datetime(ejDataFrame[ejColumnName], format=ejOptDateTimeFormat)
    return ejDataFrame
def setNumberAsADataTypeForTheGivenColumn(ejDataFrame=None,ejColumnArr=None):
    df=ejDataFrame[ejColumnArr].apply(pd.to_numeric())
    ndf=removeColumnsFromDataFrame(ejDataFrame=ejDataFrame,ejColumnNameList=ejColumnArr)
    return addNewColumns(ejDataFrame=ejDataFrame,ejNewColumnNameList=ejColumnArr,ejNewColumnDataListOfList=df[ejColumnArr])
def setStringAsADataTypeForTheGivenColumn(ejDataFrame=None,ejColumnArr=None):
    df=ejDataFrame[ejColumnArr].astype(str)
    ndf=removeColumnsFromDataFrame(ejDataFrame=ejDataFrame,ejColumnNameList=ejColumnArr)
    return addNewColumns(ejDataFrame=ejDataFrame,ejNewColumnNameList=ejColumnArr,ejNewColumnDataListOfList=df[ejColumnArr])
def getAllColumnNames(ejDataFrame=None):
    return ejDataFrame.columns
def __SingleSquareFilterCriteria(ejDataFrame=None,ejSquareFilter=None,ejIsSearchCaseSensitive=False):
    filter_string=""
    if ejSquareFilter.find("==")>-1:
        colname=ejSquareFilter.replace("[","").replace("]","").split("==")[0]
        colval=ejSquareFilter.replace("[","").replace("]","").split("==")[1]
        filter_string = filter_string + "ejDataFrame['" + colname.strip() + "'].str.contains(" + colval.strip() + ",regex=True,case="+str(ejIsSearchCaseSensitive)+")"
        return filter_string
    if ejSquareFilter.find("!=") > -1:
        colname = ejSquareFilter.replace("[", "").replace("]", "").split("!=")[0]
        colval = ejSquareFilter.replace("[", "").replace("]", "").split("!=")[1]
        filter_string = filter_string + "~ejDataFrame['" + colname.strip() + "'].str.contains(" + colval.strip() + ",regex=True,case="+str(ejIsSearchCaseSensitive)+")"
        return filter_string
def __SingleBracketFilterCriteria(ejDataFrame=None,ejBracketFilter=None,ejIsSearchCaseSensitive=False):
    #([name='manish']|[name='jagruti']&[city='nagpur'])
    final_eval_string=""
    val = ejBracketFilter.replace("(", "").replace(")", "").replace("&","#").replace("|","#").split("#")
    for v in val:
        op=__SingleSquareFilterCriteria(ejDataFrame=ejDataFrame,ejSquareFilter=v,ejIsSearchCaseSensitive=ejIsSearchCaseSensitive)
        ejBracketFilter.find(v)
        ejBracketFilter=ejBracketFilter.replace(v.strip()," "+op.strip()+" ")
    return ejBracketFilter
def searchRecordsAsPerFilterCriteria(ejDataFrame=None, ejFilterCriteria=None,ejIsSearchCaseSensitive=False):
    # 1 ([name=='manish']) 2 ([name=='manish']or[name=='rucha']&['city!='pune'] )
    # 3 ([name=='manish']) or ([name=='sumit']) and ([name=='manish']or[name=='rucha']&['city!='pune'] )
    val = ejFilterCriteria.replace("and", "#").replace("or", "#").split("#")
    for bracketfilter in val:
        op = __SingleBracketFilterCriteria(ejDataFrame=ejDataFrame, ejBracketFilter=bracketfilter,ejIsSearchCaseSensitive=ejIsSearchCaseSensitive)
        ejFilterCriteria = ejFilterCriteria.replace(bracketfilter.strip(), " " + op.strip() + " ")
    print(ejFilterCriteria)
    #ejDataFrame[( ejDataFrame['option_type'].str.contains('PE',regex=True,case=False))] # & ejDataFrame['option_type'].str.contains('PE',regex=True,case=False) )]
    final_eval_string = "ejDataFrame[(" + ejFilterCriteria.replace("or", " | ").replace("and", " & ") + ")]"
    ndf = eval(final_eval_string)
    ndf.index = range(len(ndf))  # as we have rearrange the rows it is mandatory
    return ndf
def addNewColumns(ejDataFrame=None,ejNewColumnNameList=None,ejNewColumnDataListOfList=None):
    ejDataFrame[ejNewColumnNameList]=ejNewColumnDataListOfList
    return ejDataFrame
def removeColumnsFromDataFrame(ejDataFrame=None,ejColumnNameList=None):
    df=ejDataFrame.drop(ejColumnNameList,axis=1)
    return df
#replace all records with specific text
def findAndReplaceCellText(ejDataFrame=None,ejSearchText=None,ejReplaceText=None,ejCaseSensitive=False):
    if ejCaseSensitive:
        return ejDataFrame.replace(to_replace=ejSearchText, value=ejReplaceText)
    else:
        return ejDataFrame.replace(to_replace='(?i)'+ejSearchText,value=ejReplaceText, regex=True)
#instead of row number you can set specific column values as a row index
def setColumnValueAsARowHeader(ejDataFrame=None,ejColumnName=None):
    return ejDataFrame.set_index(ejColumnName,inplace=False)
    # Function to insert row in the dataframe
def addNewRowToDataFrame(ejDataFrame=None,ejNewRowDataList=None,ejOptRowNumber=0):
        start_upper = 0  # Starting value of upper half
        end_upper = ejOptRowNumber         # End value of upper half
        start_lower = ejOptRowNumber        # Start value of lower half
        end_lower = ejDataFrame.shape[0]  # End value of lower half
        upper_half = [*range(start_upper, end_upper, 1)]   # Create a list of upper_half index
        lower_half = [*range(start_lower, end_lower, 1)] # Create a list of lower_half index
        lower_half = [x.__add__(1) for x in lower_half]  # Increment the value of lower half by 1
        index_ = upper_half + lower_half# Combine the two lists
        ejDataFrame.index = index_# Update the index of the dataframe
        ejDataFrame.loc[ejOptRowNumber] = ejNewRowDataList   # Insert a row at the end
        ejDataFrame = ejDataFrame.sort_index()# Sort the index labels
        return ejDataFrame # return the dataframe
def upperCaseAllColumnName(ejDataFrame=None):
    var = {}
    for col in ejDataFrame.columns:
        var[col] = col.upper()
    ejDataFrame.rename(columns=var, inplace=True)
def lowerCaseAllColumnName(ejDataFrame=None):
    var = {}
    for col in ejDataFrame.columns:
        var[col] = col.lower()
    ejDataFrame.rename(columns=var, inplace=True)
def getColumnCounts(ejDataFrame=None):
   return ejDataFrame.shape[1]
def getRowCounts(ejDataFrame=None):
    return ejDataFrame.shape[0]
#order any column either asc or desc order
def arrangeDataAsPerGivenOrder(ejDataFrame=None,ejColumnNameArr=None,ejOrder="ASC"):
    if ejOrder=="ASC":
       return ejDataFrame.sort_values(by=ejColumnNameArr)
    else:
       return ejDataFrame.sort_values(by=ejColumnNameArr,ascending=False)

def getCellData(ejDataFrame=None,ejColumnNameOrNumber=None,ejRowNumber=0):
    if str(type(ejColumnNameOrNumber)).find('str')!=-1:
        val=ejDataFrame[ejColumnNameOrNumber].values.tolist()[ejRowNumber]
    else:
        val = ejDataFrame[ejDataFrame.columns[ejColumnNameOrNumber]].values.tolist()[ejRowNumber]
    return val
#this will reveresed the dataframe by row means last row will be first and first will be last
def reveresedDataframe(ejDataFrame=None):
    ejDataFrame = ejDataFrame.iloc[::-1]
    return ejDataFrame
def sumOfAllHorizontalRecords(ejDataFrame=None,ejColumnArray=None):
    collst = list();  final_list=list();  val=0
    rc=getRowCounts(ejDataFrame=ejDataFrame)
    for r in range(rc):
        for colname in ejColumnArray:
            val=val+getCellData(ejDataFrame=ejDataFrame,ejColumnNameOrNumber=colname,ejRowNumber=r)
        final_list.append(val)
        val=0
    return final_list
def sumOfAllVerticalRecords(ejDataFrame=None,ejColumnArray=None):
    collst = list();  final_list=list();  val=0
    rc=getRowCounts(ejDataFrame=ejDataFrame)
    for colname in ejColumnArray:
        for r in range(rc):
             val=val+getCellData(ejDataFrame=ejDataFrame,ejColumnNameOrNumber=colname,ejRowNumber=r)
        final_list.append(val)
        val=0
    return final_list
def multiplyAllHorizontalRecords(ejDataFrame=None,ejColumnArray=None):
    collst = list();  final_list=list();  val=0
    rc=getRowCounts(ejDataFrame=ejDataFrame)
    for r in range(rc):
        for colname in ejColumnArray:
            val=val*getCellData(ejDataFrame=ejDataFrame,ejColumnNameOrNumber=colname,ejRowNumber=r)
        final_list.append(val)
        val=0
    return final_list
def multiplyAllVerticalRecords(ejDataFrame=None,ejColumnArray=None):
    collst = list();  final_list=list();  val=0
    rc=getRowCounts(ejDataFrame=ejDataFrame)
    for colname in ejColumnArray:
        for r in range(rc):
             val=val*getCellData(ejDataFrame=ejDataFrame,ejColumnNameOrNumber=colname,ejRowNumber=r)
        final_list.append(val)
        val=0
    return final_list
    # Function to insert row in the dataframe

def subtractAllHorizontalRecords(ejDataFrame=None,ejColumnArray=None):
    collst = list();  final_list=list();  val=0
    rc=getRowCounts(ejDataFrame=ejDataFrame)
    for r in range(rc):
        for colname in ejColumnArray:
            val=val-getCellData(ejDataFrame=ejDataFrame,ejColumnNameOrNumber=colname,ejRowNumber=r)
        final_list.append(val)
        val=0
    return final_list
def subtractAllVerticalRecords(ejDataFrame=None,ejColumnArray=None):
    collst = list();  final_list=list();  val=0
    rc=getRowCounts(ejDataFrame=ejDataFrame)
    for colname in ejColumnArray:
        for r in range(rc):
             val=val-getCellData(ejDataFrame=ejDataFrame,ejColumnNameOrNumber=colname,ejRowNumber=r)
        final_list.append(val)
        val=0
    return final_list
def getAllNumericDataTypeColNames(ejDataframe=None):
    numerical_columns=[]
    for col in ejDataframe.columns:
        if (str(ejDataframe[col].dtype) == 'int64' or str(ejDataframe[col].dtype) == 'float64'):
            numerical_columns.append(col)
    return numerical_columns

#---------------------------


#name=rucha or name = %ucha and age=10.12 and salary>3500

#
# #########################################################################################################
# #
# csvfilepath="F:\ML\eJagruti-ML\PANDA\Employee.csv"
# empdf=createTableFromCSV(ejCSVFilePath=csvfilepath)
# df=searchRecordsAsPerFilterCriteria(ejDataFrame=empdf,ejFilterCriteria="([city!='Pune']&[name!='.*agr.*') and ([city=='.*ai'])",ejIsSearchCaseSensitive=False)
# print(df)
# ndf=addNewRowToDataFrame(ejDataFrame=empdf,ejNewRowDataList=["20102020","abhijit","1.8","90000","aurangabad"],ejOptRowNumber=3)
# print(ndf)
# # df=selectFromTableWhereRowValueDoesNotContains(ejDataFrame=empdf,ejColumnToSearch="city",ejSearchValue="DA|pu",ejIsSearchIsCaseSensitive=False)
# # print(df)
# #
# # #mydf=setDateAsADataTypeForTheGivenColumn(ejDataFrame=empdf,ejColumnName=["date"],ejOptDateTimeFormat='%d%m%Y')
# # #ndf=selectFromTable(ejDataFrame=mydf,ejOptOrder="DESC",ejOptOrderByColNameList=["name"],ejOptStartFromRecords=2,ejOptEndToRecords=4)
# #



import xlrd
import pandas as pd

loc = ("D:\Data Science\Manish_Sir_class\Data_science_repo\DataSheet\RiskPrediction2017.xlsx")
dataFromExcel=[]
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(2)
sheet.cell_value(0, 0)

for i in range(sheet.nrows):
    dataFromExcel.append(sheet.cell_value(i, 0))

print(dataFromExcel)

xls = pd.ExcelFile("D:\Data Science\Manish_Sir_class\Data_science_repo\DataSheet\RiskPrediction2017.xlsx")
df1 = pd.read_excel(xls, 'Media Sites')
#df2 = pd.read_excel(xls, 'Sheet2')

print(df1)
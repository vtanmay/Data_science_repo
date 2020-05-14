
import GFL.ejPanda as ejpd
import GFL.ejFileOperations as ejfo
import GFL.ejDataOperations as ejDataOp
import GFL.ejRegression as ejReg
import GFL.ejCharts as ejCharts

# Car dekho Kaggle data.
# https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho/data?select=car+data.csv


# read data
loc = (ejfo.getCurrentWorkingDirecotry()+"\car_data.csv")
carData = ejpd.createTableFromCSV(ejCSVFilePath=loc)
# analyze data
#print("=== data ==", carData)
#print("=== columns==", ejpd.getAllColumnNames(ejDataframe=carData))
#print("== shape ==", ejpd.getDataframeShape(ejDataframe=carData))

# perform Data Pre-processing
# remove any NaN values.
carData = ejpd.getDataframeAfterRemovingNaNValues(ejDataframe=carData)

# remove unwanted features. in our case, car name column.
carData = ejpd.removeColumnsFromDataFrame(ejDataFrame=carData, ejColumnNameList=['Car_Name'])
print("==== data after removing car name ===", carData)

#Independent Variable: Feature matrix/(2-D)
X = carData.copy()
# remove dependent variable
del X['Selling_Price']

# one hot encoding - no of columns generated in one hot encoding = no if categories in a column - 1
# i.e. fuel_type is petrol, diesel, cng - 3-1 = 2 columns generated ,
# transmission is manual , auto - 1 column generated and so on
#Dependent Variable: Target matrix/(1-D)

y = carData.Selling_Price



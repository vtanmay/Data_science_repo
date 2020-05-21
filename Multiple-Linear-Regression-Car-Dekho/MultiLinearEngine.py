
import GFL.ejPanda as ejpd
import GFL.ejFileOperations as ejfo
import GFL.ejDataOperations as ejDataOp
import GFL.ejRegression as ejReg
import GFL.ejCharts as ejCharts
import GFL.ejCorrelation as ejCor
from GFL.ejCorrelation import Correlation
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
# Car dekho Kaggle data.
# https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho/data?select=car+data.csv


# 1. read data
loc = (ejfo.getCurrentWorkingDirecotry()+"\car_data.csv")
carData = ejpd.createTableFromCSV(ejCSVFilePath=loc)
# 2. analyze data
#print("=== data ==", carData)
#print("=== columns==", ejpd.getAllColumnNames(ejDataframe=carData))
#print("== shape ==", ejpd.getDataframeShape(ejDataframe=carData))

# 3. perform Data Pre-processing
# 3.1. remove any NaN values.
carData = ejpd.getDataframeAfterRemovingNaNValues(ejDataframe=carData)

# 3.2 remove unwanted features. in our case, car name column.
carData = ejpd.removeColumnsFromDataFrame(ejDataFrame=carData, ejColumnNameList=['Car_Name'])
#print("==== data after removing car name ===", carData)

# 4. Independent Variable: Feature matrix/(2-D)
X = carData.copy()
# remove dependent variable
del X['Selling_Price']

# 5. one hot encoding - no of columns generated in one hot encoding = no if categories in a column - 1
# i.e. fuel_type is petrol, diesel, cng - 3-1 = 2 columns generated ,
# transmission is manual , auto - 1 column generated and so on
X = ejpd.getOneHotEncodedFeatureMatrix(ejFeatureMatrix=X, ejColumnNameList=['Fuel_Type','Seller_Type','Transmission'])
#print("===== one hot encoded X ===", X.head())
# 6. Dependent Variable: Target matrix/(1-D)
y = carData.Selling_Price

# 7. check for the Collinearity between independent variables.
CorrMatrix =  Correlation.Collinearity.getCorrelationMatrix(ejDataFrame=carData)
# So, looking at the Correlation matrix, we can say there is "NO" multicollinearity.

# 8. split Dataset into train and test.
X_train,X_test,y_train,y_test = ejDataOp.getTrainAndTestData(ejFeatureArray=X, ejTargetArray=y)

# draw 3D graph with critical features.
ejCharts.draw3DGraph(ejDataFrame=carData, ejFisrtColumn="Year", ejSecondColumn="Present_Price", ejThirdColumn="Kms_Driven", ejDv="Selling_Price")





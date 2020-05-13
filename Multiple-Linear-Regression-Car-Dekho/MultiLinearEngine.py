
import GFL.ejPanda as ejpd
import GFL.ejFileOperations as ejfo
import GFL.ejDataOperations as ejDataOp
import GFL.ejRegression as ejReg
import GFL.ejCharts as ejCharts

# Car dekho Kaggle data.
# https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho/data?select=car+data.csv


# read data and analyse
loc = (ejfo.getCurrentWorkingDirecotry()+"\car data.csv")
carData = ejpd.createTableFromCSV(ejCSVFilePath=loc)
print("=== data ==", carData)
print("=== columns==", carData.columns)
print("== shape ==", carData.shape)

import GFL.ejPanda as ejpd
import GFL.ejFileOperations as ejfo
import GFL.ejDataOperations as ejDataOp
import GFL.ejRegression as ejReg
import GFL.ejCharts as ejCharts

# read data and analyse
loc = (ejfo.getCurrentWorkingDirecotry()+"\MarketFallVsOptionPremium.csv")
marketData = ejpd.createTableFromCSV(ejCSVFilePath=loc)
print("=== data ==", marketData)
#print("=== columns==", marketData.columns)
#print("== shape ==", marketData.shape)

#Independent Variable: Feature matrix/(2-D)
X = marketData[['Market fall (%)']]
#Dependent Variable: Target matrix/(1-D)
y = marketData['Option Premium']

# split data set into train and test
X_train,X_test,y_train,y_test = ejDataOp.getTrainAndTestData(ejFeatureArray=X, ejTargetArray=y)
#print("== X test shape 20% of data== ", X_test.shape)

# Build a model on train data.
regStats = ejReg.getLinearRegressionStatistics(ejFeatureArray=X_train,ejTargetArray=y_train)
print("=== graph equation ===", regStats['regression_equation'])
print("=== train data model R square ===", regStats['model_score_R_square'])

# plot the graph and regression line.
ejCharts.drawRegressionLine(ejIv='Market fall (%)', ejDv='Option Premium', ejData=marketData)

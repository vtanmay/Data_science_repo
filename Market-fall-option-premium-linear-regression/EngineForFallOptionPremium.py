

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
regStats = ejReg.getLinearRegressionStatistics(ejFeatureArrayTrain=X_train,ejTargetArrayTrain=y_train,ejFeatureArrayTest=X_test,ejTargetArrayTest=y_test)
print("=== graph equation ===", regStats['regression_equation'])
print("=== train data model R square ===", regStats['model_score_R_square_train'])
print("=== test data R square ===", regStats['model_score_R_square_test'])
#print("==== X TEST ====", X_test)
#print("==== Y Actual ====", y_test)
#print("==== Y Predicted ====", regStats['y predicted'])
#Interpolate data:  If a market falls around 15 %, based upon this study, what would be the expected Option Premium?)
y_opt_prem_15_fall=24.14319249*15+363.76467136150217
print("==== option premium for 15 % fall===", ejDataOp.getNumberRoundedToNearestTenth(ejNo=y_opt_prem_15_fall))

# If a market falls around 95% , what would be the expected Option Premium?
y_opt_prem_95_fall=24.14319249*95+363.76467136150217
print("==== option premium for 95 % fall===", ejDataOp.getNumberRoundedToNearestTenth(ejNo=y_opt_prem_95_fall))

#If  the Option Premium is around 720, based upon this study, how many % market falls expected?
y_market_fall = (720-363.76467136150217)/24.14319249
print("==== market fall % for premium 720 ===", ejDataOp.getNumberRoundedToNearestTenth(ejNo=y_market_fall))
# plot the graph and regression line.
#ejCharts.drawRegressionLine(ejIv='Market fall (%)', ejDv='Option Premium', ejData=marketData)

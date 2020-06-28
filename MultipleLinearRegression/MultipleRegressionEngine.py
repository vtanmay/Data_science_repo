import GFL.ejPanda as ejpd
import GFL.ejFileOperations as ejfo
import GFL.ejCharts as ejch
from GFL.ejCorrelation import Correlation
from sklearn.linear_model import LinearRegression

# read csv
df = ejpd.createTableFromCSV(ejCSVFilePath=ejfo.getCurrentWorkingDirecotry()+"/rds_data_delivery.csv")
#print("==== data===")
print(df)

# find out whether any relationship exists between variable V1,V2,V3 with V4 separately
#ejch.drawPairPlot(ejData=df)

# analysis
#V1 with V4 - positive correlation
# V2 with V4 - positive correlation
# V3 with V4 - not related - can drop this feature - conclusion

#V1 with V2 - positive correlation - highly correlated. 0.95 - multicollinearity ?
# V1 with V3 - not related
# V2 with V3 - not related

# correlation matrix
CorrMatrix =  Correlation.Collinearity.getCorrelationMatrix(ejDataFrame=df)
#print(CorrMatrix)
#ejch.drawHeatMap(ejCondition=df.corr())

# check for the Nan values.
#ejch.drawHeatMap(ejCondition=df.isnull())  # we dont have any Nan values.

# For MilesTraveled vs TravelTimeInHours -
reg1 = LinearRegression()
y=df['TravelTimeInHours']
X=df[['MilesTraveled']]
model1 = reg1.fit(X=X,y=y)
reg_coef1 = model1.coef_
intercept1 = model1.intercept_
print("model 1 slope ", reg_coef1)
print("model 1 intercept ", intercept1)

# For NumOfDeliveries vs TravelTimeInHours -
reg2 = LinearRegression()
y=df['TravelTimeInHours']
X=df[['NumOfDeliveries']]
model2 = reg2.fit(X=X,y=y)
reg_coef2 = model2.coef_
intercept2 = model2.intercept_
print("model 2 slope ", reg_coef2)
print("model 2 intercept ", intercept2)
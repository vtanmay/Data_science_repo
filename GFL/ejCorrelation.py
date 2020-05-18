import plotly.express as px
import pandas as pd
import numpy as np
from numpy import cov
#Defination of Correlation:
#It is a measure of relation between two or more variables
# correlation tells us about the strength between 2 variables.
#denoted as coefficient of correlation i.e. 'r' , it is unit free
# range in between strictly between 0 and 1 0 means no relation and 1 means strong relation
#Four Ways to find the Correlation between 2 variables
#1.ScatterDiagram
#2. Karl Spearsons
#---It is the best methon in all 4
#---Rule : There should be linear relation between 2 variables
#--for formula please search it on google
#3. Spearman Rank Correlation
# this method is used when we want to compare the rank of 2 judge
# it is used when we want to compare the quality compare not compare. beauty with brain
#--for formula please search it on google
#4 Coefficient of Concurrent Deviation i.e. CCD
class Correlation:
    class SpearmansRank:
        def __NormalizeAllColumns(self, dataframe):
            var = {}
            for col in dataframe.columns:
                var[col] = col.upper()
            dataframe.rename(columns=var, inplace=True)
        def getRegressionCoefficient(self, ej_csvfilepath=None, ej_ivcolname=None, ej_dvcolname=None, ej_ivlist=None,ej_dvlist=None):
            dict = {};
            if ej_csvfilepath is not None and ej_ivcolname is not None and ej_dvcolname is not None:
                df = pd.read_csv(ej_csvfilepath)
                self.__NormalizeAllColumns(df)
                x = df[ej_ivcolname.upper()].values.tolist()
                y = df[ej_dvcolname.upper()].values.tolist()
                x_rank=pd.Series(x).rank()
                y_rank = pd.Series(y).rank()
                d=np.subtract(x_rank,y_rank)
                d_square=np.square(d)
                sum_of_d_square=np.sum(d_square)
                n=len(x)
                r=1-((6*sum_of_d_square)/((n*n*n)-n))
                return r
            if ej_csvfilepath is None and ej_ivlist is not None and ej_dvlist is not None:
                x = ej_ivlist; y = ej_dvlist
                x_rank = pd.Series(x).rank()
                y_rank = pd.Series(y).rank()
                d = np.subtract(x_rank, y_rank)
                d_square = np.square(d)
                sum_of_d_square = np.sum(d_square)
                n = len(x)
                r = 1 - ((6 * sum_of_d_square) / ((n * n * n) - n))
                return r
    class KarlPearsons:
        def __NormalizeAllColumns(self, dataframe):
            var = {}
            for col in dataframe.columns:
                var[col] = col.upper()
            dataframe.rename(columns=var, inplace=True)
        def getRegressionCoefficient(self, ej_csvfilepath=None, ej_ivcolname=None, ej_dvcolname=None, ej_ivlist=None,ej_dvlist=None):
            dict = {};
            if ej_csvfilepath is not None and ej_ivcolname is not None and ej_dvcolname is not None:
                df = pd.read_csv(ej_csvfilepath)
                self.__NormalizeAllColumns(df)
                x = df[ej_ivcolname.upper()].values.tolist()
                y = df[ej_dvcolname.upper()].values.tolist()
                sum_x=np.sum(x);sum_y=np.sum(y);xy = np.multiply(x, y);sum_xy=np.sum(xy);n=len(x)
                x_square=np.square(x);sum_x_square=np.sum(x_square);y_square=np.square(y);sum_y_square=np.sum(y_square)
                numerator = ((n * sum_xy) - (sum_x * sum_y))
                denominator = np.sqrt(((n * sum_x_square) - (np.square(sum_x))) * ((n * sum_y_square) - (np.square(sum_y))))
                r = numerator / denominator
                dict["r"]=r;dict["expected_r"]=2/np.sqrt(len(x))
                dict["status"]="Expected Correlation Coefficient Value:"+str(dict["expected_r"])+",Actual Correlation Coefficient Value:"+str(r)+",is Relation Exists:"+("True" if (r > dict["expected_r"]) else "False")
                return dict
            if ej_csvfilepath is None and ej_ivlist is not None and ej_dvlist is not None:
                x = ej_ivlist; y = ej_dvlist
                sum_x = np.sum(x);sum_y = np.sum(y);xy = np.multiply(x, y);sum_xy = np.sum(xy);n = len(x)
                x_square = np.square(x);sum_x_square = np.sum(x_square);y_square = np.square(y);sum_y_square = np.sum(y_square)
                numerator=((n*sum_xy)-(sum_x*sum_y))
                denominator=np.sqrt(((n*sum_x_square)-(np.square(sum_x)))*((n*sum_y_square)-(np.square(sum_y))))
                r=numerator/denominator
                dict["r"] = r;
                dict["expected_r"] = 2 / np.sqrt(len(x))
                dict["status"] = "Expected Correlation Coefficient Value:" + str(dict["expected_r"]) + ",Actual Correlation Coefficient Value:" + str(r) + ",is Relation Exists:" + ("True" if (r > dict["expected_r"]) else "False")
                return dict

    class ScatterDiagram:
        def __NormalizeAllColumns(self, dataframe):
            var = {}
            for col in dataframe.columns:
                var[col] = col.upper()
            dataframe.rename(columns=var, inplace=True)

        def drawScatterPlot(self,ej_csvfilepath=None,ej_ivcolname=None,ej_dvcolname=None,ej_ivlist=None,ej_dvlist=None):
            if ej_csvfilepath is not None and ej_ivcolname is not None and ej_dvcolname is not None:
                  df = pd.read_csv(ej_csvfilepath)
                  self.__NormalizeAllColumns(df)
                  fig = px.scatter(df,x=ej_ivcolname.upper(),y=ej_dvcolname.upper(),)
                  fig.show()
            if ej_csvfilepath is None and ej_ivlist is not None and ej_dvlist is not None :
                fig = px.scatter(x=ej_ivlist, y=ej_dvlist)
                fig.show()

    class Collinearity:
        def getCorrelationMatrix(ejDataFrame=None):
            return ejDataFrame.corr()



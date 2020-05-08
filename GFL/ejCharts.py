import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import scatter_matrix
import seaborn as sns


def drawScatterPlot(ejXAxisValList=None, ejYAxisValList=None, ejXAxisLabel="X", ejYAxisLabel="Y"):
     plt.scatter(x=ejXAxisValList, y=ejYAxisValList,alpha=.1, s=400)
     plt.show()

def drawMultiLineChart(ejXSeries=None,ejNDYArray=None,ejYLineColorArr=['skyblue','blue','green','red','orange','black','yellow','brown','gray','purple'],ejYLineWidthArr=[2,2,2,2,2,2,2,2,2,2],ejYLineStyleArr=['solid','dashed','dotted','dashdot','solid','dashed','solid','dashed','solid','solid'],ejXLabel="X",ejChartTitle='Line Chart',ejYLabelArr=['Y1','Y2','Y3','Y4','Y5','Y6','Y7','Y8','Y9','Y10']):
     dictobj={}
     dictobj['x']=ejXSeries
     for i in range(0,len(ejNDYArray)):
          dictobj[ejYLabelArr[i]] =ejNDYArray[i]
     df=pd.DataFrame(dictobj)
     for i in range(0, len(ejNDYArray)):
          if i==0:
               plt.plot('x', ejYLabelArr[i], data=df, marker='o',markerfacecolor='blue', markersize='12',color=ejYLineColorArr[i],linestyle=ejYLineStyleArr[i], linewidth=ejYLineWidthArr[i])
          else:
               plt.plot('x', ejYLabelArr[i], data=df, marker='', markersize='12', color=ejYLineColorArr[i],linestyle=ejYLineStyleArr[i], linewidth=ejYLineWidthArr[i])
     plt.title(ejChartTitle)
     plt.xlabel(ejXLabel)
     plt.legend()
     plt.show()
def drawScatteredMatrixPlot(ejDataFrame=None,):
     scatter_matrix(ejDataFrame, alpha=1,color="red", figsize=(10, 10),diagonal = 'kde')
     plt.show()

def drawRegressionLine(ejIv, ejDv, ejData):
     sns.lmplot(ejIv, ejDv, data=ejData, truncate=True)
     plt.show()


# df=ejpd.getDataFrameFromCSV(ejCSVFile="F:\ML\eJagruti-ML\Correlation\BeautyContextResult.csv")
# drawScatteredMatrixPlot(ejDataFrame=df)
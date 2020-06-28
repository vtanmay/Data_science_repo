import matplotlib.pyplot as plt
import pandas as pd
from numpy import dot
from pandas.plotting import scatter_matrix
import seaborn as sns
from sklearn.tree import export_graphviz # provides tree in the form of .dot . we convert it into .png and then display.
from IPython.display import Image


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

def drawPredictionVsActualGraph(ejTargetArrayTest=None, ejPredictionDataframe=None, ejDv=None):
     test_index = ejTargetArrayTest.reset_index()[ejDv]
     ax = test_index.plot(label="actuals", figsize=(12, 6), linewidth=2, color="r")
     ax = ejPredictionDataframe[0].plot(label="predictions", figsize=(12, 6), linewidth=2, color="g")
     plt.legend(loc='upper right')
     plt.title("ACTUALS VS PREDICTIONS")
     plt.xlabel("index")
     plt.ylabel("values")
     plt.show()

def draw3DGraph(ejDataFrame=None,ejFisrtColumn=None, ejSecondColumn=None, ejThirdColumn=None, ejDv=None):
     fig = plt.figure(figsize=(16, 9))
     ax = fig.gca(projection="3d")

     plot = ax.scatter(ejDataFrame[ejFisrtColumn],
                       ejDataFrame[ejSecondColumn],
                       ejDataFrame[ejThirdColumn],
                       linewidth=1, edgecolor="k",
                       c=ejDataFrame[ejDv], s=100, cmap="hot")

     ax.set_xlabel(ejFisrtColumn)
     ax.set_ylabel(ejSecondColumn)
     ax.set_zlabel(ejThirdColumn)

     lab = fig.colorbar(plot, shrink=.5, aspect=5)
     lab.set_label(ejDv, fontsize=15)

     plt.title("3D plot for "+ ejFisrtColumn+" ,"+ ejSecondColumn+ " and "+ejThirdColumn, color="red")
     plt.show()

def drawDecisionTree(ejModel = None,ejFeatureNames=None):
     export_graphviz(ejModel, out_file='Regtree.dot', feature_names=ejFeatureNames)
     # using shell command to convert .dot file to .png file
   #  ! dot - Tpng Regtree.dot - o Regtree.png
     Image("Regtree.png")

def drawPairPlot(ejData=None):
     sns.pairplot(data=ejData)
     plt.show()

def drawHeatMap(ejCondition=None,ejCmap='viridis'):
     sns.heatmap(data=ejCondition,cmap=ejCmap)
     plt.show()


# df=ejpd.getDataFrameFromCSV(ejCSVFile="F:\ML\eJagruti-ML\Correlation\BeautyContextResult.csv")
# drawScatteredMatrixPlot(ejDataFrame=df)
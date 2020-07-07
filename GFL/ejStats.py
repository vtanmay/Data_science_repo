import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp

class Statistics:
    def __NormalizeAllColumns(self, dataframe):
        var = {}
        for col in dataframe.columns:
            var[col] = col.upper()
        dataframe.rename(columns=var, inplace=True)
    def __mode(self,array):
        most = max(list(map(array.count, array)))
        final_list= list(set(filter(lambda x: array.count(x) == most, array)))
        return sorted(final_list)
    def __doAnalysis(self,ejSerIV=None):
        dict = {};
        dict["values"] = ejSerIV
        dict["asc_values"] = sorted(ejSerIV, reverse=False)
        dict["desc_values"] = sorted(ejSerIV, reverse=True)
        dict["count"] = len(ejSerIV)
        dict["min"] = np.min(ejSerIV)
        dict["max"] = np.max(ejSerIV)
        dict["range"] = dict["max"] - dict["min"]
        # the middle value of the given series
        dict["median"] = np.median(ejSerIV)
        # The mode is the number that appears most frequently in a set
        dict["mode"] = self.__mode(self,ejSerIV)
        # the average
        dict["mean"] = np.mean(ejSerIV)
        dict["sample_variance"] = np.square(np.std(ejSerIV, ddof=1, dtype=np.float64))
        dict["population_variance"] = np.square(np.std(ejSerIV, dtype=np.float64))
        dict["population_standard_deviation"] = np.std(ejSerIV, dtype=np.float64)
        dict["sample_standard_deviation"] = np.std(ejSerIV, ddof=1, dtype=np.float64)
        #error Sum of Square
        dict["sse"] = np.sum(np.square(pd.Series(ejSerIV).subtract(np.mean(ejSerIV)).tolist()))  # sum of squared error i.e. residual square
        #total sum of error square
        dict["sst_y"]=dict["sse"]
        return dict
    def getStatisticalInfo(self, ej_csvfilepath=None, ej_colname=None, ej_list=None):
        if ej_csvfilepath is not None and ej_colname is not None:
            df = pd.read_csv(ej_csvfilepath)
            # normalize all the column name
            self.__NormalizeAllColumns(self,df)
            serIV = df[ej_colname.upper()].values.tolist()
            return self.__doAnalysis(self,ejSerIV=serIV)
        if ej_csvfilepath is None and ej_list is not None:
            serIV = ej_list
            return self.__doAnalysis(self,ejSerIV=serIV)

    def perform1SampleTtest(self,ejSample,ejPopulationMean):
        ttest, p_value = ttest_1samp(ejSample, ejPopulationMean)
        return ttest, p_value


def perform1SampleTtest(sample, population_mean):
    return None
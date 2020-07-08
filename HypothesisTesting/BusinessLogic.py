from GFL.ejStats import Statistics
import GFL.ejFileOperations as ejfo
import GFL.ejPanda as pd

class BusinessLogic:

    population_mean = 1.25
    t_value_level_of_significance = 1.699

    def __getSampleSubset(self, ejPlantNo, ejBatchNo, sample=None):
        if ejPlantNo == 1:
            loc = (ejfo.getCurrentWorkingDirecotry() + "/plantt1.csv")
            df = pd.createTableFromCSV(loc)
            if ejBatchNo == 1:
                sample = df.iloc[1:30, :]
            elif ejBatchNo == 2:
                sample = df.iloc[53:82, :]
            elif ejBatchNo == 3:
                sample = df.iloc[155:184, :]
            else:
                print('please enter correct batch no.')
        elif ejPlantNo == 2:
            loc = (ejfo.getCurrentWorkingDirecotry() + "/plantt2.csv")
            df = pd.createTableFromCSV(loc)
            if ejBatchNo == 1:
                sample = df.iloc[2:31, :]
            elif ejBatchNo == 2:
                sample = df.iloc[53:82, :]
            elif ejBatchNo == 3:
                sample = df.iloc[155:184, :]
            else:
                print('please enter correct batch no.')
        else:
            print('please enter correct plant no.')
        return sample

    def validateBatch(self,ejPlantNo, ejBatchNo):
        sample = self.__getSampleSubset(ejPlantNo, ejBatchNo)
        st = Statistics()
        if sample is not None:
            ttest, p_value = st.perform1SampleTtest(sample[' PpM'], self.population_mean)
            if ttest > self.t_value_level_of_significance:
                print('Batch is rejected.')
            else:
                print('Batch is accepted.')









import pandas as pd
class Descriptive():
    def init(self):
        pass
    def segreQuanQual(dataset):
        quantative=[]
        qualtative=[]

        for i in dataset.columns:
  
            if(dataset[i].dtypes =='object' or dataset[i].dtypes =='bool'):
                qualtative.append(i)
            else:
                quantative.append(i)
        print("The Quantitative Data:",quantative)
        print("The Qualtitative Data",qualtative)
        return quantative,qualtative
    def descriptive_Analysis(dataset,quantative):
        import pandas as pd
        import numpy as np
        des_data=pd.DataFrame(index=["Count","Mean","Median","Std","Mode","Min","Q1:25%","Q2:50%","Q3:75%","Q4:100%","IQR","1.5Rule",
                            "Lesser","Greater"],columns=quantative)
        

        for i in quantative:
            des_data[i]["Count"]=len(dataset[i])
            des_data[i]["Mean"]=dataset[i].mean()
            des_data[i]["Median"]=dataset[i].median()
            des_data[i]["Mode"]=dataset[i].mode()[0]
            des_data[i]["Std"]=dataset[i].std()
            des_data[i]["Min"]=dataset[i].min()
            des_data[i]["Q1:25%"]=np.percentile(dataset[i],25)
            des_data[i]["Q2:50%"]=np.percentile(dataset[i],50)
            des_data[i]["Q3:75%"]=np.percentile(dataset[i],75)
            des_data[i]["Q4:100%"]=dataset[i].max()
            des_data[i]["IQR"]=des_data[i]["Q3:75%"]-des_data[i]["Q1:25%"]
            des_data[i]["1.5Rule"]=1.5* des_data[i]["IQR"]
            des_data[i]["Lesser"]= des_data[i]["Q1:25%"]-des_data[i]["1.5Rule"]
            des_data[i]["Greater"]= des_data[i]["Q3:75%"]+des_data[i]["1.5Rule"]

        return des_data
    def outliercolumn(quantative,des_data):
        lesser=[]
        greater=[]

        for i in quantative:
            if(des_data[i]["Lesser"]>des_data[i]['Min']):
                lesser.append(i)
            if(des_data[i]['Greater']<des_data[i]['Q4:100%']):
                greater.append(i)

        print("Lesser Range",lesser)
        print("Greater Range",greater)
        return lesser,greater

    def changeoutlier(dataset,des_Data,lesser,greater):
        for i in lesser:
            dataset[i][dataset[i]<des_Data[i]['Lesser']]=des_Data[i]['Lesser']
        #print(dataset[i])
        for j in greater:
            dataset[j][dataset[j]<des_Data[j]['Greater']]=des_Data[j]['Greater']
        return des_Data
    
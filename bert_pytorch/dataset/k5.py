import numpy as np
import pandas as pd

datak5=pd.read_csv('nas.csv')
data_train_x=[]
data_train_y=[]
data_test=[]

for i in range(len(datak5)-6):
    data_train_x.append(datak5.iloc[i:i+5])
    data_train_y.append(datak5.iloc[i+6])
    data_test.append(datak5.iloc[i+1:i+6])


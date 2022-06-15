import numpy as np
import pandas as pd

datak5=pd.read_csv('nas.csv')
data_train=[]
data_y=[]

for i in range(len(datak5)-6):
    data_train.append(datak5.iloc[i:i+5])
    data_y.append(datak5.iloc[i+6])


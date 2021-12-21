import os
import pandas as pd
import numpy as np
columns=['month','average']

for i in range(2005,2016):
    columns.append(str(i))

df = pd.read_csv("D:\Irvan\work\learning\learning\data\hurricanes.csv", names=columns)

print(df.sum(axis=1))

"""
for index, row in df.iterrows():
    print(row['2005'], row['2006'])

    if(df['2005'].astype("str") == 0):
        print('No Hurricanes')
    else:
        print('with hurricanes')
"""


def _getRowColumns(df):
    rowColumns=df.shape
    rowColumns=[[rowColumns[0],rowColumns[1]]]
    rowColumns=pd.DataFrame(rowColumns, index = [""], columns = ["Rows","Columns"])

    try:
        display(rowColumns)
    except NameError:
        print(rowColumns)


_getRowColumns(df)


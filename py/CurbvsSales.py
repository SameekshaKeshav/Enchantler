#!/usr/bin/env python
# coding: utf-8

#uses cleanedSalesData when exists if not uses CleanSalesData.py to produce one and use it
#uses matplot library to produce the chart of Sales against curb weight of the vehicle
#plot is exported as jpg file to the images folder
#browser is directed to show the image via the image tag from the enclosing php file that calls this function

import numpy as np
import pandas as pd      #for data processing
import matplotlib.pyplot as plt     #for data visualization
import seaborn as sns
import os.path as path

file_exists = path.exists('./data/CleanedSalesData.csv')
if(file_exists):
    print("File exists")
else:
    print("File does not exist")
    import CleanSalesData
df_no_mv = pd.read_csv('./data/CleanedSalesData.csv')
df1 = df_no_mv[['Curb_weight','Sales_in_thousands']]
df2 = df1.groupby('Curb_weight')['Sales_in_thousands'].sum().reset_index(name ='Sales_in_thousands')

ypoints = np.array(df2['Sales_in_thousands'])
labels = np.array(df2['Curb_weight'])
plt.figure(figsize =(14, 7))
plt.pie(ypoints,labels = labels,rotatelabels =True) 
plt.title("sales share by Curb weight",bbox={'facecolor':'0.8', 'pad':5})
plt.xticks(rotation=90)
plt.gcf().subplots_adjust(bottom=0.2)
plt.savefig('./images/output.jpg')


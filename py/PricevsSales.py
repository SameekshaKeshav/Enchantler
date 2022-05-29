#!/usr/bin/env python
# coding: utf-8

#uses cleanedSalesData when exists if not uses CleanSalesData.py to produce one and use it
#uses matplot library to produce the chart of Sales against price range
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
ypoints = np.array(df_no_mv['Sales_in_thousands'])
xpoints = np.array(df_no_mv['Price_range'])
x_ticks_labels = ['05 to 10','10 to 15','15 to 20','20 to 25','25 to 30','30 to 35','35 to 40','40 to 45','45 to 50','50 to 55','60 to 65','65 to 70','70 to 75','80 to 85','85 to 90']
plt.figure(figsize =(14, 7))
sns.barplot(x=xpoints,y=ypoints,ci=None,order = x_ticks_labels)
plt.xlabel("Price_range(in thousand USD)")
plt.ylabel("Sales_in_thousands")
plt.gcf().subplots_adjust(bottom=0.15)
plt.xticks(rotation=90)
plt.savefig("./images/output.jpg")

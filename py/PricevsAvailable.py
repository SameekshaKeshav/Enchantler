
# coding: utf-8

#uses cars_engage_2022.csv sample file provided for this mentorship program
#uses matplot library to produce the chart of number of options available by the price range
#plot is exported as jpg file to the images folder
#browser is directed to show the image via the image tag from the enclosing php file that calls this function

import numpy as np
import pandas as pd      #for data processing
import matplotlib.pyplot as plt     #for data visualization
import seaborn as sns
import os.path as path
import math

df_no_mv = pd.read_csv('./data/cars_engage_2022.csv')
def custom_round_n(x, base):
    if(x>10000000):
        return  50*base*math.ceil(float(x)/(50*base))
    elif(x>2000000):
        return  10*base*math.ceil(float(x)/(10*base))
    return  base*math.ceil(float(x)/base)

df_no_mv['Ex_Showroom_Price'] = df_no_mv['Ex_Showroom_Price'].apply(lambda x: custom_round_n(x, base=100000))
counts = df_no_mv['Ex_Showroom_Price'].value_counts()
res = df_no_mv[~df_no_mv['Ex_Showroom_Price'].isin(counts[counts < 4].index)]
plt.figure(figsize=(14,7))
ax = sns.countplot(x="Ex_Showroom_Price", data=res)
plt.xlabel('Price')
plt.ylabel('count of models')
plt.gcf().subplots_adjust(bottom=0.2)
plt.xticks(rotation=90)
plt.savefig("./images/output.jpg")


# coding: utf-8

#uses cars_engage_2022.csv sample file provided for this mentorship program
#uses matplot library to produce the chart of number of options available by the manufacturer
#plot is exported as jpg file to the images folder
#browser is directed to show the image via the image tag from the enclosing php file that calls this function

import numpy as np
import pandas as pd      #for data processing
import matplotlib.pyplot as plt     #for data visualization
import seaborn as sns
import os.path as path
import math

df_no_mv = pd.read_csv('./data/cars_engage_2022.csv')

counts = df_no_mv['Make'].value_counts()
res = df_no_mv[~df_no_mv['Make'].isin(counts[counts < 20].index)]
plt.figure(figsize=(14,7))
ax = sns.countplot(x="Make", data=res)
plt.xlabel('Manufacturer')
plt.ylabel('count of models')
plt.gcf().subplots_adjust(bottom=0.25)
plt.xticks(rotation=90)
plt.savefig("./images/output.jpg")

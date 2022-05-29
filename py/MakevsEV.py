#!/usr/bin/env python
# coding: utf-8

#uses EVRegistrationData obtained from IHS website available for public consumption
#uses matplot library to produce the chart of number of vehicles registered by consumers against the manufacturer
#plot is exported as jpg file to the images folder
#browser is directed to show the image via the image tag from the enclosing php file that calls this function

import numpy as np
import pandas as pd      #for data processing
import matplotlib.pyplot as plt     #for data visualization
import seaborn as sns

df = pd.read_csv("./data/EVRegistrationData.csv")
df1 = df[['MAKE','EV_VEHICLES']]
df1=df1.groupby('MAKE')['EV_VEHICLES'].sum().reset_index(name ='EV_VEHICLES')
df3 = df1[df1['EV_VEHICLES'] > 50000]
summ = df1[df1['EV_VEHICLES'] <= 50000]['EV_VEHICLES'].sum()
df3.loc[len(df3.index)] = ['Others', summ] 

ypoints = np.array(df3['EV_VEHICLES'])
xpoints = np.array(df3['MAKE'])
plt.figure(figsize =(14, 7))
sns.barplot(x=xpoints,y=ypoints,ci=None)
plt.xlabel("Manufacturer")
plt.ylabel("Number of vehicles")
plt.gcf().subplots_adjust(bottom=0.25)
plt.xticks(rotation=90)
plt.savefig("./images/output.jpg")

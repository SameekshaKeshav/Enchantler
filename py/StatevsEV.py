
# coding: utf-8

#uses EVRegistrationData obtained from IHS website available for public consumption
#uses matplot library to produce the chart of number of vehicles registered by the state
#plot is exported as jpg file to the images folder
#browser is directed to show the image via the image tag from the enclosing php file that calls this function

import numpy as np
import pandas as pd      #for data processing
import matplotlib.pyplot as plt     #for data visualization
import seaborn as sns

df = pd.read_csv("./data/EVRegistrationData.csv")
df1 = df[['STATE','EV_VEHICLES']]
df2 = df1.groupby('STATE')['EV_VEHICLES'].sum().reset_index(name ='EV_VEHICLES')
df3 = df2[df2['EV_VEHICLES'] > 20000]
summ = df2[df2['EV_VEHICLES'] <= 20000]['EV_VEHICLES'].sum()
df3.loc[len(df3.index)] = ['Others', summ] 
ypoints = np.array(df3['EV_VEHICLES'])
labels = np.array(df3['STATE'])
plt.figure(figsize =(14, 7))
colors = sns.diverging_palette(20, 145)
colors.reverse()
plt.pie(ypoints, labels = labels,rotatelabels =True,colors = colors)
plt.gcf().subplots_adjust(bottom=0.2)
plt.savefig('./images/output.jpg')

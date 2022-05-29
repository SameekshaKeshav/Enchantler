#!/usr/bin/env python
# coding: utf-8

# cleans the source dataset (Car_sales.csv) and creates the cleaned dataset (CleanedSalesData.csv) in ..\data folder

import numpy as np
import pandas as pd      #for data processing
import matplotlib.pyplot as plt     #for data visualization
import seaborn as sns
import math

raw = pd.read_csv("./data/Car_sales.csv")
raw.head()       #displays first 5 records of the dataset
#complete analysis of dataset(each column)
raw.describe(include = "all")
#for the reggression model we need to drop certain unwanted attributes
df = raw.drop(['Model','Latest_Launch'], axis = 1)
df.describe(include="all")
#we have to clean the missing values
#to find number of missing values in each dataset
df.isnull().sum()
#lets drop records with missing values

df_no_mv = df.dropna(axis=0)
df_no_mv.describe(include="all")
#visualizing unique values in each column
for m in df_no_mv.keys():
    print(m,df_no_mv[m].unique()[:10])
#if any ? present in dataset
(df_no_mv == '?').sum()

def custom_round_n(x, base):
    return  base*math.ceil(float(x)/base)

df_no_mv['Curb_weight'] = df_no_mv['Curb_weight'].apply(lambda x: custom_round_n(x, base=0.5))
df_no_mv['Horsepower'] = df_no_mv['Horsepower'].apply(lambda x: custom_round_n(x, base=50))
df_no_mv['Fuel_efficiency'] = df_no_mv['Fuel_efficiency'].apply(lambda x: custom_round_n(x, base=2))
#Exporting the file as cleaned datset
df_no_mv.to_csv('./data/CleanedSalesData.csv')

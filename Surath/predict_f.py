# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 22:55:09 2019

@author: Surath
"""
#import useful libraries to predict fuel economy
import pandas as pd
from sklearn import linear_model

#Read Original CSV file 
df = pd.read_csv("vehicle_details_not_.csv" )

#Columns Filtter according to the data type and create new object using filtered data
obj_df = df.select_dtypes(include=['object','float','int64']).copy()

#Set dummy variables to transmission Type , Fuel type and vehicle's Body Type
cleanUp1 = {"transmission_name":{"Automatic": 1, "Manual": 2},
                "fuel_name": {"Petrol": 1, "Full-Hybrid": 2, "Mild-Hybrid": 3 },
                "type_name":{"Saloon": 1, "Hatchback": 2, "Off-Road Vehicle / SUV": 3}}
#Replace defined columns in obj_df object's columns
obj_df.replace(cleanUp1, inplace=True)

#Type name convert as float type from int64
obj_df['type_name'] = obj_df.type_name .astype(float)

#Create new object for the linear regression
reg = linear_model.LinearRegression()
reg.fit(obj_df[['type_name' ,  'year','transmission_name' ,'fuel_name','engine_engineId']] , obj_df.cons_consId)

#Incorporating necessary data for forecasting
result = reg.predict([[2.0,2012,1,1,1000]])

#outcome of the predict result
print(result)
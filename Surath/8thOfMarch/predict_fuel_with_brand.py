# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:09:25 2019

@author: Surath
"""


#import useful libraries to predict fuel economy
import pandas as pd
from sklearn import linear_model

#Read Original CSV file 
df = pd.read_csv("vehicle_details_not_II.csv" )

#Columns Filtter according to the data type and create new object using filtered data
obj_df = df.select_dtypes(include=['object','float','int64']).copy()

#Set dummy variables to transmission Type , Fuel type and vehicle's Body Type
cleanUp1 = {"transmission_name":{"Automatic": 1, "Manual": 2 , "Tiptronic":3},
                "fuel_name": {"Petrol": 1, "Full-Hybrid": 2, "Mild-Hybrid": 3 ,"Diesel":4,"Plug-in-Hybrid":5 },
                "type_name":{"Saloon": 1, "Hatchback": 2, "Off-Road Vehicle / SUV": 3},
                "brand_name":{"Suzuki": 1, "Honda": 2, "Toyota": 3 ,"Mitsubishi":4 ,"Renault":5}}
#Replace defined columns in obj_df object's columns
obj_df.replace(cleanUp1, inplace=True)

#Type name convert as float type from int64
obj_df['type_name'] = obj_df.type_name .astype(float)

#Type name convert as float type from int64
obj_df['brand_name'] = obj_df.brand_name .astype(float)

#Create new object for the linear regression
reg = linear_model.LinearRegression()
reg.fit(obj_df[['type_name' ,'brand_name',  'year','transmission_name' ,'fuel_name','engine_engineId']] , obj_df.cons_consId)

#Incorporating necessary data for forecasting
###################### Vehicle Type -- Saloon (1) -- Hatchbach (2) -- SUV (3)
###################### Brand Name  -- Suzuki (1) -- Honda (2) --Toyota (3) -- Mitsubishi (4) -- Renault (5)
###################### Manufacture Year
###################### Fuel Type --Petrol (1) -- Full-Hybrid (2) -- Mild-Hybrid (3) -- Diesel(4) -- Plug In Hybrid (5)
###################### Transmission Type -- Automatic (1) -- Manual (2) -- Triptonic (3)
###################### Engine Capacity 
result1 = reg.predict([[3.0,2.0,2011,1,1,1500]])
result2 = reg.predict([[2.0,1.0,2014,3,1,660]])
result3 = reg.predict([[2.0,1.0,2011,1,2,800]])
result4 = reg.predict([[1.0,3.0,2008,1,1,1500]])
result5 = reg.predict([[1.0,3.0,2010,1,1,1500]])
#outcome of the predict result
print("Honda CR-V")
print(result1)

print("Suzuki Wagon R")
print(result2)

print("Suzuki Alto")
print(result3)

print("Toyota Axio")
print(result4)

print("Toyota Allion")
print(result5)


#print("Toyota Axio "+result)
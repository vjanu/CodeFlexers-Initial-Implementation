# -*- coding: utf-8 -*-
"""2019
Created on Fri May  3 00:55:52 

@author: Surath
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('wagon-R-Final.csv')
X = dataset.iloc[:, 2:-1]
y = dataset.iloc[:, 9]


#Convert the column into categorical columns

states=pd.get_dummies(X['Fuel'],drop_first=True)

# Drop the state coulmn
X=X.drop('Fuel',axis=1)

# concat the dummy variables
X=pd.concat([X,states],axis=1)


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

from sklearn.metrics import r2_score
score=r2_score(y_test,y_pred)


cleanUp1 = {"Fuel":{"P - Hybrid": 1, "P": 2}}
#Replace defined columns in obj_df object's columns
dataset.replace(cleanUp1, inplace=True)

regressor.fit(dataset[['Year_of_ Man' ,'First_Reg',  'Cylinders','Fuel' ,'Capacity','kW','Mileage']] , dataset.Fuel_consumption)
result1 = regressor.predict([[2015,2015,3,2,998,50,134553]])
print(result1)


print('Coefficients: \n', regressor.coef_)
# The mean squared error
print("Mean squared error: %.2f" % np.mean((regressor.predict(X_test) - y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regressor.score(X_test, y_test))
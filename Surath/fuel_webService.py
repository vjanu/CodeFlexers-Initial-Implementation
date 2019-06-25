#!flask/bin/python
from flask import jsonify,Flask
import json
from flask import request


# Importing the libraries
import numpy as np
#import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LinearRegression
app = Flask(__name__)


@app.route('/update/', methods=['GET'])
def zz():
	return 'Updated'

@app.route('/fuel/<manYear>/<regYear>/<cylinders>/<fuel>/<capacity>/<kW>/<mileage>', methods=['GET'])
def fuelPrediction(manYear,regYear,cylinders,fuel ,capacity,kW,mileage) :

    #DEFINE FUEL PRICES
    petrol = 135.0
    diesel = 104.0


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
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

    # Fitting Multiple Linear Regression to the Training set
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = regressor.predict(X_test)

    cleanUp1 = {"Fuel":{"P - Hybrid": 1, "P": 2}}
    #Replace defined columns in obj_df object's columns
    dataset.replace(cleanUp1, inplace=True)

    regressor.fit(dataset[['Year_of_ Man' ,'First_Reg',  'Cylinders','Fuel' ,'Capacity','kW','Mileage']] , dataset.Fuel_consumption)
    result = regressor.predict([[int(manYear),int(regYear),int(cylinders),int(fuel),int(capacity),int(kW),float(mileage)]])
    print(result)
    if fuel == "1" or fuel== "2" :
        finalResult = petrol/result[0]
    else :
        finalResult =  diesel/result[0]

    print(finalResult)
    return jsonify(fuelPrediction=finalResult)


app.run(debug=True,host="192.168.8.100",port=96)
#if __name__ == '__main__':
#    app.run(debug=True)
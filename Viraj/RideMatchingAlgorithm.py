# K-Means Clustering

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import json
import re
from flask import Flask, jsonify
df = pd.read_csv('datausers.csv')
app = Flask(__name__)
#get the userID of the passenger(Frontend fetch)
UID = 544571380092

#get the index of the row which belongs to particular passenger
index = df[df['UID']== UID].index.values.astype(int)[0]
#print(df.iloc[index]) # print data of the row
#print(df[df['UID']== UID].iloc[:,11]) # print data of the row
#print(df[df['UID']== UID].iloc[:,12]) # print data of the row
#print(df[df['UID']== UID].iloc[:,13]) # print data of the row
#print(df[df['UID']== UID].iloc[:,14]) # print data of the row
#print(df[df['UID']== UID].iloc[:,10]) # print data of the row


@app.route('/ridematching/rules', methods=['GET'])
def executeRules():
	#get the properties of the specified user and assign it to variables
	isSmoking = df[df['UID']== UID].iloc[:,7].values[0]
	isMusicLover = df[df['UID']== UID].iloc[:,8].values[0]
	isMotionSickness = df[df['UID']== UID].iloc[:,9].values[0]
	isLikeQuietness = df[df['UID']== UID].iloc[:,10].values[0]
	isGenderPrefered = df[df['UID']== UID].iloc[:,6].values[0]
	rules(isSmoking, isMusicLover, isMotionSickness, isLikeQuietness, isGenderPrefered)
	return "success";

@app.route('/ridematching/kmeans', methods=['GET'])
def getSuitableDriverList():
	return driverList()


#Defining rules for the filteration
#todo add more rules - language spoken?
def rules(smokingFlag, musicFlag, motionFlag, quietnessFlag, genderFlag):
	df.loc[(df['Smoking'] == smokingFlag) & (df['Music_Lover'] == musicFlag) & (df['Motion_Sickness'] == motionFlag) & (df['Gender_Preference'] == genderFlag) 
	& (df['Like_Quietness'] == quietnessFlag)].to_csv('newUsers.csv', index=False);
	

#Execute rule based mechanism 
#rules(isSmoking, isMusicLover, isMotionSickness, isLikeQuietness);


def driverList():
	dataset = pd.read_csv('newUsers.csv')
	X = dataset.iloc[:,[3,4]].values # read columns Age-x axis and Profession-y axis

	# Using the elbow method to find the optimal number of clusters
	from sklearn.cluster import KMeans
	wcss =[]
	for i in range (1,11):
		kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter =200, n_init = 10, random_state = 0)
		kmeans.fit(X)
		wcss.append(kmeans.inertia_) #Within Cluster Sum of Squares

	# Applying KMeans to the dataset with the optimal number of cluster
	kmeans=KMeans(n_clusters = 3, init = 'k-means++', max_iter = 200, n_init = 10, random_state = 0)
	Y_Kmeans = kmeans.fit_predict(X)


	#get clusters and sort them into new file
	dataset["Cluster"] = Y_Kmeans
	dataset.sort_values(by='Cluster',  inplace=True)
	dataset.to_csv('final.csv', index=False)

	#specify the cluster where the particular passenger belongs to
	n = dataset[dataset['UID']== UID].iloc[:,11].values[0]

	#ds = X[np.where(kmeans.labels_== n)] #get particular cluster
	#print(ds)
	#print(dataset.loc[dataset['Cluster'] == n])

	#Initialize lists required
	uIDList= list()
	formattedUIDList= list()
	filteredList=list()

	dataListOfSuitableDrivers = dataset.loc[dataset['Cluster'] == n, ['UID']]
	uIDList = dataListOfSuitableDrivers.values.tolist()
    # remove reported drivers from the list(uIDList - entries from db)
	#uIDList.remove([161493])
	#print(uIDList)
	
	dataListOfSuitableDrivers.to_csv('selectedDrivers.csv', index=False)
	#uIDList.append(dataListOfSuitableDrivers.get('UID'))
		
	#database call to get reported list for particular UID
	#filteredList = uIDList - [1,2,3,4,5]
	
	#removing unwanted characters from the list
	for uid in uIDList:
		formattedUIDList.append(uid[0]) 

	
	#filteredList = [1,2,3,4,5]

	#dataset = pd.DataFrame(filteredList)
	#dataset.to_csv('selectedDrivers.csv')
	
	#return the final driver list in JSON
	return jsonify(
	UID = formattedUIDList
	)

		
	#print(dataset[kmeans.labels_== n]) # get dataset in each cluster
	#print(dataset['UID']== UID) # get true for paticular row
	#print(dataset[dataset['UID']== UID].index.values.astype(int)[0]) # get index of row which has UID index
if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=80)
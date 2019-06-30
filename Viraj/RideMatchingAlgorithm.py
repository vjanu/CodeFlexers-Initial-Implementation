# K-Means Clustering

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import json
import re
from flask import Flask, jsonify, request
#import mysql.connector
import os
from tempfile import NamedTemporaryFile

#mydb = mysql.connector.connect(
 # host="db4free.net",
  #user="cdapadmin",
  #passwd="cdapcdap",
  #database="plusgo"
#)

#mycursor = mydb.cursor()

df = pd.read_csv('datausers.csv')
#q = pd.read_csv('availableDrivers.csv')

tempfile = NamedTemporaryFile(mode='w', delete=False)
app = Flask(__name__)

def executeRules(UserID):
	global UID
	UID = UserID
	#print(UID)
	
	#get the properties of the specified user and assign it to variables
	isSmoking = df[df['UID']== UID].iloc[:,7].values[0]
	isMusicLover = df[df['UID']== UID].iloc[:,8].values[0]
	isMotionSickness = df[df['UID']== UID].iloc[:,9].values[0]
	isLikeQuietness = df[df['UID']== UID].iloc[:,10].values[0]
	isGenderPrefered = df[df['UID']== UID].iloc[:,6].values[0]
	rules(isSmoking, isMusicLover, isMotionSickness, isLikeQuietness, isGenderPrefered)
	
@app.route('/ridematching/write', methods=['POST']) # When new user is registered
def getFileData():
	uid = request.get_json().get('UID')
	profession = request.get_json().get('Profession')
	rating = request.get_json().get('Rating')
	age = request.get_json().get('Age')
	profCat = request.get_json().get('Profession_Category')
	language = request.get_json().get('Language_Spoken')
	genderPref = request.get_json().get('Gender_Preference')
	smoking = request.get_json().get('Smoking')
	musicL = request.get_json().get('Music_Lover')
	motionS = request.get_json().get('Motion_Sickness')
	likeQ = request.get_json().get('Like_Quietness')
	
	writeToFile(uid,profession,rating,age,profCat,language,genderPref,smoking,musicL,motionS,likeQ)
	return 'Added to the file'

def writeToFile(uid,profession,rating,age,profCat,language,genderPref,smoking,musicL,motionS,likeQ):
	fields=[uid,profession,rating,age,profCat,language,genderPref,smoking,musicL,motionS,likeQ]
	with open(r'datausers.csv', 'a', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(fields)
	
@app.route('/ridematching/kmeans/<UserID>', methods=['GET'])
def getSuitableDriverList(UserID):
	global uid
	uid = UserID
	#UserID = request.get_json().get('UID') #Final list of drivers
	#return uid
	print(uid)
	
	return driverList(uid)

	
@app.route('/update/<UserID>/<Rating>', methods=['GET'])
def updateDataSet(UserID, Rating):
	global uid
	global rating
	uid = UserID
	rating = Rating
	print(uid)
	print(rating)
	df.loc[df['UID'] == uid, 'Rating'] = rating
	
	df.to_csv('datausers.csv', index=False);
	#print(df)
		
	return 'Updated'

	
@app.route('/available', methods=['POST'])
def writeAvailableDriversToFile(): #  Filtering available drivers(2)
	#q = pd.read_csv('availableDrivers.csv')
	dIDList= list()
	#df = pd.read_csv('test.csv')
	print(len(request.get_json().get('uid')))
	for x in range(0, len(request.get_json().get('uid'))): 
		dIDList.append(request.get_json().get('uid')[x].get('UID'))
		#print(dIDList)
		#Smoking	Music_Lover	Motion_Sickness	Like_Quietness

	df.loc[(df['UID'] == 'UID')& (df['Profession'] == 'Profession')& (df['Rating'] == 'Rating')& (df['Age'] == 'Age')& (df['Profession_Category'] == 'Profession_Category')
	& (df['Language_Spoken'] == 'Language_Spoken')& (df['Gender_Preference'] == 'Gender_Preference')].to_csv('availableDrivers.csv',index=False,  header=True);	
	for y in range(0, len(dIDList)):	
		
		df.loc[(df['UID'] == dIDList[y])].to_csv('availableDrivers.csv',index=False, mode='a', header=False);	

	addedList = list()
	addedList.append("Added")
	return jsonify(FILE = addedList)
	
#Defining rules for the filteration
def rules(smokingFlag, musicFlag, motionFlag, quietnessFlag, genderFlag):
	q = pd.read_csv('availableDrivers.csv')
	q.loc[(df['Smoking'] == smokingFlag) & (q['Music_Lover'] == musicFlag) & (q['Motion_Sickness'] == motionFlag) & (q['Gender_Preference'] == genderFlag) 
	& (q['Like_Quietness'] == quietnessFlag)].to_csv('newUsers.csv', index=False);
	
	
def driverList(UserID):
	print(UserID)
	executeRules(UserID)
	#UID = 650444020925
	dataset = pd.read_csv('newUsers.csv')
	
	X = dataset.iloc[:,[3,4]].values # read columns Age-x axis and Profession-y axis

	# Using the elbow method to find the optimal number of clusters
	from sklearn.cluster import KMeans
	wcss =[]
	for i in range (1,1):
		kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter =200, n_init = 1, random_state = 0)
		kmeans.fit(X)
		wcss.append(kmeans.inertia_) #Within Cluster Sum of Squares

	# Applying KMeans to the dataset with the optimal number of cluster
	kmeans=KMeans(n_clusters = 1, init = 'k-means++', max_iter = 200, n_init = 1, random_state = 0)
	Y_Kmeans = kmeans.fit_predict(X)


	#get clusters and sort them into new file
	dataset["Cluster"] = Y_Kmeans
	dataset.sort_values(by='Cluster',  inplace=True)
	dataset.to_csv('final.csv', index=False)

	dataset = pd.read_csv('final.csv')
	#specify the cluster where the particular passenger belongs to
	print("kkkk"+UID)
	n = dataset[dataset['UID']== UID].iloc[:,11].values[0]

	#ds = X[np.where(kmeans.labels_== n)] #get particular cluster
	#print(ds)
	#print(dataset.loc[dataset['Cluster'] == n])

	#Initialize lists required
	uIDList= list()
	formattedUIDList= list()
	reportedList=list()

	dataListOfSuitableDrivers = dataset.loc[dataset['Cluster'] == n, ['UID']]
	uIDList = dataListOfSuitableDrivers.values.tolist()
    # remove reported drivers from the list(uIDList - entries from db)
	#mycursor.execute("SELECT DUID FROM reported_drivers WHERE PUID="+UserID)

	#myresult = mycursor.fetchall()

	#for x in myresult:
	  #print('['+str(x[0]).replace('\'', '')+']')
	  
	  #w=x[0].replace('\'', '')
	  #n = '['+w+']'
	  #print(w)
	  #print(n)
	  #reportedList.append('['+str(x[0]).replace('\'', '')+']'[0])
	  #uIDList.remove(x[0])
	#print(reportedList)
	
	#dataListOfSuitableDrivers.to_csv('selectedDrivers.csv', index=False)
	#uIDList.append(dataListOfSuitableDrivers.get('UID'))
		
	#database call to get reported list for particular UID
	#filteredList = uIDList - [1,2,3,4,5]
	
	#removing unwanted characters from the list
	for uid in uIDList:
		formattedUIDList.append(uid[0]) 
		#print(uid)

	f = open("availableDrivers.csv", "w+")
	f.close()
	#os.remove("newUsers.csv")
	#os.remove("final.csv")
	#filteredList = [1,2,3,4,5]

	#dataset = pd.DataFrame(filteredList)
	#dataset.to_csv('selectedDrivers.csv')
	#print(formattedUIDList)
	#return the final driver list in JSON
	return jsonify(formattedUIDList)

	
if __name__ == '__main__':
	app.run(debug=True, host="192.168.43.102", port=99)

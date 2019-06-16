import csv   
import json
import pandas as pd
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/x', methods=['POST'])
def getFile():
	uIDList= list()
	df = pd.read_csv('test.csv')
	
	for x in range(0, len(request.get_json().get('uid'))): 
		uIDList.append(request.get_json().get('uid')[x].get('UID'))
	
	for y in range(0, len(uIDList)):	
		print(uIDList)
		df.loc[(df['UID'] == uIDList[y])].to_csv('test12.csv',index=False, mode='a', header=False);	

	return 'ccc'

@app.route('/ridematching/write', methods=['POST'])
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
	with open('test.csv', 'a', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(fields)


if __name__ == '__main__':
	app.run(debug=True, host="192.168.43.102", port=99)
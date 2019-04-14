import numpy as np
import pandas as pd
from flask import Flask, jsonify
import RideMatchingAlgorithm


app = Flask(__name__)

df = pd.read_csv('users.csv')

#get the userID of the passenger(Frontend fetch)
UID = 130079

#get the properties of the specified user and assign it to variables
isSmoking = df[df['UID']== UID].iloc[:,11].values[0]
isMusicLover = df[df['UID']== UID].iloc[:,12].values[0]
isMotionSickness = df[df['UID']== UID].iloc[:,13].values[0]
isLikeQuietness = df[df['UID']== UID].iloc[:,14].values[0]
#isGenderPrefered = df[df['UID']== UID].iloc[:,9].values[0]

@app.route('/rule', methods=['GET'])
def get_tasks():
    return RideMatchingAlgorithm.rules(isSmoking, isMusicLover, isMotionSickness, isLikeQuietness)


if __name__ == '__main__':
  app.run(debug=True)
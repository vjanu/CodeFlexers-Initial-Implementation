import csv
import json
from flask import Flask, jsonify

app = Flask(__name__)

data = []


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():

 with open('final.csv') as f:
    for row in csv.DictReader(f):
        data.append(row)

 json_data = json.dumps(data)
 return json_data

if __name__ == '__main__':
    app.run(debug=True)
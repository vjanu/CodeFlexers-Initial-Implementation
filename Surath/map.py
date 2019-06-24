#!flask/bin/python
from flask import jsonify,Flask
from flask import request


# importing googlemaps module
import googlemaps

app = Flask(__name__)



@app.route('/map/<source>/<destination>', methods=['GET'])
def distance_duration(source,destination) :
    print(source)
    print(destination)
    #content = request.get_json()

    # Take source as input
    #print("Source")
    #source = "SLIIT"

    # Take destination as input
    #print("Destination")
    #dest = "Maharagama"

    # Requires API key
    gmaps = googlemaps.Client(key='AIzaSyA61V4HM6lh6imhP6x0nG7W9vOAp8V318E')

    # Requires cities name
    my_distance = gmaps.distance_matrix(source, destination)['rows'][0]['elements'][0]['distance']['text']
    my_duration = gmaps.distance_matrix(source, destination)['rows'][0]['elements'][0]['duration']['text']
    #print(content['source'])
    #print(content['dest'])
    # Printing the result
	
	
    print(my_distance)
    print(my_duration)
    return jsonify(duration=my_duration,distance=my_distance)


app.run(debug=True,host="0.0.0.0",port=95)
#if __name__ == '__main__':
#    app.run(debug=True)
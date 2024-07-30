import googlemaps
from googlemaps import Client
import json
import requests

API_KEY = "AIzaSyA3kdNaHOIsrsRonGCFBfrEPOtn6AezLb0"

client = Client(key=API_KEY)


#address: String text 
#return placePrediction with place info like placeid, text...
def getPlaceGeom(address):        
    location = client.gecode(address)
    if location is not None:
        geometry = location[0]['geometry']['location']
        formatted_address = location[0]['formatted_address']

        return geometry
    else:
        return False
        
#searchNearPlaces

def getNearPlaces(geometry, keyword, category):
    json_data = {
    "input": keyword,
    "includedPrimaryTypes": [category],
    "locationRestriction": {
        "circle": {
        "center": {
            "latitude": geometry["lat"],
            "longitude": geometry["lng"]},
        "radius": 3000.0               #반경은 0.0 이상 50000.0 이하
        }
    }
    
    }

    response = requests.post(
    "https://places.googleapis.com/v1/places:autocomplete",
    headers={
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "suggestions.placePrediction" #set return field
            },
    json=json_data)

    if response.status_code == 200:
        return response.json()['suggestions']
    else:
        return response.status_code


#getPlaceDetails
def getPlaceDetails(place_id):
    response = requests.get(
                f"https://places.googleapis.com/v1/places/{place_id}",
                headers={
                    "Content-Type": "application/json",
                    "X-Goog-Api-Key": API_KEY,
                    "X-Goog-FieldMask": "*"
                    }
                )
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code

#getPlaceRoutes
def getPlaceRoutes(origin_text, destination_text):
    # Define the endpoint URL
    url = 'https://routes.googleapis.com/directions/v2:computeRoutes'

    # Set up the headers
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': API_KEY,
        'X-Goog-FieldMask': 'routes.legs.steps.transitDetails',
    #    'X-Goog-FieldMask': 'routes.duration,routes.distanceMeters'
    }

    # Create the payload
    payload = {
        "origin": {
        "address": origin_text
    },
    "destination": {
        "address": destination_text
    },
    "travelMode": "TRANSIT",
    "computeAlternativeRoutes": True,
    "transitPreferences": {
        'routingPreference': "LESS_WALKING",
        'allowedTravelModes': ["TRAIN"]
    },
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Print the response
    print(response.status_code)
    print(response.json()['routes'])



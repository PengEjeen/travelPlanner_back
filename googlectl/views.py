from rest_framework.decorators import api_view
from rest_framework.response import Response
import googlemapsctl

# Create your views here.

#search near place
#post feature 
@api_view(['GET'])
def searchNearPlace(request, address, keyword=None, category=None):
    #get geom
    geometry = googlemapsctl.getPlaceGeom(address)

    #get near place
    if geometry:
        place_recommend = googlemapsctl.getNearPlaces(geometry, keyword, category)
        return Response(place_recommend, status=200)
    else:
        return Response("Invalid address",status=400) 

    
#get place detail info
@api_view(['GET'])
def getPlaceDetails(place_id):
    place_details = googlemapsctl.getPlaceDetails()
    if place_details:
         return Response(place_details, status=200)
    else:
        return Response("Invalid place_id", status=400)

#get route origin to destination
#origin and destination text are String
@api_view(['GET'])
def getPlaceRoutes(origin_text, destination_text):
    routes = googlemapsctl.getPlaceRoutes(origin_text, destination_text)
    if routes:
        return Response(routes, status=200)
    else:
        return Response("Invalid address", status=400)
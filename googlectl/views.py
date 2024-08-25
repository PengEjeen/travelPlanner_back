from rest_framework.decorators import api_view
from rest_framework.response import Response
from googlectl.googlemapsctl import *

# Create your views here.

#search near place
#post feature 
@api_view(['GET'])
def searchNearPlace(request):
    #get geom
    address = request.GET.get('address')
    keyword = request.GET.get('keyword')
    category = request.GET.get('category')
    geometry = getPlaceGeom(address)
    
    #get near place
    if geometry:
        place_recommend =getNearPlaces(geometry, keyword, category)
        return Response(place_recommend, status=200)
    else:
        return Response("Invalid address",status=400) 

    
#get place detail info
@api_view(['GET'])
def getPlaceDetail(request):
    place_id = request.GET.get('place_id')
    place_details = getPlaceDetails(place_id)
    if place_details:
         return Response(place_details, status=200)
    else:
        return Response("Invalid place_id", status=400)

#get route origin to destination
#origin and destination text are String
@api_view(['GET'])
def getPlaceRoute(request):
    origin_text = request.GET.get('origin_text')
    destination_text = request.GET.get('destination_text')

    routes = getPlaceRoutes(origin_text, destination_text)
    if routes:
        return Response(routes, status=200)
    else:
        return Response("Invalid address", status=400)

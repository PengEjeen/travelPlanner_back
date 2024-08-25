from django.urls import path
from . import views

urlpatterns = [
    path('searchNearPlace/',views.searchNearPlace, name='searchNearPlace'),
    path('placeDetails/',views.getPlaceDetail, name='getPlaceDetails'),
    path('placeRoutes/',views.getPlaceRoute, name='getPlaceRoutes'),
    path('placePhotos/',views.getPlacePhoto, name='getPlacePhotos'),
]

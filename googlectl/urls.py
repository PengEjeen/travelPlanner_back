from django.urls import path
from . import views

urlpatterns = [
    path('searchNearPlace',views.searchNearPlace, name='searchNearPlace'),
    path('placeDetails/',views.getPlaceDetails, name='getPlaceDetails'),
    path('placeRoutes/',views.getPlaceRoutes, name='getPlaceRoutes')
]
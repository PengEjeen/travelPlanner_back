from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/',include('common.urls')),
    path('planners/', include('planner_detail.urls')),
    path('polls/', include('polls.urls')),
    path('googlemaps/', include('googlectl.urls'))
]

"""
URL configuration for travelplanner_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from planner_detail import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/',include('common.urls')),
    path('planners/', views.get_AllPlanner, name='get_AllPlanner'),
    path('planners/planner_create/', views.create_Planner, name='create_planner'),
    path('planners/<str:planner_id>/', views.get_Planner, name='get_planner'),
    path('planners/<str:planner_id>/update/', views.update_Planner, name='update_planner'),
    path('planners/<str:planner_id>/delete/', views.delete_Planner, name='delete_planner'),


]

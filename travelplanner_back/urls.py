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

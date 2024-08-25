from django.urls import path
from . import views

urlpatterns = [
    path('getPlanner/', views.get_AllPlanner, name='get_AllPlanner'),
    path('planner_create/', views.create_Planner, name='create_planner'),
    path('<str:planner_id>/', views.get_Planner, name='get_planner'),
    path('<str:planner_id>/update/', views.update_Planner, name='update_planner'),
    path('<str:planner_id>/delete/', views.delete_Planner, name='delete_planner')
]
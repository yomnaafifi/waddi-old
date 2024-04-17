from django.urls import path
from . import views


urlpatterns = [
    path('details/<int:pk>/', views.DriverDetailsView, name = 'driver_details'),
    path('online/', views.OnlineDriversView, name = 'online_drivers'),
    path('tasks/', views.TasksView, name = 'tasks_view'),
]


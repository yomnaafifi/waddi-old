from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:pk>/', views.CustomerDetailsView, name = 'customer_details'),
]

 
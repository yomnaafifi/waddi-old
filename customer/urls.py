from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.CustomerSignupView, name = 'customer_signup'),
    path('details/<int:pk>/', views.CustomerDetailsView, name = 'customer_details'),
]

 
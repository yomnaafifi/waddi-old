from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('<int:pk>/', views.show_customer),
]

urlpatterns = format_suffix_patterns(urlpatterns)
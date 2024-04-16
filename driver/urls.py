from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('<int:pk>/', views.Driver.as_view()),
    path('tasks/', views.Tasks.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
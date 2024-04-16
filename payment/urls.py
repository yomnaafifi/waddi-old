from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('<int:pk>/', views.saved_cards.as_view()),
    path('withdrawals/<int:pk>/', views.withdrawal_history.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
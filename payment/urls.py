from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.CardView, name = 'cards_view'),
    path('withdrawals/<int:pk>/', views.WithdrawalHistory, name = 'withdrawal_history'),
]


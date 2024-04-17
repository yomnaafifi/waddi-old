from rest_framework import serializers
from payment.models import Card, Transactions

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card 
        fields = '__all__'

class WithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions 
        fields = ['timestamp', 'amount'] 
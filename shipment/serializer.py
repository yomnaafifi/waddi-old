from rest_framework import serializers
from shipment.models import Orders

class ShipmentHistorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['pickup_time','delivery_time', 'pickup_address','dropoff_time','order_state',]


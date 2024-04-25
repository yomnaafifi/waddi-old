from rest_framework import generics
from shipment.models import Orders
from shipment.serializer import ShipmentHistorySerializer


class ShipmentHistoryView (generics.ListAPIView):
    queryset = Orders.objects.filter(status = 'Delivered') #its supposed to get all delivered shipments of this user
    serializer_class = ShipmentHistorySerializer
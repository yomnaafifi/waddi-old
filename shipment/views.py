from rest_framework import generics
from shipment.models import Orders
from shipment.serializer import ShipmentHistorySerializer


class ShipmentHistoryView (generics.ListAPIView):
    serializer_class = ShipmentHistorySerializer

    def get(self, request, pk):
        queryset = Orders.objects.filter(status = 'Delivered', customer_id = pk)
        return queryset

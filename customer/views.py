from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from customer.models import Customer
from customer.serilaizer import CustomerSerializer

@api_view(['GET'])
def show_customer(request, pk, format=None):
    if request.method == 'GET':
        customer_data = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer_data)
        return Response(serializer.data)
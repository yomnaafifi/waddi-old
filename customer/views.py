from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from customer.models import Customer
from customer.serilaizer import CustomerSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

@api_view(['GET', 'PATCH'])
@extend_schema(
    responses=CustomerSerializer
)
def CustomerDetailsView(request, pk):
    try: 
        customer_data = Customer.objects.get(pk=pk)
    except customer_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CustomerSerializer(customer_data)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        pass
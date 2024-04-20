from rest_framework import status
from payment.models import Card, Transactions
from payment.serializer import CardSerializer, WithdrawalSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

@api_view(['GET'])
@extend_schema(
    responses=CardSerializer
)
def CardView(request, pk):
    if request.method == 'GET':
        cards = Card.objects.get(pk=pk)
        serializer= CardSerializer(cards, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
@extend_schema(
    responses=WithdrawalSerializer
)
def WithdrawalHistory(request, pk):
    if request.method == 'GET':
        withdrawals = Transactions.objects.all(pk=pk)
        serializer= WithdrawalSerializer(withdrawals, many=True)
        return Response(serializer.data)




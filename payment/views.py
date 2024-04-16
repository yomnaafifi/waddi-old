from payment.models import Card, Transactions
from payment.serializer import CardSerializer, WithdrawalSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def CardView(request, pk):
    if request.method == 'GET':
        cards = Card.objects.get(pk=pk)
        serializer= CardSerializer(cards, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def WithdrawalHistory(request, pk):
    if request.method == 'GET':
        withdrawals = Transactions.objects.all(pk=pk)
        serializer= WithdrawalSerializer(withdrawals, many=True)
        return Response(serializer.data)




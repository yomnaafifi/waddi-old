from payment.models import Card, Transactions
from payment.serializer import CardSerializer, WithdrawalSerializer
from rest_framework import mixins 
from rest_framework import generics

class saved_cards(mixins.ListModelMixin,
                  generics.GenericAPIView):
    all_cards = Card.objects.all()
    serializer_class = CardSerializer

    def get (self, request, pk): #id of the user?
        return self.list(request, pk)
    
    #adding a new card

#showing the withdrawal history of the driver's wallet
class withdrawal_history(mixins.ListModelMixin,
                         generics.GenericAPIView):
    withdrawals = Transactions.objects.all()
    serializer_class = WithdrawalSerializer

    def list_withdrawals(self, request, pk): #driver id
        return self.list(request, pk)

#this logic is soooo uncomplete&flawed

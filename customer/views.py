from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from customer.models import Customer
from customer.serilaizer import CustomerSerializer 
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from auth.forms import CustomerSignupForm

class CustomerSignupView(generics.CreateAPIView):
    serializer_class = CustomerSerializer
    def post(self, request, *args, **kwargs):
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            user_data = form.save() #the saving logic is defined in the form itself 
            serializer = self.get_serializer(user_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED) #should redirect to home? 
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST) 



@api_view(['GET', 'PATCH'])
@extend_schema(
    responses= CustomerSerializer
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
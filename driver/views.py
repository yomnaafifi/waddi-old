from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from driver.models import Driver, Tasks
from driver.serializer import DriverSerilaizer, TasksSerilaizer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from auth.forms import DriverSignupForm

class DriverSignupView(generics.CreateAPIView):
    serializer_class = DriverSerilaizer
    def post(self, request, *args, **kwargs):
        form = DriverSignupForm(request.POST)
        if form.is_valid():
            user_data = form.save()
            serializer = self.get_serializer(user_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED) #should redirect to home 
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PATCH'])
@extend_schema(
    responses=DriverSerilaizer
)
def DriverDetailsView (request, pk):
    try: 
        driver_data = Driver.objects.get(pk=pk)
    except driver_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DriverSerilaizer(driver_data)
        return Response(serializer.data)
    elif request.method == 'PATCH':
         pass
    

@api_view(['GET'])
@extend_schema(
    responses=DriverSerilaizer
)
def OnlineDriversView (request):
    if request.method == 'GET':        
        online_drivers = Driver.objects.filter(online=True)
        serializer = DriverSerilaizer(online_drivers)
        return Response(serializer.data) 

@api_view(['GET'])
@extend_schema(
    responses={201: TasksSerilaizer}
)
def TasksView (request): #this is supposed to be done with websocket
    if request.method == 'GET':
        tasks = Tasks.objects.all()
        serializer = TasksSerilaizer(tasks, many=True)
        return Response(serializer.data)


        


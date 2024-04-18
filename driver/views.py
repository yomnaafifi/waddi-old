from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from driver.models import Driver, Tasks
from driver.serializer import DriverSerilaizer, TasksSerilaizer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

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


        


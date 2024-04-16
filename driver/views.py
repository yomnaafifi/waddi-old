from driver.models import Driver, Tasks
from driver.serializer import DriverSerilaizer, TasksSerilaizer
from rest_framework.views import APIView
from rest_framework.response import Response


class Driver(APIView):
    
    def get(self, request, pk,  format=None):
        driver_data = Driver.objects.get(pk=pk)
        serializer = DriverSerilaizer(driver_data)
        return Response(serializer.data)
    

    def get_online_drivers(self, request):
        online_drivers = Driver.objects.filter(online=True)
        serializer = DriverSerilaizer(online_drivers)
        return Response(serializer.data)    

class Tasks(APIView):
    def get(self, request, format=None): #how do i get the specific tasks for each driver
        tasks = Tasks.objects.all()
        serializer = TasksSerilaizer(tasks, many=True)
        return Response(serializer.data)


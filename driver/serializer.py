from rest_framework import serializers
from driver.models import Driver, Tasks

class DriverSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Driver 
        fields = ['firstname', 'lastname', 'email', 'birthdate', 'phone_number', 'image']


class TasksSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['__all__']
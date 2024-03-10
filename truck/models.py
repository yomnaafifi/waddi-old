from django.db import models
from ..driver import Driver


# Create your models here.
class Truck(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    license = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=255)
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, related_name='truck')


    def __str__(self):
        return f"{self.type} - {self.model} ({self.registration_number})"
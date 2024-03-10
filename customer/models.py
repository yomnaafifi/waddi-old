from django.db import models
from ..driver import Driver
from ..shipment import Shipment
from ..admin import Admin
from ..payment import Payment


# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, related_name='customers')
    shipment = models.OneToOneField(Shipment, on_delete=models.SET_NULL, null=True, related_name='customer')
    admin = models.OneToOneField(Admin, on_delete=models.SET_NULL, null=True, related_name='customer')
    payment = models.OneToOneField(Payment, on_delete=models.SET_NULL, null=True, related_name='customer')

    def __str__(self):
        return self.name
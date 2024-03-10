from django.db import models
from ..customer import Customer
from ..truck import Truck
from ..shipment import Shipment
from ..admin import Admin
from ..payment import Payment

# Create your models here.
class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='driver_images/', null=True, blank=True)
    license = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='drivers')
    truck = models.OneToOneField(Truck, on_delete=models.SET_NULL, null=True, related_name='driver')
    admin = models.OneToOneField(Admin, on_delete=models.SET_NULL, null=True, related_name='driver')
    payment = models.OneToOneField(Payment, on_delete=models.SET_NULL, null=True, related_name='driver')
    shipment = models.ForeignKey(Shipment, on_delete=models.SET_NULL, null=True, related_name='drivers')

    def __str__(self):
        return self.name
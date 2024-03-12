from django.db import models
from customer.models import Customer

# Create your models here.
class Shipment(models.Model):
    location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete = models.CASCADE)

    def __str__(self):
        return f"Shipment {self.id}: {self.location} to {self.destination}"
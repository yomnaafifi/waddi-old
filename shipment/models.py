from django.db import models
from customer.models import Customer

# Create your models here.
class Shipment(models.Model):
    location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete = models.CASCADE)
    order_notes = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add = True)
    pickup_time = models.DateTimeField()
    pricing = models.BigIntegerField()
    packing = models.BooleanField()
    labor = models.BooleanField()
    states = {
        
    }
    order_state = models.CharField(max_lenght=1, choices = states)


    def __str__(self):
        return f"Shipment {self.id}: {self.location} to {self.destination}"
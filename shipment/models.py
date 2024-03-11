from django.db import models


# Create your models here.
class Shipment(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    driver = models.OneToOneField("driver.Driver", on_delete=models.SET_NULL, null=True, related_name='shipments')
    customer = models.OneToOneField("customer.Customer", on_delete=models.SET_NULL, null=True, related_name='shipments')

    def __str__(self):
        return f"Shipment {self.id}: {self.location} to {self.destination}"
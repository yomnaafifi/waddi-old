from django.db import models

# Create your models here.
class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='driver_images/', null=True, blank=True)
    license = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    customer = models.ForeignKey("customer.Customer", on_delete=models.SET_NULL, null=True, related_name='drivers')
    truck = models.OneToOneField("truck.Truck", on_delete=models.SET_NULL, null=True, related_name='drivers')
    # admin = models.OneToOneField("admin.Admin", on_delete=models.SET_NULL, null=True, related_name='drivers')
    payment = models.OneToOneField("payment.Payment", on_delete=models.SET_NULL, null=True, related_name='drivers')
    shipment = models.ForeignKey("shipment.Shipment", on_delete=models.SET_NULL, null=True, related_name='drivers')

    def __str__(self):
        return self.name
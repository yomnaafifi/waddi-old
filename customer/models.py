from django.db import models


# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    driver = models.ForeignKey("driver.Driver", on_delete=models.SET_NULL, null=True, related_name='customers')
    shipment = models.OneToOneField("shipment.Shipment", on_delete=models.SET_NULL, null=True, related_name='customers')
    # admin = models.OneToOneField("admin.Admin", on_delete=models.SET_NULL, null=True, related_name='customers')
    payment = models.OneToOneField("payment.Payment", on_delete=models.SET_NULL, null=True, related_name='customers')

    def __str__(self):
        return self.name
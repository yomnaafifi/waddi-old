from django.db import models
from ..driver import Driver
from ..customer import Customer


# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    drivers = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, related_name='admin')
    customers = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='admin')

    def __str__(self):
        return self.name
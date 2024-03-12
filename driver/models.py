from django.db import models
from customer.models import Customer
from admin_user.models import Admin 
# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='driver_images/', null=True, blank=True)
    license = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    customer = models.ManyToManyField(Customer)
    admin = models.ForeignKey(Admin, on_delete = models.CASCADE)


    def __str__(self):
        return self.name
    
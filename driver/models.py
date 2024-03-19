from django.db import models
from customer.models import Customer #, Address
from admin_user.models import Admin
# Create your models here.
class Driver(models.Model):
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255,default='lastname', null=False)
    image = models.CharField(max_length=255, null=True, blank=True)
    license = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique=True, null=False)
    phone_number = models.CharField(max_length=15, null=False)
    customer = models.ManyToManyField(Customer)
    admin = models.ForeignKey(Admin, on_delete = models.CASCADE, null=False)
    


    def __str__(self):
        return self.name

class Tasks(models.Model):
    pickup_from = models.CharField(max_length= 100, null=False)
    delivery_to = models.CharField(max_length= 100, null=False)
    destination = models.CharField(max_length= 100, null=False)

    class Meta: 
        db_table ='tasks'
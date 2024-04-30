from django.db import models
from customer.models import Customer 
from admin_user.models import Admin
# Create your models here.
class Driver(models.Model):
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255,default='lastname', null=False)
    image = models.CharField(max_length=255, null=True, blank=True)
    license = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique=True, null=False)
    phone_number = models.CharField(max_length=50, null=False)
    customer = models.ManyToManyField(Customer, null=True)
    admin = models.ForeignKey(Admin, on_delete = models.CASCADE, null=False)
    online = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Tasks(models.Model):
    destination = models.CharField(max_length= 100, null=False)
    states =[
        
    ] 
    state = models.CharField(max_length = 50, choices= states, default = 'state')
    class Meta: 
        db_table ='tasks'


class Trips(models.Model): #how to link it with orders
    pass
from django.db import models
from customer.models import Customer 
from utils.models import Address
from admin_user.models import Admin

from auth.models import CustomUser
class Driver(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    license = models.CharField(max_length=255, null=False)
    customer = models.ManyToManyField(Customer, null=True)
    admin = models.ForeignKey(Admin, on_delete = models.CASCADE, null=False)
    is_online = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Tasks(Address):
    destination = models.CharField(max_length= 100, null=False)
    states =[
        
    ] 
    state = models.CharField(max_length = 50, choices= states, default = 'state')
    class Meta: 
        db_table ='tasks'


class Trips(Address): #how to link it with orders
    pass
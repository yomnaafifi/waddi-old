from django.db import models
from customer.models import Customer
from utils.models import Address


# Create your models here.
class Orders(Address):
    location = models.CharField(max_length=255, null=False)
    destination = models.CharField(max_length=255, null=False)
    customer = models.OneToOneField(Customer, on_delete = models.CASCADE, null=False)
    order_notes = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add = True, null=False)
    types = {
        ('plastic&rubber', 'Plastic and Rubber'),
        ('appliances', 'Appliances'),
        ('glass', 'Glass'),
        ('wood', 'Wood'),
        ('food', 'Food'),
        ('furniture', 'Furinture'),
        ('multiple commodities', 'Multiple Commodities '),
    
    }
    type = models.CharField(max_length=200, choices = types, null=False)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=False)  
    pickup_time = models.DateTimeField(null=False )
    pricing = models.BigIntegerField(null=False)
    packing = models.BooleanField()
    labor = models.BooleanField()
    states = {
        
    }
    order_state = models.CharField(max_length=200, choices = states, null=False)


    class Meta:
        db_table = 'orders'
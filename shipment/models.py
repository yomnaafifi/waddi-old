from django.db import models
from customer.models import Customer
from utils.models import Address

class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
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
    pickup_date = models.DateTimeField(null=False )
    delivery_date = models.DateTimeField(null=False )
    pricing = models.BigIntegerField(null=False)
    need_packing = models.BooleanField()
    need_labor = models.BooleanField()
    states = {
        ('pending', 'Pending'),
        ('out for delivery', 'Out for delivery'),
        ('delivered', 'Delivered'),

    }
    order_state = models.CharField(max_length=200, choices = states, null=False)
    pickup_address = models.ForeignKey(Address,  on_delete=models.CASCADE)
    delivery_address = models.ForeignKey(Address, on_delete=models.CASCADE)

    @property
    def destination(self):
        pass #should calculate the destination
    class Meta:
        db_table = 'orders'
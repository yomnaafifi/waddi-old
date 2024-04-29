from django.db import models
from driver.models import Driver
from customer.models import Customer


# Create your models here.
class Transactions(models.Model):
    type = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places = 2)
    driver = models.OneToOneField(Driver, models.CASCADE)
    customer = models.OneToOneField(Customer, on_delete = models.CASCADE)
    class Meta:
        db_table = 'transactions'


class Card(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, primary_key=True)
    cardholder_name = models.CharField(max_length=200)
    card_number = models.CharField(max_length=50)  
    expiration_date = models.DateField()
    cvv_code = models.CharField(max_length=50)  
    billing_address = models.CharField(max_length=255)
    card_type = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    is_default = models.BooleanField()

    class Meta:
        db_table = 'card'
        

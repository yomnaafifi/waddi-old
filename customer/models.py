from django.db import models
from admin_user.models import Admin
from utils.models import Address
from datetime import date

from auth.models import CustomUser



class Customer(Address):
    #address = models.
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    ##admin = models.ForeignKey(Admin, on_delete = models.CASCADE, null=False)
    payment_methods = models.Choices(
        (1, 'Cash on Delivery'),
        (2, 'Mobile Banking'),
        (3, 'Credit or Debit Card'), #when chosen takes me to the cards form
          
    )
    preferred_method = models.CharField(choices=payment_methods)

    def __str__(self):
            return self.name




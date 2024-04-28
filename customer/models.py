from django.db import models
from admin_user.models import Admin
from utils.models import Address
from datetime import date

from auth.models import CustomUser



class Customer(Address):
    #address = models.
    customer = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    admin = models.ForeignKey(Admin, on_delete = models.CASCADE, null=False)

    def __str__(self):
            return self.name




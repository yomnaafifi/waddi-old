from django.db import models
from admin_user.models import Admin
from datetime import date
from utils.models import Address




class Customer(models.Model):
    firstname = models.CharField(max_length=255, default='firstname', null=False)
    lastname = models.CharField(max_length=200, null=False)
    birthdate = models.DateField(default=date.today, null=False)
    image = models.CharField(max_length=255, null=True, blank=True)
    #address = models.
    email = models.EmailField(null=False)
    phone_no = models.CharField(max_length = 50, null=False)
    admin = models.ForeignKey(Admin, on_delete = models.CASCADE, null=False)


    address = models.ForeignKey(Address, on_delte = models.CASCADE)

    def __str__(self):
            return self.name




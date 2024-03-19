from django.db import models
from admin_user.models import Admin
from datetime import date
class Customer(models.Model):
    firstname = models.CharField(max_length=255, default='firstname', null=False)
    lastname = models.CharField(max_length=100, null=False)
    birthday = models.DateField(default=date.today, null=False)
    #address = models.
    email = models.EmailField(null=False)
    phone_no = models.CharField(max_length = 20, null=False)
    admin = models.ForeignKey(Admin, on_delete = models.CASCADE, null=False)

    def __str__(self):
            return self.name


# class Address(models.Model):
#     street_address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     state_province = models.CharField(max_length=100)
#     postal_code = models.CharField(max_length=20)
#     country = models.CharField(max_length=100)

#     class Meta:
#          db_table = 'address'
#          abstract = True

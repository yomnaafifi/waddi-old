from django.db import models
from admin_user.models import Admin
from datetime import date


class Address(models.Model):
    street_address = models.CharField(max_length=255, default = 'street')
    city = models.CharField(max_length=200, default = 'city')
    state_province = models.CharField(max_length=200, default = 'state')
    postal_code = models.CharField(max_length=50, default = 'postal_code')
    country = models.CharField(max_length=200, default = 'country')

    class Meta:
         abstract = True

class Customer(Address):
    firstname = models.CharField(max_length=255, default='firstname', null=False)
    lastname = models.CharField(max_length=200, null=False)
    birthday = models.DateField(default=date.today, null=False)
    image = models.CharField(max_length=255, null=True, blank=True)
    #address = models.
    email = models.EmailField(null=False)
    phone_no = models.CharField(max_length = 50, null=False)
    admin = models.ForeignKey(Admin, on_delete = models.CASCADE, null=False)

    def __str__(self):
            return self.name




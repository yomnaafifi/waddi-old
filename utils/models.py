from django.db import models

class Address(models.Model):
    street_address = models.CharField(max_length=255, default = 'street')
    city = models.CharField(max_length=200, default = 'city')
    state_province = models.CharField(max_length=200, default = 'state')
    postal_code = models.CharField(max_length=50, default = 'postal_code')
    country = models.CharField(max_length=200, default = 'country')

    class Meta:
         abstract = True
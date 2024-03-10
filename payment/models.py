from django.db import models
from ..driver import Driver
from ..customer import Customer


# Create your models here.
class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    date = models.DateField()
    customer = models.OneToOneField(Customer, on_delete=models.SET_NULL, null=True, related_name='payment')
    driver = models.OneToOneField(Driver, on_delete=models.SET_NULL, null=True, related_name='payment')

    def __str__(self):
        return f"{self.type} - {self.date}"
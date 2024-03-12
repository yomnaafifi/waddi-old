from django.db import models
from driver.models import Driver
from customer.models import Customer


# Create your models here.
class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    date = models.DateField()
    driver = models.OneToOneField(Driver, models.CASCADE)
    customer = models.OneToOneField(Customer, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.type} - {self.date}"
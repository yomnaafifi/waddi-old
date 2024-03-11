from django.db import models


# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    driver = models.ForeignKey("driver.Driver", on_delete=models.SET_NULL, null=True, related_name='admins')
    customer = models.ForeignKey("customer.Customer", on_delete=models.SET_NULL, null=True, related_name='admins')

    def __str__(self):
        return self.name
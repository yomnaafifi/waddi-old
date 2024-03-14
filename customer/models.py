from django.db import models

from admin_user.models import Admin
class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length = 20)
    admin = models.ForeignKey(Admin, on_delete = models.CASCADE)

    def __str__(self):
            return self.name

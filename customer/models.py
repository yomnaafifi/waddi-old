from django.db import models
from admin_user.models import Admin
class Customer(models.Model):
    name = models.CharField(max = 100)
    email = models.EmailField()
    phone_no = models.CharField(max = 20)
    admin = models.ForeignKey(Admin, on_delete = models.CASCADE)

    def __str__(self):
            return self.name

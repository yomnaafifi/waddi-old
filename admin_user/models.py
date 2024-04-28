from django.db import models
from auth.models import CustomUser



# Create your models here.
class Admin(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)


    def __str__(self):
        return self.name
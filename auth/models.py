from django.contrib.auth.models import AbstractBaseUser
from auth.managers import  CustomUserManager
from django.db import models


class CustomUser(AbstractBaseUser):
    #where do i save passwords?
    email = models.EmailField(unique = True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    image = models.ImageField(upload_to=None)
    phone_no = models.CharField(max_length = 100, null=False)

    is_customer = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'birthdate', 'phone_no']

    objects = CustomUserManager()

    class Meta:
        db_table = 'user'

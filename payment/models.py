from django.db import models



# Create your models here.
class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    date = models.DateField()
    customer = models.OneToOneField("customer.Customer", on_delete=models.SET_NULL, null=True, related_name='payments')
    driver = models.OneToOneField("driver.Driver", on_delete=models.SET_NULL, null=True, related_name='payments')

    def __str__(self):
        return f"{self.type} - {self.date}"
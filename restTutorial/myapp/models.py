from django.db import models

# Create your models here.
class CarList(models.Model):
    name = models.CharField(max_length=50)
    desc=models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
    license_no=models.CharField(max_length=100, blank=True,null=True)
    def __str__(self):
        return self.name
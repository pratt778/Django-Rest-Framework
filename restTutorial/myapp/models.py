from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class ShowroomList(models.Model):
     name = models.CharField(max_length=50)
     desc = models.CharField(max_length=200)
     website = models.URLField(max_length=100)
     location = models.CharField(max_length=100)

     def __str__(self):
          return self.name

def alphanum(value):
        if not str(value).isalnum():
            raise ValidationError("License num should be alphanumeric")
        return value
class CarList(models.Model):
    name = models.CharField(max_length=50)
    desc=models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
    license_no=models.CharField(max_length=100, blank=True,null=True, validators=[alphanum])
    showroom=models.ForeignKey(ShowroomList,on_delete=models.CASCADE,related_name="showroom",null=True)
    def __str__(self):
        return self.name

class Rating(models.Model):
     rating = models.IntegerField()
     comment = models.CharField(max_length=200)
     car = models.ForeignKey(CarList,on_delete=models.CASCADE,related_name='ratings')
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
          return "The rating for "+self.car.name+" is "+str(self.rating)+" stars"

from django.db import models

# Create your models here.
class Booth(models.Model):
    name = models.CharField(max_length=32,null=False,blank=False)
    location = models.CharField(max_length=64,null=False,blank=False)
    owner_name= models.CharField(max_length=32,null=False,blank=False)

    def __str__(self):
        return self.name
    
class IceCream(Booth):
    cream_type = models.CharField(max_length=32,null=False,blank=False)
    price = models.FloatField(null=False,blank=False)
    size = models.CharField(max_length=16,null=False,blank=False)

    def __str__(self):
        return self.cream_type
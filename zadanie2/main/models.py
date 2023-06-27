from django.db import models

# Create your models here.
class Parent(models.Model):
    fname = models.CharField(max_length=32)
    lname = models.CharField(max_length=32)
    age = models.IntegerField(null=False,blank=False)
    child_counter = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.fname
    
class Child(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(null=False,blank=False)
    fk_parent = models.ForeignKey(Parent,on_delete=models.CASCADE,related_name='fk_parent')

    def __str__(self):
        return self.name
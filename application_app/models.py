from django.db import models

class Details(models.Model):
    name= models.CharField(max_length=200)
    digital=models.BooleanField(default=False,null=True,blank=True)
    image= models.ImageField(null=True,blank=True)
    price= models.IntegerField()
    more= models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name 

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    thumb= models.ImageField(default='default.png',blank=True)
    manufacturer = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
    #add in manufacturer later



    def __str__(self):
        return self.name   
    
    def snippet(self):
         return self.body[:50]+'...'
    
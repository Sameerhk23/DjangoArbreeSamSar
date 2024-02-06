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
    



    def __str__(self):
        return self.name   
    
    def snippet(self):
         return self.body[:50]+'...'
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
 
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'


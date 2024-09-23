from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Client(models.Model):
    phone_number = models.CharField(max_length=11)
    user = models.OneToOneField(User, on_delete=models.CASCADE ,null=True,blank=True)

class Seller(models.Model):
    phone_number = models.CharField(max_length=11)
    user = models.OneToOneField(User, on_delete=models.CASCADE ,null=True,blank=True)
    state =models.CharField(max_length=150)
    
class Product(models.Model):
    title=models.CharField( max_length=150)
    description =models.TextField()
    price=models.IntegerField(default=0)
    owner= models.ForeignKey(Seller,on_delete=models.CASCADE)
    
class Order(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    status = models.CharField(default="in cart",max_length=150)
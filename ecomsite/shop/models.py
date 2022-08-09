
from django.db import models


# Create your models here.
class Products(models.Model):

    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Order(models.Model):

    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    zip = models.CharField(max_length=1000)
    total = models.CharField(max_length=1000)
    

    def __str__(self):
        return self.name
    
   
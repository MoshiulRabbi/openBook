from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=25,null=True)
    detail = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.URLField(max_length=200)

    def __str__(self):
        return self.name

#Building Basic Structure
class Cart(models.Model):
    orderedProduct = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.orderedProduct.name}"

    def totalItemPrice(self):
        return self.quantity * self.orderedProduct.price
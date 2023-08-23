from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    sku = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to="gallery",blank=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
	    return self.sku

class Sold_product(models.Model):
     product = models.ForeignKey(Product,on_delete=models.CASCADE)
     available_quantity = models.IntegerField(default=1)
     price = models.IntegerField(default=0.00)
     total_price = models.DecimalField(max_digits=10, decimal_places=2)
     owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
     created_at = models.DateTimeField(auto_now_add=True, null=True)
     def __str__(self):
	     return self.product
 


     
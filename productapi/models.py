from django.db import models

# Create your models here.

class Product(models.Model):
    product_name=models.CharField(max_length=255)
    price=models.CharField(max_length=255)
    brand=models.CharField(max_length=100)

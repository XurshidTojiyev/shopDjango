from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=128)
    img = models.CharField(max_length=2000)
    price = models.IntegerField(max_length=10)

class Cart(models.Model):
    title = models.CharField(max_length=128)
    img = models.CharField(max_length=2000)
    price = models.IntegerField(max_length=10)
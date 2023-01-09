from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=255, blank=False)
    category = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=False)
    price = models.CharField(max_length=23, blank=False)
    image = models.ImageField(upload_to='products', default='', blank=False)
   
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        



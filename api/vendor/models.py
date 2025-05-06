from django.db import models

# Create your models here.
class Vendor(models.Model):
    VendorID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=20)
    RegistrationDate = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Description = models.TextField(blank=True, null=True)
    SKU = models.CharField(max_length=50, unique=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Image = models.ImageField(upload_to='products/', blank=True, null=True)
    DateAdded = models.DateTimeField(auto_now_add=True)
    LastUpdated = models.DateTimeField(auto_now=True)
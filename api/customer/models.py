from django.db import models

# Create your models here.
class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=20)
    RegistrationDate = models.DateTimeField(auto_now_add=True)
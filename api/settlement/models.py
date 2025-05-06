from django.db import models
from vendor.models import Vendor
# Create your models here.
class Settlement(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_on = models.DateField()
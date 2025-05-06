from django.db import models
from order.models import Order
# Create your models here.
class Return(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    approved = models.BooleanField(default=False)
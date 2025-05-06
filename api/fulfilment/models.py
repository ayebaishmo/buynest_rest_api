from django.db import models

# Create your models here.
class Fulfilment(models.Model):
    order_id = models.IntegerField()
    fulfilled = models.BooleanField(default=False)
    fulfilled_on = models.DateTimeField(null=True, blank=True)
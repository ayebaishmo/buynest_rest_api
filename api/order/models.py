from django.db import models
from customer.models import Customer
from vendor.models import Vendor

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendor_orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.FirstName} {self.customer.LastName} - {self.ordered_on}"
from django.shortcuts import render
from customer.models import Customer
from customer.serializers import CustomerSerializer
from rest_framework import viewsets
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
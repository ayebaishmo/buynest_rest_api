from django.shortcuts import render
from rest_framework import viewsets
from .models import Vendor, Product
from .serializers import VendorSerializer, ProductSerializer

# Create your views here.

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
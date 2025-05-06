from rest_framework import serializers
from .models import Vendor, Product

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_fields = ['VendorID', 'RegistrationDate']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['ProductID', 'DateAdded', 'LastUpdated']

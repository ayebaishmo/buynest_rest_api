from rest_framework import serializers
from .models import Administrator

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = '__all__'
        read_only_fields = ['AdministratorID', 'RegistrationDate']
        
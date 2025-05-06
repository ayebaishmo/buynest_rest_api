from rest_framework import serializers
from courier.models import Courier

class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = "__all__"
        read_only_fields = ['CourierID', 'RegistrationDate']
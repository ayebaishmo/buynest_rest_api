from django.shortcuts import render
from rest_framework import viewsets
from .models import Return
from .serializers import ReturnSerializer

# Create your views here.
class ReturnViewSet(viewsets.ModelViewSet):
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer
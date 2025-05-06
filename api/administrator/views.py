from django.shortcuts import render
from administrator.serializers import AdministratorSerializer
from administrator.models import Administrator
from rest_framework import viewsets

# Create your views here.
class AdministratorViewSet(viewsets.ModelViewSet):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer

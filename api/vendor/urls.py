# vendor/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

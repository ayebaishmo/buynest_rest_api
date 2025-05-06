# returns/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReturnViewSet

router = DefaultRouter()
router.register(r'returns', ReturnViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

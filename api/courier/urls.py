from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courier.views import CourierViewSet


router = DefaultRouter()
router.register(r'couriers', CourierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
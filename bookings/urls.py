# bookings/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet, basename='booking')  # Ensure 'basename' is defined

urlpatterns = [
    path('', include(router.urls)),  # Include the routes from the router
]

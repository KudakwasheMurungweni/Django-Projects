from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripViewSet

router = DefaultRouter()
router.register(r'', TripViewSet, basename='trip')  # Empty string for clean URLs

urlpatterns = [
    path('', include(router.urls)),  # Includes all CRUD endpoints at root
]
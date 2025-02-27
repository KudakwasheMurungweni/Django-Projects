from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripViewSet

router = DefaultRouter()
router.register(r'', TripViewSet, basename='trip')  # Ensure empty route for trips

urlpatterns = [
    path('', include(router.urls)),  # Include the router
]

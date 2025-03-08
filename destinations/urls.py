from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DestinationViewSet

router = DefaultRouter()
# Remove 'destinations' from the router registration
router.register(r'', DestinationViewSet, basename='destination')

urlpatterns = [
    path('', include(router.urls)),
]
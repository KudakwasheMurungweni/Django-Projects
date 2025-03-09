# trips/urls.py
from django.urls import path
from .views import TripViewSet, DashboardView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'trips', TripViewSet)

urlpatterns = [
    path('api/dashboard/', DashboardView.as_view(), name='dashboard'),
] + router.urls
# dashboard/urls.py
from django.urls import path
from .views import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),  # Empty path for root
]
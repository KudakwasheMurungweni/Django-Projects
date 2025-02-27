# users/urls.py - MODIFIED
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileViewSet, UserCreateView

# Create explicit view mappings for profile actions
user_profile = UserViewSet.as_view({'get': 'profile', 'put': 'update_profile'})

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')  # Changed from 'users' to empty string
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('profile/', user_profile, name='user-profile'),  # Removed the 'users/' prefix
]
# project_name/urls.py (main urls.py)
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import UserCreateView  # Import the registration view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    path('api/users/register/', UserCreateView.as_view(), name='user-register'),  # Registration endpoint
    
    # JWT Authentication (Added this section)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Preserve your existing app routes
    path('api/trips/', include('trips.urls')),
     path('api/destinations/', include('destinations.urls')),
    path('api/bookings/', include('bookings.urls')),
    path('api/reviews/', include('reviews.urls')),
    
    # Optional: Add user management routes if needed
    path('api/users/', include('users.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
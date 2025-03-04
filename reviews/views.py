from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']  # Explicitly allow POST

    def get_queryset(self):
        """Return only the current user's reviews"""
        return Review.objects.filter(user=self.request.user.profile)

    def perform_create(self, serializer):
        """Auto-assign the user's profile when creating a review"""
        serializer.save(user=self.request.user.profile)
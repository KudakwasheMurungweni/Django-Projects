from rest_framework import viewsets, serializers, views, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from .models import Profile
from .serializers import UserSerializer, ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Handles user operations including registration"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        """Allow unauthenticated users to register"""
        if self.action == "create":
            return [AllowAny()]  # Registration does not require authentication
        return [IsAuthenticated()]

    def get_queryset(self):
        """Admins see all users; regular users see only their own data"""
        user = self.request.user
        if user.is_staff:  # Admin can fetch all users
            return User.objects.all()
        return User.objects.filter(id=user.id)  # Regular users see only themselves

    def perform_create(self, serializer):
        """Create a new user with a hashed password"""
        serializer.save()

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def profile(self, request):
        """Fetch the authenticated user's profile"""
        profile, created = Profile.objects.get_or_create(user=request.user)  # Ensure profile exists
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    @action(detail=False, methods=['put'], permission_classes=[IsAuthenticated])
    def update_profile(self, request):
        """Update the authenticated user's profile"""
        try:
            profile = Profile.objects.get(user=request.user)
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)


class ProfileViewSet(viewsets.ModelViewSet):
    """Handles profile updates for authenticated users"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserCreateSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Ensure password is hashed when creating a user"""
        user = User.objects.create_user(**validated_data)
        return user


# users/views.py
class UserCreateView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Now includes profile data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
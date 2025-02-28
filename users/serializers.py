from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserCreateSerializer(serializers.ModelSerializer):
    # Example profile fields (adjust based on your Profile model)
    phone = serializers.CharField(write_only=True, required=False)
    bio = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone', 'address']  # 👈 Add profile fields
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Extract profile-related fields (customize based on your Profile model)
        phone = validated_data.pop('phone', None)
        bio = validated_data.pop('address', None)
        
        # Create the user (triggers the signal to create a Profile)
        user = User.objects.create_user(**validated_data)
        
        # Update the newly created Profile with extracted data
        profile = user.profile
        if phone:
            profile.phone = phone
        if bio:
            profile.bio = bio
        profile.save()
        
        return user

    def to_representation(self, instance):
        # Include profile data in the response
        representation = super().to_representation(instance)
        representation['profile'] = {
            'phone': instance.profile.phone,
            'bio': instance.profile.bio
        }
        return representation
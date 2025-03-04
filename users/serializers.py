from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    # Profile-related fields (should match Profile model)
    phone = serializers.CharField(write_only=True, required=False)
    bio = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        # Include only valid User fields + profile extensions
        fields = ['username', 'email', 'password', 'phone', 'bio']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Correctly extract profile fields
        phone = validated_data.pop('phone', None)
        bio = validated_data.pop('bio', None)  # Fixed from 'address'
        
        # Create user
        user = User.objects.create_user(**validated_data)
        
        # Update associated profile
        profile = user.profile
        if phone:
            profile.phone = phone
        if bio:
            profile.bio = bio
        profile.save()
        
        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Add profile data to response
        representation['profile'] = {
            'phone': instance.profile.phone,
            'bio': instance.profile.bio
        }
        return representation

# Add ProfileSerializer to fix the import error
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone', 'bio', 'address']  # Update with actual Profile model fields
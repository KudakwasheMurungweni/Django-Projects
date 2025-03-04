# users/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Creates a profile for new users with atomic transaction
    and error handling
    """
    if created:
        try:
            with transaction.atomic():
                Profile.objects.get_or_create(user=instance)
        except Exception as e:
            # Log this error in production
            print(f"Error creating profile for user {instance.id}: {str(e)}")

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Saves profile when user is updated, creates if missing
    """
    try:
        # Use get_or_create instead of hasattr check
        profile, created = Profile.objects.get_or_create(user=instance)
        if not created:  # Only save if it already existed
            profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)
    except Exception as e:
        # Log this error in production
        print(f"Error saving profile for user {instance.id}: {str(e)}")
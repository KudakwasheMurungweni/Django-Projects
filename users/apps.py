# users/apps.py
from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        # Ensures signals are connected when app is ready
        # Uses relative import to avoid circular imports
        try:
            from . import signals  # noqa: F401
        except ImportError:
            # Add error logging in production
            pass
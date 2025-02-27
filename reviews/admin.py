from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'trip', 'rating')
    search_fields = ('user__username', 'trip__title')
    list_filter = ('rating',)

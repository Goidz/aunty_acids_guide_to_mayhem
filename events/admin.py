from django.contrib import admin
from .models import City, Genre, Venue


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """Allows admin to manage cities via the admin panel"""
    list_filter = ('created_on',)
    list_display = ('name', 'created_on')
    search_fields = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Allows admin to manage genres via the admin panel"""
    list_filter = ('created_on',)
    list_display = ('name', 'created_on')
    search_fields = ('name',)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    """Allows admin to manage venues via the admin panel"""
    list_filter = ('created_on',)
    list_display = ('name', 'created_on')
    search_fields = ('name',)

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import EventListing

class SummerAdmin(SummernoteModelAdmin):
    summernote_fields ="__all__"

admin.site.register(EventListing, SummerAdmin)

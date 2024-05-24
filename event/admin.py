from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Event_listing

class SummerAdmin(SummernoteModelAdmin):
    summernote_fields ="__all__"

admin.site.register(Event_listing, SummerAdmin)

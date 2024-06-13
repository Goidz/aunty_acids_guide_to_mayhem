from django.forms import ModelForm, widgets
from .models import EventListing


class EventListingForm(ModelForm):
    class Meta:
        model = EventListing
        fields = "__all__"

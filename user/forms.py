from django.forms import ModelForm
from .models import EventListing

class EventListingForm(ModelForm):
    class Meta:
        model = EventListing
        fields = "__all__"
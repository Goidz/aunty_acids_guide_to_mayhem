from django.forms import ModelForm, widgets
from .models import EventListing


class EventListingForm(ModelForm):
    class Meta:
        model = EventListing
        fields = "__all__"


""".git/widgets={
            "event_title" : forms.TextInput(attrs={"class": "form-control"}),
            "pub_date" : forms.DateInput(attrs={"class": "form-control"}),
            "slug" : forms.SlugField(attrs={"class": "form-control"}),
            "organizer" : forms.DateInput(attrs={"class": "form-control"}),
        }
"""
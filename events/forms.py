from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    """ Create Event Form """
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        

    class Meta:
        """Get Event model, choose fields to display"""
        model = Event
        fields = ("title", "details", "city", "venue", "genres", "date", "my_link")
        widgets = {
            # Found assistance on date inputs from: https://stackoverflow.com/questions/59035021/django-dateinput-widget-not-working-in-modelform
            "date": forms.DateInput(attrs={'class':'form-control', 'type':'date'})
        }


from django.shortcuts import loader
from django.http import HttpResponse
from django.views import generic
from event.models import Event_listing

# Create your views here.

def event(request):
    return HttpResponse("This is the event form page")

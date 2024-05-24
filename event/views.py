from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import reverse
from django.http import HttpResponse
from django.views import generic
from event.models import Event_listing

# Create your views here.

def home(request):
    return render(request, "home.html")

def event(request):
    return HttpResponse("This is the event form page")

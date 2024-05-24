from django.shortcuts import loader
from django.http import HttpResponse
from django.views import generic
from event.models import Event_listing

# Create your views here.


def user(request):
    return HttpResponse("This is the user profile page")
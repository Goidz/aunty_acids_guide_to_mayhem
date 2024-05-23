from django.shortcuts import loader
from django.http import HttpResponse

# Create your views here.

def event(request):
    return HttpResponse("This is the event form page")
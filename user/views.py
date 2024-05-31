from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .forms import EventListingForm

def user(request):
    form = EventListingForm()
    context = {"form":form}
    return render(request, "user.html", context)


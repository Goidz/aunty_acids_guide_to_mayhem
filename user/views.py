from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .forms import EventListingForm

def user(request):
    form = EventListingForm()
    if request.method == "POST":
        form = EventListingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form":form}
    return render(request, "user.html", context)

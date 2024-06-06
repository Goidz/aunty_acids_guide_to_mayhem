from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from .forms import EventForm
from .models import Event


def home(request):
    return render(request, "home.html")

def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            add_event_form = form.save(commit=False)
            add_event_form.author = request.user
            add_event_form.save()
            messages.SUCCESS(request, "Hooray! Your event was added successfully!")
            return redirect("events")
        else:
            messages.error(
                request, 'Invalid, incorrect info.')
    form = EventForm()
    context = {"form": form}
    return render(request, "create_event.html", context)

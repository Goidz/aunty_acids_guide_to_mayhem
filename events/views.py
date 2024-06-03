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
        form = EventForm(data=request.POST)
        if form.is_valid():
            event_add = form.save(commit=False)
            event_add.user = request.user
            event_add.save()
            messages.success(request, "Hooray! Your event was added successfully!")
            return redirect("home")
        else:
            messages.error(
                request, 'Invalid, incorrect info.')
    form = EventForm()
    context = {"form": form}
    return render(request, "create_event.html", context)



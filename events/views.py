from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from .forms import EventForm
from .models import Event, Genre, City


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
                request, "Invalid, incorrect info.")
    form = EventForm()
    context = {"form": form}
    return render(request, "create_event.html", context)


def event_list(request):
    event_list = Event.objects.all()
    searched_by = ""
    if request.POST:
        genre_filter = int(request.POST["genre"])
        city_filter = int(request.POST["city"])
        if (genre_filter > -1):
            selected_genre = Genre.objects.get(id=genre_filter)
            event_list = event_list.filter(genres__in=[selected_genre])
            searched_by =f"Genre: {selected_genre.name}"
        if (city_filter > -1):
            selected_city = City.objects.get(id=city_filter)
            event_list = event_list.filter(city=selected_city)
            searched_by +=f" City: {selected_city.name}"
    genre_list = Genre.objects.all()
    city_list = City.objects.all()
    template = "home.html"
    context = {"event_list": event_list, "genre_list": genre_list, "city_list": city_list, "searched_by": searched_by}
    return render(request, template, context)

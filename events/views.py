from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.views import generic
from django.views.generic import UpdateView, DetailView
from django.contrib import messages
from .forms import EventForm
from .models import Event, Genre, City

"""Creating an event"""
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            add_event_form = form.save(commit=False)
            add_event_form.author = request.user
            event = add_event_form.save()
            messages.success(request, "Hooray! Event was sent successfully!")
            return redirect("event_detail", event_detail.pk)
        else:
            messages.error(
                request, "Invalid, incorrect info.")
    form = EventForm()
    context = {"form": form}

    return render(request, "create_event.html", context)


"""
Retrieving and filtering for events.
"""
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


"""
Adding events to User Page.
"""
def user_events(request):
    user_events = Event.objects.filter(author=request.user)
    template = "user.html"
    context = {"user_events": user_events}
    return render(request, template, context)


class EventInfo(DetailView):
    model = Event
    template_name = "events_info.html"
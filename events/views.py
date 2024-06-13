from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import UpdateView, DetailView
from django.contrib import messages
from .forms import EventForm
from .models import Event, Genre, City


def create_event(request):
    """Creating an event"""
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            add_event_form = form.save(commit=False)
            add_event_form.author = request.user
            add_event_form.save()
            event = add_event_form
            form.save_m2m()
            messages.success(request, "Hooray! Event was sent successfully!")
            return HttpResponseRedirect(reverse('event_detail', args=(event.pk,)))
        else:
            messages.error(
                request, "Invalid, incorrect info.")
    form = EventForm()
    context = {"form": form}

    return render(request, "create_event.html", context)


"""Got guidance with edit and delete from Alison O'Keeffe:
https://github.com/AliOKeeffe/PP4_My_Meal_Planner"""
class UpdateEvent(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, generic.UpdateView
        ):
    """This view is used to allow logged in users to edit their own recipes"""
    model = Event
    form_class = EventForm
    template_name = 'update_event.html'
    success_message = "%(calculated_field)s was edited successfully"

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        The signed in user is set as the author of the recipe.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        Prevent another user from updating other's recipes
        """
        event = self.get_object()
        return event.author == self.request.user

    def get_success_message(self, cleaned_data):
        """Override the get_success_message() method 
        to add the event title into the success message.
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )



class DeleteEvent(
        LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """Allow logged in users to delete their own events"""
    model = Event
    template_name = 'delete_event.html'
    success_message = "Event deleted successfully"
    success_url = reverse_lazy('user_events')

    def test_func(self):
        """Prevent other users deleting other's events"""
        event = self.get_object()
        return event.author == self.request.user
    
    def get_success_url(self):
        messages.success(self.request, " Event deleted successfully")
        return reverse_lazy('user_events')


def event_list(request):
    """Retrieving and filtering for events."""
    event_list = Event.objects.all()
    searched_by = ""
    if request.POST:
        genre_filter = int(request.POST["genre"])
        city_filter = int(request.POST["city"])
        if (genre_filter > -1):
            selected_genre = Genre.objects.get(id=genre_filter)
            event_list = event_list.filter(genres__in=[selected_genre])
            searched_by = f"Genre: {selected_genre.name}"
        if (city_filter > -1):
            selected_city = City.objects.get(id=city_filter)
            event_list = event_list.filter(city=selected_city)
            searched_by += f" City: {selected_city.name}"
    genre_list = Genre.objects.all()
    city_list = City.objects.all()
    template = "home.html"
    context = {"event_list": event_list, "genre_list": genre_list,
               "city_list": city_list, "searched_by": searched_by}
    return render(request, template, context)


def user_events(request):
    """Adding events to User Page."""
    user_events = Event.objects.filter(author=request.user)
    template = "user.html"
    context = {"user_events": user_events}
    return render(request, template, context)


class EventInfo(DetailView):
    """Show event info"""
    model = Event
    template_name = "events_info.html"

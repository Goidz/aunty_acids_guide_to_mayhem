from django.urls import path
from . import views

urlpatterns = [
    path("create", views.create_event, name="event_create"),
]



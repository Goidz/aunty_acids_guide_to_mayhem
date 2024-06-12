from django.urls import path
from . import views

urlpatterns = [
    path("create", views.create_event, name="event_create"),
    path("detail/<int:pk>", views.EventInfo.as_view(), name="event_detail"),
]



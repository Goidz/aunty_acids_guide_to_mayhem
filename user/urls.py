from django.urls import path
from . import views
from events import views

urlpatterns = [
    path("user/", views.user_events, name="user_events"),
]

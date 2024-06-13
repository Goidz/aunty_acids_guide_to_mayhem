"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from events import views
# from events.views import create_event, event_list, UpdateView, user_events, EventInfo



urlpatterns = [
    path("account/", include('allauth.urls')),
    path("", (views.event_list), name="home"),
    path("events/", include("events.urls"), name="event-urls"),
    path("user/", include("user.urls"), name="user_events"),
    path("summernote", include("django_summernote.urls")),
    path("admin/", admin.site.urls),
]
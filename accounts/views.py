from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request,user)
                return redirect("home")
            except IntegrityError:
                return render(request, "signup.html", {"form": UserCreationForm, "error": "User already exists"})
        else:
            return render(request, "signup.html", {"form": UserCreationForm, "error": "Passwords do not match, please try again."})

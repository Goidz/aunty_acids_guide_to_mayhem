from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    """Model for City"""
    name = models.CharField(max_length=30, unique=True)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        """To display the cities by created_on in descending order"""
        ordering = ["name", "-created_on"]


    def __str__(self):
        return f"{self.name}"


class Genre(models.Model):
    """Model for Genre"""
    name = models.CharField(max_length=50, unique=True)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        """To display the genres by created_on in descending order alphabetically"""
        ordering = ["name", "-created_on"]


    def __str__(self):
        return f"{self.name}"


class Venue(models.Model):
    """Model for Venues"""
    name = models.CharField(max_length=60, unique=True)
    created_on = models.DateTimeField(auto_now=False)

    class Meta:
        """To display the venues by name in alphabetical order"""
        ordering = ["name"]


    def __str__(self):
        return f"{self.name}"

    """Model for Event"""
class Event(models.Model):
    #STATUS_CHOICES = (
    #   ("draft", "Draft"),
    #    ("published", "Add Event!"),
    #)
    title = models.TextField(max_length=100, unique=True)
    details = models.TextField(max_length=300)
    city = models.ForeignKey(City, related_name="city", on_delete=models.DO_NOTHING)
    venue = models.ForeignKey(Venue, related_name="venue", on_delete=models.DO_NOTHING)
    genres = models.ManyToManyField(Genre, related_name="genres")
    date = models.DateField()
    created_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="events", blank=True, null=True)
    my_link = models.URLField("Add a Website")
    #status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="draft")


    def __str__(self):
        return f"{self.title} @ {self.title} on {self.venue.name}"
        
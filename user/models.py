from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Save Draft"), (1, "Add Event"))


class EventListing(models.Model):
    """Models for event details"""
    event_title = models.CharField(max_length=70, unique=True)
    pub_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(default="", null=False)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=30)
    date = models.DateField()
    venue = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    status = models.IntegerField(choices=STATUS, default=1)

    def __str__(self):
        return f"{self.event_title}"
from django.db import models


class City(models.Model):
    """Model for City"""
    name = models.CharField(max_length=30, unique=True)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        """To display the cities by created_on in descending order"""
        ordering = ["-created_on"]


    def __str__(self):
        return f"{self.name}"


class Genre(models.Model):
    """Model for Genre"""
    name = models.CharField(max_length=50, unique=True)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        """To display the genres by created_on in descending order"""
        ordering = ["name", "-created_on"]


    def __str__(self):
        return f"{self.name}"


class Venue(models.Model):
    """Model for Genre"""
    name = models.CharField(max_length=30, unique=True)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        """To display the genres by created_on in descending order"""
        ordering = ["-created_on"]


    def __str__(self):
        return f"{self.name}"



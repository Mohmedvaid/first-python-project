from django.db import models
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=225)
    release_year = models.IntegerField()
    numder_in_stock = models.IntegerField()
    daily_rates = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)


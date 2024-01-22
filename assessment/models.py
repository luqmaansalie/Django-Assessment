import datetime
from django.db import models


def current_year():
    return datetime.datetime.today().year


class Genre(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    year_released = models.PositiveIntegerField(default=current_year())
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name
    
    def genres_linked(self):
        return ', '.join([g.name for g in self.genres.all()])
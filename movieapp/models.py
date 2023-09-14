from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    #poster = models.URLField()
    genres = models.ManyToManyField('Genre')
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    year_release = models.IntegerField()
    metacritic_rating = models.DecimalField(max_digits=3, decimal_places=1)
    runtime = models.IntegerField()
    
    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
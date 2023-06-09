from django.db import models
from django.conf import settings

# Create your models here.
class Songs(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    year = models.IntegerField()
    length = models.IntegerField()
    
    def __str__(self):
        return self.title + ' - ' + self.artist
    
class Playlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    songs = models.ManyToManyField(Songs, blank=True, default=None, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Recommendation(models.Model):
    name = models.CharField(max_length=50)
    songs = models.ManyToManyField(Songs)

    def __str__(self):
        return self.name

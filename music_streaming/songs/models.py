from django.db import models

# Create your models here.
class Songs(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    year = models.IntegerField()
    length = models.IntegerField()
    #TODO maybe remove this
    def __str__(self):
        return self.title + ' - ' + self.artist
    
class Playlist(models.Model):
    name = models.CharField(max_length=50)
    songs = models.ManyToManyField(Songs)

    def __str__(self):
        return self.name
    
class Recommendation(models.Model):
    name = models.CharField(max_length=50)
    songs = models.ManyToManyField(Songs)

    def __str__(self):
        return self.name

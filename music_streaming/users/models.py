from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class MusicUser(AbstractUser):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

class Playlist(models.Model):
    name = models.CharField(max_length=50)
    songs = models.ManyToManyField('songs.Songs')
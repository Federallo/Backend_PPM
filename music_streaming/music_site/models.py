from django.db import models

# Create your models here.
class Songs(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    year = models.IntegerField()
    length = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='songs/')

    def __str__(self):
        return self.title + ' - ' + self.artist
    
class Playlist(models.Model):
    name = models.CharField(max_length=50)
    songs = models.ManyToManyField(Songs)

    def __str__(self):
        return self.name
    
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    playlists = models.ManyToManyField(Playlist)

    def __str__(self):
        return self.username
    
class Recommendations(models.Model):
    song = models.ForeignKey(Songs, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    playlists = models.ManyToManyField(Playlist)

    def __str__(self):
        return self.song.title + ' - ' + self.user.username + ' - ' + self.rating
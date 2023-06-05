from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.
class MusicUser(AbstractUser):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(("email address"), unique=True)

class MsuicUserManager(BaseUserManager):
    def create_user(self, name, surname, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            name = name,
            surname = surname,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class Playlist(models.Model):
    name = models.CharField(max_length=50)
    songs = models.ManyToManyField('songs.Songs')
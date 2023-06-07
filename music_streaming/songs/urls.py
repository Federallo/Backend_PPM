from django.urls import path
from .views import PlaylistCreateView

from .views import (SongIndexView,)

urlpatterns = [
    path('create_playlist/', PlaylistCreateView.as_view(), name='playlist_create'),
    path('', SongIndexView.as_view(), name='index'),
]
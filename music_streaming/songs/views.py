from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Songs, Playlist

# Create your views here.
class SongIndexView(ListView):
    model = Songs
    template_name = 'index.html'
    context_object_name = 'all_songs'

    def songlist(request):
        song_list = Songs.objects.all()
        return render(request, 'index.html', {'all_songs': song_list})
    
class PlaylistView(LoginRequiredMixin, ListView):
    model = Playlist
    template_name = 'playlist.html'

class PlaylistDetailView(LoginRequiredMixin, View):
    model = Playlist
    template_name = 'playlistDetail.html'

class PlaylistEditView(LoginRequiredMixin, View):
    model = Playlist
    template_name = 'playlistEdit.html'

class PlaylistDeleteView(LoginRequiredMixin, View):
    model = Playlist
    template_name = 'playlistDelete.html'

class PlaylistCreateView(LoginRequiredMixin, View):
    model = Playlist
    template_name = 'playlistCreate.html'
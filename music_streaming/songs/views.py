from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
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
    

@login_required    
class PlaylistView(ListView):
    model = Playlist
    template_name = 'playlist.html'

class PlaylistDetailView(CreateView):
    model = Playlist
    template_name = 'playlistDetail.html'

class PlaylistEditView(CreateView):
    model = Playlist
    template_name = 'playlistEdit.html'

class PlaylistDeleteView(CreateView):
    model = Playlist
    template_name = 'playlistDelete.html'

class PlaylistCreateView(CreateView):
    model = Playlist
    template_name = 'playlistCreation.html'
    fields = ('name', 'description')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
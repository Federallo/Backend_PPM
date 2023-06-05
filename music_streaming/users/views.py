from django.shortcuts import render
from django.views.generic import ListView
from .models import MusicUser, Playlist
from .admin import MusicUserCreationForm

# Create your views here.
class UserInterfaceView(ListView):
    model = MusicUser
    template_name = 'userProfile.html'

    def user_profile(request):
        userProfile = MusicUser.objects.all()
        return render(request, 'userProfile.html', {'user': userProfile})
    
class UserLoginView(ListView):
    model = MusicUser
    template_name = 'userLogin.html'

    def user_login(request):
        context = {}
        context ['form'] = MusicUserCreationForm()
        return render(request, 'userLogin.html', context)
    
class UserCreateView(ListView):
    model = MusicUser
    template_name = 'userCreation.html'
    
class PlaylistsView(ListView):
    model = Playlist
    template_name = 'userProfile.html'

    def playlist(request):
        playlist_list = Playlist.objects.all()
        return render(request, 'userProfile.html', {'playlists': playlist_list})
        

class UserCreatePlaylistView(ListView):
    model = MusicUser
    template_name = 'playlistCreation.html'

class UserDeletePlaylistView(ListView):
    model = MusicUser
    template_name = 'playlistDelete.html'

class DetailedPlaylistView(ListView):
    model = MusicUser
    template_name = 'playlistDetails.html'
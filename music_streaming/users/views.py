from django.shortcuts import render
from django.views.generic import ListView
from .models import MusicUser, Playlist
from .forms import MusicUserCreationForm
from django.http import HttpResponseRedirect

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
    
class UserCreateView(ListView):
    model = MusicUser
    template_name = 'userCreation.html'

    def user_create(request):
        if request.method == 'POST':
            user_create_form = MusicUserCreationForm(request.POST)
            if user_create_form.is_vaild():
                return HttpResponseRedirect('/users/profile/')
        else:
            user_create_form = MusicUserCreationForm()
        return render(request, 'userCreation.html', {'form': user_create_form})
    
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
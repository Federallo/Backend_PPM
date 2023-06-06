from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth import authenticate, login
from .models import MusicUser, Playlist
from .forms import MusicUserCreationForm, MusicUserLoginForm
from django.http import HttpResponseRedirect

# Create your views here.
class UserInterfaceView(ListView):
    model = MusicUser
    template_name = 'userProfile.html'

    def user_profile(request):
        userProfile = MusicUser.objects.all()
        return render(request, 'userProfile.html', {'user': userProfile})
    
def user_login_form(request):
    if request.method == 'POST':
        user_login_form = MusicUserLoginForm(request.POST)
        email = user_login_form['email'].value()
        password = user_login_form['password'].value()
        user = authenticate(request, email = email, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/users/profile/')
        else:
            user_login_form.add_error(None, 'Invalid email or password')
    else:
        user_login_form = MusicUserLoginForm
    return render(request, 'userLogin.html', {'user_login_form': user_login_form})
        


def user_create_form(request):
    if request.method == 'POST':
        user_create_form = MusicUserCreationForm(request.POST)
        return HttpResponseRedirect('/users/profile/')
    else:
        user_create_form = MusicUserCreationForm
    return render(request, 'userCreation.html', {'user_create_form': user_create_form})
    
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
from django.shortcuts import render
from django.views.generic import ListView
from .models import MusicUser

# Create your views here.
class UserInterfraceView(ListView):
    model = MusicUser
    template_name = 'userProfile.html'

    def user_profile(request):
        userProfile = MusicUser.objects.all()
        return render(request, 'userProfile.html', {'user': userProfile})
        

class UserCreatePlaylistView(ListView):
    model = MusicUser
    template_name = 'playlistCreation.html'

class UserDeletePlaylistView(ListView):
    model = MusicUser
    template_name = 'playlistDelete.html'

class UserEditPlaylistView(ListView):
    model = MusicUser
    template_name = 'playlistEdit.html'
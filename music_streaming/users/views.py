from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from songs.models import Playlist
from django.shortcuts import render

# Create your views here.      
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/signup.html'

def profile_view(request):
    playlists = Playlist.objects.filter(owner=request.user)
    return render(request, 'userProfile.html', {'user': request.user, 'playlists': playlists})
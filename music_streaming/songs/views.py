from django.views.generic import ListView, DeleteView, FormView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Songs, Playlist
from .forms import PlaylistForm

# Create your views here.
class SongIndexView(ListView):
    model = Songs
    template_name = 'index.html'
    context_object_name = 'all_songs'

    def songlist(request):
        song_list = Songs.objects.all()
        return render(request, 'index.html', {'all_songs': song_list})
    
class PlaylistCreateView(FormView, LoginRequiredMixin):
    form_class = PlaylistForm
    template_name = 'playlistCreation.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.save()
        return super().form_valid(form)

class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = 'playlistDetail.html'
    success_url = reverse_lazy('profile')

class PlaylistEditView(UpdateView):
    model = Playlist
    template_name = 'playlistEdit.html'
    form_class = PlaylistForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        playlist = self.get_object()

        form.instance.owner = self.request.user
        form.save()

        selected_songs = form.cleaned_data["songs"]
        playlist.songs.set(selected_songs)
        
        return super().form_valid(form)

class PlaylistDeleteView(DeleteView):
    model = Playlist
    template_name = 'playlistDelete.html'
    success_url = reverse_lazy('profile')
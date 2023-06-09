from django.views.generic import ListView, DeleteView, FormView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Songs, Playlist, SongSerializer
from .forms import PlaylistForm
from rest_framework import viewsets
from .filters import SongFilter

# Create your views here.
#Showing all songs
class SongIndexView(ListView):
    model = Songs
    template_name = 'index.html'
    context_object_name = 'all_songs'

    def get_queryset(self):
        queryset = super().get_queryset()
        song_filter = SongFilter(self.request.GET, queryset=queryset)
        return song_filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['song_filter'] = SongFilter(self.request.GET, queryset=self.get_queryset())
        return context
    
#All actions for playlists
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

#Filtering songs
class SongViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer
    filterset_class = SongFilter
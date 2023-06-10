from django.views.generic import ListView, DeleteView, FormView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Songs, Playlist, SongSerializer, Recommendation
from .forms import PlaylistForm
from rest_framework import viewsets
from .filters import SongFilter
from django.db.models import Count
from django.shortcuts import render

# Create your views here.
#showing all songs
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
    
#all actions for playlists
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

#filtering songs
class SongViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer
    filterset_class = SongFilter

#creating a recommendation algorithm and its view
def recommend_songs(user):
    # Get the user's most listened genre
    most_listened_genre = (
        Songs.objects.filter(playlist__owner=user)
        .values('genre')
        .annotate(count=Count('genre'))
        .order_by('-count')
        .first()
    )

    if most_listened_genre:
        # excluding songs from the user's playlists
        user_playlists = Playlist.objects.filter(owner=user)
        excluded_songs = Songs.objects.filter(playlist__in=user_playlists)

        # getting recommended songs based on the most listened genre
        subquery = Songs.objects.filter(genre=most_listened_genre['genre'])
        recommended_songs = (
            Songs.objects.exclude(id__in=excluded_songs)
            .filter(genre=most_listened_genre['genre'], id__in=subquery)
            .exclude(playlist__owner=user)
            .order_by('?')[:10]  # randomizing the order of recommended songs and limiting the number of recommended songs to 10
        )

        # creating a new recommendation object to store the recommended songs
        recommendation = Recommendation.objects.create(name="Recommended Songs")

        # adding the recommended songs to the recommendation object
        recommendation.songs.set(recommended_songs)

        return recommendation
    else:
        return None
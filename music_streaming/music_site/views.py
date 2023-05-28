from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Songs, Playlist, User, Recommendations

# Create your views here.
# Retrieve songs from the database
def index(request):
    songs = Songs.objects.all()
    context = {
        'songs': songs
    }
    return render(request, 'music/index.html', context)

# Create a new playlist object with the provided data from the form
def create_playlist(request):
    if request.method == 'POST':
        playlist = Playlist(name=request.POST['name'])
        playlist.save()
        return HttpResponse('Playlist created successfully!')
    else:
        return render(request, 'music/create_playlist.html')
    
# Add the song to the playlist    
def add_song_to_playlist(request, playlist_id, song_id):
    # Retrieve the playlist and song objects from the database using the provided IDs
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    song = get_object_or_404(Songs, pk=song_id)

    playlist.songs.add(song)
    return HttpResponse('Song added to playlist successfully!')    

# Retrieve the playlist from the database using the playlist_id
def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    context = {
        'playlist': playlist
    }
    return render(request, 'music/playlist_detail.html', context)

#TODO: create function to remove song from playlist

# Retrieve the user profile from the database using the user_id
def user_profile(request, user_id):
    profile = get_object_or_404(User, user_id=user_id)
    context = {
        'profile': profile
    }
    return render(request, 'music/user_profile.html', context)

#for users recommendations
def recommendations(request):
    # Retrieve the current user's profile
    user_profile = get_object_or_404(User, user_id=request.user.id)

    # Call a recommendation algorithm to get a list of recommended songs
    recommended_songs = recommend_songs(user_profile)

    context = {
        'recommended_songs': recommended_songs
    }
    return render(request, 'music/recommendations.html', context)

# Perform a search query on the songs based on the provided query
def search_songs(request):
    query = request.GET.get('query')

    songs = Songs.objects.filter(title__icontains=query)
    context = {
        'songs': songs
    }
    return render(request, 'music/search_results.html', context)

#filter songs
#TODO add filters for artist, album, year, length (for example)
def filter_songs(request):
    genre = request.GET.get('genre')

    # Filter the songs based on the selected genre
    songs = Songs.objects.filter(genre=genre)
    context = {
        'songs': songs
    }
    return render(request, 'music/filtered_songs.html', context)
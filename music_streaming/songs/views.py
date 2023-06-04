from django.views.generic import ListView
from django.shortcuts import render
from .models import Songs

# Create your views here.
class SongIndexView(ListView):
    model = Songs
    template_name = 'index.html'
    context_object_name = 'all_songs'

    def songlist(request):
        song_list = Songs.objects.all()
        return render(request, 'index.html', {'all_songs': song_list})
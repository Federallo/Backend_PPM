from django_filters import rest_framework as filters
from .models import Songs

class SongFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    artist = filters.CharFilter(lookup_expr='icontains')
    album = filters.CharFilter(lookup_expr='icontains')
    genre = filters.CharFilter(lookup_expr='icontains')
    year = filters.NumberFilter(lookup_expr='exact')
    length = filters.NumberFilter()
    
    class Meta:
        model = Songs
        fields = ['title', 'artist', 'album', 'genre', 'year', 'length']
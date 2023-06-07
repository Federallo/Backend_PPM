from django.urls import path
from . import views

urlpatterns = [
    path('create_playlist/', views.PlaylistCreateView.as_view(), name='playlist_create'),
    path('', views.SongIndexView.as_view(), name='index'),
]
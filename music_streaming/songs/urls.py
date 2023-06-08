from django.urls import path
from . import views

urlpatterns = [
    path('create_playlist/', views.PlaylistCreateView.as_view(), name='playlist_create'),
    path('playlist_detail/', views.PlaylistDetailView.as_view(), name='playlist_detail'),
    path('playlist_update/', views.PlaylistEditView.as_view(), name='playlist_edit'),
    path('<int:pk>/playlist_delete/', views.PlaylistDeleteView.as_view(), name='playlist_delete'),
    path('', views.SongIndexView.as_view(), name='index'),
]
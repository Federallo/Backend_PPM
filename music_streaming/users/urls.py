from django.urls import path
from .views import UserInterfaceView, UserLoginView, UserCreateView, PlaylistsView, UserCreatePlaylistView, UserDeletePlaylistView, DetailedPlaylistView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='userLogin'),
    path('create/', UserCreateView.as_view(), name='userCreate'),
    path('profile/', UserInterfaceView.as_view(), name='userProfile'),
]
from django.urls import path
from .views import user_create_form, UserInterfaceView, UserLoginView, PlaylistsView, UserCreatePlaylistView, UserDeletePlaylistView, DetailedPlaylistView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='userLogin'),
    path('create/', user_create_form, name='userCreate'),
    path('profile/', UserInterfaceView.as_view(), name='userProfile'),
] 
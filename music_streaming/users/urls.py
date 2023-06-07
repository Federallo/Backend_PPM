from django.urls import path
from .views import SignUpView#, user_create_form, UserInterfaceView, user_login_form, PlaylistsView, UserCreatePlaylistView, UserDeletePlaylistView, DetailedPlaylistView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    #path('login/', user_login_form, name='userLogin'),
    #path('create/', user_create_form, name='userCreate'),
    #path('profile/', UserInterfaceView.as_view(), name='userProfile'),
]
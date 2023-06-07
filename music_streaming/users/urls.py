from django.urls import path
from .views import SignUpView, ProfileView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('profile', ProfileView.as_view(), name='profile'),
]
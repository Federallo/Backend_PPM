from django.urls import path, include
from .views import SignUpView, profile_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('user/signup/', SignUpView.as_view(), name='signup'),
    path('user/login/', auth_views.LoginView.as_view(), name='login'),
    path('user/profile/', profile_view, name='profile'),
    path('user/', include('django.contrib.auth.urls')),
]
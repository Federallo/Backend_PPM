from django.shortcuts import render
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

# Create your views here.      
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'userProfile.html'
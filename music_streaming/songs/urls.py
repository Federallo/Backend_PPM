from django.urls import path

from .views import (SongIndexView,)

urlpatterns = [
    path('', SongIndexView.as_view(), name='index'),
]
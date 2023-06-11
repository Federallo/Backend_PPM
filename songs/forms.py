from django import forms
from .models import Playlist, Songs #TODO implement songs adding feature

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ('name', 'description','songs')
        widgets = {
            'owner': forms.HiddenInput(),
            'songs': forms.CheckboxSelectMultiple(),
        }
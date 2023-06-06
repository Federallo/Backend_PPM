from django import forms
from .models import MusicUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

#user form
#user creation
class MusicUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MusicUser
        fields = ('name', 'surname', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.name = self.cleaned_data['name']
        user.surname = self.cleaned_data['surname']
        user.email = self.cleaned_data['email']
        if commit:
           user.save()
        return user
    

class MusicUserLoginForm(forms.ModelForm):
    class Meta:
        model = MusicUser
        fields = ('email', 'password')


#user update#FIXME
#class MusicUserChangeForm(forms.ModelForm):
#    password = ReadOnlyPasswordHashField()
#    class Meta:
#       model = MusicUser
#        fields = ('name', 'surname', 'email', 'password', 'is_active', 'is_admin')
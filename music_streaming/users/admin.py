from django.contrib import admin
from .models import MusicUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(MusicUser, UserAdmin)
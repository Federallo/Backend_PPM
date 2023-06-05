from django.contrib import admin
from .models import MusicUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(MusicUser, UserAdmin)
admin.site.unregister(Group)
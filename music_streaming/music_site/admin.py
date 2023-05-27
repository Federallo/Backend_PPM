from django.contrib import admin

# Register your models here.
from .models import Songs, Playlist, User, Recommendations

admin.site.register(Songs)
admin.site.register(Playlist)
admin.site.register(User)
admin.site.register(Recommendations)
from django.contrib import admin
from .models import Notification, Album, Photo 
from .models import FriendRequest

admin.site.register(Notification)
admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(FriendRequest)

from django.contrib import admin
from .models import Notification, Album, Photo  # aur jo bhi model chahiye

admin.site.register(Notification)
admin.site.register(Album)
admin.site.register(Photo)

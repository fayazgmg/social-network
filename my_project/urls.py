from django.urls import path
from . import views
from .views import photo_delete, photo_update


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('friends/', views.friends, name='friends'),
    path('messages/', views.messages, name='messages'),
    path('albums/', views.album_list, name='album_list'),
    path('albums/create/', views.album_create, name='album_create'),
    path('albums/<int:pk>/update/', views.album_update, name='album_update'),
    path('albums/<int:pk>/delete/', views.album_delete, name='album_delete'),
    path('albums/upload/', views.upload_photo, name='upload_photo'),
    # path('photo/<int:pk>/edit/', views.photo_edit, name='photo_edit'),
    # path('photo/<int:pk>/delete/', views.photo_delete, name='photo_delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('register/', views.register_view, name='register'),
    path('photo/<int:photo_id>/delete/', photo_delete, name='photo_delete'),
    path('photo/<int:photo_id>/edit/', photo_update, name='photo_update'),


]
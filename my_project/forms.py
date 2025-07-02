from django import forms
from .models import Photo
from .models import Album



class PhotoForm(forms.Form):
    album_name = forms.CharField(label="Album Name", max_length=100)
    image = forms.ImageField()



class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name']        
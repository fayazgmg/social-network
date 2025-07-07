from django import forms
from .models import Photo
from .models import Album



# class PhotoForm(forms.Form):
#     album_name = forms.CharField(label="Album Name", max_length=100)
#     image = forms.ImageField()


class PhotoForm(forms.ModelForm):
    album_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Photo
        fields = ['album_name', 'image']



class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name']        
        widgets = {
        'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter album name'
             }),
        }
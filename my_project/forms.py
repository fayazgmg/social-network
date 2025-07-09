from django import forms
from .models import Photo
from .models import Album
from .models import Post



# class PhotoForm(forms.Form):
#     album_name = forms.CharField(label="Album Name", max_length=100)
#     image = forms.ImageField()


class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

    def value_from_datadict(self, data, files, name):
        if name in files:
            return files.getlist(name)
        return None

class PostForm(forms.ModelForm):
    images = forms.FileField(widget=MultiFileInput, required=False)
    videos = forms.FileField(widget=MultiFileInput, required=False)

    class Meta:
        model = Post
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['feelings'].queryset = Feeling.objects.all()


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
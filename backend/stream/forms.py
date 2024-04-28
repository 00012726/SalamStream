from django import forms
from .models import VideoModel, AudioModel, BookModel


class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoModel
        fields = ['title', 'description', 'thumbnail_photo', 'video_file']

class AudioForm(forms.ModelForm):
    class Meta:
        model = AudioModel
        fields = ['title', 'description', 'thumbnail_photo', 'audio_file']

class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['title', 'description', 'thumbnail_photo', 'book_file']
from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.views.generic import TemplateView, CreateView # type: ignore
from django.urls import reverse_lazy # type: ignore



from .models import VideoModel, AudioModel, BookModel


class HomeTemplate(TemplateView):
    template_name = 'welcome.html'


class AdminTemplate(TemplateView):
    template_name = 'adminPage.html'


class AudioTemplate(TemplateView):
    template_name = 'audio.html'


class AuthorBookTemplate(TemplateView):
    template_name = 'authorBook.html'


class AuthorVideoTemplate(TemplateView):
    template_name = 'authorVideo.html'


class BookTemplate(TemplateView):
    template_name = 'book.html'


class LoginTemplate(TemplateView):
    template_name = 'login.html'


class ModeratorTemplate(TemplateView):
    template_name = 'moderationPage.html'


class PlayAudioTemplate(TemplateView):
    template_name = 'playAudio.html'

def index_video_list(request):
    query = request.GET.get('q')
    videos = VideoModel.objects.all()
    if query:
        videos = videos.filter(title__icontains=query)
    return render(request, 'index.html', {'videos': videos})

def video_detail(request, pk):
    video = VideoModel.objects.get(pk=pk)
    video.views += 1
    video.save()
    related_videos = VideoModel.objects.all()
    return render(request, 'playVid.html', {'video': video, 'related_videos': related_videos})


def audio_list(request):
    query = request.GET.get('q')
    audios = AudioModel.objects.all()
    if query:
        audios = audios.filter(title__icontains=query)
    return render(request, 'audio.html', {'audios': audios})

def audio_detail(request, pk):
    audio = AudioModel.objects.get(pk=pk)
    related_audios = AudioModel.objects.all()
    return render(request, 'playAudio.html', {'audio': audio, 'related_audios': related_audios})



def book_list(request):
    query = request.GET.get('q')
    books = BookModel.objects.all()
    if query:
        books = books.filter(title__icontains=query)
    return render(request, 'book.html', {'books': books})

class AdminsTemplateView(TemplateView):
    template_name = 'adminPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_videos'] = VideoModel.objects.all()
        context['user_audios'] = AudioModel.objects.all()
        context['user_books'] = BookModel.objects.all()
        return context

class UploadTemplateView(TemplateView):
    template_name = 'uploadContent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_videos'] = VideoModel.objects.filter(user=self.request.user)
        context['user_audios'] = AudioModel.objects.filter(user=self.request.user)
        context['user_books'] = BookModel.objects.filter(user=self.request.user)
        return context

class VideoCreateView(CreateView):
    model = VideoModel
    fields = []
    template_name = 'uploadVideo.html'
    success_url = reverse_lazy('upload')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_videos'] = VideoModel.objects.filter(user=self.request.user)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        thumbnail_photo = self.request.FILES.get('thumbnail_photo')
        video_file = self.request.FILES.get('video_file')
        title = self.request.POST.get('title')
        if video_file is not None and thumbnail_photo is not None and title is not None:
            form.instance.video_file = video_file
            form.instance.thumbnail_photo = thumbnail_photo
            form.instance.title = title
            print('Success')
        else:
            return self.form_invalid(form)
        form.save()
        return super().form_valid(form)

class AudioCreateView(CreateView):
    model = AudioModel
    fields = []
    template_name = 'uploadAudio.html'
    success_url = reverse_lazy('upload')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_audios'] = AudioModel.objects.filter(user=self.request.user)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.audio_status = AudioModel.PROGRESS
        thumbnail_photo = self.request.FILES.get('thumbnail_photo')
        audio_file = self.request.FILES.get('audio_file')
        title = self.request.POST.get('title')
        if thumbnail_photo is not None and audio_file is not None and title is not None:
            form.instance.audio_file = audio_file
            form.instance.thumbnail_photo = thumbnail_photo
            form.instance.title = title
            print('Success')
        else:
            return self.form_invalid(form)
        form.save()
        return super().form_valid(form)
    
class BookCreateView(CreateView):
    model = BookModel
    fields = []
    template_name = 'uploadBook.html'
    success_url = reverse_lazy('upload')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_books'] = BookModel.objects.filter(user=self.request.user)
        return context


    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book_status = BookModel.PROGRESS
        thumbnail_photo = self.request.FILES.get('thumbnail_photo')
        book_file = self.request.FILES.get('book_file')
        title = self.request.POST.get('title')
        if thumbnail_photo is not None and book_file is not None and title is not None:
            form.instance.book_file = book_file
            form.instance.thumbnail_photo = thumbnail_photo
            form.instance.title = title
            print('Success')
        else:
            return self.form_invalid(form)
        form.save()
        return super().form_valid(form)


@login_required
def change_video_status(request, video_id, new_status):
    if request.user.user_type == 'Moderator':
        video = get_object_or_404(VideoModel, pk=video_id)
        video.video_status = new_status
        video.save()
    return redirect('admins')


@login_required
def change_audio_status(request, audio_id, new_status):
    if request.user.user_type == 'Moderator':
        audio = get_object_or_404(AudioModel, pk=audio_id)
        audio.audio_status = new_status
        audio.save()
    return redirect('admins')


@login_required
def change_book_status(request, book_id, new_status):
    if request.user.user_type == 'Moderator':
        book = get_object_or_404(BookModel, pk=book_id)
        book.book_status = new_status
        book.save()
    return redirect('admins')

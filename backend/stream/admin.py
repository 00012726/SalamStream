from django.contrib import admin # type: ignore

from .models import VideoModel, AudioModel, BookModel

@admin.register(VideoModel)
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'views', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    save_as = True
    save_as_continue = True
    save_on_top = True
@admin.register(AudioModel)
class AudioModelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    save_as = True
    save_as_continue = True
    save_on_top = True

@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    save_as = True
    save_as_continue = True
    save_on_top = True

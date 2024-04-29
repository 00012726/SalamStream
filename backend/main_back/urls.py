
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from django.conf.urls.static import static # type: ignore
from django.conf import settings # type: ignore
from stream.views import *
from users.views import register, user_login, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeTemplate.as_view(), name='home'),
    path('admins/', AdminsTemplateView.as_view(), name='admins'),
    path('audio/', audio_list, name='audio'),
    path('author/', AuthorBookTemplate.as_view(), name='author'),
    path('author-video/', AuthorVideoTemplate.as_view(), name='author-video'),
    path('book/', book_list, name='book'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('moderator/', ModeratorTemplate.as_view(), name='moderator'),
    path('play-audio/<int:pk>', audio_detail, name='audio_detail'),
    path('play-video/<int:pk>', video_detail, name='video_detail'),
    path('home/', index_video_list, name='home'),
    path('upload/', UploadTemplateView.as_view(), name='upload'),
    path('upload/create', VideoCreateView.as_view(), name='upload_video'),
    path('upload/a-create', AudioCreateView.as_view(), name='upload_audio'),
    path('upload/b-create', BookCreateView.as_view(), name='upload_book'),
    path('video/<int:video_id>/success/', change_video_status, {'new_status': 'SUCCESS'}, name='change_video_success'),
    path('video/<int:video_id>/cancel/', change_video_status, {'new_status': 'CANCEL'}, name='change_video_cancel'),
    path('audio/<int:audio_id>/success/', change_audio_status, {'new_status': 'SUCCESS'}, name='change_audio_success'),
    path('audio/<int:audio_id>/cancel/', change_audio_status, {'new_status': 'CANCEL'}, name='change_audio_cancel'),
    path('book/<int:book_id>/success/', change_book_status, {'new_status': 'SUCCESS'}, name='change_book_success'),
    path('book/<int:book_id>/cancel/', change_book_status, {'new_status': 'CANCEL'}, name='change_book_cancel'),    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

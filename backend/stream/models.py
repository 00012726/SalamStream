from django.db import models 
from django.contrib.auth import get_user_model 

User = get_user_model()

class VideoModel(models.Model): #model for videos
    PROGRESS = 'PROGRESS'
    CANCEL = 'CANCEL'
    SUCCESS = 'SUCCESS'
    VIDEO_STATUS = [
        (PROGRESS, 'В прогрессе'),
        (CANCEL, 'Отменен'),
        (SUCCESS, 'Успешно'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE) #user identification when uploaded
    title = models.CharField(max_length=110)
    # tags = models.CharField(max_length=90)
    thumbnail_photo = models.FileField(upload_to='video_photos/', null=True, blank=True)
    video_file = models.FileField(upload_to='videos/')
    description = models.TextField()
    views = models.PositiveIntegerField(default=0)
    video_status = models.CharField(max_length=70, choices=VIDEO_STATUS, default=PROGRESS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

class AudioModel(models.Model): #model for audio
    PROGRESS = 'PROGRESS'
    CANCEL = 'CANCEL'
    SUCCESS = 'SUCCESS'
    AUDIO_STATUS = [
        (PROGRESS, 'В прогрессе'),
        (CANCEL, 'Отменен'),
        (SUCCESS, 'Успешно'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=110)
    thumbnail_photo = models.FileField(upload_to='audio_photo/', null=True)
    audio_file = models.FileField(upload_to='audio/')
    description = models.TextField()
    audio_status = models.CharField(max_length=70, choices=AUDIO_STATUS, default=PROGRESS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Audio'
        verbose_name_plural = 'Audios'
 
class BookModel(models.Model): #model for book
    PROGRESS = 'PROGRESS'
    CANCEL = 'CANCEL'
    SUCCESS = 'SUCCESS'
    BOOK_STATUS = [
        (PROGRESS, 'В прогрессе'),
        (CANCEL, 'Отменен'),
        (SUCCESS, 'Успешно'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=110)
    thumbnail_photo = models.FileField(upload_to='books_photo/')
    book_file = models.FileField(upload_to='books/')
    description = models.TextField()
    book_status = models.CharField(max_length=70, choices=BOOK_STATUS, default=PROGRESS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

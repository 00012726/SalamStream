from django.contrib.auth.models import AbstractUser # type: ignore
from django.db import models # type: ignore

class CustomUser(AbstractUser):
    MODERATOR = 'Moderator'
    CONTENT_MAKER = 'Content_maker'
    USER = 'User'
    USER_TYPES = [
        (MODERATOR, 'Модератор'),
        (CONTENT_MAKER, 'Контент мейкер'),
        (USER, 'Пользователь'),
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default=USER)

    def __str__(self):
        return self.username

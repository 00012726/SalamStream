from django.apps import AppConfig # type: ignore


class StreamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stream'

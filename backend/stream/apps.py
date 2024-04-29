from django.apps import AppConfig 

class StreamConfig(AppConfig): 
    default_auto_field = 'django.db.models.BigAutoField' # auto generated primary key for each row
    name = 'stream'

# Generated by Django 4.2.9 on 2024-03-19 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0003_audiomodel_thumbnail_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiomodel',
            name='audio_status',
            field=models.CharField(choices=[('P', 'В прогрессе'), ('C', 'Отменен'), ('S', 'Успешно')], default='P', max_length=70),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='book_status',
            field=models.CharField(choices=[('P', 'В прогрессе'), ('C', 'Отменен'), ('S', 'Успешно')], default='P', max_length=70),
        ),
        migrations.AddField(
            model_name='videomodel',
            name='video_status',
            field=models.CharField(choices=[('P', 'В прогрессе'), ('C', 'Отменен'), ('S', 'Успешно')], default='P', max_length=70),
        ),
    ]

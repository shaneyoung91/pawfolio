# Generated by Django 4.2.3 on 2023-08-04 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_photo_reportcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportcard',
            name='photo_url',
            field=models.URLField(blank=True),
        ),
    ]

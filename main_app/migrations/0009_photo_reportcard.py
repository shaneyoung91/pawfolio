# Generated by Django 4.2.3 on 2023-08-03 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='reportcard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.reportcard'),
        ),
    ]

# Generated by Django 3.0.3 on 2020-07-13 14:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fifth_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfileInfoFrom',
            new_name='UserProfileInfo',
        ),
    ]

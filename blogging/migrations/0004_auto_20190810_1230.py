# Generated by Django 2.1.1 on 2019-08-10 19:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogging', '0003_create_post_published_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Create_Post',
            new_name='CreatePost',
        ),
    ]
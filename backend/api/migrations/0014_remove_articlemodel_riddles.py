# Generated by Django 5.0.6 on 2024-06-23 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_rename_bookmarks_articlemodel_riddles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlemodel',
            name='riddles',
        ),
    ]
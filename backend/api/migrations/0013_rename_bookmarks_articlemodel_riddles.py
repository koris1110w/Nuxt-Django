# Generated by Django 5.0.6 on 2024-06-23 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_articlemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlemodel',
            old_name='bookmarks',
            new_name='riddles',
        ),
    ]

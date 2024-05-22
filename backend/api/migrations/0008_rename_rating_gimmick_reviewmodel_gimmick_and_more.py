# Generated by Django 5.0.6 on 2024-05-21 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_riddlemodel_level_remove_riddlemodel_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewmodel',
            old_name='rating_gimmick',
            new_name='gimmick',
        ),
        migrations.RenameField(
            model_name='reviewmodel',
            old_name='rating_level',
            new_name='level',
        ),
        migrations.RenameField(
            model_name='reviewmodel',
            old_name='rating_story',
            new_name='story',
        ),
        migrations.RenameField(
            model_name='reviewmodel',
            old_name='rating_sukkiri',
            new_name='sukkiri',
        ),
        migrations.RenameField(
            model_name='reviewmodel',
            old_name='rating_time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='riddlemodel',
            old_name='rating_gimmick',
            new_name='gimmick',
        ),
        migrations.RenameField(
            model_name='riddlemodel',
            old_name='rating_level',
            new_name='level',
        ),
        migrations.RenameField(
            model_name='riddlemodel',
            old_name='rating_story',
            new_name='story',
        ),
        migrations.RenameField(
            model_name='riddlemodel',
            old_name='rating_sukkiri',
            new_name='sukkiri',
        ),
        migrations.RenameField(
            model_name='riddlemodel',
            old_name='rating_time',
            new_name='time',
        ),
        migrations.AlterField(
            model_name='riddlemodel',
            name='type',
            field=models.CharField(choices=[('web', 'WEB'), ('line', 'LINE@')], max_length=10),
        ),
    ]

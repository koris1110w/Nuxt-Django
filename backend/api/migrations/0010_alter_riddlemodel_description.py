# Generated by Django 5.0.6 on 2024-05-29 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_reviewmodel_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riddlemodel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

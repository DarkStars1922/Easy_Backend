# Generated by Django 5.1.2 on 2024-10-23 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_blacklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='favorite_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='likes_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
# Generated by Django 5.1.2 on 2024-10-23 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_article_favorite_count_article_likes_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='likes_count',
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-28 00:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('likes', '0001_initial'),
        ('notifications', '0008_notification_tag'),
        ('users', '0012_blacklist_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='comment',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='comments.comment'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='favorite',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='users.favorite'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='like',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='likes.like'),
        ),
    ]

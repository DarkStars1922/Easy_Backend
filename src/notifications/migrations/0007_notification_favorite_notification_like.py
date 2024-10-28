# Generated by Django 5.1.2 on 2024-10-28 00:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
        ('notifications', '0006_alter_notification_comment'),
        ('users', '0012_blacklist_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='favorite',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.favorite'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='like',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='likes.like'),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.1.2 on 2024-10-19 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created_at',)},
        ),
    ]

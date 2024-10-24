# Generated by Django 5.1.2 on 2024-10-24 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_article_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created_at', '-updated_at')},
        ),
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='article_picture/'),
        ),
    ]
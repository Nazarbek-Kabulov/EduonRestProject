# Generated by Django 4.2.6 on 2023-11-24 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_cart_courses_cart_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='thumbnail',
            field=models.FileField(upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video_location',
            field=models.FileField(upload_to='media/videos/'),
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-24 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_lesson_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='length',
            field=models.DurationField(),
        ),
    ]
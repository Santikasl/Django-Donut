# Generated by Django 3.2.12 on 2022-06-06 10:02

from django.db import migrations, models
import donut.models


class Migration(migrations.Migration):

    dependencies = [
        ('donut', '0025_rename_photo_posts_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(default=donut.models.default_datetime),
        ),
    ]

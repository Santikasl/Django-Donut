# Generated by Django 3.2.12 on 2022-06-08 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donut', '0002_likespost'),
    ]

    operations = [
        migrations.AddField(
            model_name='likespost',
            name='check',
            field=models.BooleanField(default=False),
        ),
    ]

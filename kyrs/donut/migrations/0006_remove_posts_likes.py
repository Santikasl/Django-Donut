# Generated by Django 3.2.12 on 2022-06-09 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donut', '0005_rename_check_likespost_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='likes',
        ),
    ]
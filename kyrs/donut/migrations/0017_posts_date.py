# Generated by Django 3.2.12 on 2022-05-02 17:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('donut', '0016_alter_posts_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.12 on 2022-06-22 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donut', '0020_auto_20220622_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusers',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_code/'),
        ),
        migrations.AlterField(
            model_name='likespost',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10),
        ),
    ]
# Generated by Django 2.0.5 on 2018-10-10 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_app', '0002_auto_20181010_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpofileinfo',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pictures/default_profile_picture.png', null=True, upload_to='profile_pictures'),
        ),
    ]

# Generated by Django 2.0.5 on 2018-10-12 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pictures/default.png', upload_to='profile_pictures/%Y/%m'),
        ),
    ]

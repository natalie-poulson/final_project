# Generated by Django 2.0.5 on 2018-10-12 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_app', '0002_auto_20181012_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='bio',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='current_city',
            field=models.CharField(max_length=100),
        ),
    ]
# Generated by Django 2.0.5 on 2018-10-16 05:53

from django.db import migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('final_app', '0002_auto_20181016_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='location',
            field=djgeojson.fields.PointField(blank=True, null=True),
        ),
    ]

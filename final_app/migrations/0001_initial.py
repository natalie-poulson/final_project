# Generated by Django 2.0.5 on 2018-10-20 00:09

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=200)),
                ('packed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Gear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gear_name', models.CharField(max_length=200)),
                ('packed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='post_pictures/%Y/%m')),
                ('caption', models.CharField(blank=True, max_length=200)),
                ('body', models.TextField(blank=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('slug', models.SlugField(unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('trail', models.CharField(max_length=300)),
                ('permit', models.URLField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('current_city', models.CharField(blank=True, max_length=100)),
                ('bio', models.CharField(blank=True, max_length=200)),
                ('profile_picture', models.ImageField(default='profile_pictures/default.png', upload_to='profile_pictures/%Y/%m')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_posts', to='final_app.Trip'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gear',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_gears', to='final_app.Trip'),
        ),
        migrations.AddField(
            model_name='food',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_foods', to='final_app.Trip'),
        ),
    ]

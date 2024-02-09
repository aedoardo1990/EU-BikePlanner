# Generated by Django 4.2.9 on 2024-02-09 10:28

import autoslug.fields
import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('start_date', models.DateField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('persons_number', models.IntegerField()),
                ('additional_item', models.CharField(max_length=200)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike_planner.track')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mytrips', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('route_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('excerpt', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]

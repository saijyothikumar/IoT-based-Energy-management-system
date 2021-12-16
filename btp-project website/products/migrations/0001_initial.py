# Generated by Django 3.0 on 2021-04-30 12:44

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
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('device11', models.FloatField(default=0)),
                ('device12', models.FloatField(default=0)),
                ('device13', models.FloatField(default=0)),
                ('switch11', models.FloatField(default=0)),
                ('switch12', models.FloatField(default=0)),
                ('device21', models.FloatField(default=0)),
                ('device22', models.FloatField(default=0)),
                ('device23', models.FloatField(default=0)),
                ('switch21', models.FloatField(default=0)),
                ('switch22', models.FloatField(default=0)),
                ('device31', models.FloatField(default=0)),
                ('device32', models.FloatField(default=0)),
                ('device33', models.FloatField(default=0)),
                ('switch31', models.FloatField(default=0)),
                ('switch32', models.FloatField(default=0)),
                ('pub_date', models.DateTimeField()),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('room1_upload_link', models.TextField()),
                ('room1_download_link', models.TextField()),
                ('room1_id', models.FloatField()),
                ('room2_upload_link', models.TextField()),
                ('room2_download_link', models.TextField()),
                ('room2_id', models.FloatField()),
                ('room3_upload_link', models.TextField()),
                ('room3_download_link', models.TextField()),
                ('room3_id', models.FloatField()),
                ('pub_date', models.DateTimeField()),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('device11_name', models.CharField(max_length=255)),
                ('device12_name', models.CharField(max_length=255)),
                ('device13_name', models.CharField(max_length=255)),
                ('switch11_name', models.CharField(max_length=255)),
                ('switch12_name', models.CharField(max_length=255)),
                ('device21_name', models.CharField(max_length=255)),
                ('device22_name', models.CharField(max_length=255)),
                ('device23_name', models.CharField(max_length=255)),
                ('switch21_name', models.CharField(max_length=255)),
                ('switch22_name', models.CharField(max_length=255)),
                ('device31_name', models.CharField(max_length=255)),
                ('device32_name', models.CharField(max_length=255)),
                ('device33_name', models.CharField(max_length=255)),
                ('switch31_name', models.CharField(max_length=255)),
                ('switch32_name', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField()),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

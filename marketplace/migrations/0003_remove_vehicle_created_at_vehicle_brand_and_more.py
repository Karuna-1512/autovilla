# Generated by Django 5.1.6 on 2025-04-14 13:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_remove_vehicle_title_vehicle_owner_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='created_at',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='brand',
            field=models.CharField(default='Unknow', max_length=100),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='model',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='year',
            field=models.PositiveIntegerField(default=2020),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='vehicles/'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

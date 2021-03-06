# Generated by Django 3.2.6 on 2021-09-01 17:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210901_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=25, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=25, verbose_name='URL'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.6 on 2021-09-01 17:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210901_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='description',
            field=models.TextField(default=django.utils.timezone.now, max_length=100, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]